# Phase 02: Implementation Plan

## Overview

Fix the 4 breakpoints identified in Phase 01 to deliver Feynman Lectures diagrams to Telegram.

## Step 1: Download and Convert Source Images (2h)

### 1a. Create standalone image downloader script

File: `scripts/download_images.py`

- Read `raw_html` from all chapters in DB
- For each chapter, call the existing `download_images()` logic from `scraper.py`
- Save to `data/raw/images/{volume}_{ch_num:02d}/`
- This avoids re-crawling (uses stored HTML) and respects Cloudflare concerns
- Add rate limiting: 0.5s delay between image fetches to avoid blocks
- Log summary: downloaded / failed / skipped (already exists)

```python
# Pseudocode
for chapter in all_chapters:
    chapter_dir = f"data/raw/images/{chapter.volume}_{chapter.number:02d}"
    image_map = await download_images(chapter.raw_html, chapter_dir, chapter.url)
```

### 1b. Convert SVGZ to PNG

After download, convert `.svgz` files to PNG for Telegram compatibility.

- Add dependency: `cairosvg` (pure Python, no system deps beyond cairo which is usually present)
- Or use: `gzip` decompress `.svgz` -> `.svg`, then `cairosvg.svg2png()`
- Target DPI: match `config.yaml renderer.dpi` (1200) or use a lower default (300) for diagrams
- Store converted PNGs alongside originals: `data/raw/images/{vol}_{num}/filename.png`

```python
import gzip
import cairosvg

def convert_svgz_to_png(svgz_path: str, png_path: str, dpi: int = 300):
    with gzip.open(svgz_path, 'rb') as f:
        svg_data = f.read()
    cairosvg.svg2png(bytestring=svg_data, write_to=png_path, dpi=dpi)
```

### 1c. Re-run parser to update `image_refs` with local paths

- After images are downloaded, re-parse chapters to update `image_refs` from web-relative to local
- Or: add a migration script that updates existing `sections.image_refs` to point to local converted PNG paths
- **Preferred**: migration script (avoids full re-parse which would duplicate sections)

```python
# For each section with image_refs:
#   Replace "img/FLP_I/f01-01/f01-01_tc_big.svgz"
#   With    "data/raw/images/I_01/f01-01_tc_big.png"
```

## Step 2: Propagate image_refs Through Pipeline (1h)

### 2a. Add `image_refs` to `Chunk` dataclass

File: `src/knowledge/models.py`

```python
@dataclass
class Chunk:
    text: str
    formulas: list = field(default_factory=list)
    image_refs: list = field(default_factory=list)  # ADD THIS
    word_count: int = 0
    section_ids: list = field(default_factory=list)
    chapter_number: int = 0
    section_number: int = 0
    section_title: str = ""
```

### 2b. Carry image_refs in chunker

File: `src/content/chunker.py`, in `chunk_sections()`:

```python
# After line 49: current.formulas.extend(section.latex_formulas)
current.image_refs.extend(section.image_refs)
```

### 2c. Add `diagram_images_json` to Lesson model and DB

File: `src/knowledge/models.py` -- add field to `Lesson`:
```python
diagram_images_json: Optional[str] = None  # JSON list of local image paths
```

File: `src/knowledge/db.py` -- add migration:
```sql
ALTER TABLE lessons ADD COLUMN diagram_images_json TEXT DEFAULT NULL;
```

### 2d. Store image_refs when creating lesson stubs

File: `src/content/chunker.py`, in lesson creation loop:

```python
import json
lesson = Lesson(
    ...
    diagram_images_json=json.dumps(chunk.image_refs) if chunk.image_refs else None,
)
```

## Step 3: Include Image Context in Enhanced Content (1h)

### 3a. Add image placeholders in enhancer prompts

File: `src/content/enhancer.py`

- Fetch `diagram_images_json` for each lesson
- Add to prompt template: list of available figures with descriptions
- Add instruction: "Use `{{FIGURE_N}}` placeholders where the original diagrams should appear"

```python
PROMPT_TEMPLATES["concept"] += """
HÌNH ẢNH MINH HỌA CÓ SẴN:
{figures}
Sử dụng placeholder {{FIGURE_N}} ở vị trí phù hợp trong bài giảng.
"""
```

### 3b. Parse FIGURE_N placeholders in enhanced content

After enhancement, record which figures were referenced and at what text positions.

## Step 4: Deliver Diagram Images via Telegram (1h)

### 4a. Extend `_build_interleaved_segments()` in handlers.py

File: `src/bot/handlers.py`

- Load `diagram_images_json` from lesson
- Find `{{FIGURE_N}}` placeholders in `content_enhanced`
- Insert image segments at placeholder positions
- Merge with existing math image segments, sort by position

```python
# In send_lesson():
diagram_blocks = []
if lesson.diagram_images_json:
    diagrams = json.loads(lesson.diagram_images_json)
    for i, path in enumerate(diagrams):
        placeholder = f"{{{{FIGURE_{i}}}}}"
        pos = lesson.content_enhanced.find(placeholder)
        if pos >= 0 and os.path.exists(path):
            diagram_blocks.append({
                "type": "image",
                "path": path,
                "start": pos,
                "end": pos + len(placeholder),
            })

# Merge math blocks + diagram blocks, sort by position
all_blocks = blocks + diagram_blocks
all_blocks.sort(key=lambda b: b["start"])
```

### 4b. Alternative: Append diagrams after section text

Simpler approach if positional interleaving is too complex for v1:
- After sending text + math PNGs, send all diagram images in order
- Add caption: "Hinh {N}: {description}" for each

## Migration Strategy for Existing Data

Since 420 sections already have `image_refs` and lessons already exist:

1. Run image download script (Step 1a)
2. Run SVGZ-to-PNG conversion (Step 1b)
3. Run DB migration to add `diagram_images_json` column (Step 2c)
4. Run migration script to backfill `diagram_images_json` for existing lessons from their linked sections' `image_refs`
5. No need to re-run enhancer for existing lessons -- use the "append after text" approach (Step 4b) as default for already-enhanced content

## Dependency Tree

```
Step 1a (download)
    -> Step 1b (convert svgz)
        -> Step 1c (update DB refs)
            -> Step 2c+2d (lesson field + backfill)
                -> Step 4 (delivery)

Step 2a+2b (chunk model) -- independent, can run anytime
Step 3 (enhancer prompts) -- only needed for NEW lessons
```

## Testing

1. **Unit**: download a single chapter's images, verify files exist
2. **Unit**: convert one .svgz to .png, verify readable
3. **Integration**: run `scripts/download_images.py`, verify `data/raw/images/` populated
4. **Integration**: use `scripts/test-interleaved.py` to send a lesson with diagrams to Telegram
5. **Manual QA**: check image quality on mobile Telegram

## Risks

| Risk | Mitigation |
|------|-----------|
| Cloudflare blocks image downloads | Use stored `raw_html` to get URLs, add User-Agent + delays |
| SVGZ files need system-level cairo | Use `cairosvg` pip package; fallback: skip SVGZ, only serve JPG/PNG |
| Large image files slow Telegram delivery | Resize to max 1280px wide before sending |
| Enhanced content doesn't have FIGURE placeholders | Use append-after-text approach for existing lessons |
