"""Unit tests for LLM provider module.

Tests:
- Provider initialization
- Retry logic with exponential backoff
- Error handling (retryable vs non-retryable)
- Anthropic and OpenAI backends
"""
import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.llm.provider import (
    LLMError,
    LLMProvider,
    LLMRetryExhaustedError,
    RETRYABLE_ERRORS,
)


class TestLLMProviderInit:
    """Tests for LLMProvider initialization."""

    def test_init_with_defaults(self, sample_config):
        """Test provider initializes with config values."""
        provider = LLMProvider(sample_config["enhancement"])

        assert provider.provider == "anthropic"
        assert provider.model == "claude-haiku-4-5-20251001"
        assert provider.temperature == 0.7
        assert provider.max_tokens == 1024
        assert provider.max_retries == 2
        assert provider.retry_base_delay == 0.1
        assert provider.retry_max_delay == 1.0

    def test_init_with_env_var_api_key(self, sample_config, monkeypatch):
        """Test API key resolution from environment variable."""
        monkeypatch.setenv("TEST_API_KEY", "sk-test-123")
        config = sample_config["enhancement"].copy()
        config["api_key"] = "${TEST_API_KEY}"

        provider = LLMProvider(config)
        assert provider._api_key == "sk-test-123"

    def test_init_with_missing_env_var(self, sample_config):
        """Test missing env var results in empty string."""
        config = sample_config["enhancement"].copy()
        config["api_key"] = "${NONEXISTENT_VAR}"

        provider = LLMProvider(config)
        assert provider._api_key == ""


class TestLLMProviderRetry:
    """Tests for retry logic."""

    @pytest.mark.asyncio
    async def test_success_on_first_attempt(self, sample_config, mock_anthropic_response):
        """Test successful call without retry."""
        provider = LLMProvider(sample_config["enhancement"])

        with patch.object(provider, "_get_anthropic") as mock_get:
            mock_client = MagicMock()
            mock_client.messages.create = AsyncMock(return_value=mock_anthropic_response)
            mock_get.return_value = mock_client

            result = await provider.generate(
                system_prompt="Test system",
                user_prompt="Test user"
            )

            assert result == "This is a mock enhanced lesson content."
            mock_client.messages.create.assert_called_once()

    @pytest.mark.asyncio
    async def test_retry_on_connection_error(self, sample_config, mock_anthropic_response):
        """Test retry on ConnectionError."""
        config = sample_config["enhancement"].copy()
        config["max_retries"] = 3
        config["retry_base_delay"] = 0.01  # Fast for testing
        provider = LLMProvider(config)

        call_count = 0

        async def mock_create(*args, **kwargs):
            nonlocal call_count
            call_count += 1
            if call_count < 3:
                raise ConnectionError("Network error")
            return mock_anthropic_response

        with patch.object(provider, "_get_anthropic") as mock_get:
            mock_client = MagicMock()
            mock_client.messages.create = mock_create
            mock_get.return_value = mock_client

            result = await provider.generate(
                system_prompt="Test",
                user_prompt="Test"
            )

            assert call_count == 3
            assert result == "This is a mock enhanced lesson content."

    @pytest.mark.asyncio
    async def test_retry_exhausted_raises_error(self, sample_config):
        """Test LLMRetryExhaustedError after all retries fail."""
        config = sample_config["enhancement"].copy()
        config["max_retries"] = 2
        config["retry_base_delay"] = 0.01
        provider = LLMProvider(config)

        with patch.object(provider, "_get_anthropic") as mock_get:
            mock_client = MagicMock()
            mock_client.messages.create = AsyncMock(
                side_effect=ConnectionError("Always fails")
            )
            mock_get.return_value = mock_client

            with pytest.raises(LLMRetryExhaustedError) as exc_info:
                await provider.generate(
                    system_prompt="Test",
                    user_prompt="Test"
                )

            assert "All 2 retry attempts failed" in str(exc_info.value)

    @pytest.mark.asyncio
    async def test_non_retryable_error_no_retry(self, sample_config):
        """Test non-retryable errors don't trigger retry."""
        provider = LLMProvider(sample_config["enhancement"])

        with patch.object(provider, "_get_anthropic") as mock_get:
            mock_client = MagicMock()
            mock_client.messages.create = AsyncMock(
                side_effect=ValueError("Invalid parameter")
            )
            mock_get.return_value = mock_client

            with pytest.raises(LLMError) as exc_info:
                await provider.generate(
                    system_prompt="Test",
                    user_prompt="Test"
                )

            # Should only be called once (no retry)
            mock_client.messages.create.assert_called_once()
            assert "LLM API error" in str(exc_info.value)

    @pytest.mark.asyncio
    async def test_exponential_backoff_timing(self, sample_config, mock_anthropic_response):
        """Test backoff delay increases exponentially."""
        config = sample_config["enhancement"].copy()
        config["max_retries"] = 3
        config["retry_base_delay"] = 0.1
        config["retry_max_delay"] = 1.0
        config["request_delay"] = 0  # No post-success delay
        provider = LLMProvider(config)

        retry_delays = []

        # Patch the generate method's internal sleep calls by checking the delay values
        original_sleep = asyncio.sleep

        async def track_sleep(delay):
            # Only track retry delays (which are 0.1, 0.2, etc.)
            # Request delay is 0, so any delay > 0 is a retry delay
            if delay > 0:
                retry_delays.append(delay)
            await original_sleep(0.001)

        call_count = 0

        async def mock_create(*args, **kwargs):
            nonlocal call_count
            call_count += 1
            if call_count < 3:
                raise ConnectionError("Retry needed")
            return mock_anthropic_response

        with patch.object(provider, "_get_anthropic") as mock_get:
            mock_client = MagicMock()
            mock_client.messages.create = mock_create
            mock_get.return_value = mock_client

            with patch("asyncio.sleep", track_sleep):
                await provider.generate(
                    system_prompt="Test",
                    user_prompt="Test"
                )

        # First retry: 0.1s, second retry: 0.2s
        assert len(retry_delays) == 2
        assert retry_delays[0] == 0.1
        assert retry_delays[1] == 0.2


class TestLLMProviderBackends:
    """Tests for different LLM backends."""

    @pytest.mark.asyncio
    async def test_anthropic_backend_called(self, sample_config, mock_anthropic_response):
        """Test Anthropic backend is selected correctly."""
        provider = LLMProvider(sample_config["enhancement"])

        with patch.object(provider, "_get_anthropic") as mock_get:
            mock_client = MagicMock()
            mock_client.messages.create = AsyncMock(return_value=mock_anthropic_response)
            mock_get.return_value = mock_client

            await provider.generate(
                system_prompt="System",
                user_prompt="User"
            )

            mock_client.messages.create.assert_called_once()
            call_kwargs = mock_client.messages.create.call_args[1]
            assert call_kwargs["model"] == "claude-haiku-4-5-20251001"
            assert call_kwargs["system"] == "System"

    @pytest.mark.asyncio
    async def test_openai_backend_called(self, sample_config, mock_openai_response):
        """Test OpenAI-compatible backend is selected correctly."""
        provider = LLMProvider(sample_config["qa"])

        with patch.object(provider, "_get_openai") as mock_get:
            mock_client = MagicMock()
            mock_client.chat.completions.create = AsyncMock(
                return_value=mock_openai_response
            )
            mock_get.return_value = mock_client

            result = await provider.generate(
                system_prompt="System",
                user_prompt="User",
                history=[{"role": "user", "content": "Previous"}]
            )

            assert result == "This is a mock Q&A response."
            mock_client.chat.completions.create.assert_called_once()

    @pytest.mark.asyncio
    async def test_openai_with_history(self, sample_config, mock_openai_response):
        """Test OpenAI backend includes conversation history."""
        provider = LLMProvider(sample_config["qa"])
        history = [
            {"role": "user", "content": "What is energy?"},
            {"role": "assistant", "content": "Energy is..."}
        ]

        with patch.object(provider, "_get_openai") as mock_get:
            mock_client = MagicMock()
            mock_client.chat.completions.create = AsyncMock(
                return_value=mock_openai_response
            )
            mock_get.return_value = mock_client

            await provider.generate(
                system_prompt="System",
                user_prompt="Continue",
                history=history
            )

            call_kwargs = mock_client.chat.completions.create.call_args[1]
            messages = call_kwargs["messages"]

            # Should have: system, history[0], history[1], user
            assert messages[0]["role"] == "system"
            assert len(messages) == 4


class TestLLMErrorTypes:
    """Tests for error type classification."""

    def test_retryable_errors_tuple(self):
        """Test RETRYABLE_ERRORS contains expected types."""
        assert ConnectionError in RETRYABLE_ERRORS
        assert TimeoutError in RETRYABLE_ERRORS
        assert asyncio.TimeoutError in RETRYABLE_ERRORS

    def test_llm_error_with_original(self):
        """Test LLMError preserves original exception."""
        original = ValueError("Original error")
        error = LLMError("Wrapped error", original_error=original)

        assert str(error) == "Wrapped error"
        assert error.original_error == original

    def test_llm_retry_exhausted_inherits_llm_error(self):
        """Test LLMRetryExhaustedError is subclass of LLMError."""
        error = LLMRetryExhaustedError("All retries failed")
        assert isinstance(error, LLMError)
