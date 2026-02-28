# Feynman Bot - Codebase Summary

## Executive Summary

Feynman Bot is a Python-based automated learning system consisting of two main components:
1. **Content Pipeline** (`pipeline.py`): 5-stage offline batch processing for content acquisition and enhancement
2. **Telegram Bot** (`main.py`): Interactive service for lesson delivery and Q&A

The codebase follows a modular architecture with clear separation of concerns across 7 modules.

---

## Module Structure

```
src/
├── bot/              # Telegram bot application layer
├── content/          # Content transformation (chunking, enhancement)
├── crawler/          # Web scraping and HTML parsing
├── knowledge/        # Database layer and data models
├── llm/              # Unified LLM provider interface
├── renderer/         # LaTeX to PNG conversion
└── utils.py          # Configuration, logging, validation
```

---

## Module Details

### 1. Bot Module (`src/bot/`)

**Purpose**: Telegram bot application and command handlers

**Files**:
- `bot.py` (91 lines): Application factory and bot runner
- `handlers.py` (600+ lines): Command/message handlers with error handling ⚠️ exceeds 200-line guideline
- `scheduler.py` (172 lines): JobQueue-based lesson scheduling

**Key Functions**:

| File | Function | Purpose |
|------|----------|---------|
| `bot.py` | `create_app(config)` | Build Telegram Application |
| `bot.py` | `run_bot(config)` | Start bot polling (blocking) |
| `handlers.py` | `start_handler()` | Welcome message |
| `handlers.py` | `next_handler()` | Deliver next lesson |
| `handlers.py` | `quiz_handler()` | Send interactive quiz |
| `handlers.py` | `message_handler()` | Free-form Q&A |
| `handlers.py` | `split_message()` | Split text for 4096-char limit |
| `handlers.py` | `error_handler()` | Global exception handler |
| `scheduler.py` | `setup_schedule()` | Configure daily delivery times |
| `scheduler.py` | `catchup_missed_lessons()` | Resume missed deliveries |

**Error Handling (2026-02-28)**:
- `ERROR_MESSAGES` dict: Vietnamese user-friendly messages
- All handlers wrapped in try/except
- LLM-specific error handling (retry exhausted, timeout)
- Database error recovery
- Graceful degradation on failures

**Commands Implemented**:
- `/start`, `/next`, `/quiz`, `/explain`, `/example`
- `/progress`, `/schedule`, `/role`, `/search`, `/help`

### 2. Content Module (`src/content/`)

**Purpose**: Transform raw content into enhanced lessons

**Files**:
- `chunker.py` (120+ lines): Section to chunk conversion with semantic title generation
- `enhancer.py` (286 lines): Claude Code session workflow for enhancement
- `preview_exporter.py` (287 lines): Export lessons to markdown for review

**Key Functions**:

| File | Function | Purpose |
|------|----------|---------|
| `chunker.py` | `run_chunker(config)` | Split sections into chunks with target 2000w |
| `chunker.py` | `chunk_sections()` | Per-chapter semantic chunking, generates titles "ChN-M: Title — type" |
| `enhancer.py` | `generate_prompts(config)` | Create pending_prompts.jsonl |
| `enhancer.py` | `import_outputs(config)` | Import enhanced_outputs.jsonl |
| `enhancer.py` | `run_enhancer(config, import_mode)` | Orchestrator |
| `enhancer.py` | `_extract_title()` | Extract title from content |
| `enhancer.py` | `_extract_quiz_json()` | Parse quiz answers |
| `preview_exporter.py` | `export_lesson(lesson_id)` | Export single lesson to markdown |
| `preview_exporter.py` | `export_all_lessons()` | Export all completed lessons |
| `preview_exporter.py` | `export_lessons_by_type(type)` | Export by lesson type |

**Chunker Update (2026-02-28)**: Now processes per-chapter sections with target 2000-word lessons. Title format: "ChN-M: Section Title — type" (e.g., "Ch1-2: Conservation of Energy — concept"). Results: 843 lessons total (was 282), meaningful topic-based titles.

**Enhancement Workflow**:
- **Step 1**: `generate_prompts()` writes `data/pending_prompts.jsonl`
- **Step 2**: Claude Code processes prompts → `data/enhanced_outputs.jsonl`
- **Step 3**: `import_outputs()` imports results into database
- **Optional**: Set `ENHANCEMENT_PROVIDER=api` for direct API mode

**Lesson Types**:
- `concept`: ~800 words, intuitive intro with analogies
- `deep_dive`: ~1000 words, detailed derivations
- `quiz`: ~600 words, 3 MCQs + 1 open-ended

### 3. Crawler Module (`src/crawler/`)

**Purpose**: Web scraping and HTML parsing

**Files**:
- `scraper.py` (243 lines): Playwright-based stealth crawler
- `parser.py` (250+ lines): HTML/LaTeX extraction with recursive heading detection

**Key Functions**:

| File | Function | Purpose |
|------|----------|---------|
| `scraper.py` | `run_crawler(config)` | Main crawler orchestrator |
| `scraper.py` | `get_chapter_list()` | Extract chapter links |
| `scraper.py` | `crawl_chapter()` | Fetch chapter HTML |
| `scraper.py` | `download_images()` | Save referenced images |
| `scraper.py` | `create_browser()` | Context manager with stealth |
| `parser.py` | `run_parser(config)` | Parse all uncrawled chapters |
| `parser.py` | `extract_sections()` | Recursive h2/h3 heading detection via `find_all()` |
| `parser.py` | `extract_latex()` | Multi-method formula extraction |

**Parser Fix (2026-02-28)**: Now uses `content.find_all(HEADING_TAGS)` recursive search instead of direct children iteration, detecting h2/h3 headings at any nesting depth. Results: 607 sections across 94 chapters (~6.5/chapter), up from 94 sections (1/chapter).

**Anti-Detection Features**:
- Random user agents
- `playwright-stealth` plugin
- Webdriver override
- Exponential backoff retry
- Circuit breaker (20 failures)

### 4. Knowledge Module (`src/knowledge/`)

**Purpose**: Database layer and data models

**Files**:
- `models.py` (90 lines): Dataclass definitions
- `db.py` (473 lines): SQLite async operations
- `preview_db.py` (153 lines): Preview workflow queries

**Key Functions**:

| File | Function | Purpose |
|------|----------|---------|
| `db.py` | `init_db(config)` | Create tables and indexes |
| `db.py` | `get_db()` | Async connection context manager |
| `db.py` | `get_next_lesson()` | Fetch next unread lesson |
| `db.py` | `get_progress_stats()` | Calculate completion/streak |
| `db.py` | `get_conversation_history()` | Retrieve Q&A context |
| `db.py` | `save_quiz_score()` | Record quiz results |
| `preview_db.py` | `get_completed_lessons()` | Fetch all enhanced lessons |
| `preview_db.py` | `get_lessons_by_approval_status(status)` | Filter by approval status |
| `preview_db.py` | `update_approval_status(lesson_id, status)` | Mark approved/rejected |
| `preview_db.py` | `bulk_update_approval_status(status)` | Batch update |

**Database Schema**:
- `chapters`: Raw HTML from website
- `sections`: Parsed content with formulas
- `lessons`: Enhanced content by type (with approval_status: pending/approved/rejected)
- `user_progress`: Tracking sent/read/scores
- `conversation_history`: Q&A context
- `scheduled_lessons`: Delivery queue

### 5. LLM Module (`src/llm/`)

**Purpose**: Unified interface for multiple LLM providers with retry logic

**Files**:
- `provider.py` (180 lines): Anthropic/OpenAI-compatible client with exponential backoff

**Key Functions**:

| Function | Purpose |
|----------|---------|
| `LLMProvider.generate()` | Async completion with history + retry |
| `build_enhancement_provider()` | Anthropic Claude for pipeline |
| `build_qa_provider()` | DeepSeek for bot Q&A |

**Error Classes**:
| Class | Purpose |
|-------|---------|
| `LLMError` | Base exception for LLM operations |
| `LLMRetryExhaustedError` | All retry attempts failed |

**Retry Configuration** (config.yaml):
- `max_retries`: Number of retry attempts (default: 3)
- `retry_base_delay`: Initial delay in seconds (default: 2)
- `retry_max_delay`: Maximum delay cap (default: 30)

**Retry Behavior**:
- Exponential backoff: `delay = min(base * 2^(attempt-1), max)`
- Retries on: ConnectionError, TimeoutError
- Non-retryable: Auth errors, rate limits

**Providers**:
- Enhancement: `claude-sonnet-4-6`
- Q&A: `deepseek-chat`

### 6. Renderer Module (`src/renderer/`)

**Purpose**: LaTeX to PNG conversion with grouped block rendering

**Files**:
- `math_renderer.py` (217 lines): Formula rendering pipeline ⚠️ exceeds 200-line guideline

**Key Functions**:

| Function | Purpose |
|----------|---------|
| `run_renderer(config)` | Process all pending lessons |
| `render_lesson_math()` | Route to pdflatex or xelatex per lesson |
| `render_latex_pdflatex()` | Single formula (fast) |
| `render_combined_block()` | Combined blocks (xelatex, UTF-8, fontspec) |
| `_group_nearby_formulas()` | Group formulas within 300 chars |
| `_is_real_latex()` | Filter false positives (plain text, single vars) |

**Features**:
- **Two-tier rendering**: Single (pdflatex) vs. Combined (xelatex+fontspec)
- **Grouped blocks**: Nearby formulas (<300 char gap) merged into xelatex minipage(12cm) images
- **Block dictionary**: `math_images_json` stores `{type, path, start, end}` for each block
- **Filename convention**: Single: `{md5_hash}.png`, Combined: `cb_{md5_hash}.png`
- **MD5-based caching**: Same formula re-rendered instantly from cache
- **Block cap**: Max 50 combined blocks per lesson
- **DPI**: Configurable 1200 (from config.yaml) for high-quality LaTeX
- **Async-safe via executor**: Blocking LaTeX commands run in thread pool
- **DejaVu Serif font**: UTF-8 Vietnamese support in combined blocks via fontspec

### 7. Utils (`src/utils.py`)

**Purpose**: Shared utilities

**Key Functions**:

| Function | Purpose |
|----------|---------|
| `load_config()` | Load YAML with env var resolution |
| `validate_config()` | Assert required fields exist |
| `setup_logging()` | Configure file + console logging |
| `_get_nested()` | Dot-notation dict access |

---

## Source URL Delivery Feature

**Purpose**: Attribute content to source chapters on Feynman Lectures website

**Implementation**: Added in handlers.py `send_lesson()` function

**Workflow**:

1. Bot retrieves next approved lesson
2. Handler calls `db.get_lesson_source_url(lesson_id)` which:
   - JOINs lessons → sections → chapters
   - Returns `chapters.url` from source
3. After delivering all lesson segments and images, appends:
   ```
   📖 Nguồn: https://www.feynmanlectures.caltech.edu/I_01.html
   ```
4. Users can click link to see full Feynman Lecture chapter

**Database Pattern** (`src/knowledge/db.py`):

```python
async def get_lesson_source_url(lesson_id: int) -> Optional[str]:
    """Fetch source URL via lessons→sections→chapters JOIN."""
    query = """
        SELECT c.url FROM lessons l
        JOIN sections s ON l.section_id = s.id
        JOIN chapters c ON s.chapter_id = c.id
        WHERE l.id = ?
    """
    result = await conn.execute_fetchone(query, (lesson_id,))
    return result[0] if result else None
```

---

## Approval Workflow Feature

**Purpose**: Human review gate before lesson delivery

**Implementation**: Lessons tracked with `approval_status` column (pending | approved | rejected)

**Flow**:

1. **Stage 4 (Enhancement)** → All new lessons: `approval_status = "pending"`
2. **Preview Export** (`scripts/lesson-preview.py export`) → Creates markdown files with YAML frontmatter
3. **Human Review** → Editor opens markdown, evaluates quality
4. **Approval** → `python scripts/lesson-preview.py approve --id 5` → Sets `approval_status = "approved"`
5. **Bot Delivery Gate** → `send_lesson()` checks: only deliver if `lesson.approval_status == "approved"`
6. **Scheduler Gate** → Scheduled jobs skip non-approved lessons automatically

**Components**:

- **Preview DB** (`src/knowledge/preview_db.py`): Queries for approved/pending/rejected lessons
- **Preview Exporter** (`src/content/preview_exporter.py`): Export to markdown with frontmatter
- **Preview CLI** (`scripts/lesson-preview.py`): Approve/reject/list commands
- **Bot Handlers** (`src/bot/handlers.py`): Delivery gates check `approval_status`

**CLI Commands**:

```bash
python scripts/lesson-preview.py export          # Export pending to markdown
python scripts/lesson-preview.py list --status pending
python scripts/lesson-preview.py approve --id 5
python scripts/lesson-preview.py approve --all   # Bulk approve
python scripts/lesson-preview.py reject --id 5
```

---

## Current Data Status (2026-02-28)

**Database**: `data/feynman.db`
- **Total Lessons**: 843 lessons (up from 282 after parser/chunker fix)
- **Sections**: 607 sections across 94 chapters (avg 6.5/chapter, was 1)
- **Enhanced Lessons**: 19 completed lessons in `enhanced_outputs.jsonl`
- **Pending Lessons**: 824 lessons awaiting enhancement in `pending_prompts.jsonl`
- **Rendered Images**: 263+ PNG formula images in `data/images/`

**Processing Progress**:
- Parser: Sections per chapter increased from 1 → 6.5 (recursive h2/h3 detection)
- Chunker: Lessons increased from 282 → 843 with semantic titles
- Enhancement: ~2.3% complete (19/843 lessons total)
- Rendering: 263+ formula blocks rendered with grouped xelatex blocks
- Approval: Workflow implemented; lessons gated at delivery
- Pipeline: Stages 1-3 (crawl, parse, chunk) complete; enhancement in progress

---

## Data Flow

### Pipeline Flow
```
crawl → parse → chunk → enhance → render
  ↓        ↓        ↓        ↓         ↓
chapters sections chunks lessons  PNG images
```

### Bot Runtime Flow
```
User Input → Handler → DB Query → LLM (optional) → Response
Scheduler → JobQueue → next_lesson → Delivery
```

---

## Configuration

**File**: `config.yaml`

| Section | Key Settings |
|---------|--------------|
| `telegram` | Bot token, chat ID |
| `schedule` | Times, timezone, lesson types |
| `crawler` | Daily limit, circuit breaker, retries |
| `enhancement` | Provider, model, API key |
| `qa` | Provider, model, history limit |
| `user` | Role, language |
| `chunker` | Target words, tolerance |
| `renderer` | DPI, output directory |

**Environment Variables** (`.env`):
- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_CHAT_ID`
- `ANTHROPIC_API_KEY`
- `DEEPSEEK_API_KEY`

---

## Entry Points

### Pipeline Entry Point (`pipeline.py`)

**Stages**: `crawl`, `parse`, `chunk`, `enhance`, `render`

```bash
python pipeline.py                          # All stages
python pipeline.py --stage crawl            # Single stage
python pipeline.py --stage enhance          # Generate prompts
python pipeline.py --stage enhance --import # Import results
```

**Stage Functions**:
- `run_crawler()`: `src/crawler/scraper.py`
- `run_parser()`: `src/crawler/parser.py`
- `run_chunker()`: `src/content/chunker.py`
- `run_enhancer()`: `src/content/enhancer.py` (with `--import` flag)
- `run_renderer()`: `src/renderer/math_renderer.py`

### Bot Entry Point (`main.py`)

```bash
python main.py  # Start bot daemon
```

**Flow**:
1. Load and validate config
2. Initialize database
3. Create bot application
4. Setup scheduler
5. Start polling

### Preview CLI Entry Point (`scripts/lesson-preview.py`)

```bash
python scripts/lesson-preview.py export          # Export all to markdown
python scripts/lesson-preview.py export --id 5   # Export single lesson
python scripts/lesson-preview.py list --status pending
python scripts/lesson-preview.py approve --id 5
python scripts/lesson-preview.py approve --all   # Bulk approve
python scripts/lesson-preview.py reject --id 5 --reason "quality"
python scripts/lesson-preview.py show --id 5
python scripts/lesson-preview.py sync            # Re-export changed lessons
```

**Commands**: export, list, approve, reject, show, sync

---

## Key Patterns

### 1. Async-First Architecture
- All I/O uses `async/await`
- `aiosqlite` for database
- `async_playwright` for crawling
- Executor-wrapped sync operations (LaTeX)

### 2. Resumable Pipeline
- Status tracking per stage
- `get_unparsed_chapters()`, `get_pending_lessons()`
- No duplicate processing
- Enhancement workflow supports resume via `_load_done_ids()`

### 3. Provider Abstraction
- `LLMProvider` interface
- Swap Anthropic/OpenAI/DeepSeek
- Conversation history support

### 4. Circuit Breaker
- Crawler stops after 20 failures
- User-friendly error message

### 5. Message Splitting
- Paragraph-aware splitting
- Fallback to line-by-line
- Respects 4096-char limit

---

## Dependencies

### Python
```
playwright==1.49.0
playwright-stealth==1.0.6
beautifulsoup4==4.12.3
aiosqlite==0.20.0
openai==1.58.1
python-telegram-bot[job-queue]==21.7
pyyaml==6.0.2
pytz==2024.2
anthropic==0.42.0
aiohttp==3.11.11
```

### System
- Chromium (Playwright)
- TeX Live (pdflatex)
- dvipng, poppler-utils

---

## File Locations

| Type | Location |
|------|----------|
| Database | `data/feynman.db` |
| Logs | `data/feynman-bot.log` |
| Raw images | `data/raw/images/{volume}_{chapter}/` |
| Math images | `data/images/{md5_hash}.png` |
| Pending prompts | `data/pending_prompts.jsonl` |
| Enhanced outputs | `data/enhanced_outputs.jsonl` |
| Lesson previews | `docs/lessons-preview/{id:04d}-{type}-{slug}.md` |
| Config | `config.yaml` |
| Environment | `.env` |

---

## Testing

**End-to-End Test**: `scripts/test-e2e.py`
- Runs pipeline for one chapter
- Verifies database state
- Tests bot commands

---

## Deployment

**systemd Service**: `scripts/feynman-bot.service`
- Auto-restart on failure
- Runs bot as daemon
- Logs to journalctl

---

## Known Limitations

1. **Single-user design**: Single `chat_id` in config
2. **No backups**: No automated database backup
3. **SQLite limits**: May bottleneck at high concurrency
4. **Fixed schedule**: Review days hardcoded (Thu, Sun)
5. **Large file size**: `handlers.py` (565 LOC) and `math_renderer.py` (217 LOC) exceed 200-line guideline

---

## Future Enhancements

1. Multi-user support with per-user preferences
2. Database backup automation
3. PostgreSQL migration option
4. Configurable review days
5. Lesson feedback/rating system
6. Alternative LLM providers (local models)
