"""SQLite database layer using aiosqlite for async access."""
import json
import logging
from contextlib import asynccontextmanager
from typing import Optional

import aiosqlite

from src.knowledge.models import Chapter, Section, Lesson, UserProgress, ConversationMessage, ScheduledLesson

log = logging.getLogger(__name__)

_db_path: str = "data/feynman.db"


def set_db_path(path: str):
    global _db_path
    _db_path = path


@asynccontextmanager
async def get_db():
    """Async context manager for DB connection."""
    async with aiosqlite.connect(_db_path) as conn:
        conn.row_factory = aiosqlite.Row
        await conn.execute("PRAGMA journal_mode=WAL")
        await conn.execute("PRAGMA foreign_keys=ON")
        yield conn


async def init_db(config: Optional[dict] = None):
    """Create all tables and indexes. Idempotent."""
    if config:
        set_db_path(config["database"]["path"])

    async with get_db() as conn:
        await conn.executescript("""
            CREATE TABLE IF NOT EXISTS chapters (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                volume      TEXT NOT NULL,
                number      INTEGER NOT NULL,
                title       TEXT NOT NULL,
                url         TEXT NOT NULL UNIQUE,
                raw_html    TEXT DEFAULT '',
                crawled_at  TEXT DEFAULT NULL
            );
            CREATE UNIQUE INDEX IF NOT EXISTS idx_chapters_vol_num
                ON chapters(volume, number);

            CREATE TABLE IF NOT EXISTS sections (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                chapter_id      INTEGER NOT NULL REFERENCES chapters(id),
                number          INTEGER NOT NULL,
                title           TEXT NOT NULL,
                content_text    TEXT NOT NULL,
                latex_formulas  TEXT DEFAULT '[]',
                image_refs      TEXT DEFAULT '[]',
                parsed_at       TEXT DEFAULT NULL
            );
            CREATE INDEX IF NOT EXISTS idx_sections_chapter
                ON sections(chapter_id);

            CREATE TABLE IF NOT EXISTS lessons (
                id                  INTEGER PRIMARY KEY AUTOINCREMENT,
                section_id          INTEGER NOT NULL REFERENCES sections(id),
                lesson_type         TEXT NOT NULL,
                sequence            INTEGER NOT NULL DEFAULT 0,
                title               TEXT NOT NULL DEFAULT '',
                content_enhanced    TEXT NOT NULL DEFAULT '',
                examples_json       TEXT DEFAULT NULL,
                quiz_json           TEXT DEFAULT NULL,
                math_images_json    TEXT DEFAULT NULL,
                enhancement_status  TEXT NOT NULL DEFAULT 'pending',
                created_at          TEXT DEFAULT (datetime('now'))
            );
            CREATE INDEX IF NOT EXISTS idx_lessons_section
                ON lessons(section_id, lesson_type);
            CREATE INDEX IF NOT EXISTS idx_lessons_status
                ON lessons(enhancement_status);

            CREATE TABLE IF NOT EXISTS user_progress (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id     INTEGER NOT NULL,
                lesson_id   INTEGER NOT NULL REFERENCES lessons(id),
                sent_at     TEXT DEFAULT NULL,
                read_at     TEXT DEFAULT NULL,
                quiz_score  REAL DEFAULT NULL
            );
            CREATE UNIQUE INDEX IF NOT EXISTS idx_progress_user_lesson
                ON user_progress(user_id, lesson_id);

            CREATE TABLE IF NOT EXISTS conversation_history (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id     INTEGER NOT NULL,
                lesson_id   INTEGER NOT NULL,
                role        TEXT NOT NULL,
                message     TEXT NOT NULL,
                created_at  TEXT DEFAULT (datetime('now'))
            );
            CREATE INDEX IF NOT EXISTS idx_convo_user_lesson
                ON conversation_history(user_id, lesson_id);

            CREATE TABLE IF NOT EXISTS scheduled_lessons (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id         INTEGER NOT NULL,
                lesson_id       INTEGER NOT NULL REFERENCES lessons(id),
                lesson_type     TEXT NOT NULL,
                scheduled_time  TEXT NOT NULL,
                delivered       INTEGER NOT NULL DEFAULT 0,
                delivered_at    TEXT DEFAULT NULL
            );
            CREATE INDEX IF NOT EXISTS idx_scheduled_user
                ON scheduled_lessons(user_id, delivered);
        """)

        # Migration: Add approval_status column if not exists
        try:
            await conn.execute("ALTER TABLE lessons ADD COLUMN approval_status TEXT DEFAULT 'pending'")
            log.info("Added approval_status column to lessons table")
        except aiosqlite.OperationalError:
            pass  # Column already exists

        await conn.execute("""
            CREATE INDEX IF NOT EXISTS idx_lessons_approval
            ON lessons(approval_status)
        """)
        await conn.commit()
    log.info("Database initialized at %s", _db_path)


# ─── Chapters ───────────────────────────────────────────────────────────────

async def insert_chapter(chapter: Chapter) -> int:
    """Insert or update chapter. Returns row id."""
    async with get_db() as conn:
        cursor = await conn.execute(
            """INSERT INTO chapters (volume, number, title, url, raw_html, crawled_at)
               VALUES (?, ?, ?, ?, ?, datetime('now'))
               ON CONFLICT(url) DO UPDATE SET
                   raw_html   = excluded.raw_html,
                   crawled_at = excluded.crawled_at""",
            (chapter.volume, chapter.number, chapter.title, chapter.url, chapter.raw_html)
        )
        await conn.commit()
        return cursor.lastrowid


async def get_crawled_urls() -> set[str]:
    """Return URLs of already-crawled chapters (have raw_html)."""
    async with get_db() as conn:
        rows = await conn.execute_fetchall(
            "SELECT url FROM chapters WHERE raw_html != '' AND crawled_at IS NOT NULL"
        )
        return {r["url"] for r in rows}


async def get_unparsed_chapters() -> list[Chapter]:
    """Chapters crawled but not yet parsed (no sections)."""
    async with get_db() as conn:
        rows = await conn.execute_fetchall(
            """SELECT c.* FROM chapters c
               WHERE c.raw_html != ''
               AND NOT EXISTS (SELECT 1 FROM sections s WHERE s.chapter_id = c.id)"""
        )
        return [Chapter(id=r["id"], volume=r["volume"], number=r["number"],
                        title=r["title"], url=r["url"], raw_html=r["raw_html"],
                        crawled_at=r["crawled_at"]) for r in rows]


async def get_all_chapters() -> list[Chapter]:
    async with get_db() as conn:
        rows = await conn.execute_fetchall("SELECT * FROM chapters ORDER BY volume, number")
        return [Chapter(id=r["id"], volume=r["volume"], number=r["number"],
                        title=r["title"], url=r["url"], raw_html=r["raw_html"],
                        crawled_at=r["crawled_at"]) for r in rows]


# ─── Sections ────────────────────────────────────────────────────────────────

async def insert_section(chapter_id: int, section: Section) -> int:
    async with get_db() as conn:
        cursor = await conn.execute(
            """INSERT INTO sections
               (chapter_id, number, title, content_text, latex_formulas, image_refs, parsed_at)
               VALUES (?, ?, ?, ?, ?, ?, datetime('now'))""",
            (chapter_id, section.number, section.title, section.content_text,
             section.latex_formulas_json, section.image_refs_json)
        )
        await conn.commit()
        return cursor.lastrowid


async def get_all_sections() -> list[Section]:
    async with get_db() as conn:
        rows = await conn.execute_fetchall("""
            SELECT s.*, c.number AS chapter_number, c.title AS chapter_title
            FROM sections s
            JOIN chapters c ON s.chapter_id = c.id
            ORDER BY c.number, s.number
        """)
        return [_row_to_section(r, with_chapter=True) for r in rows]


async def get_sections_for_chapter(chapter_id: int) -> list[Section]:
    async with get_db() as conn:
        rows = await conn.execute_fetchall(
            "SELECT * FROM sections WHERE chapter_id = ? ORDER BY number", (chapter_id,)
        )
        return [_row_to_section(r) for r in rows]


def _row_to_section(r, with_chapter: bool = False) -> Section:
    s = Section(
        id=r["id"], chapter_id=r["chapter_id"], number=r["number"],
        title=r["title"], content_text=r["content_text"],
        latex_formulas=json.loads(r["latex_formulas"] or "[]"),
        image_refs=json.loads(r["image_refs"] or "[]"),
        parsed_at=r["parsed_at"],
    )
    if with_chapter:
        s.chapter_number = r["chapter_number"]
        s.chapter_title = r["chapter_title"]
    return s


# ─── Lessons ─────────────────────────────────────────────────────────────────

async def insert_lesson(lesson: Lesson) -> int:
    async with get_db() as conn:
        cursor = await conn.execute(
            """INSERT INTO lessons
               (section_id, lesson_type, sequence, title, content_enhanced,
                examples_json, quiz_json, math_images_json, enhancement_status)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (lesson.section_id, lesson.lesson_type, lesson.sequence, lesson.title,
             lesson.content_enhanced, lesson.examples_json, lesson.quiz_json,
             lesson.math_images_json, lesson.enhancement_status)
        )
        await conn.commit()
        return cursor.lastrowid


async def update_lesson_status(lesson_id: int, status: str):
    async with get_db() as conn:
        await conn.execute(
            "UPDATE lessons SET enhancement_status = ? WHERE id = ?", (status, lesson_id)
        )
        await conn.commit()


async def update_lesson_content(lesson: Lesson):
    async with get_db() as conn:
        await conn.execute(
            """UPDATE lessons SET
               title = ?, content_enhanced = ?, examples_json = ?,
               quiz_json = ?, math_images_json = ?, enhancement_status = 'completed'
               WHERE id = ?""",
            (lesson.title, lesson.content_enhanced, lesson.examples_json,
             lesson.quiz_json, lesson.math_images_json, lesson.id)
        )
        await conn.commit()


async def get_pending_lessons() -> list[Lesson]:
    """Lessons not yet enhanced."""
    async with get_db() as conn:
        rows = await conn.execute_fetchall(
            "SELECT * FROM lessons WHERE enhancement_status != 'completed' ORDER BY section_id, lesson_type"
        )
        return [_row_to_lesson(r) for r in rows]


async def get_next_lesson(user_id: int) -> Optional[Lesson]:
    """Next undelivered approved lesson for user (any type)."""
    async with get_db() as conn:
        rows = await conn.execute_fetchall(
            """SELECT l.* FROM lessons l
               WHERE l.enhancement_status = 'completed'
               AND l.approval_status = 'approved'
               AND NOT EXISTS (
                   SELECT 1 FROM user_progress p
                   WHERE p.user_id = ? AND p.lesson_id = l.id AND p.sent_at IS NOT NULL
               )
               ORDER BY l.sequence, l.lesson_type
               LIMIT 1""",
            (user_id,)
        )
        return _row_to_lesson(rows[0]) if rows else None


async def get_next_lesson_by_type(user_id: int, lesson_type: str) -> Optional[Lesson]:
    """Next undelivered approved lesson of specific type for user."""
    async with get_db() as conn:
        rows = await conn.execute_fetchall(
            """SELECT l.* FROM lessons l
               WHERE l.lesson_type = ? AND l.enhancement_status = 'completed'
               AND l.approval_status = 'approved'
               AND NOT EXISTS (
                   SELECT 1 FROM user_progress p
                   WHERE p.user_id = ? AND p.lesson_id = l.id AND p.sent_at IS NOT NULL
               )
               ORDER BY l.sequence
               LIMIT 1""",
            (lesson_type, user_id)
        )
        return _row_to_lesson(rows[0]) if rows else None


async def get_enhanced_pending_review() -> list[Lesson]:
    """Lessons enhanced but awaiting human approval."""
    async with get_db() as conn:
        rows = await conn.execute_fetchall(
            """SELECT * FROM lessons
               WHERE enhancement_status = 'completed'
               AND approval_status = 'pending'
               ORDER BY sequence, lesson_type"""
        )
        return [_row_to_lesson(r) for r in rows]


async def set_approval_status(lesson_id: int, status: str):
    """Set approval_status: 'approved' | 'rejected' | 'pending'."""
    async with get_db() as conn:
        await conn.execute(
            "UPDATE lessons SET approval_status = ? WHERE id = ?",
            (status, lesson_id)
        )
        await conn.commit()


async def get_approved_lessons_needing_render() -> list[Lesson]:
    """Approved lessons without rendered math images."""
    async with get_db() as conn:
        rows = await conn.execute_fetchall(
            """SELECT * FROM lessons
               WHERE approval_status = 'approved'
               AND enhancement_status = 'completed'
               AND (math_images_json IS NULL OR math_images_json = '[]' OR math_images_json = '')
               ORDER BY sequence"""
        )
        return [_row_to_lesson(r) for r in rows]


async def get_current_lesson(user_id: int) -> Optional[Lesson]:
    """Most recently sent lesson for user."""
    async with get_db() as conn:
        rows = await conn.execute_fetchall(
            """SELECT l.* FROM lessons l
               JOIN user_progress p ON p.lesson_id = l.id
               WHERE p.user_id = ? AND p.sent_at IS NOT NULL
               ORDER BY p.sent_at DESC
               LIMIT 1""",
            (user_id,)
        )
        return _row_to_lesson(rows[0]) if rows else None


async def get_lessons_delivered_this_week(user_id: int) -> list[Lesson]:
    """Lessons delivered Mon–Sat this week (for Thu/Sun review compilation)."""
    async with get_db() as conn:
        rows = await conn.execute_fetchall(
            """SELECT l.* FROM lessons l
               JOIN user_progress p ON p.lesson_id = l.id
               WHERE p.user_id = ?
               AND p.sent_at >= datetime('now', 'weekday 1', '-7 days')
               AND l.lesson_type != 'quiz'
               ORDER BY p.sent_at""",
            (user_id,)
        )
        return [_row_to_lesson(r) for r in rows]


def _row_to_lesson(r) -> Lesson:
    # Handle approval_status column (may not exist on older DBs)
    approval_status = "pending"
    try:
        approval_status = r["approval_status"] if r["approval_status"] else "pending"
    except (KeyError, IndexError):
        pass

    return Lesson(
        id=r["id"], section_id=r["section_id"], lesson_type=r["lesson_type"],
        sequence=r["sequence"], title=r["title"],
        content_enhanced=r["content_enhanced"],
        examples_json=r["examples_json"], quiz_json=r["quiz_json"],
        math_images_json=r["math_images_json"],
        enhancement_status=r["enhancement_status"], approval_status=approval_status,
        created_at=r["created_at"]
    )


# ─── User Progress ────────────────────────────────────────────────────────────

async def ensure_user(user_id: int):
    """No-op if user already tracked; creates first-touch record."""
    # user tracking is implicit via user_progress rows
    pass


async def mark_sent(user_id: int, lesson_id: int):
    async with get_db() as conn:
        await conn.execute(
            """INSERT INTO user_progress (user_id, lesson_id, sent_at)
               VALUES (?, ?, datetime('now'))
               ON CONFLICT(user_id, lesson_id) DO UPDATE SET sent_at = excluded.sent_at""",
            (user_id, lesson_id)
        )
        await conn.commit()


async def get_progress_stats(user_id: int) -> dict:
    async with get_db() as conn:
        total = (await conn.execute_fetchall(
            "SELECT COUNT(*) as n FROM lessons WHERE enhancement_status='completed'"
        ))[0]["n"]
        completed = (await conn.execute_fetchall(
            "SELECT COUNT(*) as n FROM user_progress WHERE user_id=? AND sent_at IS NOT NULL",
            (user_id,)
        ))[0]["n"]
        avg_score = (await conn.execute_fetchall(
            "SELECT AVG(quiz_score) as avg FROM user_progress WHERE user_id=? AND quiz_score IS NOT NULL",
            (user_id,)
        ))[0]["avg"] or 0

        # Current chapter from latest lesson
        chapter_rows = await conn.execute_fetchall(
            """SELECT c.title FROM lessons l
               JOIN sections s ON s.id = l.section_id
               JOIN chapters c ON c.id = s.chapter_id
               JOIN user_progress p ON p.lesson_id = l.id
               WHERE p.user_id = ? AND p.sent_at IS NOT NULL
               ORDER BY p.sent_at DESC LIMIT 1""",
            (user_id,)
        )
        current_chapter = chapter_rows[0]["title"] if chapter_rows else "N/A"

        # Streak: consecutive days with at least 1 lesson sent
        streak_rows = await conn.execute_fetchall(
            """SELECT DISTINCT date(sent_at) as d FROM user_progress
               WHERE user_id=? AND sent_at IS NOT NULL
               ORDER BY d DESC""",
            (user_id,)
        )
        streak = _calculate_streak([r["d"] for r in streak_rows])

        return {
            "total": total, "completed": completed,
            "current_chapter": current_chapter,
            "avg_score": round(avg_score, 1),
            "streak": streak
        }


def _calculate_streak(dates: list[str]) -> int:
    """Count consecutive days ending today or yesterday."""
    from datetime import date, timedelta
    if not dates:
        return 0
    streak = 0
    expected = date.today()
    for d_str in dates:
        d = date.fromisoformat(d_str)
        if d == expected or d == expected - timedelta(days=1) and streak == 0:
            streak += 1
            expected = d - timedelta(days=1)
        elif d == expected:
            streak += 1
            expected = d - timedelta(days=1)
        else:
            break
    return streak


# ─── Conversation History ─────────────────────────────────────────────────────

async def save_conversation(user_id: int, lesson_id: int, role: str, message: str):
    async with get_db() as conn:
        await conn.execute(
            "INSERT INTO conversation_history (user_id, lesson_id, role, message) VALUES (?, ?, ?, ?)",
            (user_id, lesson_id, role, message)
        )
        await conn.commit()


async def get_conversation_history(user_id: int, lesson_id: int, limit: int = 10) -> list[dict]:
    async with get_db() as conn:
        rows = await conn.execute_fetchall(
            """SELECT role, message FROM conversation_history
               WHERE user_id=? AND lesson_id=?
               ORDER BY created_at DESC LIMIT ?""",
            (user_id, lesson_id, limit)
        )
        # Return in chronological order for LLM context
        return [{"role": r["role"], "content": r["message"]} for r in reversed(rows)]


# ─── Scheduled Lessons ────────────────────────────────────────────────────────

async def insert_scheduled_record(user_id: int, lesson_id: int, lesson_type: str):
    async with get_db() as conn:
        await conn.execute(
            """INSERT INTO scheduled_lessons (user_id, lesson_id, lesson_type, scheduled_time, delivered, delivered_at)
               VALUES (?, ?, ?, datetime('now'), 1, datetime('now'))""",
            (user_id, lesson_id, lesson_type)
        )
        await conn.commit()


async def get_undelivered_scheduled(user_id: int) -> list[ScheduledLesson]:
    """Scheduled lessons not yet delivered (for catch-up on restart)."""
    async with get_db() as conn:
        rows = await conn.execute_fetchall(
            """SELECT * FROM scheduled_lessons
               WHERE user_id=? AND delivered=0 AND scheduled_time < datetime('now')
               ORDER BY scheduled_time""",
            (user_id,)
        )
        return [ScheduledLesson(id=r["id"], user_id=r["user_id"], lesson_id=r["lesson_id"],
                                lesson_type=r["lesson_type"], scheduled_time=r["scheduled_time"],
                                delivered=bool(r["delivered"]), delivered_at=r["delivered_at"])
                for r in rows]


async def mark_scheduled_delivered(scheduled_id: int):
    async with get_db() as conn:
        await conn.execute(
            "UPDATE scheduled_lessons SET delivered=1, delivered_at=datetime('now') WHERE id=?",
            (scheduled_id,)
        )
        await conn.commit()


async def save_quiz_score(user_id: int, lesson_id: int, score: float):
    async with get_db() as conn:
        await conn.execute(
            "UPDATE user_progress SET quiz_score=? WHERE user_id=? AND lesson_id=?",
            (score, user_id, lesson_id)
        )
        await conn.commit()
