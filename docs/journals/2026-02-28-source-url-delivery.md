# Source URL Attribution in Lesson Delivery

**Date**: 2026-02-28 17:24
**Severity**: Low
**Component**: `src/knowledge/db.py`, `src/bot/handlers.py`, lesson delivery
**Status**: Implemented

## What Happened

Added source URL attribution to every lesson delivery. When a lesson is sent to the user, after all content segments and images, a final message is appended with "📖 Nguồn: {url}" showing where the lesson comes from. Implemented `get_lesson_source_url()` in db.py that joins through the lesson → section → chapter hierarchy to construct a readable URL. Updated the test-interleaved.py script to include the same source URL delivery step for manual QA.

## The Brutal Truth

This is a small feature, but it matters for credibility. Without source attribution, users have no way to verify the lesson or find the original context. It's the academic equivalent of citing your sources—obvious in retrospect, but easy to forget when rushing to get functionality working.

The implementation is straightforward, but it exposed a potential problem: what if the chapter or section has been deleted? The join query would silently return NULL. We're not handling this case yet; it just silently fails to append a source URL. This needs validation.

## Technical Details

**Database query logic:**
```sql
SELECT chapters.url FROM lessons
JOIN sections ON lessons.section_id = sections.id
JOIN chapters ON sections.chapter_id = chapters.id
WHERE lessons.id = ?
```

The URL hierarchy is:
- Lesson → Section (many lessons per section)
- Section → Chapter (many sections per chapter)
- Chapter → URL (each chapter has a url field)

**Implementation in handlers.py:**
```python
source_url = await db.get_lesson_source_url(lesson.id)
if source_url:
    await context.bot.send_message(
        chat_id=chat_id,
        text=f"📖 Nguồn: {source_url}"
    )
```

**Test coverage:**
Updated scripts/test-interleaved.py to include the same step, so manual QA validates that the source URL appears at the end of lesson delivery.

## What We Tried

1. **Inline source in lesson text**: Considered appending it to the last text segment
   - Problem: breaks markdown parsing, looks cluttered
   - Rejected

2. **Separate message at the end** (final approach)
   - Clean, non-intrusive
   - Telegram still groups it with the lesson
   - Easy to skip if URL is None

## Root Cause Analysis

This isn't a fix for a bug—it's a missing feature that should have been there from the start. The data model already has the URL at the chapter level; we just weren't surfacing it to users. Simple oversight.

## Lessons Learned

1. **Attribution is a feature, not an afterthought**: Users need to know where content comes from. Make it explicit in the UX design, not a "nice to have".

2. **Test manual workflows too**: The test-interleaved.py script is valuable because it simulates the full user flow. It catches missing pieces like source attribution.

3. **Handle NULL cases gracefully**: If chapter is deleted, `get_lesson_source_url()` returns None. The code handles it (no message sent), but we should log this as a warning so admins know data is inconsistent.

## Next Steps

- Add logging to handlers.py if source_url is None (indicates orphaned lesson/section/chapter)
- Consider adding a fallback URL format if chapter.url is missing (e.g., "Lesson {lesson_id}" with at least some identifier)
- Add database integrity check: find lessons whose chapters have been deleted
