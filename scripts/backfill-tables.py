"""Re-render approved lessons containing markdown tables to add table blocks to math_images_json."""
import asyncio
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils import load_config
from src.knowledge import db
from src.renderer.math_renderer import render_lesson_math


async def main():
    config = load_config()
    await db.init_db(config)

    output_dir = config["renderer"]["output_dir"]
    dpi = config["renderer"]["dpi"]

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
