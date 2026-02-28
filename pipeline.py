"""Content pipeline entry point.

Stages (run in order):
  crawl   - fetch Feynman Lectures HTML via Playwright
  parse   - extract sections + LaTeX from raw HTML
  chunk   - split sections into ~1000-word micro-lessons
  enhance - rewrite with LLM into concept/deep_dive/quiz lessons
  render  - convert LaTeX formulas to PNG images (approved lessons only)
  preview - export enhanced lessons to markdown for human review

Usage:
  python pipeline.py                         # run all stages
  python pipeline.py --stage crawl           # single stage
  python pipeline.py --stage enhance --batch 10  # enhance 10 lessons
  python pipeline.py --stage enhance --import    # import Claude outputs
  python pipeline.py --stage preview         # export for review
"""
import argparse
import asyncio
import logging

from src.knowledge.db import init_db
from src.utils import load_config, setup_logging, validate_config

log = logging.getLogger(__name__)

STAGES = ["crawl", "parse", "chunk", "enhance", "render", "preview"]


async def run_pipeline(config: dict, stages: list[str], import_mode: bool = False, batch_size: int = 0):
    await init_db(config)

    if "crawl" in stages:
        log.info("=== Stage: crawl ===")
        from src.crawler.scraper import run_crawler
        await run_crawler(config)

    if "parse" in stages:
        log.info("=== Stage: parse ===")
        from src.crawler.parser import run_parser
        await run_parser(config)

    if "chunk" in stages:
        log.info("=== Stage: chunk ===")
        from src.content.chunker import run_chunker
        await run_chunker(config)

    if "enhance" in stages:
        log.info("=== Stage: enhance ===")
        from src.content.enhancer import run_enhancer
        await run_enhancer(config, import_mode=import_mode, batch_size=batch_size)

    if "render" in stages:
        log.info("=== Stage: render ===")
        from src.renderer.math_renderer import run_renderer
        await run_renderer(config)

    if "preview" in stages:
        log.info("=== Stage: preview ===")
        from src.content.preview_exporter import export_all_lessons
        await export_all_lessons()

    log.info("Pipeline complete.")


def main():
    parser = argparse.ArgumentParser(description="Feynman Bot content pipeline")
    parser.add_argument(
        "--stage", choices=STAGES,
        help="Run a single stage only (default: all stages in order)"
    )
    parser.add_argument("--config", default="config.yaml", help="Path to config.yaml")
    parser.add_argument("--import", dest="import_mode", action="store_true",
                        help="Import enhanced_outputs.jsonl into DB (use with --stage enhance)")
    parser.add_argument("--batch", type=int, default=0,
                        help="Limit enhance stage to N lessons per run (0=all)")
    args = parser.parse_args()

    config = load_config(args.config)
    setup_logging(config)

    stages = [args.stage] if args.stage else STAGES
    log.info("Running stages: %s", stages)
    asyncio.run(run_pipeline(config, stages, import_mode=args.import_mode, batch_size=args.batch))


if __name__ == "__main__":
    main()
