---
title: "Phase 04: Bot Delivery Gate — Approved Only"
phase: 4
status: pending
effort: 1h
---

# Phase 04: Bot Delivers Approved Lessons Only

## Goal

Bot (`/next`, scheduler) only delivers lessons with `approval_status = 'approved'`.

## Current State

Bot queries lessons without approval filter — would deliver raw unapproved content.

## Find Delivery Queries

```bash
grep -n "get_next_lesson\|get_lesson\|SELECT.*lessons" src/bot/handlers.py src/bot/scheduler.py
```

## Changes

### `src/knowledge/db.py`

Gate the lesson delivery query:

```python
async def get_next_lesson_for_user(user_id: int) -> Optional[Lesson]:
    """Get next undelivered approved lesson for user."""
    async with get_db() as conn:
        rows = await conn.execute_fetchall("""
            SELECT l.* FROM lessons l
            LEFT JOIN user_progress up
                ON up.lesson_id = l.id AND up.user_id = ?
            WHERE l.approval_status = 'approved'
            AND l.enhancement_status = 'completed'
            AND up.id IS NULL
            ORDER BY l.sequence
            LIMIT 1
        """, (user_id,))
        return _row_to_lesson(rows[0]) if rows else None
```

### `src/bot/handlers.py` / `scheduler.py`

Replace any direct lesson query with `get_next_lesson_for_user()`.

### Status Command (`/status`)

Add approval stats to bot status:
```
📚 Feynman Bot Status
Approved lessons: 10/843
Your progress: 3/10 lessons
```

## Todo

- [ ] Audit all lesson-fetch queries in `handlers.py` + `scheduler.py`
- [ ] Add `approval_status = 'approved'` filter to all delivery queries
- [ ] Update `/status` command to show approved count
- [ ] Test: with 0 approved → bot replies "No lessons available yet"
- [ ] Test: approve 3 lessons → bot delivers correctly

## Notes

- Gate applies to both manual `/next` and scheduled delivery
- If no approved lessons exist, bot should reply gracefully (not error)
- Admin commands (if any) may bypass gate — review separately
