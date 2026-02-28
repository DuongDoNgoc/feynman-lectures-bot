---
title: "Phase 05: Daily Workflow Script"
phase: 5
status: completed
effort: 0.5h
---

# Phase 05: `daily-enhance.sh` — One-Command Daily Workflow

## Goal

Single script to run the full daily enhance → review → render → deploy cycle.

## New File: `daily-enhance.sh`

```bash
#!/usr/bin/env bash
# daily-enhance.sh — Daily rolling enhancement workflow
# Usage: ./daily-enhance.sh [--batch N]

set -e
BATCH=${2:-10}  # default 10 lessons/day

echo "════════════════════════════════════════"
echo " Feynman Bot — Daily Enhancement Cycle"
echo " Batch size: $BATCH lessons"
echo "════════════════════════════════════════"

# Step 0: Show current stats
echo ""
echo "📊 Current status:"
python3 -c "
import sqlite3
conn = sqlite3.connect('data/feynman.db')
total = conn.execute('SELECT COUNT(*) FROM lessons').fetchone()[0]
enhanced = conn.execute('SELECT COUNT(*) FROM lessons WHERE enhancement_status=\"completed\"').fetchone()[0]
approved = conn.execute('SELECT COUNT(*) FROM lessons WHERE approval_status=\"approved\"').fetchone()[0]
pending = total - enhanced
print(f'  Total: {total} | Enhanced: {enhanced} | Approved: {approved} | Pending: {pending}')
conn.close()
"

# Step 1: Clear stale prompts/outputs
echo ""
echo "🧹 Clearing stale prompt/output files..."
rm -f data/pending_prompts.jsonl data/enhanced_outputs.jsonl

# Step 2: Generate prompts for next batch
echo ""
echo "📝 Generating prompts for next $BATCH lessons..."
python3 pipeline.py --stage enhance --batch "$BATCH"

# Step 3: Claude Session (manual)
echo ""
echo "════════════════════════════════════════"
echo "  ⏸  PAUSE: Claude Session Required"
echo ""
echo "  In Claude Code, run:"
echo '  "Process enhancement prompts in data/pending_prompts.jsonl'
echo '   and write results to data/enhanced_outputs.jsonl"'
echo ""
read -p "  Press ENTER when Claude has finished writing outputs... " _

# Step 4: Import enhanced results
echo ""
echo "📥 Importing enhanced outputs..."
python3 pipeline.py --stage enhance --import

# Step 5: Export previews for review
echo ""
echo "📄 Exporting lesson previews..."
python3 pipeline.py --stage preview

# Step 6: Human review (interactive)
echo ""
echo "👁  Starting human review..."
python3 review.py approve-batch

# Step 7: Render approved lessons
echo ""
echo "🎨 Rendering approved lessons..."
python3 pipeline.py --stage render

# Step 8: Final stats
echo ""
echo "✅ Done! Updated status:"
python3 -c "
import sqlite3
conn = sqlite3.connect('data/feynman.db')
approved = conn.execute('SELECT COUNT(*) FROM lessons WHERE approval_status=\"approved\"').fetchone()[0]
rendered = conn.execute('SELECT COUNT(*) FROM lessons WHERE approval_status=\"approved\" AND math_images_json IS NOT NULL').fetchone()[0]
pending = conn.execute('SELECT COUNT(*) FROM lessons WHERE enhancement_status=\"pending\"').fetchone()[0]
print(f'  Approved: {approved} | Rendered: {rendered} | Still pending: {pending}')
print(f'  Bot can now deliver {approved} lessons')
conn.close()
"
echo ""
echo "🤖 Telegram bot is live with new approved lessons!"
```

## Usage

```bash
chmod +x daily-enhance.sh

# Default: 10 lessons
./daily-enhance.sh

# Custom batch size
./daily-enhance.sh --batch 5
```

## Todo

- [ ] Create `daily-enhance.sh` with above content
- [ ] Make executable: `chmod +x daily-enhance.sh`
- [ ] Add `--stage preview` to `pipeline.py` (if not exists — check `preview_exporter.py`)
- [ ] Test full run end-to-end with batch=2

## Notes

- Script pauses at Step 3 for human to run Claude session — intentional
- Bot doesn't need restart — queries DB on each delivery, picks up new approved lessons
- `--batch` flag passed as second positional arg for simplicity
