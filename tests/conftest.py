"""Pytest configuration and shared fixtures."""
import asyncio
import os
import sys
import tempfile

import pytest

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# ─── Async configuration ───────────────────────────────────────────────────────

@pytest.fixture(scope="session")
def event_loop():
    """Create event loop for async tests."""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


# ─── Config fixtures ────────────────────────────────────────────────────────────

@pytest.fixture
def sample_config():
    """Minimal config for testing."""
    return {
        "database": {"path": ":memory:"},
        "user": {"role": "engineer", "language": "vi-en"},
        "enhancement": {
            "provider": "anthropic",
            "model": "claude-haiku-4-5-20251001",
            "api_key": "test-key",
            "temperature": 0.7,
            "max_tokens": 1024,
            "request_delay": 0,
            "max_retries": 2,
            "retry_base_delay": 0.1,
            "retry_max_delay": 1.0,
        },
        "qa": {
            "provider": "deepseek",
            "model": "deepseek-chat",
            "api_key": "test-key",
            "base_url": "https://api.deepseek.com",
            "temperature": 0.7,
            "max_tokens": 1024,
            "history_limit": 5,
            "max_retries": 2,
            "retry_base_delay": 0.1,
            "retry_max_delay": 1.0,
        },
        "chunker": {
            "target_words": 2000,
            "tolerance": 0.25,
            "min_words": 800,
        },
        "renderer": {
            "dpi": 300,
            "output_dir": tempfile.mkdtemp(),
        },
        "logging": {"level": "DEBUG", "file": None},
    }


@pytest.fixture
def sample_lesson_data():
    """Sample lesson data for testing."""
    return {
        "id": 1,
        "section_id": 1,
        "lesson_type": "concept",
        "sequence": 0,
        "title": "Test Lesson: Energy Conservation",
        "content_enhanced": """
## Energy Conservation

Energy is a fundamental concept in physics. The total energy of an isolated system
remains constant over time. This is known as the law of **conservation of energy**.

The kinetic energy of an object is given by:

$$KE = \\frac{1}{2}mv^2$$

Where $m$ is mass and $v$ is velocity. The potential energy is:

$$PE = mgh$$

### Key Points
- Energy cannot be created or destroyed
- Energy can only be transformed from one form to another
- The total energy before and after any process is the same

**Điểm mấu chốt**: Năng lượng bảo toàn trong hệ kín.
""",
        "enhancement_status": "completed",
        "quiz_json": None,
        "math_images_json": None,
    }


@pytest.fixture
def sample_quiz_json():
    """Sample quiz JSON for testing."""
    import json
    return json.dumps({
        "questions": [
            {
                "id": "q1",
                "type": "mcq",
                "question": "What is the SI unit of energy?",
                "options": ["A. Watt", "B. Joule", "C. Newton", "D. Pascal"],
                "answer": "B",
                "explanation": "Joule (J) is the SI unit of energy."
            },
            {
                "id": "q2",
                "type": "mcq",
                "question": "Which formula represents kinetic energy?",
                "options": ["A. F=ma", "B. KE=1/2mv²", "C. PE=mgh", "D. E=mc²"],
                "answer": "B",
                "explanation": "Kinetic energy = 1/2 × mass × velocity²"
            },
        ]
    })


# ─── Mock fixtures ──────────────────────────────────────────────────────────────

@pytest.fixture
def mock_anthropic_response():
    """Mock Anthropic API response."""
    class MockContent:
        text = "This is a mock enhanced lesson content."

    class MockResponse:
        content = [MockContent()]

    return MockResponse()


@pytest.fixture
def mock_openai_response():
    """Mock OpenAI-compatible API response."""
    class MockMessage:
        content = "This is a mock Q&A response."

    class MockChoice:
        message = MockMessage()

    class MockResponse:
        choices = [MockChoice()]

    return MockResponse()


# ─── Database fixtures ──────────────────────────────────────────────────────────

@pytest.fixture
async def test_db(sample_config):
    """Create in-memory test database."""
    from src.knowledge.db import init_db, get_db

    await init_db(sample_config)

    async with get_db() as conn:
        yield conn
