# Phase 1: Database Layer

## Overview

**Priority:** P1 (highest - foundation for other phases)
**Status:** Pending
**Effort:** 1h
**File:** `src/knowledge/preview_db.py`

Add database functions for querying completed lessons with full context and managing approval status.

---

## Context Links

- Related: `src/knowledge/db.py` (existing DB layer)
- Related: `src/knowledge/models.py` (data models)
- Related: `docs/system-architecture.md` (schema reference)

---

## Requirements

### Functional

- FR1.1: Query all completed lessons (`enhancement_status='completed'`)
- FR1.2: Query lessons by type (concept, deep_dive, quiz)
- FR1.3: Get lesson with chapter/section context (join query)
- FR1.4: Update approval status (pending/approved/rejected)
- FR1.5: Get lessons by approval status

### Non-Functional

- NFR1.1: Async operations using aiosqlite
- NFR1.2: Parameterized queries (no SQL injection)
- NFR1.3: Type hints on all functions
- NFR1.4: Google-style docstrings

---

## Architecture

### Database Migration

Add column to `lessons` table:

```sql
ALTER TABLE lessons ADD COLUMN approval_status TEXT DEFAULT 'pending';
CREATE INDEX IF NOT EXISTS idx_lessons_approval ON lessons(approval_status);
```

**Status values:**
- `pending` - exported but not reviewed
- `approved` - ready for Telegram delivery
- `rejected` - needs re-enhancement

### New Functions

```
preview_db.py
├── get_completed_lessons() -> list[Lesson]
├── get_completed_lessons_by_type(lesson_type: str) -> list[Lesson]
├── get_lesson_with_context(lesson_id: int) -> dict
├── get_lessons_by_approval_status(status: str) -> list[Lesson]
├── update_approval_status(lesson_id: int, status: str) -> None
└── run_migration() -> None
```

---

## Related Code Files

### Files to Create

| File | Purpose |
|------|---------|
| `src/knowledge/preview_db.py` | New preview-specific DB functions |

### Files to Modify

| File | Changes |
|------|---------|
| `src/knowledge/models.py` | Add `approval_status` field to Lesson dataclass |
| `src/knowledge/db.py` | Add migration in `init_db()` |

---

## Implementation Steps

### Step 1: Update Lesson Model

**File:** `src/knowledge/models.py`

Add field to Lesson dataclass:

```python
@dataclass
class Lesson:
    # ... existing fields ...
    approval_status: str = "pending"  # pending | approved | rejected
```

### Step 2: Add Migration to init_db

**File:** `src/knowledge/db.py`

In `init_db()` function, after existing table creation:

```python
# Migration: Add approval_status column if not exists
try:
    await conn.execute("ALTER TABLE lessons ADD COLUMN approval_status TEXT DEFAULT 'pending'")
except aiosqlite.OperationalError:
    pass  # Column already exists

await conn.execute("""
    CREATE INDEX IF NOT EXISTS idx_lessons_approval
    ON lessons(approval_status)
""")
```

Update `_row_to_lesson()` to include new field:

```python
def _row_to_lesson(r) -> Lesson:
    return Lesson(
        # ... existing fields ...
        approval_status=r["approval_status"] if "approval_status" in r.keys() else "pending"
    )
```

### Step 3: Create preview_db.py

**File:** `src/knowledge/preview_db.py`

```python
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
        lesson_row = await conn.execute_fetchone(
            "SELECT * FROM lessons WHERE id = ?", (lesson_id,)
        )
        if not lesson_row:
            return None

        lesson = _row_to_lesson(lesson_row)

        # Get section
        section_row = await conn.execute_fetchone(
            "SELECT * FROM sections WHERE id = ?", (lesson.section_id,)
        )
        section = _row_to_section(section_row) if section_row else None

        # Get chapter
        chapter_row = None
        if section:
            chapter_row = await conn.execute_fetchone(
                "SELECT * FROM chapters WHERE id = ?", (section.chapter_id,)
            )

        return {
            "lesson": lesson,
            "section": section,
            "chapter": dict(chapter_row) if chapter_row else None
        }


async def get_lessons_by_approval_status(status: str) -> list[Lesson]:
    """Fetch lessons by approval status.

    Args:
        status: One of 'pending', 'approved', 'rejected'
    """
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
```

---

## Todo List

- [ ] Add `approval_status` field to Lesson dataclass
- [ ] Add migration in `init_db()` function
- [ ] Update `_row_to_lesson()` to handle new field
- [ ] Create `src/knowledge/preview_db.py`
- [ ] Implement `get_completed_lessons()`
- [ ] Implement `get_completed_lessons_by_type()`
- [ ] Implement `get_lesson_with_context()`
- [ ] Implement `get_lessons_by_approval_status()`
- [ ] Implement `update_approval_status()`
- [ ] Add `__init__.py` exports

---

## Success Criteria

- [ ] All functions have type hints and docstrings
- [ ] Migration runs without error on existing DB
- [ ] `get_completed_lessons()` returns lessons with `enhancement_status='completed'`
- [ ] `get_lesson_with_context()` includes chapter/section data
- [ ] `update_approval_status()` persists changes to DB

---

## Security Considerations

- Parameterized queries prevent SQL injection
- Status values validated against allowlist
- No sensitive data exposed

---

## Next Steps

After completion:
1. Test migration on copy of production DB
2. Proceed to Phase 2: Markdown Exporter
