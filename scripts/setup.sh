#!/usr/bin/env bash
# Setup script for Feynman Bot on WSL2/Ubuntu
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

echo "=== Feynman Bot Setup ==="
cd "$PROJECT_DIR"

# Python virtual environment
if [ ! -d ".venv" ]; then
    echo "[1/5] Creating virtual environment..."
    python3 -m venv .venv
fi
echo "[2/5] Installing Python dependencies..."
.venv/bin/pip install --upgrade pip -q
.venv/bin/pip install -r requirements.txt -q

# Playwright browsers
echo "[3/5] Installing Playwright Chromium..."
.venv/bin/playwright install chromium --with-deps

# LaTeX (minimal install for math rendering)
echo "[4/5] Installing LaTeX tools..."
if ! command -v pdflatex &>/dev/null; then
    sudo apt-get update -q
    sudo apt-get install -y -q \
        texlive-latex-base \
        texlive-fonts-recommended \
        texlive-latex-extra \
        dvipng \
        poppler-utils
else
    echo "  pdflatex already installed, skipping."
fi

# Data directories
echo "[5/5] Creating data directories..."
mkdir -p data/raw/images data/images

echo ""
echo "=== Setup complete ==="
echo ""
echo "Required environment variables:"
echo "  export TELEGRAM_BOT_TOKEN=your_token_here"
echo "  export TELEGRAM_CHAT_ID=your_chat_id_here"
echo "  export ANTHROPIC_API_KEY=your_key_here      # for content enhancement"
echo "  export DEEPSEEK_API_KEY=your_key_here       # for interactive Q&A"
echo ""
echo "Run the pipeline:  .venv/bin/python pipeline.py"
echo "Run the bot:       .venv/bin/python main.py"
