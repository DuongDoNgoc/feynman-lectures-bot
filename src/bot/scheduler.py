"""JobQueue-based lesson scheduler.

Delivers 3 lessons/day at configured times (Asia/Bangkok default).
Review days (Thu + Sun): generate weekly quiz compilation instead of new lessons.
Missed lesson catch-up: on bot restart, immediately send any undelivered lessons.
"""
import json
import logging
import os
from datetime import time

import pytz

from src.knowledge import db
from src.knowledge.models import Lesson

log = logging.getLogger(__name__)

# Day abbreviations → Python weekday integers (Mon=0 … Sun=6)
DAY_MAP = {
    "mon": 0, "tue": 1, "wed": 2, "thu": 3,
    "fri": 4, "sat": 5, "sun": 6,
}


def setup_schedule(app, config: dict):
    """Register JobQueue daily jobs for lesson delivery."""
    tz = pytz.timezone(config["schedule"]["timezone"])
    chat_id = int(config["telegram"]["chat_id"])
    times: list[str] = config["schedule"]["times"]
    lesson_types: list[str] = config["schedule"]["lesson_types"]
    review_days: list[str] = [d.lower() for d in config["schedule"].get("review_days", [])]
    review_day_nums = {DAY_MAP[d] for d in review_days if d in DAY_MAP}

    for t_str, lesson_type in zip(times, lesson_types):
        h, m = map(int, t_str.split(":"))
        job_time = time(hour=h, minute=m, tzinfo=tz)

        app.job_queue.run_daily(
            deliver_lesson_callback,
            time=job_time,
            chat_id=chat_id,
            data={
                "lesson_type": lesson_type,
                "config": config,
                "review_day_nums": review_day_nums,
            },
            name=f"lesson_{lesson_type}",
        )
        log.info("Scheduled %s at %s %s", lesson_type, t_str, config["schedule"]["timezone"])


async def deliver_lesson_callback(context):
    """JobQueue callback: deliver one lesson or a review quiz."""
    from telegram import InputFile
    from src.bot.handlers import send_quiz_questions, split_message

    job = context.job
    chat_id = job.chat_id
    data = job.data
    lesson_type: str = data["lesson_type"]
    config: dict = data["config"]
    review_day_nums: set = data["review_day_nums"]

    # Check if today is a review day
    from datetime import datetime
    import pytz as _pytz
    tz = _pytz.timezone(config["schedule"]["timezone"])
    today_weekday = datetime.now(tz).weekday()

    if today_weekday in review_day_nums:
        # Only send review quiz once (on the quiz slot, not concept/deep_dive)
        if lesson_type == "quiz":
            await _deliver_review_quiz(context.bot, chat_id, config)
        else:
            log.info("Review day — skipping %s slot", lesson_type)
        return

    # Normal lesson delivery
    lesson = await db.get_next_lesson_by_type(chat_id, lesson_type)
    if not lesson:
        await context.bot.send_message(
            chat_id,
            f"🎉 Bạn đã hoàn thành tất cả bài {lesson_type}! Chờ thêm nội dung mới.",
        )
        return

    await _send_lesson_content(context.bot, chat_id, lesson)
    await db.mark_sent(chat_id, lesson.id)
    await db.insert_scheduled_record(chat_id, lesson.id, lesson_type)
    log.info("Delivered %s lesson %d to chat %d", lesson_type, lesson.id, chat_id)


async def _send_lesson_content(bot, chat_id: int, lesson: Lesson):
    """Send lesson text + math images to chat."""
    from telegram import InputFile
    from src.bot.handlers import split_message

    parts = split_message(lesson.content_enhanced)
    for part in parts:
        await bot.send_message(chat_id, part, parse_mode="HTML")

    if lesson.math_images_json:
        for png_path in json.loads(lesson.math_images_json):
            if os.path.exists(png_path):
                try:
                    await bot.send_photo(chat_id, photo=InputFile(open(png_path, "rb")))
                except Exception as e:
                    log.warning("Failed sending math image %s: %s", png_path, e)

    # Auto-send quiz questions if it's a quiz lesson
    if lesson.lesson_type == "quiz" and lesson.quiz_json:
        from src.bot.handlers import send_quiz_questions
        await send_quiz_questions(bot, chat_id, lesson)


async def _deliver_review_quiz(bot, chat_id: int, config: dict):
    """Compile a weekly review quiz from lessons delivered this week."""
    from src.bot.handlers import split_message

    lessons = await db.get_lessons_delivered_this_week(chat_id)
    if not lessons:
        await bot.send_message(chat_id, "📅 Ngày ôn tập — chưa có bài học nào trong tuần này.")
        return

    # Build a summary quiz from lesson titles
    titles = "\n".join(f"  • {l.title}" for l in lessons[:10])
    header = (
        f"🔄 <b>ÔN TẬP TUẦN</b>\n\n"
        f"Bạn đã học {len(lessons)} bài trong tuần:\n{titles}\n\n"
        f"Hãy ôn lại và trả lời các câu hỏi bên dưới:"
    )
    await bot.send_message(chat_id, header, parse_mode="HTML")

    # Send quiz for the most recent quiz lesson
    quiz_lessons = [l for l in lessons if l.quiz_json]
    if quiz_lessons:
        from src.bot.handlers import send_quiz_questions
        for ql in quiz_lessons[-3:]:  # Last 3 quiz lessons
            await send_quiz_questions(bot, chat_id, ql)
    else:
        await bot.send_message(chat_id, "Chưa có câu hỏi quiz cho tuần này.")


async def catchup_missed_lessons(app, config: dict):
    """On bot restart: deliver any undelivered scheduled lessons immediately."""
    chat_id_str = config["telegram"].get("chat_id", "")
    if not chat_id_str:
        return
    chat_id = int(chat_id_str)

    missed = await db.get_undelivered_scheduled(chat_id)
    if not missed:
        return

    log.info("Catching up %d missed lessons for chat %d", len(missed), chat_id)
    for scheduled in missed:
        lesson_rows = None
        from src.knowledge.db import get_db, _row_to_lesson
        async with get_db() as conn:
            rows = await conn.execute_fetchall(
                "SELECT * FROM lessons WHERE id=?", (scheduled.lesson_id,)
            )
        if not rows:
            continue
        lesson = _row_to_lesson(rows[0])
        try:
            await _send_lesson_content(app.bot, chat_id, lesson)
            await db.mark_scheduled_delivered(scheduled.id)
            log.info("Caught up: lesson %d (%s)", lesson.id, lesson.lesson_type)
        except Exception as e:
            log.error("Catch-up failed for lesson %d: %s", lesson.id, e)
