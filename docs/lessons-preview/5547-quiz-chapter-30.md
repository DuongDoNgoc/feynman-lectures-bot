---
lesson_id: 5547
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:07.652470+00:00"
content_hash: 151ac6ad41b6
chapter_number: 30
chapter_title: Chapter 30
section_number: 4
section_title: 30–3Resolving power of a grating
---
# ## Quiz: Năng Lực Phân Giải Của Cách Tử Nhiễu Xạ

*Source: Chapter 30 - Chapter 30 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_30.html)*

## Quiz: Năng Lực Phân Giải Của Cách Tử Nhiễu Xạ

Bài kiểm tra này giúp bạn kiểm tra hiểu biết về năng lực phân giải (resolving power) của cách tử nhiễu xạ — một chủ đề cực kỳ quan trọng trong thiết kế hệ thống đo lường quang học độ chính xác cao.

---

**Câu 1.** Tiêu chí Rayleigh (Rayleigh's criterion) để phân giải hai nguồn sáng bước sóng gần nhau qua cách tử phát biểu rằng:

A. Hai cực đại nằm cách nhau ít nhất một bước sóng
B. Cực đại của vân nhiễu xạ này rơi đúng vào cực tiểu đầu tiên của vân kia
C. Hai cực tiểu đầu tiên trùng nhau
D. Cường độ tại điểm giữa bằng không

**Đáp án: B**
*Giải thích:* Tiêu chí Rayleigh định nghĩa giới hạn phân giải là khi cực đại của một vạch phổ rơi trùng vào cực tiểu đầu tiên của vạch phổ kia. Ở điều kiện này, cường độ tổng hợp tại điểm giữa giảm đủ để mắt (hoặc sensor) nhận ra hai đỉnh riêng biệt.

---

**Câu 2.** Năng lực phân giải $\mathcal{R}$ của cách tử nhiễu xạ có $N$ khe ở bậc nhiễu xạ $m$ được xác định bởi công thức nào?

A. $\mathcal{R} = \lambda / \Delta\lambda = N$
B. $\mathcal{R} = \lambda / \Delta\lambda = mN$
C. $\mathcal{R} = m / N$
D. $\mathcal{R} = N / m$

**Đáp án: B**
*Giải thích:* Năng lực phân giải của cách tử bằng $\mathcal{R} = \lambda/\Delta\lambda = mN$, trong đó $m$ là bậc nhiễu xạ và $N$ là tổng số khe. Công thức này cho thấy muốn phân giải tốt hơn thì cần tăng số khe hoặc dùng bậc nhiễu xạ cao hơn.

---

**Câu 3.** Một cách tử có 600 khe/mm, chiều rộng tổng cộng 30 mm, hoạt động ở bậc nhiễu xạ $m = 2$. Năng lực phân giải của cách tử này là bao nhiêu?

A. 600
B. 18,000
C. 36,000
D. 1,200

**Đáp án: C**
*Giải thích:* Tổng số khe $N = 600 \times 30 = 18{,}000$. Năng lực phân giải $\mathcal{R} = mN = 2 \times 18{,}000 = 36{,}000$. Điều này có nghĩa là có thể phân biệt hai bước sóng cách nhau $\Delta\lambda = \lambda / 36{,}000$ — ví dụ ở $\lambda = 600\,\text{nm}$ thì phân giải được $\Delta\lambda \approx 0.017\,\text{nm}$.

---

**Câu 4 (Tự luận).** Là một kỹ sư cơ điện tử thiết kế hệ thống đo lường độ chính xác micro-mét, bạn cần chọn cách tử nhiễu xạ cho một máy quang phổ dùng để kiểm tra chất lượng bề mặt bằng phương pháp phân tích phổ phản xạ. Hãy phân tích: (1) Tại sao năng lực phân giải của cách tử lại quan trọng trong ứng dụng này? (2) Bạn sẽ ưu tiên tăng $N$ (số khe) hay tăng $m$ (bậc nhiễu xạ) và tại sao? (3) Có những đánh đổi (trade-off) nào cần cân nhắc?

**Gợi ý trả lời mẫu:**
(1) Trong đo lường bề mặt quang học, phổ phản xạ chứa các đỉnh hẹp đặc trưng cho độ nhám, ứng suất bề mặt, hoặc thành phần vật liệu. Nếu cách tử không đủ năng lực phân giải, hai đỉnh gần nhau sẽ bị chập lại thành một đỉnh giả, dẫn đến sai số đo lường.
(2) Trong thực tế thiết kế, tăng $N$ (dùng cách tử rộng hơn hoặc mật độ khe cao hơn) thường an toàn hơn vì duy trì hiệu suất nhiễu xạ cao. Tăng $m$ cho năng lực phân giải tốt hơn nhưng cường độ sáng bậc cao giảm nhanh, và góc nhiễu xạ lớn hơn gây khó khăn cho thiết kế cơ khí.
(3) Trade-off chính: độ phân giải vs. thông lượng ánh sáng (light throughput); góc nhiễu xạ rộng vs. kích thước hệ quang; chi phí chế tạo cách tử mật độ cao vs. hiệu năng.

---

```json
{
  "questions": [
    {"id": "q1", "type": "mcq", "question": "Tiêu chí Rayleigh (Rayleigh's criterion) để phân giải hai nguồn sáng bước sóng gần nhau qua cách tử phát biểu rằng:", "options": ["A. Hai cực đại nằm cách nhau ít nhất một bước sóng", "B. Cực đại của vân nhiễu xạ này rơi đúng vào cực tiểu đầu tiên của vân kia", "C. Hai cực tiểu đầu tiên trùng nhau", "D. Cường độ tại điểm giữa bằng không"], "answer": "B", "explanation": "Tiêu chí Rayleigh định nghĩa giới hạn phân giải là khi cực đại của một vạch phổ rơi trùng vào cực tiểu đầu tiên của vạch phổ kia."},
    {"id": "q2", "type": "mcq", "question": "Năng lực phân giải R của cách tử nhiễu xạ có N khe ở bậc nhiễu xạ m được xác định bởi công thức nào?", "options": ["A. R = λ/Δλ = N", "B. R = λ/Δλ = mN", "C. R = m/N", "D. R = N/m"], "answer": "B", "explanation": "Năng lực phân giải bằng mN — tích của bậc nhiễu xạ và tổng số khe."},
    {"id": "q3", "type": "mcq", "question": "Cách tử 600 khe/mm, rộng 30 mm, bậc m=2. Năng lực phân giải là bao nhiêu?", "options": ["A. 600", "B. 18,000", "C. 36,000", "D. 1,200"], "answer": "C", "explanation": "N = 600×30 = 18,000; R = mN = 2×18,000 = 36,000."},
    {"id": "q4", "type": "open", "question": "Là kỹ sư cơ điện tử thiết kế máy quang phổ đo bề mặt độ chính xác micro-mét, hãy phân tích: tại sao năng lực phân giải cách tử quan trọng, nên tăng N hay m, và có trade-off gì?", "sample_answer": "Năng lực phân giải cao giúp tách các đỉnh phổ hẹp đặc trưng bề mặt; tăng N an toàn hơn vì duy trì hiệu suất; trade-off gồm thông lượng ánh sáng, góc nhiễu xạ, chi phí."}
  ]
}
```


## Quiz Questions

**Q1:** Tiêu chí Rayleigh (Rayleigh's criterion) để phân giải hai nguồn sáng bước sóng gần nhau qua cách tử phát biểu rằng:
- A) A. Hai cực đại nằm cách nhau ít nhất một bước sóng
- B) B. Cực đại của vân nhiễu xạ này rơi đúng vào cực tiểu đầu tiên của vân kia
- C) C. Hai cực tiểu đầu tiên trùng nhau
- D) D. Cường độ tại điểm giữa bằng không

**Correct:** B

**Explanation:** Tiêu chí Rayleigh định nghĩa giới hạn phân giải là khi cực đại của một vạch phổ rơi trùng vào cực tiểu đầu tiên của vạch phổ kia.

**Q2:** Năng lực phân giải R của cách tử nhiễu xạ có N khe ở bậc nhiễu xạ m được xác định bởi công thức nào?
- A) A. R = λ/Δλ = N
- B) B. R = λ/Δλ = mN
- C) C. R = m/N
- D) D. R = N/m

**Correct:** B

**Explanation:** Năng lực phân giải bằng mN — tích của bậc nhiễu xạ và tổng số khe.

**Q3:** Cách tử 600 khe/mm, rộng 30 mm, bậc m=2. Năng lực phân giải là bao nhiêu?
- A) A. 600
- B) B. 18,000
- C) C. 36,000
- D) D. 1,200

**Correct:** C

**Explanation:** N = 600×30 = 18,000; R = mN = 2×18,000 = 36,000.

**Q4:** Là kỹ sư cơ điện tử thiết kế máy quang phổ đo bề mặt độ chính xác micro-mét, hãy phân tích: tại sao năng lực phân giải cách tử quan trọng, nên tăng N hay m, và có trade-off gì?

**Correct:** N/A


---
*Exported from Feynman Bot*
