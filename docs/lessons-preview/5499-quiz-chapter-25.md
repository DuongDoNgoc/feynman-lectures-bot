---
lesson_id: 5499
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:06.606414+00:00"
content_hash: 05ac09e536d9
chapter_number: 25
chapter_title: Chapter 25
section_number: 2
section_title: 25–1Linear differential equations
---
# ## Bài Kiểm Tra: Tính Tuyến Tính và Nguyên Lý Chồng Chất

*Source: Chapter 25 - Chapter 25 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_25.html)*

## Bài Kiểm Tra: Tính Tuyến Tính và Nguyên Lý Chồng Chất

**Câu 1:** Toán tử $\mathcal{L}(x) = m\frac{d^2x}{dt^2} + \gamma m\frac{dx}{dt} + m\omega_0^2 x$ được gọi là tuyến tính vì:

A) Phương trình chỉ chứa các đạo hàm bậc nhất và bậc hai
B) Toán tử thỏa mãn $\mathcal{L}(ax + by) = a\mathcal{L}(x) + b\mathcal{L}(y)$ với mọi hằng số $a, b$
C) Hệ số của phương trình là hằng số không phụ thuộc vào thời gian
D) Phương trình có nghiệm dạng hàm mũ $e^{i\omega t}$

**Đáp án: B** - Định nghĩa chính xác của tuyến tính là tính chất kép: cộng tính ($\mathcal{L}(x+y) = \mathcal{L}(x) + \mathcal{L}(y)$) và đồng nhất tính ($\mathcal{L}(ax) = a\mathcal{L}(x)$). Phương án C là điều kiện đủ nhưng không phải định nghĩa.

---

**Câu 2:** Nếu $x_1(t)$ và $x_2(t)$ là hai nghiệm của phương trình thuần nhất $\mathcal{L}(x) = 0$, và $x_p(t)$ là nghiệm riêng của $\mathcal{L}(x) = F(t)$, thì nghiệm tổng quát của phương trình đầy đủ là:

A) $x(t) = x_1(t) + x_2(t)$
B) $x(t) = x_p(t)$
C) $x(t) = C_1 x_1(t) + C_2 x_2(t) + x_p(t)$
D) $x(t) = C_1 x_1(t) \cdot C_2 x_2(t) + x_p(t)$

**Đáp án: C** - Nghiệm tổng quát của phương trình tuyến tính không thuần nhất = tổ hợp tuyến tính của các nghiệm thuần nhất (transient) + một nghiệm riêng (steady-state). Đây là nguyên lý superposition.

---

**Câu 3:** Trong thiết kế hệ servo điều khiển độ chính xác cao, một hệ thống chịu đồng thời rung động ở tần số 50 Hz và 200 Hz. Nếu hệ là tuyến tính, kỹ sư có thể:

A) Chỉ phân tích rung động ở tần số cao hơn vì nó ảnh hưởng nhiều hơn
B) Phân tích đáp ứng riêng với từng tần số rồi cộng kết quả lại (superposition)
C) Nhân hai đáp ứng riêng với nhau để có đáp ứng tổng
D) Bỏ qua tần số 50 Hz vì hệ tuyến tính tự lọc

**Đáp án: B** - Nguyên lý chồng chất (superposition) cho phép tách bài toán phức hợp thành các bài toán đơn giản hơn. Đây là lý do tại sao phân tích tần số (frequency domain analysis) và bộ lọc (filter) hoạt động hiệu quả trong hệ tuyến tính.

---

**Câu 4 - Tự luận:** Trong công việc thiết kế hệ thống điều khiển tự động hoặc vũ khí chính xác cao của bạn, hãy nêu một ví dụ cụ thể về hệ thống mà bạn đã từng giả định là tuyến tính để phân tích, nhưng thực tế lại có tính phi tuyến đáng kể. Tính phi tuyến đó biểu hiện như thế nào trong thực nghiệm? Bạn đã xử lý nó bằng cách nào (tuyến tính hóa, bù phi tuyến, hay phương pháp khác)?

*Gợi ý tham khảo: Hiện tượng stiction (ma sát tĩnh) trong hệ truyền động chính xác, vùng dead-band trong van điều khiển, từ trễ (hysteresis) trong cảm biến từ, phi tuyến của encoder ở vùng chuyển tiếp...*

---

```json
{
  "quiz_metadata": {
    "topic": "Tính tuyến tính và nguyên lý chồng chất trong dao động",
    "lesson_ids_related": [5497, 5498],
    "questions": [
      {
        "id": 1,
        "type": "MCQ",
        "correct_answer": "B",
        "concept": "Định nghĩa toán tử tuyến tính"
      },
      {
        "id": 2,
        "type": "MCQ",
        "correct_answer": "C",
        "concept": "Cấu trúc nghiệm tổng quát"
      },
      {
        "id": 3,
        "type": "MCQ",
        "correct_answer": "B",
        "concept": "Ứng dụng superposition trong kỹ thuật"
      },
      {
        "id": 4,
        "type": "open",
        "concept": "Phi tuyến trong hệ thực tế"
      }
    ]
  }
}
```


## Quiz Questions


---
*Exported from Feynman Bot*
