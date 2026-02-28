#!/usr/bin/env python3
"""CLI tool for lesson preview workflow.

Commands:
    export      Export lessons to markdown
    list        List lessons with status
    approve     Mark lesson as approved
    reject      Mark lesson as rejected
    show        Display lesson content
    sync        Re-export changed lessons

Usage:
    python scripts/lesson-preview.py export
    python scripts/lesson-preview.py export --id 5
    python scripts/lesson-preview.py list --status pending
    python scripts/lesson-preview.py approve --id 5
    python scripts/lesson-preview.py approve --all
"""
import argparse
import asyncio
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.knowledge.preview_db import (
    get_completed_lessons,
    get_lessons_by_approval_status,
    get_lesson_with_context,
    update_approval_status,
    bulk_update_approval_status,
)
from src.content.preview_exporter import (
    export_lesson,
    export_all_lessons,
    export_lessons_by_type,
    OUTPUT_DIR,
)


# ANSI color codes
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"


def color_status(status: str) -> str:
    """Colorize status for display."""
    colors = {
        "approved": GREEN,
        "pending": YELLOW,
        "rejected": RED,
    }
    color = colors.get(status, "")
    return f"{color}{status}{RESET}"


async def cmd_export(args):
    """Export lessons to markdown."""
    if args.id:
        path = await export_lesson(args.id)
        if path:
            print(f"{GREEN}Exported:{RESET} {path}")
            return 0
        else:
            print(f"{RED}Error:{RESET} Lesson {args.id} not found")
            return 1

    if args.type:
        paths = await export_lessons_by_type(args.type)
    else:
        paths = await export_all_lessons()

    print(f"{GREEN}Exported {len(paths)} lessons to {OUTPUT_DIR}{RESET}")
    return 0


async def cmd_list(args):
    """List lessons with status."""
    if args.status:
        lessons = await get_lessons_by_approval_status(args.status)
    else:
        lessons = await get_completed_lessons()

    if not lessons:
        print(f"{YELLOW}No lessons found{RESET}")
        return 0

    print(f"\n{BLUE}{'ID':>4} {'Type':<12} {'Status':<10} {'Title':<40}{RESET}")
    print("-" * 70)

    for lesson in lessons:
        status = getattr(lesson, "approval_status", "pending")
        title = lesson.title[:38] + ".." if len(lesson.title) > 40 else lesson.title
        status_colored = color_status(status)
        print(f"{lesson.id:>4} {lesson.lesson_type:<12} {status_colored:<19} {title}")

    print(f"\nTotal: {len(lessons)} lessons")
    return 0


async def cmd_approve(args):
    """Mark lesson as approved."""
    if args.all:
        # Count pending lessons first
        pending = await get_lessons_by_approval_status("pending")
        if not pending:
            print(f"{YELLOW}No pending lessons to approve{RESET}")
            return 0

        # Require confirmation for bulk operations
        if not args.yes:
            print(f"{YELLOW}Warning:{RESET} This will approve {len(pending)} pending lessons.")
            response = input("Continue? [y/N] ")
            if response.lower() != "y":
                print("Cancelled.")
                return 1

        count = await bulk_update_approval_status("approved")
        print(f"{GREEN}Approved:{RESET} {count} lessons")
        return 0

    if not args.id:
        print(f"{RED}Error:{RESET} --id is required (or use --all)")
        return 1

    success = await update_approval_status(args.id, "approved")
    if success:
        print(f"{GREEN}Approved:{RESET} Lesson {args.id}")
        return 0
    else:
        print(f"{RED}Error:{RESET} Lesson {args.id} not found")
        return 1


async def cmd_reject(args):
    """Mark lesson as rejected."""
    if args.all:
        # Count pending lessons first
        pending = await get_lessons_by_approval_status("pending")
        if not pending:
            print(f"{YELLOW}No pending lessons to reject{RESET}")
            return 0

        # Require confirmation for bulk operations
        if not args.yes:
            print(f"{YELLOW}Warning:{RESET} This will reject {len(pending)} pending lessons.")
            response = input("Continue? [y/N] ")
            if response.lower() != "y":
                print("Cancelled.")
                return 1

        count = await bulk_update_approval_status("rejected")
        reason = f" - {args.reason}" if args.reason else ""
        print(f"{RED}Rejected:{RESET} {count} lessons{reason}")
        return 0

    if not args.id:
        print(f"{RED}Error:{RESET} --id is required (or use --all)")
        return 1

    success = await update_approval_status(args.id, "rejected")
    if success:
        reason = f" - {args.reason}" if args.reason else ""
        print(f"{RED}Rejected:{RESET} Lesson {args.id}{reason}")
        return 0
    else:
        print(f"{RED}Error:{RESET} Lesson {args.id} not found")
        return 1


async def cmd_show(args):
    """Display lesson content."""
    if not args.id:
        print(f"{RED}Error:{RESET} --id is required")
        return 1

    context = await get_lesson_with_context(args.id)
    if not context:
        print(f"{RED}Error:{RESET} Lesson {args.id} not found")
        return 1

    lesson = context["lesson"]
    section = context.get("section")
    chapter = context.get("chapter")

    print(f"\n{BLUE}=== Lesson {lesson.id} ==={RESET}")
    print(f"Type:    {lesson.lesson_type}")
    print(f"Status:  {color_status(getattr(lesson, 'approval_status', 'pending'))}")

    if chapter:
        print(f"Chapter: {chapter['number']} - {chapter['title']}")
    if section:
        print(f"Section: {section.number} - {section.title}")

    print(f"\n{lesson.content_enhanced[:500]}...")
    return 0


async def cmd_sync(args):
    """Re-export lessons where content changed.

    Compares content_hash in frontmatter with current hash.
    """
    import yaml

    lessons = await get_completed_lessons()
    re_exported = 0

    for lesson in lessons:
        # Find existing preview file
        pattern = f"{lesson.id:04d}-*.md"
        matches = list(OUTPUT_DIR.glob(pattern))

        if not matches:
            # No existing file, export it
            await export_lesson(lesson.id)
            re_exported += 1
            continue

        # Read frontmatter and check hash
        for match in matches:
            content = match.read_text(encoding="utf-8")

            # Parse frontmatter
            if content.startswith("---"):
                end = content.find("---", 3)
                if end > 0:
                    fm_text = content[3:end].strip()
                    try:
                        fm = yaml.safe_load(fm_text)
                        stored_hash = fm.get("content_hash", "")

                        # Compute current hash
                        from src.content.preview_exporter import _compute_hash
                        current_hash = _compute_hash(lesson.content_enhanced)

                        if stored_hash != current_hash:
                            await export_lesson(lesson.id)
                            re_exported += 1
                            print(f"Updated: Lesson {lesson.id}")
                    except Exception as e:
                        print(f"{YELLOW}Warning:{RESET} Could not parse {match}: {e}")

    print(f"{GREEN}Sync complete: {re_exported} lessons re-exported{RESET}")
    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Lesson preview workflow CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", help="Command")

    # Export command
    export_parser = subparsers.add_parser("export", help="Export lessons to markdown")
    export_parser.add_argument("--id", type=int, help="Export specific lesson")
    export_parser.add_argument("--type", choices=["concept", "deep_dive", "quiz"],
                               help="Export by lesson type")
    export_parser.add_argument("--all", action="store_true", help="Export all (default)")

    # List command
    list_parser = subparsers.add_parser("list", help="List lessons with status")
    list_parser.add_argument("--status", choices=["pending", "approved", "rejected"],
                             help="Filter by approval status")
    list_parser.add_argument("--type", choices=["concept", "deep_dive", "quiz"],
                             help="Filter by lesson type")

    # Approve command
    approve_parser = subparsers.add_parser("approve", help="Mark lesson as approved")
    approve_parser.add_argument("--id", type=int, help="Lesson ID")
    approve_parser.add_argument("--all", action="store_true", help="Approve all pending lessons")
    approve_parser.add_argument("-y", "--yes", action="store_true", help="Skip confirmation for bulk ops")

    # Reject command
    reject_parser = subparsers.add_parser("reject", help="Mark lesson as rejected")
    reject_parser.add_argument("--id", type=int, help="Lesson ID")
    reject_parser.add_argument("--all", action="store_true", help="Reject all pending lessons")
    reject_parser.add_argument("--reason", type=str, help="Rejection reason")
    reject_parser.add_argument("-y", "--yes", action="store_true", help="Skip confirmation for bulk ops")

    # Show command
    show_parser = subparsers.add_parser("show", help="Display lesson content")
    show_parser.add_argument("--id", type=int, required=True, help="Lesson ID")

    # Sync command
    subparsers.add_parser("sync", help="Re-export changed lessons")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    # Map commands to handlers
    handlers = {
        "export": cmd_export,
        "list": cmd_list,
        "approve": cmd_approve,
        "reject": cmd_reject,
        "show": cmd_show,
        "sync": cmd_sync,
    }

    handler = handlers.get(args.command)
    if handler:
        return asyncio.run(handler(args))

    return 1


if __name__ == "__main__":
    sys.exit(main())
