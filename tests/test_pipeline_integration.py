"""Integration tests for pipeline stages.

Tests the flow: parse → chunk → enhance with mock data.
Does not test crawler (requires network) or renderer (requires LaTeX).
"""
import asyncio
import os
import tempfile
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.knowledge.models import Section, Lesson


class TestParserIntegration:
    """Integration tests for parser module."""

    def test_parse_chapter_from_html(self):
        """Test section extraction from sample HTML."""
        from src.crawler.parser import parse_chapter

        html = """
        <html>
        <body>
            <h2>1.1 Introduction</h2>
            <p>Some content about physics.</p>
            <p>More content here.</p>
            <h3>1.1.1 Details</h3>
            <p>Detailed explanation.</p>
            <h2>1.2 Main Topic</h2>
            <p>Main content.</p>
        </body>
        </html>
        """

        sections = parse_chapter(html, {})

        assert len(sections) >= 1
        # Check that sections have required fields
        for s in sections:
            assert s.title
            assert s.content_text is not None

    def test_extract_latex_formulas(self):
        """Test LaTeX formula extraction."""
        from src.crawler.parser import extract_latex

        html = """
        <p>The energy is $$E = mc^2$$.</p>
        <p>Force is defined as \\(F = ma\\).</p>
        <script type="math/tex">a^2 + b^2 = c^2</script>
        """

        result = extract_latex(html)

        # extract_latex returns a dict with 'all' key containing all formulas
        assert "all" in result
        assert len(result["all"]) >= 2

    def test_parser_handles_empty_html(self):
        """Test parser handles empty HTML gracefully."""
        from src.crawler.parser import parse_chapter

        sections = parse_chapter("", {})
        assert sections == []

        sections = parse_chapter("<html><body></body></html>", {})
        assert sections == []


class TestChunkerIntegration:
    """Integration tests for chunker module."""

    @pytest.fixture
    def sample_sections(self):
        """Create sample sections for chunking."""
        return [
            Section(
                id=1,
                chapter_id=1,
                number=1,
                title="Introduction to Energy",
                content_text="Energy is fundamental. " * 200,  # ~800 words
                latex_formulas=["E = mc^2", "KE = 1/2 mv^2"],
            ),
            Section(
                id=2,
                chapter_id=1,
                number=2,
                title="Conservation Laws",
                content_text="Conservation is important. " * 200,
                latex_formulas=["dE/dt = 0"],
            ),
            Section(
                id=3,
                chapter_id=1,
                number=3,
                title="Applications",
                content_text="Real world applications. " * 200,
                latex_formulas=[],
            ),
        ]

    def test_chunk_sections_basic(self, sample_sections, sample_config):
        """Test basic chunking produces lessons."""
        from src.content.chunker import chunk_sections

        chunks = chunk_sections(
            sample_sections,
            target=sample_config["chunker"]["target_words"],
            tolerance=sample_config["chunker"]["tolerance"],
            min_words=sample_config["chunker"]["min_words"],
        )

        assert len(chunks) > 0
        for chunk in chunks:
            assert chunk.word_count >= sample_config["chunker"]["min_words"]
            assert chunk.text

    def test_chunk_preserves_formulas(self, sample_sections, sample_config):
        """Test chunking preserves LaTeX formulas."""
        from src.content.chunker import chunk_sections

        chunks = chunk_sections(
            sample_sections,
            target=2000,
            tolerance=0.25,
            min_words=500,
        )

        # At least one chunk should have formulas
        has_formulas = any(len(c.formulas) > 0 for c in chunks)
        assert has_formulas

    def test_chunk_has_required_fields(self, sample_sections, sample_config):
        """Test chunks have required fields."""
        from src.content.chunker import chunk_sections

        chunks = chunk_sections(
            sample_sections,
            target=2000,
            tolerance=0.25,
            min_words=500,
        )

        for chunk in chunks:
            # Chunk should have these fields
            assert chunk.text
            assert chunk.word_count > 0
            assert chunk.section_ids  # Should reference source sections


class TestEnhancerIntegration:
    """Integration tests for enhancer module."""

    def test_extract_title_from_markdown(self):
        """Test title extraction from markdown content."""
        from src.content.enhancer import _extract_title

        content = "## Energy Conservation\n\nContent here."
        title = _extract_title(content)
        assert title == "Energy Conservation"

    def test_extract_title_from_first_line(self):
        """Test title extraction when no heading exists."""
        from src.content.enhancer import _extract_title

        content = "This is the first line.\n\nMore content."
        title = _extract_title(content)
        assert title == "This is the first line."

    def test_normalize_content_fixes_heading_artifacts(self):
        """Test normalization fixes common LLM heading issues."""
        from src.content.enhancer import _normalize_content

        # Haiku sometimes outputs '# ## Title' instead of '## Title'
        content = "# ## Energy Conservation\n\nContent."
        normalized = _normalize_content(content)

        assert normalized.startswith("## Energy Conservation")

    def test_extract_quiz_json(self):
        """Test quiz JSON extraction from content."""
        from src.content.enhancer import _extract_quiz_json

        content = """
        ## Quiz: Energy

        Some intro text.

        ```json
        {
          "questions": [
            {"id": "q1", "type": "mcq", "question": "Test?", "answer": "A"}
          ]
        }
        ```

        More text.
        """

        quiz_json = _extract_quiz_json(content)
        assert quiz_json is not None

        import json
        quiz = json.loads(quiz_json)
        assert len(quiz["questions"]) == 1

    def test_format_formulas_for_prompt(self):
        """Test formula formatting for LLM prompts."""
        from src.content.enhancer import _format_formulas

        formulas = ["E = mc^2", "F = ma", "a^2 + b^2 = c^2"]
        result = _format_formulas(formulas)

        assert "$E = mc^2$" in result
        assert "$F = ma$" in result
        assert len(result.split("\n")) == 3

    def test_format_empty_formulas(self):
        """Test formatting when no formulas exist."""
        from src.content.enhancer import _format_formulas

        result = _format_formulas([])
        assert "không có công thức" in result


class TestDatabaseIntegration:
    """Integration tests for database operations."""

    @pytest.mark.skip(reason="Requires isolated db fixture - use test-e2e.py for full DB tests")
    @pytest.mark.asyncio
    async def test_init_db_creates_tables(self, sample_config):
        """Test database initialization creates all tables."""
        pass

    @pytest.mark.skip(reason="Requires isolated db fixture - use test-e2e.py for full DB tests")
    @pytest.mark.asyncio
    async def test_insert_and_retrieve_lesson(self, sample_config, sample_lesson_data):
        """Test lesson insert and retrieval roundtrip."""
        pass

    @pytest.mark.skip(reason="Requires isolated db fixture - use test-e2e.py for full DB tests")
    @pytest.mark.asyncio
    async def test_conversation_history(self, sample_config):
        """Test conversation history storage and retrieval."""
        pass


class TestEndToEndPipeline:
    """End-to-end pipeline tests with mocked LLM."""

    @pytest.mark.asyncio
    async def test_parse_chunk_flow(self, sample_config):
        """Test parse → chunk flow without external dependencies."""
        from src.crawler.parser import parse_chapter
        from src.content.chunker import chunk_sections

        # Sample HTML simulating crawled content
        html = """
        <html><body>
        <h2>Chapter 1: Atoms</h2>
        <p>Atoms are the basic units of matter. """ + ("word " * 300) + """</p>
        <h3>1.1 Atomic Structure</h3>
        <p>Atoms consist of protons, neutrons, and electrons. """ + ("word " * 300) + """</p>
        <script type="math/tex">E = mc^2</script>
        <p>Energy and mass are related. """ + ("word " * 300) + """</p>
        </body></html>
        """

        # Parse
        sections = parse_chapter(html, {})
        assert len(sections) >= 1

        # Chunk
        chunks = chunk_sections(
            sections,
            target=sample_config["chunker"]["target_words"],
            tolerance=sample_config["chunker"]["tolerance"],
            min_words=sample_config["chunker"]["min_words"],
        )
        assert len(chunks) >= 1

        # Verify chunk properties
        for chunk in chunks:
            assert chunk.word_count >= sample_config["chunker"]["min_words"]
            assert chunk.text
            assert chunk.section_ids  # Should reference source sections
