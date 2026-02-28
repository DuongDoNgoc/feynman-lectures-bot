---
title: "Phase 04: Update Lesson Generation"
phase: 4
status: completed
effort: 1h
completed: 2026-02-28
---

# Phase 04: Update Lesson Generation

## Overview

Improve lesson titles and sequence generation after parser/chunker fixes.

## Context Links

- Main plan: [plan.md](plan.md)
- Chunker code: `src/content/chunker.py`
- DB module: `src/knowledge/db.py`

## Key Insights

Current lesson titles: "Chunk 1 — concept" (generic)

Desired lesson titles: "Ch1-2: Conservation of Energy — concept" (meaningful)

Need to:
1. Include chapter info in title
2. Include section title in title
3. Better sequence numbering

## Requirements

### Functional
- Lesson titles include chapter number, section number, and section title
- Format: "Ch{chapter}-{section}: {section_title} — {lesson_type}"
- Sequence tracks within chapter, not globally

### Non-Functional
- Titles should be human-readable
- Max title length: ~100 chars

## Related Code Files

### Files to Modify
| File | Changes |
|------|---------|
| `src/content/chunker.py` | Update title generation in `run_chunker()` |
| `src/knowledge/db.py` | May need query updates for section info |

### Files to Create
- None

### Files to Delete
- None

## Implementation Steps

### Step 1: Update Chunk Data Structure
```python
# chunker.py - Add chapter info to Chunk
@dataclass
class Chunk:
    text: str
    formulas: list = field(default_factory=list)
    word_count: int = 0
    section_ids: list = field(default_factory=list)
    # New fields
    chapter_number: int = 0
    chapter_title: str = ""
    section_number: int = 0
    section_title: str = ""
```

### Step 2: Update chunk_sections()
```python
def chunk_sections(sections: list[Section], ...) -> list[Chunk]:
    # ... existing logic ...

    for section in sections:
        # ... chunk creation ...

        # Populate new fields
        chunk.chapter_number = section.chapter_number  # Need to add to Section model
        chunk.chapter_title = section.chapter_title
        chunk.section_number = section.number
        chunk.section_title = section.title
```

### Step 3: Update run_chunker() Title Generation
```python
# chunker.py:run_chunker()
for seq, chunk in enumerate(chunks):
    anchor_section_id = chunk.section_ids[0] if chunk.section_ids else 0

    # Build meaningful title
    if chunk.section_title and chunk.chapter_number:
        title = f"Ch{chunk.chapter_number}-{chunk.section_number}: {chunk.section_title[:50]} — {lesson_type}"
    else:
        title = f"Chunk {seq + 1} — {lesson_type}"

    lesson = Lesson(
        id=None,
        section_id=anchor_section_id,
        lesson_type=lesson_type,
        sequence=seq,
        title=title,  # New meaningful title
        content_enhanced=chunk.text,
        enhancement_status="pending",
    )
```

### Step 4: Update Section Model (if needed)
```python
# models.py - Add chapter info to Section
@dataclass
class Section:
    id: Optional[int]
    chapter_id: int
    number: int
    title: str
    content_text: str
    latex_formulas: list = field(default_factory=list)
    image_refs: list = field(default_factory=list)
    parsed_at: Optional[str] = None
    # New fields (populated from join query)
    chapter_number: int = 0
    chapter_title: str = ""
```

### Step 5: Update DB Query
```python
# db.py - Update get_all_sections() to include chapter info
async def get_all_sections() -> list[Section]:
    async with get_db() as db:
        cursor = await db.execute("""
            SELECT s.*, c.number as chapter_number, c.title as chapter_title
            FROM sections s
            JOIN chapters c ON s.chapter_id = c.id
            ORDER BY c.number, s.number
        """)
        rows = await cursor.fetchall()
        # ... map to Section with chapter info ...
```

## Todo List

- [ ] Update Chunk dataclass with chapter/section info
- [ ] Update Section model (optional, or use dict)
- [ ] Update chunk_sections() to populate new fields
- [ ] Update run_chunker() title generation
- [ ] Update db.py query if needed
- [ ] Test title generation

## Success Criteria

1. Lesson titles follow format: "Ch{N}-{M}: {Title} — {type}"
2. Titles are meaningful and searchable
3. Sequence numbers track within chapter
4. No regression in lesson delivery

## Example Output

Before:
```
Lesson 1: "Chunk 1 — concept"
Lesson 2: "Chunk 1 — deep_dive"
Lesson 3: "Chunk 1 — quiz"
Lesson 4: "Chunk 2 — concept"
```

After:
```
Lesson 1: "Ch1-1: Introduction — concept"
Lesson 2: "Ch1-1: Introduction — deep_dive"
Lesson 3: "Ch1-1: Introduction — quiz"
Lesson 4: "Ch1-2: Conservation of Energy — concept"
```

## Risk Assessment

| Risk | Impact | Mitigation |
|------|--------|------------|
| Section titles too long | Low | Truncate to 50 chars |
| DB query performance | Low | Indexes already exist on chapter_id |

## Next Steps

Proceed to Phase 05 for testing and validation.
