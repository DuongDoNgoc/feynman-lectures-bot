---
title: "Interleaved LaTeX Formula Delivery"
description: "Send LaTeX PNG images inline between text segments for natural reading flow in Telegram"
status: completed
priority: P1
effort: 1h
branch: master
tags: [telegram, latex, ux, handlers]
created: 2026-02-27
---

# Interleaved LaTeX Formula Delivery

## Problem

`send_lesson()` sends full text first, then dumps all math PNGs at the bottom. Users cannot map images to formulas in text. Long lessons with many formulas become unreadable.

## Solution

Add `_build_interleaved_segments()` helper to `src/bot/handlers.py` that splits `content_enhanced` at formula boundaries and produces an ordered list of text/image segments. Refactor `send_lesson()` to iterate segments, sending text and photos inline.

## Critical Design Constraint

`render_lesson_math()` extracts formulas **grouped by pattern type** (all `$$` first, then all `\[`, then all `$`, then all `\(`), NOT by text position. The PNG list in `math_images_json` follows this grouped order. The new helper must reproduce this exact extraction order to correctly map PNGs to formulas.

## Phases

| Phase | Description | Effort | Details |
|-------|-------------|--------|---------|
| 01 | Implement interleaved delivery | 1h | [phase-01](phase-01-interleaved-delivery.md) |

## Files Changed

- `src/bot/handlers.py` -- add `_build_interleaved_segments()`, refactor `send_lesson()`

## Files NOT Changed

- `src/renderer/math_renderer.py` -- no changes to rendering or extraction
- DB schema -- untouched
- Any other module
