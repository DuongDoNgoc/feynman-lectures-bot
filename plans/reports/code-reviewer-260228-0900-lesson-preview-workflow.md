# Code Review: Lesson Preview Workflow

## Scope
- Files: `src/knowledge/models.py`, `src/knowledge/db.py`, `src/knowledge/preview_db.py`, `src/content/preview_exporter.py`, `scripts/lesson-preview.py`, `scripts/test-preview-workflow.py`
- LOC: ~530 lines total
- Focus: New lesson preview/approval workflow implementation
- Scout findings: None (no git history for edge case analysis)

## Overall Assessment
Well-structured implementation following project conventions. Clean separation of concerns between database layer, exporter, and CLI. Good use of parameterized queries and async patterns. Minor issues in error handling and validation.

---

## Critical Issues

None identified.

---

## High Priority

### 1. Missing Input Validation in CLI (lesson-preview.py)
**File:** `/mnt/d/Vibecoding/FeynmanLecture/feynman-bot/scripts/lesson-preview.py`
**Lines:** 105-146

**Problem:** `--all` flag with `approve`/`reject` updates ALL pending lessons without confirmation. Destructive bulk operation with no safety check.

```python
if args.all:
    # Bulk approve all pending lessons
    count = await bulk_update_approval_status("approved")  # No confirmation!
```

**Impact:** Accidental bulk approval/rejection of all pending lessons.

**Recommendation:** Add confirmation prompt for bulk operations:
```python
if args.all:
    if not args.yes:  # Add --yes flag to skip confirmation
        confirm = input(f"Approve ALL pending lessons? [y/N]: ")
        if confirm.lower() != 'y':
            print("Cancelled")
            return 0
    count = await bulk_update_approval_status("approved")
```

### 2. Potential File Overwrite on Multi-Part Export
**File:** `/mnt/d/Vibecoding/FeynmanLecture/feynman-bot/src/content/preview_exporter.py`
**Lines:** 229-241

**Problem:** When splitting long content into parts, existing part files are overwritten without warning. Also, single-file export at line 233 creates a file, but multi-part export doesn't clean it up.

```python
if len(parts) == 1:
    output_path.write_text(markdown, encoding="utf-8")
else:
    # Write multiple parts - but original output_path file may exist from previous run
    for i, part in enumerate(parts, 1):
        part_path = OUTPUT_DIR / f"{lesson.id:04d}-{lesson.lesson_type}-{chapter_slug}-part{i}.md"
```

**Impact:** Stale files from single-part exports could coexist with multi-part exports.

**Recommendation:** Clean up old parts before writing new ones, or use a consistent naming scheme.

### 3. Unvalidated Status in get_lessons_by_approval_status
**File:** `/mnt/d/Vibecoding/FeynmanLecture/feynman-bot/src/knowledge/preview_db.py`
**Lines:** 78-91

**Problem:** Unlike `update_approval_status()`, the `get_lessons_by_approval_status()` function doesn't validate the status parameter. Invalid status would silently return empty results.

```python
async def get_lessons_by_approval_status(status: str) -> list[Lesson]:
    # No validation here, but update_approval_status has it
    async with get_db() as conn:
        rows = await conn.execute_fetchall(...)
```

**Impact:** Typos in status filter go undetected.

**Recommendation:** Add same validation as `update_approval_status()`:
```python
valid_statuses = ("pending", "approved", "rejected")
if status not in valid_statuses:
    raise ValueError(f"Invalid status: {status}")
```

---

## Medium Priority

### 4. Inconsistent Error Handling Pattern
**File:** `/mnt/d/Vibecoding/FeynmanLecture/feynman-bot/src/content/preview_exporter.py`
**Lines:** 57-60

**Problem:** JSON parse failure returns soft error string instead of raising exception.

```python
try:
    quiz = json.loads(quiz_json)
except json.JSONDecodeError:
    return "\n\n*Quiz data could not be parsed*\n"  # Silent failure
```

**Impact:** Malformed quiz data goes unnoticed during export.

**Recommendation:** Log the warning and optionally raise if strict validation needed.

### 5. Frontmatter YAML Escaping May Be Incomplete
**File:** `/mnt/d/Vibecoding/FeynmanLecture/feynman-bot/src/content/preview_exporter.py`
**Lines:** 166-173

**Problem:** Custom YAML escaping only handles `"` and `:`. Other special YAML characters (newlines, backslashes, leading special chars) are not handled.

```python
if isinstance(value, str) and ('"' in value or ":" in value):
    fm_lines.append(f'{key}: "{value}"')
```

**Impact:** Titles with newlines or other YAML special chars could break frontmatter parsing.

**Recommendation:** Use proper YAML library or broader escaping:
```python
import yaml
fm_lines.append(yaml.dump({key: value}).strip())
```

### 6. Sync Command Accesses Private Function
**File:** `/mnt/d/Vibecoding/FeynmanLecture/feynman-bot/scripts/lesson-preview.py`
**Lines:** 212-213

**Problem:** CLI imports private function `_compute_hash` from exporter module.

```python
from src.content.preview_exporter import _compute_hash
```

**Impact:** Breaks encapsulation, makes refactoring harder.

**Recommendation:** Either make `_compute_hash` public (`compute_content_hash`) or expose a `needs_reexport()` helper function.

### 7. No Index on approval_status in New Installations
**File:** `/mnt/d/Vibecoding/FeynmanLecture/feynman-bot/src/knowledge/db.py`
**Lines:** 123-126

**Problem:** Index creation is outside the main `executescript` block, runs every init. While harmless, the migration approach is inconsistent with other schema changes.

```python
await conn.execute("""
    CREATE INDEX IF NOT EXISTS idx_lessons_approval
    ON lessons(approval_status)
""")
```

**Impact:** Minor - no functional issue, just code organization.

---

## Low Priority

### 8. Hardcoded Output Directory
**File:** `/mnt/d/Vibecoding/FeynmanLecture/feynman-bot/src/content/preview_exporter.py`
**Line:** 18

```python
OUTPUT_DIR = Path(__file__).parent.parent.parent / "docs" / "lessons-preview"
```

**Impact:** Not configurable via config file. Fine for now but may need flexibility later.

### 9. Missing Type Hint for Optional Dict
**File:** `/mnt/d/Vibecoding/FeynmanLecture/feynman-bot/src/content/preview_exporter.py`
**Line:** 137

```python
def _generate_markdown(
    lesson,
    section: Optional,  # Should be Optional[Section]
    chapter: Optional[dict],
) -> str:
```

**Impact:** Type checkers won't catch Section type errors.

### 10. Color Code Magic Strings
**File:** `/mnt/d/Vibecoding/FeynmanLecture/feynman-bot/scripts/lesson-preview.py`
**Lines:** 42-47

```python
GREEN = "\033[92m"
YELLOW = "\033[93m"
```

**Impact:** Minor - could use a library like `colorama` for cross-platform support, but fine for POSIX.

---

## Positive Observations

1. **SQL Injection Prevention**: All database queries use parameterized queries properly
2. **Async Patterns**: Correct use of async/await throughout
3. **Context Managers**: Database connections properly managed with `async with`
4. **Docstrings**: Good documentation following project standards
5. **Migration Safety**: ALTER TABLE wrapped in try/except to handle existing column
6. **Backward Compatibility**: `_row_to_lesson()` handles missing `approval_status` column gracefully
7. **File Organization**: Clean separation - db.py for core, preview_db.py for workflow-specific queries
8. **Test Coverage**: Integration tests cover all major workflow paths

---

## Recommended Actions

1. **High**: Add confirmation for bulk approve/reject operations
2. **High**: Add status validation to `get_lessons_by_approval_status()`
3. **High**: Handle file cleanup for multi-part exports
4. **Medium**: Use proper YAML library for frontmatter generation
5. **Medium**: Make `_compute_hash` public or add helper function
6. **Low**: Fix `Optional` type hint in `_generate_markdown`

---

## Metrics

| Metric | Value |
|--------|-------|
| Type Coverage | ~90% (minor gap in Optional hint) |
| Test Coverage | Integration tests present |
| Linting Issues | None critical |
| Security Issues | None (SQL injection prevented) |

---

## Unresolved Questions

1. Should the `--reason` flag for rejection be stored in the database? Currently only displayed in CLI output.
2. What's the expected behavior when re-exporting a lesson that was previously split into parts? Should old parts be deleted?
3. Should there be a rate limit on bulk operations to prevent accidental mass changes?
