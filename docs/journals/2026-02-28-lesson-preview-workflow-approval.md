# Quy trình Xem trước Bài học - Human Approval Gate

**Date**: 2026-02-28 09:25
**Severity**: Medium
**Component**: Content Delivery / Telegram Bot
**Status**: Resolved

## What Happened

Đã implement quy trình xem trước bài học bằng Markdown với bước phê duyệt thủ công trước khi Telegram Bot gửi nội dung. Tạo ra "checkpoint" giữa hệ thống tạo bài học tự động và người dùng cuối.

## The Brutal Truth

Thực tế phũ phàng: AI-generated content thì tiện nhưng không phải lúc nào cũng chính xác. Có những bài dịch sai ngữ pháp, LaTeX bị lỗi, thậm chí nội dung lệch xa với nguồn. Nếu gửi thẳng qua Telegram cho người dùng, mình đang "xả rác" chất lượng cao ra cho họ. Thà delay thêm 5 phút để review còn hơn nhận feedback kiểu "nội dung dở tệ" vào ngày thứ 2.

## Technical Details

**Database Schema:**
```python
# src/knowledge/models.py:59
approval_status: str = "pending"  # pending | approved | rejected
```

**3 New Modules Created:**
1. `preview_db.py` - Query completed lessons bằng approval status
2. `preview_exporter.py` - Export markdown với YAML frontmatter
3. `lesson-preview.py` - CLI tool với 6 commands

**YAML Frontmatter Structure:**
```yaml
---
lesson_id: 1
lesson_type: concept
approval_status: pending
exported_at: "2026-02-28T02:03:03.895762+00:00"
content_hash: 3746c5b3a27d
---
```

**Telegram Bot Gate:**
```python
# Only approved lessons get delivered
if lesson.approval_status != "approved":
    return None
```

## What We Tried

**Approach 1:** Export thẳng tất cả lessons ra markdown → Folder lộn xộn, không biết bài nào đã review.
**Approach 2:** Chỉ add flag `approved` boolean → Không đủ ngữ cảnh, không track rejected lessons.
**Approach 3 (Current):** Three-state status + CLI tool + YAML metadata → Clean, maintainable.

## Root Cause Analysis

Tại sao lại cần cái này?
1. **No Quality Control**: Hệ thống tự động gen nội dung nhưng không có bước QA
2. **One-shot Delivery**: Một khi đã gửi qua Telegram thì không retract được
3. **Blind Trust**: Mình assumed AI luôn gen content tốt - assumption sai lầm

## Lessons Learned

1. **Human-in-the-loop isn't anti-AI** - Nó là essential layer cho production systems
2. **Export with metadata** - YAML frontmatter giúp track source, hash, timestamp
3. **CLI beats GUI for bulk ops** - `approve --all` nhanh hơn click từng checkbox
4. **Three-state > Boolean** - pending/approved/rejected cho tracking đầy đủ

## Next Steps

1. Create CI/CD integration để auto-export khi lesson mới completed
2. Add `auto-approve` flag cho trusted sources (Feynman Lectures chính thức)
3. Metrics: Track rejection rate để improve content generation pipeline
4. Consider thêm "revision" workflow cho rejected lessons

---

**File locations:**
- `/mnt/d/Vibecoding/FeynmanLecture/feynman-bot/scripts/lesson-preview.py`
- `/mnt/d/Vibecoding/FeynmanLecture/feynman-bot/src/content/preview_exporter.py`
- `/mnt/d/Vibecoding/FeynmanLecture/feynman-bot/src/knowledge/preview_db.py`
- `/mnt/d/Vibecoding/FeynmanLecture/feynman-bot/docs/lessons-preview/` (export outputs)
