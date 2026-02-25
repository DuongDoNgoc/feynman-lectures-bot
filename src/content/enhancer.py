"""LLM-based lesson enhancer.

Rewrites raw chunk text into 3 lesson types:
- concept    (~800 words) : intuitive intro, analogies, 1-2 key formulas
- deep_dive  (~1000 words): detailed derivation, worked example for role
- quiz       (~600 words) : 3 MCQs + 1 open-ended + answer key (JSON embedded)

Enhancement is idempotent: already-completed lessons are skipped.
Pipeline is resumable: tracks status per lesson in DB.
"""
import json
import logging
import re

from src.knowledge import db
from src.knowledge.models import Lesson
from src.llm.provider import LLMProvider, build_enhancement_provider

log = logging.getLogger(__name__)

# ─── System prompt ────────────────────────────────────────────────────────────

SYSTEM_PROMPT = """Bạn là giảng viên vật lý giỏi, giỏi giải thích khái niệm phức tạp theo cách dễ hiểu.
Người học là {role} người Việt Nam, đang học vật lý Feynman để nâng cao kiến thức.
Viết bằng tiếng Việt, xen kẽ thuật ngữ vật lý tiếng Anh khi cần thiết.
Giữ công thức LaTeX trong ký hiệu $...$ hoặc $$...$$."""

# ─── Per-type prompt templates ────────────────────────────────────────────────

PROMPT_TEMPLATES = {
    "concept": """\
Dựa vào nội dung vật lý sau đây, viết BÀI GIẢNG GIỚI THIỆU (concept lesson) khoảng 800 từ.

YÊU CẦU:
- Mở đầu bằng câu hỏi thú vị hoặc hiện tượng thực tế mà người học quen thuộc
- Giải thích ý tưởng cốt lõi bằng ngôn ngữ trực quan, sử dụng tối đa 2 công thức quan trọng nhất
- Dùng ít nhất 1 phép so sánh/ẩn dụ phù hợp với {role}
- Kết thúc bằng tóm tắt ngắn gọn "Điểm mấu chốt"
- Tiêu đề: bắt đầu bằng "## [Tên chủ đề]"

NỘI DUNG GỐC:
{content}

CÔNG THỨC LIÊN QUAN:
{formulas}
""",

    "deep_dive": """\
Dựa vào nội dung vật lý sau đây, viết BÀI GIẢNG CHUYÊN SÂU (deep dive) khoảng 1000 từ.

YÊU CẦU:
- Trình bày đầy đủ các bước suy luận/chứng minh quan trọng
- Thêm VÍ DỤ THỰC TẾ cụ thể liên quan đến {role} (cảm biến, đo lường, cơ điện tử)
- Bài tập mẫu có lời giải từng bước
- Giải thích ý nghĩa vật lý đằng sau mỗi bước
- Tiêu đề: bắt đầu bằng "## [Tên chủ đề] — Phân tích Chuyên sâu"

NỘI DUNG GỐC:
{content}

CÔNG THỨC LIÊN QUAN:
{formulas}
""",

    "quiz": """\
Dựa vào nội dung vật lý sau đây, tạo BÀI KIỂM TRA (quiz) theo định dạng sau.

YÊU CẦU:
- 3 câu hỏi trắc nghiệm (A/B/C/D), mỗi câu có 1 đáp án đúng
- 1 câu hỏi tự luận mở (liên hệ với kinh nghiệm {role})
- Đáp án và giải thích ngắn gọn cho từng câu
- Tiêu đề: bắt đầu bằng "## Quiz: [Tên chủ đề]"

ĐỊNH DẠNG JSON PHẢI CÓ ở cuối bài (giữa thẻ ```json và ```):
```json
{{
  "questions": [
    {{"id": "q1", "type": "mcq", "question": "...", "options": ["A. ...", "B. ...", "C. ...", "D. ..."], "answer": "A", "explanation": "..."}},
    {{"id": "q2", "type": "mcq", "question": "...", "options": ["A. ...", "B. ...", "C. ...", "D. ..."], "answer": "B", "explanation": "..."}},
    {{"id": "q3", "type": "mcq", "question": "...", "options": ["A. ...", "B. ...", "C. ...", "D. ..."], "answer": "C", "explanation": "..."}},
    {{"id": "q4", "type": "open", "question": "...", "sample_answer": "..."}}
  ]
}}
```

NỘI DUNG GỐC:
{content}

CÔNG THỨC LIÊN QUAN:
{formulas}
""",
}


# ─── Helpers ─────────────────────────────────────────────────────────────────

def _extract_title(content: str) -> str:
    """Extract markdown heading as lesson title."""
    for line in content.splitlines():
        line = line.strip()
        if line.startswith("#"):
            return re.sub(r"^#+\s*", "", line).strip()
    # Fallback: first non-empty line
    for line in content.splitlines():
        if line.strip():
            return line.strip()[:80]
    return "Untitled"


def _extract_quiz_json(content: str) -> str | None:
    """Extract ```json ... ``` block from quiz lesson content."""
    m = re.search(r"```json\s*(\{.*?\})\s*```", content, re.DOTALL)
    if m:
        try:
            parsed = json.loads(m.group(1))
            return json.dumps(parsed, ensure_ascii=False)
        except json.JSONDecodeError as e:
            log.warning("Quiz JSON parse error: %s", e)
    return None


# ─── Core enhancement ────────────────────────────────────────────────────────

async def enhance_lesson(lesson: Lesson, llm: LLMProvider, role: str) -> Lesson:
    """Enhance a single lesson using the LLM. Updates lesson in-place and returns it."""
    template = PROMPT_TEMPLATES[lesson.lesson_type]
    user_prompt = template.format(
        role=role,
        content=lesson.content_enhanced[:4000],  # cap to avoid token overrun
        formulas=_format_formulas(lesson),
    )
    system_prompt = SYSTEM_PROMPT.format(role=role)

    enhanced_text = await llm.generate(system_prompt, user_prompt)

    lesson.title = _extract_title(enhanced_text)
    lesson.content_enhanced = enhanced_text
    lesson.enhancement_status = "completed"

    if lesson.lesson_type == "quiz":
        lesson.quiz_json = _extract_quiz_json(enhanced_text)

    return lesson


def _format_formulas(lesson: Lesson) -> str:
    """Format formula list for prompt injection."""
    # formulas are embedded in the raw content_enhanced text as {{FORMULA_N}} placeholders;
    # also attempt to collect any raw LaTeX snippets visible in the text
    latex_pattern = re.compile(r"\$\$?[^$]+\$\$?|\\\(.*?\\\)|\\\[.*?\\\]", re.DOTALL)
    found = latex_pattern.findall(lesson.content_enhanced[:3000])
    if found:
        return "\n".join(f"- {f}" for f in found[:10])
    return "(see content above)"


# ─── Pipeline orchestrator ────────────────────────────────────────────────────

async def run_enhancer(config: dict):
    """Enhance all pending lessons. Idempotent and resumable."""
    role = config["user"]["role"]
    llm = build_enhancement_provider(config)

    pending = await db.get_pending_lessons()
    if not pending:
        log.info("No pending lessons. Enhancement already complete.")
        return

    log.info("Enhancing %d pending lessons (role: %s)...", len(pending), role)
    succeeded = failed = 0

    for lesson in pending:
        await db.update_lesson_status(lesson.id, "in_progress")
        try:
            enhanced = await enhance_lesson(lesson, llm, role)
            await db.update_lesson_content(enhanced)
            succeeded += 1
            log.info("Enhanced lesson %d [%s] — %s",
                     lesson.id, lesson.lesson_type, enhanced.title[:50])
        except Exception as e:
            failed += 1
            await db.update_lesson_status(lesson.id, "pending")  # allow retry
            log.error("Failed lesson %d [%s]: %s", lesson.id, lesson.lesson_type, e)

    log.info("Enhancement done: %d succeeded, %d failed", succeeded, failed)
