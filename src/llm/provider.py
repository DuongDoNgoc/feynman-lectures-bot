"""Unified LLM client supporting Anthropic API and OpenAI-compatible endpoints (DeepSeek, etc.).

Enhancement (offline pipeline): uses Anthropic SDK → claude-haiku-4-5
Interactive Q&A (real-time bot): uses OpenAI-compat SDK → deepseek-chat

Features:
- Exponential backoff retry on transient failures
- Configurable retry attempts and delays
- Graceful error handling with specific error types
"""
import asyncio
import logging
import os
from typing import Optional

log = logging.getLogger(__name__)

# Error types that should trigger retry (transient/network errors)
RETRYABLE_ERRORS = (
    ConnectionError,
    TimeoutError,
    asyncio.TimeoutError,
)


class LLMError(Exception):
    """Base exception for LLM operations."""
    def __init__(self, message: str, original_error: Optional[Exception] = None):
        super().__init__(message)
        self.original_error = original_error


class LLMRetryExhaustedError(LLMError):
    """Raised when all retry attempts have failed."""
    pass


class LLMProvider:
    """Async LLM client. Selects backend from config['provider']."""

    def __init__(self, cfg: dict):
        """
        cfg keys: provider, model, api_key, base_url (optional),
                  temperature, max_tokens, request_delay,
                  max_retries, retry_base_delay, retry_max_delay
        """
        self.provider: str = cfg["provider"]          # "anthropic" | "deepseek" | "openai"
        self.model: str = cfg["model"]
        self.temperature: float = cfg.get("temperature", 0.7)
        self.max_tokens: int = cfg.get("max_tokens", 2048)
        self.request_delay: float = cfg.get("request_delay", 1.0)

        # Retry configuration
        self.max_retries: int = cfg.get("max_retries", 3)
        self.retry_base_delay: float = cfg.get("retry_base_delay", 2.0)
        self.retry_max_delay: float = cfg.get("retry_max_delay", 30.0)

        api_key = cfg.get("api_key", "")
        # Resolve remaining ${VAR} placeholders (in case utils.load_config missed them)
        if api_key.startswith("${"):
            env_name = api_key.strip("${}")
            api_key = os.environ.get(env_name, "")

        self._api_key = api_key
        self._base_url: Optional[str] = cfg.get("base_url")

        # Lazy-init SDK clients
        self._anthropic_client = None
        self._openai_client = None

    # ─── Public API ─────────────────────────────────────────────────────────

    async def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        history: Optional[list[dict]] = None,
    ) -> str:
        """Generate a response with retry logic. Returns text string.

        Raises:
            LLMRetryExhaustedError: When all retry attempts fail
            LLMError: For non-retryable errors
        """
        last_error: Optional[Exception] = None

        for attempt in range(1, self.max_retries + 1):
            try:
                if self.provider == "anthropic":
                    return await self._anthropic_generate(system_prompt, user_prompt, history)
                else:
                    return await self._openai_generate(system_prompt, user_prompt, history)
            except RETRYABLE_ERRORS as e:
                last_error = e
                if attempt < self.max_retries:
                    delay = min(self.retry_base_delay * (2 ** (attempt - 1)), self.retry_max_delay)
                    log.warning(
                        "LLM API attempt %d/%d failed (%s): %s. Retrying in %.1fs...",
                        attempt, self.max_retries, self.provider, e, delay
                    )
                    await asyncio.sleep(delay)
                else:
                    log.error(
                        "LLM API all %d attempts failed (%s): %s",
                        self.max_retries, self.provider, e
                    )
            except Exception as e:
                # Non-retryable error (auth, rate limit, etc.)
                log.error("LLM API non-retryable error (%s): %s", self.provider, e)
                raise LLMError(f"LLM API error: {e}", original_error=e) from e

        raise LLMRetryExhaustedError(
            f"All {self.max_retries} retry attempts failed for {self.provider}",
            original_error=last_error
        )

    # ─── Anthropic backend ───────────────────────────────────────────────────

    def _get_anthropic(self):
        if self._anthropic_client is None:
            try:
                import anthropic
            except ImportError:
                raise RuntimeError("Install 'anthropic' package: pip install anthropic")
            self._anthropic_client = anthropic.AsyncAnthropic(api_key=self._api_key)
        return self._anthropic_client

    async def _anthropic_generate(
        self, system_prompt: str, user_prompt: str, history: Optional[list[dict]]
    ) -> str:
        client = self._get_anthropic()
        messages = _build_messages(user_prompt, history)
        response = await client.messages.create(
            model=self.model,
            system=system_prompt,
            messages=messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        )
        await asyncio.sleep(self.request_delay)
        return response.content[0].text

    # ─── OpenAI-compatible backend (DeepSeek, OpenAI, etc.) ──────────────────

    def _get_openai(self):
        if self._openai_client is None:
            try:
                from openai import AsyncOpenAI
            except ImportError:
                raise RuntimeError("Install 'openai' package: pip install openai")
            kwargs = {"api_key": self._api_key}
            if self._base_url:
                kwargs["base_url"] = self._base_url
            self._openai_client = AsyncOpenAI(**kwargs)
        return self._openai_client

    async def _openai_generate(
        self, system_prompt: str, user_prompt: str, history: Optional[list[dict]]
    ) -> str:
        client = self._get_openai()
        messages = [{"role": "system", "content": system_prompt}]
        if history:
            messages.extend(history)
        messages.append({"role": "user", "content": user_prompt})

        response = await client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        )
        await asyncio.sleep(self.request_delay)
        return response.choices[0].message.content


def build_enhancement_provider(config: dict) -> LLMProvider:
    """LLM client for offline content enhancement."""
    return LLMProvider(config["enhancement"])


def build_qa_provider(config: dict) -> LLMProvider:
    """LLM client for real-time interactive Q&A."""
    return LLMProvider(config["qa"])


def _build_messages(user_prompt: str, history: Optional[list[dict]]) -> list[dict]:
    """Assemble messages list for Anthropic (no system in messages array)."""
    messages = []
    if history:
        messages.extend(history)
    messages.append({"role": "user", "content": user_prompt})
    return messages
