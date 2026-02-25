"""HTML parser for Feynman Lectures pages.

Extracts:
- Sections (split by h2/h3 headings)
- LaTeX formulas (script tags + regex fallbacks)
- Image references (mapped to local downloaded files)

Stores structured data in `sections` table.
"""
import json
import logging
import re
from datetime import datetime
from typing import Optional

from bs4 import BeautifulSoup, NavigableString, Tag

from src.knowledge import db
from src.knowledge.models import Section

log = logging.getLogger(__name__)

# Content container selectors (in priority order; verified against feynmanlectures.caltech.edu)
CONTENT_SELECTORS = [
    {"class": "content"},
    {"id": "content"},
    "article",
    "main",
    {"class": "chapter"},
]

HEADING_TAGS = {"h2", "h3"}
BLOCK_TAGS = {"p", "div", "table", "ul", "ol", "blockquote", "pre", "figure"}


def _find_content_div(soup: BeautifulSoup) -> Optional[Tag]:
    """Locate the main content container."""
    for selector in CONTENT_SELECTORS:
        if isinstance(selector, dict):
            el = soup.find(True, selector)
        else:
            el = soup.find(selector)
        if el:
            return el
    # Fallback: body
    return soup.find("body")


def extract_latex(html: str) -> dict:
    """Extract LaTeX formulas from HTML using script tags + regex fallbacks."""
    soup = BeautifulSoup(html, "html.parser")

    # Method 1: <script type="math/tex"> tags (MathJax source - most reliable)
    script_tags = soup.find_all("script", {"type": re.compile(r"math/tex", re.I)})
    script_formulas = [s.string.strip() for s in script_tags if s.string and s.string.strip()]

    # Method 2: regex fallbacks for common LaTeX delimiters
    # Remove script tags before regex to avoid double-counting
    text = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.DOTALL)

    display_formulas = []
    for m in re.finditer(r"\$\$(.*?)\$\$|\\\[(.*?)\\\]", text, re.DOTALL):
        formula = (m.group(1) or m.group(2)).strip()
        if formula:
            display_formulas.append(formula)

    inline_formulas = []
    for m in re.finditer(r"\\\((.*?)\\\)", text, re.DOTALL):
        formula = m.group(1).strip()
        if formula:
            inline_formulas.append(formula)

    all_formulas = script_formulas + display_formulas + inline_formulas
    # Deduplicate while preserving order
    seen, unique = set(), []
    for f in all_formulas:
        if f not in seen:
            seen.add(f)
            unique.append(f)

    return {"script_tags": script_formulas, "display": display_formulas,
            "inline": inline_formulas, "all": unique}


def _element_text(el: Tag) -> str:
    """Extract plain text from element, collapsing whitespace."""
    return " ".join(el.get_text().split())


def extract_sections(soup: BeautifulSoup) -> list[dict]:
    """Split content into sections by h2/h3 headings.

    Returns list of {number, title, elements, text, latex_placeholders}.
    """
    content = _find_content_div(soup)
    if not content:
        log.warning("No content container found; using full document body")
        content = soup

    sections = []
    current: dict = {"number": 0, "title": "Introduction", "elements": [], "text_parts": []}

    for el in content.children:
        if isinstance(el, NavigableString):
            text = el.strip()
            if text:
                current["text_parts"].append(text)
            continue
        if not isinstance(el, Tag):
            continue

        if el.name in HEADING_TAGS:
            # Save current section if it has content
            if current["text_parts"] or current["elements"]:
                sections.append(current)
            current = {
                "number": len(sections) + 1,
                "title": el.get_text(strip=True),
                "elements": [],
                "text_parts": [],
            }
        elif el.name in BLOCK_TAGS or el.name in HEADING_TAGS:
            current["elements"].append(el)
            current["text_parts"].append(_element_text(el))

    # Append last section
    if current["text_parts"] or current["elements"]:
        sections.append(current)

    return sections


def _build_section_text(section: dict, all_formulas: list[str]) -> tuple[str, list[str]]:
    """Build plain text with {{FORMULA_N}} placeholders. Returns (text, used_formulas)."""
    text = " ".join(section["text_parts"])

    # Replace LaTeX formula occurrences with placeholders
    used_formulas = []
    formula_idx = 0
    for formula in all_formulas:
        escaped = re.escape(formula)
        if re.search(escaped, text):
            placeholder = f"{{{{FORMULA_{formula_idx}}}}}"
            text = re.sub(escaped, placeholder, text, count=1)
            used_formulas.append(formula)
            formula_idx += 1

    return text.strip(), used_formulas


def parse_chapter(raw_html: str, image_map: dict[str, str]) -> list[Section]:
    """Parse raw chapter HTML into a list of Section objects."""
    soup = BeautifulSoup(raw_html, "html.parser")

    latex_data = extract_latex(raw_html)
    all_formulas = latex_data["all"]

    sections_raw = extract_sections(soup)
    sections: list[Section] = []

    for i, raw in enumerate(sections_raw):
        content_text, section_formulas = _build_section_text(raw, all_formulas)

        # Map image src attrs to local paths
        image_refs = []
        for el in raw["elements"]:
            for img in el.find_all("img", src=True) if hasattr(el, "find_all") else []:
                src = img.get("src", "")
                local = image_map.get(src, src)
                if local not in image_refs:
                    image_refs.append(local)

        if not content_text.strip():
            continue  # skip empty sections

        section = Section(
            id=None,
            chapter_id=0,  # set by caller
            number=i + 1,
            title=raw["title"],
            content_text=content_text,
            latex_formulas=section_formulas,
            image_refs=image_refs,
        )
        sections.append(section)

    return sections


async def run_parser(config: dict):
    """Parse all unprocessed chapters and store sections in DB."""
    chapters = await db.get_unparsed_chapters()
    log.info("Parsing %d chapters...", len(chapters))

    for chapter in chapters:
        # Reconstruct image_map from filesystem (images already downloaded in crawl phase)
        chapter_dir = f"data/raw/images/{chapter.volume}_{chapter.number:02d}"
        image_map = _build_image_map(chapter.url, chapter_dir)

        try:
            sections = parse_chapter(chapter.raw_html, image_map)
            for section in sections:
                section.chapter_id = chapter.id
                await db.insert_section(chapter.id, section)

            log.info("Parsed Vol %s Ch %02d: %d sections, total %d formulas",
                     chapter.volume, chapter.number, len(sections),
                     sum(len(s.latex_formulas) for s in sections))
        except Exception as e:
            log.error("Failed to parse Vol %s Ch %02d: %s", chapter.volume, chapter.number, e)

    log.info("Parser complete.")


def _build_image_map(chapter_url: str, chapter_dir: str) -> dict[str, str]:
    """Build {original_src: local_path} map from downloaded image directory."""
    import os, urllib.parse
    if not os.path.isdir(chapter_dir):
        return {}
    image_map = {}
    base = chapter_url.rsplit("/", 1)[0] + "/"
    for fname in os.listdir(chapter_dir):
        local_path = os.path.join(chapter_dir, fname)
        # Map both relative and absolute URL forms
        image_map[fname] = local_path
        image_map[base + fname] = local_path
    return image_map
