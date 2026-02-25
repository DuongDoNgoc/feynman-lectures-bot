"""Unified LLM client supporting Anthropic API and OpenAI-compatible endpoints (DeepSeek, etc.).

Enhancement (offline pipeline): uses Anthropic SDK → claude-haiku-4-5
Interactive Q&A (real-time bot): uses OpenAI-compat SDK → deepseek-chat
"""
import asyncio
import logging
import os
from typing import Optional

log = logging.getLogger(__name__)


class LLMProvider:
    """Async LLM client. Selects backend from config['provider']."""

    def __init__(self, cfg: dict):
        """
        cfg keys: provider, model, api_key, base_url (optional),
                  temperature, max_tokens, request_delay
        """
        self.provider: str = cfg["provider"]          # "anthropic" | "deepseek" | "openai"
        self.model: str = cfg["model"]
        self.temperature: float = cfg.get("temperature", 0.7)
        self.max_tokens: int = cfg.get("max_tokens", 2048)
        self.request_delay: float = cfg.get("request_delay", 1.0)

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
        """Generate a response. Returns text string."""
        if self.provider == "anthropic":
            return await self._anthropic_generate(system_prompt, user_prompt, history)
        else:
            return await self._openai_generate(system_prompt, user_prompt, history)

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
