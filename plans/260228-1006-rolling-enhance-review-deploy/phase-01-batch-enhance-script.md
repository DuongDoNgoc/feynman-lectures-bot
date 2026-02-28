---
title: "Phase 01: Batch Limit for Enhance Stage"
phase: 1
status: completed
effort: 1h
---

# Phase 01: Add `--batch N` to Enhance Stage

## Goal

Limit `pipeline.py --stage enhance` to process N lessons per run.

## Current State

`generate_prompts()` in `enhancer.py` fetches ALL pending lessons:
```python
pending = await db.get_pending_lessons()  # returns all 843
```

## Changes

### `src/content/enhancer.py`

```python
async def generate_prompts(config: dict, batch_size: int = 0) -> int:
    """Generate enhancement prompts. batch_size=0 means all pending."""
    pending = await db.get_pending_lessons()

    # Limit to batch_size if specified
    if batch_size > 0:
        pending = pending[:batch_size]
    ...
```

Also update `run_enhancer()`:
```python
async def run_enhancer(config: dict, import_mode: bool = False, batch_size: int = 0):
    if import_mode:
        await import_outputs(config)
    else:
        await generate_prompts(config, batch_size=batch_size)
```

### `pipeline.py`

Add `--batch` argument:
```python
parser.add_argument("--batch", type=int, default=0,
                    help="Limit enhance stage to N lessons (0=all)")
```

Pass to enhancer:
```python
if "enhance" in stages:
    await run_enhancer(config, import_mode=import_mode, batch_size=args.batch)
```

## Usage After Fix

```bash
# Enhance exactly 10 lessons
python pipeline.py --stage enhance --batch 10

# Import results
python pipeline.py --stage enhance --import
```

## Todo

- [ ] Add `batch_size` param to `generate_prompts()`
- [ ] Add `batch_size` param to `run_enhancer()`
- [ ] Add `--batch` arg to `pipeline.py`
- [ ] Also: clear `data/pending_prompts.jsonl` before each batch run (avoid stale data)

## Notes

- Enhancer already uses append mode + done_ids tracking → idempotent
- Delete or truncate `pending_prompts.jsonl` at start of each batch to keep it clean
- `enhanced_outputs.jsonl` should also be cleared after each `--import` run
