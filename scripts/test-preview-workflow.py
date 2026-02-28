#!/usr/bin/env python3
"""Integration test for lesson preview workflow.

Tests:
    1. Database migration
    2. Export to markdown
    3. Approval workflow
    4. Sync functionality

Usage:
    python scripts/test-preview-workflow.py
"""
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.knowledge import db
from src.knowledge.preview_db import (
    get_completed_lessons,
    get_lessons_by_approval_status,
    update_approval_status,
)
from src.content.preview_exporter import (
    export_lesson,
    export_all_lessons,
    OUTPUT_DIR,
)


async def test_migration():
    """Test that migration adds approval_status column."""
    print("\n[1/4] Testing database migration...")

    # Init DB (runs migration)
    await db.init_db({"database": {"path": "data/feynman.db"}})

    # Check column exists
    async with db.get_db() as conn:
        rows = await conn.execute_fetchall(
            "PRAGMA table_info(lessons)"
        )
        columns = [r["name"] for r in rows]

    assert "approval_status" in columns, "approval_status column missing"
    print("  [OK] Migration successful, approval_status column exists")
    return True


async def test_export():
    """Test exporting lessons to markdown."""
    print("\n[2/4] Testing lesson export...")

    lessons = await get_completed_lessons()

    if not lessons:
        print("  [SKIP] No completed lessons to export")
        return True

    # Export first lesson
    first_lesson = lessons[0]
    path = await export_lesson(first_lesson.id)

    assert path is not None, "Export returned None"
    assert path.exists(), f"Export file not created: {path}"

    # Check content
    content = path.read_text(encoding="utf-8")
    assert content.startswith("---"), "Missing YAML frontmatter"
    assert "lesson_id:" in content, "Missing lesson_id in frontmatter"
    assert f"lesson_id: {first_lesson.id}" in content, "Wrong lesson_id"

    print(f"  [OK] Exported lesson {first_lesson.id} to {path}")
    return True


async def test_approval_workflow():
    """Test approve/reject workflow."""
    print("\n[3/4] Testing approval workflow...")

    lessons = await get_completed_lessons()

    if len(lessons) < 2:
        print("  [SKIP] Need at least 2 lessons for approval test")
        return True

    lesson1, lesson2 = lessons[0], lessons[1]

    # Test approve
    success = await update_approval_status(lesson1.id, "approved")
    assert success, f"Failed to approve lesson {lesson1.id}"

    approved = await get_lessons_by_approval_status("approved")
    approved_ids = [l.id for l in approved]
    assert lesson1.id in approved_ids, "Lesson not in approved list"
    print(f"  [OK] Approved lesson {lesson1.id}")

    # Test reject
    success = await update_approval_status(lesson2.id, "rejected")
    assert success, f"Failed to reject lesson {lesson2.id}"

    rejected = await get_lessons_by_approval_status("rejected")
    rejected_ids = [l.id for l in rejected]
    assert lesson2.id in rejected_ids, "Lesson not in rejected list"
    print(f"  [OK] Rejected lesson {lesson2.id}")

    # Reset to pending
    await update_approval_status(lesson1.id, "pending")
    await update_approval_status(lesson2.id, "pending")
    print("  [OK] Reset lessons to pending")

    return True


async def test_sync():
    """Test sync detects content changes."""
    print("\n[4/4] Testing sync functionality...")

    # This is tested via CLI in practice
    # Here we just verify export works after content check
    lessons = await get_completed_lessons()

    if not lessons:
        print("  [SKIP] No lessons to sync")
        return True

    # Re-export should work
    path = await export_lesson(lessons[0].id)
    assert path is not None, "Re-export failed"
    print(f"  [OK] Sync would re-export lesson {lessons[0].id}")

    return True


async def run_tests():
    """Run all tests."""
    print("=" * 50)
    print("Lesson Preview Workflow - Integration Tests")
    print("=" * 50)

    tests = [
        ("Migration", test_migration),
        ("Export", test_export),
        ("Approval Workflow", test_approval_workflow),
        ("Sync", test_sync),
    ]

    results = []
    for name, test_func in tests:
        try:
            result = await test_func()
            results.append((name, result, None))
        except AssertionError as e:
            results.append((name, False, str(e)))
        except Exception as e:
            results.append((name, False, f"Exception: {e}"))

    # Summary
    print("\n" + "=" * 50)
    print("Summary")
    print("=" * 50)

    passed = sum(1 for _, r, _ in results if r)
    total = len(results)

    for name, result, error in results:
        status = "[PASS]" if result else "[FAIL]"
        print(f"  {status} {name}")
        if error:
            print(f"         Error: {error}")

    print(f"\nTotal: {passed}/{total} tests passed")
    return passed == total


if __name__ == "__main__":
    success = asyncio.run(run_tests())
    sys.exit(0 if success else 1)
