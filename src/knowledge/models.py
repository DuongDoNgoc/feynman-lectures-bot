"""Data models matching SQLite schema."""
from dataclasses import dataclass, field
from typing import Optional
import json


@dataclass
class Chapter:
    id: Optional[int]
    volume: str           # "I" or "II"
    number: int
    title: str
    url: str
    raw_html: str = ""
    crawled_at: Optional[str] = None


@dataclass
class Section:
    id: Optional[int]
    chapter_id: int
    number: int
    title: str
    content_text: str                # plain text with {{FORMULA_N}} placeholders
    latex_formulas: list = field(default_factory=list)   # list of LaTeX strings
    image_refs: list = field(default_factory=list)       # local image paths
    parsed_at: Optional[str] = None
    # Populated from JOIN query (not stored in sections table)
    chapter_number: int = 0
    chapter_title: str = ""

    @property
    def latex_formulas_json(self) -> str:
        return json.dumps(self.latex_formulas)

    @property
    def image_refs_json(self) -> str:
        return json.dumps(self.image_refs)


@dataclass
class Chunk:
    """Intermediate: not persisted; produced by chunker, consumed by enhancer."""
    text: str
    formulas: list = field(default_factory=list)
    word_count: int = 0
    section_ids: list = field(default_factory=list)
    # Populated from first section in chunk for title generation
    chapter_number: int = 0
    section_number: int = 0
    section_title: str = ""


@dataclass
class Lesson:
    id: Optional[int]
    section_id: int
    lesson_type: str        # "concept" | "deep_dive" | "quiz"
    sequence: int           # ordering within chapter
    title: str
    content_enhanced: str
    examples_json: Optional[str] = None
    quiz_json: Optional[str] = None
    math_images_json: Optional[str] = None
    enhancement_status: str = "pending"   # pending | in_progress | completed
    approval_status: str = "pending"      # pending | approved | rejected
    created_at: Optional[str] = None


@dataclass
class UserProgress:
    id: Optional[int]
    user_id: int
    lesson_id: int
    sent_at: Optional[str] = None
    read_at: Optional[str] = None
    quiz_score: Optional[float] = None


@dataclass
class ConversationMessage:
    id: Optional[int]
    user_id: int
    lesson_id: int
    role: str       # "user" | "assistant"
    message: str
    created_at: Optional[str] = None


@dataclass
class ScheduledLesson:
    id: Optional[int]
    user_id: int
    lesson_id: int
    lesson_type: str
    scheduled_time: str
    delivered: bool = False
    delivered_at: Optional[str] = None
