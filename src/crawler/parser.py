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

from bs4 import BeautifulSoup, NavigableString, Tag  # NavigableString used in _element_text

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
    """Extract plain text from element, collapsing whitespace.

    get_text() skips <script> content, so we:
    1. Replace each <script type="math/tex"> with a plain-text span holding the LaTeX.
    2. Remove MathJax-rendered spans (they duplicate content from script tags).
    Result: clean text with raw LaTeX strings inline (e.g. '\\tfrac{1}{2}kT'),
    which _build_section_text() can then match and replace with {{FORMULA_N}}.
    """
    # Re-parse a copy so we don't mutate the shared parse tree
    el_copy = BeautifulSoup(str(el), "html.parser")

    # Step 1: Replace math script tags with NavigableString (plain text nodes).
    # get_text() skips <script> content but includes NavigableString text directly.
    for script in el_copy.find_all("script", type=re.compile(r"math/tex", re.I)):
        latex = (script.string or "").strip()
        script.replace_with(NavigableString(f" {latex} "))

    # Step 2: Remove MathJax output spans (rendered duplicates, now redundant)
    for span in el_copy.find_all("span", class_=re.compile(r"MathJax")):
        span.decompose()

    return " ".join(el_copy.get_text().split())


def extract_sections(soup: BeautifulSoup) -> list[dict]:
    """Split content into sections by h2/h3 headings (recursive search).

    Uses find_all() to detect headings nested inside div/section wrappers,
    which content.children misses.

    Returns list of {number, title, elements, text_parts}.
    """
    content = _find_content_div(soup)
    if not content:
        log.warning("No content container found; using full document body")
        content = soup

    # Find ALL h2/h3 headings recursively (handles any nesting depth)
    all_headings = content.find_all(list(HEADING_TAGS))

    if not all_headings:
        # No headings → return single section with all block content
        blocks = content.find_all(list(BLOCK_TAGS))
        if not blocks:
            return []
        return [{
            "number": 1,
            "title": "Full Chapter",
            "elements": blocks,
            "text_parts": [_element_text(el) for el in blocks],
        }]

    sections = []

    # Collect intro content before first heading
    intro_parts = _collect_text_before(all_headings[0], content)
    if intro_parts:
        sections.append({
            "number": 0,
            "title": "Introduction",
            "elements": [],
            "text_parts": intro_parts,
        })

    # Create one section per heading
    for i, heading in enumerate(all_headings):
        next_heading = all_headings[i + 1] if i + 1 < len(all_headings) else None
        elements, text_parts = _collect_between_headings(heading, next_heading)
        sections.append({
            "number": len(sections) + 1,
            "title": heading.get_text(strip=True),
            "elements": elements,
            "text_parts": text_parts,
        })

    return sections


def _collect_text_before(first_heading: Tag, content: Tag) -> list[str]:
    """Collect block-level text appearing before the first heading."""
    parts = []
    for el in content.descendants:
        if el is first_heading:
            break
        if isinstance(el, Tag) and el.name in BLOCK_TAGS:
            # Skip ancestors of the first heading
            if first_heading in el.descendants:
                continue
            # Skip blocks that contain nested blocks (avoid double-counting)
            if el.find(list(BLOCK_TAGS)):
                continue
            text = _element_text(el)
            if text:
                parts.append(text)
    return parts


def _collect_between_headings(
    heading: Tag, next_heading: Optional[Tag]
) -> tuple[list[Tag], list[str]]:
    """Collect block elements and text between two headings.

    Walks siblings after the heading within its parent container (div.section).
    Since Feynman Lectures wrap each section in a div.section, all content
    between headings is within the same parent — no cross-container walking needed.
    """
    elements: list[Tag] = []
    text_parts: list[str] = []

    current = heading.next_sibling
    while current:
        if current is next_heading:
            break
        if isinstance(current, Tag):
            # Stop if this element contains the next heading
            if next_heading and next_heading in current.descendants:
                break
            if current.name in HEADING_TAGS:
                break
            if current.name in BLOCK_TAGS:
                elements.append(current)
                text_parts.append(_element_text(current))
        current = current.next_sibling

    return elements, text_parts


def _build_section_text(section: dict, all_formulas: list[str]) -> tuple[str, list[str]]:
    """Build plain text with {{FORMULA_N}} placeholders. Returns (text, used_formulas).

    Uses a single-pass replacement to prevent already-inserted placeholders from
    being matched again by subsequent formula patterns (which caused nested corruption
    like {{FORM{{FORMULA_14}}_{{FORMULA_17}}}}LA_0}}).
    """
    text = " ".join(section["text_parts"])

    # Phase 1: locate the first occurrence of each formula in the original text.
    # We collect (start, end, formula) tuples without modifying the text yet.
    # Use word-boundary anchors so single-char formulas (x, a, t, 1...) don't
    # match inside regular English words (e.g. 'a' in 'about', 'x' in 'hexagonal').
    raw_matches: list[tuple[int, int, str]] = []
    for formula in all_formulas:
        pattern = r"(?<!\w)" + re.escape(formula) + r"(?!\w)"
        m = re.search(pattern, text)
        if m:
            raw_matches.append((m.start(), m.end(), formula))

    if not raw_matches:
        return text.strip(), []

    # Phase 2: sort by position and drop overlapping spans (keep first).
    raw_matches.sort(key=lambda x: x[0])
    non_overlapping: list[tuple[int, int, str]] = []
    prev_end = -1
    for start, end, formula in raw_matches:
        if start >= prev_end:
            non_overlapping.append((start, end, formula))
            prev_end = end

    # Phase 3: build result in one sweep — no re-scanning of replaced text.
    result: list[str] = []
    used_formulas: list[str] = []
    cursor = 0
    for idx, (start, end, formula) in enumerate(non_overlapping):
        result.append(text[cursor:start])
        result.append(f"{{{{FORMULA_{idx}}}}}")
        used_formulas.append(formula)
        cursor = end
    result.append(text[cursor:])

    return "".join(result).strip(), used_formulas


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
