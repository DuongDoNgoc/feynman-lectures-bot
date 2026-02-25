"""Bot daemon entry point."""
import asyncio
import logging

from src.knowledge.db import init_db
from src.utils import load_config, setup_logging, validate_config

log = logging.getLogger(__name__)


async def _start(config: dict):
    await init_db(config)
    # Import here so logging is configured before telegram's handlers fire
    from src.bot.bot import run_bot
    await run_bot(config)


def main():
    config = load_config()
    setup_logging(config)
    validate_config(config)
    log.info("Starting Feynman Bot...")
    asyncio.run(_start(config))


if __name__ == "__main__":
    main()
