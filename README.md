# Feynman Bot

Automated Telegram-based physics learning system delivering personalized micro-lessons from Richard Feynman's "Lectures on Physics."

## Features

- **Automated Content Pipeline**: 5-stage offline batch processing (crawl, parse, chunk, enhance, render)
- **Smart Lesson Delivery**: 3 daily lessons at configurable times (concept, deep_dive, quiz)
- **AI-Powered Enhancement**: LLM-transformation of raw physics content into engaging lessons
- **Interactive Q&A**: Real-time AI assistance with conversation history
- **Progress Tracking**: Streak monitoring and completion statistics
- **Vietnamese Language**: Localized content with English physics terminology
- **LaTeX Rendering**: Automatic formula-to-image conversion

## Quick Start

### Prerequisites

- Python 3.12+
- Telegram Bot Token (from [@BotFather](https://t.me/botfather))
- Anthropic API Key (for content enhancement)
- DeepSeek API Key (for interactive Q&A)

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
ANTHROPIC_API_KEY=your_anthropic_key
DEEPSEEK_API_KEY=your_deepseek_key
```

### Running the Pipeline

```bash
# Run all pipeline stages (fetches and processes content)
python pipeline.py

# Run specific stage (for resuming)
python pipeline.py --stage crawl
python pipeline.py --stage enhance
```

Pipeline stages:
1. **crawl**: Scrape Feynman Lectures website
2. **parse**: Extract sections and LaTeX formulas
3. **chunk**: Split into ~1000-word micro-lessons
4. **enhance**: LLM-powered content transformation
5. **render**: Convert LaTeX to PNG images

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
