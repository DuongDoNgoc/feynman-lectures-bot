# Planner Report: Lesson Preview Markdown Generator

**Date:** 2026-02-28
**Plan:** `/mnt/d/Vibecoding/FeynmanLecture/feynman-bot/plans/260228-0748-lesson-preview-markdown/`
**Status:** Complete

---

## Summary

Created comprehensive implementation plan for exporting Telegram Bot lessons to human-readable markdown files with approval workflow.

## Problem Analyzed

- Lessons stored in SQLite (`data/feynman.db`) with `enhancement_status='completed'`
- User cannot preview content before Telegram delivery
- No manual editing capability
- No approval workflow

## Solution Designed

4-phase implementation:
1. **Database Layer** - Query functions + approval_status column migration
2. **Markdown Exporter** - Generate structured MD files with YAML frontmatter
3. **CLI Tool** - Commands for export/approve/reject/list/sync
4. **Integration Testing** - E2E tests + documentation

## Key Decisions

| Decision | Rationale |
|----------|-----------|
| Store approval_status in DB | Source of truth, persists across re-exports |
| YAML frontmatter in MD files | Machine-readable metadata, standard format |
| Content hash for sync | Detect changes without full comparison |
| Split files >800 LOC | Maintain readability, code standards compliance |
| CLI over web UI | YAGNI, simpler to implement |

## Files Planned

### New Files
- `src/knowledge/preview_db.py` - Preview-specific DB queries
- `src/content/preview_exporter.py` - Markdown generation
- `scripts/lesson-preview.py` - CLI tool
- `scripts/test-preview-workflow.py` - Integration test

### Modified Files
- `src/knowledge/models.py` - Add approval_status field
- `src/knowledge/db.py` - Add migration
- `docs/codebase-summary.md` - Add preview module docs
- `README.md` - Add usage instructions

### Output Directory
- `docs/lessons-preview/` - Generated markdown files

## Database Changes

```sql
ALTER TABLE lessons ADD COLUMN approval_status TEXT DEFAULT 'pending';
-- Values: pending, approved, rejected
```

## CLI Commands

```bash
python scripts/lesson-preview.py export           # Export all
python scripts/lesson-preview.py export --id 5    # Export specific
python scripts/lesson-preview.py list             # List with status
python scripts/lesson-preview.py approve --id 5   # Approve
python scripts/lesson-preview.py reject --id 5    # Reject
python scripts/lesson-preview.py show --id 5      # Display content
python scripts/lesson-preview.py sync             # Re-export changed
```

## Effort Estimate

| Phase | Effort |
|-------|--------|
| Database Layer | 1h |
| Markdown Exporter | 1.5h |
| CLI Tool | 1h |
| Integration | 0.5h |
| **Total** | **4h** |

## Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Large lessons exceed 800 LOC | Auto-split at paragraph boundaries |
| Manual edits lost on re-export | Content hash detection, warn user |
| LaTeX not rendered in preview | Keep raw LaTeX, render at Telegram time |

## Unresolved Questions

1. Should approved lessons auto-delete preview files? (Recommend: No, keep for reference)
2. Track edit history in DB? (Recommend: No, YAGNI)
3. Support bulk approve/reject? (Recommend: Yes, add `--all` flag in future)

## Plan Files Created

```
plans/260228-0748-lesson-preview-markdown/
├── plan.md                           # Overview + phases
├── phase-01-database-layer.md        # DB functions + migration
├── phase-02-markdown-exporter.md     # MD generation
├── phase-03-cli-tool.md              # CLI interface
└── phase-04-integration-testing.md   # Tests + docs
```

## Next Steps

1. Delegate to `coder` agent to implement Phase 1
2. Run migration on copy of production DB
3. Continue through phases sequentially
4. Final testing and documentation update

---

## Compliance Checklist

- [x] Follows YAGNI (no unnecessary features)
- [x] Follows KISS (simple CLI, no web UI)
- [x] Follows DRY (reuse existing db.py patterns)
- [x] File naming: kebab-case for Python
- [x] Async-first architecture
- [x] Type hints and docstrings specified
- [x] Under 200 LOC per file guideline
- [x] Parameterized SQL queries
