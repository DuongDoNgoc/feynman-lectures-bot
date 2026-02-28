# Feynman Bot - Troubleshooting Guide

**Last Updated**: 2026-02-28

This guide covers common issues, error messages, and recovery procedures for the Feynman Lectures Bot.

---

## Table of Contents

1. [Bot Errors](#bot-errors)
2. [Pipeline Errors](#pipeline-errors)
3. [LLM API Errors](#llm-api-errors)
4. [Database Errors](#database-errors)
5. [Crawler Errors](#crawler-errors)
6. [Renderer Errors](#renderer-errors)
7. [Recovery Procedures](#recovery-procedures)

---

## Bot Errors

### Bot Not Responding

**Symptoms**: Bot doesn't reply to commands or messages.

**Diagnosis**:
```bash
# Check if bot process is running
ps aux | grep python | grep bot

# Check bot logs
tail -100 data/feynman-bot.log | grep -i error
```

**Solutions**:
1. Restart the bot: `python -m src.bot.bot`
2. Check `TELEGRAM_BOT_TOKEN` environment variable
3. Verify network connectivity to Telegram API

---

### "AI tạm thời không khả dụng" Error

**Symptoms**: User sees Vietnamese message about AI being unavailable.

**Cause**: LLM API (Anthropic/DeepSeek) is down or rate-limited.

**Diagnosis**:
```bash
# Check LLM API logs
grep -i "LLM" data/feynman-bot.log | tail -20

# Test Anthropic API
curl -H "x-api-key: $ANTHROPIC_API_KEY" https://api.anthropic.com/v1/messages

# Test DeepSeek API
curl -H "Authorization: Bearer $DEEPSEEK_API_KEY" https://api.deepseek.com/v1/models
```

**Solutions**:
1. Wait 5-10 minutes for rate limit to reset
2. Check API status pages
3. Verify API keys are valid and have credits
4. Check `config.yaml` for correct API endpoints

---

### "AI phản hồi quá lâu" Timeout Error

**Symptoms**: User sees timeout message after asking a question.

**Cause**: LLM response took too long (>30s typically).

**Solutions**:
1. Ask user to shorten their question
2. Increase timeout in config if needed
3. Check network latency to API endpoints

---

## Pipeline Errors

### Enhancement Pipeline Fails

**Symptoms**: `python pipeline.py --stage enhance` fails.

**Diagnosis**:
```bash
# Run with verbose logging
LOGLEVEL=DEBUG python pipeline.py --stage enhance --direct --batch 1

# Check pending lessons count
sqlite3 data/feynman.db "SELECT COUNT(*) FROM lessons WHERE enhancement_status='pending'"
```

**Solutions**:
1. Check `ANTHROPIC_API_KEY` is set
2. Verify API credits available
3. Try smaller batch size: `--batch 5`
4. Check disk space for output files

---

### Parser Fails to Extract Sections

**Symptoms**: Parser produces 0 or few sections.

**Diagnosis**:
```bash
# Check raw HTML exists
sqlite3 data/feynman.db "SELECT COUNT(*) FROM chapters WHERE raw_html IS NOT NULL"

# Run parser with debug
LOGLEVEL=DEBUG python pipeline.py --stage parse
```

**Solutions**:
1. Re-crawl affected chapters
2. Check HTML structure hasn't changed on source website
3. Verify BeautifulSoup is parsing correctly

---

## LLM API Errors

### Rate Limit Exceeded

**Symptoms**: HTTP 429 errors in logs.

**Diagnosis**:
```bash
grep -i "429\|rate limit" data/feynman-bot.log | tail -10
```

**Solutions**:
1. Increase `request_delay` in `config.yaml`
2. Reduce batch size for enhancement
3. Wait for rate limit window to reset (usually 1 minute)
4. Consider upgrading API tier

**Config Changes**:
```yaml
enhancement:
  request_delay: 2.0  # Increase from 1.0
  max_retries: 5      # Increase retry attempts
```

---

### Authentication Failed

**Symptoms**: HTTP 401 errors.

**Diagnosis**:
```bash
# Verify API key format
echo $ANTHROPIC_API_KEY | head -c 10
# Should show: sk-ant-a...

# Test authentication
curl -H "x-api-key: $ANTHROPIC_API_KEY" https://api.anthropic.com/v1/messages
```

**Solutions**:
1. Regenerate API key from provider dashboard
2. Update environment variable or `config.yaml`
3. Check for extra whitespace in key

---

### Model Not Found

**Symptoms**: HTTP 404 with "model not found".

**Solutions**:
1. Update model name in `config.yaml`:
   - Anthropic: `claude-sonnet-4-6` or `claude-haiku-4-5-20251001`
   - DeepSeek: `deepseek-chat` or `deepseek-reasoner`

---

## Database Errors

### Database Locked

**Symptoms**: `database is locked` errors.

**Diagnosis**:
```bash
# Check for other processes using DB
fuser data/feynman.db

# Check DB integrity
sqlite3 data/feynman.db "PRAGMA integrity_check"
```

**Solutions**:
1. Stop all bot/pipeline processes
2. Wait a few seconds for locks to release
3. Restart processes one at a time
4. Consider enabling WAL mode:
   ```bash
   sqlite3 data/feynman.db "PRAGMA journal_mode=WAL"
   ```

---

### Database Corruption

**Symptoms**: Random errors, missing data.

**Recovery**:
```bash
# Backup first
cp data/feynman.db data/feynman.db.backup

# Try to recover
sqlite3 data/feynman.db ".recover" | sqlite3 data/feynman_recovered.db

# If recovery fails, may need to re-initialize
# WARNING: This loses all progress data
python -c "from src.knowledge.db import init_db; import asyncio; asyncio.run(init_db())"
```

---

## Crawler Errors

### Cloudflare Block

**Symptoms**: HTTP 403, circuit breaker trips after 20 failures.

**Diagnosis**:
```bash
grep -i "circuit breaker\|cloudflare" data/feynman-bot.log | tail -5
```

**Solutions**:
1. **Wait 24 hours** - Cloudflare blocks are usually temporary
2. **Manual download**:
   - Download HTML from browser (logged in session)
   - Import to DB: `python scripts/import-chapter.py <volume> <number> <html_file>`
3. **Use VPN** - Different IP may bypass block
4. **Reduce crawl rate**:
   ```yaml
   crawler:
     daily_limit: 10
     request_delay_min: 3.0
     request_delay_max: 6.0
   ```

---

### Crawler Timeout

**Symptoms**: Pages take >60s to load.

**Solutions**:
1. Check network connectivity
2. Increase timeout in `scraper.py` (line 90)
3. Try non-headless mode for debugging:
   ```python
   async with create_browser(headless=False) as (browser, page):
   ```

---

## Renderer Errors

### pdflatex Not Found

**Symptoms**: `FileNotFoundError: pdflatex not found`

**Solutions**:
```bash
# Ubuntu/Debian
sudo apt-get install texlive-latex-base texlive-fonts-recommended

# macOS
brew install --cask mactex

# Verify
which pdflatex
```

---

### xelatex Font Errors

**Symptoms**: `Font ... not found` errors.

**Solutions**:
```bash
# Install DejaVu fonts
sudo apt-get install fonts-dejavu-core fonts-dejavu-extra

# Verify font
fc-list | grep DejaVu
```

---

### Formula Rendering Fails

**Symptoms**: Missing formula images in lessons.

**Diagnosis**:
```bash
# Check renderer logs
grep -i "render\|latex\|formula" data/feynman-bot.log | tail -20

# Check output directory
ls -la data/images/ | head -20
```

**Solutions**:
1. Check LaTeX installation
2. Verify output directory permissions
3. Check for invalid LaTeX syntax in content
4. Renderer falls back gracefully - raw LaTeX shown as text

---

## Recovery Procedures

### Full System Recovery

If multiple components fail:

```bash
# 1. Stop all processes
pkill -f "python.*bot"
pkill -f "python.*pipeline"

# 2. Backup database
cp data/feynman.db data/feynman.db.$(date +%Y%m%d).backup

# 3. Check DB integrity
sqlite3 data/feynman.db "PRAGMA integrity_check"

# 4. Restart services in order
python -m src.bot.bot &

# 5. Verify bot is running
curl "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/getMe"
```

---

### Reset User Progress

If user wants to start over:

```bash
# Clear progress for specific chat_id
sqlite3 data/feynman.db "DELETE FROM user_progress WHERE chat_id = <CHAT_ID>"
sqlite3 data/feynman.db "DELETE FROM conversations WHERE chat_id = <CHAT_ID>"
```

---

### Re-enhance Failed Lessons

If enhancement partially failed:

```bash
# Reset status for failed lessons
sqlite3 data/feynman.db "UPDATE lessons SET enhancement_status='pending' WHERE enhancement_status='failed'"

# Re-run enhancement
python pipeline.py --stage enhance --direct --batch 10
```

---

## Error Codes Reference

| Code | Meaning | Action |
|------|---------|--------|
| `LLM_RETRY_EXHAUSTED` | All retry attempts failed | Wait 5 min, check API status |
| `DB_LOCKED` | Database locked | Stop other processes |
| `CRAWLER_CIRCUIT_BREAKER` | Too many crawl failures | Wait 24h or manual download |
| `RENDERER_LATEX_FAIL` | LaTeX compilation failed | Check LaTeX installation |
| `AUTH_INVALID` | Invalid API credentials | Regenerate API key |

---

## Contact & Support

- **Logs**: `data/feynman-bot.log`
- **Config**: `config.yaml`
- **Database**: `data/feynman.db`

For persistent issues, check logs for specific error patterns and consult the relevant section above.
