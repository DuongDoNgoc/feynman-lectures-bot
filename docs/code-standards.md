# Feynman Bot - Code Standards

## File Naming Conventions

| File Type | Convention | Example |
|-----------|------------|---------|
| Python modules | `kebab-case.py` | `math_renderer.py` |
| Directories | `kebab-case/` | `src/bot/` |
| Classes | `PascalCase` | `LLMProvider` |
| Functions | `snake_case` | `get_next_lesson()` |
| Constants | `UPPER_SNAKE_CASE` | `USER_AGENTS` |
| Private functions | `_leading_underscore` | `_format_formulas()` |
| Markdown files | `{id:04d}-{type}-{slug}.md` | `0001-concept-electromagnetism.md` |

---

## Code Organization

### Module Structure

```
src/
├── __init__.py           # Empty or module exports
├── utils.py              # Shared utilities (no dependencies on other src modules)
├── bot/                  # Telegram bot layer
├── content/              # Content transformation
├── crawler/              # Web scraping
├── knowledge/            # Database + models
├── llm/                  # LLM providers
└── renderer/             # LaTeX rendering
```

### Import Order

```python
# 1. Standard library
import asyncio
import logging
from pathlib import Path

# 2. Third-party packages
from telegram import Update
from yaml import safe_load

# 3. Local imports
from src.knowledge import db
from src.utils import load_config
```

### File Size Guidelines

- **Target**: Under 200 lines per file
- **Maximum**: 300 lines (split if exceeded)
- **Exceptions**: Database schema definitions, large prompt templates

---

## Python Style Guidelines

### Type Hints

**Required for**:
- Function parameters
- Return values
- Class attributes (dataclasses)

```python
from typing import Optional, List

async def get_next_lesson(user_id: int) -> Optional[Lesson]:
    """Fetch next unread lesson for user."""
    ...

@dataclass
class Chapter:
    id: Optional[int]
    volume: str
    number: int
```

### Docstrings

**Format**: Google-style (concise)

```python
async def enhance_lesson(lesson: Lesson, llm: LLMProvider, role: str) -> Lesson:
    """Enhance a single lesson using the LLM.

    Args:
        lesson: Lesson to enhance with pending content_enhanced
        llm: LLM provider instance
        role: User role for personalization

    Returns:
        Enhanced lesson with completed status

    Raises:
        LLMError: If LLM API call fails
    """
```

### Async/Await Patterns

**Always use async for**:
- I/O operations (database, HTTP, file system)
- LLM API calls
- Telegram bot handlers

**Executor for sync operations**:
```python
from concurrent.futures import ThreadPoolExecutor

async def render_latex(latex: str) -> str:
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as executor:
        return await loop.run_in_executor(executor, sync_render, latex)
```

### Error Handling

```python
# Specific exceptions
try:
    chapter = await db.get_chapter(chapter_id)
except NotFoundError:
    log.warning("Chapter %d not found", chapter_id)
    return None

# Always log errors
except Exception as e:
    log.error("Failed to process chapter %d: %s", chapter_id, e)
    raise

# Cleanup in finally
finally:
    await browser.close()
```

### Logging

**Levels**:
- `DEBUG`: Detailed diagnostic info
- `INFO`: Normal operation milestones
- `WARNING**: Recoverable issues
- `ERROR`: Failures requiring attention

**Format**:
```python
log.info("Processing chapter %d: %s", chapter_id, title)
log.warning("Circuit breaker tripped after %d failures", count)
log.error("LLM API error: %s", str(e))
```

### Context Managers

**Use for**:
- Database connections
- Browser sessions
- File operations

```python
async with get_db() as conn:
    result = await conn.execute_fetchall("SELECT * FROM lessons")

async with create_browser() as (browser, page):
    await page.goto(url)
```

---

## Database Standards

### SQLite Configuration

```python
# Required settings
await conn.execute("PRAGMA journal_mode=WAL")
await conn.execute("PRAGMA foreign_keys=ON")
```

### Query Style

**Use parameterized queries** (never string formatting):
```python
# Correct
await conn.execute("SELECT * FROM lessons WHERE id=?", (lesson_id,))

# Wrong (SQL injection risk)
await conn.execute(f"SELECT * FROM lessons WHERE id={lesson_id}")
```

### Source URL Retrieval Pattern

Pattern for fetching lesson source URL (requires JOIN from lessons → sections → chapters):

```python
async def get_lesson_source_url(lesson_id: int) -> Optional[str]:
    """Fetch source URL for lesson via JOIN chain."""
    query = """
        SELECT c.url FROM lessons l
        JOIN sections s ON l.section_id = s.id
        JOIN chapters c ON s.chapter_id = c.id
        WHERE l.id = ?
    """
    result = await conn.execute_fetchone(query, (lesson_id,))
    return result[0] if result else None
```

### Approval Status Pattern

Column `approval_status` in lessons table tracks content review status:

```python
# Values: "pending" (default) | "approved" | "rejected"
await conn.execute(
    "UPDATE lessons SET approval_status=? WHERE id=?",
    ("approved", lesson_id)
)

# Gated delivery example
lesson = await get_next_lesson(user_id)
if lesson.approval_status == "approved":
    await send_lesson(...)
```

### Naming Conventions

| Entity | Convention | Example |
|--------|------------|---------|
| Tables | `snake_case` | `user_progress` |
| Columns | `snake_case` | `lesson_id` |
| Indexes | `idx_{table}_{column}` | `idx_lessons_status` |

---

## Formula Rendering System

### Single vs. Combined Rendering Decision

```python
def should_combine(formulas: List[str], max_gap: int = 300) -> bool:
    """Decide whether to render as combined block or individual formulas."""
    if len(formulas) < 2:
        return False  # Single formula → pdflatex

    # Check character distance between nearby formulas
    for i in range(len(formulas) - 1):
        gap = get_char_distance(formulas[i], formulas[i+1])
        if gap <= max_gap:
            return True  # Within grouping threshold → xelatex

    return False  # Too far apart → individual pdflatex
```

### Rendering Function Signatures

**Single Formula**:
```python
async def render_with_pdflatex(formula: str, dpi: int) -> str:
    """Render single formula. Fast, high-quality. Returns PNG path."""
    # 1. Hash formula: md5_hash = hashlib.md5(formula.encode()).hexdigest()
    # 2. Check cache: if data/images/{md5_hash}.png exists, return path
    # 3. Write .tex file → pdflatex → pdftoppm → PNG
    # 4. Return path
```

**Combined Block**:
```python
async def render_with_xelatex(block_text: str, dpi: int) -> str:
    """Render combined block with UTF-8 support (DejaVu Serif).

    Returns PNG path with cb_ prefix (cb_abc123def456.png).
    """
    # 1. Hash: md5_hash = hashlib.md5(block_text.encode()).hexdigest()
    # 2. Check cache: if data/images/cb_{md5_hash}.png exists, return
    # 3. Build template with fontspec + minipage(12cm)
    # 4. xelatex → PDF → pdftoppm → PNG
    # 5. Return path
```

### xelatex Template Pattern

```python
XELATEX_TEMPLATE = r"""
\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage{fontspec}
\setmainfont{DejaVu Serif}
\usepackage{amsmath,amssymb,amsfonts}
\pagestyle{empty}
\usepackage[margin=0.5cm]{geometry}
\begin{document}
\begin{minipage}{12cm}
{content}
\end{minipage}
\end{document}
"""
```

### Block Dictionary Structure

Store in `lessons.math_images_json` as JSON array:

```python
@dataclass
class RenderBlock:
    type: str  # "single" or "combined"
    path: str  # "data/images/abc123.png" or "data/images/cb_abc123.png"
    start: int  # Character position in original content
    end: int    # Character position in original content
```

### Grouping Logic Implementation

```python
def _group_nearby_formulas(
    formulas: List[Tuple[str, int, int]],
    content: str,
    max_gap: int = 300
) -> List[List[int]]:
    """Group nearby formulas into blocks.

    Args:
        formulas: List of (text, start, end) tuples
        content: Original lesson content
        max_gap: Max char distance to group (default 300)

    Returns:
        List of groups, each group is list of formula indices
    """
    # Iterate through formulas; if gap to next < max_gap, same group
    # Otherwise, start new group
```

### Real LaTeX Filter Pattern

```python
def _is_real_latex(formula: str) -> bool:
    """Filter out false positives (plain text, single var, etc)."""

    # Reject: single variable, numbers, abbreviations
    if formula in SINGLE_VAR_CACHE or formula.isdigit():
        return False

    # Reject: plain text without operators
    latex_operators = {
        r'\alpha', r'\beta', r'\int', r'\sum', r'\frac',
        r'\sqrt', r'\sin', r'\cos', '^', '_', '=', '+'
    }

    if not any(op in formula for op in latex_operators):
        return False

    return True
```

### Configuration Keys

In `config.yaml`:

```yaml
renderer:
  output_dir: data/images/
  dpi: 1200
  max_blocks_per_lesson: 50       # Cap on formula groups
  group_max_gap: 300              # Char distance for grouping formulas
```

### Filename Convention

- **Single formula**: `{md5(formula)}.png`
  - Example: `a1b2c3d4e5f6g7h8.png`

- **Combined block**: `cb_{md5(block_text)}.png`
  - Example: `cb_x9y8z7w6v5u4t3.png`

- **Table**: `tbl_{md5(table_text)}.png`
  - Example: `tbl_m9n8o7p6q5r4s3.png`

### Table Rendering

**See**: [Table Rendering Feature](./table-rendering.md)

**Quick Implementation**:
- Tables detected via `_extract_table_positions()` using regex pattern
- Markdown → LaTeX conversion via `_markdown_table_to_latex()`
- PNG rendering via `render_table()` using xelatex
- Block dictionary format: `{type: "table", path: "tbl_*.png", start, end}`
- Backfill script: `python scripts/backfill-tables.py`

---

## Message Delivery Patterns

### Interleaved Segments Pattern

Function: `_build_interleaved_segments(lesson: Lesson) -> List[Union[str, ImagePath]]`

Creates a list alternating text chunks and image paths based on `math_images_json`:

```python
# Input: lesson with content and math_images_json
# Process:
#   1. Parse math_images_json blocks with char positions
#   2. Split content by block positions
#   3. Create segments: [text_chunk_0, image_0, text_chunk_1, image_1, ...]
# Output: List suitable for send_lesson() iteration
```

### Coalescing Segments

Function: `_coalesce_segments(segments: List) -> List[Union[str, ImagePath]]`

Merges adjacent text segments if combined length < 4096 chars (Telegram limit):

```python
# Input: [text_300, image, text_200, text_500, image]
# Output: [text_300, image, text_700, image]  # Merged middle texts
```

### Message Splitting

Function: `split_message(text: str, max_length: int = 4096) -> List[str]`

Splits long text respecting Telegram limits:

```python
# Strategy: Paragraph-aware first
# 1. Try split by \n\n (paragraph breaks)
# 2. Fallback to \n (line breaks)
# 3. Fallback to word boundaries
# 4. Last resort: character split (with safety margin)
```

### Lesson Delivery with Source URL

```python
async def send_lesson(user_id: int, lesson: Lesson):
    """Send lesson segments and append source URL."""

    segments = _build_interleaved_segments(lesson)
    segments = _coalesce_segments(segments)

    for segment in segments:
        if isinstance(segment, str):
            parts = split_message(segment)
            for part in parts:
                await bot.send_message(chat_id=user_id, text=part)
        else:  # ImagePath
            await bot.send_photo(chat_id=user_id, photo=open(segment, 'rb'))

    # Append source URL as final message
    source_url = await db.get_lesson_source_url(lesson.id)
    if source_url:
        await bot.send_message(
            chat_id=user_id,
            text=f"📖 Nguồn: {source_url}"
        )

    await db.mark_sent(user_id, lesson.id)
```

---

## API Design

### LLM Provider Interface

```python
class LLMProvider:
    """Unified interface for LLM providers."""

    async def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        history: Optional[List[dict]] = None,
    ) -> str:
        """Generate completion with optional conversation history."""
        raise NotImplementedError
```

### Handler Signatures

```python
async def command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Telegram command handler signature."""
    chat_id = update.effective_chat.id
    user_text = update.message.text
    ...
```

---

## CLI Tool Patterns

### Argument Parsing

Use `argparse` with subcommands for multi-function CLIs:

```python
parser = argparse.ArgumentParser(description="Tool description")
subparsers = parser.add_subparsers(dest="command", help="Command")

# Add subcommands
export_parser = subparsers.add_parser("export", help="Export function")
export_parser.add_argument("--id", type=int, help="Specific item ID")
export_parser.add_argument("--type", choices=["a", "b", "c"], help="Filter by type")

args = parser.parse_args()
```

### Colored Terminal Output

Use ANSI escape codes for status indication:

```python
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

print(f"{GREEN}Success:{RESET} Operation completed")
print(f"{YELLOW}Warning:{RESET} Check output")
print(f"{RED}Error:{RESET} Operation failed")
```

### Confirmation Prompts

Require user confirmation for destructive bulk operations:

```python
if args.all:
    if not args.yes:
        print(f"{YELLOW}Warning:{RESET} This will affect {count} items.")
        response = input("Continue? [y/N] ")
        if response.lower() != "y":
            print("Cancelled.")
            return 1
```

---

## Markdown File Conventions

### Frontmatter Format

YAML frontmatter for generated markdown files:

```yaml
---
lesson_id: 1
lesson_type: concept
approval_status: pending
exported_at: "2026-02-28T12:34:56+00:00"
content_hash: "a1b2c3d4e5f6"
chapter_number: 1
chapter_title: "Atoms in Motion"
---
```

### Filename Pattern

For lesson preview exports:
- Format: `{id:04d}-{type}-{slug}.md`
- Example: `0001-concept-atoms-in-motion.md`
- Slug: lowercase, hyphens, max 50 chars

---

## Configuration Management

### config.yaml Structure

```yaml
section:
  key: value              # Simple value
  key: ${ENV_VAR}         # Environment variable
  key:                    # Nested object
    subkey: value
  key: [1, 2, 3]          # List
```

### Access Pattern

```python
# Safe nested access
value = config.get("section", {}).get("key", default_value)

# Required keys (raise if missing)
token = config["telegram"]["bot_token"]
```

### Renderer Configuration Keys

```yaml
renderer:
  output_dir: data/images/          # Where PNG images stored
  dpi: 1200                         # Resolution (1200 recommended)
  max_blocks_per_lesson: 50         # Cap on combined blocks
  group_max_gap: 300                # Char distance for grouping
  cache_enabled: true               # MD5 cache toggle
```

**Cache Invalidation**: If you change `dpi`, delete all PNG files in `output_dir` before re-rendering. Cache uses MD5(formula), so higher DPI won't regenerate automatically.

---

## Prompt Engineering

### System Prompts

**Location**: Module-level constants

```python
SYSTEM_PROMPT = """Bạn là giảng viên vật lý giỏi.
Người học là {role} người Việt Nam.
Giữ công thức LaTeX trong $...$."""
```

### Template Patterns

```python
PROMPT_TEMPLATE = """Dựa vào nội dung sau, viết {lesson_type} bài giảng.

YÊU CẦU:
- Độ dài: {word_count} từ
- Ngôn ngữ: tiếng Việt xen tiếng Anh

NỘI DUNG:
{content}

CÔNG THỨC:
{formulas}
"""
```

---

## Testing Standards

### End-to-End Tests

**Location**: `scripts/test-e2e.py`

**Coverage**:
- Pipeline execution (all stages)
- Database state verification
- Basic bot commands

### Test Structure

```python
async def test_pipeline_flow():
    # 1. Setup
    config = load_config("test_config.yaml")
    await init_db(config)

    # 2. Execute
    await run_crawler(config)
    chapters = await db.get_all_chapters()
    assert len(chapters) > 0

    # 3. Cleanup
    os.remove("test.db")
```

---

## Security Guidelines

### API Keys

**Never commit**:
- `.env` files
- API keys in code
- Hardcoded credentials

**Always use**:
- Environment variables
- `config.yaml` with `${VAR}` placeholders
- `.gitignore` for sensitive files

### Input Validation

```python
# Sanitize user inputs
keyword = " ".join(context.args).lower()[:100]  # Limit length

# Validate chat_id
if str(chat_id) != config["telegram"]["chat_id"]:
    log.warning("Unauthorized chat_id: %s", chat_id)
    return
```

---

## Git Commit Conventions

### Commit Message Format

```
type(scope): brief description

Detailed explanation (optional)
```

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `refactor`: Code restructuring
- `docs`: Documentation
- `test`: Test additions
- `chore`: Maintenance

**Examples**:
```
feat(bot): add /search command for keyword lookup
fix(crawler): handle missing MathJax gracefully
docs(readme): update installation instructions
```

---

## Code Review Checklist

- [ ] File names follow `kebab-case`
- [ ] Functions have type hints
- [ ] Docstrings for public APIs
- [ ] Async/await used for I/O
- [ ] Errors logged with context
- [ ] No hardcoded credentials
- [ ] Parameterized SQL queries
- [ ] Message length handling (4096 char limit)
- [ ] Under 200 lines per file (or split)
- [ ] Tests added for new features

---

## Performance Guidelines

### Database

- Use indexes for frequently queried columns
- Batch operations where possible
- Close connections via context managers

### LLM Calls

- Implement rate limiting
- Cache results when idempotent
- Use appropriate models (Haiku for batch, Chat for interactive)

### Crawler

- Respect rate limits
- Implement circuit breaker
- Use connection pooling

---

## Documentation Standards

### README.md

**Required sections**:
- Project description
- Quick start guide
- Installation steps
- Configuration
- Usage examples
- Project structure overview

### Module Docs

**Inline**:
- Docstrings for classes/functions
- Comments for complex logic
- Type hints throughout

### External

- Architecture diagrams (Mermaid)
- API specifications
- Deployment guides

---

## Linter Configuration

**Recommended**:
```bash
# Install
pip install ruff black

# Format
black src/

# Lint
ruff check src/
```

**Tolerate**:
- Line length > 88 (black default) - use 100
- Minor style issues - prioritize readability

**Reject**:
- Syntax errors
- Undefined variables
- Missing imports
