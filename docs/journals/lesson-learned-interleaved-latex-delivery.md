# Lesson Learned: Interleaved LaTeX Formula Delivery

**Plan:** 260227-2237-interleaved-latex-delivery
**Date:** 2026-02-28
**Status:** Completed
**Commit:** 99a0c61

---

## Context

Telegram Bot gửi lessons với công thức LaTeX. Trước đây, `send_lesson()` gửi toàn bộ text trước, rồi dump tất cả PNG images ở cuối → User không map được image với formula trong text.

## Solution Implemented

Interleaved delivery: split content tại formula boundaries, gửi text và images xen kẽ theo đúng vị trí trong bài.

### Key Technical Decisions

| Decision | Rationale |
|----------|-----------|
| Hash-based PNG lookup | Renderer có thể skip failed formulas → index-based matching không reliable. Hash (MD5[:12]) match với filename → robust |
| Pattern order replication | Renderer extract theo pattern groups ($$ → \[ → $ → \(). Phải replicate exact order để map đúng |
| Segment coalescing | Nhiều short text segments → Telegram rate limiting. Merge text < 200 chars |
| Graceful fallback | Missing PNG → keep original LaTeX text inline. Không silent failure |

### Code Added

```python
# src/bot/handlers.py
_formula_hash()           # MD5[:12] matching renderer
_extract_formula_positions()  # Find all formulas with positions
_build_interleaved_segments() # Split content at formula boundaries
_coalesce_segments()      # Merge short text segments
```

## What Went Well

1. **Clear design constraint identified upfront** - Formula extraction order critical, documented clearly
2. **Single file change** - Only `handlers.py` modified, minimal blast radius
3. **Hash-based mapping** - More robust than index-based, handles failed renders gracefully
4. **Edge cases covered** - No formulas, no images, missing PNGs, duplicates all handled

## Challenges

1. **Regex synchronization** - `FORMULA_PATTERNS` in handlers.py must match `math_renderer.py` exactly. Future changes to renderer require updating handlers.

2. **Deduplication logic** - Renderer skips duplicate formulas, delivery must do same. `seen_formulas` set required.

## Lessons for Future

### 1. Cross-Module Contract
Khi 2 modules depend on same logic (extraction order, hashing), document the contract explicitly:
```python
# NOTE: Must match math_renderer.py:155-159 pattern order
FORMULA_PATTERNS = [...]
```

### 2. Graceful Degradation
Luôn có fallback khi external resource missing (PNG not rendered). User vẫn đọc được content (LaTeX text).

### 3. Test with Real Data
Run với lesson thực từ DB, không chỉ mock data. Formula patterns in wild có edge cases (escaped delimiters, nested $).

### 4. Single Responsibility
Plan focused on ONE change: delivery order. Không refactor khác, không add features. Small PR = easy review.

## Metrics

| Metric | Value |
|--------|-------|
| LOC added | ~80 |
| Files changed | 1 |
| Time estimate | 1h |
| Actual time | ~1h |
| Test coverage | Manual testing via bot |

## Follow-up Actions

- [ ] Consider adding `asyncio.sleep(0.3)` between sends if rate limiting observed
- [ ] Add unit tests for `_extract_formula_positions` and `_build_interleaved_segments`
- [ ] Monitor Telegram API rate limits in production

## Related Plans

- `260227-2237-interleaved-latex-delivery` (this plan) → archived
- `260228-0748-lesson-preview-markdown` (pending) - preview workflow before delivery

---

**Archived to:** `plans/archive/260227-2237-interleaved-latex-delivery/`
