"""Unit tests for bot handlers module.

Tests:
- Message splitting for Telegram limits
- Segment coalescing
- Error message formatting
- Interleaved segment building
"""
import json
import pytest

from src.bot.handlers import (
    split_message,
    _build_interleaved_segments,
    _coalesce_segments,
    ERROR_MESSAGES,
)


class TestSplitMessage:
    """Tests for message splitting functionality."""

    def test_short_message_unchanged(self):
        """Test short message is not split."""
        text = "This is a short message."
        result = split_message(text)

        assert len(result) == 1
        assert result[0] == text

    def test_exact_limit_message(self):
        """Test message at exact limit is not split."""
        text = "x" * 4096
        result = split_message(text)

        assert len(result) == 1
        assert len(result[0]) == 4096

    def test_long_message_split(self):
        """Test long message is split at paragraph boundaries."""
        # Create message with multiple short paragraphs
        paragraphs = ["Paragraph " + str(i) + " short content." for i in range(20)]
        text = "\n\n".join(paragraphs)

        result = split_message(text, max_len=200)

        assert len(result) > 1

    def test_split_preserves_paragraph_breaks(self):
        """Test split preserves content at paragraph boundaries."""
        para1 = "First paragraph with some content."
        para2 = "Second paragraph with more content."
        text = f"{para1}\n\n{para2}"

        result = split_message(text, max_len=100)

        # Should split at paragraph boundary
        assert para1 in result[0] or para1 in result[1]

    def test_single_long_paragraph_split_by_line(self):
        """Test very long single paragraph splits by line."""
        lines = ["Line " + str(i) * 100 for i in range(50)]
        text = "\n".join(lines)

        result = split_message(text, max_len=500)

        # Should split into multiple parts
        assert len(result) > 1


class TestInterleavedSegments:
    """Tests for interleaved segment building."""

    def test_no_blocks_returns_single_text(self, sample_lesson_data):
        """Test content without formula blocks returns single text segment."""
        content = sample_lesson_data["content_enhanced"]
        result = _build_interleaved_segments(content, blocks=[])

        assert len(result) == 1
        assert result[0]["type"] == "text"
        assert result[0]["content"] == content

    def test_single_image_block(self, sample_lesson_data, tmp_path):
        """Test single image block creates correct segments."""
        # Create test image
        img_path = tmp_path / "test_formula.png"
        img_path.write_bytes(b"fake png data")

        content = "Text before\n$$E=mc^2$$\nText after"
        blocks = [{
            "type": "single",
            "path": str(img_path),
            "start": content.find("$$E=mc^2$$"),
            "end": content.find("$$E=mc^2$$") + len("$$E=mc^2$$")
        }]

        result = _build_interleaved_segments(content, blocks)

        # Should have: text before, image, text after
        assert len(result) == 3
        assert result[0]["type"] == "text"
        assert result[1]["type"] == "image"
        assert result[2]["type"] == "text"

    def test_missing_image_falls_back_to_text(self, sample_lesson_data):
        """Test missing image file falls back to text segment."""
        content = "Text before\n$$E=mc^2$$\nText after"
        blocks = [{
            "type": "single",
            "path": "/nonexistent/image.png",
            "start": content.find("$$E=mc^2$$"),
            "end": content.find("$$E=mc^2$$") + len("$$E=mc^2$$")
        }]

        result = _build_interleaved_segments(content, blocks)

        # Missing image should become text
        assert all(seg["type"] == "text" for seg in result)

    def test_multiple_blocks_ordered(self, sample_lesson_data, tmp_path):
        """Test multiple blocks are processed in order."""
        img1 = tmp_path / "img1.png"
        img2 = tmp_path / "img2.png"
        img1.write_bytes(b"fake")
        img2.write_bytes(b"fake")

        content = "A\n$$F_1$$\nB\n$$F_2$$\nC"
        pos1 = content.find("$$F_1$$")
        pos2 = content.find("$$F_2$$")

        blocks = [
            {"type": "single", "path": str(img2), "start": pos2, "end": pos2 + 7},
            {"type": "single", "path": str(img1), "start": pos1, "end": pos1 + 7},
        ]

        result = _build_interleaved_segments(content, blocks)

        # Should be sorted by position despite input order
        text_segments = [s for s in result if s["type"] == "text"]
        assert "A" in text_segments[0]["content"]


class TestCoalesceSegments:
    """Tests for segment coalescing."""

    def test_empty_segments_returns_empty(self):
        """Test empty input returns empty output."""
        result = _coalesce_segments([])
        assert result == []

    def test_consecutive_text_merged(self):
        """Test consecutive text segments are merged."""
        segments = [
            {"type": "text", "content": "Hello "},
            {"type": "text", "content": "world!"},
        ]

        result = _coalesce_segments(segments)

        assert len(result) == 1
        assert result[0]["content"] == "Hello world!"

    def test_image_breaks_text_merge(self):
        """Test image segment breaks text merging."""
        segments = [
            {"type": "text", "content": "Before"},
            {"type": "image", "path": "/path/to/img.png"},
            {"type": "text", "content": "After"},
        ]

        result = _coalesce_segments(segments)

        assert len(result) == 3
        assert result[0]["type"] == "text"
        assert result[1]["type"] == "image"
        assert result[2]["type"] == "text"

    def test_short_text_merged_with_previous(self):
        """Test short text segments are merged with previous."""
        segments = [
            {"type": "text", "content": "A" * 500},  # Long enough
            {"type": "image", "path": "/img1.png"},  # Break
            {"type": "text", "content": "Short"},     # Too short - will merge with next
            {"type": "text", "content": "B" * 500},  # Long enough
        ]

        result = _coalesce_segments(segments, min_text_len=200)

        # Short segment should be merged with B, resulting in 3 segments
        assert len(result) == 3
        assert result[0]["type"] == "text"
        assert result[1]["type"] == "image"
        assert result[2]["type"] == "text"


class TestErrorMessages:
    """Tests for error message constants."""

    def test_all_messages_are_html_formatted(self):
        """Test all error messages contain HTML tags."""
        for key, msg in ERROR_MESSAGES.items():
            assert "<b>" in msg, f"Missing <b> tag in {key}"
            assert "</b>" in msg, f"Missing </b> tag in {key}"

    def test_all_messages_are_vietnamese(self):
        """Test all error messages are in Vietnamese."""
        vietnamese_markers = ["không", "lỗi", "vui lòng", "thử lại", "chưa", "bài", "quiz", "học"]
        for key, msg in ERROR_MESSAGES.items():
            has_vietnamese = any(marker in msg.lower() for marker in vietnamese_markers)
            assert has_vietnamese, f"Message {key} doesn't appear to be Vietnamese"

    def test_required_error_keys_exist(self):
        """Test all required error keys exist."""
        required_keys = [
            "llm_unavailable",
            "llm_timeout",
            "db_error",
            "no_lesson",
            "no_quiz",
            "generic_error",
        ]
        for key in required_keys:
            assert key in ERROR_MESSAGES, f"Missing error key: {key}"

    def test_messages_reasonable_length(self):
        """Test error messages are not too long for Telegram."""
        for key, msg in ERROR_MESSAGES.items():
            # Remove HTML tags for length check
            import re
            plain_text = re.sub(r"<[^>]+>", "", msg)
            assert len(plain_text) < 200, f"Error message {key} too long: {len(plain_text)}"


class TestQuizJsonParsing:
    """Tests for quiz JSON handling."""

    def test_valid_quiz_json(self, sample_quiz_json):
        """Test parsing valid quiz JSON."""
        quiz = json.loads(sample_quiz_json)

        assert "questions" in quiz
        assert len(quiz["questions"]) == 2
        assert quiz["questions"][0]["type"] == "mcq"
        assert quiz["questions"][0]["answer"] == "B"

    def test_quiz_has_required_fields(self, sample_quiz_json):
        """Test quiz questions have all required fields."""
        quiz = json.loads(sample_quiz_json)

        for q in quiz["questions"]:
            assert "id" in q
            assert "type" in q
            assert "question" in q

            if q["type"] == "mcq":
                assert "options" in q
                assert "answer" in q
                assert "explanation" in q
