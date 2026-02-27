"""Quick test: send lesson #1 interleaved to Telegram.

Run from feynman-bot/:
  source .env && python scripts/test-interleaved.py [lesson_id]
"""
import asyncio
import json
import os
import sqlite3
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from telegram import Bot, InputFile
from src.bot.handlers import _build_interleaved_segments, _coalesce_segments, split_message

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = int(os.environ["TELEGRAM_CHAT_ID"])
DB_PATH = "data/feynman.db"


async def main():
    lesson_id = int(sys.argv[1]) if len(sys.argv) > 1 else 1

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    row = conn.execute(
        "SELECT id, title, lesson_type, content_enhanced, math_images_json FROM lessons WHERE id=?",
        (lesson_id,),
    ).fetchone()
    conn.close()

    if not row:
        print(f"Lesson {lesson_id} not found")
        return

    print(f"Sending lesson #{row['id']}: {row['title']} ({row['lesson_type']})")

    img_paths = []
    if row["math_images_json"]:
        img_paths = [p for p in json.loads(row["math_images_json"]) if os.path.exists(p)]
    print(f"  {len(img_paths)} PNG(s) available")

    segments = _coalesce_segments(
        _build_interleaved_segments(row["content_enhanced"], img_paths)
    )
    text_count = sum(1 for s in segments if s["type"] == "text")
    img_count = sum(1 for s in segments if s["type"] == "image")
    print(f"  Segments: {len(segments)} total ({text_count} text, {img_count} image)")

    bot = Bot(token=BOT_TOKEN)
    sent = 0
    for i, seg in enumerate(segments):
        if seg["type"] == "text":
            for part in split_message(seg["content"]):
                try:
                    await bot.send_message(CHAT_ID, part, parse_mode="Markdown")
                except Exception:
                    await bot.send_message(CHAT_ID, part)
                sent += 1
        elif seg["type"] == "image":
            try:
                await bot.send_photo(
                    chat_id=CHAT_ID,
                    photo=InputFile(open(seg["path"], "rb")),
                )
                sent += 1
            except Exception as e:
                print(f"  [!] Image failed: {e}")
        print(f"  [{i+1}/{len(segments)}] {seg['type']} sent")

    print(f"\n✅ Done — {sent} messages sent to chat {CHAT_ID}")


if __name__ == "__main__":
    asyncio.run(main())
