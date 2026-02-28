---
title: "Phase 02: CLI Review Tool"
phase: 2
status: completed
effort: 1.5h
---

# Phase 02: CLI Review Tool — Approve/Reject Lessons

## Goal

Interactive terminal tool to review enhanced lessons and approve/reject.

## New File: `review.py`

```python
"""CLI tool for reviewing and approving enhanced lessons.

Usage:
  python review.py list                    # list lessons pending review
  python review.py show <lesson_id>        # print lesson content
  python review.py approve <lesson_id>     # approve single lesson
  python review.py reject <lesson_id>      # reject single lesson
  python review.py approve-batch           # interactive: show each, approve/reject/skip
"""
```

## Commands

### `list`
```
ID   | Type       | Title                                    | Status
-----|------------|------------------------------------------|--------
 42  | concept    | Ch1-2: 1–1Introduction                   | completed/pending
 43  | deep_dive  | Ch1-2: 1–1Introduction — Phân tích...    | completed/pending
```

### `approve-batch` (main workflow)
Loops through all `enhancement_status=completed, approval_status=pending`:
```
══════════════════════════════════════════
Lesson 42 — concept (Ch1-2: 1–1Introduction)
══════════════════════════════════════════
[content preview — first 500 chars]
...
[a]pprove  [r]eject  [s]kip  [v]iew full  [q]uit
>
```

## DB Changes (`src/knowledge/db.py`)

```python
async def get_enhanced_pending_review() -> list[Lesson]:
    """Lessons enhanced but not yet reviewed."""
    async with get_db() as conn:
        rows = await conn.execute_fetchall("""
            SELECT * FROM lessons
            WHERE enhancement_status = 'completed'
            AND approval_status = 'pending'
            ORDER BY sequence
        """)
        return [_row_to_lesson(r) for r in rows]

async def set_approval_status(lesson_id: int, status: str):
    """Set approval_status: 'approved' | 'rejected'."""
    async with get_db() as conn:
        await conn.execute(
            "UPDATE lessons SET approval_status=? WHERE id=?",
            (status, lesson_id)
        )
        await conn.commit()
```

## Todo

- [ ] Create `review.py` with argparse CLI
- [ ] Add `get_enhanced_pending_review()` to `db.py`
- [ ] Add `set_approval_status()` to `db.py`
- [ ] `approve-batch`: show title + first 400 chars, inline keys a/r/s/v/q
- [ ] `v` (view full): pipe to `less` or print full content
- [ ] Summary at end: "Approved: 8, Rejected: 1, Skipped: 1"

## Notes

- Keep review.py simple — single file, no new deps
- Use `input()` for interactive prompts (not curses)
- Show lesson_type (concept/deep_dive/quiz) clearly — quiz has different format
