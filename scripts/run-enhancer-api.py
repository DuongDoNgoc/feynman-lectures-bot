"""Process pending_prompts.jsonl via LLM API → enhanced_outputs.jsonl.

Usage:
  source .env && python scripts/run-enhancer-api.py

Resumable: skips already-processed lesson IDs in enhanced_outputs.jsonl.
"""
import asyncio
import json
import logging
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils import load_config, setup_logging
from src.llm.provider import LLMProvider

PROMPTS_FILE = "data/pending_prompts.jsonl"
OUTPUTS_FILE = "data/enhanced_outputs.jsonl"

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
log = logging.getLogger("enhancer-api")


def load_done_ids() -> set[str]:
    done = set()
    if not os.path.exists(OUTPUTS_FILE):
        return done
    with open(OUTPUTS_FILE) as f:
        for line in f:
            try:
                r = json.loads(line.strip())
                done.add(f"{r['lesson_id']}_{r.get('lesson_type','')}")
            except Exception:
                pass
    return done


async def main():
    config = load_config()
    # Fallback to qa (DeepSeek) config if enhancement key missing
    llm_cfg = config.get("enhancement", config.get("qa"))
    # Override max_tokens for long-form content
    if llm_cfg.get("max_tokens", 0) < 2000:
        llm_cfg = dict(llm_cfg, max_tokens=3500, request_delay=1.0)
    llm = LLMProvider(llm_cfg)

    log.info("Provider: %s / Model: %s", llm.provider, llm.model)

    with open(PROMPTS_FILE) as f:
        prompts = [json.loads(l.strip()) for l in f if l.strip()]

    done_ids = load_done_ids()
    pending = [p for p in prompts if f"{p['lesson_id']}_{p['lesson_type']}" not in done_ids]

    log.info("Total: %d | Already done: %d | Remaining: %d",
             len(prompts), len(prompts) - len(pending), len(pending))

    if not pending:
        log.info("All done. Run: python pipeline.py --stage enhance --import")
        return

    succeeded = 0
    failed = 0

    with open(OUTPUTS_FILE, "a") as out:
        for i, p in enumerate(pending, 1):
            lesson_id = p["lesson_id"]
            lesson_type = p["lesson_type"]
            log.info("[%d/%d] lesson_id=%d type=%s", i, len(pending), lesson_id, lesson_type)
            try:
                content = await llm.generate(
                    system_prompt=p["system"],
                    user_prompt=p["prompt"],
                )
                record = {
                    "lesson_id": lesson_id,
                    "lesson_type": lesson_type,
                    "content": content,
                }
                out.write(json.dumps(record, ensure_ascii=False) + "\n")
                out.flush()
                succeeded += 1
            except Exception as e:
                log.error("  Failed lesson %d: %s", lesson_id, e)
                failed += 1

            # Rate limit delay
            if i < len(pending):
                await asyncio.sleep(llm.request_delay)

    log.info("\nDone: %d succeeded, %d failed", succeeded, failed)
    if succeeded > 0:
        log.info("Now run: python pipeline.py --stage enhance --import")


if __name__ == "__main__":
    asyncio.run(main())
