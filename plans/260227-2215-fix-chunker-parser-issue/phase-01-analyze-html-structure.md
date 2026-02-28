---
title: "Phase 01: Analyze HTML Structure"
phase: 1
status: pending
effort: 1h
---

# Phase 01: Analyze HTML Structure & Nested Heading Detection

## Overview

Investigate actual HTML structure from crawled chapters to understand why h3 headings aren't detected.

## Context Links

- Main plan: [plan.md](plan.md)
- Parser code: `src/crawler/parser.py`
- Sample data: `data/raw/` (if HTML cached)

## Requirements

### Functional
- Identify actual HTML nesting pattern for h2/h3 headings
- Determine if headings are in direct children or nested in divs/sections
- Document findings for Phase 02 implementation

### Non-Functional
- Analysis should cover at least 3 different chapters
- Document any variations in HTML structure between chapters

## Implementation Steps

### Step 1: Locate Sample HTML
```bash
# Check if raw HTML is stored in database or filesystem
ls -la data/raw/
sqlite3 data/feynman.db "SELECT volume, number, length(raw_html) FROM chapters LIMIT 3"
```

### Step 2: Extract Sample HTML
```python
# Extract one chapter's HTML for analysis
import sqlite3
conn = sqlite3.connect('data/feynman.db')
cur = conn.execute("SELECT raw_html FROM chapters WHERE volume='I' AND number=1")
html = cur.fetchone()[0]
# Save to temp file for inspection
with open('temp_ch1.html', 'w') as f:
    f.write(html)
```

### Step 3: Analyze Heading Structure
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
content = soup.find(class_='content') or soup.find(id='content')

# Find all h2/h3 anywhere in content
all_h2 = content.find_all('h2') if content else []
all_h3 = content.find_all('h3') if content else []

# Find direct children only
direct_children = list(content.children) if content else []
direct_h2 = [c for c in direct_children if getattr(c, 'name', None) == 'h2']
direct_h3 = [c for c in direct_children if getattr(c, 'name', None) == 'h3']

print(f"All h2: {len(all_h2)}, Direct h2: {len(direct_h2)}")
print(f"All h3: {len(all_h3)}, Direct h3: {len(direct_h3)}")

# Check parent structure of h3 tags
for h3 in all_h3[:5]:
    print(f"h3 parent: {h3.parent.name}, text: {h3.get_text()[:50]}")
```

### Step 4: Document Findings

Create analysis report with:
- HTML structure diagram
- Heading nesting pattern
- Recommended fix approach

## Todo List

- [ ] Locate sample HTML (DB or filesystem)
- [ ] Extract 3+ chapter HTML samples
- [ ] Analyze h2/h3 nesting structure
- [ ] Identify why direct children check fails
- [ ] Document findings in reports/

## Success Criteria

1. Clear understanding of HTML structure
2. Confirmed root cause of heading detection failure
3. Documented recommendation for Phase 02

## Deliverables

- Analysis report in `reports/phase-01-html-analysis.md`
- Sample HTML snippets showing nesting pattern

## Next Steps

Proceed to Phase 02 with concrete understanding of HTML structure.
