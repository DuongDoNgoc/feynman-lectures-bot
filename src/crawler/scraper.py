"""Playwright stealth crawler for feynmanlectures.caltech.edu.

Features:
- Multi-layer stealth (playwright-stealth + webdriver override + random UA)
- networkidle wait for MathJax rendering
- Daily crawl limit (~10 pages) + circuit breaker (20 consecutive failures)
- Exponential backoff retry (3 attempts)
- Resume support: skips already-crawled chapters
- Image download (SVG + PNG) to filesystem
"""
import asyncio
import logging
import os
import random
import re
import urllib.parse
from contextlib import asynccontextmanager
from typing import AsyncGenerator

import aiohttp
from bs4 import BeautifulSoup
from playwright.async_api import Browser, BrowserContext, Page, async_playwright

from src.knowledge import db
from src.knowledge.models import Chapter

log = logging.getLogger(__name__)

TOC_URLS = {
    "I":  "https://www.feynmanlectures.caltech.edu/I_toc.html",
    "II": "https://www.feynmanlectures.caltech.edu/II_toc.html",
    "III": "https://www.feynmanlectures.caltech.edu/III_toc.html",
}
BASE_URL = "https://www.feynmanlectures.caltech.edu"

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
]


@asynccontextmanager
async def create_browser(headless: bool = True) -> AsyncGenerator[tuple[Browser, Page], None]:
    """Context manager: yields (browser, page) with stealth configured."""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=headless)
        context = await browser.new_context(
            user_agent=random.choice(USER_AGENTS),
            viewport={"width": 1280, "height": 800},
            locale="en-US",
        )
        # Apply playwright-stealth if available
        try:
            from playwright_stealth import stealth_async
            await stealth_async(context)
        except ImportError:
            log.warning("playwright-stealth not installed; proceeding without stealth plugin")

        page = await context.new_page()
        # Override navigator.webdriver to avoid bot detection
        await page.add_init_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => false})"
        )
        try:
            yield browser, page
        finally:
            await browser.close()


async def crawl_toc(page: Page, volume: str) -> list[dict]:
    """Fetch ToC page and return list of {url, number, title} dicts."""
    toc_url = TOC_URLS[volume]
    log.info("Crawling ToC: %s", toc_url)
    await page.goto(toc_url, wait_until="networkidle", timeout=30_000)
    await asyncio.sleep(random.uniform(1.0, 2.0))

    # Extract chapter links matching pattern /{vol}_NN.html
    pattern = re.compile(rf"/{volume}_(\d+)\.html$", re.IGNORECASE)
    links = await page.query_selector_all("a[href]")
    chapters = []
    seen = set()
    for link in links:
        href = await link.get_attribute("href")
        text = (await link.inner_text()).strip()
        if not href:
            continue
        # Resolve relative URLs
        full_url = urllib.parse.urljoin(BASE_URL + "/", href.lstrip("/"))
        m = pattern.search(href)
        if m and full_url not in seen:
            seen.add(full_url)
            chapters.append({
                "url": full_url,
                "number": int(m.group(1)),
                "title": text or f"Chapter {m.group(1)}",
            })
    chapters.sort(key=lambda c: c["number"])
    log.info("Found %d chapters in Vol %s", len(chapters), volume)
    return chapters


async def crawl_chapter(page: Page, url: str, delay: tuple[float, float] = (1.0, 3.0)) -> str:
    """Fetch chapter HTML. Returns full page HTML after MathJax renders."""
    await page.goto(url, wait_until="networkidle", timeout=60_000)
    # Extra wait for MathJax to finish rendering
    try:
        await page.wait_for_function("typeof MathJax !== 'undefined'", timeout=5_000)
        await page.wait_for_function(
            "MathJax.isReady || (MathJax.Hub && MathJax.Hub.queue.running === 0)",
            timeout=15_000
        )
    except Exception:
        pass  # Continue even if MathJax check times out
    await asyncio.sleep(random.uniform(*delay))
    return await page.content()


async def _fetch_image(session: aiohttp.ClientSession, url: str, dest: str) -> bool:
    """Download a single image to dest path. Returns True on success."""
    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=15)) as resp:
            if resp.status == 200:
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                with open(dest, "wb") as f:
                    f.write(await resp.read())
                return True
    except Exception as e:
        log.debug("Image download failed %s: %s", url, e)
    return False


async def download_images(html: str, chapter_dir: str, base_url: str = BASE_URL) -> dict[str, str]:
    """Download all images referenced in HTML. Returns {original_url: local_path}."""
    soup = BeautifulSoup(html, "html.parser")
    image_map: dict[str, str] = {}
    urls_to_fetch: list[tuple[str, str]] = []

    for img in soup.find_all("img", src=True):
        src = img["src"]
        full_url = urllib.parse.urljoin(base_url + "/", src)
        filename = os.path.basename(urllib.parse.urlparse(full_url).path) or "img.png"
        local_path = os.path.join(chapter_dir, filename)
        if not os.path.exists(local_path):
            urls_to_fetch.append((full_url, local_path))
        image_map[src] = local_path

    if urls_to_fetch:
        async with aiohttp.ClientSession(headers={"User-Agent": random.choice(USER_AGENTS)}) as session:
            tasks = [_fetch_image(session, url, path) for url, path in urls_to_fetch]
            results = await asyncio.gather(*tasks)
            ok = sum(results)
            log.debug("Downloaded %d/%d images to %s", ok, len(urls_to_fetch), chapter_dir)

    return image_map


def _with_retry(max_attempts: int = 3, base_delay: float = 5, max_delay: float = 30):
    """Decorator: exponential backoff retry for async functions."""
    def decorator(fn):
        async def wrapper(*args, **kwargs):
            delay = base_delay
            for attempt in range(1, max_attempts + 1):
                try:
                    return await fn(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise
                    wait = min(delay * (2 ** (attempt - 1)), max_delay)
                    log.warning("Attempt %d/%d failed: %s. Retrying in %.0fs...",
                                attempt, max_attempts, e, wait)
                    await asyncio.sleep(wait)
        return wrapper
    return decorator


async def run_crawler(config: dict):
    """Main crawler orchestrator. Runs all volumes respecting daily limit + circuit breaker."""
    daily_limit: int = config["crawler"]["daily_limit"]
    circuit_limit: int = config["crawler"]["circuit_breaker"]
    delay_range = (
        config["crawler"]["request_delay_min"],
        config["crawler"]["request_delay_max"],
    )
    volumes: list[str] = config["crawler"]["volumes"]
    image_base = config.get("renderer", {}).get("output_dir", "data/images")

    crawled_urls = await db.get_crawled_urls()
    log.info("Already crawled: %d chapters", len(crawled_urls))

    pages_today = 0
    consecutive_failures = 0

    async with create_browser() as (browser, page):
        crawl_chapter_retry = _with_retry(
            config["crawler"]["max_retries"],
            config["crawler"]["retry_base_delay"],
            config["crawler"]["retry_max_delay"],
        )(crawl_chapter)

        for volume in volumes:
            if pages_today >= daily_limit:
                log.warning("Daily limit (%d) reached, stopping.", daily_limit)
                break
            if consecutive_failures >= circuit_limit:
                log.error("Circuit breaker tripped (%d consecutive failures). Stopping.", circuit_limit)
                log.error("ACTION NEEDED: Check Cloudflare status or switch to manual download.")
                break

            chapters = await crawl_toc(page, volume)
            pending = [c for c in chapters if c["url"] not in crawled_urls]
            log.info("Vol %s: %d/%d chapters to crawl", volume, len(pending), len(chapters))

            for ch_info in pending:
                if pages_today >= daily_limit:
                    log.info("Daily limit reached mid-volume, will resume tomorrow.")
                    break
                if consecutive_failures >= circuit_limit:
                    log.error("Circuit breaker: stopping. Notify user.")
                    break

                url = ch_info["url"]
                ch_num = ch_info["number"]
                log.info("Crawling Vol %s Ch %02d: %s", volume, ch_num, url)

                try:
                    html = await crawl_chapter_retry(page, url, delay_range)
                    chapter_dir = os.path.join("data/raw/images", f"{volume}_{ch_num:02d}")
                    image_map = await download_images(html, chapter_dir)

                    chapter = Chapter(
                        id=None,
                        volume=volume,
                        number=ch_num,
                        title=ch_info["title"],
                        url=url,
                        raw_html=html,
                    )
                    await db.insert_chapter(chapter)

                    crawled_urls.add(url)
                    pages_today += 1
                    consecutive_failures = 0
                    log.info("  ✓ Stored Vol %s Ch %02d (%d images)", volume, ch_num, len(image_map))

                except Exception as e:
                    consecutive_failures += 1
                    log.error("  ✗ Failed Vol %s Ch %02d: %s (failures: %d/%d)",
                               volume, ch_num, e, consecutive_failures, circuit_limit)

    log.info("Crawler finished. Crawled %d pages today.", pages_today)
    if consecutive_failures >= circuit_limit:
        print(
            "\n⚠️  CRAWLER STOPPED: Too many consecutive failures.\n"
            "   Possible Cloudflare block. Options:\n"
            "   1. Wait 24h and retry\n"
            "   2. Manually download HTML and import to DB\n"
        )
