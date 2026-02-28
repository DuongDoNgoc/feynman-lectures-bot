"""Database functions for lesson preview workflow."""
import logging
from typing import Optional

import aiosqlite

from src.knowledge.db import get_db, _row_to_lesson, _row_to_section
from src.knowledge.models import Lesson

log = logging.getLogger(__name__)


async def get_completed_lessons() -> list[Lesson]:
    """Fetch all lessons with enhancement_status='completed'."""
    async with get_db() as conn:
        rows = await conn.execute_fetchall(
            """SELECT * FROM lessons
               WHERE enhancement_status = 'completed'
               ORDER BY sequence, lesson_type"""
        )
        return [_row_to_lesson(r) for r in rows]


async def get_completed_lessons_by_type(lesson_type: str) -> list[Lesson]:
    """Fetch completed lessons of specific type.

    Args:
        lesson_type: One of 'concept', 'deep_dive', 'quiz'
    """
    async with get_db() as conn:
        rows = await conn.execute_fetchall(
            """SELECT * FROM lessons
               WHERE enhancement_status = 'completed' AND lesson_type = ?
               ORDER BY sequence""",
            (lesson_type,)
        )
        return [_row_to_lesson(r) for r in rows]


async def get_lesson_with_context(lesson_id: int) -> Optional[dict]:
    """Fetch lesson with chapter and section context.

    Returns:
        Dict with keys: lesson, section, chapter
        None if lesson not found
    """
    async with get_db() as conn:
        # Get lesson
        lesson_rows = await conn.execute_fetchall(
            "SELECT * FROM lessons WHERE id = ?", (lesson_id,)
        )
        if not lesson_rows:
            return None

        lesson = _row_to_lesson(lesson_rows[0])

        # Get section
        section_rows = await conn.execute_fetchall(
            "SELECT * FROM sections WHERE id = ?", (lesson.section_id,)
        )
        section = _row_to_section(section_rows[0]) if section_rows else None

        # Get chapter
        chapter_row = None
        if section:
            chapter_rows = await conn.execute_fetchall(
                "SELECT * FROM chapters WHERE id = ?", (section.chapter_id,)
            )
            chapter_row = chapter_rows[0] if chapter_rows else None

        return {
            "lesson": lesson,
            "section": section,
            "chapter": dict(chapter_row) if chapter_row else None
        }


async def get_lessons_by_approval_status(status: str) -> list[Lesson]:
    """Fetch lessons by approval status.

    Args:
        status: One of 'pending', 'approved', 'rejected'

    Raises:
        ValueError: If status is invalid
    """
    valid_statuses = ("pending", "approved", "rejected")
    if status not in valid_statuses:
        raise ValueError(f"Invalid status: {status}. Must be one of {valid_statuses}")

    async with get_db() as conn:
        rows = await conn.execute_fetchall(
            """SELECT * FROM lessons
               WHERE approval_status = ? AND enhancement_status = 'completed'
               ORDER BY sequence""",
            (status,)
        )
        return [_row_to_lesson(r) for r in rows]


async def update_approval_status(lesson_id: int, status: str) -> bool:
    """Update approval status for a lesson.

    Args:
        lesson_id: Lesson ID
        status: One of 'pending', 'approved', 'rejected'

    Returns:
        True if updated, False if lesson not found
    """
    valid_statuses = ("pending", "approved", "rejected")
    if status not in valid_statuses:
        raise ValueError(f"Invalid status: {status}. Must be one of {valid_statuses}")

    async with get_db() as conn:
        cursor = await conn.execute(
            "UPDATE lessons SET approval_status = ? WHERE id = ?",
            (status, lesson_id)
        )
        await conn.commit()
        return cursor.rowcount > 0


async def bulk_update_approval_status(status: str, lesson_ids: Optional[list[int]] = None) -> int:
    """Bulk update approval status for multiple lessons.

    Args:
        status: One of 'pending', 'approved', 'rejected'
        lesson_ids: Optional list of lesson IDs. If None, updates all pending lessons.

    Returns:
        Number of lessons updated
    """
    valid_statuses = ("pending", "approved", "rejected")
    if status not in valid_statuses:
        raise ValueError(f"Invalid status: {status}. Must be one of {valid_statuses}")

    async with get_db() as conn:
        if lesson_ids:
            placeholders = ",".join("?" * len(lesson_ids))
            cursor = await conn.execute(
                f"UPDATE lessons SET approval_status = ? WHERE id IN ({placeholders})",
                (status, *lesson_ids)
            )
        else:
            # Update all pending lessons
            cursor = await conn.execute(
                "UPDATE lessons SET approval_status = ? WHERE approval_status = 'pending' AND enhancement_status = 'completed'",
                (status,)
            )
        await conn.commit()
        return cursor.rowcount
