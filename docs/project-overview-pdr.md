# Feynman Bot - Project Overview & PDR

## Product Overview

Feynman Bot is an automated Telegram-based learning system that delivers personalized physics micro-lessons from Richard Feynman's "Lectures on Physics." The system combines web scraping, AI-powered content enhancement, and interactive bot functionality to create an engaging learning experience.

### Target Users

- Vietnamese-speaking students and professionals
- Mechatronics engineers and STEM professionals
- Self-directed learners seeking physics knowledge

### Value Proposition

- **Automated Learning**: Daily lessons delivered without manual intervention
- **Personalized Content**: Role-specific examples and explanations
- **Interactive Q&A**: Real-time AI assistance for concept clarification
- **Progress Tracking**: Streak gamification and completion statistics

---

## Product Development Requirements (PDR)

### 1. Functional Requirements

#### FR1: Content Acquisition
- **FR1.1**: System shall scrape HTML content from feynmanlectures.caltech.edu
- **FR1.2**: System shall extract LaTeX formulas with placeholder preservation
- **FR1.3**: System shall download and store referenced images
- **FR1.4**: Crawler shall implement anti-detection measures (stealth mode, random delays)
- **FR1.5**: System shall respect daily rate limits (configurable, default: 10 pages)

#### FR2: Content Processing
- **FR2.1**: System shall parse HTML into structured sections by heading
- **FR2.2**: System shall split sections into 800-1200 word chunks
- **FR2.3**: System shall create 3 lesson types per chunk: concept, deep_dive, quiz
- **FR2.4**: System shall enhance raw content using Claude Code session workflow with role-specific prompts
- **FR2.5**: System shall render LaTeX formulas as PNG images

**Enhancement Workflow**:
- **FR2.4.1**: System shall generate prompts file (`pending_prompts.jsonl`) for pending lessons
- **FR2.4.2**: System shall support Claude Code CLI processing of prompts to `enhanced_outputs.jsonl`
- **FR2.4.3**: System shall import enhanced outputs into database via `--import` flag
- **FR2.4.4**: System shall support optional direct API mode when `ENHANCEMENT_PROVIDER=api`

#### FR3: Lesson Delivery
- **FR3.1**: Bot shall deliver 3 lessons daily at configurable times
- **FR3.2**: System shall rotate lesson types (concept, deep_dive, quiz)
- **FR3.3**: Bot shall split messages exceeding 4096 character limit
- **FR3.4**: System shall send math images as separate photo messages
- **FR3.5**: System shall support review day compilations (Thu, Sun)

#### FR4: Interactive Features
- **FR4.1**: Bot shall respond to `/next` command with next unread lesson
- **FR4.2**: Bot shall provide interactive quiz with inline keyboard
- **FR4.3**: Bot shall offer AI-powered Q&A with conversation history
- **FR4.4**: System shall track user progress and calculate streaks
- **FR4.5**: Bot shall support keyword search across lessons

#### FR5: Personalization
- **FR5.1**: System shall customize content based on user role (default: mechatronics engineer)
- **FR5.2**: Bot shall allow role updates via `/role` command
- **FR5.3**: Content shall mix Vietnamese and English physics terminology

### 2. Non-Functional Requirements

#### NFR1: Performance
- **NFR1.1**: Pipeline shall process 1 chapter in < 5 minutes (excluding enhancement)
- **NFR1.2**: Bot shall respond to commands within 3 seconds
- **NFR1.3**: System shall support concurrent access for 10+ users
- **NFR1.4**: Enhancement workflow shall be resumable (skip already-processed lessons)

#### NFR2: Reliability
- **NFR2.1**: Pipeline shall be resumable (track completion status per stage)
- **NFR2.2**: Crawler shall implement circuit breaker after 20 consecutive failures
- **NFR2.3**: Bot shall recover from crashes without data loss (SQLite WAL mode)
- **NFR2.4**: System shall handle LLM API failures gracefully

#### NFR3: Scalability
- **NFR3.1**: Database schema shall support multiple users
- **NFR3.2**: System shall cache rendered formulas (MD5-based)
- **NFR3.3**: LLM provider interface shall support multiple backends

#### NFR4: Security
- **NFR4.1**: API keys shall be stored in environment variables, not committed
- **NFR4.2**: Bot shall validate chat_id before delivering lessons
- **NFR4.3**: System shall sanitize user inputs before database queries

#### NFR5: Maintainability
- **NFR5.1**: Code shall follow module boundaries (crawler, content, bot, knowledge)
- **NFR5.2**: Configuration shall be externalized (config.yaml + .env)
- **NFR5.3**: Logs shall be written to file with rotation support

### 3. Technical Constraints

- **TC1**: Python 3.12+ required
- **TC2**: SQLite for data storage (no external database)
- **TC3**: Telegram Bot API for messaging
- **TC4**: Claude Code CLI for content enhancement (primary), optional Anthropic API
- **TC5**: DeepSeek Chat for interactive Q&A
- **TC6**: LaTeX tools required (pdflatex, dvipng, poppler-utils)

### 4. Data Model

#### Core Entities

**Chapter**: Raw HTML from website
- `id`, `volume`, `number`, `title`, `url`, `raw_html`, `crawled_at`

**Section**: Parsed content with formulas
- `id`, `chapter_id`, `number`, `title`, `content_text`, `latex_formulas[]`, `image_refs[]`

**Lesson**: Enhanced content
- `id`, `section_id`, `lesson_type`, `sequence`, `title`, `content_enhanced`, `quiz_json`, `math_images_json`, `enhancement_status`

**UserProgress**: Tracking
- `id`, `user_id`, `lesson_id`, `sent_at`, `read_at`, `quiz_score`

**ConversationMessage**: Q&A history
- `id`, `user_id`, `lesson_id`, `role`, `message`, `created_at`

**ScheduledLesson**: Delivery queue
- `id`, `user_id`, `lesson_id`, `lesson_type`, `scheduled_time`, `delivered`, `delivered_at`

### 5. Interface Specifications

#### Bot Commands

| Command | Parameters | Response |
|---------|-----------|----------|
| `/start` | None | Welcome message + bot overview |
| `/next` | None | Next lesson (text + images) |
| `/quiz` | None | Interactive quiz inline keyboard |
| `/explain` | topic | Deep explanation (~400 words) |
| `/example` | None | Role-specific example (~300 words) |
| `/progress` | None | Stats: completed/total, avg score, streak |
| `/schedule` | [HH:MM...] | View or update delivery times |
| `/role` | [description] | View or update user role |
| `/search` | keyword | Top 5 matching lessons |
| `/help` | None | Command reference |

#### Pipeline Stages

```bash
python pipeline.py                          # Run all stages
python pipeline.py --stage crawl            # Single stage
python pipeline.py --stage enhance          # Generate prompts
python pipeline.py --stage enhance --import # Import results
```

**Enhancement Workflow**:
1. `python pipeline.py --stage enhance` → generates `data/pending_prompts.jsonl`
2. Claude Code processes prompts → `data/enhanced_outputs.jsonl`
3. `python pipeline.py --stage enhance --import` → imports to database

### 6. Acceptance Criteria

- **AC1**: Bot successfully delivers 3 lessons daily for 7 consecutive days
- **AC2**: Quiz inline keyboard correctly validates answers and provides explanations
- **AC3**: Q&A maintains conversation context for last 10 messages
- **AC4**: Pipeline processes Volume I chapters without manual intervention
- **AC5**: Streak calculation accurately reflects consecutive day completion
- **AC6**: Search returns relevant results within 2 seconds

### 7. Success Metrics

- **Usage**: Daily active users > 80% of registered users
- **Engagement**: Average quiz completion rate > 70%
- **Learning**: Streak retention > 14 days for 50% of users
- **Quality**: LLM enhancement success rate > 95%
- **Reliability**: Bot uptime > 99%

### 8. Dependencies

#### External Services
- Telegram Bot API
- Claude Code CLI (Anthropic)
- Anthropic API (optional, for automated enhancement mode)
- DeepSeek API

#### Python Packages
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

#### System Tools
- Chromium (via Playwright)
- TeX Live (texlive-latex-base, texlive-fonts-recommended)
- dvipng, poppler-utils

---

## Open Questions

1. **Multi-user Scale**: What is the maximum user count before SQLite becomes a bottleneck?
2. **Content Updates**: How to handle updates to source Feynman Lectures website?
3. **Backup Strategy**: Should automated database backups be implemented?
4. **LLM Fallback**: What happens if Anthropic/DeepSeek APIs are unavailable?
5. **Cost Management**: Estimated monthly cost for LLM API usage at scale?

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2025-02-25 | Initial PDR documentation |
| 1.0.1 | 2026-02-27 | Updated code statistics and current status |
