---
status: completed
completed: 2026-02-28
---

# Phase 2: Renderer Extension

## Goal
Add table detection and PNG rendering to `src/renderer/math_renderer.py`. Tables become blocks in `math_images_json` alongside formula blocks.

## Changes to `src/renderer/math_renderer.py`

### 2.1 Add table regex constant

After `INLINE_PATTERNS`, add:

```python
# Markdown table pattern: header row + separator row + 1+ data rows
TABLE_PATTERN = r'(?:^|\n)((?:\|[^\n]+\|\n)(?:\|[-:| ]+\|\n)(?:\|[^\n]+\|\n?)+)'
```

### 2.2 Add `_extract_table_positions(content)` function

After `_extract_formula_positions`:

```python
def _extract_table_positions(content: str) -> list[dict]:
    """Find all markdown tables with their text positions.
    Returns list of dicts: start, end, table_text, hash.
    """
    results = []
    for m in re.finditer(TABLE_PATTERN, content):
        table_text = m.group(1).strip()
        if table_text.count('|') >= 4:  # at least 2 columns
            results.append({
                "start": m.start(1),
                "end": m.end(1),
                "table_text": table_text,
                "hash": _formula_hash(table_text),
            })
    return results
```

### 2.3 Add `_markdown_table_to_latex(md_table)` converter

```python
def _markdown_table_to_latex(md_table: str) -> str:
    """Convert markdown table to LaTeX tabular environment."""
    lines = [l.strip() for l in md_table.strip().split('\n') if l.strip()]
    if len(lines) < 3:
        return None  # need header + separator + at least 1 data row

    def parse_row(line):
        cells = [c.strip() for c in line.strip('|').split('|')]
        return cells

    header = parse_row(lines[0])
    # Skip separator row (lines[1])
    data_rows = [parse_row(l) for l in lines[2:]]
    ncols = len(header)

    # Build column spec
    col_spec = '|' + '|'.join(['l'] * ncols) + '|'

    # Convert markdown bold to LaTeX bold
    def convert_cell(cell):
        cell = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', cell)
        cell = re.sub(r'\*(.+?)\*', r'\\textit{\1}', cell)
        # Escape LaTeX specials in plain text portions
        for ch in ['&', '%', '#', '_']:
            # Don't double-escape
            cell = re.sub(r'(?<!\\)' + re.escape(ch), '\\' + ch, cell)
        return cell

    parts = []
    parts.append(f'\\begin{{tabular}}{{{col_spec}}}')
    parts.append('\\hline')
    parts.append(' & '.join(f'\\textbf{{{convert_cell(h)}}}' for h in header) + ' \\\\')
    parts.append('\\hline')
    for row in data_rows:
        # Pad or truncate to match header column count
        cells = (row + [''] * ncols)[:ncols]
        parts.append(' & '.join(convert_cell(c) for c in cells) + ' \\\\')
    parts.append('\\hline')
    parts.append('\\end{tabular}')

    return '\n'.join(parts)
```

### 2.4 Add `render_table()` function

After `render_combined_block`:

```python
def render_table(table_text: str, output_dir: str, dpi: int = 200) -> str | None:
    """Render a markdown table as PNG using xelatex. Returns png_path or None."""
    latex_table = _markdown_table_to_latex(table_text)
    if not latex_table:
        return None

    thash = _formula_hash(table_text)
    png_path = os.path.join(output_dir, f"tbl_{thash}.png")
    if os.path.exists(png_path):
        return png_path  # cache hit

    if not HAS_XELATEX or not HAS_PDFTOPPM:
        log.warning("xelatex/pdftoppm not available for table rendering")
        return None

    os.makedirs(output_dir, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmpdir:
        tex_file = os.path.join(tmpdir, "table.tex")
        pdf_file = os.path.join(tmpdir, "table.pdf")
        png_stem = os.path.join(tmpdir, "table")

        with open(tex_file, "w", encoding="utf-8") as f:
            f.write(XELATEX_TEMPLATE % latex_table)

        subprocess.run(
            ["xelatex", "-interaction=nonstopmode", "-output-directory", tmpdir, tex_file],
            capture_output=True, timeout=30,
        )
        if not os.path.exists(pdf_file):
            log.debug("xelatex failed for table %s", thash)
            return None

        subprocess.run(
            ["pdftoppm", "-png", "-singlefile", "-r", str(dpi), pdf_file, png_stem],
            capture_output=True, timeout=15,
        )
        tmp_png = png_stem + ".png"
        if not os.path.exists(tmp_png):
            log.debug("pdftoppm failed for table %s", thash)
            return None

        import shutil as sh
        sh.copy2(tmp_png, png_path)

    return _ensure_min_size(png_path)
```

### 2.5 Integrate into `render_lesson_math()`

Modify `render_lesson_math` to also extract and render tables, merging them into the block list.

After the formula extraction + rendering loop, before `return blocks`:

```python
    # --- Table rendering ---
    tables = _extract_table_positions(lesson.content_enhanced)
    for tbl in tables[:20]:  # cap tables per lesson
        path = render_table(tbl["table_text"], output_dir, dpi)
        if path:
            blocks.append({
                "type": "table",
                "path": path,
                "start": tbl["start"],
                "end": tbl["end"],
            })

    # Re-sort all blocks (formulas + tables) by position
    blocks.sort(key=lambda b: b["start"])

    return blocks
```

**Important**: move `return blocks` after the table section. The existing `return blocks` at the end of the function becomes the single return point.

## Testing Strategy

1. **Unit test `_markdown_table_to_latex`**: feed the 3 distinct table formats from DB samples, verify LaTeX output compiles
2. **Unit test `_extract_table_positions`**: verify correct start/end positions on sample content
3. **Integration test**: call `render_table` on a simple 2x2 table, verify PNG exists and is readable
4. **Manual QA**: use `scripts/test-interleaved.py` with a table lesson (e.g., L5305) to verify Telegram delivery

## Edge Cases

| Case | Handling |
|------|----------|
| Table overlaps with formula block positions | Unlikely (tables are plain text, formulas are `$...$`). If overlap occurs, both blocks render; `_build_interleaved_segments` processes them in order. |
| Very wide table (>4 columns) | `minipage{12cm}` constrains width. For >5 columns consider `tabularx` with `X` columns. Current data has max 3 columns, so not urgent. |
| Empty cells | `_markdown_table_to_latex` pads short rows with empty strings |
| Bold/italic in cells | Converted to `\textbf`/`\textit` |
| LaTeX-special chars in cells (`&`, `%`, `#`, `_`) | Escaped by `convert_cell()` |
