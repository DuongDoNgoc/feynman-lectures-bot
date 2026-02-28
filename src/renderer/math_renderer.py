"""LaTeX → PNG renderer using pdflatex + pdftoppm.

Features:
- 150dpi output (readable on Telegram mobile)
- Cache by MD5 hash of formula — no re-render
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

LATEX_TEMPLATE = r"""\documentclass[border=4pt]{standalone}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{xcolor}
\begin{document}
\color{black}
%s
\end{document}
"""

HAS_PDFLATEX = shutil.which("pdflatex") is not None
HAS_PDFTOPPM = shutil.which("pdftoppm") is not None


def _formula_hash(formula: str) -> str:
    return hashlib.md5(formula.encode()).hexdigest()[:12]


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


def render_latex_pdflatex(formula: str, output_dir: str, dpi: int = 200) -> str | None:
    """Render formula to PNG using pdflatex → pdftoppm. Returns png_path or None."""
    formula_hash = _formula_hash(formula)
    png_path = os.path.join(output_dir, f"{formula_hash}.png")
    if os.path.exists(png_path):
        return png_path  # cache hit

    os.makedirs(output_dir, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmpdir:
        tex_file = os.path.join(tmpdir, "formula.tex")
        pdf_file = os.path.join(tmpdir, "formula.pdf")
        png_stem = os.path.join(tmpdir, "formula")

        # Write .tex
        with open(tex_file, "w") as f:
            f.write(LATEX_TEMPLATE % _clean_formula(formula))

        # pdflatex → .pdf
        result = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "-output-directory", tmpdir, tex_file],
            capture_output=True, text=True, encoding="latin-1", timeout=30,
        )
        if not os.path.exists(pdf_file):
            log.debug("pdflatex failed for formula %s: %s", formula_hash, result.stderr[-300:])
            return None

        # pdftoppm → .png
        result = subprocess.run(
            ["pdftoppm", "-png", "-singlefile", "-r", str(dpi), pdf_file, png_stem],
            capture_output=True, text=True, encoding="latin-1", timeout=15,
        )
        tmp_png = png_stem + ".png"
        if not os.path.exists(tmp_png):
            log.debug("pdftoppm failed for formula %s", formula_hash)
            return None

        # Move to cache and ensure minimum dimensions
        import shutil as sh
        sh.copy2(tmp_png, png_path)

    return _ensure_min_size(png_path)


def render_latex_matplotlib(formula: str, output_dir: str, dpi: int = 150) -> str | None:
    """Fallback renderer using matplotlib's mathtext. Lower quality but no LaTeX needed."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        formula_hash = _formula_hash(formula)
        png_path = os.path.join(output_dir, f"{formula_hash}.png")
        if os.path.exists(png_path):
            return png_path

        os.makedirs(output_dir, exist_ok=True)

        # Ensure formula is wrapped in $ for matplotlib
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
    """Render a LaTeX formula to PNG. Tries pdflatex first, falls back to matplotlib."""
    if HAS_PDFLATEX and HAS_PDFTOPPM:
        path = render_latex_pdflatex(formula, output_dir, dpi)
        if path:
            return path
        log.warning("pdflatex failed, trying matplotlib for: %s...", formula[:40])
    return render_latex_matplotlib(formula, output_dir, dpi)


def render_lesson_math(lesson: Lesson, output_dir: str, dpi: int = 150) -> list[str]:
    """Render all LaTeX formulas found in lesson content. Returns list of PNG paths."""
    # Extract formulas from content_enhanced
    patterns = [
        r"\$\$(.*?)\$\$",          # display $$...$$
        r"\\\[(.*?)\\\]",          # display \[...\]
        r"\$((?:[^$]|\\.)+?)\$",   # inline $...$
        r"\\\((.*?)\\\)",          # inline \(...\)
    ]
    formulas = []
    for pattern in patterns:
        for m in re.finditer(pattern, lesson.content_enhanced, re.DOTALL):
            formula = m.group(1).strip()
            if formula and len(formula) > 2 and formula not in formulas:
                formulas.append(formula)

    png_paths = []
    for formula in formulas[:20]:  # cap at 20 per lesson to avoid huge batches
        path = render_latex(formula, output_dir, dpi)
        if path:
            png_paths.append(path)
        else:
            log.warning("Could not render formula: %s...", formula[:40])

    return png_paths


async def run_renderer(config: dict):
    """Render math images for all completed lessons that lack math_images_json."""
    output_dir = config["renderer"]["output_dir"]
    dpi = config["renderer"]["dpi"]
    os.makedirs(output_dir, exist_ok=True)

    rendered = 0
    # Only render approved lessons — avoids rendering content not yet human-reviewed
    lessons = await db.get_approved_lessons_needing_render()

    log.info("Rendering math for %d lessons...", len(lessons))

    for lesson in lessons:
        # Run sync rendering in executor to avoid blocking event loop
        loop = asyncio.get_event_loop()
        png_paths = await loop.run_in_executor(
            None, render_lesson_math, lesson, output_dir, dpi
        )
        if png_paths:
            lesson.math_images_json = json.dumps(png_paths)
            await db.update_lesson_content(lesson)
            rendered += 1
            log.debug("Lesson %d: %d math images", lesson.id, len(png_paths))

    log.info("Renderer done: %d lessons with math images", rendered)
