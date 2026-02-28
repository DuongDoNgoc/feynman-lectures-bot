# Feynman Bot - Deployment Guide

**Last Updated**: 2026-02-28

This guide covers deploying Feynman Bot to production environments.

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Environment Setup](#environment-setup)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Running the Bot](#running-the-bot)
6. [Running the Pipeline](#running-the-pipeline)
7. [Process Management](#process-management)
8. [Monitoring](#monitoring)
9. [Backup & Recovery](#backup--recovery)
10. [Troubleshooting](#troubleshooting)

---

## Prerequisites

### System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| OS | Ubuntu 20.04+ | Ubuntu 22.04 LTS |
| RAM | 1 GB | 2 GB |
| Disk | 5 GB | 10 GB |
| Python | 3.11+ | 3.12 |

### Required Software

```bash
# Python 3.11+
python3 --version

# pip
pip3 --version

# LaTeX (for formula rendering)
pdflatex --version
xelatex --version

# Git
git --version
```

### External Services

| Service | Purpose | Required |
|---------|---------|----------|
| Telegram Bot API | Messaging | Yes |
| Anthropic API | Content enhancement | Yes |
| DeepSeek API | Q&A | Yes |

---

## Environment Setup

### 1. Create Bot Token

1. Open Telegram and search for `@BotFather`
2. Send `/newbot` and follow instructions
3. Save the bot token

### 2. Get API Keys

**Anthropic:**
1. Go to https://console.anthropic.com/
2. Create account and get API key
3. Key format: `sk-ant-api03-...`

**DeepSeek:**
1. Go to https://platform.deepseek.com/
2. Create account and get API key
3. Key format: `sk-...`

### 3. Get Chat ID

```bash
# Start your bot, then visit:
https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates

# Send a message to your bot, then refresh
# Look for "chat":{"id":123456789}
```

---

## Installation

### Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/feynman-bot.git
cd feynman-bot
```

### Step 2: Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
# or
.venv\Scripts\activate  # Windows
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Install LaTeX

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install -y texlive-latex-base texlive-fonts-recommended texlive-fonts-extra

# Install DejaVu fonts (for xelatex)
sudo apt-get install -y fonts-dejavu-core fonts-dejavu-extra

# Verify
pdflatex --version
xelatex --version
fc-list | grep DejaVu
```

### Step 5: Create Data Directories

```bash
mkdir -p data/images data/raw/images
```

---

## Configuration

### Environment Variables

Create `.env` file or export variables:

```bash
# Required
export TELEGRAM_BOT_TOKEN="123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
export TELEGRAM_CHAT_ID="123456789"
export ANTHROPIC_API_KEY="sk-ant-api03-..."
export DEEPSEEK_API_KEY="sk-..."
```

### config.yaml

The main configuration file. Key sections:

```yaml
telegram:
  bot_token: "${TELEGRAM_BOT_TOKEN}"
  chat_id: "${TELEGRAM_CHAT_ID}"

schedule:
  timezone: "Asia/Bangkok"
  times: ["07:20", "12:15", "18:30"]
  lesson_types: ["concept", "deep_dive", "quiz"]
  review_days: ["thu", "sun"]

database:
  path: "data/feynman.db"

enhancement:
  provider: "anthropic"
  model: "claude-sonnet-4-6"
  api_key: "${ANTHROPIC_API_KEY}"
  max_retries: 3

qa:
  provider: "deepseek"
  model: "deepseek-chat"
  api_key: "${DEEPSEEK_API_KEY}"
  max_retries: 2

logging:
  level: "INFO"
  file: "data/feynman-bot.log"
```

---

## Running the Bot

### Initial Database Setup

```bash
# Initialize database (creates tables)
python -c "import asyncio; from src.utils import load_config; from src.knowledge.db import init_db; asyncio.run(init_db(load_config()))"
```

### Run Content Pipeline (First Time)

```bash
# Stage 1: Crawl chapters
python pipeline.py --stage crawl

# Stage 2: Parse HTML to sections
python pipeline.py --stage parse

# Stage 3: Chunk sections into lessons
python pipeline.py --stage chunk

# Stage 4: Enhance lessons (batch of 10)
python pipeline.py --stage enhance --direct --batch 10

# Stage 5: Render math formulas
python pipeline.py --stage render

# Review and approve lessons
python scripts/review.py list
python scripts/review.py approve-batch
```

### Start Bot

```bash
python main.py
```

---

## Running the Pipeline

### Daily Enhancement Workflow

```bash
# Enhance 10 more lessons
python pipeline.py --stage enhance --direct --batch 10

# Review pending lessons
python scripts/review.py list

# Approve batch
python scripts/review.py approve-batch

# Render new formulas
python pipeline.py --stage render
```

### Using the Daily Script

```bash
# Created: scripts/daily-enhance.sh
./scripts/daily-enhance.sh
```

---

## Process Management

### Using systemd (Recommended)

Create service file:

```bash
sudo nano /etc/systemd/system/feynman-bot.service
```

```ini
[Unit]
Description=Feynman Lectures Bot
After=network.target

[Service]
Type=simple
User=youruser
WorkingDirectory=/home/youruser/feynman-bot
Environment="TELEGRAM_BOT_TOKEN=..."
Environment="TELEGRAM_CHAT_ID=..."
Environment="ANTHROPIC_API_KEY=..."
Environment="DEEPSEEK_API_KEY=..."
ExecStart=/home/youruser/feynman-bot/.venv/bin/python main.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start:

```bash
sudo systemctl daemon-reload
sudo systemctl enable feynman-bot
sudo systemctl start feynman-bot
sudo systemctl status feynman-bot
```

### Using screen (Simple)

```bash
screen -S feynman-bot
source .venv/bin/activate
python main.py
# Press Ctrl+A, D to detach
# screen -r feynman-bot to reattach
```

---

## Monitoring

### Log Files

```bash
# View recent logs
tail -100 data/feynman-bot.log

# Follow logs in real-time
tail -f data/feynman-bot.log

# Search for errors
grep -i error data/feynman-bot.log | tail -20
```

### Health Check

```bash
# Run health check
python -m src.monitoring.health

# Expected output:
# ==================================================
# Health Check Report: HEALTHY
# Timestamp: 2026-02-28T20:00:00
# ==================================================
# ✅ database: OK (8 tables) (5.23ms)
# ✅ llm_api: OK (deepseek) (1234.56ms)
# ✅ telegram_api: OK (@yourbot) (234.56ms)
# ==================================================
```

### Bot Status Command

Send `/status` to the bot in Telegram to see:
- Uptime
- Lessons sent
- Errors
- Average response times

---

## Backup & Recovery

### Database Backup

```bash
# Manual backup
cp data/feynman.db data/backups/feynman-$(date +%Y%m%d).db

# Automated backup script
cat > scripts/backup-db.sh << 'EOF'
#!/bin/bash
BACKUP_DIR="data/backups"
mkdir -p $BACKUP_DIR
cp data/feynman.db $BACKUP_DIR/feynman-$(date +%Y%m%d-%H%M).db
# Keep last 7 days
find $BACKUP_DIR -name "*.db" -mtime +7 -delete
EOF
chmod +x scripts/backup-db.sh

# Add to crontab (daily at 2am)
# 0 2 * * * /home/youruser/feynman-bot/scripts/backup-db.sh
```

### Recovery

```bash
# Stop bot
sudo systemctl stop feynman-bot

# Restore database
cp data/backups/feynman-20260228.db data/feynman.db

# Restart bot
sudo systemctl start feynman-bot
```

---

## Troubleshooting

### Bot Not Starting

```bash
# Check logs
tail -50 data/feynman-bot.log

# Verify environment variables
echo $TELEGRAM_BOT_TOKEN
echo $ANTHROPIC_API_KEY

# Test database
sqlite3 data/feynman.db "SELECT COUNT(*) FROM lessons"

# Test API connectivity
python -m src.monitoring.health
```

### Common Issues

| Issue | Solution |
|-------|----------|
| "API key not configured" | Set environment variables |
| "database is locked" | Stop all processes using DB |
| "pdflatex not found" | Install texlive |
| "Circuit breaker tripped" | Wait 24h or use manual download |

See `docs/troubleshooting-guide.md` for detailed troubleshooting.

---

## Security Checklist

- [ ] `.env` file not in git (add to `.gitignore`)
- [ ] API keys stored in environment variables
- [ ] Database file not world-readable (`chmod 600 data/feynman.db`)
- [ ] Bot token kept secret
- [ ] Regular database backups configured

---

## Upgrade Procedure

```bash
# 1. Stop bot
sudo systemctl stop feynman-bot

# 2. Backup database
cp data/feynman.db data/feynman.db.backup

# 3. Pull changes
git pull origin main

# 4. Update dependencies
source .venv/bin/activate
pip install -r requirements.txt

# 5. Run migrations (if any)
# python scripts/migrate.py

# 6. Start bot
sudo systemctl start feynman-bot

# 7. Verify
tail -f data/feynman-bot.log
```

---

## Support

- **Logs**: `data/feynman-bot.log`
- **Health Check**: `python -m src.monitoring.health`
- **Troubleshooting**: `docs/troubleshooting-guide.md`
- **Architecture**: `docs/system-architecture.md`
