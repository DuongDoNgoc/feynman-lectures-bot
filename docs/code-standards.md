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

### Naming Conventions

| Entity | Convention | Example |
|--------|------------|---------|
| Tables | `snake_case` | `user_progress` |
| Columns | `snake_case` | `lesson_id` |
| Indexes | `idx_{table}_{column}` | `idx_lessons_status` |

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
