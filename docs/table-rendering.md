# Table Rendering Feature

## Overview

The renderer now detects and converts markdown tables in lesson content to PNG images for Telegram delivery. Tables are rendered alongside LaTeX formulas using the same unified block dictionary format.

## Features

- **Markdown Detection**: Tables identified via regex pattern (header | separator | rows)
- **LaTeX Conversion**: Markdown tables converted to LaTeX tabular environment
- **UTF-8 Support**: xelatex + fontspec (DejaVu Serif) for Vietnamese text in tables
- **MD5 Caching**: Same table → reuse PNG (no re-rendering)
- **Unified Delivery**: Handlers generically handle `type: "table"` blocks (no special code needed)
- **Per-Lesson Cap**: Max 20 tables per lesson

## Block Dictionary Format

Tables stored in `lessons.math_images_json` with same structure as formula blocks:

```json
{
  "type": "table",
  "path": "data/images/tbl_abc123def456.png",
  "start": 450,
  "end": 700
}
```

**Fields**:
- `type`: Always `"table"`
- `path`: Full path to rendered PNG (with `tbl_` prefix)
- `start`, `end`: Character positions in original content (for segmentation during delivery)

## Implementation Details

### Markdown Table Pattern

Regex pattern matches: header row + separator row (contains `---`) + 1+ data rows

```python
TABLE_PATTERN = r'(?:^|\n)((?:\|[^\n]+\|\n)(?:\|[ |:-]*---[ |:-]*\|\n)(?:\|[^\n]+\|\n?)+)'
```

Example markdown table:
```
| Column 1 | Column 2 |
|----------|----------|
| Data A   | Data B   |
| Data C   | Data D   |
```

### Markdown to LaTeX Conversion

Function: `_markdown_table_to_latex(md_table: str) -> str | None`

**Process**:
1. Parse header row (first `|`-delimited line)
2. Skip separator row (contains `---` and pipes)
3. Parse all data rows
4. **Escape LaTeX special characters** in cells:
   - `$` → `\$` (not LaTeX math)
   - `&` → `\&` (tabular column separator)
   - `%` → `\%` (comment char)
   - `#` → `\#` (macro char)
   - `_` → `\_` (subscript)
5. **Convert markdown formatting** (after escaping):
   - `**text**` → `\textbf{text}` (bold)
   - `*text*` → `\textit{text}` (italic)
6. Build LaTeX tabular with:
   - Column spec: `|l|l|...|` (left-aligned)
   - Header row: bold cells separated by `&`
   - Data rows: cells separated by `&`
   - Horizontal lines: `\hline` after header and end

**Output Example**:
```latex
\begin{tabular}{|l|l|}
\hline
\textbf{Column 1} & \textbf{Column 2} \\
\hline
Data A & Data B \\
Data C & Data D \\
\hline
\end{tabular}
```

### Rendering Function

Function: `render_table(table_text: str, output_dir: str, dpi: int = 200) -> str | None`

**Cache Check**:
1. Hash table text: `md5_hash = hashlib.md5(table_text.encode()).hexdigest()[:12]`
2. Check for existing PNG: `data/images/tbl_{md5_hash}.png`
3. If exists, return path (skip rendering)

**Rendering Process**:
1. Convert markdown to LaTeX tabular via `_markdown_table_to_latex()`
2. Wrap in `XELATEX_TABLE_TEMPLATE` (no minipage — tabular uses natural width)
3. Write temporary `.tex` file
4. Run `xelatex -interaction=nonstopmode` → `.pdf`
5. Run `pdftoppm -png -r {dpi}` → `.png`
6. Copy PNG to output directory with `tbl_` prefix
7. Return PNG path

**Template**:
```latex
\documentclass[border=4pt]{standalone}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{fontspec}
\setmainfont{DejaVu Serif}
\usepackage{xcolor}
\begin{document}
\color{black}
{content}
\end{document}
```

**Why no minipage?** Unlike formula blocks, tabular environments have specific width requirements and benefit from natural width based on column content. minipage would constrain width unnecessarily.

### Integration with `render_lesson_math()`

The main rendering function processes both formulas and tables:

```python
def render_lesson_math(lesson: Lesson, output_dir: str, dpi: int = 150) -> list[dict]:
    """Render formulas and tables from lesson content.

    Returns: List of mixed block dicts (type: "single" | "combined" | "table")
    """
    # 1. Extract and render formulas (existing logic)
    formulas = _extract_formula_positions(lesson.content_enhanced)
    groups = _group_nearby_formulas(formulas, lesson.content_enhanced)
    blocks = []  # formula blocks appended here

    # 2. Extract and render tables
    tables = _extract_table_positions(lesson.content_enhanced)
    for tbl in tables[:20]:  # cap at 20 tables per lesson
        path = render_table(tbl["table_text"], output_dir, dpi)
        if path:
            blocks.append({
                "type": "table",
                "path": path,
                "start": tbl["start"],
                "end": tbl["end"],
            })

    # 3. Re-sort all blocks (formulas + tables) by position
    blocks.sort(key=lambda b: b["start"])
    return blocks
```

## Usage

### Manual Rendering

Tables are automatically detected and rendered during the normal pipeline:

```bash
python pipeline.py --stage render
```

### Backfill Existing Lessons

To add table blocks to approved lessons that weren't previously rendered with tables:

```bash
python scripts/backfill-tables.py
```

**What it does**:
1. Query for approved lessons containing markdown table markers (`|---|`)
2. Re-run `render_lesson_math()` for each lesson
3. Update `lessons.math_images_json` to include both formula and table blocks
4. Print summary: `L5: 3 formula blocks + 2 table blocks`

## Configuration

In `config.yaml`:

```yaml
renderer:
  output_dir: data/images/          # Where PNG images stored
  dpi: 1200                         # Resolution (1200 recommended)
  max_blocks_per_lesson: 50         # Cap on formula groups
  group_max_gap: 300                # Char distance for grouping formulas
```

**Table-specific limits**:
- **Per-lesson cap**: 20 tables (hardcoded in `render_lesson_math()`)
- **Cache**: MD5-based, no invalidation needed (same table → same PNG)

## Error Handling

If table rendering fails:
- `_markdown_table_to_latex()` returns `None` → table skipped with debug log
- `render_table()` returns `None` → table not added to blocks
- Handlers still deliver lesson content (fallback to raw markdown)

## Delivery via Telegram

Handlers treat table blocks generically (no special code needed):

```python
def _build_interleaved_segments(content: str, blocks: list[dict]) -> list[dict]:
    """Split content into text/image segments based on block positions.

    Handles type: "table", "single", "combined" identically.
    """
    for block in sorted_blocks:
        if os.path.exists(block["path"]):
            segments.append({"type": "image", "path": block["path"]})
```

Result: Tables delivered as PNG images between text segments, just like formula images.

## Example Lesson Flow

**Input markdown**:
```
This lesson covers the fundamental relationships:

| Quantity | Symbol | Unit |
|----------|--------|------|
| Energy   | E      | Joule |
| Force    | F      | Newton |

These are foundational concepts...
```

**Processing**:
1. Extract table positions: `start=88, end=180`
2. Convert to LaTeX tabular
3. Render with xelatex → `tbl_abc123.png`
4. Store block: `{type: "table", path: "data/images/tbl_abc123.png", start: 88, end: 180}`

**Delivery to Telegram**:
1. Text: "This lesson covers the fundamental relationships:"
2. Image: PNG of table
3. Text: "These are foundational concepts..."
