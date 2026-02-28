# Code Review: Parser & Chunker Section Detection Fix

**Date:** 2026-02-28
**Branch:** `fix/chunker-parser-section-detection`
**Reviewer:** code-reviewer

## Scope

- Files: `src/crawler/parser.py`, `src/content/chunker.py`, `src/knowledge/models.py`, `src/knowledge/db.py`, `config.yaml`
- Focus: correctness, edge cases, potential bugs
- Dependents checked: `math_renderer.py`, `preview_db.py`, `preview_exporter.py`

## Overall Assessment

Solid improvement. The switch from `content.children` (direct children only) to `find_all()` (recursive) correctly handles headings nested inside `<div class="section">` wrappers. The per-chapter chunking and metadata propagation are well-structured. Several edge cases need attention.

---

## Critical Issues

None found.

---

## High Priority

### 1. `_collect_between_headings` parent-check logic is a dead branch (parser.py:191-196)

```python
if parent and parent.name not in ("body", "html", "[document]") and parent.name != "div" or (
    parent and parent.get("class") and "section" in parent.get("class", [])
):
    pass
```

**Problem:** This entire block is a no-op (`pass`). But worse, the boolean logic is wrong due to operator precedence. The expression evaluates as:

```
(parent and name not in (...) and name != "div") or (parent and has class "section")
```

This means when the heading IS inside a `div.section` wrapper, the condition is True and... does nothing. When the heading is in a non-div, non-body container (e.g., `<section>`, `<article>`), it also does nothing.

**Real risk:** If a heading is inside a wrapper like `<div class="section">`, `next_sibling` only walks siblings within that div. Content in the next sibling div of the parent is never collected. The `pass` block was presumably meant to handle this case by walking parent siblings.

**Impact:** Sections inside wrapper divs may have truncated content -- only text within the same wrapper div is captured, content in subsequent parent siblings is lost.

**Fix:** Either implement the parent-sibling walking or, if the current `find_all()` approach makes this unnecessary, remove the dead code entirely to avoid confusion. If the Feynman Lectures HTML consistently nests each heading+content within a single `div.section`, the current approach works. But this should be verified.

### 2. `_collect_text_before` double-counting nested block elements (parser.py:144-158)

```python
for el in content.descendants:
    if el is first_heading:
        break
    if isinstance(el, Tag) and el.name in BLOCK_TAGS:
        if first_heading in el.descendants:
            continue
        text = _element_text(el)
```

**Problem:** Walking `descendants` visits both parent and child elements. If you have `<div><p>text</p></div>`, both the `<div>` and the `<p>` are visited. Both are in `BLOCK_TAGS`. The `<div>` will emit "text" and then the `<p>` will also emit "text" -- duplicating content.

**Fix:** Skip block elements that contain other block elements, or use `find_all(BLOCK_TAGS, recursive=True)` with a filter that only picks leaf-level blocks:

```python
def _collect_text_before(first_heading, content):
    parts = []
    for el in content.descendants:
        if el is first_heading:
            break
        if isinstance(el, Tag) and el.name in BLOCK_TAGS:
            if first_heading in el.descendants:
                continue
            # Skip if contains nested block elements
            if el.find(list(BLOCK_TAGS)):
                continue
            text = _element_text(el)
            if text:
                parts.append(text)
    return parts
```

### 3. `groupby` requires pre-sorted input (chunker.py:87-89)

```python
from itertools import groupby
sections_by_chapter = {
    k: list(g) for k, g in groupby(sections, key=lambda s: s.chapter_id)
}
```

**Problem:** `itertools.groupby` only groups **consecutive** elements with the same key. The `get_all_sections()` query orders by `c.number, s.number`, which should produce sections sorted by chapter -- but `chapter_id` and `c.number` are different columns. If chapter IDs are non-sequential (e.g., after deletions/re-inserts), `chapter_id` ordering may not match `c.number` ordering, causing a single chapter to be split into multiple groups.

**Impact:** A chapter's sections could be chunked separately, producing fragmented chunks.

**Fix:** Either sort by `chapter_id` in the SQL query, or sort the sections list before groupby:

```python
sections_sorted = sorted(sections, key=lambda s: s.chapter_id)
sections_by_chapter = {
    k: list(g) for k, g in groupby(sections_sorted, key=lambda s: s.chapter_id)
}
```

---

## Medium Priority

### 4. `chunk_sections` default params diverge from config (chunker.py:22-26)

```python
def chunk_sections(
    sections: list[Section],
    target: int = 1000,      # config says 2000
    tolerance: float = 0.20, # config says 0.25
    min_words: int = 500,    # config says 800
) -> list[Chunk]:
```

**Problem:** The function signature defaults (`1000/0.20/500`) are stale vs the config values (`2000/0.25/800`). If `chunk_sections` is ever called without explicit params (e.g., in tests, from another module), it will use the old behavior.

**Fix:** Update defaults to match config, or remove defaults to force explicit params.

### 5. Section numbering skips on empty sections (parser.py:228-252)

```python
for i, raw in enumerate(sections_raw):
    ...
    if not content_text.strip():
        continue  # skip empty sections
    section = Section(
        ...
        number=i + 1,
        ...
    )
```

**Problem:** If section 2 is empty and skipped, section numbers go 1, 3, 4... This creates gaps in `section.number`. Combined with the intro section (number=0), and `extract_sections` using `len(sections) + 1` for numbering, the numbering semantics are inconsistent.

**Impact:** The `section_number` shown in chunk titles (`Ch1-2: ...`) may not correspond to the actual heading position, confusing users.

### 6. Intro section has empty `elements` list (parser.py:122-128)

```python
sections.append({
    "number": 0,
    "title": "Introduction",
    "elements": [],  # <-- always empty
    "text_parts": intro_parts,
})
```

**Impact:** Image extraction in `parse_chapter` iterates `raw["elements"]` to find `<img>` tags. Intro sections will never have images extracted, even if the intro HTML contains images.

### 7. Merge logic merges ALL small chunks, not just trailing (chunker.py:57-66)

The docstring says "merge small **trailing** sections" but the code merges ANY chunk below `min_words` into the previous one:

```python
for chunk in chunks:
    if chunk.word_count < min_words and merged:
        prev = merged[-1]
        prev.text += chunk.text
        ...
```

This means a small chunk in the middle of a chapter gets absorbed into its predecessor, potentially creating an oversized chunk. This is probably acceptable behavior, but the docstring is misleading.

---

## Low Priority

### 8. `chapter_title` on Section model is populated but never used

`Section.chapter_title` is set via the JOIN in `get_all_sections()` but is never read anywhere in the codebase. Not harmful, but unnecessary data transfer.

### 9. No test coverage

No test files found in the repository. These parsing and chunking changes are the kind most prone to regressions.

---

## Positive Observations

- Per-chapter chunking prevents cross-chapter content mixing -- good design
- `_build_chunk_title` produces human-readable titles (`Ch1-2: Matter is made of atoms`)
- The `with_chapter` param on `_row_to_section` is a clean opt-in pattern
- Defensive `getattr(section, "chapter_number", 0)` in chunker handles sections without chapter metadata
- The `find_all(list(HEADING_TAGS))` approach is more robust than walking direct children

---

## Recommended Actions (Priority Order)

1. **Fix groupby pre-sort** (issue #3) -- most likely to cause real bugs silently
2. **Fix or remove dead parent-sibling code** (issue #1) -- verify against actual HTML, then either implement or delete
3. **Fix double-counting in `_collect_text_before`** (issue #2) -- depends on actual HTML structure
4. **Update `chunk_sections` defaults** (issue #4) -- quick fix
5. **Add intro `elements` population** (issue #6) -- if intro images matter
6. **Add basic tests** for `extract_sections` and `chunk_sections` -- prevent regressions

---

## Unresolved Questions

1. What does the actual Feynman Lectures HTML structure look like? Are headings inside `div.section` wrappers or direct children of the content div? This determines severity of issues #1 and #2.
2. Is `section.id` always populated when `chunk_sections` runs? The `section_ids` list appends `section.id` which could be `None` if sections come from parsing rather than DB.
3. Should the chunker deduplicate lessons on re-run? Currently `run_chunker` inserts new lessons every time without checking for existing ones.
