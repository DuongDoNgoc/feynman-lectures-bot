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
    participant DB as Database
    participant T as Telegram API

    S->>JQ: Daily job at 07:20
    JQ->>DB: get_next_lesson_by_type("concept")
    DB-->>JQ: Lesson object
    JQ->>T: send_message()
    T-->>S: Message delivered

    S->>JQ: Daily job at 12:15
    JQ->>DB: get_next_lesson_by_type("deep_dive")
    DB-->>JQ: Lesson object
    JQ->>T: send_message()

    S->>JQ: Daily job at 18:30
    JQ->>DB: get_next_lesson_by_type("quiz")
    DB-->>JQ: Quiz lesson
    JQ->>T: send_quiz_keyboard()
```

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
        B1[chapters.raw_html] --> B2[BeautifulSoup Parser]
        B2 --> B3[sections table]
    end

    subgraph "Stage 3: Chunk"
        C1[sections.content_text] --> C2[Chunker]
        C2 --> C3[lessons stubs]
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
    DB-->>B: Lesson object

    B->>B: split_message(content)
    loop For each message part
        B->>U: send_message(part)
    end

    loop For each math image
        B->>U: send_photo(image.png)
    end

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

    Found --> Splitting: Check message length
    Splitting --> Sending: Within 4096 chars
    Splitting --> Splitting: Exceeds limit

    Sending --> SendingImages: Text sent
    SendingImages --> Recording: All images sent
    Recording --> Delivered: mark_sent()
    Delivered --> [*]

    Skipped --> [*]
```

---

## Error Handling Strategy

### Circuit Breaker Pattern (Crawler)

```mermaid
stateDiagram-v2
    [*] --> Normal: Start crawling

    Normal --> Failure: Request fails
    Failure --> Normal: Retry succeeds
    Failure --> Failure: Retry fails (count < 20)

    Failure --> Open: 20 consecutive failures
    Open --> [*]: Stop crawling

    note right of Open
        User action required:
        1. Wait 24h
        2. Manual download
    end note
```

### Graceful Degradation (Rendering)

```mermaid
flowchart TD
    START[LaTeX Formula] --> TRY1[pdflatex]
    TRY1 -->|Success| DONE[PNG Generated]
    TRY1 -->|Failure| TRY2[matplotlib fallback]
    TRY2 -->|Success| DONE
    TRY2 -->|Failure| SKIP[Skip formula, log warning]

    style DONE fill:#c8e6c9
    style SKIP fill:#ffcdd2
```

---

## Deployment Architecture

### Development

```mermaid
graph TB
    DEV[Developer Machine]
    DEV --> PIPELINE[python pipeline.py]
    DEV --> BOT[python main.py]

    PIPELINE --> DB[(data/feynman.db)]
    BOT --> DB

    style DEV fill:#e1f5fe
```

### Production (systemd)

```mermaid
graph TB
    SYSTEM[Linux Server]
    SYSTEM --> SERVICE[feynman-bot.service]
    SERVICE --> BOT[python main.py]

    BOT --> DB[(data/feynman.db)]
    BOT --> LOG[/var/log/feynman-bot/]

    SYSTEM --> TIMER[systemd timer]
    TIMER --> PIPELINE[python pipeline.py --stage crawl]

    style SERVICE fill:#c8e6c9
```

---

## Security Architecture

```mermaid
graph TB
    subgraph "Environment Variables"
        ENV[.env file]
    end

    subgraph "Configuration"
        CONFIG[config.yaml]
    end

    subgraph "Application"
        APP[Python Application]
    end

    subgraph "External APIs"
        ANTH[Anthropic API]
        CLAUDE[Claude Code CLI]
        DEEP[DeepSeek API]
        TG[Telegram API]
    end

    ENV -->|load_config| CONFIG
    CONFIG -->|${VAR} resolution| APP
    APP -->|API Key| ANTH
    APP -->|Claude Code| CLAUDE
    APP -->|API Key| DEEP
    APP -->|Token| TG

    style ENV fill:#ffcdd2
    style ANTH fill:#fff9c4
    style CLAUDE fill:#ffcc80
    style DEEP fill:#fff9c4
    style TG fill:#fff9c4
```

---

## Scalability Considerations

### Current Limitations

| Component | Limitation | Impact |
|-----------|------------|--------|
| SQLite | Single-writer concurrency | Bottleneck at 10+ concurrent users |
| Single chat_id | One user per deployment | Not multi-user ready |
| Sequential LLM calls | Slow enhancement pipeline | Hours for full volume |
| No caching | Repeated rendering | Wasted computation |

### Future Scaling Paths

```mermaid
graph LR
    CURRENT[Current] --> PG[PostgreSQL Migration]
    CURRENT --> MULTI[Multi-user Support]
    CURRENT --> CACHE[Redis Cache Layer]
    CURRENT --> QUEUE[Task Queue]

    PG --> SCALE1[100+ users]
    MULTI --> SCALE2[Per-user preferences]
    CACHE --> SCALE3[10x faster responses]
    QUEUE --> SCALE4[Parallel enhancement]

    style CURRENT fill:#ffcdd2
    style PG fill:#c8e6c9
    style MULTI fill:#c8e6c9
```

---

## Monitoring & Observability

### Logging Strategy

```mermaid
graph TB
    APP[Application] --> LOG[logging module]

    LOG --> FILE[data/feynman-bot.log]
    LOG --> STREAM[stdout/stderr]

    STREAM --> JOURNAL[systemd journalctl]
    STREAM --> DOCKER[Docker logs]

    style LOG fill:#fff9c4
    style JOURNAL fill:#c8e6c9
```

### Log Levels by Component

| Component | Levels Used | Examples |
|-----------|-------------|----------|
| Crawler | INFO, WARNING, ERROR | Pages crawled, failures |
| Parser | DEBUG, INFO | Sections extracted |
| Enhancer | INFO, ERROR | Lessons enhanced |
| Bot | INFO, WARNING | Commands executed |
| Scheduler | INFO, WARNING | Jobs scheduled |
