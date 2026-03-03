---
lesson_id: 5520
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:07.059309+00:00"
content_hash: af0dae09a0d1
chapter_number: 27
chapter_title: Chapter 27
section_number: 4
section_title: 27–3The focal length of a lens
---
# ## Quiz: Thấu Kính Hai Bề Mặt và Phương Trình Lensmaker

*Source: Chapter 27 - Chapter 27 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_27.html)*

## Quiz: Thấu Kính Hai Bề Mặt và Phương Trình Lensmaker

### Câu 1 (Trắc nghiệm)
Theo phương trình lensmaker, tiêu cự $f$ của thấu kính mỏng với chiết suất thuỷ tinh $n$ và hai bán kính cong $R_1$, $R_2$ được tính bằng:

A. $\frac{1}{f} = (n+1)\left(\frac{1}{R_1} + \frac{1}{R_2}\right)$

B. $\frac{1}{f} = (n-1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right)$

C. $\frac{1}{f} = \frac{n-1}{R_1 \cdot R_2}$

D. $\frac{1}{f} = (n-1)\left(\frac{1}{R_1} + \frac{1}{R_2}\right)$

**Đáp án: B**
*Giải thích:* Đây là phương trình lensmaker chuẩn cho thấu kính mỏng. Nó thu được bằng cách áp dụng tuần tự công thức bề mặt khúc xạ cho hai bề mặt và cộng kết quả lại khi bề dày thấu kính tiệm cận về không.

---

### Câu 2 (Trắc nghiệm)
Khi hai thấu kính mỏng đặt tiếp xúc nhau (ghép sát), tiêu cự tổng hợp $f$ liên hệ với tiêu cự hai thấu kính thành phần $f_1$ và $f_2$ như thế nào?

A. $f = f_1 + f_2$

B. $f = f_1 \cdot f_2 / (f_1 + f_2)$

C. $\frac{1}{f} = \frac{1}{f_1} + \frac{1}{f_2}$

D. $\frac{1}{f} = \frac{1}{f_1} - \frac{1}{f_2}$

**Đáp án: C**
*Giải thích:* Khi áp dụng công thức khúc xạ tuần tự qua hai thấu kính mỏng ghép sát, optical power (công suất quang học) $P = 1/f$ cộng trực tiếp: $P_{tổng} = P_1 + P_2$, dẫn đến $1/f = 1/f_1 + 1/f_2$.

---

### Câu 3 (Trắc nghiệm)
Trong hệ quang học nhiều bề mặt, kỹ sư xác định vị trí ảnh cuối cùng bằng cách:

A. Giải đồng thời phương trình cho tất cả các bề mặt cùng lúc

B. Áp dụng công thức khúc xạ tuần tự từ bề mặt đầu đến cuối, mỗi ảnh trung gian là vật cho bề mặt tiếp theo

C. Cộng tất cả bán kính cong của các bề mặt rồi dùng một công thức duy nhất

D. Tính trung bình tiêu cự của tất cả các bề mặt

**Đáp án: B**
*Giải thích:* Đây là nguyên tắc cơ bản của ray tracing: mỗi ảnh trung gian $O'$ trở thành vật cho bề mặt tiếp theo. Phương pháp này hiệu quả và chính xác, đặc biệt khi kết hợp với máy tính.

---

### Câu 4 (Tự luận)
**Câu hỏi mở:** Trong thiết kế một hệ autofocus laser cho máy CNC chính xác micromet, bạn cần xác định tiêu cự của objective lens sao cho điểm hội tụ nằm đúng tại bề mặt phôi gia công. Hãy mô tả quy trình bạn sẽ sử dụng để:
(a) Tính toán tiêu cự cần thiết dựa trên thông số hình học của hệ thống
(b) Chọn hoặc thiết kế thấu kính phù hợp từ lensmaker's equation
(c) Kiểm tra tính hợp lệ của xấp xỉ paraxial trong thiết kế của bạn

**Gợi ý trả lời mẫu:** (a) Dựa trên khoảng cách làm việc (working distance) cần thiết và khoảng cách từ nguồn laser đến thấu kính, dùng $1/s + 1/s' = 1/f$ để tính $f$; (b) Chọn vật liệu thuỷ tinh (ví dụ BK7 có $n=1.515$), sau đó từ $1/f = (n-1)(1/R_1 - 1/R_2)$ chọn $R_1, R_2$ phù hợp — ví dụ thấu kính plano-convex đơn giản cho ứng dụng không yêu cầu quá cao; (c) Kiểm tra $h/f$ của tia biên: nếu $< 0.1$ thì paraxial tốt, nếu lớn hơn cần xét spherical aberration và cân nhắc dùng doublet hoặc aspheric lens.

```json
{
  "questions": [
    {"id": "q1", "type": "mcq", "question": "Phương trình lensmaker tính tiêu cự f của thấu kính mỏng chiết suất n, bán kính R1 và R2 là:", "options": ["A. 1/f = (n+1)(1/R1 + 1/R2)", "B. 1/f = (n-1)(1/R1 - 1/R2)", "C. 1/f = (n-1)/(R1*R2)", "D. 1/f = (n-1)(1/R1 + 1/R2)"], "answer": "B", "explanation": "Phương trình lensmaker chuẩn, thu được từ áp dụng tuần tự công thức bề mặt khúc xạ."},
    {"id": "q2", "type": "mcq", "question": "Hai thấu kính mỏng tiêu cự f1 và f2 đặt tiếp xúc nhau. Tiêu cự tổng hợp f tính bằng:", "options": ["A. f = f1 + f2", "B. f = f1*f2/(f1+f2)", "C. 1/f = 1/f1 + 1/f2", "D. 1/f = 1/f1 - 1/f2"], "answer": "C", "explanation": "Optical power cộng trực tiếp khi thấu kính tiếp xúc: P_total = P1 + P2."},
    {"id": "q3", "type": "mcq", "question": "Để xác định vị trí ảnh qua hệ quang học nhiều bề mặt, kỹ sư dùng phương pháp nào?", "options": ["A. Giải đồng thời cho tất cả bề mặt", "B. Áp dụng tuần tự: ảnh của bề mặt trước là vật của bề mặt sau", "C. Cộng tất cả bán kính cong rồi dùng một công thức", "D. Tính trung bình tiêu cự các bề mặt"], "answer": "B", "explanation": "Ray tracing tuần tự: mỗi ảnh trung gian trở thành vật cho bề mặt tiếp theo."},
    {"id": "q4", "type": "open", "question": "Trong thiết kế hệ autofocus laser cho máy CNC chính xác micromet, mô tả quy trình: (a) tính tiêu cự cần thiết, (b) thiết kế thấu kính từ lensmaker equation, (c) kiểm tra xấp xỉ paraxial.", "sample_answer": "(a) Dùng 1/s + 1/s' = 1/f với thông số hình học của hệ; (b) Chọn vật liệu (BK7 n=1.515), dùng lensmaker equation chọn R1, R2; (c) Kiểm tra h/f < 0.1 cho paraxial hợp lệ, nếu không cần doublet hoặc aspheric lens."}
  ]
}
```


## Quiz Questions

**Q1:** Phương trình lensmaker tính tiêu cự f của thấu kính mỏng chiết suất n, bán kính R1 và R2 là:
- A) A. 1/f = (n+1)(1/R1 + 1/R2)
- B) B. 1/f = (n-1)(1/R1 - 1/R2)
- C) C. 1/f = (n-1)/(R1*R2)
- D) D. 1/f = (n-1)(1/R1 + 1/R2)

**Correct:** B

**Explanation:** Phương trình lensmaker chuẩn, thu được từ áp dụng tuần tự công thức bề mặt khúc xạ.

**Q2:** Hai thấu kính mỏng tiêu cự f1 và f2 đặt tiếp xúc nhau. Tiêu cự tổng hợp f tính bằng:
- A) A. f = f1 + f2
- B) B. f = f1*f2/(f1+f2)
- C) C. 1/f = 1/f1 + 1/f2
- D) D. 1/f = 1/f1 - 1/f2

**Correct:** C

**Explanation:** Optical power cộng trực tiếp khi thấu kính tiếp xúc: P_total = P1 + P2.

**Q3:** Để xác định vị trí ảnh qua hệ quang học nhiều bề mặt, kỹ sư dùng phương pháp nào?
- A) A. Giải đồng thời cho tất cả bề mặt
- B) B. Áp dụng tuần tự: ảnh của bề mặt trước là vật của bề mặt sau
- C) C. Cộng tất cả bán kính cong rồi dùng một công thức
- D) D. Tính trung bình tiêu cự các bề mặt

**Correct:** B

**Explanation:** Ray tracing tuần tự: mỗi ảnh trung gian trở thành vật cho bề mặt tiếp theo.

**Q4:** Trong thiết kế hệ autofocus laser cho máy CNC chính xác micromet, mô tả quy trình: (a) tính tiêu cự cần thiết, (b) thiết kế thấu kính từ lensmaker equation, (c) kiểm tra xấp xỉ paraxial.

**Correct:** N/A


---
*Exported from Feynman Bot*
