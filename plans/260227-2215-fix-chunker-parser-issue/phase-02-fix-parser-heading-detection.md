---
title: "Phase 02: Fix Parser Heading Detection"
phase: 2
status: pending
effort: 2h
---

# Phase 02: Fix Parser Heading Detection

## Overview

Implement recursive heading search in parser to detect h2/h3 headings regardless of nesting depth.

## Context Links

- Main plan: [plan.md](plan.md)
- Phase 01 findings: [reports/phase-01-html-analysis.md](reports/phase-01-html-analysis.md)
- Target file: `src/crawler/parser.py`

## Key Insights

From Phase 01 analysis, headings are likely nested in:
- `<div class="section">` wrappers
- `<section>` elements
- Other container elements

Current code only checks `content.children` (direct children).

## Requirements

### Functional
- Detect ALL h2/h3 headings in content div, regardless of nesting
- Preserve section ordering (document order)
- Handle edge cases (empty sections, consecutive headings)

### Non-Functional
- Maintain backward compatibility with existing tests
- Performance: no significant slowdown on large chapters

## Architecture

### Current Implementation (BROKEN)
```python
# parser.py:103
for el in content.children:  # Direct children only
    if el.name in HEADING_TAGS:
        # Start new section
```

### Fixed Implementation
```python
# Option 1: Use find_all with recursive=True (default)
def extract_sections(soup: BeautifulSoup) -> list[dict]:
    content = _find_content_div(soup)
    if not content:
        return []

    # Get ALL headings in document order
    all_headings = content.find_all(HEADING_TAGS)

    sections = []
    for i, heading in enumerate(all_headings):
        # Get content between this heading and next
        section_elements = _get_elements_between(heading, all_headings[i+1] if i+1 < len(all_headings) else None)
        sections.append({
            "number": i + 1,
            "title": heading.get_text(strip=True),
            "elements": section_elements,
            "text_parts": [_element_text(el) for el in section_elements]
        })

    return sections
```

## Related Code Files

### Files to Modify
| File | Changes |
|------|---------|
| `src/crawler/parser.py` | Replace `extract_sections()` function |

### Files to Create
- None (modification only)

### Files to Delete
- None

## Implementation Steps

### Step 1: Add Helper Function
```python
def _get_elements_between(start: Tag, end: Optional[Tag]) -> list[Tag]:
    """Get all block elements between start heading and end heading."""
    elements = []
    current = start.next_sibling

    while current:
        if end and current == end:
            break
        if isinstance(current, Tag):
            if current.name in HEADING_TAGS:
                break  # Stop at any heading
            if current.name in BLOCK_TAGS:
                elements.append(current)
        current = current.next_sibling

    return elements
```

### Step 2: Rewrite extract_sections()
```python
def extract_sections(soup: BeautifulSoup) -> list[dict]:
    """Split content into sections by h2/h3 headings (recursive search)."""
    content = _find_content_div(soup)
    if not content:
        log.warning("No content container found; using full document body")
        content = soup

    # Find ALL h2/h3 headings in document order
    all_headings = content.find_all(list(HEADING_TAGS))

    if not all_headings:
        # No headings found - return single section with all content
        return [{
            "number": 1,
            "title": "Full Chapter",
            "elements": [el for el in content.find_all(BLOCK_TAGS)],
            "text_parts": [_element_text(el) for el in content.find_all(BLOCK_TAGS)]
        }]

    sections = []

    # Handle content before first heading (introduction)
    first_heading = all_headings[0]
    intro_elements = _get_elements_before(first_heading, content)
    if intro_elements:
        sections.append({
            "number": 0,
            "title": "Introduction",
            "elements": intro_elements,
            "text_parts": [_element_text(el) for el in intro_elements]
        })

    # Create sections from headings
    for i, heading in enumerate(all_headings):
        next_heading = all_headings[i + 1] if i + 1 < len(all_headings) else None
        section_elements = _get_elements_between(heading, next_heading)

        sections.append({
            "number": len(sections) + 1,
            "title": heading.get_text(strip=True),
            "elements": section_elements,
            "text_parts": [_element_text(el) for el in section_elements]
        })

    return sections
```

### Step 3: Add _get_elements_before Helper
```python
def _get_elements_before(first_heading: Tag, content: Tag) -> list[Tag]:
    """Get block elements before the first heading."""
    elements = []
    for el in content.children:
        if el == first_heading:
            break
        if isinstance(el, Tag) and el.name in BLOCK_TAGS:
            elements.append(el)
    return elements
```

### Step 4: Test Locally
```bash
# Run parser on single chapter to verify
python -c "
import asyncio
from src.utils import load_config
from src.crawler.parser import run_parser

config = load_config()
asyncio.run(run_parser(config))
"
```

## Todo List

- [ ] Add `_get_elements_between()` helper function
- [ ] Add `_get_elements_before()` helper function
- [ ] Rewrite `extract_sections()` to use `find_all()`
- [ ] Test on sample chapters
- [ ] Verify section count increases
- [ ] Check for edge cases (empty sections, etc.)

## Success Criteria

1. Parser detects all h2/h3 headings regardless of nesting
2. Section count increases from 94 to 300+ (3-8 per chapter)
3. No regressions in existing functionality
4. LaTeX formulas still extracted correctly
5. Image references still mapped correctly

## Risk Assessment

| Risk | Impact | Mitigation |
|------|--------|------------|
| Some headings in nav/footer | Low | Scope search to content div only |
| Empty sections from consecutive headings | Medium | Filter empty sections in post-processing |
| Performance on large chapters | Low | BeautifulSoup is efficient |

## Security Considerations

- No external input changes (still reading from crawled HTML)
- No API keys or credentials involved

## Next Steps

After parser fix validated, proceed to Phase 03 to optimize chunker config.
