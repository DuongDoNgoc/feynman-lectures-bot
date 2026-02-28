# Phase 1: Investigation Report

## Data Inventory

### Markdown Tables (`|---|`)
- **Count**: 9 lessons
- **All approved**: yes
- **Lesson IDs**: L5305, L5309, L5312, L5313, L5317, L5323, L5326, L5329, L5363
- **Types**: 5 concept, 3 deep_dive, 1 quiz
- **8 of 9** already have non-empty `math_images_json` (formula blocks coexist)

### LaTeX Tabular (`\begin{tabular}`)
- **Count**: 0 lessons. Not present in any `content_enhanced`.

### LaTeX Array (`\begin{array}`)
- **Count**: 6 lessons (L5695, L5696, L5697 + 3 others)
- **Context**: all inside `\begin{equation}...\end{equation}` wrappers
- **Already handled**: formula renderer's display pattern `\[...\]` / `$$...$$` captures the outer equation environment. The `\begin{array}` inside renders correctly via pdflatex.
- **Conclusion**: no action needed.

## Table Format Analysis

Sample from L5305:
```
| Khai niem | Y nghia |
|---|---|
| **Boc hoi** | Phan tu co nang luong cao nhat thoat khoi be mat |
| **Can bang dong** | Toc do bay ra = toc do tro ve |
```

Characteristics:
- Standard GitHub-flavored Markdown tables
- Vietnamese text with bold (`**...**`) inside cells
- 2-4 columns typically
- 3-10 rows typically
- No colspan/rowspan
- Separator row always uses `|---|` pattern (no `:---:` alignment seen)

## Rendering Pipeline Analysis

### Current flow (`render_lesson_math`)
1. `_extract_formula_positions(content)` -> list of `{start, end, formula, hash}`
2. `_group_nearby_formulas(formulas, content)` -> groups within 300 chars
3. For each group: render single (pdflatex) or combined (xelatex)
4. Returns `blocks: list[dict]` with `{type, path, start, end}`

### Delivery flow (`_build_interleaved_segments`)
1. Takes `content` string + `blocks` list
2. Sorts blocks by `start` position
3. Iterates: text before block -> image -> advance cursor
4. **Type-agnostic**: only uses `start`, `end`, `path` keys. The `type` field is informational.
5. `_coalesce_segments` merges consecutive short text segments

### Key insight
`_build_interleaved_segments` does NOT check `block["type"]`. Adding `type: "table"` blocks requires zero changes to handlers.py.

## DB Schema

```
lessons.math_images_json  TEXT DEFAULT NULL
```
- Stores JSON: `[{type, path, start, end}, ...]`
- Updated via `db.update_lesson_content(lesson)` which writes `lesson.math_images_json`
- Queried via `db.get_approved_lessons_needing_render()` -- checks `math_images_json IS NULL OR = '[]' OR = ''`

**Backfill concern**: The 9 table lessons already have `math_images_json` with formula blocks. `get_approved_lessons_needing_render()` will NOT pick them up. Backfill script must query directly and merge table blocks into existing block list.

## Rendering Strategy

### Markdown-to-LaTeX conversion
Convert pipe-delimited table to `\begin{tabular}` with proper column spec.

Example input:
```
| Col A | Col B |
|---|---|
| cell 1 | cell 2 |
```

Example output:
```latex
\begin{tabular}{|l|l|}
\hline
\textbf{Col A} & \textbf{Col B} \\
\hline
cell 1 & cell 2 \\
\hline
\end{tabular}
```

### Engine choice
Use **xelatex** (not pdflatex) because:
- Table cells contain Vietnamese text (UTF-8)
- Same engine already used for combined blocks
- `fontspec` + DejaVu Serif handles Vietnamese

### Template
Reuse `XELATEX_TEMPLATE` with `minipage{12cm}` to constrain width. Tables naturally fit within this.

### Cache key
Hash the raw markdown table text -> filename `tbl_{hash}.png`. Analogous to `cb_{hash}.png` for combined blocks.

## Regex for Table Detection

Pattern to match a complete markdown table:
```python
TABLE_PATTERN = r'(?:^|\n)((?:\|[^\n]+\|\n)(?:\|[-:| ]+\|\n)(?:\|[^\n]+\|\n?)+)'
```

Explanation:
- Starts with a header row: `|...|`
- Followed by separator row: `|---|---|`
- Followed by 1+ data rows: `|...|`
- Each row ends with `\n` (last row optionally)

This matches all 9 samples found in the DB.
