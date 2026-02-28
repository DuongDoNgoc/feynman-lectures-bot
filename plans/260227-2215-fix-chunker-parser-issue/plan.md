---
title: "Fix Chunker/Parser Issue - Section Detection & Lesson Generation"
description: "Fix parser to detect nested h3 headings and optimize chunker for proper lesson boundaries"
status: pending
priority: P1
effort: 6h
branch: main
tags: [parser, chunker, content-pipeline, bugfix]
created: 2026-02-27
---

# Fix Chunker/Parser Issue - Implementation Plan

## Problem Summary

Current system creates **1 section per chapter** (~6500 words avg), then chunks into 6-7 pieces of ~1000 words. This causes:
- Later chunks lose context from earlier parts
- Lesson titles become generic "Chunk N - type"
- No semantic boundaries between lessons

## Root Cause Analysis

### Parser Issue (parser.py:103)
```python
for el in content.children:  # Only iterates DIRECT children
    if el.name in HEADING_TAGS:  # h2/h3 check
        # Save section...
```

**Problem**: `content.children` only yields **direct children** of the content div. If h3 headings are wrapped in `<div>`, `<section>`, or other containers, they are never detected.

### Chunker Behavior (chunker.py:34-45)
- Receives 1 giant section per chapter
- Splits purely by word count (800-1200 range)
- No semantic awareness of topic boundaries
- Creates generic "Chunk N" titles

## Recommended Solution: Option A (Fix Parser)

**Why not B (increase chunk size)?**
- 3000-4000 word chunks still lose context
- Doesn't fix semantic boundary issue
- Lesson quality remains poor

**Why not C (1 lesson per chapter)?**
- Too long for micro-learning (5-10 min lessons)
- Telegram message limits
- Loses granular progress tracking

**Why A (fix parser) is best:**
- Proper sections = semantic boundaries
- Natural lesson topics (e.g., "1-2: Conservation of Energy")
- Maintains micro-learning format
- Root cause fix, not symptom treatment

## Implementation Phases

| Phase | Description | Effort | Status |
|-------|-------------|--------|--------|
| [Phase 01](phase-01-analyze-html-structure.md) | Analyze HTML structure & nested heading detection | 1h | pending |
| [Phase 02](phase-02-fix-parser-heading-detection.md) | Fix parser to detect nested h2/h3 headings | 2h | pending |
| [Phase 03](phase-03-optimize-chunker-config.md) | Optimize chunker config for new section sizes | 1h | pending |
| [Phase 04](phase-04-update-lesson-generation.md) | Update lesson title/sequence generation | 1h | pending |
| [Phase 05](phase-05-testing-validation.md) | Testing & validation | 1h | pending |

**Total Effort**: 6 hours

## Key Files

| File | Changes |
|------|---------|
| `src/crawler/parser.py` | Fix `extract_sections()` to use recursive heading search |
| `src/content/chunker.py` | Adjust for smaller sections, improve title generation |
| `config.yaml` | Potentially adjust chunker settings |
| `src/knowledge/db.py` | May need section re-query updates |

## Success Criteria

1. Parser creates 3-8 sections per chapter (vs 1 currently)
2. Section word counts: 500-3000 words (vs 3369-10505 currently)
3. Lessons have meaningful titles (e.g., "Ch1-2: Conservation of Energy - concept")
4. Chunks preserve semantic boundaries (no mid-topic splits)
5. All existing tests pass
6. Re-parsing Vol I Ch 1-5 produces correct sections

## Dependencies

- No external dependencies
- Requires database re-parse after fix (existing data will be replaced)

## Risk Assessment

| Risk | Impact | Mitigation |
|------|--------|------------|
| HTML structure varies by chapter | Medium | Test on 5+ chapters before full reparse |
| Too many small sections created | Low | Configurable min_words threshold |
| Breaking existing lesson references | Medium | Section IDs change; lessons must regenerate |

## Next Steps

1. Start with Phase 01: Analyze actual HTML structure from crawled chapters
2. Implement recursive heading detection in parser
3. Validate on sample chapters
4. Adjust chunker if needed
5. Full re-parse and re-chunk

---

## Unresolved Questions

~~1. Should we keep existing lesson progress or reset after re-parse?~~ → Resolved: Full reset on separate branch
~~2. What is the actual HTML structure? Need to inspect `data/raw/` for sample HTML files.~~ → Resolved: Keep Phase 01 for inspection
~~3. Should h4 headings also create sections, or only h2/h3?~~ → Resolved: h2 + h3 only

---

## Validation Log

### Session 1 — 2026-02-28
**Trigger:** Initial plan validation before implementation
**Questions asked:** 6

#### Questions & Answers

1. **[Data Migration]** Should existing lesson progress (streaks, read status) be preserved or reset after re-parsing chapters?
   - Options: Full reset (Recommended) | Preserve progress | Backup + reset
   - **Answer:** Full reset
   - **Custom input:** "Work in another branch to test Full reset"
   - **Rationale:** Section IDs will change after re-parse, making progress mapping fragile. Working on a separate branch de-risks the reset — can validate before merging to main.

2. **[Architecture]** Which heading levels should create section boundaries?
   - Options: h2 + h3 only (Recommended) | h2 + h3 + h4 | h2 only
   - **Answer:** h2 + h3 only
   - **Rationale:** h2/h3 provides the right granularity (3-8 sections/chapter). h4 risks too many tiny sections; h2-only would still produce oversized sections needing chunker splits.

3. **[Architecture]** How should the parser handle HTML structure variations across chapters?
   - Options: content.find_all() recursive (Recommended) | CSS selector approach | Analyze first, decide later
   - **Answer:** content.find_all() recursive
   - **Rationale:** Simple, robust approach that handles any nesting depth. Avoids fragile assumptions about HTML structure.

4. **[Scope]** If a section is still over the chunk target (>1200 words) after proper heading detection, how should the chunker handle it?
   - Options: Keep as single lesson (Recommended) | Split at paragraph boundaries | Configurable threshold
   - **Answer:** Keep as single lesson
   - **Rationale:** Preserves semantic coherence. Enhancement LLM can summarize long sections. Avoids adding chunker complexity for edge cases.

5. **[Operations]** Should the re-parse be manual or automatic on bot startup?
   - Options: Manual pipeline run (Recommended) | Auto-detect + prompt
   - **Answer:** Manual pipeline run
   - **Rationale:** Predictable, no side effects on bot startup. User explicitly controls when data regenerates.

6. **[Scope]** Should we skip Phase 01 (HTML analysis) since the fix approach is confirmed?
   - Options: Skip Phase 01 (Recommended) | Keep Phase 01
   - **Answer:** Keep Phase 01
   - **Rationale:** Still valuable to inspect raw HTML for edge cases before committing to implementation. More cautious approach.

#### Confirmed Decisions
- **Data reset**: Full reset on separate branch — avoids risk to production data
- **Heading levels**: h2 + h3 only — optimal granularity
- **Parser approach**: `find_all()` recursive — simple, handles any nesting
- **Long sections**: Keep as single lesson up to ~3000 words — preserve semantic coherence
- **Re-parse trigger**: Manual `pipeline.py --stage parse` — predictable, explicit
- **Phase 01**: Keep — inspect HTML before implementing fix

#### Action Items
- [ ] Create a separate branch for this fix (user requested "work in another branch")
- [ ] Phase 01 should output HTML structure findings to inform Phase 02
- [ ] Chunker should NOT split sections that are under ~3000 words (even if over 1200)

#### Impact on Phases
- Phase 01: No change — keep as planned, inspect raw HTML
- Phase 02: Confirmed approach: use `content.find_all(HEADING_TAGS)` instead of `content.children`
- Phase 03: Simplify — remove paragraph-boundary splitting logic. Only chunk if section > configurable max (default ~3000 words)
- Phase 04: No change
- Phase 05: Add branch-based testing workflow — validate on branch before merging
