# Interleaved LaTeX PNG Delivery in Telegram

**Date**: 2026-02-27 22:50
**Severity**: Medium
**Component**: Bot message delivery (`send_lesson()`)
**Status**: Implemented with known cache bug

## What Happened

Refactored `send_lesson()` in `src/bot/handlers.py` to deliver lesson content with formula PNG images interleaved inline with text, instead of the previous pattern of dumping all text first then stacking all images at the bottom. This improves UX by placing context-rich images exactly where the reader encounters the formula explanation.

Added four helper functions to orchestrate the segmentation:
- `_formula_hash()` — MD5 hash (first 12 chars) matching math_renderer logic
- `_extract_formula_positions()` — finds all formulas by regex, deduplicates by formula text
- `_build_interleaved_segments()` — splits content at formula boundaries, maps hashes to PNG files
- `_coalesce_segments()` — merges consecutive short text segments to reduce Telegram message spam

Also increased renderer DPI from 200 → 1200 (6x resolution) to improve formula legibility on mobile devices.

## The Brutal Truth

The DPI increase was necessary because 200 DPI looked fuzzy on Telegram's mobile view. But here's the problem: **the math_renderer caches by filename**, so if a PNG already exists at `data/images/{hash}.png`, it skips re-rendering. This means bumping DPI from 200 → 1200 doesn't actually re-render existing images unless you manually delete the old cache.

We discovered this the hard way when testing showed formulas still looked blurry after the DPI config change. The old low-res PNGs were silently reused. This is a silent failure that wastes time and frustration during QA.

Also, the interleaving logic relies on hash consistency between handlers.py and math_renderer.py. If these patterns diverge, formulas won't match PNG filenames and will fall back to inline LaTeX text instead of images. The comment flags this cross-reference but it's fragile.

## Technical Details

**Interleaving logic flow:**
1. Extract all formulas from `content_enhanced` using `FORMULA_PATTERNS` (4 regex patterns: `$$..$$`, `\[..\]`, `$..$`, `\(..\)`)
2. For each formula, compute hash and look up corresponding PNG file
3. Build segments: `[text → image → text → image → text]`
4. Coalesce consecutive text segments shorter than 200 chars to avoid chat spam
5. Send each text segment with `parse_mode="Markdown"` (fallback to plain text on error)
6. Send each image with `InputFile()`

**Cache bug example:**
```
Config: renderer.dpi = 200  →  generate data/images/abc123def456.png at 200 DPI
Commit:  renderer.dpi = 1200  →  same filename, old PNG already exists
Result:  Renderer skips re-render, old low-res PNG is reused
```

## What We Tried

1. **Initial approach**: Dump all images at bottom (commits prior to 99a0c61)
   - Simple but poor UX; reader has no formula context

2. **New approach**: Interleave images with text
   - Complex segment-building logic, but matches academic text layout
   - Discovered hash matching must be exact; any deviation breaks PNG lookup

3. **DPI increase**: 200 → 1200 for sharpness
   - Worked in theory, but cache invalidation broke it in practice
   - Added `test-interleaved.py` for manual QA to surface this

## Root Cause Analysis

The core issue: **cache invalidation without explicit cache busting**. The renderer filename is deterministic (hash-based), which is good for deduplication, but becomes a liability when config changes. Changing DPI should trigger re-renders, but the system doesn't know that.

Secondary issue: **cross-file pattern synchronization**. `FORMULA_PATTERNS` in handlers.py must exactly match math_renderer.py or formulas go unmatched. No automated check exists. If someone modifies one and forgets the other, silent failures occur (formula text stays inline, no visual error).

## Lessons Learned

1. **Cache busting matters**: Hash-based caching is elegant for dedup but requires explicit invalidation on config changes. Consider adding a version prefix to filenames (`{version}_{hash}.png`) or a separate config hash.

2. **Synchronize cross-file constants**: The `FORMULA_PATTERNS` duplication between handlers.py and math_renderer.py is brittle. Extract to `src/constants.py` and import both places. Add a unit test that verifies they match.

3. **Test cache behavior**: The test-interleaved.py script caught the DPI bug, but only by manual inspection. Automate this: add a CLI flag `--no-cache` or `--force-render` to let tests force re-renders and verify PNG resolution.

4. **Document the interleaving assumption**: The feature assumes math_images_json paths exist on disk. If a PNG is deleted but the DB still references it, the image silently drops from delivery (fallback to plain text). Document this gracefully or add validation.

## Next Steps

1. Add cache invalidation: either bump DPI in filename or add explicit cache-clear flag to renderer
2. Consolidate `FORMULA_PATTERNS` into a shared constant module
3. Add unit test: verify pattern consistency between handlers.py and math_renderer.py
4. Enhance test-interleaved.py to validate PNG resolution (use PIL/Pillow to check actual DPI)
5. Monitor: track in logs how many formulas fall back to text (indicates missing PNGs)
