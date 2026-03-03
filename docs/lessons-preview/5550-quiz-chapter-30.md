---
lesson_id: 5550
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:07.727416+00:00"
content_hash: 1fd5fc558c5b
chapter_number: 30
chapter_title: Chapter 30
section_number: 7
section_title: 30–6Diffraction by opaque screens
---
# ## Quiz: Nhiễu Xạ Fresnel và Nguyên Lý Babinet

*Source: Chapter 30 - Chapter 30 (Section 7) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_30.html)*

## Quiz: Nhiễu Xạ Fresnel và Nguyên Lý Babinet

Kiểm tra hiểu biết về nhiễu xạ Fresnel, nguyên lý Babinet, và ứng dụng trong hệ quang học chính xác.

---

**Câu 1.** Theo nguyên lý Huygens-Fresnel, khi tính cường độ ánh sáng phía sau một tấm chắn đục lỗ, ta coi:

A. Chỉ có vật liệu tấm chắn là nguồn sóng thứ cấp
B. Mỗi điểm trong lỗ hổng là nguồn sóng thứ cấp đồng pha với sóng tới
C. Ánh sáng truyền thẳng qua lỗ mà không bị nhiễu xạ
D. Chỉ các điểm tại rìa lỗ là nguồn sóng thứ cấp

**Đáp án: B**
*Giải thích:* Nguyên lý Huygens-Fresnel coi mỗi điểm trên vùng hở (lỗ) là một nguồn sóng thứ cấp với pha bằng pha sóng tới tại điểm đó. Mặc dù trong thực tế không có nguồn vật chất tại lỗ, phương pháp này cho kết quả chính xác.

---

**Câu 2.** Nguyên lý Babinet phát biểu rằng nếu tấm A là tấm chắn đục lỗ và tấm B là đĩa chắn đặc bổ sung (vừa khít che lỗ đó), thì:

A. $I_A + I_B = I_0$ (cường độ cộng lại bằng cường độ tự do)
B. $E_A + E_B = E_0$ (trường cộng lại bằng trường tự do)
C. $|E_A| = |E_B|$ chỉ đúng khi nguồn và màn ở vô cực
D. Cả B và C đều đúng

**Đáp án: D**
*Giải thích:* Nguyên lý Babinet: $E_A + E_B = E_0$ (luôn đúng). Ở điều kiện Fraunhofer (nguồn và màn ở xa, bỏ tia thẳng): $|E_A| = |E_B|$ nên $I_A = I_B$ — hoa văn nhiễu xạ cường độ giống nhau.

---

**Câu 3.** Điểm Poisson-Arago là hiện tượng gì?

A. Điểm tối xuất hiện tại tâm vùng sáng sau khi ánh sáng đi qua lỗ tròn
B. Điểm sáng xuất hiện tại chính giữa bóng tối của đĩa tròn đặc nhỏ
C. Điểm mà cường độ nhiễu xạ bằng đúng một nửa cường độ ánh sáng tới
D. Vùng chuyển tiếp giữa vùng sáng và vùng tối hoàn toàn

**Đáp án: B**
*Giải thích:* Điểm Poisson-Arago: tất cả sóng nhiễu xạ vòng quanh đĩa tròn có cùng khoảng đường đến tâm bóng, cộng hưởng xây dựng tạo điểm sáng tại chính giữa bóng tối. Arago xác nhận thực nghiệm năm 1818.

---

**Câu 4 (Tự luận).** Trong hệ thống kiểm tra bề mặt quang học (optical surface inspection) dùng laser của bạn, chùm tia phải đi qua nhiều khẩu độ cơ học. Hãy giải thích: (1) Khi nào bạn cần lo lắng về nhiễu xạ Fresnel? (2) Dùng số Fresnel để đưa ra quyết định thiết kế cụ thể. (3) Nếu phát hiện hiệu ứng Fresnel gây sai số, bạn sẽ xử lý bằng cách nào?

**Gợi ý trả lời mẫu:**
(1) Lo lắng khi số Fresnel $F = a^2/(\lambda z) \gtrsim 1$, tức là khi khẩu độ lớn, bước sóng nhỏ, hoặc khoảng cách ngắn. Ví dụ: laser 633 nm, khẩu độ 2 mm, khoảng cách 100 mm: $F = (10^{-3})^2/(633\times10^{-9}\times0.1) \approx 16$ — ở chế độ Fresnel mạnh.
(2) Nếu $F > 5$: thêm thấu kính chuẩn trực để tăng $z_{\text{hiệu dụng}}$ hoặc thu nhỏ khẩu độ. Nếu $F < 0.1$: hệ ở Fraunhofer, yên tâm.
(3) Xử lý: (a) điều chỉnh khoảng cách quang học, (b) dùng spatial filter (lỗ nhỏ + thấu kính) để làm sạch chùm tia, (c) mô phỏng số (simulation) để đặc trưng hóa sai số và hiệu chỉnh phần mềm.

---

```json
{
  "questions": [
    {"id": "q1", "type": "mcq", "question": "Theo nguyên lý Huygens-Fresnel, khi tính cường độ phía sau tấm chắn đục lỗ, ta coi:", "options": ["A. Chỉ vật liệu tấm chắn là nguồn thứ cấp", "B. Mỗi điểm trong lỗ là nguồn sóng thứ cấp đồng pha sóng tới", "C. Ánh sáng truyền thẳng không nhiễu xạ", "D. Chỉ rìa lỗ là nguồn thứ cấp"], "answer": "B", "explanation": "Huygens-Fresnel coi mỗi điểm trong vùng hở là nguồn thứ cấp với pha bằng sóng tới, dù không có nguồn vật chất."},
    {"id": "q2", "type": "mcq", "question": "Nguyên lý Babinet: tấm A (lỗ) + tấm B (đĩa bổ sung) thì:", "options": ["A. I_A + I_B = I_0", "B. E_A + E_B = E_0", "C. |E_A| = |E_B| chỉ khi Fraunhofer", "D. Cả B và C đúng"], "answer": "D", "explanation": "E_A + E_B = E_0 luôn đúng; ở điều kiện Fraunhofer (bỏ tia thẳng) thì |E_A|=|E_B|."},
    {"id": "q3", "type": "mcq", "question": "Điểm Poisson-Arago là:", "options": ["A. Điểm tối tại tâm vùng sáng", "B. Điểm sáng tại giữa bóng tối của đĩa tròn", "C. Điểm cường độ bằng nửa cường độ tới", "D. Rìa chuyển tiếp sáng-tối"], "answer": "B", "explanation": "Sóng vòng quanh đĩa đến tâm bóng cùng pha, cộng hưởng xây dựng tạo điểm sáng."},
    {"id": "q4", "type": "open", "question": "Trong hệ kiểm tra bề mặt quang học laser của bạn, khi nào cần lo về Fresnel? Dùng số Fresnel ra quyết định thiết kế. Nếu phát hiện Fresnel gây sai số thì xử lý thế nào?", "sample_answer": "Khi F=a²/(λz)≥1 thì lo. Nếu F>5 thêm collimating lens hoặc thu nhỏ khẩu độ. Xử lý: điều chỉnh khoảng cách quang học, dùng spatial filter, hoặc mô phỏng số để đặc trưng hóa sai số."}
  ]
}
```


## Quiz Questions

**Q1:** Theo nguyên lý Huygens-Fresnel, khi tính cường độ phía sau tấm chắn đục lỗ, ta coi:
- A) A. Chỉ vật liệu tấm chắn là nguồn thứ cấp
- B) B. Mỗi điểm trong lỗ là nguồn sóng thứ cấp đồng pha sóng tới
- C) C. Ánh sáng truyền thẳng không nhiễu xạ
- D) D. Chỉ rìa lỗ là nguồn thứ cấp

**Correct:** B

**Explanation:** Huygens-Fresnel coi mỗi điểm trong vùng hở là nguồn thứ cấp với pha bằng sóng tới, dù không có nguồn vật chất.

**Q2:** Nguyên lý Babinet: tấm A (lỗ) + tấm B (đĩa bổ sung) thì:
- A) A. I_A + I_B = I_0
- B) B. E_A + E_B = E_0
- C) C. |E_A| = |E_B| chỉ khi Fraunhofer
- D) D. Cả B và C đúng

**Correct:** D

**Explanation:** E_A + E_B = E_0 luôn đúng; ở điều kiện Fraunhofer (bỏ tia thẳng) thì |E_A|=|E_B|.

**Q3:** Điểm Poisson-Arago là:
- A) A. Điểm tối tại tâm vùng sáng
- B) B. Điểm sáng tại giữa bóng tối của đĩa tròn
- C) C. Điểm cường độ bằng nửa cường độ tới
- D) D. Rìa chuyển tiếp sáng-tối

**Correct:** B

**Explanation:** Sóng vòng quanh đĩa đến tâm bóng cùng pha, cộng hưởng xây dựng tạo điểm sáng.

**Q4:** Trong hệ kiểm tra bề mặt quang học laser của bạn, khi nào cần lo về Fresnel? Dùng số Fresnel ra quyết định thiết kế. Nếu phát hiện Fresnel gây sai số thì xử lý thế nào?

**Correct:** N/A


---
*Exported from Feynman Bot*
