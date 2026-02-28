---
title: "Phase 03: Optimize Chunker Config"
phase: 3
status: completed
effort: 1h
completed: 2026-02-28
---

# Phase 03: Optimize Chunker Config

## Overview

Adjust chunker settings for smaller section sizes after parser fix.

## Context Links

- Main plan: [plan.md](plan.md)
- Chunker code: `src/content/chunker.py`
- Config: `config.yaml`

## Key Insights

After Phase 02, sections will be smaller (500-3000 words vs 3369-10505).

Current config:
- target_words: 1000
- tolerance: 0.2 (800-1200 range)
- min_words: 500

With proper sections, chunker may need adjustment:
- Smaller sections might not need chunking at all
- Some sections may still be large enough for 2 chunks

## Requirements

### Functional
- Evaluate if chunker still needed for most sections
- Adjust config if needed for optimal lesson sizes
- Maintain 3 lesson types per chunk

### Non-Functional
- Target lesson word counts: concept (~800), deep_dive (~1000), quiz (~600)
- Avoid over-fragmentation of topics

## Analysis

### Scenario A: Section = Lesson (No Chunking)
If sections are 500-2000 words, could map 1 section → 1 lesson group.

**Pros:**
- Simpler pipeline
- Semantic coherence
- Better titles

**Cons:**
- Some sections too large for single lesson
- Less granular progress

### Scenario B: Keep Chunking with Higher Threshold
Increase target_words to 2000, so only large sections get chunked.

**Pros:**
- Handles outlier large sections
- Maintains current structure

**Cons:**
- Added complexity

### Recommended: Hybrid Approach
```yaml
chunker:
  target_words: 2000    # Up from 1000
  tolerance: 0.25       # 1500-2500 range
  min_words: 800        # Up from 500
```

This means:
- Sections < 1500 words → 1 chunk
- Sections 1500-2500 words → 1 chunk
- Sections > 2500 words → 2+ chunks

## Related Code Files

### Files to Modify
| File | Changes |
|------|---------|
| `config.yaml` | Update chunker settings |
| `src/content/chunker.py` | May need title generation update |

### Files to Create
- None

### Files to Delete
- None

## Implementation Steps

### Step 1: Analyze Post-Fix Section Sizes
```bash
# After Phase 02, get section size distribution
sqlite3 data/feynman.db "
SELECT
  COUNT(*) as total,
  AVG(word_count) as avg,
  MIN(word_count) as min,
  MAX(word_count) as max
FROM (
  SELECT id, LENGTH(content_text) - LENGTH(REPLACE(content_text, ' ', '')) + 1 as word_count
  FROM sections
)
"
```

### Step 2: Update config.yaml
```yaml
chunker:
  target_words: 2000    # Increased from 1000
  tolerance: 0.25       # Increased from 0.20
  min_words: 800        # Increased from 500
```

### Step 3: Optional - Add Skip Logic for Small Sections
```python
# In chunker.py, consider adding:
def chunk_sections(sections, target=2000, tolerance=0.25, min_words=800):
    """Only chunk sections larger than target * (1 + tolerance)."""
    upper = int(target * (1 + tolerance))

    chunks = []
    for section in sections:
        words = len(section.content_text.split())

        if words <= upper:
            # Small section → single chunk
            chunks.append(Chunk(
                text=section.content_text,
                formulas=section.latex_formulas,
                word_count=words,
                section_ids=[section.id]
            ))
        else:
            # Large section → needs splitting
            # ... existing split logic
```

### Step 4: Re-chunk and Validate
```bash
python pipeline.py --stage chunk
# Check chunk sizes in DB
```

## Todo List

- [ ] Analyze section size distribution after Phase 02
- [ ] Update config.yaml chunker settings
- [ ] Consider skip logic for small sections
- [ ] Re-run chunker and validate output
- [ ] Check lesson count per chapter

## Success Criteria

1. Most sections produce 1 chunk (not 6-7)
2. Average chunk size: 1000-2000 words
3. No chunks smaller than 800 words
4. Lesson count more manageable (3-8 per chapter vs 18-21)

## Risk Assessment

| Risk | Impact | Mitigation |
|------|--------|------------|
| Some sections still too large | Medium | Keep splitting logic for large sections |
| Too few lessons overall | Low | Can adjust target_words down if needed |

## Next Steps

Proceed to Phase 04 to update lesson title generation.
