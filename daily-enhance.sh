#!/usr/bin/env bash
# daily-enhance.sh — Daily rolling enhancement workflow
#
# Usage:
#   ./daily-enhance.sh           # enhance 10 lessons (default)
#   ./daily-enhance.sh 5         # enhance 5 lessons
#   ./daily-enhance.sh --stats   # show stats only

set -e
cd "$(dirname "$0")"

BATCH=${1:-10}

# Stats-only mode
if [[ "$1" == "--stats" ]]; then
    python3 review.py stats
    exit 0
fi

echo "════════════════════════════════════════════════════"
echo "  Feynman Bot — Daily Enhancement Cycle"
echo "  Batch: $BATCH lessons"
echo "════════════════════════════════════════════════════"

# Step 0: Current stats
echo ""
python3 review.py stats

# Step 1: Generate prompts for next batch (auto-clears stale files)
echo "📝 Step 1/5 — Generating prompts for $BATCH lessons..."
python3 pipeline.py --stage enhance --batch "$BATCH"

# Step 2: Claude Session (manual pause)
echo ""
echo "════════════════════════════════════════════════════"
echo "  ⏸  PAUSE — Claude Session Required"
echo ""
echo "  In Claude Code (this session), run:"
echo '  "Process each prompt in data/pending_prompts.jsonl.'
echo '   For each record, generate enhanced content based on'
echo '   the system + prompt fields, and append the result to'
echo '   data/enhanced_outputs.jsonl as JSON:'
echo '   {\"lesson_id\": N, \"lesson_type\": \"...\", \"content\": \"...\"}'
echo '   Process all records in the file."'
echo ""
read -rp "  Press ENTER when Claude has finished writing outputs... "

# Step 3: Import enhanced results
echo ""
echo "📥 Step 2/5 — Importing enhanced outputs..."
python3 pipeline.py --stage enhance --import

# Step 4: Export previews for review
echo ""
echo "📄 Step 3/5 — Exporting lesson previews..."
python3 pipeline.py --stage preview

# Step 5: Human review (interactive)
echo ""
echo "👁  Step 4/5 — Human review..."
python3 review.py approve-batch

# Step 6: Render approved lessons
echo ""
echo "🎨 Step 5/5 — Rendering approved lessons..."
python3 pipeline.py --stage render

# Done
echo ""
echo "════════════════════════════════════════════════════"
echo "  ✅ Daily cycle complete!"
echo ""
python3 review.py stats
echo "  Telegram bot is live with new approved lessons."
echo "════════════════════════════════════════════════════"
