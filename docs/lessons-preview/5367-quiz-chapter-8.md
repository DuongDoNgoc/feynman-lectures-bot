---
lesson_id: 5367
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:00.536020+00:00"
content_hash: e97a914d5e0c
chapter_number: 8
chapter_title: Chapter 8
section_number: 4
section_title: 8–3Speed as a derivative
---
# ## Quiz: Ký Hiệu Vi Tích Phân và Đạo Hàm

*Source: Chapter 8 - Chapter 8 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_08.html)*

## Quiz: Ký Hiệu Vi Tích Phân và Đạo Hàm

**Câu 1.** Đạo hàm của hàm $s(t) = 5t^3 - 2t + 7$ là:

A. $15t^2 - 2$
B. $15t^2 + 7$
C. $5t^2 - 2$
D. $15t^3 - 2$

---

**Câu 2.** Encoder đọc vị trí tại $t_1 = 1.000\,\text{s}$: $s_1 = 10.000\,\text{mm}$ và $t_2 = 1.001\,\text{s}$: $s_2 = 10.025\,\text{mm}$. Vận tốc trung bình trên khoảng này là:

A. $0.025\,\text{mm/s}$
B. $25\,\text{mm/s}$
C. $250\,\text{mm/s}$
D. $10025\,\text{mm/s}$

---

**Câu 3.** Trong sai phân trung tâm $v(t_k) \approx [s(t_{k+1}) - s(t_{k-1})]/(2T_s)$, sai số xấp xỉ là bậc:

A. $O(T_s)$
B. $O(T_s^2)$
C. $O(T_s^3)$
D. $O(1/T_s)$

---

**Câu 4 (Tự luận).** Hệ thống đo lực cắt trong gia công chính xác dùng cảm biến piezo lấy mẫu ở 10 kHz. Bạn cần tính đạo hàm của tín hiệu lực để phát hiện va chạm đột ngột (jerk trong lực). Hãy đề xuất cách tiếp cận và giải thích tại sao cần lọc tín hiệu trước khi vi phân.

---

```json
{"questions": [
  {"id": "q1", "type": "mcq", "question": "Đạo hàm của hàm s(t) = 5t³ - 2t + 7 là gì?", "options": ["A. 15t² - 2", "B. 15t² + 7", "C. 5t² - 2", "D. 15t³ - 2"], "answer": "A", "explanation": "Áp dụng quy tắc lũy thừa: d(5t³)/dt = 15t², d(-2t)/dt = -2, d(7)/dt = 0. Kết quả: 15t² - 2."},
  {"id": "q2", "type": "mcq", "question": "Encoder đọc s₁=10.000 mm tại t=1.000s và s₂=10.025 mm tại t=1.001s. Vận tốc trung bình là bao nhiêu?", "options": ["A. 0.025 mm/s", "B. 25 mm/s", "C. 250 mm/s", "D. 10025 mm/s"], "answer": "B", "explanation": "v = Δs/Δt = (10.025 - 10.000)/(1.001 - 1.000) = 0.025/0.001 = 25 mm/s."},
  {"id": "q3", "type": "mcq", "question": "Trong sai phân trung tâm, sai số xấp xỉ là bậc nào theo Ts?", "options": ["A. O(Ts)", "B. O(Ts²)", "C. O(Ts³)", "D. O(1/Ts)"], "answer": "B", "explanation": "Khai triển Taylor: s(t±Ts) = s(t) ± Ts·s'(t) + (Ts²/2)·s''(t) ± (Ts³/6)·s'''(t) + ... Sai phân trung tâm triệt tiêu các số hạng bậc lẻ, để lại sai số bắt đầu từ Ts²."},
  {"id": "q4", "type": "open", "question": "Cảm biến lực piezo 10 kHz cần tính đạo hàm để phát hiện va chạm. Đề xuất cách tiếp cận và giải thích vai trò của bộ lọc.", "sample_answer": "Áp dụng lọc thông thấp Butterworth bậc 2 (fc ≈ 500 Hz - 1 kHz, dưới tần số Nyquist 5 kHz) trước khi vi phân để loại nhiễu cao tần. Sau đó dùng sai phân trung tâm với Ts = 0.1 ms. Lý do cần lọc: vi phân khuếch đại nhiễu tỉ lệ với tần số (|H(f)| = 2πf/Ts), nhiễu trắng ở 10 kHz bị khuếch đại mạnh. Ngưỡng phát hiện va chạm đặt ở dF/dt > threshold (ví dụ 3σ của nhiễu nền). Cần đánh đổi: fc thấp → ít nhiễu nhưng trễ phát hiện; fc cao → phát hiện nhanh nhưng nhiều báo động giả."}
]}
```



## Quiz Questions

**Q1:** Đạo hàm của hàm s(t) = 5t³ - 2t + 7 là gì?
- A) A. 15t² - 2
- B) B. 15t² + 7
- C) C. 5t² - 2
- D) D. 15t³ - 2

**Correct:** A

**Explanation:** Áp dụng quy tắc lũy thừa: d(5t³)/dt = 15t², d(-2t)/dt = -2, d(7)/dt = 0. Kết quả: 15t² - 2.

**Q2:** Encoder đọc s₁=10.000 mm tại t=1.000s và s₂=10.025 mm tại t=1.001s. Vận tốc trung bình là bao nhiêu?
- A) A. 0.025 mm/s
- B) B. 25 mm/s
- C) C. 250 mm/s
- D) D. 10025 mm/s

**Correct:** B

**Explanation:** v = Δs/Δt = (10.025 - 10.000)/(1.001 - 1.000) = 0.025/0.001 = 25 mm/s.

**Q3:** Trong sai phân trung tâm, sai số xấp xỉ là bậc nào theo Ts?
- A) A. O(Ts)
- B) B. O(Ts²)
- C) C. O(Ts³)
- D) D. O(1/Ts)

**Correct:** B

**Explanation:** Khai triển Taylor: s(t±Ts) = s(t) ± Ts·s'(t) + (Ts²/2)·s''(t) ± (Ts³/6)·s'''(t) + ... Sai phân trung tâm triệt tiêu các số hạng bậc lẻ, để lại sai số bắt đầu từ Ts².

**Q4:** Cảm biến lực piezo 10 kHz cần tính đạo hàm để phát hiện va chạm. Đề xuất cách tiếp cận và giải thích vai trò của bộ lọc.

**Correct:** N/A


---
*Exported from Feynman Bot*
