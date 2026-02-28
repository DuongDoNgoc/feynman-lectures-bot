---
title: "Fix Image Capture Pipeline"
description: "Deliver Feynman Lectures inline images/diagrams to Telegram lessons"
status: completed
priority: P1
effort: 6h
branch: main
tags: [images, crawler, delivery, pipeline]
created: 2026-02-28
---

# Fix Image Capture Pipeline

## Problem Summary

Feynman Lectures pages contain inline diagrams/figures (1044 total across 420/607 sections) that are critical for understanding physics. These images never reach Telegram users despite being partially tracked in the DB.

## Root Cause Analysis

**There are 4 distinct breakpoints in the pipeline where images are lost:**

### Break 1: Images Never Downloaded to Disk

- `scraper.py:download_images()` runs during crawl and saves to `data/raw/images/{vol}_{num:02d}/`
- **FINDING**: `data/raw/images/` is completely empty (0 subdirectories)
- Likely cause: chapters were imported/crawled before `download_images()` was added, or the crawl was done on a different machine, or images failed silently
- The function downloads via aiohttp to local filesystem, but nothing persists

### Break 2: Parser Maps to Non-Existent Local Files

- `parser.py:_build_image_map()` reconstructs `{src: local_path}` from files in `data/raw/images/{vol}_{num:02d}/`
- Since that directory is empty, `image_map` is always `{}`
- Result: `image_refs` in DB stores the **original web-relative paths** (e.g., `img/FLP_I/f01-01/f01-01_tc_big.svgz`) rather than local paths
- These relative paths are useless for Telegram delivery

### Break 3: Chunker Discards image_refs Entirely

- `chunker.py` creates `Chunk` objects from sections but **never copies `section.image_refs`** to the chunk
- The `Chunk` dataclass has no `image_refs` field at all
- When stub `Lesson` objects are created, they have no image data
- `lesson.content_enhanced = chunk.text` is plain text with `{{FORMULA_N}}` placeholders -- no image references

### Break 4: Enhancer and Delivery Ignore Original Images

- `enhancer.py` sends `content_enhanced` text to LLM for rewriting. The LLM has no knowledge of which images exist or where they should appear
- `handlers.py:send_lesson()` only handles `math_images_json` (LaTeX formula PNGs) -- there is no code path to send original Feynman diagrams
- The `_build_interleaved_segments()` function only interleaves LaTeX-rendered PNGs, not source images

### Image Format Issue

- 916 of 1044 image refs are `.svgz` (compressed SVG) -- Telegram does not support SVGZ
- 120 are `.jpg`, 8 are `.png`
- SVGZ images must be converted to PNG/JPEG before Telegram delivery

## Pipeline Gap Visualization

```
[Crawl] --html--> [Parse] --sections(image_refs)--> [Chunk] --lessons(NO images)--> [Enhance] --enhanced text--> [Render math] --> [Deliver]
                       |                                 |                                                             |
                  image_refs stored              image_refs DROPPED                                          Only LaTeX PNGs sent
                  as web-relative URLs           from Chunk model                                            No diagram images
                  (local files missing)
```

## Phases

| Phase | Description | Effort |
|-------|-------------|--------|
| 01 | Investigation report (this plan) | done |
| 02 | Implementation: download, convert, propagate, deliver images | 5h |

## Files to Modify

1. `src/crawler/scraper.py` -- re-download images or add standalone image fetch command
2. `src/crawler/parser.py` -- fix `_build_image_map()` to handle both local and web paths
3. `src/knowledge/models.py` -- add `image_refs` to `Chunk` dataclass
4. `src/content/chunker.py` -- propagate `image_refs` through chunks
5. `src/content/enhancer.py` -- include image context in LLM prompts
6. `src/bot/handlers.py` -- add image delivery alongside text and math PNGs
7. DB migration (optional) -- store converted image paths in lessons table

## Unresolved Questions

1. Should images be re-downloaded from feynmanlectures.caltech.edu (risk of Cloudflare blocking), or extracted from the stored `raw_html` in the DB?
2. For SVGZ conversion to PNG: use `cairosvg`, `librsvg`, or `Inkscape` CLI? Need to pick a dependency.
3. Should image placement in enhanced lessons be positional (like math blocks) or appended at section boundaries?
4. For combined sections in a chunk, should all image_refs from all constituent sections be included, or only from the anchor section?
