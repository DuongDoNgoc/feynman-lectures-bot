# Feynman Bot

Automated Telegram-based physics learning system delivering personalized micro-lessons from Richard Feynman's "Lectures on Physics."

**Project Status**: Live (v2.0.0)
**Last Updated**: 2026-03-01
**Bot Status**: Running (since 2026-03-01, polling mode, 3 lessons/day)

## Features

- **Automated Content Pipeline**: 5-stage offline batch processing (crawl, parse, chunk, enhance, render)
- **Smart Lesson Delivery**: 3 daily lessons at configurable times (concept, deep_dive, quiz) with source attribution
- **AI-Powered Enhancement**: LLM-transformation of raw physics content into engaging lessons
- **Interactive Q&A**: Real-time AI assistance with conversation history
- **Progress Tracking**: Streak monitoring and completion statistics
- **Vietnamese Language**: Localized content with English physics terminology
- **Advanced Formula Rendering**: Single formula (pdflatex) and grouped blocks (xelatex+fontspec) with UTF-8 support
- **Table Rendering**: Markdown tables converted to PNG via LaTeX for Telegram delivery
- **Diagram Support**: Inline SVG/JPG diagrams from Feynman Lectures chapters included in lessons
- **Approval Workflow**: Human review gate with preview export and approval tracking before delivery
- **Source Attribution**: Lessons link back to source Feynman Lectures chapters

## Quick Start

### Prerequisites

- Python 3.12+
- Telegram Bot Token (from [@BotFather](https://t.me/botfather))
- Claude Code (Anthropic's Claude Code CLI for content enhancement)
- DeepSeek API Key (for interactive Q&A)
- Optional: Anthropic API Key for automated enhancement mode

### Installation

```bash
# Clone repository
git clone <repository-url>
cd feynman-bot

# Run setup script (installs dependencies and system tools)
./scripts/setup.sh

# Activate virtual environment
source .venv/bin/activate  # Linux/macOS
# or
.venv\Scripts\activate  # Windows
```

### Configuration

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your API keys
nano .env  # or your preferred editor
```

Required environment variables:
```bash
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_telegram_chat_id
DEEPSEEK_API_KEY=your_deepseek_key
# Optional (for automated API mode):
ANTHROPIC_API_KEY=your_anthropic_key
ENHANCEMENT_PROVIDER=api  # Set to 'api' for direct API calls
```

### Running the Pipeline

```bash
# Run all pipeline stages (fetches and processes content)
python pipeline.py

# Run specific stage (for resuming)
python pipeline.py --stage crawl
python pipeline.py --stage parse
python pipeline.py --stage chunk
```

Pipeline stages:
1. **crawl**: Scrape Feynman Lectures website
2. **parse**: Extract sections and LaTeX formulas
3. **chunk**: Split into ~1000-word micro-lessons
4. **enhance**: LLM-powered content transformation (see below)
5. **render**: Convert LaTeX to PNG images

### Enhancement Workflow

The enhancement stage uses a **Claude Code session workflow** to avoid API costs:

**Step 1: Generate prompts**
```bash
python pipeline.py --stage enhance
# Creates data/pending_prompts.jsonl
```

**Step 2: Process with Claude Code**
```
In Claude Code CLI, run:
"Process enhancement prompts in data/pending_prompts.jsonl
and write results to data/enhanced_outputs.jsonl"
```

**Step 3: Import results**
```bash
python pipeline.py --stage enhance --import
# Imports enhanced content into database
```

**Optional: Automated API Mode**
Set `ENHANCEMENT_PROVIDER=api` in `.env` to use direct Anthropic API calls (requires `ANTHROPIC_API_KEY`).

### Starting the Bot

```bash
# Run the bot daemon
python main.py
```

The bot will start sending lessons at scheduled times (default: 07:20, 12:15, 18:30 Asia/Bangkok).

## Bot Commands

| Command | Description |
|---------|-------------|
| `/start` | Welcome message and first lesson |
| `/next` | Fetch next unread lesson |
| `/quiz` | Interactive quiz for current lesson |
| `/explain [topic]` | Deep explanation via AI |
| `/example` | Role-specific practical example |
| `/progress` | Learning statistics and streak |
| `/schedule [times]` | View/update delivery schedule |
| `/role [description]` | Change user role for personalization |
| `/search [keyword]` | Search lessons by keyword |
| `/help` | Show all commands |

## Project Structure

```
feynman-bot/
├── main.py              # Bot entry point
├── pipeline.py          # Content pipeline entry point
├── config.yaml          # Configuration settings
├── requirements.txt     # Python dependencies
├── src/
│   ├── bot/            # Telegram bot application
│   ├── content/        # Content chunking and enhancement
│   ├── crawler/        # Web scraping and parsing
│   ├── knowledge/      # Database layer and models
│   ├── llm/            # LLM provider interface
│   └── renderer/       # LaTeX to PNG rendering
├── scripts/            # Setup and utility scripts
└── data/               # Database and generated content
```

## Configuration

Edit `config.yaml` to customize:

- **Schedule**: Delivery times and timezone
- **Crawler**: Daily limits and retry behavior
- **LLM Settings**: Model selection and parameters
- **User Role**: Personalization for content generation

## Development

Run tests:
```bash
python scripts/test-e2e.py
```

## Deployment (systemd)

```bash
# Install service
sudo cp scripts/feynman-bot.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable feynman-bot
sudo systemctl start feynman-bot
```

## Documentation

- [Project Overview & PDR](docs/project-overview-pdr.md)
- [Codebase Summary](docs/codebase-summary.md)
- [Code Standards](docs/code-standards.md)
- [System Architecture](docs/system-architecture.md)
- [Project Roadmap](docs/project-roadmap.md)

## License

MIT License - see LICENSE file for details.
