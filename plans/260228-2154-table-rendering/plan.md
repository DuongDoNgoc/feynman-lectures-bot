---
title: "Render LaTeX Tables as PNG in Lessons"
description: "Detect and render LaTeX/markdown tables as PNG images, interleaved inline like formula blocks"
status: completed
priority: P2
effort: 4h
branch: master
tags: [renderer, tables, latex, delivery]
created: 2026-02-28
completed: 2026-02-28
---

# Render Tables as PNG Images

## Problem

Markdown tables in `content_enhanced` are sent as raw pipe-delimited text in Telegram -- unreadable on mobile. Need to render them as PNG images and interleave inline, same as formula blocks.

## Scope

- **9 markdown tables** (`|---|`) across 9 lessons (all approved)
- **6 `\begin{array}`** occurrences -- already inside `\begin{equation}` blocks, already handled by formula renderer. **Out of scope.**
- **0 `\begin{tabular}`** occurrences. Not present in current data.
- All 9 affected lessons already have `math_images_json` (8 with blocks, 1 possibly empty)

## Architecture Decision: Extend `math_images_json`

Reuse existing block list format `{type, path, start, end}` with `type: "table"`. No new DB column needed. This is the simplest approach because:
- `_build_interleaved_segments()` in handlers.py already works with any block type -- it only uses `start`, `end`, `path`
- `render_lesson_math()` already returns a flat list of blocks sorted by position
- Adding table blocks to the same list preserves correct interleaving with formulas

## Implementation Phases

### Phase 1: Investigation Report (done)
See `phase-01-investigation-report.md`.

### Phase 2: Renderer Extension (~2h)
Add table detection + rendering to `math_renderer.py`. See `phase-02-renderer-extension.md`.

**Key changes:**
1. Add `_extract_table_positions(content)` -- regex to find markdown tables
2. Add `render_table(table_text, output_dir, dpi)` -- xelatex render via tabular
3. Add `_markdown_table_to_latex(md_table)` -- parser converting `|col|col|` to `\begin{tabular}`
4. Integrate into `render_lesson_math()` -- merge table blocks with formula blocks, sort by position

### Phase 3: Backfill Existing Lessons (~1h)
Re-render the 9 approved lessons that contain tables. See `phase-03-existing-lessons-backfill.md`.

**Key changes:**
1. Script `scripts/backfill-tables.py` -- calls `render_lesson_math()` for affected lessons, updates `math_images_json`
2. Does NOT re-enhance content, does NOT change `content_enhanced`

## File Changes Summary

| File | Change |
|------|--------|
| `src/renderer/math_renderer.py` | Add table detection, parsing, rendering; integrate into pipeline |
| `scripts/backfill-tables.py` | New: re-render 9 lessons with table blocks |
| No DB schema change | Reuse `math_images_json` column |
| No handlers.py change | `_build_interleaved_segments` already generic |

## Risk Assessment

| Risk | Mitigation |
|------|-----------|
| Markdown table regex edge cases | Strict pattern: require `|---|` separator row; test on all 9 samples |
| Table PNG too wide for Telegram | Use `minipage{12cm}` constraint (same as combined blocks); `tabularx` with `X` columns for auto-wrap |
| xelatex failure on Vietnamese text in cells | Already solved: use `fontspec` + DejaVu Serif (same as combined blocks) |
| Merging table blocks into existing `math_images_json` | Backfill script must deserialize existing blocks, append new table blocks, re-sort by position, re-serialize |
