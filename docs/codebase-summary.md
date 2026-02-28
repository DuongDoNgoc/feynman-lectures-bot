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
- `handlers.py` (565 lines): Command/message handlers ⚠️ exceeds 200-line guideline
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
| `scheduler.py` | `setup_schedule()` | Configure daily delivery times |
| `scheduler.py` | `catchup_missed_lessons()` | Resume missed deliveries |

**Commands Implemented**:
- `/start`, `/next`, `/quiz`, `/explain`, `/example`
- `/progress`, `/schedule`, `/role`, `/search`, `/help`

### 2. Content Module (`src/content/`)

**Purpose**: Transform raw content into enhanced lessons

**Files**:
- `chunker.py` (98 lines): Section to chunk conversion
- `enhancer.py` (286 lines): Claude Code session workflow for enhancement
- `preview_exporter.py` (287 lines): Export lessons to markdown for review

**Key Functions**:

| File | Function | Purpose |
|------|----------|---------|
| `chunker.py` | `run_chunker(config)` | Split sections into chunks |
| `chunker.py` | `split_section_to_chunks()` | 800-1200 word splitting |
| `enhancer.py` | `generate_prompts(config)` | Create pending_prompts.jsonl |
| `enhancer.py` | `import_outputs(config)` | Import enhanced_outputs.jsonl |
| `enhancer.py` | `run_enhancer(config, import_mode)` | Orchestrator |
| `enhancer.py` | `_extract_title()` | Extract title from content |
| `enhancer.py` | `_extract_quiz_json()` | Parse quiz answers |
| `preview_exporter.py` | `export_lesson(lesson_id)` | Export single lesson to markdown |
| `preview_exporter.py` | `export_all_lessons()` | Export all completed lessons |
| `preview_exporter.py` | `export_lessons_by_type(type)` | Export by lesson type |

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
- `parser.py` (227 lines): HTML/LaTeX extraction

**Key Functions**:

| File | Function | Purpose |
|------|----------|---------|
| `scraper.py` | `run_crawler(config)` | Main crawler orchestrator |
| `scraper.py` | `crawl_toc()` | Extract chapter links |
| `scraper.py` | `crawl_chapter()` | Fetch chapter HTML |
| `scraper.py` | `download_images()` | Save referenced images |
| `scraper.py` | `create_browser()` | Context manager with stealth |
| `parser.py` | `run_parser(config)` | Parse all uncrawled chapters |
| `parser.py` | `parse_chapter_html()` | Extract sections by heading |
| `parser.py` | `extract_latex_formulas()` | Multi-method formula extraction |

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

**Purpose**: Unified interface for multiple LLM providers

**Files**:
- `provider.py` (130 lines): Anthropic/OpenAI-compatible client

**Key Functions**:

| Function | Purpose |
|----------|---------|
| `LLMProvider.generate()` | Async completion with history |
| `build_enhancement_provider()` | Anthropic Claude for pipeline |
| `build_qa_provider()` | DeepSeek for bot Q&A |

**Providers**:
- Enhancement: `claude-haiku-4-5-20251001`
- Q&A: `deepseek-chat`

### 6. Renderer Module (`src/renderer/`)

**Purpose**: LaTeX to PNG conversion

**Files**:
- `math_renderer.py` (217 lines): Formula rendering pipeline ⚠️ exceeds 200-line guideline

**Key Functions**:

| Function | Purpose |
|----------|---------|
| `run_renderer(config)` | Process all pending lessons |
| `render_latex_to_png()` | Convert formula to image |
| `render_with_pdflatex()` | Primary method (high quality) |
| `render_with_matplotlib()` | Fallback method |

**Features**:
- MD5-based caching
- Async-safe via executor
- Max 20 formulas per lesson

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

## Current Data Status (2026-02-27)

**Database**: `data/feynman.db` - 84 MB
- **Enhanced Lessons**: 19 completed lessons in `enhanced_outputs.jsonl`
- **Pending Lessons**: 545 lessons awaiting enhancement in `pending_prompts.jsonl`
- **Rendered Images**: 263 PNG formula images in `data/images/`

**Processing Progress**:
- Enhancement: ~3.4% complete (19/564 lessons)
- Rendering: 263 formulas rendered
- Pipeline: Stages 1-3 (crawl, parse, chunk) complete
- Enhancement: In progress (Claude Code workflow)

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
