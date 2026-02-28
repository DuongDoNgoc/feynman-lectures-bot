# Phase 01: Investigation Report

## Methodology

Analyzed these files end-to-end: `scraper.py`, `parser.py`, `chunker.py`, `enhancer.py`, `math_renderer.py`, `handlers.py`, `db.py`, `models.py`, `pipeline.py`, `config.yaml`. Queried `data/feynman.db` directly. Inspected filesystem.

## Findings by Component

### 1. `src/crawler/scraper.py` -- Image Download

- `download_images(html, chapter_dir, base_url)` extracts all `<img src>` from HTML, downloads via aiohttp to `chapter_dir`
- Called in `run_crawler()` at line 214: `image_map = await download_images(html, chapter_dir)`
- `chapter_dir = data/raw/images/{volume}_{ch_num:02d}` (e.g., `data/raw/images/I_01`)
- **Status: FUNCTION EXISTS but files missing.** `data/raw/images/` has 0 subdirectories
- Probable causes: (a) chapters crawled before download_images was added, (b) crawled on another machine, (c) images lost during data migration
- The `image_map` returned by download_images is not stored anywhere -- only used transiently during crawl

### 2. `src/crawler/parser.py` -- Image Extraction

- `parse_chapter(raw_html, image_map)` receives `image_map: dict[str, str]` (original_src -> local_path)
- At lines 273-279: iterates `<img>` tags in section elements, maps `src` to local path via `image_map`
- `_build_image_map()` reconstructs map from filesystem: reads filenames in `data/raw/images/{vol}_{num:02d}/`
- **Since filesystem is empty, `image_map` = `{}`**
- Result: `image_refs` stores raw web-relative URLs like `img/FLP_I/f01-01/f01-01_tc_big.svgz`
- The mapping logic (`image_map.get(src, src)`) falls back to `src` when no local file found

### 3. DB `sections.image_refs` -- What's Actually Stored

```
Sections with non-empty image_refs: 420 / 607 (69%)
Total image references: 1044
Breakdown: 916 svgz, 120 jpg, 8 png
```

Sample values (all web-relative, not local):
```
["img/FLP_I/f01-00/f01-00.jpg"]
["img/FLP_I/f01-01/f01-01_tc_big.svgz", "img/FLP_I/f01-02/f01-02_tc_big.svgz"]
```

These are the `src` attribute values from `<img>` tags, relative to `https://www.feynmanlectures.caltech.edu/`.

### 4. `src/content/chunker.py` -- Image Refs Dropped

- `Chunk` dataclass (models.py:42-51) has: `text, formulas, word_count, section_ids, chapter_number, section_number, section_title`
- **No `image_refs` field**
- `chunk_sections()` copies `section.content_text` and `section.latex_formulas` but **ignores `section.image_refs`**
- Lesson stubs created with `content_enhanced=chunk.text` have zero image awareness

### 5. `src/content/enhancer.py` -- No Image Context

- LLM prompt templates include `{content}` (plain text) and `{formulas}` (LaTeX strings)
- No template field for images/diagrams
- The LLM sometimes references "Figure" or "Hinh" in output (363 lessons mention "figure/Figure", 35 mention "Hinh") but these are from the original text descriptions, not actual image references
- **Enhanced content never includes actionable image paths or placeholders**

### 6. `src/bot/handlers.py` -- Delivery Only Handles Math PNGs

- `send_lesson()` (line 204) loads `lesson.math_images_json`
- `_build_interleaved_segments()` interleaves text chunks with rendered LaTeX PNG images
- **No code reads `image_refs` from the section or resolves original diagram images**
- The `Lesson` model has `math_images_json` for rendered formulas but no field for source diagram images

### 7. `src/renderer/math_renderer.py` -- Renders LaTeX Only

- `render_lesson_math()` extracts LaTeX from `content_enhanced`, renders to PNG
- Stores results in `lesson.math_images_json` as block dicts: `{type, path, start, end}`
- **Completely unrelated to source images** -- only handles inline/display LaTeX formulas
- 326 rendered PNGs exist in `data/images/` (all formula renders, no diagrams)

### 8. Image Format Compatibility

| Format | Count | Telegram Support | Action Needed |
|--------|-------|-----------------|---------------|
| .svgz  | 916   | Not supported   | Decompress + rasterize to PNG |
| .jpg   | 120   | Supported       | Download only |
| .png   | 8     | Supported       | Download only |

### 9. HTML Structure of Feynman Lectures Images

Chapter I_01 has 21 content-area `<img>` tags (excluding 5 nav icons). Example:
```
img/FLP_I/f01-00/f01-00.jpg          (chapter header photo)
img/FLP_I/f01-01/f01-01_tc_big.svgz  (physics diagram)
```

Full URLs resolve to: `https://www.feynmanlectures.caltech.edu/img/FLP_I/f01-01/f01-01_tc_big.svgz`

The parser correctly identifies which `<img>` tags belong to which section (lines 273-279 of parser.py). The extraction logic is sound -- the problem is entirely in the downstream pipeline.

## Summary: Where Images Are Lost

| Stage | Has Images? | Issue |
|-------|------------|-------|
| Raw HTML in DB | YES (26 `<img>` per chapter avg) | Stored correctly |
| `sections.image_refs` | YES (1044 refs, 420 sections) | Paths are web-relative, not local |
| `data/raw/images/` filesystem | NO (empty) | Files never persisted or were lost |
| Chunk model | NO | `image_refs` field missing from `Chunk` dataclass |
| Lesson creation (chunker) | NO | No image data propagated |
| Enhancer prompts | NO | LLM has no image context |
| `lesson.math_images_json` | LaTeX only | Only formula PNGs, no diagrams |
| `send_lesson()` delivery | LaTeX PNGs only | No code path for diagram images |
