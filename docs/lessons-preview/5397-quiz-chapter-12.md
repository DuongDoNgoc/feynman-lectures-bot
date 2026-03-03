---
lesson_id: 5397
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:04.040221+00:00"
content_hash: b01c7a281f65
chapter_number: 12
chapter_title: Chapter 12
section_number: 3
section_title: 12–2Friction
---
# ## Quiz: Các Loại Lực và Ý Nghĩa Định Luật

*Source: Chapter 12 - Chapter 12 (Section 3) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_12.html)*

## Quiz: Các Loại Lực và Ý Nghĩa Định Luật

**Câu 1.** Lực cản $F_{drag} = \frac{1}{2}\rho C_D A v^2$ là:

A. Định luật cơ bản, đúng trong mọi điều kiện
B. Mô hình thực nghiệm, đúng trong regime Reynolds number lớn
C. Xấp xỉ tuyến tính, đúng ở tốc độ thấp
D. Hệ quả trực tiếp từ phương trình Maxwell

**Đáp án: B** — Công thức $cv^2$ là mô hình thực nghiệm cho chế độ inertial drag (Re > 1000). Ở tốc độ thấp (Re < 1), lực cản tỷ lệ với $v$ (Stokes). $C_D$ cũng phụ thuộc vào hình dạng và Reynolds number.

---

**Câu 2.** Tên lửa dẫn đường cần mô hình lực chính xác. Lực nào có thể tính chính xác từ lý thuyết mà không cần dữ liệu thực nghiệm?

A. Lực cản khí động $F_{drag}$
B. Lực đẩy động cơ $F_{thrust}$
C. Lực hấp dẫn $\mathbf{F}_g = m\mathbf{g}$
D. Lực gió ngang

**Đáp án: C** — Lực hấp dẫn $\mathbf{F}_g = m\mathbf{g}$ tính được chính xác từ vị trí (hấp dẫn cơ bản). Lực cản cần wind tunnel data; lực đẩy cần firing test; gió ngang cần đo thực địa.

---

**Câu 3.** Tại sao motor tuyến tính điện từ (linear motor) dễ điều khiển ở độ chính xác micro-mét hơn vít me (ballscrew)?

A. Motor tuyến tính nhanh hơn
B. Lực EM $F=BIL$ tuyến tính với dòng điện, không có backslash hay ma sát tiếp xúc
C. Ballscrew không thể chuyển động chính xác
D. Motor tuyến tính nhẹ hơn

**Đáp án: B** — Lực điện từ $F = BIL$ là cơ bản, tuyến tính hoàn toàn theo $I$. Ballscrew có ma sát phi tuyến, backslash, biến dạng đàn hồi — tất cả là lực thực nghiệm, khó mô hình hóa chính xác.

---

**Câu 4 (Tự luận).** Trong thiết kế hệ thống dẫn đường đạn đạo, kỹ sư quyết định dùng hai phương pháp khác nhau cho hai loại lực: (1) tính toán giải tích cho trọng lực, (2) look-up table từ thực nghiệm cho lực cản. Giải thích cơ sở vật lý của quyết định này.

**Gợi ý đáp án:** Trọng lực $\mathbf{F}_g = -GmM/r^2\hat{r}$ là định luật cơ bản — $G$, $M_E$, $r$ đều biết chính xác, tính giải tích cho kết quả chính xác hơn thực nghiệm. Lực cản phụ thuộc $C_D(v, M, h, \alpha)$ — không có lý thuyết nào cho kết quả chính xác hơn wind tunnel test. Look-up table từ thực nghiệm phản ánh đúng hơn vật lý thực. Kết hợp hai phương pháp tối ưu hóa độ chính xác và chi phí tính toán.

```json
{
  "questions": [
    {"id": "q1", "type": "mcq", "question": "Lực cản F=ρC_D·Av²/2 là:", "options": ["A. Định luật cơ bản mọi điều kiện", "B. Mô hình thực nghiệm cho Re lớn", "C. Xấp xỉ tuyến tính tốc độ thấp", "D. Hệ quả Maxwell"], "answer": "B", "explanation": "Công thức cv² là thực nghiệm cho Re>1000. C_D phụ thuộc hình dạng và Reynolds."},
    {"id": "q2", "type": "mcq", "question": "Lực nào tính chính xác từ lý thuyết không cần thực nghiệm?", "options": ["A. Lực cản khí động", "B. Lực đẩy động cơ", "C. Lực hấp dẫn mg", "D. Lực gió ngang"], "answer": "C", "explanation": "F_g = mg là lực cơ bản, tính được từ hằng số G và khối lượng."},
    {"id": "q3", "type": "mcq", "question": "Tại sao linear motor dễ điều khiển ở micro-mét hơn ballscrew?", "options": ["A. Nhanh hơn", "B. F=BIL tuyến tính, không backslash/ma sát tiếp xúc", "C. Ballscrew không chính xác được", "D. Nhẹ hơn"], "answer": "B", "explanation": "Lực EM là cơ bản, tuyến tính hoàn toàn theo I. Ballscrew có lực thực nghiệm phi tuyến."},
    {"id": "q4", "type": "open", "question": "Tại sao dùng giải tích cho trọng lực nhưng look-up table cho lực cản trong hệ dẫn đường?", "sample_answer": "Trọng lực = định luật cơ bản: G, M_E, r đã biết → giải tích chính xác hơn thực nghiệm. Lực cản C_D(v,M,h,α) phức tạp → wind tunnel cho kết quả thực hơn mọi lý thuyết. Mỗi loại lực dùng phương pháp phù hợp với bản chất của nó."}
  ]
}
```


## Quiz Questions

**Q1:** Lực cản F=ρC_D·Av²/2 là:
- A) A. Định luật cơ bản mọi điều kiện
- B) B. Mô hình thực nghiệm cho Re lớn
- C) C. Xấp xỉ tuyến tính tốc độ thấp
- D) D. Hệ quả Maxwell

**Correct:** B

**Explanation:** Công thức cv² là thực nghiệm cho Re>1000. C_D phụ thuộc hình dạng và Reynolds.

**Q2:** Lực nào tính chính xác từ lý thuyết không cần thực nghiệm?
- A) A. Lực cản khí động
- B) B. Lực đẩy động cơ
- C) C. Lực hấp dẫn mg
- D) D. Lực gió ngang

**Correct:** C

**Explanation:** F_g = mg là lực cơ bản, tính được từ hằng số G và khối lượng.

**Q3:** Tại sao linear motor dễ điều khiển ở micro-mét hơn ballscrew?
- A) A. Nhanh hơn
- B) B. F=BIL tuyến tính, không backslash/ma sát tiếp xúc
- C) C. Ballscrew không chính xác được
- D) D. Nhẹ hơn

**Correct:** B

**Explanation:** Lực EM là cơ bản, tuyến tính hoàn toàn theo I. Ballscrew có lực thực nghiệm phi tuyến.

**Q4:** Tại sao dùng giải tích cho trọng lực nhưng look-up table cho lực cản trong hệ dẫn đường?

**Correct:** N/A


---
*Exported from Feynman Bot*
