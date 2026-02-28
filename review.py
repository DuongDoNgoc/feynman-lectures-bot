"""CLI tool for reviewing and approving enhanced lessons.

Human-in-the-loop review step in the rolling enhance pipeline.

Usage:
  python review.py list                   # list lessons pending review
  python review.py stats                  # show enhancement/approval stats
  python review.py show <lesson_id>       # print full lesson content
  python review.py approve <lesson_id>    # approve single lesson
  python review.py reject <lesson_id>     # reject single lesson
  python review.py approve-batch          # interactive: review each lesson
"""
import argparse
import asyncio
import sys
import textwrap

from src.knowledge import db
from src.utils import load_config


def _truncate(text: str, max_chars: int = 400) -> str:
    text = text.strip()
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + "\n…"


def _print_lesson_summary(lesson, index: int = 0, total: int = 0):
    counter = f"[{index}/{total}] " if total else ""
    print(f"\n{'═' * 60}")
    print(f"{counter}Lesson #{lesson.id} — {lesson.lesson_type.upper()}")
    print(f"Title: {lesson.title}")
    print(f"Status: enhancement={lesson.enhancement_status} | approval={lesson.approval_status}")
    print("─" * 60)
    print(_truncate(lesson.content_enhanced))
    print("─" * 60)


async def cmd_list():
    config = load_config()
    await db.init_db(config)
    lessons = await db.get_enhanced_pending_review()
    if not lessons:
        print("✓ No lessons pending review.")
        return
    print(f"\n{'ID':>5}  {'Type':<10}  {'Title':<55}  Status")
    print("─" * 90)
    for l in lessons:
        title = (l.title or "")[:55]
        print(f"{l.id:>5}  {l.lesson_type:<10}  {title:<55}  {l.approval_status}")
    print(f"\n{len(lessons)} lesson(s) pending review.")


async def cmd_stats():
    import sqlite3
    conn = sqlite3.connect("data/feynman.db")
    total = conn.execute("SELECT COUNT(*) FROM lessons").fetchone()[0]
    enhanced = conn.execute("SELECT COUNT(*) FROM lessons WHERE enhancement_status='completed'").fetchone()[0]
    pending_review = conn.execute(
        "SELECT COUNT(*) FROM lessons WHERE enhancement_status='completed' AND approval_status='pending'"
    ).fetchone()[0]
    approved = conn.execute("SELECT COUNT(*) FROM lessons WHERE approval_status='approved'").fetchone()[0]
    rejected = conn.execute("SELECT COUNT(*) FROM lessons WHERE approval_status='rejected'").fetchone()[0]
    pending_enhance = total - enhanced
    conn.close()

    print(f"""
📊 Enhancement & Review Stats
─────────────────────────────
Total lessons:     {total}
Enhanced:          {enhanced} ({enhanced * 100 // max(total, 1)}%)
  ├─ Pending review: {pending_review}
  ├─ Approved:       {approved}
  └─ Rejected:       {rejected}
Still pending:     {pending_enhance}
─────────────────────────────
Bot can deliver:   {approved} approved lessons
""")


async def cmd_show(lesson_id: int):
    config = load_config()
    await db.init_db(config)
    from src.knowledge.db import get_db, _row_to_lesson
    async with get_db() as conn:
        rows = await conn.execute_fetchall("SELECT * FROM lessons WHERE id=?", (lesson_id,))
    if not rows:
        print(f"Lesson {lesson_id} not found.")
        return
    lesson = _row_to_lesson(rows[0])
    print(f"\n{'═' * 60}")
    print(f"Lesson #{lesson.id} — {lesson.lesson_type.upper()}")
    print(f"Title: {lesson.title}")
    print(f"Status: enhancement={lesson.enhancement_status} | approval={lesson.approval_status}")
    print("─" * 60)
    print(lesson.content_enhanced)
    print("═" * 60)


async def cmd_approve(lesson_id: int):
    config = load_config()
    await db.init_db(config)
    await db.set_approval_status(lesson_id, "approved")
    print(f"✓ Lesson {lesson_id} approved.")


async def cmd_reject(lesson_id: int):
    config = load_config()
    await db.init_db(config)
    await db.set_approval_status(lesson_id, "rejected")
    print(f"✗ Lesson {lesson_id} rejected.")


async def cmd_approve_batch():
    """Interactive batch review: show each lesson, approve/reject/skip."""
    config = load_config()
    await db.init_db(config)
    lessons = await db.get_enhanced_pending_review()

    if not lessons:
        print("✓ No lessons pending review.")
        return

    approved = rejected = skipped = 0
    total = len(lessons)
    print(f"\n{total} lesson(s) to review. Keys: [a]pprove | [r]eject | [s]kip | [v]iew full | [q]uit\n")

    for i, lesson in enumerate(lessons, 1):
        _print_lesson_summary(lesson, i, total)
        while True:
            try:
                choice = input("  > ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print("\nAborted.")
                break

            if choice == "a":
                await db.set_approval_status(lesson.id, "approved")
                print(f"  ✓ Approved")
                approved += 1
                break
            elif choice == "r":
                await db.set_approval_status(lesson.id, "rejected")
                print(f"  ✗ Rejected")
                rejected += 1
                break
            elif choice == "s":
                print(f"  → Skipped")
                skipped += 1
                break
            elif choice == "v":
                print("\n" + lesson.content_enhanced + "\n")
            elif choice == "q":
                print(f"\nStopped early. Approved: {approved}, Rejected: {rejected}, Skipped: {skipped}")
                return
            else:
                print("  Unknown key. Use: a / r / s / v / q")

    print(f"\n{'═' * 60}")
    print(f"Review complete: Approved={approved} | Rejected={rejected} | Skipped={skipped}")
    print(f"{'═' * 60}")


def main():
    parser = argparse.ArgumentParser(description="Feynman Bot — Lesson Review CLI")
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("list", help="List lessons pending review")
    sub.add_parser("stats", help="Show enhancement/approval stats")

    p_show = sub.add_parser("show", help="Show full content of a lesson")
    p_show.add_argument("lesson_id", type=int)

    p_approve = sub.add_parser("approve", help="Approve a lesson")
    p_approve.add_argument("lesson_id", type=int)

    p_reject = sub.add_parser("reject", help="Reject a lesson")
    p_reject.add_argument("lesson_id", type=int)

    sub.add_parser("approve-batch", help="Interactive batch review")

    args = parser.parse_args()

    if args.cmd == "list":
        asyncio.run(cmd_list())
    elif args.cmd == "stats":
        asyncio.run(cmd_stats())
    elif args.cmd == "show":
        asyncio.run(cmd_show(args.lesson_id))
    elif args.cmd == "approve":
        asyncio.run(cmd_approve(args.lesson_id))
    elif args.cmd == "reject":
        asyncio.run(cmd_reject(args.lesson_id))
    elif args.cmd == "approve-batch":
        asyncio.run(cmd_approve_batch())
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
