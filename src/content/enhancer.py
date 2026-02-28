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


def _format_formulas(formulas: list[str]) -> str:
    """Format a list of LaTeX formula strings for inclusion in LLM prompts."""
    if not formulas:
        return "(không có công thức riêng biệt)"
    # Wrap each formula in $...$ so the LLM sees proper LaTeX delimiters
    lines = [f"- ${f}$" for f in formulas[:15] if f.strip()]
    return "\n".join(lines) if lines else "(không có công thức riêng biệt)"


def _build_prompt(lesson: Lesson, role: str, formulas: list[str] | None = None) -> str:
    template = PROMPT_TEMPLATES[lesson.lesson_type]
    return template.format(
        role=role,
        content=lesson.content_enhanced[:4000],
        formulas=_format_formulas(formulas or []),
    )


# ─── Step 1: Generate prompts file ────────────────────────────────────────────

async def generate_prompts(config: dict, batch_size: int = 0):
    """Write pending lessons as prompts to data/pending_prompts.jsonl.

    Args:
        batch_size: Max lessons to process. 0 means all pending.
    """
    role = config["user"]["role"]
    os.makedirs("data", exist_ok=True)

    # Clear stale files so each batch run is clean
    for f in [PROMPTS_FILE, OUTPUTS_FILE]:
        if os.path.exists(f):
            os.remove(f)
            log.info("Cleared stale file: %s", f)

    pending = await db.get_pending_lessons()
    if not pending:
        log.info("No pending lessons. Enhancement already complete.")
        return 0

    # Apply batch limit
    if batch_size > 0:
        pending = pending[:batch_size]
        log.info("Batch mode: processing %d of available lessons", len(pending))

    # Load already-output lesson IDs to skip
    done_ids = _load_done_ids()

    # Pre-fetch section formulas keyed by section_id to avoid N+1 queries
    section_formulas = await db.get_section_formulas_map()

    written = 0
    with open(PROMPTS_FILE, "a") as f:  # append mode = resumable
        for lesson in pending:
            key = f"{lesson.id}_{lesson.lesson_type}"
            if key in done_ids:
                continue
            system = SYSTEM_PROMPT.format(role=role)
            formulas = section_formulas.get(lesson.section_id, [])
            user_prompt = _build_prompt(lesson, role, formulas=formulas)
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


# ─── Direct API enhancement ───────────────────────────────────────────────────

async def enhance_direct(config: dict, batch_size: int = 30):
    """Call the Anthropic API directly to enhance lessons — no manual step needed.

    Uses config.enhancement settings. Auto-approves each lesson after success.

    Args:
        batch_size: Max lessons to process per run (default 30).
    """
    import anthropic
    import asyncio

    econf = config.get("enhancement", {})
    api_key = os.environ.get("ANTHROPIC_API_KEY") or econf.get("api_key", "")
    model = econf.get("model", "claude-haiku-4-5-20251001")
    temperature = econf.get("temperature", 0.7)
    max_tokens = econf.get("max_tokens", 3500)
    delay = econf.get("request_delay", 1.0)
    role = config["user"]["role"]

    client = anthropic.Anthropic(api_key=api_key)
    pending = await db.get_pending_lessons()
    if not pending:
        log.info("No pending lessons to enhance.")
        return 0

    if batch_size > 0:
        pending = pending[:batch_size]

    section_formulas = await db.get_section_formulas_map()
    succeeded = failed = 0

    for lesson in pending:
        formulas = section_formulas.get(lesson.section_id, [])
        system_msg = SYSTEM_PROMPT.format(role=role)
        user_prompt = _build_prompt(lesson, role, formulas=formulas)

        try:
            response = client.messages.create(
                model=model,
                max_tokens=max_tokens,
                temperature=temperature,
                system=system_msg,
                messages=[{"role": "user", "content": user_prompt}],
            )
            content = _normalize_content(response.content[0].text)
            lesson.title = _extract_title(content)
            lesson.content_enhanced = content
            lesson.enhancement_status = "completed"
            if lesson.lesson_type == "quiz":
                lesson.quiz_json = _extract_quiz_json(content)
            await db.update_lesson_content(lesson)
            # Auto-approve after successful enhancement
            await db.set_approval_status(lesson.id, "approved")
            succeeded += 1
            log.info("Enhanced+approved lesson %d: %s", lesson.id, lesson.title[:50])
        except Exception as e:
            log.error("Failed lesson %d: %s", lesson.id, e)
            failed += 1

        await asyncio.sleep(delay)

    log.info("Direct enhance: %d succeeded, %d failed (of %d)", succeeded, failed, len(pending))
    return succeeded


# ─── Orchestrator ─────────────────────────────────────────────────────────────

async def run_enhancer(config: dict, import_mode: bool = False, batch_size: int = 0,
                       direct: bool = False):
    if import_mode:
        await import_outputs(config)
    elif direct:
        await enhance_direct(config, batch_size=batch_size)
    else:
        await generate_prompts(config, batch_size=batch_size)


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
