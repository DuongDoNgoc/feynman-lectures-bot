"""End-to-end pipeline test on Chapter I_01.

Tests: crawl → parse → chunk → enhance (1 lesson) → render math → verify
Run: python scripts/test-e2e.py

Requires:
  - ANTHROPIC_API_KEY or DEEPSEEK_API_KEY in environment
  - Playwright chromium installed
  - pdflatex installed (optional, falls back to matplotlib)
"""
import asyncio
import os
import sys

# Allow running from project root
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

TEST_URL = "https://www.feynmanlectures.caltech.edu/I_01.html"
TEST_DB = "/tmp/feynman_e2e_test.db"


async def test_pipeline():
    from src.utils import load_config, setup_logging
    config = load_config()
    config["database"]["path"] = TEST_DB
    setup_logging(config)

    import logging
    log = logging.getLogger("e2e")

    # ── 1. DB init ───────────────────────────────────────────────────────────
    from src.knowledge.db import init_db
    await init_db(config)
    log.info("[1/6] DB initialized at %s", TEST_DB)

    # ── 2. Crawl one chapter ─────────────────────────────────────────────────
    from src.crawler.scraper import create_browser, crawl_chapter, download_images
    from src.knowledge.db import insert_chapter
    from src.knowledge.models import Chapter

    log.info("[2/6] Crawling %s ...", TEST_URL)
    async with create_browser() as (browser, page):
        html = await crawl_chapter(page, TEST_URL)

    assert len(html) > 5000, f"Crawl returned too little HTML ({len(html)} chars)"
    assert "MathJax" in html or "math/tex" in html, "No MathJax found in HTML"
    log.info("  ✓ Crawled %d chars", len(html))

    image_map = await download_images(html, "data/raw/images/I_01")
    log.info("  ✓ Downloaded %d images", len(image_map))

    chapter = Chapter(id=None, volume="I", number=1,
                      title="Atoms in Motion", url=TEST_URL, raw_html=html)
    ch_id = await insert_chapter(chapter)
    log.info("  ✓ Stored chapter id=%d", ch_id)

    # ── 3. Parse ─────────────────────────────────────────────────────────────
    from src.crawler.parser import parse_chapter
    from src.knowledge.db import insert_section

    log.info("[3/6] Parsing HTML...")
    sections = parse_chapter(html, image_map)
    assert len(sections) > 0, "No sections extracted"
    total_formulas = sum(len(s.latex_formulas) for s in sections)
    assert total_formulas >= 5, f"Too few formulas extracted: {total_formulas}"
    log.info("  ✓ %d sections, %d formulas", len(sections), total_formulas)

    for section in sections:
        section.chapter_id = ch_id
        await insert_section(ch_id, section)

    # ── 4. Chunk ─────────────────────────────────────────────────────────────
    from src.content.chunker import chunk_sections
    from src.knowledge.db import get_all_sections

    log.info("[4/6] Chunking sections...")
    all_sections = await get_all_sections()
    chunks = chunk_sections(
        all_sections,
        target=config["chunker"]["target_words"],
        tolerance=config["chunker"]["tolerance"],
        min_words=config["chunker"]["min_words"],
    )
    assert len(chunks) > 0, "No chunks produced"
    small = [c for c in chunks if c.word_count < 500]
    assert not small, f"{len(small)} chunks below 500 words minimum"
    log.info("  ✓ %d chunks, avg %d words",
             len(chunks), sum(c.word_count for c in chunks) // len(chunks))

    # ── 5. Enhance 1 lesson (concept only to save API calls) ─────────────────
    from src.content.enhancer import enhance_lesson
    from src.knowledge.db import insert_lesson
    from src.knowledge.models import Lesson
    from src.llm.provider import build_enhancement_provider

    log.info("[5/6] Enhancing first chunk (concept)...")
    chunk = chunks[0]
    raw_lesson = Lesson(
        id=None,
        section_id=chunk.section_ids[0],
        lesson_type="concept",
        sequence=0,
        title="Test Chunk",
        content_enhanced=chunk.text,
        enhancement_status="pending",
    )
    lesson_id = await insert_lesson(raw_lesson)
    raw_lesson.id = lesson_id

    llm = build_enhancement_provider(config)
    enhanced = await enhance_lesson(raw_lesson, llm, config["user"]["role"])
    assert len(enhanced.content_enhanced) > 200, "Enhancement too short"
    assert enhanced.title and enhanced.title != "Untitled", "No title extracted"
    log.info("  ✓ Enhanced: '%s' (%d chars)", enhanced.title, len(enhanced.content_enhanced))

    from src.knowledge.db import update_lesson_content
    await update_lesson_content(enhanced)

    # ── 6. Render math ────────────────────────────────────────────────────────
    from src.renderer.math_renderer import render_lesson_math

    log.info("[6/6] Rendering math images...")
    os.makedirs("data/images", exist_ok=True)
    png_paths = render_lesson_math(enhanced, "data/images", dpi=config["renderer"]["dpi"])
    if chunk.formulas:
        assert len(png_paths) > 0, "No math images rendered despite formulas existing"
    for path in png_paths:
        assert os.path.exists(path), f"PNG not found: {path}"
    log.info("  ✓ %d math images rendered", len(png_paths))

    # ── Cleanup ───────────────────────────────────────────────────────────────
    os.remove(TEST_DB)
    log.info("\n✅ E2E test PASSED (all 6 stages)")
    print("\n✅ E2E test PASSED")


if __name__ == "__main__":
    asyncio.run(test_pipeline())
