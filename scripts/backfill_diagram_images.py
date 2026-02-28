#!/usr/bin/env python3
"""Backfill diagram_images_json for existing lessons from sections.image_refs.

Resolves web-relative image_refs (e.g. "img/FLP_I/f01-01/f01-01_tc_big.svgz")
to local PNG paths (e.g. "data/raw/images/I_01/f01-01_tc_big.png").

Run AFTER scripts/download_images.py to ensure local files exist.

Usage:
    python scripts/backfill_diagram_images.py
    python scripts/backfill_diagram_images.py --dry-run
"""
import argparse
import asyncio
import json
import logging
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import aiosqlite

from src.knowledge import db

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger(__name__)


def resolve_local_path(image_ref: str, volume: str, chapter_num: int) -> str:
    """Map a web-relative image src to local filesystem path.

    Example:
        "img/FLP_I/f01-01/f01-01_tc_big.svgz" -> "data/raw/images/I_01/f01-01_tc_big.png"
        "img/FLP_I/f01-00/f01-00.jpg"          -> "data/raw/images/I_01/f01-00.jpg"
    """
    filename = os.path.basename(image_ref)
    chapter_dir = f"data/raw/images/{volume}_{chapter_num:02d}"
    stem = Path(filename).stem
    ext = Path(filename).suffix.lower()

    if ext == ".svgz":
        return os.path.join(chapter_dir, stem + ".png")
    return os.path.join(chapter_dir, filename)


async def main(dry_run: bool = False):
    await db.init_db()

    async with aiosqlite.connect("data/feynman.db") as conn:
        conn.row_factory = aiosqlite.Row

        # Fetch all sections with image_refs, plus chapter info
        rows = await conn.execute_fetchall("""
            SELECT s.id AS section_id, s.image_refs, c.volume, c.number AS chapter_num
            FROM sections s
            JOIN chapters c ON c.id = s.chapter_id
            WHERE s.image_refs IS NOT NULL AND s.image_refs != '[]'
        """)

        log.info("Found %d sections with image_refs", len(rows))

        # Build {section_id: [local_png_path, ...]} map
        section_paths: dict[int, list[str]] = {}
        for row in rows:
            refs = json.loads(row["image_refs"])
            local_paths = [
                resolve_local_path(ref, row["volume"], row["chapter_num"])
                for ref in refs
            ]
            # Only keep paths that actually exist on disk
            existing = [p for p in local_paths if os.path.exists(p)]
            if existing:
                section_paths[row["section_id"]] = existing

        log.info(
            "%d sections have locally available images (of %d with refs)",
            len(section_paths), len(rows),
        )

        # Fetch all lessons that need backfill
        lessons = await conn.execute_fetchall("""
            SELECT id, section_id, diagram_images_json FROM lessons
            WHERE diagram_images_json IS NULL OR diagram_images_json = ''
        """)

        updated = skipped = 0
        for lesson in lessons:
            lesson_id = lesson["id"]
            section_id = lesson["section_id"]
            paths = section_paths.get(section_id, [])

            if not paths:
                skipped += 1
                continue

            diagram_json = json.dumps(paths)
            log.debug("Lesson %d → %d images: %s", lesson_id, len(paths), paths[:2])

            if not dry_run:
                await db.update_lesson_diagram_images(lesson_id, diagram_json)
            updated += 1

        if dry_run:
            log.info("[DRY RUN] Would update %d lessons, skip %d (no images)", updated, skipped)
        else:
            log.info("Backfill complete: %d lessons updated, %d skipped (no images)", updated, skipped)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Backfill diagram_images_json for existing lessons")
    parser.add_argument("--dry-run", action="store_true", help="Preview only, no DB writes")
    args = parser.parse_args()

    os.chdir(Path(__file__).parent.parent)
    asyncio.run(main(dry_run=args.dry_run))
