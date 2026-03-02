---
lesson_id: 5457
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-02T15:10:29.914631+00:00"
content_hash: 09d72692c703
chapter_number: 19
chapter_title: Chapter 19
section_number: 2
section_title: 19–1Properties of the center of mass
---
# ## Quiz: Khối Tâm (Center of Mass)

*Source: Chapter 19 - Chapter 19 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_19.html)*

## Quiz: Khối Tâm (Center of Mass)

Bài kiểm tra này giúp bạn củng cố kiến thức về khái niệm khối tâm và ứng dụng của nó trong cơ học.

---

**Câu 1.** Khối tâm (center of mass) của một hệ nhiều hạt được xác định bởi công thức:

A. $X_{\text{CM}} = \sum m_i x_i \cdot \sum m_i$

B. $X_{\text{CM}} = \dfrac{\sum m_i x_i}{\sum m_i}$

C. $X_{\text{CM}} = \dfrac{\sum x_i}{N}$ với $N$ là số hạt và mỗi hạt có khối lượng bằng nhau bất kể giá trị $m_i$

D. $X_{\text{CM}} = \dfrac{M \cdot \sum x_i}{N}$

**Đáp án: B**
*Giải thích:* Khối tâm được tính theo trung bình có trọng số: $X_{\text{CM}} = \dfrac{\sum m_i x_i}{\sum m_i}$. Mỗi hạt đóng góp vào vị trí khối tâm theo tỷ lệ khối lượng của nó. Trường hợp đặc biệt khi mọi hạt có cùng khối lượng $m$, công thức rút gọn thành $X_{\text{CM}} = \dfrac{\sum x_i}{N}$, nhưng đây chỉ là trường hợp riêng.

---

**Câu 2.** Một kỹ sư thiết kế cánh tay robot gồm hai đoạn: đoạn A có khối lượng $M_A = 2\,\text{kg}$, khối tâm tại vị trí $x = 0.3\,\text{m}$; đoạn B có khối lượng $M_B = 1\,\text{kg}$, khối tâm tại $x = 0.8\,\text{m}$. Khối tâm của toàn cánh tay ở vị trí nào?

A. $x = 0.55\,\text{m}$

B. $x = 0.467\,\text{m}$

C. $x = 0.40\,\text{m}$

D. $x = 0.50\,\text{m}$

**Đáp án: B**
*Giải thích:* $X_{\text{CM}} = \dfrac{M_A \cdot 0.3 + M_B \cdot 0.8}{M_A + M_B} = \dfrac{2 \times 0.3 + 1 \times 0.8}{3} = \dfrac{0.6 + 0.8}{3} = \dfrac{1.4}{3} \approx 0.467\,\text{m}$. Kỹ thuật phân chia vật thể thành các phần rồi xử lý từng phần như một điểm khối lượng đặt tại khối tâm của phần đó rất hữu ích trong thiết kế cơ khí.

---

**Câu 3.** Nguyên lý quan trọng nhất về khối tâm liên quan đến lực ngoại tác là:

A. Lực ngoại tác làm thay đổi vị trí khối tâm tức thời, bất kể cấu trúc bên trong vật.

B. Tổng lực ngoại tác bằng tổng khối lượng nhân với gia tốc của khối tâm: $F_{\text{net}} = M a_{\text{CM}}$.

C. Lực nội tác giữa các phần trong vật cũng ảnh hưởng đến gia tốc khối tâm.

D. Khối tâm luôn nằm bên trong vật thể, không thể nằm ngoài.

**Đáp án: B**
*Giải thích:* Định lý cơ bản là $\mathbf{F}_{\text{net}} = M \mathbf{a}_{\text{CM}}$. Các lực nội tác (internal forces) triệt tiêu nhau theo định luật Newton III, nên chỉ lực ngoại tác (external forces) mới tạo ra gia tốc cho khối tâm. Lưu ý: khối tâm *có thể* nằm ngoài vật thể — ví dụ khối tâm của vòng nhẫn nằm ở tâm hình học, trong khoảng trống.

---

**Câu 4 (Tự luận).** Trong hệ thống vũ khí dẫn đường chính xác hoặc robot quân sự mà bạn thiết kế, tại sao việc xác định chính xác khối tâm của hệ thống lại quan trọng? Hãy nêu ít nhất hai tình huống thực tế và giải thích cách lệch khối tâm ảnh hưởng đến hiệu năng hay độ chính xác của hệ thống.

*Gợi ý trả lời:*
1. **Cân bằng cánh tay robot/pháo quay:** Khi khối tâm của cánh tay không nằm trên trục quay, moment trọng lực tạo ra lực dư làm servo phải liên tục bù tải — gây sai số vị trí ở cấp độ micrometer và tăng nhiệt động cơ. Trong hệ đo lường độ chính xác cao (CMM — Coordinate Measuring Machine), lệch khối tâm đầu đo chỉ vài gram·cm có thể gây sai số hàng chục micromet.
2. **Tên lửa và đạn dẫn đường:** Khối tâm phải nằm trước tâm áp lực khí động học (center of pressure) để đảm bảo độ ổn định đạn đạo. Nếu khối tâm lệch khỏi trục đối xứng do lắp ráp không đều (asymmetric mass distribution), đạn sẽ bị yaw/pitch không mong muốn, giảm độ chính xác CEP (Circular Error Probable).

```json
{"questions":[{"id":"q1","type":"mcq","question":"Khối tâm (center of mass) của một hệ nhiều hạt được xác định bởi công thức nào?","options":["A. X_CM = Σ(m_i · x_i) · Σm_i","B. X_CM = Σ(m_i · x_i) / Σm_i","C. X_CM = Σx_i / N với mọi khối lượng bằng nhau","D. X_CM = M · Σx_i / N"],"answer":"B","explanation":"Khối tâm là trung bình có trọng số của vị trí các hạt: X_CM = Σ(m_i x_i)/Σm_i. Chỉ khi mọi hạt có cùng khối lượng thì X_CM = Σx_i/N."},{"id":"q2","type":"mcq","question":"Cánh tay robot gồm đoạn A (M_A=2kg, x=0.3m) và đoạn B (M_B=1kg, x=0.8m). Khối tâm ở đâu?","options":["A. x = 0.55 m","B. x = 0.467 m","C. x = 0.40 m","D. x = 0.50 m"],"answer":"B","explanation":"X_CM = (2×0.3 + 1×0.8)/(2+1) = 1.4/3 ≈ 0.467 m. Đây là ứng dụng trực tiếp công thức khối tâm cho hệ hai vật."},{"id":"q3","type":"mcq","question":"Nguyên lý về lực ngoại tác và khối tâm phát biểu rằng:","options":["A. Lực ngoại tác thay đổi vị trí khối tâm tức thời","B. F_net = M·a_CM, chỉ lực ngoại tác ảnh hưởng đến gia tốc khối tâm","C. Lực nội tác cũng góp phần vào gia tốc khối tâm","D. Khối tâm luôn nằm bên trong vật thể"],"answer":"B","explanation":"Theo định luật Newton cho hệ nhiều hạt: F_net_external = M·a_CM. Lực nội tác triệt tiêu nhau (Newton III), không ảnh hưởng gia tốc khối tâm. Khối tâm có thể nằm ngoài vật (ví dụ: vòng nhẫn)."},{"id":"q4","type":"open","question":"Trong hệ thống vũ khí dẫn đường chính xác hoặc robot đo lường mà bạn thiết kế, tại sao xác định chính xác khối tâm lại quan trọng? Nêu ít nhất hai tình huống thực tế.","sample_answer":"1. Cân bằng cánh tay robot/đầu đo CMM: lệch khối tâm gây moment trọng lực dư, servo phải bù liên tục, sai số vị trí tăng lên hàng chục micromet. 2. Tên lửa/đạn dẫn đường: khối tâm phải trước tâm áp lực để ổn định đạn đạo; lệch khối tâm do lắp ráp không đều gây yaw/pitch không kiểm soát, tăng CEP."}]}
```


## Quiz Questions

**Q1:** Khối tâm (center of mass) của một hệ nhiều hạt được xác định bởi công thức nào?
- A) A. X_CM = Σ(m_i · x_i) · Σm_i
- B) B. X_CM = Σ(m_i · x_i) / Σm_i
- C) C. X_CM = Σx_i / N với mọi khối lượng bằng nhau
- D) D. X_CM = M · Σx_i / N

**Correct:** B

**Explanation:** Khối tâm là trung bình có trọng số của vị trí các hạt: X_CM = Σ(m_i x_i)/Σm_i. Chỉ khi mọi hạt có cùng khối lượng thì X_CM = Σx_i/N.

**Q2:** Cánh tay robot gồm đoạn A (M_A=2kg, x=0.3m) và đoạn B (M_B=1kg, x=0.8m). Khối tâm ở đâu?
- A) A. x = 0.55 m
- B) B. x = 0.467 m
- C) C. x = 0.40 m
- D) D. x = 0.50 m

**Correct:** B

**Explanation:** X_CM = (2×0.3 + 1×0.8)/(2+1) = 1.4/3 ≈ 0.467 m. Đây là ứng dụng trực tiếp công thức khối tâm cho hệ hai vật.

**Q3:** Nguyên lý về lực ngoại tác và khối tâm phát biểu rằng:
- A) A. Lực ngoại tác thay đổi vị trí khối tâm tức thời
- B) B. F_net = M·a_CM, chỉ lực ngoại tác ảnh hưởng đến gia tốc khối tâm
- C) C. Lực nội tác cũng góp phần vào gia tốc khối tâm
- D) D. Khối tâm luôn nằm bên trong vật thể

**Correct:** B

**Explanation:** Theo định luật Newton cho hệ nhiều hạt: F_net_external = M·a_CM. Lực nội tác triệt tiêu nhau (Newton III), không ảnh hưởng gia tốc khối tâm. Khối tâm có thể nằm ngoài vật (ví dụ: vòng nhẫn).

**Q4:** Trong hệ thống vũ khí dẫn đường chính xác hoặc robot đo lường mà bạn thiết kế, tại sao xác định chính xác khối tâm lại quan trọng? Nêu ít nhất hai tình huống thực tế.

**Correct:** N/A


---
*Exported from Feynman Bot*
