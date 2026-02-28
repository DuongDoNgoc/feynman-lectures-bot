---
status: completed
completed: 2026-02-28
---

# Phase 3: Backfill Existing Lessons

## Goal
Re-render the 9 approved lessons containing markdown tables so their `math_images_json` includes table blocks. No content changes.

## Why a Separate Script

`db.get_approved_lessons_needing_render()` checks `math_images_json IS NULL OR = '[]' OR = ''`. Since 8 of 9 target lessons already have formula blocks in `math_images_json`, they will NOT be picked up by `run_renderer()`. A targeted backfill script is needed.

## Approach: Full Re-render

Instead of surgically appending table blocks, **re-run `render_lesson_math()`** on each affected lesson. This:
- Picks up both formulas AND tables in a single pass (after Phase 2 changes)
- Produces correctly sorted block list
- Avoids merge logic bugs
- Formula PNGs are cached (no re-render cost)

## Script: `scripts/backfill-tables.py`

```python
"""Re-render lessons containing markdown tables to add table blocks."""
import asyncio
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils import load_config
from src.knowledge import db
from src.renderer.math_renderer import render_lesson_math


async def main():
    config = load_config()
    await db.init_db(config)

    output_dir = config["renderer"]["output_dir"]
    dpi = config["renderer"]["dpi"]

    # Find lessons with markdown tables
    async with db.get_db() as conn:
        rows = await conn.execute_fetchall(
            "SELECT id FROM lessons WHERE content_enhanced LIKE '%|---|%' AND approval_status = 'approved'"
        )
    lesson_ids = [r["id"] for r in rows]
    print(f"Found {len(lesson_ids)} lessons with tables: {lesson_ids}")

    for lid in lesson_ids:
        async with db.get_db() as conn:
            row = await conn.execute_fetchall("SELECT * FROM lessons WHERE id = ?", (lid,))
        if not row:
            continue
        lesson = db._row_to_lesson(row[0])

        loop = asyncio.get_event_loop()
        blocks = await loop.run_in_executor(None, render_lesson_math, lesson, output_dir, dpi)

        table_count = sum(1 for b in blocks if b["type"] == "table")
        formula_count = sum(1 for b in blocks if b["type"] != "table")

        lesson.math_images_json = json.dumps(blocks)
        await db.update_lesson_content(lesson)
        print(f"  L{lid}: {formula_count} formula blocks + {table_count} table blocks")

    print("Done.")


if __name__ == "__main__":
    asyncio.run(main())
```

## Execution

```bash
cd /mnt/d/Vibecoding/FeynmanLecture/feynman-bot
.venv/bin/python3.12 scripts/backfill-tables.py
```

## Verification

After backfill:
1. Check `math_images_json` for one lesson contains `"type": "table"` blocks
2. Check `tbl_*.png` files exist in `data/images/`
3. Send one lesson via `scripts/test-interleaved.py` to Telegram and verify table renders inline

```bash
# Quick DB check
.venv/bin/python3.12 -c "
import aiosqlite, asyncio, json
async def check():
    async with aiosqlite.connect('data/feynman.db') as conn:
        conn.row_factory = aiosqlite.Row
        rows = await conn.execute_fetchall(
            \"SELECT id, math_images_json FROM lessons WHERE id = 5305\"
        )
        blocks = json.loads(rows[0]['math_images_json'])
        tables = [b for b in blocks if b['type'] == 'table']
        print(f'L5305: {len(blocks)} total blocks, {len(tables)} table blocks')
        for t in tables:
            print(f'  {t}')
asyncio.run(check())
"
```

## Rollback

If something goes wrong, `math_images_json` can be reset to formula-only blocks by re-running `run_renderer()` (which will overwrite with formula-only blocks since the old code path didn't detect tables). However, after Phase 2 is merged, `run_renderer` will also include tables. To rollback fully, revert the Phase 2 code change first.

## Future: Automatic Handling

After Phase 2 is deployed, all new lessons processed by `run_renderer()` will automatically detect and render tables. No further backfill needed unless existing data changes.
