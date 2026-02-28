"""Splits sections into word-bounded micro-lesson chunks.

Rules:
- Target: 2000 words (configurable), tolerance ±25% → 1500-2500 range
- Minimum: 800 words per chunk (merge small trailing sections)
- Never split mid-formula or mid-derivation (formulas travel with their section)
- Heading tags = preferred chunk boundaries
- Stores stub lessons (pending enhancement) in DB for each chunk × lesson_type
"""
import logging
from dataclasses import dataclass, field

from src.knowledge import db
from src.knowledge.models import Chunk, Lesson, Section

log = logging.getLogger(__name__)

LESSON_TYPES = ["concept", "deep_dive", "quiz"]


def chunk_sections(
    sections: list[Section],
    target: int = 2000,
    tolerance: float = 0.25,
    min_words: int = 800,
) -> list[Chunk]:
    """Group sections into chunks respecting word-count boundaries."""
    upper = int(target * (1 + tolerance))
    lower = int(target * (1 - tolerance))

    chunks: list[Chunk] = []
    current = Chunk(text="", formulas=[], word_count=0, section_ids=[])

    for section in sections:
        words = len(section.content_text.split())

        # If adding this section would overflow and we already have enough content → flush
        if current.word_count >= lower and (current.word_count + words) > upper:
            chunks.append(current)
            current = Chunk(text="", formulas=[], word_count=0, section_ids=[])

        # Use first substantial section (>100 words) for title, or first section
        if not current.section_ids or (current.word_count < 100 and words >= 100):
            current.chapter_number = getattr(section, "chapter_number", 0)
            current.section_number = section.number
            current.section_title = section.title

        current.text += section.content_text + "\n\n"
        current.formulas.extend(section.latex_formulas)
        current.word_count += words
        current.section_ids.append(section.id)

    if current.word_count > 0:
        chunks.append(current)

    # Merge trailing chunks smaller than min_words into the previous one
    merged: list[Chunk] = []
    for chunk in chunks:
        if chunk.word_count < min_words and merged:
            prev = merged[-1]
            prev.text += chunk.text
            prev.formulas.extend(chunk.formulas)
            prev.word_count += chunk.word_count
            prev.section_ids.extend(chunk.section_ids)
        else:
            merged.append(chunk)

    log.info("Chunked %d sections → %d chunks (avg %.0f words)",
             len(sections), len(merged),
             sum(c.word_count for c in merged) / max(len(merged), 1))
    return merged


async def run_chunker(config: dict):
    """Load all sections, chunk per chapter, insert pending lessons into DB."""
    target = config["chunker"]["target_words"]
    tolerance = config["chunker"]["tolerance"]
    min_words = config["chunker"]["min_words"]

    sections = await db.get_all_sections()
    if not sections:
        log.warning("No sections found. Run the parse stage first.")
        return

    # Group sections by chapter to avoid cross-chapter merging
    from itertools import groupby
    sorted_sections = sorted(sections, key=lambda s: s.chapter_id)
    sections_by_chapter = {
        k: list(g) for k, g in groupby(sorted_sections, key=lambda s: s.chapter_id)
    }

    chunks: list[Chunk] = []
    for chapter_id, chapter_sections in sections_by_chapter.items():
        chunks.extend(chunk_sections(
            chapter_sections, target=target, tolerance=tolerance, min_words=min_words
        ))

    inserted = 0
    for seq, chunk in enumerate(chunks):
        # Use first section_id as anchor for the lesson group
        anchor_section_id = chunk.section_ids[0] if chunk.section_ids else 0

        # Build meaningful title from chapter/section metadata
        base_title = _build_chunk_title(chunk, seq)

        for lesson_type in LESSON_TYPES:
            lesson = Lesson(
                id=None,
                section_id=anchor_section_id,
                lesson_type=lesson_type,
                sequence=seq,
                title=f"{base_title} — {lesson_type}",
                content_enhanced=chunk.text,  # raw text; replaced after enhancement
                enhancement_status="pending",
            )
            await db.insert_lesson(lesson)
            inserted += 1

    log.info("Inserted %d pending lessons (%d chunks × 3 types)", inserted, len(chunks))


def _build_chunk_title(chunk: Chunk, seq: int) -> str:
    """Build a human-readable title like 'Ch1-2: Matter is made of atoms'."""
    if chunk.chapter_number and chunk.section_title:
        # Truncate long section titles
        title = chunk.section_title[:60]
        return f"Ch{chunk.chapter_number}-{chunk.section_number}: {title}"
    return f"Chunk {seq + 1}"
