---
lesson_id: 5502
lesson_type: quiz
approval_status: pending
exported_at: "2026-03-02T15:10:31.210362+00:00"
content_hash: 7321222f368b
chapter_number: 25
chapter_title: Chapter 25
section_number: 4
section_title: 25–3Oscillations in linear systems
---
# ## Bài Kiểm Tra: Dao Động Tắt Dần và Suy Giảm Hàm Mũ

*Source: Chapter 25 - Chapter 25 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_25.html)*

## Bài Kiểm Tra: Dao Động Tắt Dần và Suy Giảm Hàm Mũ

**Câu 1:** Tại sao ma sát nhớt (tỉ lệ với vận tốc) tạo ra suy giảm hàm mũ, trong khi ma sát Coulomb (hằng số) không tạo ra suy giảm hàm mũ?

A) Vì ma sát nhớt tỉ lệ với vận tốc, nên khi biên độ nhỏ thì lực ma sát cũng nhỏ theo, mỗi chu kỳ biên độ giảm đi cùng một **tỉ lệ phần trăm**
B) Vì ma sát Coulomb không phụ thuộc thời gian
C) Vì ma sát nhớt tạo ra lực lớn hơn ma sát Coulomb
D) Vì ma sát nhớt luôn hướng về vị trí cân bằng

**Đáp án: A** - Cốt lõi của vấn đề: với ma sát nhớt, khi biên độ giảm đôi thì lực ma sát cũng giảm đôi (vì vận tốc đỉnh $\propto A$). Tất cả các lực đều tỉ lệ với $A$, nên tỉ lệ suy giảm mỗi chu kỳ là hằng số, dẫn đến $A(t) = A_0 e^{-\gamma t/2}$.

---

**Câu 2:** Hệ số phẩm chất $Q = \omega_0/\gamma$ của một cảm biến dao động. Hệ nào sau đây phù hợp nhất để đo gia tốc (accelerometer) cần đáp ứng nhanh, không ringing?

A) $Q = 100,000$ (như thạch anh oscillator)
B) $Q = 0.5$ (quá cản)
C) $Q = 0.707$ (cản tới hạn Butterworth, $\zeta \approx 0.707$)
D) $Q = 10$ (cản nhỏ)

**Đáp án: C** - Accelerometer cần đáp ứng phẳng nhất trong băng thông ($\zeta = 0.707$ cho flat frequency response), không quá slow như overdamped ($Q = 0.5$), không ringing như underdamped ($Q = 10$ hay cao hơn). $Q \approx 0.707$ là giá trị tối ưu cho đo lường.

---

**Câu 3:** Một hệ dao động có tần số tự nhiên $\omega_0 = 1000$ rad/s và hệ số cản $\gamma = 10$ rad/s. Tần số dao động thực khi có cản là:

A) $\omega_1 = \sqrt{1000^2 - 10^2/4} \approx 999.975$ rad/s - gần bằng $\omega_0$
B) $\omega_1 = 1000 - 10 = 990$ rad/s
C) $\omega_1 = 1000 \times 10 = 10000$ rad/s
D) $\omega_1 = 0$ rad/s vì hệ bị cản

**Đáp án: A** - $\omega_1 = \sqrt{\omega_0^2 - \gamma^2/4} = \sqrt{10^6 - 25} \approx 999.9875$ rad/s. Với $Q = \omega_0/\gamma = 100 \gg 1$, cản nhỏ làm thay đổi tần số rất ít. Đây là lý do tại sao cộng hưởng điện từ và cơ học vẫn hoạt động ở đúng tần số thiết kế dù có cản nhỏ.

---

**Câu 4 - Tự luận:** Trong các hệ thống cơ khí chính xác bạn đã thiết kế (như đầu đo CMM, bàn trượt micrometer, hay cơ cấu vũ khí), hiện tượng stiction (stick-slip do ma sát Coulomb) ảnh hưởng như thế nào đến độ chính xác định vị? Bạn đã áp dụng kỹ thuật nào để giảm thiểu ảnh hưởng của ma sát phi tuyến này - ví dụ: dither, feedforward compensation, air bearing, hay các phương pháp khác? Trong trường hợp cụ thể đó, tần số dither được chọn như thế nào so với tần số cộng hưởng của hệ?

---

```json
{
  "quiz_metadata": {
    "topic": "Dao động tắt dần - suy giảm hàm mũ và hệ số phẩm chất Q",
    "lesson_ids_related": [5500, 5501],
    "questions": [
      {
        "id": 1,
        "type": "MCQ",
        "correct_answer": "A",
        "concept": "Cơ chế suy giảm hàm mũ từ ma sát nhớt"
      },
      {
        "id": 2,
        "type": "MCQ",
        "correct_answer": "C",
        "concept": "Hệ số phẩm chất Q và ứng dụng cảm biến"
      },
      {
        "id": 3,
        "type": "MCQ",
        "correct_answer": "A",
        "concept": "Tính toán tần số dao động có cản"
      },
      {
        "id": 4,
        "type": "open",
        "concept": "Stiction và các kỹ thuật bù ma sát phi tuyến"
      }
    ]
  }
}
```


## Quiz Questions


---
*Exported from Feynman Bot*
