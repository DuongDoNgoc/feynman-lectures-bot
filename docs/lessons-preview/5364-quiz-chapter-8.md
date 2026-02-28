---
lesson_id: 5364
lesson_type: quiz
approval_status: pending
exported_at: "2026-02-28T14:08:59.717053+00:00"
content_hash: ea20465be0c9
chapter_number: 8
chapter_title: Chapter 8
section_number: 1
section_title: 8Motion
---
# ## Quiz: Chuyển Động — Mô Tả Vị Trí Theo Thời Gian

*Source: Chapter 8 - Chapter 8 (Section 1) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_08.html)*

## Quiz: Chuyển Động — Mô Tả Vị Trí Theo Thời Gian

**Câu 1.** Một đầu đo CMM di chuyển với hàm vị trí $s(t) = 4t^3 - 6t^2$ (mm, s). Vận tốc tức thời tại $t = 1\,\text{s}$ là bao nhiêu?

A. $6\,\text{mm/s}$
B. $0\,\text{mm/s}$
C. $12\,\text{mm/s}$
D. $-2\,\text{mm/s}$

---

**Câu 2.** Trong phương pháp tích phân số Euler, để tính vị trí tại bước tiếp theo ta dùng công thức nào?

A. $s(t+\epsilon) = s(t) + a(t)\cdot\epsilon$
B. $s(t+\epsilon) = s(t) + v(t)\cdot\epsilon$
C. $s(t+\epsilon) = v(t) + a(t)\cdot\epsilon$
D. $s(t+\epsilon) = s(t) - v(t)\cdot\epsilon$

---

**Câu 3.** Đồ thị $s$-$t$ của một vật có đoạn nằm ngang (song song trục $t$). Điều này có nghĩa là:

A. Gia tốc bằng 0
B. Vận tốc cực đại
C. Vật đứng yên
D. Vật chuyển động đều

---

**Câu 4 (Tự luận).** Trong hệ thống servo CNC của bạn, encoder đọc vị trí mỗi 1 ms. Bạn cần tính vận tốc và gia tốc từ dữ liệu encoder này để đưa vào bộ lọc Kalman. Hãy mô tả phương pháp tính vi phân số (sai phân hữu hạn) bạn sẽ dùng, nêu rõ ưu nhược điểm về độ chính xác và nhiễu đo.

---

```json
{"questions": [
  {"id": "q1", "type": "mcq", "question": "Một đầu đo CMM di chuyển với hàm vị trí s(t) = 4t³ - 6t² (mm, s). Vận tốc tức thời tại t = 1 s là bao nhiêu?", "options": ["A. 6 mm/s", "B. 0 mm/s", "C. 12 mm/s", "D. -2 mm/s"], "answer": "B", "explanation": "v(t) = ds/dt = 12t² - 12t. Tại t=1: v = 12 - 12 = 0 mm/s. Đây là điểm cực trị của s(t)."},
  {"id": "q2", "type": "mcq", "question": "Trong phương pháp tích phân số Euler, công thức tính vị trí bước tiếp theo là gì?", "options": ["A. s(t+ε) = s(t) + a(t)·ε", "B. s(t+ε) = s(t) + v(t)·ε", "C. s(t+ε) = v(t) + a(t)·ε", "D. s(t+ε) = s(t) - v(t)·ε"], "answer": "B", "explanation": "Phương pháp Euler thuận: vị trí mới = vị trí cũ + vận tốc × bước thời gian. Vận tốc được cập nhật riêng bằng v(t+ε) = v(t) + a(t)·ε."},
  {"id": "q3", "type": "mcq", "question": "Đồ thị s-t của một vật có đoạn nằm ngang (song song trục t). Điều này có nghĩa là gì?", "options": ["A. Gia tốc bằng 0", "B. Vận tốc cực đại", "C. Vật đứng yên", "D. Vật chuyển động đều"], "answer": "C", "explanation": "Đoạn nằm ngang nghĩa là s không đổi theo t, tức ds/dt = v = 0. Vật đứng yên tại chỗ. (Gia tốc = 0 chỉ đúng khi vật chuyển động đều, không phải đứng yên tổng quát.)"},
  {"id": "q4", "type": "open", "question": "Trong hệ thống servo CNC, encoder đọc vị trí mỗi 1 ms. Bạn cần tính vận tốc và gia tốc từ dữ liệu này cho bộ lọc Kalman. Mô tả phương pháp sai phân hữu hạn và nêu ưu nhược điểm.", "sample_answer": "Vận tốc dùng sai phân trung tâm: v(t) ≈ [s(t+Δt) - s(t-Δt)] / (2Δt), chính xác hơn sai phân thuận/lùi vì sai số bậc O(Δt²). Gia tốc: a(t) ≈ [s(t+Δt) - 2s(t) + s(t-Δt)] / Δt². Ưu điểm: đơn giản, ít tài nguyên tính toán. Nhược điểm: khuếch đại nhiễu bậc cao — với encoder có nhiễu lượng tử hóa 1 LSB, nhiễu vận tốc ~ 1 LSB / Δt = 1000 LSB/s, gia tốc ~ 10⁶ LSB/s². Cần lọc thông thấp trước hoặc dùng bộ lọc Kalman để tách tín hiệu khỏi nhiễu."}
]}
```



## Quiz Questions

**Q1:** Một đầu đo CMM di chuyển với hàm vị trí s(t) = 4t³ - 6t² (mm, s). Vận tốc tức thời tại t = 1 s là bao nhiêu?
- A) A. 6 mm/s
- B) B. 0 mm/s
- C) C. 12 mm/s
- D) D. -2 mm/s

**Correct:** B

**Explanation:** v(t) = ds/dt = 12t² - 12t. Tại t=1: v = 12 - 12 = 0 mm/s. Đây là điểm cực trị của s(t).

**Q2:** Trong phương pháp tích phân số Euler, công thức tính vị trí bước tiếp theo là gì?
- A) A. s(t+ε) = s(t) + a(t)·ε
- B) B. s(t+ε) = s(t) + v(t)·ε
- C) C. s(t+ε) = v(t) + a(t)·ε
- D) D. s(t+ε) = s(t) - v(t)·ε

**Correct:** B

**Explanation:** Phương pháp Euler thuận: vị trí mới = vị trí cũ + vận tốc × bước thời gian. Vận tốc được cập nhật riêng bằng v(t+ε) = v(t) + a(t)·ε.

**Q3:** Đồ thị s-t của một vật có đoạn nằm ngang (song song trục t). Điều này có nghĩa là gì?
- A) A. Gia tốc bằng 0
- B) B. Vận tốc cực đại
- C) C. Vật đứng yên
- D) D. Vật chuyển động đều

**Correct:** C

**Explanation:** Đoạn nằm ngang nghĩa là s không đổi theo t, tức ds/dt = v = 0. Vật đứng yên tại chỗ. (Gia tốc = 0 chỉ đúng khi vật chuyển động đều, không phải đứng yên tổng quát.)

**Q4:** Trong hệ thống servo CNC, encoder đọc vị trí mỗi 1 ms. Bạn cần tính vận tốc và gia tốc từ dữ liệu này cho bộ lọc Kalman. Mô tả phương pháp sai phân hữu hạn và nêu ưu nhược điểm.

**Correct:** N/A


---
*Exported from Feynman Bot*
