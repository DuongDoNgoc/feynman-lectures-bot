---
lesson_id: 5460
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:05.563188+00:00"
content_hash: 3489f47d0cbe
chapter_number: 19
chapter_title: Chapter 19
section_number: 3
section_title: 19–2Locating the center of mass
---
# ## Quiz: Định Lý Pappus và Moment Quán Tính

*Source: Chapter 19 - Chapter 19 (Section 3) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_19.html)*

## Quiz: Định Lý Pappus và Moment Quán Tính

Bài kiểm tra về ứng dụng định lý Pappus và tính toán moment quán tính trong kỹ thuật cơ điện tử.

---

**Câu 1.** Định lý Pappus phát biểu rằng thể tích của khối tròn xoay tạo ra khi quay diện tích phẳng $A$ một vòng quanh trục bên ngoài bằng:

A. $V = A \cdot H$ với $H$ là chiều cao

B. $V = 2\pi x_{\text{CM}} \cdot A$ với $x_{\text{CM}}$ là khoảng cách từ khối tâm đến trục quay

C. $V = \pi x_{\text{CM}}^2 \cdot A$

D. $V = 2\pi \cdot A^2 / x_{\text{CM}}$

**Đáp án: B**
*Giải thích:* Định lý Pappus: $V = 2\pi x_{\text{CM}} \cdot A$. Ý nghĩa hình học: $2\pi x_{\text{CM}}$ là chu vi đường tròn mà khối tâm quét khi quay một vòng. Định lý này biến bài toán tích phân 3D thành bài toán tìm khối tâm 2D đơn giản hơn nhiều.

---

**Câu 2.** Moment quán tính hình trụ đặc khối lượng $M$, bán kính $R$, quay quanh trục tâm là:

A. $I = MR^2$

B. $I = \dfrac{2}{3}MR^2$

C. $I = \dfrac{1}{2}MR^2$

D. $I = \dfrac{1}{4}MR^2$

**Đáp án: C**
*Giải thích:* Tích phân $I = \int_0^R r^2 \cdot \frac{2M}{R^2}r\,dr = \frac{2M}{R^2} \cdot \frac{R^4}{4} = \frac{1}{2}MR^2$. So sánh: hình trụ rỗng (vành tròn) $I = MR^2$ — lớn hơn gấp đôi với cùng $M$ và $R$, vì toàn bộ khối lượng tập trung ở bán kính tối đa.

---

**Câu 3.** Theo định lý trục song song (Steiner), nếu moment quán tính qua khối tâm là $I_{\text{CM}}$ và trục quay mới cách khối tâm một khoảng $d$, moment quán tính theo trục mới là:

A. $I = I_{\text{CM}} - Md^2$

B. $I = I_{\text{CM}} \cdot Md^2$

C. $I = I_{\text{CM}} + Md^2$

D. $I = I_{\text{CM}} / (Md^2)$

**Đáp án: C**
*Giải thích:* $I = I_{\text{CM}} + Md^2$ — luôn lớn hơn $I_{\text{CM}}$ vì $Md^2 \geq 0$. Số hạng $Md^2$ đại diện cho đóng góp do chuyển trục. Trong thiết kế cánh tay robot, khi trục motor lệch khỏi khối tâm tải, số hạng này có thể chiếm phần lớn $I$ tổng, đòi hỏi motor lớn hơn để đạt cùng gia tốc.

---

**Câu 4 (Tự luận).** Trong công việc thiết kế encoder hoặc cơ cấu truyền động quay cho hệ đo lường độ chính xác cao, bạn áp dụng khái niệm moment quán tính như thế nào để tối ưu hóa hiệu năng? Hãy đề xuất một giải pháp kỹ thuật cụ thể dựa trên phân tích moment quán tính.

*Gợi ý trả lời:*
Trong thiết kế đĩa encoder cho trục đo góc chính xác, có hai mục tiêu mâu thuẫn: (1) $I$ đủ lớn để ổn định tốc độ (lọc rung động), (2) $I$ đủ nhỏ để servo đáp ứng nhanh. Giải pháp: dùng vật liệu mật độ cao (tungsten alloy) ở vành ngoài và vật liệu nhẹ (aluminum/carbon fiber) ở phần tâm — tập trung khối lượng hiệu quả ở bán kính lớn nhất, tăng $I$ mà không tăng tổng khối lượng nhiều. Định lý trục song song nhắc nhở rằng mọi lệch tâm lắp ghép đều tăng $I$ hiệu dụng — cần kiểm soát run-out khi lắp ráp ở cấp micromet.

```json
{"questions":[{"id":"q1","type":"mcq","question":"Định lý Pappus: thể tích khối tròn xoay tạo ra khi quay diện tích A quanh trục ngoài một vòng bằng:","options":["A. V = A·H","B. V = 2π·x_CM·A","C. V = π·x_CM²·A","D. V = 2π·A²/x_CM"],"answer":"B","explanation":"V = 2π·x_CM·A. Số 2π·x_CM là chu vi đường tròn mà khối tâm quét qua. Định lý biến tích phân 3D thành bài toán khối tâm 2D."},{"id":"q2","type":"mcq","question":"Moment quán tính hình trụ đặc khối lượng M, bán kính R quay quanh trục tâm là:","options":["A. I = MR²","B. I = (2/3)MR²","C. I = (1/2)MR²","D. I = (1/4)MR²"],"answer":"C","explanation":"I = (1/2)MR². Tích phân I = ∫r²dm = (2M/R²)∫₀ᴿ r³dr = MR²/2. Hình trụ rỗng (vành) có I = MR², lớn gấp đôi vì khối lượng tập trung ở R tối đa."},{"id":"q3","type":"mcq","question":"Định lý trục song song (Steiner): moment quán tính khi trục cách khối tâm d là:","options":["A. I = I_CM - Md²","B. I = I_CM · Md²","C. I = I_CM + Md²","D. I = I_CM / (Md²)"],"answer":"C","explanation":"I = I_CM + Md². Luôn lớn hơn I_CM. Trong cánh tay robot, khi trục motor lệch khỏi khối tâm tải, số hạng Md² chiếm phần lớn I tổng, đòi hỏi torque motor lớn hơn."},{"id":"q4","type":"open","question":"Trong thiết kế encoder hoặc cơ cấu truyền động quay cho hệ đo lường độ chính xác cao, bạn áp dụng moment quán tính như thế nào để tối ưu hóa hiệu năng?","sample_answer":"Dùng vật liệu mật độ cao (tungsten) ở vành ngoài và vật liệu nhẹ (aluminum/carbon fiber) ở tâm để tập trung khối lượng tại bán kính lớn — tăng I hiệu quả. Định lý trục song song nhắc rằng mọi lệch tâm lắp ghép tăng I hiệu dụng, cần kiểm soát run-out ở cấp micromet."}]}
```


## Quiz Questions

**Q1:** Định lý Pappus: thể tích khối tròn xoay tạo ra khi quay diện tích A quanh trục ngoài một vòng bằng:
- A) A. V = A·H
- B) B. V = 2π·x_CM·A
- C) C. V = π·x_CM²·A
- D) D. V = 2π·A²/x_CM

**Correct:** B

**Explanation:** V = 2π·x_CM·A. Số 2π·x_CM là chu vi đường tròn mà khối tâm quét qua. Định lý biến tích phân 3D thành bài toán khối tâm 2D.

**Q2:** Moment quán tính hình trụ đặc khối lượng M, bán kính R quay quanh trục tâm là:
- A) A. I = MR²
- B) B. I = (2/3)MR²
- C) C. I = (1/2)MR²
- D) D. I = (1/4)MR²

**Correct:** C

**Explanation:** I = (1/2)MR². Tích phân I = ∫r²dm = (2M/R²)∫₀ᴿ r³dr = MR²/2. Hình trụ rỗng (vành) có I = MR², lớn gấp đôi vì khối lượng tập trung ở R tối đa.

**Q3:** Định lý trục song song (Steiner): moment quán tính khi trục cách khối tâm d là:
- A) A. I = I_CM - Md²
- B) B. I = I_CM · Md²
- C) C. I = I_CM + Md²
- D) D. I = I_CM / (Md²)

**Correct:** C

**Explanation:** I = I_CM + Md². Luôn lớn hơn I_CM. Trong cánh tay robot, khi trục motor lệch khỏi khối tâm tải, số hạng Md² chiếm phần lớn I tổng, đòi hỏi torque motor lớn hơn.

**Q4:** Trong thiết kế encoder hoặc cơ cấu truyền động quay cho hệ đo lường độ chính xác cao, bạn áp dụng moment quán tính như thế nào để tối ưu hóa hiệu năng?

**Correct:** N/A


---
*Exported from Feynman Bot*
