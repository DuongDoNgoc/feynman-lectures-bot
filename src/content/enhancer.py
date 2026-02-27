"""LLM-based lesson enhancer — Claude Code session workflow.

Flow:
  Step 1: pipeline.py --stage enhance
          → generates data/pending_prompts.jsonl (one JSON per line)
          → prints instructions for Claude Code session

  Step 2: Claude Code reads + processes each prompt in data/pending_prompts.jsonl
          → writes results to data/enhanced_outputs.jsonl

  Step 3: pipeline.py --stage enhance --import
          → imports data/enhanced_outputs.jsonl into DB (idempotent)

This avoids Anthropic API costs — uses Claude Code subscription instead.
For automated/API mode, set ENHANCEMENT_PROVIDER=api in env (uses config.yaml).
"""
import json
import logging
import os
import re

from src.knowledge import db
from src.knowledge.models import Lesson

log = logging.getLogger(__name__)

PROMPTS_FILE = "data/pending_prompts.jsonl"
OUTPUTS_FILE = "data/enhanced_outputs.jsonl"

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
    for line in content.splitlines():
        line = line.strip()
        if line.startswith("#"):
            return re.sub(r"^#+\s*", "", line).strip()
    for line in content.splitlines():
        if line.strip():
            return line.strip()[:80]
    return "Untitled"


def _normalize_content(content: str) -> str:
    """Fix common LLM heading artifacts.

    Haiku sometimes outputs '# ## Title' (h1 + h2 prefix) instead of '## Title'.
    Collapse repeated leading hashes on the first heading line to the innermost level.
    """
    lines = content.splitlines()
    if lines:
        # Replace any run of '#' followed by spaces + more '#' (e.g. '# ## ') with
        # just the last hash group to preserve the intended heading level.
        lines[0] = re.sub(r"^#+\s+(#+\s+)", r"\1", lines[0])
    return "\n".join(lines)


def _extract_quiz_json(content: str) -> str | None:
    m = re.search(r"```json\s*(\{.*?\})\s*```", content, re.DOTALL)
    if m:
        try:
            return json.dumps(json.loads(m.group(1)), ensure_ascii=False)
        except json.JSONDecodeError as e:
            log.warning("Quiz JSON parse error: %s", e)
    return None


def _format_formulas(content: str) -> str:
    latex_pattern = re.compile(r"\$\$?[^$]+\$\$?|\\\(.*?\\\)|\\\[.*?\\\]", re.DOTALL)
    found = latex_pattern.findall(content[:3000])
    return "\n".join(f"- {f}" for f in found[:10]) if found else "(see content above)"


def _build_prompt(lesson: Lesson, role: str) -> str:
    template = PROMPT_TEMPLATES[lesson.lesson_type]
    return template.format(
        role=role,
        content=lesson.content_enhanced[:4000],
        formulas=_format_formulas(lesson.content_enhanced),
    )


# ─── Step 1: Generate prompts file ────────────────────────────────────────────

async def generate_prompts(config: dict):
    """Write pending lessons as prompts to data/pending_prompts.jsonl."""
    role = config["user"]["role"]
    os.makedirs("data", exist_ok=True)

    pending = await db.get_pending_lessons()
    if not pending:
        log.info("No pending lessons. Enhancement already complete.")
        return 0

    # Load already-output lesson IDs to skip
    done_ids = _load_done_ids()

    written = 0
    with open(PROMPTS_FILE, "a") as f:  # append mode = resumable
        for lesson in pending:
            key = f"{lesson.id}_{lesson.lesson_type}"
            if key in done_ids:
                continue
            system = SYSTEM_PROMPT.format(role=role)
            user_prompt = _build_prompt(lesson, role)
            record = {
                "lesson_id": lesson.id,
                "lesson_type": lesson.lesson_type,
                "sequence": lesson.sequence,
                "system": system,
                "prompt": user_prompt,
            }
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
            written += 1

    log.info("Wrote %d prompts to %s", written, PROMPTS_FILE)

    if written > 0:
        print(f"""
╔══════════════════════════════════════════════════════════════╗
║         ENHANCEMENT: Claude Code Session Required            ║
╠══════════════════════════════════════════════════════════════╣
║  {written} lessons need enhancement.                         ║
║                                                              ║
║  Ask Claude Code to run:                                     ║
║    "Process enhancement prompts in data/pending_prompts.jsonl║
║     and write results to data/enhanced_outputs.jsonl"        ║
║                                                              ║
║  Then import results:                                        ║
║    python pipeline.py --stage enhance --import               ║
╚══════════════════════════════════════════════════════════════╝
""")
    return written


# ─── Step 2 (done by Claude Code): process prompts → outputs ─────────────────
# Claude Code reads PROMPTS_FILE, generates enhanced content, writes OUTPUTS_FILE
# Format per line: {"lesson_id": N, "lesson_type": "...", "content": "...enhanced..."}


# ─── Step 3: Import outputs into DB ──────────────────────────────────────────

async def import_outputs(config: dict):
    """Import enhanced_outputs.jsonl into DB. Idempotent."""
    if not os.path.exists(OUTPUTS_FILE):
        log.error("No outputs file found: %s", OUTPUTS_FILE)
        return

    succeeded = failed = skipped = 0
    with open(OUTPUTS_FILE) as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
                lesson_id = record["lesson_id"]
                content = record["content"]
            except (json.JSONDecodeError, KeyError) as e:
                log.warning("Line %d malformed: %s", line_num, e)
                failed += 1
                continue

            # Fetch the lesson
            from src.knowledge.db import get_db, _row_to_lesson
            async with get_db() as conn:
                rows = await conn.execute_fetchall(
                    "SELECT * FROM lessons WHERE id=?", (lesson_id,)
                )
            if not rows:
                log.warning("Lesson %d not found in DB", lesson_id)
                skipped += 1
                continue

            lesson = _row_to_lesson(rows[0])
            if lesson.enhancement_status == "completed":
                skipped += 1
                continue

            lesson.title = _extract_title(content)
            lesson.content_enhanced = content
            lesson.enhancement_status = "completed"
            if lesson.lesson_type == "quiz":
                lesson.quiz_json = _extract_quiz_json(content)

            await db.update_lesson_content(lesson)
            succeeded += 1

    log.info("Import done: %d succeeded, %d failed, %d skipped", succeeded, failed, skipped)


# ─── Orchestrator ─────────────────────────────────────────────────────────────

async def run_enhancer(config: dict, import_mode: bool = False):
    if import_mode:
        await import_outputs(config)
    else:
        await generate_prompts(config)


def _load_done_ids() -> set[str]:
    """Return set of 'lesson_id_lesson_type' already in outputs file."""
    done = set()
    if not os.path.exists(OUTPUTS_FILE):
        return done
    with open(OUTPUTS_FILE) as f:
        for line in f:
            try:
                r = json.loads(line.strip())
                done.add(f"{r['lesson_id']}_{r.get('lesson_type','')}")
            except Exception:
                pass
    return done
