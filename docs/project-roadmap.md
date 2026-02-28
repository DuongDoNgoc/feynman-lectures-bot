# Feynman Bot - Project Roadmap

## Project Status

**Current Version**: 1.0.0
**Last Updated**: 2026-02-27
**Status**: Production Ready

---

## Development Phases

### Phase 1: Foundation ✅ COMPLETE

**Timeline**: Completed
**Status**: All core features implemented

**Deliverables**:
- [x] Web crawler with anti-detection
- [x] HTML/LaTeX parser
- [x] Content chunker
- [x] LLM enhancer
- [x] LaTeX renderer
- [x] Telegram bot with all commands
- [x] Scheduler with JobQueue
- [x] Database layer with all tables
- [x] Configuration management
- [x] End-to-end testing

**Success Metrics**:
- ✅ Pipeline processes full chapters end-to-end
- ✅ Bot delivers 3 daily lessons
- ✅ Quiz functionality with inline keyboard
- ✅ Q&A with conversation history

---

### Phase 2: Production Hardening 🚧 IN PROGRESS

**Timeline**: Current focus (Started 2025-02, ongoing)
**Priority**: HIGH
**Current Progress**: Content enhancement in progress (19/843 lessons complete)

**Goals**: Ensure reliability and maintainability

**Tasks**:

#### 2.0 Preview & Approval Workflow ✅ COMPLETE
- [x] Lesson preview export to markdown
- [x] CLI tool for approval workflow (review.py)
- [x] Approval status tracking (pending/approved/rejected)
- [x] Bot delivery gating to approved lessons only

#### 2.1 Rolling Enhancement Pipeline ✅ COMPLETE
- [x] Rolling enhancement pipeline with --batch flag
- [x] Human review CLI (review.py approve-batch)
- [x] Renderer gated to approved-only lessons
- [x] Bot delivery gated to approved-only lessons
- [x] daily-enhance.sh workflow script

#### 2.1.1 Formula Rendering System ✅ COMPLETE
- [x] Single formula rendering via pdflatex
- [x] Combined block rendering via xelatex+fontspec (DejaVu Serif)
- [x] Grouping logic (_group_nearby_formulas, max_gap=300)
- [x] Block dictionary format ({type, path, start, end})
- [x] MD5 caching with cb_ prefix for combined blocks
- [x] Real LaTeX filter (_is_real_latex)
- [x] 50-block per lesson cap
- [x] DPI=1200 configuration

#### 2.1.2 Source URL Delivery ✅ COMPLETE
- [x] get_lesson_source_url() JOIN pattern in db.py
- [x] send_lesson() appends "📖 Nguồn: {url}" as final message
- [x] Users can click source link to full Feynman chapter

#### 2.2 Error Handling & Monitoring
- [x] Circuit breaker for crawler (20 failures)
- [x] Implement retry logic for LLM API failures
- [x] Graceful degradation for renderer failures (pdflatex + xelatex fallback)
- [x] User-friendly error messages for all failure modes
- [x] Error recovery procedures documentation

#### 2.3 Testing
- [x] Unit tests for each module
- [x] Integration tests for pipeline stages
- [ ] Bot handler tests with mocked Telegram API
- [ ] Performance benchmarks for enhancement

#### 2.4 Monitoring
- [x] Structured logging with file + console output
- [x] Metrics collection (lessons sent, errors, response times)
- [x] Health check endpoint
- [ ] Database connection monitoring

#### 2.5 Documentation
- [x] README.md
- [x] Project Overview & PDR
- [x] Codebase Summary (updated 2026-02-27)
- [x] Code Standards
- [x] System Architecture
- [x] Project Roadmap (this document)
- [x] Deployment Guide
- [x] Troubleshooting Guide

**Current Status**:
- Pipeline stages 1-3 (crawl, parse, chunk): Complete
  - Parser: Recursive h2/h3 detection working (607 sections, avg 6.5/chapter)
  - Chunker: Semantic titles "ChN-M: Title — type" (843 lessons total)
- Enhancement stage: 19 lessons enhanced, 824 pending
- Rendering stage: 263+ formulas rendered
- Bot: Operational with all 10 commands

**Success Criteria**:
- 99%+ bot uptime
- < 3 second response time for commands
- All errors logged with context

---

### Phase 3: Multi-User Support 📋 PLANNED

**Timeline**: Q2 2025
**Priority**: MEDIUM

**Goals**: Scale beyond single-user deployment

**Tasks**:

#### 3.1 Database Changes
- [ ] Add `users` table with preferences
- [ ] Migrate from single chat_id to user_id
- [ ] Add user settings (timezone, role, schedule)
- [ ] Per-user progress isolation

#### 3.2 Bot Enhancements
- [ ] Multi-user command handlers
- [ ] User registration flow
- [ ] Per-user customization commands
- [ ] Admin commands for management

#### 3.3 Scheduler Updates
- [ ] Per-user scheduling
- [ ] Timezone-aware delivery
- [ ] Batch job optimization

**Success Criteria**:
- Support 10+ concurrent users
- Per-user lesson preferences
- Isolated progress tracking

---

### Phase 4: Content Expansion 📋 PLANNED

**Timeline**: Q3 2025
**Priority**: MEDIUM

**Goals**: Expand beyond Feynman Lectures

**Tasks**:

#### 4.1 Additional Sources
- [ ] Support for custom content upload
- [ ] Integration with other physics resources
- [ ] Content versioning and updates

#### 4.2 Enhanced Lessons
- [ ] Video lesson support
- [ ] Interactive simulations
- [ ] Worked problem sets
- [ ] Formula derivation step-by-step

#### 4.3 Adaptive Learning
- [ ] Difficulty adjustment based on quiz scores
- [ ] Spaced repetition algorithm
- [ ] Personalized review schedules

**Success Criteria**:
- 2x content library size
- Adaptive difficulty working
- Spaced repetition improving retention

---

### Phase 5: Platform Features 📋 PLANNED

**Timeline**: Q4 2025
**Priority**: LOW

**Goals**: Advanced learning platform features

**Tasks**:

#### 5.1 Gamification
- [ ] Achievement system
- [ ] Leaderboards (opt-in)
- [ ] Badges and milestones
- [ ] Learning streak bonuses

#### 5.2 Social Features
- [ ] Study groups
- [ ] Shared quizzes
- [ ] Discussion forums per lesson
- [ ] Peer-to-peer questions

#### 5.3 Analytics Dashboard
- [ ] Web dashboard for progress
- [ ] Learning statistics visualization
- [ ] Weakness identification
- [ ] Export learning reports

**Success Criteria**:
- 50% DAU/MAU ratio
- 30%+ engagement with social features
- Positive user feedback on analytics

---

## Technical Debt

### High Priority

1. **No Database Backups**
   - Risk: Data loss from corruption
   - Solution: Automated backup with retention policy

2. **Hardcoded Review Days**
   - Risk: Inflexible schedule
   - Solution: Configurable review days in config.yaml

3. **No Rate Limiting**
   - Risk: API abuse
   - Solution: Per-user rate limits on commands

4. ~~Manual Content Review~~ ✅ RESOLVED
   - Implemented preview CLI with approval workflow
   - Bot now gates delivery to approved lessons only

### Medium Priority

4. **Single Point of Failure (SQLite)**
   - Risk: Bottleneck under load
   - Solution: PostgreSQL migration path

5. **No Caching Layer**
   - Risk: Repeated expensive operations
   - Solution: Redis for frequently accessed data

6. **Manual Deployment**
   - Risk: Deployment errors
   - Solution: Docker container + CI/CD pipeline

### Low Priority

7. **Mixed Language Code**
   - Risk: Maintenance confusion
   - Solution: Standardize on English for code, Vietnamese for content

8. **No API Versioning**
   - Risk: Breaking changes
   - Solution: Version API endpoints if exposed

---

## Milestones

| Milestone | Target | Status | Description |
|-----------|--------|--------|-------------|
| MVP Launch | 2025-02 | ✅ Complete | Basic pipeline + bot working |
| Production Hardening | 2025-03 | 🚧 In Progress | Testing, monitoring, docs |
| Multi-User Alpha | 2025-06 | 📋 Planned | 5-10 beta users |
| Multi-User Beta | 2025-08 | 📋 Planned | 50+ users |
| Public Launch | 2025-10 | 📋 Planned | Open registration |

---

## Risk Assessment

### Technical Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Cloudflare blocks crawler | HIGH | HIGH | Circuit breaker, manual download option |
| LLM API downtime | MEDIUM | MEDIUM | Retry logic, graceful degradation |
| SQLite corruption | LOW | HIGH | Automated backups, WAL mode |
| Telegram API changes | LOW | MEDIUM | Monitor changelog, version pinning |

### Operational Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| High API costs | MEDIUM | MEDIUM | Usage monitoring, caching |
| User support burden | LOW | MEDIUM | Self-service documentation |
| Content copyright | LOW | HIGH | Fair use analysis, attribution |

---

## Resource Requirements

### Current Phase (Production Hardening)

**Development**:
- 1 developer (part-time)
- 2-4 weeks

**Infrastructure**:
- Single VPS (2GB RAM)
- ~$10/month

**API Costs** (estimated):
- Anthropic Haiku: $5/month
- DeepSeek Chat: $2/month

### Multi-User Phase

**Development**:
- 1-2 developers
- 4-8 weeks

**Infrastructure**:
- Managed database (PostgreSQL)
- Redis cache
- ~$30/month

**API Costs** (100 users):
- Anthropic: $20/month
- DeepSeek: $15/month

---

## Dependencies

### External Services

| Service | Purpose | Critical | Backup Plan |
|---------|---------|----------|-------------|
| Telegram Bot API | Messaging | YES | None (platform dependency) |
| Anthropic API | Content enhancement | YES | DeepSeek fallback |
| DeepSeek API | Q&A | YES | Anthropic fallback |
| Caltech Website | Content source | YES | Manual download |

### Python Packages

| Package | Version | Purpose | Update Policy |
|---------|---------|---------|---------------|
| playwright | 1.49.0 | Web scraping | Monitor for breaking changes |
| python-telegram-bot | 21.7 | Bot framework | Minor updates only |
| anthropic | 0.42.0 | LLM client | Keep updated |
| aiosqlite | 0.20.0 | Database | Stable, no updates needed |

---

## Success Metrics

### Phase 2 (Production Hardening)

- [ ] 99%+ uptime over 30 days
- [ ] < 1% error rate on commands
- [ ] < 3s median response time
- [ ] Zero data loss incidents

### Phase 3 (Multi-User)

- [ ] 10+ active users
- [ ] 70%+ daily engagement
- [ ] 50%+ week-2 retention
- [ ] < 5s lesson delivery time

### Phase 4+ (Content Expansion)

- [ ] 2x content library
- [ ] 4.5+ average user rating
- [ ] 30%+ improvement in quiz scores
- [ ] Positive NPS score

---

## Open Questions

1. **Monetization**: Should we consider paid tiers for advanced features?
2. **Privacy**: What data retention policy for conversation history?
3. **Content Licensing**: How to handle copyrighted physics content beyond Feynman?
4. **Internationalization**: Expand beyond Vietnamese users?
5. **Mobile App**: Native app vs web app for better UX?

---

## Change Log

| Date | Version | Changes |
|------|---------|---------|
| 2025-02-25 | 1.0.0 | Initial roadmap document |
| 2026-02-28 | 1.1.0 | Added preview & approval workflow; removed "no manual review" from technical debt |
| 2026-02-28 | 1.2.0 | **Parser fix**: Recursive h2/h3 detection (607 sections, 6.5/chapter avg). **Chunker update**: Semantic titles "ChN-M: Title — type" (843 total lessons, up from 282). Enhanced lesson count: 19/843 (~2.3%). |
| 2026-02-28 | 1.3.0 | **Phase 2.1 Complete**: Rolling enhancement pipeline with --batch flag, review.py CLI for batch approval, renderer gated to approved-only lessons, bot delivery approval gate, daily-enhance.sh workflow script. Ready for daily 10-lesson rolling enhancement. |
| 2026-02-28 | 1.4.0 | **Phase 2.1.1 + 2.1.2 Complete**: (1) Formula rendering system—single (pdflatex) vs. combined blocks (xelatex+fontspec), _group_nearby_formulas(max_gap=300), block dict {type,path,start,end}, MD5 cache with cb_ prefix, _is_real_latex() filter, 50-block cap, DPI=1200. (2) Source URL delivery—db.get_lesson_source_url() JOIN pattern, send_lesson() appends "📖 Nguồn: {url}". Documentation updated in system-architecture.md, code-standards.md, codebase-summary.md, project-roadmap.md. |
| 2026-02-28 | 1.5.0 | **Phase 2.2 Complete**: Error handling & monitoring. (1) LLM retry logic—exponential backoff in LLMProvider, configurable max_retries/retry_base_delay/retry_max_delay, LLMError/LLMRetryExhaustedError exceptions. (2) User-friendly error messages—Vietnamese error dict for all failure modes (LLM unavailable, timeout, DB error, no lesson, no quiz). (3) Troubleshooting guide—docs/troubleshooting-guide.md with recovery procedures for bot, pipeline, LLM API, database, crawler, renderer errors. |
| 2026-02-28 | 1.6.0 | **Phase 2.3 Partial**: Testing infrastructure. (1) Added pytest, pytest-asyncio, pytest-cov to requirements. (2) Created tests/ directory with conftest.py fixtures. (3) Unit tests: test_llm_provider.py (14 tests for retry logic, backends, error types), test_bot_handlers.py (18 tests for message splitting, segments, error messages). (4) Integration tests: test_pipeline_integration.py (14 tests for parser, chunker, enhancer). Total: 46 tests passing. E2E tests remain in scripts/test-e2e.py. |
| 2026-02-28 | 1.7.0 | **Phase 2.4 Partial**: Monitoring. (1) Metrics collection—src/monitoring/metrics.py with MetricsCollector class, tracks lessons sent (by type), errors (by category), LLM/DB response times, bot commands. (2) Health check—src/monitoring/health.py with check_database(), check_llm_api(), check_telegram_api(), full_health_check() for CLI/HTTP endpoints. (3) /status command—shows uptime, lessons sent, errors, avg response times. Remaining: DB connection pool monitoring. |
| 2026-02-28 | 1.8.0 | **Phase 2.5 Complete**: Documentation. (1) Deployment Guide—docs/deployment-guide.md with prerequisites, environment setup, installation, configuration, process management (systemd), monitoring, backup/recovery, security checklist, upgrade procedure. (2) Troubleshooting Guide—created in Phase 2.2. All Phase 2 documentation now complete. |
