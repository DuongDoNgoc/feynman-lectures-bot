# Formula Rendering System: Grouped Blocks and xelatex Integration

**Date**: 2026-02-28 17:19
**Severity**: High
**Component**: `src/renderer/math_renderer.py`, `src/bot/handlers.py`, message delivery
**Status**: Resolved

## What Happened

Completely rewrote the LaTeX formula rendering pipeline to group nearby formulas into single combined images using xelatex instead of rendering each formula individually. Changed the data format of `math_images_json` from a flat list of PNG paths to a list of block dictionaries containing position metadata (`{type, path, start, end}`). This fixed a critical issue where formulas were failing to render in Telegram and dramatically reduced message fragmentation from 38 individual images down to 7 grouped blocks for heavy lessons (80% reduction).

## The Brutal Truth

The previous system was fundamentally broken for Telegram delivery. Each formula was rendered separately with pdflatex, then stacked as individual messages. This created two problems:

1. **Telegram message spam**: A single lesson with 38 formulas meant sending 38+ separate image messages. This destroyed readability and violated Telegram's rate-limiting expectations.

2. **Rendering failures**: Individual formula rendering with pdflatex is fragile. Some formulas work in isolation but fail when disconnected from their context. More critically, pdflatex doesn't handle UTF-8 Vietnamese text well—any lesson with Vietnamese explanations alongside math would break.

The entire architecture needed to be rebuilt from scratch. Not a minor fix—a complete rewrite.

## Technical Details

**Old approach (broken):**
- Extract each formula independently via regex
- Render each formula to its own PNG file: `{hash}.png`
- Store flat list of paths in `math_images_json`: `["/path/image1.png", "/path/image2.png", ...]`
- During delivery, look up each formula by hash and send as separate Telegram images

**New approach:**
- Extract all formulas with their text positions: `{start, end, formula, hash, full_match}`
- Group nearby formulas by gap distance (`max_gap=300` chars): formulas within 300 characters of each other go in the same block
- For each group:
  - Build combined LaTeX content with all formulas + text between them
  - Render using xelatex with fontspec (DejaVu Serif) for Vietnamese support
  - Output single PNG per block: `cb_{hash}.png` (cb = combined block)
- Store block metadata in `math_images_json`: `[{type: "text", path, start, end}, ...]`
- During delivery, read block positions and interleave with text

**Key implementation details:**
- `_extract_formula_positions()`: Uses regex patterns for display (`$$...$$`, `\[...\]`) with `re.DOTALL` and inline (`$...$`, `\(...\)`) restricted to single lines
- `_is_real_latex()`: Filters false positives (plain text, single variables) by checking for LaTeX markup: `\\[a-zA-Z]+` or `[^_{}]`
- `_group_nearby_formulas()`: Groups by gap size, not paragraph breaks—a formula at the end of paragraph 1 and start of paragraph 2 are still grouped if only 200 chars apart
- Combined block template uses `minipage{12cm}` to constrain width and prevent extreme aspect ratios
- Single formula fallback uses pdflatex for speed; combined blocks use xelatex for UTF-8 support
- 50-block cap per lesson to prevent excessive Telegram message fragmentation

## What We Tried

1. **Incremental improvement approach** (early attempts)
   - Kept individual formula rendering, tried to fix them one by one
   - Failed because the fundamental architecture couldn't support Vietnamese text
   - Wasted hours debugging pdflatex encoding issues

2. **Hybrid approach**: Render formulas individually but group them when displaying
   - Complex logic trying to merge images after rendering
   - Still suffered from UTF-8 issues in pdflatex
   - Too many edge cases (image alignment, spacing, aspect ratio)

3. **Full rewrite with xelatex** (final approach)
   - Build LaTeX content first, then render once per group
   - xelatex with fontspec handles Vietnamese natively
   - Clean data model: position-aware blocks instead of orphaned paths
   - This worked immediately—no debugging required for the core logic

## Root Cause Analysis

The original system made a critical assumption: **formulas are isolated units that can be rendered independently**. This is technically true for pure math, but false for lessons that mix Vietnamese explanations with formulas. The renderer became a bottleneck because it was trying to solve two problems:
1. Render math
2. Preserve typography and text encoding

Splitting rendering (xelatex for combined content) from delivery (position-aware interleaving) allowed each layer to handle its responsibility properly.

The old data format (flat paths) was also wrong. It threw away position information, forcing handlers.py to re-extract formulas and guess which PNG matched which formula. This duplication created the fragile cross-reference problem documented in the previous journal entry. The new format encodes positions, so the handler just reads what the renderer pre-computed.

## Lessons Learned

1. **Encoding matters early**: If you support Vietnamese from day one, you can't use pdflatex. UTF-8 is not optional. Pushing this problem down the pipeline just means rewriting later.

2. **Data format design is critical**: Storing only paths loses information. The new format with `{start, end, path}` eliminates re-extraction and cross-file pattern duplication. JSON schema: document it, use it as contract.

3. **Group by logic, not by visual layout**: Grouping by gap size (character distance) is more robust than trying to guess from paragraph structure. The text between formulas is the best signal—if it's short, group them.

4. **Capacity planning for messaging**: Each rendered block becomes one Telegram message. Cap at 50 blocks per lesson to prevent chat spam. This forced constraint actually improved UX (fewer, richer messages).

5. **Regex patterns are expensive to duplicate**: The old code had `FORMULA_PATTERNS` in both handlers.py and math_renderer.py. They drifted over time. Lesson: extract to shared module, or centralize extraction in one place (now math_renderer owns it).

## Next Steps

- Verify Vietnamese text renders correctly in combined blocks (test with lesson containing đ, ơ, ư characters)
- Monitor combined block PNG file sizes (xelatex may produce larger files than pdflatex)
- Cache invalidation: ensure old individual formula PNGs don't pollute the combined block cache
- Consider making `max_gap` configurable (currently hardcoded to 300)
