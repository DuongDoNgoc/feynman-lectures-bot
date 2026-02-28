---
status: completed
---

# Phase 01: Interleaved LaTeX Delivery

## Overview

Replace the current "text dump + image pile" approach in `send_lesson()` with interleaved text/image segments. Only `src/bot/handlers.py` is modified.

## Critical: Formula-to-PNG Mapping

`render_lesson_math()` (math_renderer.py:152-176) extracts formulas in this order:

```python
patterns = [
    r"\$\$(.*?)\$\$",          # 1. display $$...$$
    r"\\\[(.*?)\\\]",          # 2. display \[...\]
    r"\$((?:[^$]|\\.)+?)\$",   # 3. inline $...$
    r"\\\((.*?)\\\)",          # 4. inline \(...\)
]
# Iterates each pattern, then each match within that pattern
# Deduplicates: skips if formula text already seen
# Caps at 20 formulas
```

The PNGs in `math_images_json` follow this grouped order. **Some formulas may have failed to render** (the renderer skips them with a warning), so `len(png_paths)` can be less than `len(formulas)`.

### Mapping Strategy

To correctly map PNGs to text positions:

1. Re-extract formulas using the **same patterns and order** as the renderer
2. For each extracted formula, check if a PNG was successfully rendered by using the **same hash function** (`md5(formula.encode()).hexdigest()[:12]`) and checking against filenames in `math_images_json`
3. This hash-based lookup is more robust than index-based matching because it handles skipped/failed renders

## Step 1: Add Formula Position Extraction

Add helper `_extract_formula_positions(content: str) -> list[dict]`:

```python
import re
import hashlib

FORMULA_PATTERNS = [
    (r"\$\$(.*?)\$\$", "$$"),
    (r"\\\[(.*?)\\\]", r"\["),
    (r"\$((?:[^$]|\\.)+?)\$", "$"),
    (r"\\\((.*?)\\\)", r"\("),
]

def _formula_hash(formula: str) -> str:
    """Same hash as math_renderer._formula_hash."""
    return hashlib.md5(formula.encode()).hexdigest()[:12]

def _extract_formula_positions(content: str) -> list[dict]:
    """Find all formulas with their text positions, ordered by position.

    Returns list of:
      {"start": int, "end": int, "formula": str, "hash": str, "full_match": str}
    sorted by start position.
    """
    seen_formulas = set()
    results = []

    # Collect ALL matches across all patterns with positions
    for pattern, _ in FORMULA_PATTERNS:
        for m in re.finditer(pattern, content, re.DOTALL):
            formula = m.group(1).strip()
            if formula and len(formula) > 2 and formula not in seen_formulas:
                seen_formulas.add(formula)
                results.append({
                    "start": m.start(),
                    "end": m.end(),
                    "formula": formula,
                    "hash": _formula_hash(formula),
                    "full_match": m.group(0),
                })

    # Sort by position in text (critical for interleaving)
    results.sort(key=lambda x: x["start"])
    return results
```

**Key**: The deduplication logic (`seen_formulas`) must match the renderer exactly. Same formula appearing twice: first occurrence gets the PNG, second occurrence stays as text.

## Step 2: Add Segment Builder

Add `_build_interleaved_segments(content: str, img_paths: list[str]) -> list[dict]`:

```python
def _build_interleaved_segments(
    content: str,
    img_paths: list[str],
) -> list[dict]:
    """Split content into interleaved text/image segments.

    Args:
        content: lesson content_enhanced text
        img_paths: list of PNG file paths from math_images_json

    Returns:
        list of {"type": "text", "content": str} or {"type": "image", "path": str}
    """
    # Build hash -> path lookup from available PNGs
    png_by_hash = {}
    for p in img_paths:
        # Extract hash from filename: "{hash}.png"
        basename = os.path.basename(p)
        h = os.path.splitext(basename)[0]
        if os.path.exists(p):
            png_by_hash[h] = p

    formulas = _extract_formula_positions(content)

    if not formulas:
        # No formulas found — return entire content as text
        return [{"type": "text", "content": content}]

    segments = []
    cursor = 0

    for f in formulas:
        # Text before this formula
        text_before = content[cursor:f["start"]]
        if text_before.strip():
            segments.append({"type": "text", "content": text_before})

        # Formula segment
        png_path = png_by_hash.get(f["hash"])
        if png_path:
            segments.append({"type": "image", "path": png_path})
        else:
            # Fallback: keep formula text inline
            segments.append({"type": "text", "content": f["full_match"]})

        cursor = f["end"]

    # Remaining text after last formula
    text_after = content[cursor:]
    if text_after.strip():
        segments.append({"type": "text", "content": text_after})

    return segments
```

## Step 3: Add Segment Coalescing

Consecutive short text segments should be merged to avoid Telegram message spam:

```python
def _coalesce_segments(segments: list[dict], min_text_len: int = 200) -> list[dict]:
    """Merge consecutive text segments shorter than min_text_len."""
    if not segments:
        return segments

    result = []
    text_buffer = ""

    for seg in segments:
        if seg["type"] == "text":
            text_buffer += seg["content"]
        else:
            # Image segment — flush text buffer first
            if text_buffer.strip():
                result.append({"type": "text", "content": text_buffer})
                text_buffer = ""
            result.append(seg)

    # Flush remaining text
    if text_buffer.strip():
        result.append({"type": "text", "content": text_buffer})

    # Second pass: merge consecutive short text segments
    # (This happens when multiple formulas have fallback text in a row)
    merged = []
    for seg in result:
        if (seg["type"] == "text" and merged and merged[-1]["type"] == "text"
                and len(merged[-1]["content"]) < min_text_len):
            merged[-1]["content"] += seg["content"]
        else:
            merged.append(seg)

    return merged
```

## Step 4: Refactor `send_lesson()`

Replace the current implementation (handlers.py:94-118):

```python
async def send_lesson(update: Update, context: ContextTypes.DEFAULT_TYPE, lesson: Lesson):
    """Deliver lesson with text and formula images interleaved inline."""
    chat_id = update.effective_chat.id

    # Parse available math images
    img_paths = []
    if lesson.math_images_json:
        img_paths = [p for p in json.loads(lesson.math_images_json) if os.path.exists(p)]

    # Build interleaved segments
    segments = _build_interleaved_segments(lesson.content_enhanced, img_paths)
    segments = _coalesce_segments(segments)

    for seg in segments:
        if seg["type"] == "text":
            # Split long text to respect Telegram 4096 char limit
            for part in split_message(seg["content"]):
                try:
                    await context.bot.send_message(chat_id, part, parse_mode="Markdown")
                except Exception:
                    await context.bot.send_message(chat_id, part)
        elif seg["type"] == "image":
            try:
                await context.bot.send_photo(
                    chat_id=chat_id,
                    photo=InputFile(open(seg["path"], "rb")),
                )
            except Exception as e:
                log.warning("Failed to send math image %s: %s", seg["path"], e)
```

### What Changed vs. Current Code

| Aspect | Before | After |
|--------|--------|-------|
| Text delivery | Full content sent first | Content split at formula boundaries |
| Image delivery | All PNGs dumped at end | Each PNG sent at its formula position |
| `"Cong thuc"` header | Sent before image pile | Removed (no longer needed) |
| Missing PNG fallback | Image silently skipped | Original formula text kept inline |
| New helpers | None | `_extract_formula_positions`, `_build_interleaved_segments`, `_coalesce_segments`, `_formula_hash` |

## Step 5: Add Imports

Add to existing imports at top of handlers.py:

```python
import hashlib
import re
```

(`os` and `json` are already imported.)

## Edge Cases

1. **Lesson with no formulas**: `_extract_formula_positions` returns empty list; `_build_interleaved_segments` returns single text segment. Behaves identically to current code.
2. **Lesson with no math_images_json** (None or empty): `img_paths` is empty; all formulas fall back to inline text. Same as current text-only delivery.
3. **All PNGs missing from disk**: Every formula keeps its original LaTeX text in the message. Graceful degradation.
4. **Duplicate formula text**: First occurrence gets the PNG (matches renderer dedup). Subsequent occurrences also map to the same PNG via hash lookup, so they also get the image. This is correct behavior.
5. **Very long lesson with 20+ formulas**: Renderer caps at 20. Formulas beyond the 20th will not have PNGs; they fall back to text. The hash-based lookup handles this naturally.
6. **Formula containing nested `$` or escaped delimiters**: Same regex as renderer, so same extraction. If renderer handled it, delivery handles it.

## Testing Approach

1. **Unit test `_extract_formula_positions`**: Provide sample content with mixed formula types, verify positions and hashes match what renderer would produce.
2. **Unit test `_build_interleaved_segments`**: Mock img_paths with known hashes, verify correct segment ordering.
3. **Unit test `_coalesce_segments`**: Verify short text segments merge, image segments preserved.
4. **Integration test**: Use existing lesson from DB, render math, then verify `send_lesson()` sends messages in correct order (mock bot).

## Risks

- **Regex mismatch**: If `render_lesson_math()` regex patterns ever change without updating `FORMULA_PATTERNS` in handlers.py, PNG mapping breaks. Mitigation: add a comment cross-referencing `math_renderer.py:155-159`.
- **Telegram rate limiting**: Many short messages in rapid succession may trigger rate limits. Mitigation: coalescing handles this; could add `asyncio.sleep(0.3)` between sends if needed, but start without it.
- **Message ordering**: Telegram guarantees in-order delivery for sequential `await` calls to same chat. No race condition.

## Unresolved Questions

None -- all design decisions are covered above.
