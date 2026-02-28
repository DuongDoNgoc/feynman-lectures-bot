---
title: "Phase 03: Render Approved Lessons Only"
phase: 3
status: completed
effort: 1h
---

# Phase 03: Gate Renderer to Approved Lessons Only

## Goal

`pipeline.py --stage render` should only render formulas for `approval_status = 'approved'` lessons.

## Current State

`math_renderer.py` renders all lessons with unrendered formulas, regardless of approval.

## Changes

### `src/renderer/math_renderer.py`

Change the query that fetches lessons to render:

```python
# BEFORE
lessons = await db.get_lessons_needing_render()

# AFTER
lessons = await db.get_approved_lessons_needing_render()
```

### `src/knowledge/db.py`

```python
async def get_approved_lessons_needing_render() -> list[Lesson]:
    """Approved lessons that have not been rendered yet."""
    async with get_db() as conn:
        rows = await conn.execute_fetchall("""
            SELECT * FROM lessons
            WHERE approval_status = 'approved'
            AND enhancement_status = 'completed'
            AND (math_images_json IS NULL OR math_images_json = '[]')
            ORDER BY sequence
        """)
        return [_row_to_lesson(r) for r in rows]
```

### `pipeline.py` (optional `--approved-only` flag)

```python
parser.add_argument("--approved-only", action="store_true",
                    help="Render only approved lessons")
```

Pass to renderer — though since approval gate is the new default, this flag may not be needed.

## Todo

- [ ] Add `get_approved_lessons_needing_render()` to `db.py`
- [ ] Update `run_renderer()` to use new query
- [ ] Verify renderer still skips already-rendered lessons (idempotent)
- [ ] Test: approve 1 lesson → render → check `math_images_json` populated

## Notes

- Existing `math_images_json` check ensures idempotency
- Rejected lessons are never rendered — saves compute
- If lesson later approved after rejection, render runs on next `--stage render` call
