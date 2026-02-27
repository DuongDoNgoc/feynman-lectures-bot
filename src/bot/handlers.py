"""Telegram command + message handlers.

Commands:
  /start    - welcome + first lesson preview
  /next     - fetch and deliver next unread lesson
  /quiz     - send quiz inline keyboard for current lesson
  /explain  - deeper explanation via DeepSeek
  /example  - role-specific practical example via DeepSeek
  /progress - completion stats + streak
  /schedule - view or update delivery times
  /role     - change user role (affects LLM prompts)
  /search   - search lessons by keyword

Text messages (non-command) → free-form Q&A via DeepSeek
"""
import hashlib
import json
import logging
import os
import re

from telegram import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputFile,
    Update,
)
from telegram.constants import ChatAction
from telegram.ext import ContextTypes

from src.knowledge import db
from src.knowledge.models import Lesson

log = logging.getLogger(__name__)

# Formula extraction patterns — must match math_renderer.py:155-159 exactly
# (cross-reference: src/renderer/math_renderer.py `render_lesson_math`)
FORMULA_PATTERNS = [
    (r"\$\$(.*?)\$\$", "$$"),
    (r"\\\[(.*?)\\\]", r"\["),
    (r"\$((?:[^$]|\\.)+?)\$", "$"),
    (r"\\\((.*?)\\\)", r"\("),
]

# Injected at bot startup (see bot.py)
_config: dict = {}
_qa_llm = None


def init_handlers(config: dict, qa_llm):
    global _config, _qa_llm
    _config = config
    _qa_llm = qa_llm


# ─── Prompts for interactive Q&A ─────────────────────────────────────────────

QA_SYSTEM_PROMPT = """Bạn là trợ lý học vật lý, hỗ trợ học viên hiểu bài giảng Feynman Lectures.
Học viên là {role}.
Trả lời bằng tiếng Việt, ngắn gọn (tối đa 300 từ), dùng thuật ngữ vật lý tiếng Anh khi cần.
Nếu câu hỏi nằm ngoài nội dung bài học, hãy nhắc nhẹ và hướng về chủ đề chính.

Nội dung bài học hiện tại:
{lesson_snippet}"""

EXPLAIN_SYSTEM_PROMPT = """Bạn là giảng viên vật lý chuyên giải thích sâu các khái niệm.
Học viên là {role}. Viết khoảng 400 từ, dùng tiếng Việt xen tiếng Anh."""

EXAMPLE_SYSTEM_PROMPT = """Bạn tạo ví dụ thực tế liên quan đến {role}.
Ví dụ phải cụ thể, áp dụng trực tiếp vào công việc của {role}.
Viết khoảng 300 từ, tiếng Việt."""


# ─── Utility ─────────────────────────────────────────────────────────────────

def split_message(text: str, max_len: int = 4096) -> list[str]:
    """Split long text at paragraph boundaries within Telegram's 4096-char limit."""
    if len(text) <= max_len:
        return [text]
    parts = []
    current = ""
    for paragraph in text.split("\n\n"):
        chunk = paragraph + "\n\n"
        if len(current) + len(chunk) > max_len:
            if current:
                parts.append(current.strip())
            # If a single paragraph is too long, split by newline
            if len(chunk) > max_len:
                for line in chunk.split("\n"):
                    if len(current) + len(line) + 1 > max_len:
                        parts.append(current.strip())
                        current = line + "\n"
                    else:
                        current += line + "\n"
            else:
                current = chunk
        else:
            current += chunk
    if current.strip():
        parts.append(current.strip())
    return parts


def _formula_hash(formula: str) -> str:
    """Same hash function as math_renderer._formula_hash."""
    return hashlib.md5(formula.encode()).hexdigest()[:12]


def _extract_formula_positions(content: str) -> list[dict]:
    """Find all formulas with their text positions, sorted by position.

    Deduplicates by formula text (first occurrence wins), matching renderer logic.
    Returns list of dicts with keys: start, end, formula, hash, full_match.
    """
    seen_formulas: set[str] = set()
    results = []

    for pattern, _ in FORMULA_PATTERNS:
        for m in re.finditer(pattern, content, re.DOTALL):
            formula = m.group(1).strip()
            if formula and len(formula) > 2 and formula not in seen_formulas:
                seen_formulas.add(formula)
                results.append({
                    "start": m.start(),
                    "end": m.end(),
                    "formula": formula,
                    "hash": _formula_hash(formula),
                    "full_match": m.group(0),
                })

    results.sort(key=lambda x: x["start"])
    return results


def _build_interleaved_segments(content: str, img_paths: list[str]) -> list[dict]:
    """Split content into ordered text/image segments.

    Args:
        content: lesson content_enhanced text
        img_paths: PNG file paths from math_images_json (only existing files)

    Returns:
        list of {"type": "text", "content": str} or {"type": "image", "path": str}
    """
    # Build hash → path lookup from available PNGs (filename is "{hash}.png")
    png_by_hash: dict[str, str] = {}
    for p in img_paths:
        basename = os.path.basename(p)
        h = os.path.splitext(basename)[0]
        png_by_hash[h] = p

    formulas = _extract_formula_positions(content)
    if not formulas:
        return [{"type": "text", "content": content}]

    segments = []
    cursor = 0

    for f in formulas:
        text_before = content[cursor:f["start"]]
        if text_before.strip():
            segments.append({"type": "text", "content": text_before})

        png_path = png_by_hash.get(f["hash"])
        if png_path:
            segments.append({"type": "image", "path": png_path})
        else:
            # No PNG available — keep formula text inline
            segments.append({"type": "text", "content": f["full_match"]})

        cursor = f["end"]

    text_after = content[cursor:]
    if text_after.strip():
        segments.append({"type": "text", "content": text_after})

    return segments


def _coalesce_segments(segments: list[dict], min_text_len: int = 200) -> list[dict]:
    """Merge consecutive text segments to reduce Telegram message count."""
    if not segments:
        return segments

    result = []
    text_buffer = ""

    for seg in segments:
        if seg["type"] == "text":
            text_buffer += seg["content"]
        else:
            if text_buffer.strip():
                result.append({"type": "text", "content": text_buffer})
                text_buffer = ""
            result.append(seg)

    if text_buffer.strip():
        result.append({"type": "text", "content": text_buffer})

    # Second pass: merge consecutive short text segments
    merged = []
    for seg in result:
        if (
            seg["type"] == "text"
            and merged
            and merged[-1]["type"] == "text"
            and len(merged[-1]["content"]) < min_text_len
        ):
            merged[-1]["content"] += seg["content"]
        else:
            merged.append(seg)

    return merged


async def send_lesson(update: Update, context: ContextTypes.DEFAULT_TYPE, lesson: Lesson):
    """Deliver lesson with text and formula images interleaved inline."""
    chat_id = update.effective_chat.id

    img_paths = []
    if lesson.math_images_json:
        img_paths = [p for p in json.loads(lesson.math_images_json) if os.path.exists(p)]

    segments = _coalesce_segments(_build_interleaved_segments(lesson.content_enhanced, img_paths))

    for seg in segments:
        if seg["type"] == "text":
            for part in split_message(seg["content"]):
                try:
                    await context.bot.send_message(chat_id, part, parse_mode="Markdown")
                except Exception:
                    await context.bot.send_message(chat_id, part)
        elif seg["type"] == "image":
            try:
                await context.bot.send_photo(
                    chat_id=chat_id,
                    photo=InputFile(open(seg["path"], "rb")),
                )
            except Exception as e:
                log.warning("Failed to send math image %s: %s", seg["path"], e)


async def send_quiz_questions(bot, chat_id: int, lesson: Lesson):
    """Send MCQ inline keyboard for quiz lesson."""
    if not lesson.quiz_json:
        await bot.send_message(chat_id, "Không có câu hỏi quiz cho bài này.")
        return
    try:
        quiz = json.loads(lesson.quiz_json)
    except (json.JSONDecodeError, TypeError):
        await bot.send_message(chat_id, "Lỗi đọc dữ liệu quiz.")
        return

    for q in quiz.get("questions", []):
        if q.get("type") == "mcq":
            keyboard = [
                [InlineKeyboardButton(opt, callback_data=f"quiz_{lesson.id}_{q['id']}_{i}")]
                for i, opt in enumerate(q.get("options", []))
            ]
            await bot.send_message(
                chat_id,
                q["question"],
                reply_markup=InlineKeyboardMarkup(keyboard),
            )
        else:  # open-ended
            await bot.send_message(chat_id, f"📝 {q['question']}")


# ─── Command handlers ─────────────────────────────────────────────────────────

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await db.ensure_user(chat_id)
    role = _config.get("user", {}).get("role", "engineer")
    await update.message.reply_text(
        f"👋 Chào mừng đến với <b>Feynman Lectures Bot</b>!\n\n"
        f"Vai trò của bạn: <code>{role}</code>\n\n"
        f"Bot sẽ gửi 3 bài học mỗi ngày:\n"
        f"  🌅 7:20 — Khái niệm (concept)\n"
        f"  ☀️ 12:15 — Chuyên sâu (deep dive)\n"
        f"  🌙 18:30 — Kiểm tra (quiz)\n\n"
        f"Lệnh:\n"
        f"/next — Bài tiếp theo\n"
        f"/quiz — Câu hỏi kiểm tra\n"
        f"/explain — Giải thích sâu hơn\n"
        f"/example — Ví dụ thực tế\n"
        f"/progress — Tiến độ học tập\n"
        f"/schedule — Xem lịch học\n"
        f"/help — Trợ giúp\n\n"
        f"Gõ bất kỳ câu hỏi nào về vật lý để hỏi AI! 🔬",
        parse_mode="HTML",
    )


async def next_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await context.bot.send_chat_action(chat_id, ChatAction.TYPING)

    lesson = await db.get_next_lesson(chat_id)
    if not lesson:
        await update.message.reply_text(
            "🎉 Bạn đã hoàn thành tất cả bài học hiện có!\n"
            "Hãy chờ thêm nội dung mới hoặc dùng /quiz để ôn tập."
        )
        return

    await send_lesson(update, context, lesson)
    await db.mark_sent(chat_id, lesson.id)
    await update.message.reply_text(
        f"✅ Bài học đã giao: <b>{lesson.title}</b>\n"
        f"Loại: {lesson.lesson_type} | Chuỗi #{lesson.sequence + 1}",
        parse_mode="HTML",
    )


async def quiz_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    lesson = await db.get_current_lesson(chat_id)
    if not lesson:
        await update.message.reply_text("Bạn chưa có bài học nào. Dùng /next để bắt đầu.")
        return
    # Get quiz lesson for current sequence
    quiz_lesson = await db.get_next_lesson_by_type(chat_id, "quiz")
    if not quiz_lesson:
        await update.message.reply_text("Không tìm thấy bài quiz. Hãy hoàn thành thêm bài học.")
        return
    await send_quiz_questions(context.bot, chat_id, quiz_lesson)


async def quiz_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle inline quiz answer button tap."""
    query: CallbackQuery = update.callback_query
    await query.answer()

    parts = query.data.split("_")  # quiz_{lesson_id}_{q_id}_{answer_idx}
    if len(parts) < 4:
        return
    _, lesson_id_str, q_id, answer_idx_str = parts[:4]

    lesson = None
    try:
        lesson_id = int(lesson_id_str)
        answer_idx = int(answer_idx_str)
    except ValueError:
        return

    # Fetch quiz from DB
    from src.knowledge.db import get_db
    async with get_db() as conn:
        rows = await conn.execute_fetchall(
            "SELECT quiz_json FROM lessons WHERE id=?", (lesson_id,)
        )
    if not rows or not rows[0]["quiz_json"]:
        return

    try:
        quiz = json.loads(rows[0]["quiz_json"])
    except json.JSONDecodeError:
        return

    # Find the question
    for q in quiz.get("questions", []):
        if q.get("id") == q_id and q.get("type") == "mcq":
            correct_letter = q.get("answer", "A")
            options = q.get("options", [])
            correct_idx = "ABCD".index(correct_letter) if correct_letter in "ABCD" else 0
            is_correct = answer_idx == correct_idx
            explanation = q.get("explanation", "")

            selected_opt = options[answer_idx] if answer_idx < len(options) else "?"
            result_text = (
                f"{'✅ Đúng!' if is_correct else '❌ Sai!'}\n\n"
                f"Bạn chọn: {selected_opt}\n"
                f"Đáp án đúng: {options[correct_idx] if correct_idx < len(options) else correct_letter}\n\n"
                f"💡 {explanation}"
            )
            await query.edit_message_text(result_text)

            # Record quiz score
            chat_id = update.effective_chat.id
            await db.save_quiz_score(chat_id, lesson_id, 100.0 if is_correct else 0.0)
            break


async def explain_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await context.bot.send_chat_action(chat_id, ChatAction.TYPING)

    lesson = await db.get_current_lesson(chat_id)
    if not lesson:
        await update.message.reply_text("Chưa có bài học hiện tại. Dùng /next để bắt đầu.")
        return

    topic = " ".join(context.args) if context.args else "khái niệm chính"
    role = _config.get("user", {}).get("role", "engineer")

    response = await _qa_llm.generate(
        system_prompt=EXPLAIN_SYSTEM_PROMPT.format(role=role),
        user_prompt=f"Giải thích chi tiết về '{topic}' từ bài học này:\n\n{lesson.content_enhanced[:2000]}",
    )
    for part in split_message(response):
        await update.message.reply_text(part)


async def example_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await context.bot.send_chat_action(chat_id, ChatAction.TYPING)

    lesson = await db.get_current_lesson(chat_id)
    if not lesson:
        await update.message.reply_text("Chưa có bài học hiện tại. Dùng /next để bắt đầu.")
        return

    role = _config.get("user", {}).get("role", "engineer")
    response = await _qa_llm.generate(
        system_prompt=EXAMPLE_SYSTEM_PROMPT.format(role=role),
        user_prompt=f"Tạo ví dụ thực tế cho {role} từ nội dung:\n\n{lesson.content_enhanced[:2000]}",
    )
    for part in split_message(response):
        await update.message.reply_text(part)


async def progress_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    stats = await db.get_progress_stats(chat_id)
    pct = round(stats["completed"] / max(stats["total"], 1) * 100, 1)
    await update.message.reply_text(
        f"📊 <b>Tiến độ học tập</b>\n\n"
        f"✅ Đã hoàn thành: {stats['completed']}/{stats['total']} ({pct}%)\n"
        f"📖 Chương hiện tại: {stats['current_chapter']}\n"
        f"🎯 Điểm quiz TB: {stats['avg_score']}%\n"
        f"🔥 Streak: {stats['streak']} ngày",
        parse_mode="HTML",
    )


async def schedule_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        # Show current schedule
        tz = _config.get("schedule", {}).get("timezone", "Asia/Bangkok")
        times = _config.get("schedule", {}).get("times", [])
        types = _config.get("schedule", {}).get("lesson_types", [])
        review_days = _config.get("schedule", {}).get("review_days", [])
        lines = [f"🕐 <b>Lịch học hiện tại</b> ({tz})\n"]
        for t, lt in zip(times, types):
            lines.append(f"  {t} → {lt}")
        lines.append(f"\n📅 Ngày ôn tập: {', '.join(review_days)}")
        lines.append(f"\nĐể thay đổi: /schedule 08:00 13:00 19:00")
        await update.message.reply_text("\n".join(lines), parse_mode="HTML")
    else:
        # Update times
        if len(context.args) < 3:
            await update.message.reply_text("Cần 3 thời gian: /schedule HH:MM HH:MM HH:MM")
            return
        new_times = context.args[:3]
        _config["schedule"]["times"] = new_times
        # Re-setup scheduler
        from src.bot.scheduler import setup_schedule
        for job in context.application.job_queue.jobs():
            if job.name and job.name.startswith("lesson_"):
                job.schedule_removal()
        setup_schedule(context.application, _config)
        await update.message.reply_text(
            f"✅ Đã cập nhật lịch: {', '.join(new_times)}"
        )


async def role_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        current = _config.get("user", {}).get("role", "engineer")
        await update.message.reply_text(
            f"Vai trò hiện tại: <code>{current}</code>\n\n"
            f"Để thay đổi: /role mechatronics engineer",
            parse_mode="HTML",
        )
        return
    new_role = " ".join(context.args)
    _config["user"]["role"] = new_role
    await update.message.reply_text(f"✅ Đã cập nhật vai trò: <code>{new_role}</code>", parse_mode="HTML")


async def search_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Dùng: /search từ_khóa")
        return
    keyword = " ".join(context.args).lower()

    from src.knowledge.db import get_db
    async with get_db() as conn:
        rows = await conn.execute_fetchall(
            """SELECT id, title, lesson_type, sequence FROM lessons
               WHERE enhancement_status='completed'
               AND (LOWER(title) LIKE ? OR LOWER(content_enhanced) LIKE ?)
               LIMIT 5""",
            (f"%{keyword}%", f"%{keyword}%"),
        )

    if not rows:
        await update.message.reply_text(f"Không tìm thấy bài học nào với từ khóa: '{keyword}'")
        return

    lines = [f"🔍 Kết quả tìm kiếm '{keyword}':\n"]
    for r in rows:
        lines.append(f"  #{r['id']} [{r['lesson_type']}] {r['title']}")
    await update.message.reply_text("\n".join(lines))


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Free-form Q&A via DeepSeek with conversation history."""
    chat_id = update.effective_chat.id
    user_text = update.message.text

    await context.bot.send_chat_action(chat_id, ChatAction.TYPING)

    lesson = await db.get_current_lesson(chat_id)
    lesson_snippet = lesson.content_enhanced[:1500] if lesson else "Chưa có bài học"
    lesson_id = lesson.id if lesson else 0

    history = await db.get_conversation_history(chat_id, lesson_id,
                                                 limit=_config.get("qa", {}).get("history_limit", 10))
    role = _config.get("user", {}).get("role", "engineer")

    try:
        response = await _qa_llm.generate(
            system_prompt=QA_SYSTEM_PROMPT.format(role=role, lesson_snippet=lesson_snippet),
            user_prompt=user_text,
            history=history,
        )
    except Exception as e:
        log.error("Q&A LLM error: %s", e)
        await update.message.reply_text("⚠️ Xin lỗi, có lỗi xảy ra. Vui lòng thử lại sau.")
        return

    for part in split_message(response):
        await update.message.reply_text(part)

    # Persist conversation
    await db.save_conversation(chat_id, lesson_id, "user", user_text)
    await db.save_conversation(chat_id, lesson_id, "assistant", response)


async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "<b>Feynman Lectures Bot — Trợ giúp</b>\n\n"
        "/start — Khởi động bot\n"
        "/next — Bài học tiếp theo\n"
        "/quiz — Câu hỏi kiểm tra\n"
        "/explain [chủ đề] — Giải thích sâu\n"
        "/example — Ví dụ thực tế\n"
        "/progress — Tiến độ học tập\n"
        "/schedule [h:m h:m h:m] — Xem/đặt lịch\n"
        "/role [mô tả] — Thay đổi vai trò\n"
        "/search [từ khóa] — Tìm kiếm bài học\n\n"
        "💬 Gõ bất kỳ câu hỏi → AI trả lời dựa trên bài học hiện tại",
        parse_mode="HTML",
    )


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    log.error("Unhandled exception", exc_info=context.error)
    if isinstance(update, Update) and update.effective_message:
        await update.effective_message.reply_text(
            "⚠️ Có lỗi xảy ra. Vui lòng thử lại hoặc dùng /start để khởi động lại."
        )
