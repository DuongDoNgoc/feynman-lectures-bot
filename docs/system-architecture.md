# Feynman Bot - System Architecture

## High-Level Architecture

```mermaid
graph TB
    subgraph "Offline Pipeline"
        A[Crawl] --> B[Parse]
        B --> C[Chunk]
        C --> D[Enhance]
        D --> E[Render]
    end

    subgraph "Data Layer"
        F[(SQLite DB)]
        G[Images/]
    end

    subgraph "Runtime Services"
        H[Telegram Bot]
        I[JobQueue Scheduler]
    end

    subgraph "External APIs"
        J[Anthropic Claude]
        K[Claude Code CLI]
        L[DeepSeek Chat]
        M[Telegram API]
    end

    A --> F
    B --> F
    C --> F
    D --> F
    D --> K
    E --> F
    E --> G

    H --> F
    H --> L
    H --> M
    I --> H
    I --> F

    style F fill:#e1f5fe
    style H fill:#c8e6c9
    style J fill:#fff9c4
    style K fill:#fff9c4
```

---

## Component Overview

### 1. Content Pipeline (Offline)

**Purpose**: Transform raw Feynman Lectures into enhanced lessons

**Entry Point**: `pipeline.py`

```mermaid
flowchart LR
    START[Start] --> STAGE{Select Stage}
    STAGE -->|All| A[Stage 1: Crawl]
    STAGE -->|Single| A
    A --> B[Stage 2: Parse]
    B --> C[Stage 3: Chunk]
    C --> D[Stage 4: Enhance]
    D --> E[Stage 5: Render]
    E --> END[Complete]
```

#### Stage Details

| Stage | Input | Output | Location |
|-------|-------|--------|----------|
| **Crawl** | Feynman website | `chapters` table | `src/crawler/scraper.py` |
| **Parse** | `chapters.raw_html` | `sections` table | `src/crawler/parser.py` |
| **Chunk** | `sections` rows | `lessons` stubs | `src/content/chunker.py` |
| **Enhance** | `lessons` (pending) | `lessons.content_enhanced` | `src/content/enhancer.py` + Claude Code |
| **Render** | LaTeX formulas | `lessons.math_images_json` | `src/renderer/math_renderer.py` |
| **Preview** | `lessons` (completed) | Markdown files | `scripts/lesson-preview.py` |
| **Approve** | Human review | `lessons.approval_status` | `scripts/lesson-preview.py` |

### 2. Telegram Bot (Runtime)

**Purpose**: Deliver lessons and handle user interaction

**Entry Point**: `main.py`

```mermaid
flowchart TB
    START[Start Bot] --> CONFIG[Load Config]
    CONFIG --> DB[Init Database]
    DB --> APP[Create Application]
    APP --> SCHED[Setup Scheduler]
    SCHED --> POLL[Start Polling]

    POLL --> CMD{User Input}
    CMD -->|/next| NEXT[Next Lesson Handler]
    CMD -->|/quiz| QUIZ[Quiz Handler]
    CMD -->|/explain| EXPLAIN[Explain Handler]
    CMD -->|Text| QA[Q&A Handler]
    CMD -->|Other| HELP[Help Handler]

    NEXT --> DBQUERY[(DB Query)]
    QUIZ --> DBQUERY
    EXPLAIN --> LLM[(DeepSeek API)]
    QA --> LLM
    HELP --> RESPONSE[Send Response]

    DBQUERY --> RESPONSE
    LLM --> RESPONSE
    RESPONSE --> POLL
```

### 3. Scheduler

**Purpose**: Automated lesson delivery at configured times

**Location**: `src/bot/scheduler.py`

```mermaid
sequenceDiagram
    participant S as Scheduler
    participant JQ as JobQueue
    participant H as Handlers
    participant DB as Database
    participant T as Telegram API

    S->>JQ: Daily job at 07:20
    JQ->>DB: get_next_lesson_by_type("concept")
    DB-->>JQ: Lesson object
    JQ->>H: send_lesson_to_chat(bot, chat_id, lesson)
    H->>T: send_message(text segments)
    H->>T: send_photo(math/table images)
    H->>T: send_message(source URL)
    T-->>S: Message delivered

    S->>JQ: Daily job at 12:15
    JQ->>DB: get_next_lesson_by_type("deep_dive")
    DB-->>JQ: Lesson object
    JQ->>H: send_lesson_to_chat(bot, chat_id, lesson)

    S->>JQ: Daily job at 18:30
    JQ->>DB: get_next_lesson_by_type("quiz")
    DB-->>JQ: Quiz lesson
    JQ->>H: send_lesson_to_chat(bot, chat_id, lesson)
```

**Note**: Scheduler now imports and calls `send_lesson_to_chat()` from `handlers.py`, which is the core delivery function used by both scheduler and command handlers.

---

## Data Flow Diagrams

### Pipeline Data Flow

```mermaid
flowchart LR
    subgraph "Stage 1: Crawl"
        A1[feynmanlectures.caltech.edu] --> A2[Playwright Browser]
        A2 --> A3[chapters table]
    end

    subgraph "Stage 2: Parse"
        B1[chapters.raw_html] --> B2[Recursive h2/h3 Detection]
        B2 --> B3[sections table<br/>607 sections, 6.5/ch avg]
    end

    subgraph "Stage 3: Chunk"
        C1[sections.content_text] --> C2[Per-Chapter Chunker<br/>Target 2000w]
        C2 --> C3[lessons stubs<br/>843 total, semantic titles]
    end

    subgraph "Stage 4: Enhance"
        D1[lessons pending] --> D2[generate_prompts]
        D2 --> D3[pending_prompts.jsonl]
        D3 --> D4[Claude Code Session]
        D4 --> D5[enhanced_outputs.jsonl]
        D5 --> D6[import_outputs]
        D6 --> D7[lessons enhanced]
    end

    subgraph "Stage 5: Render"
        E1[LaTeX formulas] --> E2[Math Renderer]
        E2 --> E3[PNG images]
    end

    subgraph "Stage 6: Preview & Approve"
        F1[lessons completed] --> F2[Export Markdown]
        F2 --> F3[Human Review]
        F3 --> F4{Approve?}
        F4 -->|Yes| F5[approval_status = approved]
        F4 -->|No| F6[approval_status = rejected]
        F5 --> G1[Ready for Delivery]
    end

    A3 --> B1
    B3 --> C1
    C3 --> D1
    D3 --> E1
    D7 --> F1
```

### Bot Runtime Flow

```mermaid
sequenceDiagram
    participant U as User
    participant B as Bot
    participant DB as Database
    participant L as LLM API

    U->>B: /next command
    B->>DB: get_next_lesson(user_id)
    DB-->>B: Lesson object (approved only)

    B->>DB: get_lesson_source_url(lesson_id)
    DB-->>B: Source URL via JOIN

    B->>B: _build_interleaved_segments()
    B->>B: _coalesce_segments()
    B->>B: split_message(content)
    loop For each message part
        B->>U: send_message(part)
    end

    loop For each math image
        B->>U: send_photo(image.png)
    end

    B->>U: send_message(📖 Nguồn: {source_url})

    B->>DB: mark_sent(user_id, lesson_id)

    U->>B: Question text
    B->>DB: get_conversation_history()
    DB-->>B: Last 10 messages

    B->>L: generate(user_prompt, history)
    L-->>B: AI response

    B->>U: send_message(response)
    B->>DB: save_conversation(...)
```

---

## Database Schema

```mermaid
erDiagram
    chapters ||--o{ sections : contains
    sections ||--o{ lessons : generates
    lessons ||--o{ user_progress : tracks
    lessons ||--o{ conversation_history : contexts
    lessons ||--o{ scheduled_lessons : schedules

    chapters {
        int id PK
        str volume
        int number
        str title
        str url
        text raw_html
        str crawled_at
    }

    sections {
        int id PK
        int chapter_id FK
        int number
        str title
        text content_text
        list latex_formulas
        list image_refs
        str parsed_at
    }

    lessons {
        int id PK
        int section_id FK
        str lesson_type
        int sequence
        str title
        text content_enhanced
        text content_summary
        text examples_json
        text quiz_json
        text math_images_json
        str enhancement_status
        str approval_status
    }

    user_progress {
        int id PK
        int user_id
        int lesson_id FK
        str sent_at
        str read_at
        float quiz_score
    }

    conversation_history {
        int id PK
        int user_id
        int lesson_id FK
        str role
        text message
        str created_at
    }

    scheduled_lessons {
        int id PK
        int user_id
        int lesson_id FK
        str lesson_type
        str scheduled_time
        bool delivered
        str delivered_at
    }
```

---

## Module Interactions

### Crawler Module

```mermaid
graph TB
    A[scraper.py] --> B[parser.py]
    A --> C[knowledge/db.py]
    B --> C

    A --> D[Playwright]
    A --> E[aiohttp]
    B --> F[BeautifulSoup]

    style A fill:#ffcdd2
    style B fill:#ffcdd2
    style C fill:#e1f5fe
```

### Content Module

```mermaid
graph TB
    A[chunker.py] --> B[enhancer.py]
    A --> C[knowledge/db.py]
    B --> C
    B --> D[llm/provider.py]
    B --> E[Claude Code CLI]

    E --> F[enhanced_outputs.jsonl]
    B --> F

    style A fill:#fff9c4
    style B fill:#fff9c4
    style C fill:#e1f5fe
    style D fill:#c8e6c9
    style E fill:#ffcc80
    style F fill:#b2dfdb
```

### Bot Module

```mermaid
graph TB
    A[bot.py] --> B[handlers.py]
    A --> C[scheduler.py]
    B --> D[knowledge/db.py]
    B --> E[llm/provider.py]
    C --> D

    style A fill:#c8e6c9
    style B fill:#c8e6c9
    style C fill:#c8e6c9
    style D fill:#e1f5fe
    style E fill:#fff9c4
```

### Preview & Approval Module

```mermaid
graph TB
    A[preview_db.py] --> B[preview_exporter.py]
    A --> C[lesson-preview.py CLI]
    B --> D[docs/lessons-preview/]
    C --> A
    C --> B

    E[Bot Handlers] -->|gate delivery| F{approval_status}
    F -->|approved| G[Deliver Lesson]
    F -->|pending/rejected| H[Skip]

    style A fill:#e1f5fe
    style B fill:#fff9c4
    style C fill:#c8e6c9
    style D fill:#b2dfdb
    style F fill:#ffcdd2
    style G fill:#c8e6c9
    style H fill:#ffcc80
```

**Purpose**: Human-in-the-loop quality control before Telegram delivery

**Workflow**:
1. Pipeline completes lesson → `approval_status = "pending"`
2. `lesson-preview.py export` → Markdown files with YAML frontmatter
3. Human review → `lesson-preview.py approve/reject`
4. Bot handlers → Only deliver `approval_status = "approved"`
5. Scheduled jobs → Skip non-approved lessons automatically

**CLI Commands**:
```bash
python scripts/lesson-preview.py export              # Export all pending
python scripts/lesson-preview.py list --status pending  # Review queue
python scripts/lesson-preview.py show --id 5          # View content
python scripts/lesson-preview.py approve --id 5       # Approve single
python scripts/lesson-preview.py approve --all        # Bulk approve
python scripts/lesson-preview.py sync                 # Re-export changed
```

**Markdown Frontmatter**:
```yaml
---
lesson_id: 1
lesson_type: concept
approval_status: pending
exported_at: "2026-02-28T02:03:03.895762+00:00"
content_hash: 3746c5b3a27d
chapter_number: 1
section_number: 1
---
```

---

## LLM Provider Architecture

```mermaid
classDiagram
    class LLMProvider {
        <<interface>>
        +generate(system, user, history) str
        +generate_with_tools(system, user, tools) str
    }

    class AnthropicProvider {
        -client: Anthropic
        -model: str
        -request_delay: float
        +generate(system, user, history) str
    }

    class OpenAIProvider {
        -client: OpenAI
        -model: str
        -base_url: str
        +generate(system, user, history) str
    }

    LLMProvider <|.. AnthropicProvider
    LLMProvider <|.. OpenAIProvider

    class build_enhancement_provider() {
        Returns AnthropicProvider for Claude Haiku
    }

    class build_qa_provider() {
        Returns OpenAIProvider for DeepSeek
    }

    build_enhancement_provider ..> AnthropicProvider
    build_qa_provider ..> OpenAIProvider
```

---

## Message Flow: Lesson Delivery

```mermaid
stateDiagram-v2
    [*] --> Scheduled: JobQueue triggers

    Scheduled --> Fetching: get_next_lesson_by_type()
    Fetching --> Found: Lesson exists
    Fetching --> Skipped: No lesson available

    Found --> BuildSegments: _build_interleaved_segments()
    BuildSegments --> Coalesce: _coalesce_segments()
    Coalesce --> Splitting: Check message length
    Splitting --> Sending: Within 4096 chars
    Splitting --> Splitting: Exceeds limit

    Sending --> SendingImages: Text sent
    SendingImages --> SourceURL: Append source URL
    SourceURL --> Recording: All images sent
    Recording --> Delivered: mark_sent()
    Delivered --> [*]

    Skipped --> [*]
```

---

## Formula Rendering Subsystem

**Purpose**: Convert LaTeX formulas in lessons to PNG images for Telegram delivery

**Architecture**: Two-tier rendering system optimized for quality and performance

### Rendering Decision Tree

| Condition | Renderer | Template | Speed | Quality |
|-----------|----------|----------|-------|---------|
| Single formula (1-5 in lesson) | pdflatex | Standard article | Fast | High |
| Multiple nearby formulas (>5, <300 char gap) | xelatex + fontspec | minipage(12cm) block | Slower | High (UTF-8) |
| Same formula appears multiple times | MD5 cache | N/A | Instant | N/A |

### Single Formula Rendering

```latex
\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage{amsmath,amssymb}
\pagestyle{empty}
\begin{document}
$<formula>$
\end{document}
```

**Process**:
1. Write temporary `.tex` file
2. Run `pdflatex` → `.pdf`
3. Run `pdftoppm` (poppler) → `.png` at configurable DPI

### Combined Block Rendering

**Trigger**: 2+ formulas within 300-character proximity

**Template**:
```latex
\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage{fontspec}
\setmainfont{DejaVu Serif}
\usepackage{amsmath,amssymb}
\pagestyle{empty}
\begin{document}
\begin{minipage}{12cm}
  $<formula_1>$

  ... text/formula interleaving ...

  $<formula_n>$
\end{minipage}
\end{document}
```

**Advantages**:
- UTF-8 Vietnamese support via fontspec
- Proper spacing and alignment for multiple formulas
- Single image avoids Telegram spam
- Reduced image count (max 50 blocks/lesson)

### Block Dictionary Format

Each rendered block stored in `math_images_json` as:

```json
[
  {
    "type": "single",
    "path": "data/images/a1b2c3.png",
    "start": 234,
    "end": 250
  },
  {
    "type": "combined",
    "path": "data/images/cb_d4e5f6.png",
    "start": 450,
    "end": 800
  }
]
```

**Fields**:
- `type`: `"single"` (pdflatex) or `"combined"` (xelatex)
- `path`: Full path to PNG image
- `start`, `end`: Character positions in original content (for segmentation during delivery)

### Caching & Filename Convention

**MD5 Hash Caching**: Formulas cached by MD5(formula_text) to avoid re-rendering

**Filename Convention**:
- Single formula: `{md5_hash}.png`
- Combined block: `cb_{md5_hash}.png` (cb = combined block)

**Cache Invalidation**: Delete `.png` files in `data/images/` if DPI config changes

### Configuration

In `config.yaml`:

```yaml
renderer:
  output_dir: data/images/
  dpi: 1200              # Resolution for PNG output
  max_blocks_per_lesson: 50
  group_max_gap: 300     # Characters to consider formulas "nearby"
```

### Grouping Logic

Function: `_group_nearby_formulas(max_gap=300)`

```
Formula A at pos 0-20    } gap 50 chars
Formula B at pos 70-90   } gap 200 chars
Formula C at pos 290-310 ─ Combined into 1 block

Formula D at pos 400-420 ─ Separate block (gap 90 > 300 threshold)
Formula E at pos 510-530
```

### Real LaTeX Filter

Function: `_is_real_latex(formula)`

Rejects false positives:
- Plain text (no operators)
- Single variable: `$x$` → skip
- Numbers only: `$123$` → skip
- Common abbreviations (not LaTeX): `$P.S.$` → skip

Accepts:
- Math operators: `$E=mc^2$` ✓
- Multi-variable: `$\alpha + \beta$` ✓
- Greek letters: `$\Delta T$` ✓
- Complex expressions: `$\int_0^\infty e^{-x} dx$` ✓

---

## Table Rendering Subsystem

**See**: [Table Rendering Feature](./table-rendering.md)

**Quick Summary**:
- Detects markdown tables in lesson content via regex pattern (header | separator | rows)
- Converts markdown tables to LaTeX tabular environment via `_markdown_table_to_latex()`
- Renders as PNG using xelatex with filename prefix `tbl_`
- Ensures PNG size stays within Telegram limits via `_ensure_max_size()` (max width + height = 9500 pixels)
- Stores in unified `math_images_json` block dictionary with `type: "table"`
- MD5-based caching; cap: 20 tables per lesson
- Interleaved delivery via handlers (no special code needed)

---

## Error Handling and Reliability

**See**: [Error Handling Strategy](./error-handling.md)

**Summary**:
- Circuit breaker pattern for crawler (stops after 20 failures)
- Graceful degradation for rendering (skip formula, continue delivery)
- LLM retry logic with exponential backoff
- Database WAL mode for crash recovery
- Systemd auto-restart for bot process
- Health check system for monitoring

---

## Deployment Architecture

**See**: [Deployment Guide](./deployment-guide.md)

- **Development**: `python pipeline.py` and `python main.py` on developer machine
- **Production**: systemd service + timer for bot and pipeline
- **Process Management**: Auto-restart on failure via systemd
- **Logging**: File + console to `data/feynman-bot.log`

---

## Security

**Configuration Management**:
- API keys in `.env` (environment variables)
- Configuration externalized in `config.yaml`
- No secrets committed to git

**API Key Isolation**:
- Anthropic API: content enhancement
- Claude Code CLI: enhancement workflow
- DeepSeek API: Q&A functionality
- Telegram Bot API: messaging

---

## Scalability Roadmap

**Current Constraints**:
- SQLite single-writer (10+ concurrent user bottleneck)
- Single chat_id (not multi-user)
- Sequential enhancement (hours per volume)

**Future Scaling**:
- PostgreSQL migration for multi-user
- Redis cache layer for formula caching
- Task queue for parallel enhancement
- Per-user preferences and timezones

---

## Monitoring & Observability

Logging via Python `logging` module → `data/feynman-bot.log` + stdout/stderr (systemd journalctl / Docker logs).

| Component | Levels | Examples |
|-----------|--------|----------|
| Crawler | INFO, WARNING, ERROR | Pages crawled, failures |
| Parser | DEBUG, INFO | Sections extracted |
| Enhancer | INFO, ERROR | Lessons enhanced |
| Bot | INFO, WARNING | Commands executed |
| Scheduler | INFO, WARNING | Jobs scheduled |
