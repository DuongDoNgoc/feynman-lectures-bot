"""Export lessons to human-readable markdown for preview and approval."""
import hashlib
import json
import logging
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from src.knowledge.preview_db import (
    get_completed_lessons,
    get_completed_lessons_by_type,
    get_lesson_with_context,
)

log = logging.getLogger(__name__)

OUTPUT_DIR = Path(__file__).parent.parent.parent / "docs" / "lessons-preview"
MAX_FILENAME_LENGTH = 50
MAX_LINES_PER_FILE = 800


def _generate_slug(text: str) -> str:
    """Convert text to URL-safe slug.

    Args:
        text: Input text (e.g., chapter title)

    Returns:
        Slug string (lowercase, hyphens, max 50 chars)
    """
    # Lowercase and replace non-alphanumeric with hyphens
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower())
    # Remove leading/trailing hyphens
    slug = slug.strip("-")
    # Limit length
    return slug[:MAX_FILENAME_LENGTH]


def _compute_hash(content: str) -> str:
    """Compute MD5 hash of content for change detection."""
    return hashlib.md5(content.encode()).hexdigest()[:12]


def _format_quiz(quiz_json: Optional[str]) -> str:
    """Format quiz JSON as markdown questions.

    Args:
        quiz_json: JSON string with quiz data

    Returns:
        Formatted markdown string
    """
    if not quiz_json:
        return ""

    try:
        quiz = json.loads(quiz_json)
    except json.JSONDecodeError:
        return "\n\n*Quiz data could not be parsed*\n"

    lines = ["\n\n## Quiz Questions\n"]

    questions = quiz.get("questions", [])
    for i, q in enumerate(questions, 1):
        question_text = q.get("question", "No question text")
        lines.append(f"**Q{i}:** {question_text}")

        options = q.get("options", [])
        for j, opt in enumerate(options):
            letter = chr(65 + j)  # A, B, C, D
            lines.append(f"- {letter}) {opt}")

        correct = q.get("correct_answer", q.get("answer", "N/A"))
        if isinstance(correct, int) and correct < len(options):
            correct = chr(65 + correct)
        lines.append(f"\n**Correct:** {correct}")

        explanation = q.get("explanation", "")
        if explanation:
            lines.append(f"\n**Explanation:** {explanation}")

        lines.append("")  # Blank line between questions

    return "\n".join(lines)


def _extract_title(content: str) -> str:
    """Extract title from content_enhanced (first heading or first line)."""
    # Look for markdown heading
    match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    # Fall back to first non-empty line
    lines = [l for l in content.split("\n") if l.strip()]
    return lines[0][:80] if lines else "Untitled"


def _split_long_content(content: str) -> list[str]:
    """Split content if exceeds MAX_LINES_PER_FILE.

    Splits at paragraph boundaries when possible.

    Args:
        content: Full markdown content

    Returns:
        List of content parts
    """
    lines = content.split("\n")
    if len(lines) <= MAX_LINES_PER_FILE:
        return [content]

    parts = []
    current_part = []
    current_lines = 0

    for line in lines:
        current_part.append(line)
        current_lines += 1

        # Split at paragraph boundary if over limit
        if current_lines >= MAX_LINES_PER_FILE and not line.strip():
            parts.append("\n".join(current_part))
            current_part = ["\n*(continued)*\n"]
            current_lines = 2

    if current_part:
        parts.append("\n".join(current_part))

    return parts


def _generate_markdown(
    lesson,
    section: Optional,
    chapter: Optional[dict],
) -> str:
    """Generate full markdown content for a lesson.

    Args:
        lesson: Lesson dataclass
        section: Section dataclass or None
        chapter: Chapter dict or None

    Returns:
        Complete markdown string with frontmatter
    """
    # Build frontmatter
    frontmatter = {
        "lesson_id": lesson.id,
        "lesson_type": lesson.lesson_type,
        "approval_status": getattr(lesson, "approval_status", "pending"),
        "exported_at": datetime.now(timezone.utc).isoformat(),
        "content_hash": _compute_hash(lesson.content_enhanced),
    }

    if chapter:
        frontmatter["chapter_number"] = chapter["number"]
        frontmatter["chapter_title"] = chapter["title"]

    if section:
        frontmatter["section_number"] = section.number
        frontmatter["section_title"] = section.title

    # Build frontmatter YAML
    fm_lines = ["---"]
    for key, value in frontmatter.items():
        if isinstance(value, str) and ('"' in value or ":" in value):
            fm_lines.append(f'{key}: "{value}"')
        else:
            fm_lines.append(f"{key}: {value}")
    fm_lines.append("---\n")

    # Build content
    title = _extract_title(lesson.content_enhanced)
    content_lines = [f"# {title}\n"]

    # Add source context
    if chapter and section:
        source_url = chapter.get("url", "")
        url_part = f" | [📖 Nguồn]({source_url})" if source_url else ""
        content_lines.append(
            f"*Source: Chapter {chapter['number']} - {chapter['title']} "
            f"(Section {section.number}){url_part}*\n"
        )

    content_lines.append(lesson.content_enhanced)

    # Add quiz section if applicable
    if lesson.lesson_type == "quiz":
        content_lines.append(_format_quiz(lesson.quiz_json))

    # Footer
    content_lines.append("\n---\n*Exported from Feynman Bot*\n")

    # Combine all
    full_content = "\n".join(fm_lines) + "\n".join(content_lines)
    return full_content


async def export_lesson(lesson_id: int) -> Optional[Path]:
    """Export a single lesson to markdown.

    Args:
        lesson_id: Database ID of lesson

    Returns:
        Path to created file, or None if lesson not found
    """
    context = await get_lesson_with_context(lesson_id)
    if not context:
        log.warning("Lesson %d not found", lesson_id)
        return None

    lesson = context["lesson"]
    section = context.get("section")
    chapter = context.get("chapter")

    # Generate markdown
    markdown = _generate_markdown(lesson, section, chapter)

    # Generate filename
    chapter_slug = _generate_slug(chapter["title"]) if chapter else "unknown"
    filename = f"{lesson.id:04d}-{lesson.lesson_type}-{chapter_slug}.md"
    output_path = OUTPUT_DIR / filename

    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Handle split content
    parts = _split_long_content(markdown)

    if len(parts) == 1:
        output_path.write_text(markdown, encoding="utf-8")
        log.info("Exported lesson %d to %s", lesson_id, output_path)
    else:
        # Write multiple parts
        for i, part in enumerate(parts, 1):
            part_path = OUTPUT_DIR / f"{lesson.id:04d}-{lesson.lesson_type}-{chapter_slug}-part{i}.md"
            part_path.write_text(part, encoding="utf-8")
        output_path = OUTPUT_DIR / f"{lesson.id:04d}-{lesson.lesson_type}-{chapter_slug}-part1.md"
        log.info("Exported lesson %d to %d parts", lesson_id, len(parts))

    return output_path


async def export_all_lessons() -> list[Path]:
    """Export all completed lessons.

    Returns:
        List of paths to created files
    """
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    lessons = await get_completed_lessons()
    paths = []

    for lesson in lessons:
        path = await export_lesson(lesson.id)
        if path:
            paths.append(path)

    log.info("Exported %d lessons to %s", len(paths), OUTPUT_DIR)
    return paths


async def export_lessons_by_type(lesson_type: str) -> list[Path]:
    """Export completed lessons of specific type.

    Args:
        lesson_type: One of 'concept', 'deep_dive', 'quiz'

    Returns:
        List of paths to created files
    """
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    lessons = await get_completed_lessons_by_type(lesson_type)
    paths = []

    for lesson in lessons:
        path = await export_lesson(lesson.id)
        if path:
            paths.append(path)

    log.info("Exported %d %s lessons", len(paths), lesson_type)
    return paths
