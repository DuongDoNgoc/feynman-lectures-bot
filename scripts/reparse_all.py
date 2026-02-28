"""Re-parse all chapters and re-chunk into lessons.

Use after fixing a parser bug that corrupted stored content.
Wipes sections + lessons (no user progress exists) and re-runs
the parse → chunk pipeline using existing raw HTML.

Usage:
    python scripts/reparse_all.py [--config config.yaml] [--dry-run]
"""
import argparse
import asyncio
import logging
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.knowledge.db import init_db, get_db
from src.crawler.parser import parse_chapter, _build_image_map
from src.knowledge import db
from src.utils import load_config, setup_logging

log = logging.getLogger(__name__)


async def wipe_and_reparse(config: dict, dry_run: bool = False):
    await init_db(config)

    async with get_db() as conn:
        # Count existing rows
        sec_count = (await conn.execute_fetchall("SELECT COUNT(*) AS n FROM sections"))[0]["n"]
        les_count = (await conn.execute_fetchall("SELECT COUNT(*) AS n FROM lessons"))[0]["n"]
        log.info("Existing: %d sections, %d lessons", sec_count, les_count)

        if dry_run:
            log.info("[DRY-RUN] Would wipe and re-parse %d chapters.", sec_count)
            return

        # Wipe derived tables (no user data present)
        await conn.execute("DELETE FROM lessons")
        await conn.execute("DELETE FROM sections")
        await conn.commit()
        log.info("Wiped sections + lessons.")

    # Re-run parse stage
    log.info("=== Re-parsing chapters ===")
    chapters = await _get_all_chapters()
    log.info("%d chapters to parse", len(chapters))

    total_sections = 0
    for chapter in chapters:
        chapter_dir = f"data/raw/images/{chapter['volume']}_{chapter['number']:02d}"
        image_map = _build_image_map(chapter["url"], chapter_dir)
        try:
            sections = parse_chapter(chapter["raw_html"], image_map)
            for section in sections:
                section.chapter_id = chapter["id"]
                await db.insert_section(chapter["id"], section)
            total_sections += len(sections)
            log.info("  Parsed Vol %s Ch %02d: %d sections", chapter["volume"], chapter["number"], len(sections))
        except Exception as e:
            log.error("  Failed to parse Vol %s Ch %02d: %s", chapter["volume"], chapter["number"], e)

    log.info("Parse complete: %d sections inserted.", total_sections)

    # Re-run chunk stage
    log.info("=== Re-chunking into lessons ===")
    from src.content.chunker import run_chunker
    await run_chunker(config)
    log.info("Reparse + rechunk complete.")


async def _get_all_chapters() -> list[dict]:
    async with get_db() as conn:
        rows = await conn.execute_fetchall(
            "SELECT id, volume, number, title, url, raw_html FROM chapters WHERE raw_html != ''"
        )
        return [dict(r) for r in rows]


def main():
    parser = argparse.ArgumentParser(description="Re-parse + re-chunk all chapters")
    parser.add_argument("--config", default="config.yaml")
    parser.add_argument("--dry-run", action="store_true", help="Show counts without making changes")
    args = parser.parse_args()

    config = load_config(args.config)
    setup_logging(config)
    asyncio.run(wipe_and_reparse(config, dry_run=args.dry_run))


if __name__ == "__main__":
    main()
