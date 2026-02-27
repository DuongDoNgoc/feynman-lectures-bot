"""Bot daemon entry point."""
import asyncio
import logging

from src.knowledge.db import init_db
from src.utils import load_config, setup_logging, validate_config

log = logging.getLogger(__name__)


def main():
    config = load_config()
    setup_logging(config)
    validate_config(config)
    log.info("Starting Feynman Bot...")

    # Create a persistent event loop that PTB will reuse via get_event_loop().
    # asyncio.run() would close the loop afterwards, leaving PTB with no loop.
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # Init DB on this loop (loop stays open after run_until_complete)
    loop.run_until_complete(init_db(config))

    # Import here so logging is configured before telegram's handlers fire
    # run_bot is synchronous — PTB v20 calls get_event_loop() internally
    from src.bot.bot import run_bot
    run_bot(config)


if __name__ == "__main__":
    main()
