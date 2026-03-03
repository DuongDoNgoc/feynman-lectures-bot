---
lesson_id: 5370
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:00.637796+00:00"
content_hash: aac2b3731e67
chapter_number: 9
chapter_title: Chapter 9
section_number: 1
section_title: 9Newton’s Laws of Dynamics
---
# ## Quiz: Các Định Luật Động Lực Học Newton

*Source: Chapter 9 - Chapter 9 (Section 1) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_09.html)*

## Quiz: Các Định Luật Động Lực Học Newton

**Câu 1.** Một servo motor có rotor khối lượng $m = 0.2\,\text{kg}$, bán kính $r = 0.05\,\text{m}$. Lực tiếp tuyến tác dụng lên rotor $F = 10\,\text{N}$. Gia tốc dài của điểm trên vành rotor là:

A. $2\,\text{m/s}^2$
B. $50\,\text{m/s}^2$
C. $100\,\text{m/s}^2$
D. $0.5\,\text{m/s}^2$

---

**Câu 2.** Phương trình $m\ddot{x} + c\dot{x} + kx = 0$ mô tả hệ nào sau đây?

A. Dao động tự do không tắt dần
B. Dao động tắt dần với lực hồi phục đàn hồi
C. Chuyển động thẳng đều
D. Dao động cưỡng bức

---

**Câu 3.** Trong định luật Newton III, khi đạn bay ra khỏi nòng súng, điều nào sau đây ĐÚNG?

A. Lực lên đạn lớn hơn lực giật của súng
B. Xung lực lên đạn bằng xung lực giật của súng về độ lớn
C. Gia tốc đạn bằng gia tốc giật của súng
D. Năng lượng đạn bằng năng lượng giật của súng

---

**Câu 4 (Tự luận).** Trong hệ thống đo lực cắt cho máy phay CNC, đầu đo lực (dynamometer) được mô hình hóa như hệ lò xo-khối lượng-giảm chấn với $k = 5\times10^6\,\text{N/m}$, $m = 0.1\,\text{kg}$, $c = 500\,\text{N·s/m}$. Hãy tính tần số cộng hưởng và giải thích tại sao điều này quan trọng khi chọn tần số lấy mẫu cho bộ thu thập dữ liệu.

---

```json
{"questions": [
  {"id": "q1", "type": "mcq", "question": "Servo motor: m=0.2 kg, r=0.05 m, lực tiếp tuyến F=10 N. Gia tốc dài của điểm trên vành rotor là bao nhiêu?", "options": ["A. 2 m/s²", "B. 50 m/s²", "C. 100 m/s²", "D. 0.5 m/s²"], "answer": "B", "explanation": "F = ma → a = F/m = 10/0.2 = 50 m/s². Bán kính r không ảnh hưởng đến gia tốc dài (đây là chuyển động tịnh tiến của điểm chất). Nếu hỏi gia tốc góc: α = a/r = 50/0.05 = 1000 rad/s²."},
  {"id": "q2", "type": "mcq", "question": "Phương trình mẍ + cẋ + kx = 0 mô tả hệ nào?", "options": ["A. Dao động tự do không tắt dần", "B. Dao động tắt dần với lực hồi phục đàn hồi", "C. Chuyển động thẳng đều", "D. Dao động cưỡng bức"], "answer": "B", "explanation": "Số hạng kx là lực đàn hồi (hồi phục), cẋ là lực tắt dần tỉ lệ vận tốc, mẍ là quán tính. Không có ngoại lực (vế phải = 0) → dao động tự do tắt dần. Nếu vế phải = F(t) thì là cưỡng bức."},
  {"id": "q3", "type": "mcq", "question": "Khi đạn bay ra khỏi nòng súng, điều nào đúng về định luật Newton III?", "options": ["A. Lực lên đạn lớn hơn lực giật của súng", "B. Xung lực lên đạn bằng xung lực giật của súng về độ lớn", "C. Gia tốc đạn bằng gia tốc giật của súng", "D. Năng lượng đạn bằng năng lượng giật của súng"], "answer": "B", "explanation": "Định luật III: lực tác dụng bằng phản lực về độ lớn, do đó xung lực (tích phân lực theo thời gian) cũng bằng nhau. Gia tốc không bằng vì khối lượng khác nhau (a = F/m). Năng lượng không bằng vì E = p²/2m phụ thuộc m."},
  {"id": "q4", "type": "open", "question": "Dynamometer: k=5×10⁶ N/m, m=0.1 kg, c=500 N·s/m. Tính tần số cộng hưởng và ý nghĩa khi chọn tần số lấy mẫu.", "sample_answer": "ωn = √(k/m) = √(5×10⁷) ≈ 7071 rad/s → fn ≈ 1125 Hz. ζ = c/(2√(km)) = 500/(2√(5×10⁵)) ≈ 0.35 (underdamped). Tần số cộng hưởng có đỉnh đáp ứng tại fd = fn√(1-2ζ²) ≈ 1041 Hz. Để thu tín hiệu lực cắt đúng, tần số lấy mẫu cần > 2×1125 Hz (Nyquist) = 2250 Hz, thực tế chọn 5-10 kHz để có biên độ đủ. Nếu lực cắt chứa thành phần gần 1125 Hz (ví dụ rung dao), dynamometer sẽ cộng hưởng và đọc sai — cần bộ lọc thông thấp trước 1 kHz hoặc chọn dynamometer cứng hơn."}
]}
```



## Quiz Questions

**Q1:** Servo motor: m=0.2 kg, r=0.05 m, lực tiếp tuyến F=10 N. Gia tốc dài của điểm trên vành rotor là bao nhiêu?
- A) A. 2 m/s²
- B) B. 50 m/s²
- C) C. 100 m/s²
- D) D. 0.5 m/s²

**Correct:** B

**Explanation:** F = ma → a = F/m = 10/0.2 = 50 m/s². Bán kính r không ảnh hưởng đến gia tốc dài (đây là chuyển động tịnh tiến của điểm chất). Nếu hỏi gia tốc góc: α = a/r = 50/0.05 = 1000 rad/s².

**Q2:** Phương trình mẍ + cẋ + kx = 0 mô tả hệ nào?
- A) A. Dao động tự do không tắt dần
- B) B. Dao động tắt dần với lực hồi phục đàn hồi
- C) C. Chuyển động thẳng đều
- D) D. Dao động cưỡng bức

**Correct:** B

**Explanation:** Số hạng kx là lực đàn hồi (hồi phục), cẋ là lực tắt dần tỉ lệ vận tốc, mẍ là quán tính. Không có ngoại lực (vế phải = 0) → dao động tự do tắt dần. Nếu vế phải = F(t) thì là cưỡng bức.

**Q3:** Khi đạn bay ra khỏi nòng súng, điều nào đúng về định luật Newton III?
- A) A. Lực lên đạn lớn hơn lực giật của súng
- B) B. Xung lực lên đạn bằng xung lực giật của súng về độ lớn
- C) C. Gia tốc đạn bằng gia tốc giật của súng
- D) D. Năng lượng đạn bằng năng lượng giật của súng

**Correct:** B

**Explanation:** Định luật III: lực tác dụng bằng phản lực về độ lớn, do đó xung lực (tích phân lực theo thời gian) cũng bằng nhau. Gia tốc không bằng vì khối lượng khác nhau (a = F/m). Năng lượng không bằng vì E = p²/2m phụ thuộc m.

**Q4:** Dynamometer: k=5×10⁶ N/m, m=0.1 kg, c=500 N·s/m. Tính tần số cộng hưởng và ý nghĩa khi chọn tần số lấy mẫu.

**Correct:** N/A


---
*Exported from Feynman Bot*
