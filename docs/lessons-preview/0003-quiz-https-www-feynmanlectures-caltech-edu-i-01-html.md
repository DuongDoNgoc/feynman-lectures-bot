---
lesson_id: 3
lesson_type: quiz
approval_status: pending
exported_at: "2026-02-28T02:21:51.354628+00:00"
content_hash: eac04146128c
chapter_number: 1
chapter_title: "https://www.feynmanlectures.caltech.edu/I_01.html"
section_number: 1
section_title: Introduction
---
# ## Quiz: Nguyên tử trong Chuyển động

*Source: Chapter 1 - https://www.feynmanlectures.caltech.edu/I_01.html (Section 1)*

## Quiz: Nguyên tử trong Chuyển động

### Câu 1 (Trắc nghiệm)

Ở nhiệt độ phòng (T = 300 K), vận tốc rms của phân tử N₂ (khối lượng $m = 4.65 \times 10^{-26}$ kg) là bao nhiêu?

**A.** ~170 m/s
**B.** ~340 m/s
**C.** ~517 m/s
**D.** ~1500 m/s

*Đáp án: C*

*Giải thích:* Sử dụng công thức $v_{rms} = \sqrt{3k_BT/m}$, với $k_B = 1.38 \times 10^{-23}$ J/K, T = 300 K:
$$v_{rms} = \sqrt{\frac{3 \times 1.38 \times 10^{-23} \times 300}{4.65 \times 10^{-26}}} \approx 517 \text{ m/s}$$

---

### Câu 2 (Trắc nghiệm)

Theo mô hình nguyên tử Feynman, khi ta ép hai nguyên tử lại gần nhau hơn khoảng cách cân bằng, lực nào xuất hiện?

**A.** Lực hút mạnh hơn (do điện từ)
**B.** Lực đẩy mạnh (do nguyên lý loại trừ Pauli)
**C.** Không có lực nào — nguyên tử trung tính không tương tác
**D.** Lực hút hấp dẫn tăng lên

*Đáp án: B*

*Giải thích:* Khi khoảng cách nguyên tử nhỏ hơn $r_0 = 2^{1/6}\sigma$, số hạng $1/r^{12}$ trong thế năng Lennard-Jones chiếm ưu thế, tạo ra lực đẩy rất mạnh. Về bản chất lượng tử, nguyên lý loại trừ Pauli ngăn electron của hai nguyên tử chiếm cùng trạng thái, gây ra "áp suất suy biến" đẩy nguyên tử ra xa.

---

### Câu 3 (Trắc nghiệm)

Phương pháp khoa học của Feynman nhấn mạnh điều gì là "thẩm phán tối cao" của mọi kiến thức vật lý?

**A.** Toán học và sự nhất quán lý thuyết
**B.** Ý kiến đồng thuận của cộng đồng khoa học
**C.** Thực nghiệm (experiment)
**D.** Sự đơn giản và tính thẩm mỹ của lý thuyết

*Đáp án: C*

*Giải thích:* Feynman khẳng định rõ ràng: *"The test of all knowledge is experiment. Experiment is the sole judge of scientific truth."* Dù lý thuyết có đẹp đẽ đến đâu, nếu mâu thuẫn với thực nghiệm — nó sai. Đây là điểm phân biệt khoa học tự nhiên với triết học hay toán học thuần túy.

---

### Câu 4 (Tự luận mở)

*Câu hỏi cho mechatronics engineer:*

Bạn đang thiết kế hệ thống làm mát cho một bộ điều khiển servo công suất cao, hoạt động trong môi trường từ -10°C đến +80°C. Dựa trên hiểu biết về chuyển động nguyên tử và nhiệt động lực học, hãy phân tích:

a) Tại sao nhiệt độ cao lại ảnh hưởng tiêu cực đến tuổi thọ linh kiện điện tử?
b) Cơ chế nào ở mức nguyên tử giải thích tại sao kim loại dẫn điện tốt hơn ở nhiệt độ thấp?
c) Đề xuất 2 biện pháp kỹ thuật để kiểm soát nhiệt độ, lý giải bằng nguyên lý vật lý nguyên tử.

*Đáp án mẫu:*

a) Ở nhiệt độ cao, nguyên tử dao động mạnh hơn (động năng $\overline{E_k} = \frac{3}{2}k_BT$ tăng), làm tăng tốc độ khuếch tán và phản ứng hóa học. Quá trình điện di (electromigration) trong dây dẫn tăng mạnh: ion kim loại bị "cuốn đi" bởi dòng điện, tạo ra đứt gãy dây dẫn vi mô — đây là nguyên nhân chính gây hỏng IC ở nhiệt độ cao.

b) Trong kim loại, electron tự do di chuyển trong mạng tinh thể. Ở nhiệt độ thấp, nguyên tử dao động ít hơn → ít "chướng ngại vật" hơn cho electron → điện trở suất giảm (theo công thức $\rho \propto T$ cho kim loại). Một số kim loại đặc biệt đạt trạng thái siêu dẫn khi $T < T_c$, điện trở bằng 0.

c) Biện pháp 1: **Tản nhiệt bằng đối lưu cưỡng bức** — quạt tạo dòng không khí làm tăng số va chạm phân tử khí với bề mặt nóng, tăng tốc độ truyền nhiệt. Biện pháp 2: **Heat pipe (ống nhiệt)** — sử dụng chuyển pha lỏng-khí: chất lỏng bay hơi ở đầu nóng (hấp thụ nhiệt ẩn), hơi di chuyển đến đầu lạnh, ngưng tụ và tỏa nhiệt. Hiệu quả gấp hàng trăm lần dẫn nhiệt thông thường.

---

```json
{
  "questions": [
    {
      "id": "q1",
      "type": "mcq",
      "question": "Ở nhiệt độ phòng (T = 300 K), vận tốc rms của phân tử N₂ (m = 4.65×10⁻²⁶ kg) là bao nhiêu?",
      "options": ["A. ~170 m/s", "B. ~340 m/s", "C. ~517 m/s", "D. ~1500 m/s"],
      "answer": "C",
      "explanation": "v_rms = sqrt(3k_BT/m) = sqrt(3 × 1.38×10⁻²³ × 300 / 4.65×10⁻²⁶) ≈ 517 m/s"
    },
    {
      "id": "q2",
      "type": "mcq",
      "question": "Khi hai nguyên tử bị ép lại gần hơn khoảng cách cân bằng, lực nào xuất hiện?",
      "options": ["A. Lực hút điện từ mạnh hơn", "B. Lực đẩy mạnh do nguyên lý Pauli", "C. Không có lực tương tác", "D. Lực hút hấp dẫn tăng"],
      "answer": "B",
      "explanation": "Số hạng 1/r¹² trong thế Lennard-Jones tạo lực đẩy mạnh khi r < r₀. Nguyên nhân lượng tử: nguyên lý loại trừ Pauli ngăn electron trùng trạng thái."
    },
    {
      "id": "q3",
      "type": "mcq",
      "question": "Feynman coi điều gì là thẩm phán tối cao của kiến thức vật lý?",
      "options": ["A. Toán học và nhất quán lý thuyết", "B. Đồng thuận khoa học", "C. Thực nghiệm (experiment)", "D. Tính đơn giản thẩm mỹ"],
      "answer": "C",
      "explanation": "Feynman: 'The test of all knowledge is experiment. Experiment is the sole judge of scientific truth.' Lý thuyết dù đẹp đến đâu mà mâu thuẫn thực nghiệm thì sai."
    },
    {
      "id": "q4",
      "type": "open",
      "question": "Bạn thiết kế hệ thống làm mát servo (-10°C đến +80°C). Phân tích: (a) Tại sao nhiệt cao hại linh kiện? (b) Tại sao kim loại dẫn điện tốt hơn khi lạnh? (c) Đề xuất 2 biện pháp làm mát với lý giải nguyên lý nguyên tử.",
      "sample_answer": "(a) T cao → dao động nguyên tử mạnh → electromigration tăng, phá hủy dây dẫn vi mô trong IC. (b) T thấp → dao động ít → ít cản trở electron tự do → điện trở suất ρ ∝ T giảm. (c) Quạt cưỡng bức tăng va chạm phân tử khí; heat pipe dùng ẩn nhiệt bay hơi-ngưng tụ hiệu quả gấp trăm lần dẫn nhiệt."
    }
  ]
}
```



## Quiz Questions

**Q1:** Ở nhiệt độ phòng (T = 300 K), vận tốc rms của phân tử N₂ (m = 4.65×10⁻²⁶ kg) là bao nhiêu?
- A) A. ~170 m/s
- B) B. ~340 m/s
- C) C. ~517 m/s
- D) D. ~1500 m/s

**Correct:** C

**Explanation:** v_rms = sqrt(3k_BT/m) = sqrt(3 × 1.38×10⁻²³ × 300 / 4.65×10⁻²⁶) ≈ 517 m/s

**Q2:** Khi hai nguyên tử bị ép lại gần hơn khoảng cách cân bằng, lực nào xuất hiện?
- A) A. Lực hút điện từ mạnh hơn
- B) B. Lực đẩy mạnh do nguyên lý Pauli
- C) C. Không có lực tương tác
- D) D. Lực hút hấp dẫn tăng

**Correct:** B

**Explanation:** Số hạng 1/r¹² trong thế Lennard-Jones tạo lực đẩy mạnh khi r < r₀. Nguyên nhân lượng tử: nguyên lý loại trừ Pauli ngăn electron trùng trạng thái.

**Q3:** Feynman coi điều gì là thẩm phán tối cao của kiến thức vật lý?
- A) A. Toán học và nhất quán lý thuyết
- B) B. Đồng thuận khoa học
- C) C. Thực nghiệm (experiment)
- D) D. Tính đơn giản thẩm mỹ

**Correct:** C

**Explanation:** Feynman: 'The test of all knowledge is experiment. Experiment is the sole judge of scientific truth.' Lý thuyết dù đẹp đến đâu mà mâu thuẫn thực nghiệm thì sai.

**Q4:** Bạn thiết kế hệ thống làm mát servo (-10°C đến +80°C). Phân tích: (a) Tại sao nhiệt cao hại linh kiện? (b) Tại sao kim loại dẫn điện tốt hơn khi lạnh? (c) Đề xuất 2 biện pháp làm mát với lý giải nguyên lý nguyên tử.

**Correct:** N/A


---
*Exported from Feynman Bot*
