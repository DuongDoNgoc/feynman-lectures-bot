#!/usr/bin/env python3
"""Download all Feynman Lectures images using Playwright (Cloudflare bypass).

Direct HTTP requests are blocked by Cloudflare. This script navigates each chapter
with a stealth browser to obtain valid session cookies, then fetches images via the
browser's fetch() API. Converts .svgz files to PNG for Telegram compatibility.

Usage:
    python scripts/download_images.py
    python scripts/download_images.py --chapter 1 --volume I
    python scripts/download_images.py --dry-run
"""
import argparse
import asyncio
import base64
import gzip
import logging
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from bs4 import BeautifulSoup
from playwright.async_api import Browser, Page, async_playwright

from src.knowledge import db

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger(__name__)

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".svgz", ".svg"}


def convert_svgz_to_png(svgz_path: str, png_path: str, dpi: int = 150) -> bool:
    """Convert a .svgz (or plain .svg) file to .png using cairosvg.

    Browsers often decompress SVGZ during transmission, so the downloaded file
    may be plain SVG XML despite the .svgz extension. Tries gzip first, falls
    back to treating as plain SVG.
    """
    try:
        import cairosvg
        with open(svgz_path, "rb") as f:
            raw = f.read()
        # Try gzip decompression first; fall back to plain SVG
        try:
            svg_data = gzip.decompress(raw)
        except Exception:
            svg_data = raw  # already plain SVG
        cairosvg.svg2png(bytestring=svg_data, write_to=png_path, dpi=dpi)
        return True
    except Exception as e:
        log.warning("SVG conversion failed %s: %s", svgz_path, e)
        return False


async def fetch_image_via_browser(page: Page, src: str) -> bytes | None:
    """Fetch an image src using the browser's fetch() (has Cloudflare cookies)."""
    try:
        data_b64 = await page.evaluate(
            """async (src) => {
                const resp = await fetch(src);
                if (!resp.ok) return null;
                const buf = await resp.arrayBuffer();
                const bytes = new Uint8Array(buf);
                let str = '';
                for (let i = 0; i < bytes.length; i++) str += String.fromCharCode(bytes[i]);
                return btoa(str);
            }""",
            src,
        )
        if data_b64:
            return base64.b64decode(data_b64)
    except Exception as e:
        log.debug("Browser fetch failed for %s: %s", src, e)
    return None


async def download_chapter_images(
    page: Page,
    chapter_url: str,
    raw_html: str,
    chapter_dir: str,
) -> tuple[int, int]:
    """Download images for one chapter. Returns (downloaded, converted)."""
    # Navigate to the chapter page to get Cloudflare session cookies
    try:
        await page.goto(chapter_url, wait_until="domcontentloaded", timeout=30_000)
    except Exception as e:
        log.warning("Failed to load %s: %s", chapter_url, e)
        return 0, 0

    soup = BeautifulSoup(raw_html, "html.parser")
    imgs = soup.find_all("img", src=True)
    figure_imgs = [img for img in imgs if Path(img["src"]).suffix.lower() in IMAGE_EXTS]

    os.makedirs(chapter_dir, exist_ok=True)
    downloaded = 0

    for img in figure_imgs:
        src = img["src"]
        filename = os.path.basename(src)
        if not filename:
            continue
        local_path = os.path.join(chapter_dir, filename)
        if os.path.exists(local_path):
            continue

        data = await fetch_image_via_browser(page, src)
        if data:
            with open(local_path, "wb") as f:
                f.write(data)
            downloaded += 1
            log.debug("  Saved %s (%d bytes)", filename, len(data))
        else:
            log.debug("  Failed to fetch %s", src)

    # Convert all SVGZ files (including pre-existing ones) to PNG
    converted = 0
    for fname in os.listdir(chapter_dir):
        if fname.endswith(".svgz"):
            svgz_path = os.path.join(chapter_dir, fname)
            png_path = svgz_path[:-5] + ".png"
            if not os.path.exists(png_path):
                if convert_svgz_to_png(svgz_path, png_path):
                    converted += 1

    return downloaded, converted


async def main(chapter_filter: int = 0, volume_filter: str = "", dry_run: bool = False):
    await db.init_db()
    chapters = await db.get_all_chapters()

    if volume_filter:
        chapters = [c for c in chapters if c.volume == volume_filter]
    if chapter_filter:
        chapters = [c for c in chapters if c.number == chapter_filter]

    chapters_with_html = [c for c in chapters if c.raw_html]
    log.info("Processing %d chapters (with raw_html)...", len(chapters_with_html))

    if dry_run:
        for chapter in chapters_with_html:
            soup = BeautifulSoup(chapter.raw_html, "html.parser")
            imgs = soup.find_all("img", src=True)
            fig = [img for img in imgs if Path(img["src"]).suffix.lower() in IMAGE_EXTS]
            log.info("[DRY RUN] %s_%02d: %d figure images", chapter.volume, chapter.number, len(fig))
        return

    total_downloaded = total_converted = 0

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            ),
            viewport={"width": 1280, "height": 800},
            locale="en-US",
        )
        # Apply playwright-stealth if available
        try:
            from playwright_stealth import stealth_async
            await stealth_async(context)
        except ImportError:
            pass

        page = await context.new_page()

        for chapter in chapters_with_html:
            chapter_dir = f"data/raw/images/{chapter.volume}_{chapter.number:02d}"
            log.info("Chapter %s_%02d → %s", chapter.volume, chapter.number, chapter_dir)

            downloaded, converted = await download_chapter_images(
                page, chapter.url, chapter.raw_html, chapter_dir
            )
            total_downloaded += downloaded
            total_converted += converted
            log.info("  → %d new images, %d SVGZ→PNG converted", downloaded, converted)

            await asyncio.sleep(1.0)  # polite delay between chapters

        await browser.close()

    log.info(
        "Done: %d images downloaded, %d SVGZ→PNG converted",
        total_downloaded, total_converted,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Download Feynman Lectures images via Playwright (Cloudflare bypass)"
    )
    parser.add_argument("--chapter", type=int, default=0, help="Process only this chapter number")
    parser.add_argument("--volume", default="", help="Process only this volume (I/II/III)")
    parser.add_argument("--dry-run", action="store_true", help="Preview only, no downloads")
    args = parser.parse_args()

    os.chdir(Path(__file__).parent.parent)
    asyncio.run(main(chapter_filter=args.chapter, volume_filter=args.volume, dry_run=args.dry_run))
