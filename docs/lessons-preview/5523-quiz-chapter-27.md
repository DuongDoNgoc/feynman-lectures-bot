---
lesson_id: 5523
lesson_type: quiz
approval_status: pending
exported_at: "2026-03-02T15:10:31.669063+00:00"
content_hash: ab8b2d69c5c5
chapter_number: 27
chapter_title: Chapter 27
section_number: 7
section_title: 27–6Aberrations
---
# ## Quiz: Aberration Trong Quang Học — Giới Hạn Của Thấu Kính

*Source: Chapter 27 - Chapter 27 (Section 7) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_27.html)*

## Quiz: Aberration Trong Quang Học — Giới Hạn Của Thấu Kính

### Câu 1 (Trắc nghiệm)
Spherical aberration (quang sai cầu) trong thấu kính hình cầu xảy ra chủ yếu vì:

A. Ánh sáng có nhiều màu sắc khác nhau và mỗi màu có chiết suất khác nhau

B. Tia sáng đi qua mép thấu kính (xa trục) không tuân theo xấp xỉ paraxial và hội tụ ở điểm khác so với tia gần trục

C. Thấu kính bị nứt hoặc có bọt khí trong thuỷ tinh

D. Bề mặt thấu kính bị bụi bẩn hoặc trầy xước

**Đáp án: B**
*Giải thích:* Spherical aberration là hệ quả trực tiếp của việc xấp xỉ paraxial ($\sin\theta \approx \theta$) không đúng với tia sáng xa trục. Tia đi qua mép thấu kính bị khúc xạ mạnh hơn so với dự đoán của công thức paraxial, dẫn đến điểm hội tụ khác nhau.

---

### Câu 2 (Trắc nghiệm)
Nguyên nhân gây chromatic aberration (quang sai màu sắc) là:

A. Thấu kính có hai bề mặt với bán kính cong khác nhau

B. Chiết suất của thuỷ tinh thay đổi theo bước sóng (dispersion), khiến tiêu cự khác nhau cho mỗi màu sắc

C. Tia sáng bị phản xạ một phần tại bề mặt thấu kính

D. Thấu kính bị nóng lên khi có ánh sáng chiếu vào, thay đổi chiết suất

**Đáp án: B**
*Giải thích:* Dispersion (tán sắc) là hiện tượng chiết suất phụ thuộc bước sóng. Do $n = n(\lambda)$, từ lensmaker's equation $1/f = (n-1)(1/R_1 - 1/R_2)$, tiêu cự $f$ cũng phụ thuộc $\lambda$. Ánh sáng tím hội tụ gần hơn, ánh sáng đỏ hội tụ xa hơn.

---

### Câu 3 (Trắc nghiệm)
Giới hạn nhiễu xạ (*diffraction limit*) của hệ quang học liên quan đến:

A. Chất lượng bề mặt thấu kính và độ chính xác gia công cơ khí

B. Bản chất sóng của ánh sáng: khi sai lệch thời gian giữa các tia nhỏ hơn một chu kỳ dao động, không thể cải thiện thêm chất lượng ảnh

C. Công suất của nguồn sáng và cường độ chiếu sáng

D. Nhiệt độ môi trường và độ ổn định nhiệt của hệ quang học

**Đáp án: B**
*Giải thích:* Feynman chỉ ra rằng nguyên lý thời gian cực tiểu chỉ là xấp xỉ — ánh sáng là sóng. Khi OPD (optical path difference) giữa tia biên và tia trục nhỏ hơn $\lambda$ (một bước sóng), hệ quang học đã đạt diffraction limit. Kích thước điểm hội tụ tối thiểu: $r_{min} \approx 1.22\lambda/2NA$.

---

### Câu 4 (Tự luận)
**Câu hỏi mở:** Trong hệ đo vị trí laser (laser displacement sensor) bạn thiết kế cho máy gia công CNC có yêu cầu độ phân giải 0.1 μm, hãy phân tích:
(a) Tại sao chromatic aberration là vấn đề quan trọng nếu dùng đèn LED thay vì laser đơn sắc?
(b) Giải thích cách thiết kế achromatic doublet giúp khắc phục vấn đề này
(c) Tại sao kể cả khi khắc phục được tất cả aberration, vẫn có một giới hạn vật lý cho độ phân giải của hệ quang học?

**Gợi ý trả lời mẫu:** (a) LED có bandwidth rộng (~20-50 nm). Do chromatic aberration, mỗi bước sóng hội tụ ở điểm khác nhau, làm mờ điểm đo, giảm SNR và độ chính xác; (b) Achromatic doublet dùng hai thấu kính vật liệu khác Abbe number, điều kiện: $P_1/V_1 + P_2/V_2 = 0$. Hai bước sóng cách nhau (~486 nm và 656 nm) hội tụ tại cùng một điểm; (c) Giới hạn nhiễu xạ Rayleigh: $r_{Airy} = 1.22\lambda/(2NA)$. Với $\lambda = 530$ nm, $NA = 0.3$: $r_{min} \approx 1.08$ μm. Muốn đạt 0.1 μm cần $NA > 3$ (không khả thi trong không khí) hoặc dùng kỹ thuật near-field.

```json
{
  "questions": [
    {"id": "q1", "type": "mcq", "question": "Spherical aberration xảy ra chủ yếu vì:", "options": ["A. Ánh sáng nhiều màu, mỗi màu có chiết suất khác nhau", "B. Tia xa trục không tuân theo xấp xỉ paraxial, hội tụ ở điểm khác", "C. Thấu kính có bọt khí trong thuỷ tinh", "D. Bề mặt thấu kính bị trầy xước"], "answer": "B", "explanation": "Spherical aberration là hệ quả của xấp xỉ paraxial không đúng với tia xa trục."},
    {"id": "q2", "type": "mcq", "question": "Nguyên nhân chromatic aberration là:", "options": ["A. Thấu kính có hai bề mặt bán kính khác nhau", "B. Chiết suất thuỷ tinh thay đổi theo bước sóng (dispersion)", "C. Tia sáng bị phản xạ tại bề mặt", "D. Thấu kính nóng lên thay đổi chiết suất"], "answer": "B", "explanation": "Dispersion khiến n phụ thuộc bước sóng, dẫn đến tiêu cự f khác nhau cho mỗi màu."},
    {"id": "q3", "type": "mcq", "question": "Giới hạn nhiễu xạ liên quan đến:", "options": ["A. Chất lượng bề mặt thấu kính", "B. Bản chất sóng của ánh sáng: OPD < λ thì không cải thiện thêm được", "C. Công suất nguồn sáng", "D. Nhiệt độ môi trường"], "answer": "B", "explanation": "Khi OPD < λ, hệ đạt diffraction limit. r_min ≈ 1.22λ/(2NA)."},
    {"id": "q4", "type": "open", "question": "Hệ đo vị trí laser độ phân giải 0.1 μm: (a) tại sao LED gây vấn đề chromatic aberration? (b) achromatic doublet khắc phục thế nào? (c) tại sao vẫn có giới hạn vật lý cho độ phân giải?", "sample_answer": "(a) LED có bandwidth ~30-50 nm, mỗi bước sóng hội tụ khác điểm; (b) Doublet dùng P1/V1 + P2/V2 = 0 để 2 bước sóng hội tụ cùng điểm; (c) Giới hạn Rayleigh r=1.22λ/(2NA), với λ=530nm, NA=0.3 thì r≈1μm > 0.1μm yêu cầu."}
  ]
}
```


## Quiz Questions

**Q1:** Spherical aberration xảy ra chủ yếu vì:
- A) A. Ánh sáng nhiều màu, mỗi màu có chiết suất khác nhau
- B) B. Tia xa trục không tuân theo xấp xỉ paraxial, hội tụ ở điểm khác
- C) C. Thấu kính có bọt khí trong thuỷ tinh
- D) D. Bề mặt thấu kính bị trầy xước

**Correct:** B

**Explanation:** Spherical aberration là hệ quả của xấp xỉ paraxial không đúng với tia xa trục.

**Q2:** Nguyên nhân chromatic aberration là:
- A) A. Thấu kính có hai bề mặt bán kính khác nhau
- B) B. Chiết suất thuỷ tinh thay đổi theo bước sóng (dispersion)
- C) C. Tia sáng bị phản xạ tại bề mặt
- D) D. Thấu kính nóng lên thay đổi chiết suất

**Correct:** B

**Explanation:** Dispersion khiến n phụ thuộc bước sóng, dẫn đến tiêu cự f khác nhau cho mỗi màu.

**Q3:** Giới hạn nhiễu xạ liên quan đến:
- A) A. Chất lượng bề mặt thấu kính
- B) B. Bản chất sóng của ánh sáng: OPD < λ thì không cải thiện thêm được
- C) C. Công suất nguồn sáng
- D) D. Nhiệt độ môi trường

**Correct:** B

**Explanation:** Khi OPD < λ, hệ đạt diffraction limit. r_min ≈ 1.22λ/(2NA).

**Q4:** Hệ đo vị trí laser độ phân giải 0.1 μm: (a) tại sao LED gây vấn đề chromatic aberration? (b) achromatic doublet khắc phục thế nào? (c) tại sao vẫn có giới hạn vật lý cho độ phân giải?

**Correct:** N/A


---
*Exported from Feynman Bot*
