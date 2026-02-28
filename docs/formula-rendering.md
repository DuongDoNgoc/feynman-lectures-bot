# Formula Rendering System

Comprehensive guide to LaTeX formula rendering pipeline for Feynman Bot.

---

## Single vs. Combined Rendering Decision

```python
def should_combine(formulas: List[str], max_gap: int = 300) -> bool:
    """Decide whether to render as combined block or individual formulas."""
    if len(formulas) < 2:
        return False  # Single formula → pdflatex

    # Check character distance between nearby formulas
    for i in range(len(formulas) - 1):
        gap = get_char_distance(formulas[i], formulas[i+1])
        if gap <= max_gap:
            return True  # Within grouping threshold → xelatex

    return False  # Too far apart → individual pdflatex
```

---

## Rendering Function Signatures

### Single Formula

```python
async def render_with_pdflatex(formula: str, dpi: int) -> str:
    """Render single formula. Fast, high-quality. Returns PNG path."""
    # 1. Hash formula: md5_hash = hashlib.md5(formula.encode()).hexdigest()
    # 2. Check cache: if data/images/{md5_hash}.png exists, return path
    # 3. Write .tex file → pdflatex → pdftoppm → PNG
    # 4. Return path
```

### Combined Block

```python
async def render_with_xelatex(block_text: str, dpi: int) -> str:
    """Render combined block with UTF-8 support (DejaVu Serif).

    Returns PNG path with cb_ prefix (cb_abc123def456.png).
    """
    # 1. Hash: md5_hash = hashlib.md5(block_text.encode()).hexdigest()
    # 2. Check cache: if data/images/cb_{md5_hash}.png exists, return
    # 3. Build template with fontspec + minipage(12cm)
    # 4. xelatex → PDF → pdftoppm → PNG
    # 5. Return path
```

---

## xelatex Template Pattern

```python
XELATEX_TEMPLATE = r"""
\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage{fontspec}
\setmainfont{DejaVu Serif}
\usepackage{amsmath,amssymb,amsfonts}
\pagestyle{empty}
\usepackage[margin=0.5cm]{geometry}
\begin{document}
\begin{minipage}{12cm}
{content}
\end{minipage}
\end{document}
"""
```

---

## Block Dictionary Structure

Store in `lessons.math_images_json` as JSON array:

```python
@dataclass
class RenderBlock:
    type: str  # "single" or "combined"
    path: str  # "data/images/abc123.png" or "data/images/cb_abc123.png"
    start: int  # Character position in original content
    end: int    # Character position in original content
```

---

## Grouping Logic Implementation

```python
def _group_nearby_formulas(
    formulas: List[Tuple[str, int, int]],
    content: str,
    max_gap: int = 300
) -> List[List[int]]:
    """Group nearby formulas into blocks.

    Args:
        formulas: List of (text, start, end) tuples
        content: Original lesson content
        max_gap: Max char distance to group (default 300)

    Returns:
        List of groups, each group is list of formula indices
    """
    # Iterate through formulas; if gap to next < max_gap, same group
    # Otherwise, start new group
```

---

## Real LaTeX Filter Pattern

```python
def _is_real_latex(formula: str) -> bool:
    """Filter out false positives (plain text, single var, etc)."""

    # Reject: single variable, numbers, abbreviations
    if formula in SINGLE_VAR_CACHE or formula.isdigit():
        return False

    # Reject: plain text without operators
    latex_operators = {
        r'\alpha', r'\beta', r'\int', r'\sum', r'\frac',
        r'\sqrt', r'\sin', r'\cos', '^', '_', '=', '+'
    }

    if not any(op in formula for op in latex_operators):
        return False

    return True
```

---

## Configuration Keys

In `config.yaml`:

```yaml
renderer:
  output_dir: data/images/
  dpi: 1200
  max_blocks_per_lesson: 50       # Cap on formula groups
  group_max_gap: 300              # Char distance for grouping formulas
```

---

## Filename Convention

- **Single formula**: `{md5(formula)}.png`
  - Example: `a1b2c3d4e5f6g7h8.png`

- **Combined block**: `cb_{md5(block_text)}.png`
  - Example: `cb_x9y8z7w6v5u4t3.png`

- **Table**: `tbl_{md5(table_text)}.png`
  - Example: `tbl_m9n8o7p6q5r4s3.png`

---

## Related Features

- **Table Rendering**: See [Table Rendering Feature](./table-rendering.md)
  - Tables detected via `_extract_table_positions()` using regex pattern
  - Markdown → LaTeX conversion via `_markdown_table_to_latex()`
  - PNG rendering via `render_table()` using xelatex
  - Block dictionary format: `{type: "table", path: "tbl_*.png", start, end}`

---

## Caching Strategy

All formulas and tables cached by MD5 hash to avoid re-rendering:

```
First render:  formula → MD5 → /data/images/{hash}.png
Subsequent:    formula → MD5 → check cache → instant return
```

Delete PNG files in `data/images/` if DPI config changes to force re-render.
