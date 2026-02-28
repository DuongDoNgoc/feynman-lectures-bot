---
title: "Phase 05: Testing & Validation"
phase: 5
status: pending
effort: 1h
---

# Phase 05: Testing & Validation

## Overview

Comprehensive testing of parser and chunker fixes before full re-parse.

## Context Links

- Main plan: [plan.md](plan.md)
- Test script: `scripts/test-e2e.py`

## Requirements

### Functional
- All existing tests pass
- Parser creates 3-8 sections per chapter
- Lesson titles are meaningful
- No data loss (formulas, images preserved)

### Non-Functional
- Test on at least 5 chapters before full reparse
- Document any edge cases

## Test Cases

### Test 1: Parser Section Detection
```bash
# Parse single chapter and check section count
python -c "
import asyncio
from src.utils import load_config
from src.knowledge import db
from src.crawler.parser import parse_chapter

async def test():
    config = load_config()
    await db.init_db(config)

    # Get a chapter
    chapters = await db.get_unparsed_chapters()
    if not chapters:
        print('No unparsed chapters - need to reset')
        return

    chapter = chapters[0]
    sections = parse_chapter(chapter.raw_html, {})
    print(f'Chapter {chapter.number}: {len(sections)} sections')
    for s in sections:
        print(f'  - {s.title}: {len(s.content_text.split())} words')

asyncio.run(test())
"
```

**Expected**: 3-8 sections per chapter

### Test 2: Chunk Size Distribution
```bash
# After chunking, check size distribution
sqlite3 data/feynman.db "
SELECT
  CASE
    WHEN words < 500 THEN '0-500'
    WHEN words < 1000 THEN '500-1000'
    WHEN words < 2000 THEN '1000-2000'
    ELSE '2000+'
  END as range,
  COUNT(*) as count
FROM (
  SELECT LENGTH(content_enhanced) - LENGTH(REPLACE(content_enhanced, ' ', '')) + 1 as words
  FROM lessons
)
GROUP BY 1
ORDER BY 1
"
```

**Expected**: Most chunks in 1000-2000 range

### Test 3: Lesson Title Format
```bash
# Check lesson titles
sqlite3 data/feynman.db "SELECT title FROM lessons LIMIT 10"
```

**Expected**: Format "Ch{N}-{M}: {Title} — {type}"

### Test 4: Formula Preservation
```bash
# Check formulas are still extracted
sqlite3 data/feynman.db "
SELECT COUNT(*) as total_formulas
FROM sections, json_each(latex_formulas)
"
```

**Expected**: Similar count to before fix

### Test 5: End-to-End Pipeline
```bash
# Run full pipeline on one chapter
python scripts/test-e2e.py
```

**Expected**: All tests pass

## Implementation Steps

### Step 1: Backup Database
```bash
cp data/feynman.db data/feynman.db.backup
```

### Step 2: Clear Sections/Lessons for Test Chapters
```sql
-- Clear parsed data for chapters 1-5
DELETE FROM lessons WHERE section_id IN (SELECT id FROM sections WHERE chapter_id IN (SELECT id FROM chapters WHERE number <= 5));
DELETE FROM sections WHERE chapter_id IN (SELECT id FROM chapters WHERE number <= 5);
```

### Step 3: Re-parse Test Chapters
```bash
python pipeline.py --stage parse
```

### Step 4: Re-chunk Test Chapters
```bash
python pipeline.py --stage chunk
```

### Step 5: Validate Results
Run all test cases above.

### Step 6: Full Re-parse (if tests pass)
```sql
-- Clear all parsed data
DELETE FROM lessons;
DELETE FROM sections;
```
```bash
python pipeline.py --stage parse
python pipeline.py --stage chunk
```

## Todo List

- [ ] Backup database
- [ ] Clear test chapter data
- [ ] Re-parse test chapters
- [ ] Run Test 1: Section count
- [ ] Run Test 2: Chunk sizes
- [ ] Run Test 3: Title format
- [ ] Run Test 4: Formula preservation
- [ ] Run Test 5: E2E pipeline
- [ ] Document results
- [ ] Full re-parse if tests pass

## Success Criteria

| Metric | Before | After (Target) |
|--------|--------|----------------|
| Sections per chapter | 1 | 3-8 |
| Avg section word count | 6540 | 1000-2000 |
| Chunks per section | 6-7 | 1-2 |
| Lesson title quality | "Chunk N" | "ChN-M: Title" |

## Rollback Plan

If tests fail:
```bash
# Restore database
cp data/feynman.db.backup data/feynman.db

# Revert code changes
git checkout src/crawler/parser.py
git checkout src/content/chunker.py
git checkout config.yaml
```

## Risk Assessment

| Risk | Impact | Mitigation |
|------|--------|------------|
| Tests reveal edge cases | Medium | Document and fix iteratively |
| Data loss during re-parse | Low | Backup before starting |
| Pipeline takes too long | Low | Can run in background |

## Final Checklist

- [ ] All tests pass
- [ ] Section counts improved
- [ ] Chunk sizes reasonable
- [ ] Titles meaningful
- [ ] Formulas preserved
- [ ] Images preserved
- [ ] No regression in bot functionality
- [ ] Documentation updated

## Completion

After all tests pass:
1. Update `docs/codebase-summary.md` with new section/chunk behavior
2. Update `docs/project-roadmap.md` with completion status
3. Create git commit with all changes
