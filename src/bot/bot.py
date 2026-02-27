"""Telegram Application factory and bot runner."""
import logging

from telegram.ext import (
    ApplicationBuilder,
    CallbackQueryHandler,
    CommandHandler,
    MessageHandler,
    filters,
)

from src.bot.handlers import (
    error_handler,
    example_handler,
    explain_handler,
    help_handler,
    init_handlers,
    message_handler,
    next_handler,
    progress_handler,
    quiz_callback,
    quiz_handler,
    role_handler,
    schedule_handler,
    search_handler,
    start_handler,
)
from src.bot.scheduler import catchup_missed_lessons, setup_schedule
from src.llm.provider import build_qa_provider

log = logging.getLogger(__name__)


def create_app(config: dict):
    """Build and configure the Telegram Application."""
    token = config["telegram"]["bot_token"]

    # Init Q&A LLM provider (DeepSeek)
    qa_llm = build_qa_provider(config)
    init_handlers(config, qa_llm)

    app = (
        ApplicationBuilder()
        .token(token)
        .concurrent_updates(False)   # prevent state corruption in ConversationHandler
        .post_init(_make_post_init(config))
        .build()
    )

    # ── Command handlers ─────────────────────────────────────────────────────
    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(CommandHandler("next", next_handler))
    app.add_handler(CommandHandler("quiz", quiz_handler))
    app.add_handler(CommandHandler("explain", explain_handler))
    app.add_handler(CommandHandler("example", example_handler))
    app.add_handler(CommandHandler("progress", progress_handler))
    app.add_handler(CommandHandler("schedule", schedule_handler))
    app.add_handler(CommandHandler("role", role_handler))
    app.add_handler(CommandHandler("search", search_handler))
    app.add_handler(CommandHandler("help", help_handler))

    # ── Quiz inline-button callbacks ─────────────────────────────────────────
    app.add_handler(CallbackQueryHandler(quiz_callback, pattern=r"^quiz_"))

    # ── Free-form Q&A (any non-command text) ────────────────────────────────
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    # ── Top-level error handler ──────────────────────────────────────────────
    app.add_error_handler(error_handler)

    return app


def _make_post_init(config: dict):
    """Factory returning the post_init coroutine (runs after app is built)."""
    async def post_init(app):
        setup_schedule(app, config)
        await catchup_missed_lessons(app, config)
        log.info("Bot scheduler configured and running.")
    return post_init


def run_bot(config: dict):
    """Create app and start polling (blocks until stopped).

    PTB v20 run_polling() is a synchronous method that manages its own event
    loop — it must NOT be awaited inside asyncio.run().
    """
    app = create_app(config)
    log.info("Starting Telegram bot polling...")
    app.run_polling(drop_pending_updates=True)
