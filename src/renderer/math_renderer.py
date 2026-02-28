"""LaTeX → PNG renderer using pdflatex + pdftoppm.

Features:
- Configurable DPI output (readable on Telegram mobile)
- Cache by MD5 hash of formula — no re-render
- Combined block rendering: groups nearby formulas into single images via xelatex
- Fallback to matplotlib mathtext if pdflatex unavailable
- Wraps render errors gracefully (broken formula → logged, skipped)
"""
import asyncio
import hashlib
import json
import logging
import os
import re
import shutil
import subprocess
import tempfile

from src.knowledge import db
from src.knowledge.models import Lesson

log = logging.getLogger(__name__)

# Template for single formulas (pdflatex)
LATEX_TEMPLATE = r"""\documentclass[border=4pt]{standalone}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{xcolor}
\begin{document}
\color{black}
%s
\end{document}
"""

# Template for combined blocks with Vietnamese text (xelatex + fontspec)
# minipage constrains width so long content wraps instead of producing extreme aspect ratios
XELATEX_TEMPLATE = r"""\documentclass[border=4pt]{standalone}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{fontspec}
\setmainfont{DejaVu Serif}
\usepackage{xcolor}
\begin{document}
\color{black}
\begin{minipage}{12cm}
%s
\end{minipage}
\end{document}
"""

# Template for tables — no minipage, tabular uses its natural width
XELATEX_TABLE_TEMPLATE = r"""\documentclass[border=4pt]{standalone}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{fontspec}
\setmainfont{DejaVu Serif}
\usepackage{xcolor}
\begin{document}
\color{black}
%s
\end{document}
"""

HAS_PDFLATEX = shutil.which("pdflatex") is not None
HAS_XELATEX = shutil.which("xelatex") is not None
HAS_PDFTOPPM = shutil.which("pdftoppm") is not None

# Formula extraction patterns
DISPLAY_PATTERNS = [
    r"\$\$(.*?)\$\$",          # display $$...$$
    r"\\\[(.*?)\\\]",          # display \[...\]
]
INLINE_PATTERNS = [
    r"\$((?:[^$\n]|\\.)+?)\$",   # inline $...$ (no newlines)
    r"\\\(((?:[^\n])*?)\\\)",    # inline \(...\) (no newlines)
]

# Markdown table: header row + separator row (must contain ---) + 1+ data rows
TABLE_PATTERN = r'(?:^|\n)((?:\|[^\n]+\|\n)(?:\|[ |:-]*---[ |:-]*\|\n)(?:\|[^\n]+\|\n?)+)'


def _formula_hash(formula: str) -> str:
    return hashlib.md5(formula.encode()).hexdigest()[:12]


def _is_real_latex(formula: str) -> bool:
    """Return True if formula contains actual LaTeX markup, not just plain text/single vars."""
    return bool(re.search(r'\\[a-zA-Z]+|[\^_{}]', formula))


def _clean_formula(formula: str) -> str:
    """Wrap bare formula in display math if not already wrapped."""
    formula = formula.strip()
    if not (formula.startswith("$") or formula.startswith(r"\[")):
        formula = f"$\\displaystyle {formula}$"
    return formula


MIN_PNG_SIZE = 80  # Telegram requires photos ≥ ~80px on each side


def _ensure_min_size(png_path: str, min_px: int = MIN_PNG_SIZE) -> str:
    """Upscale PNG in-place if either dimension is below min_px. Returns path."""
    try:
        from PIL import Image
        img = Image.open(png_path)
        w, h = img.size
        if w < min_px or h < min_px:
            scale = max(min_px / w, min_px / h)
            img = img.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
            img.save(png_path)
    except Exception:
        pass  # non-critical — image left as-is
    return png_path


# ─── Formula position extraction ─────────────────────────────────────────────

def _extract_formula_positions(content: str) -> list[dict]:
    """Find all formulas with their text positions, sorted by position.

    Deduplicates by formula text (first occurrence wins).
    Returns list of dicts: start, end, formula, hash, full_match.
    """
    seen: set[str] = set()
    results = []

    for pattern in DISPLAY_PATTERNS:
        for m in re.finditer(pattern, content, re.DOTALL):
            formula = m.group(1).strip()
            if formula and len(formula) > 2 and _is_real_latex(formula) and formula not in seen:
                seen.add(formula)
                results.append({
                    "start": m.start(), "end": m.end(),
                    "formula": formula, "hash": _formula_hash(formula),
                    "full_match": m.group(0),
                })

    for pattern in INLINE_PATTERNS:
        for m in re.finditer(pattern, content):
            formula = m.group(1).strip()
            if formula and len(formula) > 2 and _is_real_latex(formula) and formula not in seen:
                seen.add(formula)
                results.append({
                    "start": m.start(), "end": m.end(),
                    "formula": formula, "hash": _formula_hash(formula),
                    "full_match": m.group(0),
                })

    results.sort(key=lambda x: x["start"])
    return results


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


def _markdown_table_to_latex(md_table: str) -> str | None:
    """Convert markdown table to LaTeX tabular environment."""
    lines = [l.strip() for l in md_table.strip().split('\n') if l.strip()]
    if len(lines) < 3:
        return None  # need header + separator + at least 1 data row

    def parse_row(line):
        return [c.strip() for c in line.strip('|').split('|')]

    header = parse_row(lines[0])
    # Skip separator row (lines[1])
    data_rows = [parse_row(l) for l in lines[2:]]
    ncols = len(header)

    col_spec = '|' + '|'.join(['l'] * ncols) + '|'

    def convert_cell(cell):
        # Escape LaTeX specials first (before markdown conversion inserts backslashes)
        # Note: do NOT escape $ — cells may contain $...$  inline math (e.g. $^{12}C$)
        for ch in ['&', '%', '#', '_']:
            cell = re.sub(r'(?<!\\)' + re.escape(ch), '\\' + ch, cell)
        # Apply markdown bold/italic after escaping (* is not a LaTeX special)
        cell = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', cell)
        cell = re.sub(r'\*(.+?)\*', r'\\textit{\1}', cell)
        return cell

    parts = [
        f'\\begin{{tabular}}{{{col_spec}}}',
        '\\hline',
        ' & '.join(f'\\textbf{{{convert_cell(h)}}}' for h in header) + ' \\\\',
        '\\hline',
    ]
    for row in data_rows:
        cells = (row + [''] * ncols)[:ncols]
        parts.append(' & '.join(convert_cell(c) for c in cells) + ' \\\\')
    parts.extend(['\\hline', '\\end{tabular}'])
    return '\n'.join(parts)


def _group_nearby_formulas(
    formulas: list[dict], content: str, max_gap: int = 300
) -> list[list[dict]]:
    """Group formulas that are close together (same paragraph, within max_gap chars)."""
    if not formulas:
        return []
    groups = [[formulas[0]]]
    for f in formulas[1:]:
        prev = groups[-1][-1]
        gap_text = content[prev["end"]:f["start"]]
        # Merge if gap is short (regardless of paragraph breaks)
        if len(gap_text.strip()) < max_gap:
            groups[-1].append(f)
        else:
            groups.append([f])
    return groups


# ─── Single formula rendering ────────────────────────────────────────────────

def render_latex_pdflatex(formula: str, output_dir: str, dpi: int = 200) -> str | None:
    """Render formula to PNG using pdflatex → pdftoppm. Returns png_path or None."""
    fhash = _formula_hash(formula)
    png_path = os.path.join(output_dir, f"{fhash}.png")
    if os.path.exists(png_path):
        return png_path  # cache hit

    os.makedirs(output_dir, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmpdir:
        tex_file = os.path.join(tmpdir, "formula.tex")
        pdf_file = os.path.join(tmpdir, "formula.pdf")
        png_stem = os.path.join(tmpdir, "formula")

        with open(tex_file, "w") as f:
            f.write(LATEX_TEMPLATE % _clean_formula(formula))

        subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "-output-directory", tmpdir, tex_file],
            capture_output=True, text=True, encoding="latin-1", timeout=30,
        )
        if not os.path.exists(pdf_file):
            log.debug("pdflatex failed for formula %s", fhash)
            return None

        subprocess.run(
            ["pdftoppm", "-png", "-singlefile", "-r", str(dpi), pdf_file, png_stem],
            capture_output=True, text=True, encoding="latin-1", timeout=15,
        )
        tmp_png = png_stem + ".png"
        if not os.path.exists(tmp_png):
            log.debug("pdftoppm failed for formula %s", fhash)
            return None

        import shutil as sh
        sh.copy2(tmp_png, png_path)

    return _ensure_min_size(png_path)


def render_latex_matplotlib(formula: str, output_dir: str, dpi: int = 150) -> str | None:
    """Fallback renderer using matplotlib's mathtext."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        fhash = _formula_hash(formula)
        png_path = os.path.join(output_dir, f"{fhash}.png")
        if os.path.exists(png_path):
            return png_path

        os.makedirs(output_dir, exist_ok=True)

        clean = formula.strip()
        if not clean.startswith("$"):
            clean = f"${clean}$"

        fig, ax = plt.subplots(figsize=(6, 1))
        ax.text(0.5, 0.5, clean, fontsize=14, ha="center", va="center",
                transform=ax.transAxes)
        ax.axis("off")
        fig.savefig(png_path, dpi=dpi, bbox_inches="tight", pad_inches=0.1)
        plt.close(fig)
        return _ensure_min_size(png_path)
    except Exception as e:
        log.warning("matplotlib render failed: %s", e)
        return None


def render_latex(formula: str, output_dir: str, dpi: int = 150) -> str | None:
    """Render a single LaTeX formula to PNG. Tries pdflatex first, falls back to matplotlib."""
    if HAS_PDFLATEX and HAS_PDFTOPPM:
        path = render_latex_pdflatex(formula, output_dir, dpi)
        if path:
            return path
        log.warning("pdflatex failed, trying matplotlib for: %s...", formula[:40])
    return render_latex_matplotlib(formula, output_dir, dpi)


# ─── Combined block rendering (xelatex for mixed text + math) ────────────────

def _build_combined_content(group: list[dict], content: str) -> str:
    """Build xelatex content for a group of nearby formulas with text between them.

    Formulas are output in $...$ math mode. Vietnamese text between formulas
    is kept as-is (xelatex + fontspec handles UTF-8). Markdown is stripped.
    """
    parts = []
    for i, f in enumerate(group):
        if i > 0:
            prev = group[i - 1]
            gap = content[prev["end"]:f["start"]]
            # Strip Markdown bold/italic
            gap = re.sub(r'\*\*(.+?)\*\*', r'\1', gap)
            gap = re.sub(r'\*(.+?)\*', r'\1', gap)
            # Escape LaTeX-special chars in plain text (but not already-escaped ones)
            gap = gap.replace('&', r'\&').replace('%', r'\%').replace('#', r'\#')
            parts.append(gap)
        parts.append(f"${f['formula']}$")
    return "".join(parts)


def render_combined_block(
    group: list[dict], content: str, output_dir: str, dpi: int = 200
) -> str | None:
    """Render a group of nearby formulas + text as a single PNG using xelatex."""
    combined = _build_combined_content(group, content)
    chash = _formula_hash(combined)
    png_path = os.path.join(output_dir, f"cb_{chash}.png")
    if os.path.exists(png_path):
        return png_path

    if not HAS_XELATEX or not HAS_PDFTOPPM:
        log.warning("xelatex/pdftoppm not available for combined block")
        return None

    os.makedirs(output_dir, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmpdir:
        tex_file = os.path.join(tmpdir, "block.tex")
        pdf_file = os.path.join(tmpdir, "block.pdf")
        png_stem = os.path.join(tmpdir, "block")

        with open(tex_file, "w", encoding="utf-8") as f:
            f.write(XELATEX_TEMPLATE % combined)

        subprocess.run(
            ["xelatex", "-interaction=nonstopmode", "-output-directory", tmpdir, tex_file],
            capture_output=True, timeout=30,
        )
        if not os.path.exists(pdf_file):
            log.debug("xelatex failed for combined block %s", chash)
            return None

        subprocess.run(
            ["pdftoppm", "-png", "-singlefile", "-r", str(dpi), pdf_file, png_stem],
            capture_output=True, timeout=15,
        )
        tmp_png = png_stem + ".png"
        if not os.path.exists(tmp_png):
            log.debug("pdftoppm failed for combined block %s", chash)
            return None

        import shutil as sh
        sh.copy2(tmp_png, png_path)

    return _ensure_min_size(png_path)


# ─── Table rendering ─────────────────────────────────────────────────────────

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
            f.write(XELATEX_TABLE_TEMPLATE % latex_table)

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

        shutil.copy2(tmp_png, png_path)

    return _ensure_min_size(png_path)


# ─── Main rendering pipeline ────────────────────────────────────────────────

def render_lesson_math(lesson: Lesson, output_dir: str, dpi: int = 150) -> list[dict]:
    """Render all LaTeX formula blocks found in lesson content.

    Groups nearby formulas into combined blocks for cleaner Telegram delivery.
    Returns list of block dicts with keys: type, path, start, end.
    """
    formulas = _extract_formula_positions(lesson.content_enhanced)
    groups = _group_nearby_formulas(formulas, lesson.content_enhanced)

    blocks = []
    for group in groups[:50]:  # cap at 50 blocks per lesson
        if len(group) == 1:
            # Single formula — render individually
            f = group[0]
            path = render_latex(f["formula"], output_dir, dpi)
            if path:
                blocks.append({
                    "type": "single",
                    "path": path,
                    "start": f["start"],
                    "end": f["end"],
                })
        else:
            # Multiple nearby formulas — render as combined block
            path = render_combined_block(group, lesson.content_enhanced, output_dir, dpi)
            if path:
                blocks.append({
                    "type": "combined",
                    "path": path,
                    "start": group[0]["start"],
                    "end": group[-1]["end"],
                })
            else:
                # Fallback: render each formula individually
                for f in group:
                    path = render_latex(f["formula"], output_dir, dpi)
                    if path:
                        blocks.append({
                            "type": "single",
                            "path": path,
                            "start": f["start"],
                            "end": f["end"],
                        })

    # --- Table rendering ---
    tables = _extract_table_positions(lesson.content_enhanced)
    if len(tables) > 20:
        log.warning("Lesson %d: %d tables found, capping at 20", lesson.id, len(tables))
    for tbl in tables[:20]:
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


async def run_renderer(config: dict):
    """Render math images for all completed lessons that lack math_images_json."""
    output_dir = config["renderer"]["output_dir"]
    dpi = config["renderer"]["dpi"]
    os.makedirs(output_dir, exist_ok=True)

    rendered = 0
    lessons = await db.get_approved_lessons_needing_render()

    log.info("Rendering math for %d lessons...", len(lessons))

    for lesson in lessons:
        loop = asyncio.get_event_loop()
        blocks = await loop.run_in_executor(
            None, render_lesson_math, lesson, output_dir, dpi
        )
        if blocks:
            lesson.math_images_json = json.dumps(blocks)
            await db.update_lesson_content(lesson)
            rendered += 1
            log.debug("Lesson %d: %d math blocks", lesson.id, len(blocks))

    log.info("Renderer done: %d lessons with math images", rendered)
