---
title: "Rolling Enhance → Review → Deploy Pipeline"
description: "Daily 10-lesson enhancement with Claude Session, human review loop, render + deploy to Telegram without waiting for full batch"
status: completed
priority: P1
effort: 8h
branch: main
tags: [enhancement, review, deploy, pipeline, rolling]
created: 2026-02-28
---

# Rolling Enhance → Review → Deploy Pipeline

## Problem Summary

843 lessons are pending enhancement. Current blocker:
- Enhancer exists but requires manual Claude Code session step
- No daily batch limiting (would exhaust API/session budget at once)
- Review workflow exists (`preview_exporter.py`) but disconnected from deploy
- Bot can't deliver quality lessons until enhancement + approval complete

**Goal:** Create a daily rolling pipeline:
1. Enhance 10 lessons/day via Claude Session (no API cost)
2. Human reviews & approves each batch
3. Approved lessons → render → mark deployable → bot delivers immediately
4. Repeat next day — don't wait for all 843

---

## Architecture: Rolling Pipeline

```
Daily Cycle:
────────────
[Batch Select]          Select next 10 pending lessons
      ↓
[Export Prompts]        pipeline.py --stage enhance --batch 10
      ↓
[Claude Session]        Claude processes pending_prompts.jsonl → enhanced_outputs.jsonl
      ↓
[Import Results]        pipeline.py --stage enhance --import
      ↓
[Preview Export]        pipeline.py --stage preview  (→ docs/lessons-preview/)
      ↓
[Human Review]          Review markdown previews → approve/reject
      ↓
[Render]                pipeline.py --stage render --approved-only
      ↓
[Bot Deploy]            Bot now serves approved lessons immediately
```

---

## Implementation Phases

| Phase | Description | Effort | Status |
|-------|-------------|--------|--------|
| [Phase 01](phase-01-batch-enhance-script.md) | Add `--batch N` limit to enhance stage | 1h | completed |
| [Phase 02](phase-02-review-cli.md) | CLI review tool: approve/reject from terminal | 1.5h | completed |
| [Phase 03](phase-03-render-approved-only.md) | Render only approved lessons, mark render_status | 1h | completed |
| [Phase 04](phase-04-bot-delivery-gate.md) | Bot delivers approved + rendered lessons only | 1h | completed |
| [Phase 05](phase-05-daily-workflow-script.md) | `daily_enhance.sh` — one-command daily workflow | 0.5h | completed |

**Total Effort**: 5 hours

---

## Key Design Decisions

### 1. Claude Session Enhancement (Not API)
Current design already uses JSONL file exchange:
- `pipeline.py --stage enhance` → writes `data/pending_prompts.jsonl`
- Claude processes it → writes `data/enhanced_outputs.jsonl`
- `pipeline.py --stage enhance --import` → imports to DB

**Change needed**: Add `--batch N` to limit prompts generated to N lessons/run.

### 2. Human Review = Approve in CLI
After import, run preview export → review markdown files → `approve` command:
```bash
python pipeline.py --stage preview          # export to docs/lessons-preview/
python review.py list                       # list pending review
python review.py approve <lesson_id>        # approve one
python review.py approve-batch              # interactive batch approve
```

### 3. Render Only Approved
Add `render_status` field or filter by `approval_status = 'approved'` when rendering.
Already have `approval_status` in `Lesson` model — just need to gate renderer.

### 4. Bot Delivery Gate
Bot currently queries lessons without approval filter.
Add `WHERE approval_status = 'approved'` to lesson fetch queries.

### 5. Rolling = No Dependencies Between Days
Each day is independent:
- Day 1: Enhance lessons 1-10, review, deploy
- Day 2: Enhance lessons 11-20, review, deploy (bot now has 20 approved)
- ...
- Day 84: All 843 done (if 10/day)

---

## Daily Workflow (After Implementation)

```bash
# Morning (5 min)
python pipeline.py --stage enhance --batch 10
# → opens: "Run Claude Code session to process data/pending_prompts.jsonl"

# Claude Session (10-15 min)
# In Claude Code: "Process enhancement prompts in data/pending_prompts.jsonl..."

# Import + preview (2 min)
python pipeline.py --stage enhance --import
python pipeline.py --stage preview

# Review (15-20 min)
python review.py approve-batch   # interactive CLI review

# Render + done (2 min)
python pipeline.py --stage render --approved-only
# Bot now delivers new lessons
```

**Total daily time: ~30-40 min**

---

## Key Files

| File | Changes |
|------|---------|
| `src/content/enhancer.py` | Add batch limit to `generate_prompts()` |
| `pipeline.py` | Add `--batch` arg to enhance stage |
| `src/knowledge/db.py` | Add `get_pending_review_lessons()`, `approve_lesson()` |
| `src/renderer/math_renderer.py` | Filter by `approval_status = 'approved'` |
| `src/bot/handlers.py` | Add approval gate to lesson delivery query |
| `review.py` (new) | CLI review tool |
| `daily_enhance.sh` (new) | One-command daily workflow |

---

## Success Criteria

1. `--batch 10` limits enhance to 10 lessons/run
2. Review CLI shows lesson content + approve/reject in terminal
3. Bot only delivers `approval_status = 'approved'` lessons
4. Renderer skips non-approved lessons
5. Daily workflow runnable in < 40 min
6. After Day 1: bot delivers first 10 enhanced lessons
7. Incremental: each day adds more approved lessons to bot

---

## Post-Merge Continuity Checklist (Immediate)

After Chunker-Parser merge, verify:
- [ ] `pipeline.py --stage enhance` still works (843 pending lessons exist)
- [ ] `data/pending_prompts.jsonl` + `data/enhanced_outputs.jsonl` state is consistent
  - If stale outputs file exists from pre-fix era → delete to avoid wrong lesson_ids
- [ ] Bot delivery still works (`/next` command) — lessons have new IDs post-reparse
- [ ] Any hardcoded lesson IDs in user_progress → already reset (branch strategy confirmed)

---

## Risk Assessment

| Risk | Impact | Mitigation |
|------|--------|------------|
| 10 lessons/day = 84 days to full enhancement | Low | Bot works with partial set; most important chapters done first |
| Claude Session quality variability | Medium | Human review catches bad output |
| Stale outputs.jsonl with old lesson IDs | High | Delete on first run, re-generate |
| Bot delivers unapproved raw content | High | Add approval gate before Phase 05 |

---

## Unresolved Questions

1. Order of enhancement: sequential (Ch1→Ch2→...) or by priority chapters?
2. Should rejected lessons auto-retry or require manual fix?
3. `review.py` as standalone script or integrated into `pipeline.py`?
