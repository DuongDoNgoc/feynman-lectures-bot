---
lesson_id: 5334
lesson_type: quiz
approval_status: approved
exported_at: "2026-02-28T14:08:58.999095+00:00"
content_hash: 16688a62d421
chapter_number: 4
chapter_title: Chapter 4
section_number: 4
section_title: 4–3Kinetic energy
---
# ## Quiz: Động Năng và Bảo Toàn Năng Lượng

*Source: Chapter 4 - Chapter 4 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_04.html)*

## Quiz: Động Năng và Bảo Toàn Năng Lượng

### Câu 1
Một vật khối lượng 2 kg đang chuyển động với vận tốc 6 m/s. Nếu vận tốc tăng gấp đôi lên 12 m/s, động năng thay đổi như thế nào?

A. Tăng gấp đôi (từ 36 J lên 72 J)
B. Tăng gấp 4 lần (từ 36 J lên 144 J)
C. Tăng gấp 3 lần (từ 36 J lên 108 J)
D. Tăng gấp đôi (từ 72 J lên 144 J)

**Đáp án: B**
*Giải thích: $KE = \frac{1}{2}mv^2$. Ban đầu: $KE_1 = \frac{1}{2}(2)(6^2) = 36$ J. Sau: $KE_2 = \frac{1}{2}(2)(12^2) = 144$ J. Tỷ lệ = 4. Vì $KE \propto v^2$, tăng $v$ gấp đôi → KE tăng gấp 4.*

### Câu 2
Con lắc đơn dài 1 m dao động với biên độ góc nhỏ. Tại vị trí nào động năng bằng thế năng?

A. Tại vị trí cân bằng (đáy)
B. Tại vị trí cực biên
C. Tại vị trí có góc lệch bằng $\theta_0/\sqrt{2}$ (khi $h = h_{max}/2$)
D. Không bao giờ bằng nhau

**Đáp án: C**
*Giải thích: $E_{total} = KE + PE$. Khi $KE = PE$, ta có $KE = E_{total}/2$, tức $PE = mgh = mgh_{max}/2$, suy ra $h = h_{max}/2$.*

### Câu 3
Rotor servo motor có mô men quán tính $I = 0.01 \, \text{kg}\cdot\text{m}^2$ quay ở $\omega = 1000 \, \text{rpm}$. Động năng quay là:

A. 500 J
B. 274 J
C. 548 J
D. 5000 J

**Đáp án: C**
*Giải thích: $\omega = 1000 \times \frac{2\pi}{60} \approx 104.7$ rad/s. $KE = \frac{1}{2}I\omega^2 = \frac{1}{2}(0.01)(104.7)^2 \approx 548$ J.*

### Câu 4 (Tự luận)
Trong hệ thống vũ khí tự động hoặc cánh tay robot bạn đang thiết kế, hãy mô tả một tình huống cụ thể mà việc tính toán sai động năng của một bộ phận chuyển động có thể gây ra hỏng hóc nghiêm trọng. Bạn sẽ áp dụng nguyên lý $KE = \frac{1}{2}mv^2$ (hoặc $KE = \frac{1}{2}I\omega^2$) như thế nào để thiết kế hệ thống an toàn?

*Gợi ý trả lời mẫu: Ví dụ, khi thiết kế hệ phanh cho trục quay của cơ cấu ngắm tự động, nếu tính thiếu động năng của rotor và bánh răng, resistor xả sẽ bị quá tải nhiệt và cháy, khiến hệ không dừng được đúng vị trí. Cần tính tổng $KE = \sum \frac{1}{2}I_i\omega_i^2$ cho tất cả bộ phận quay, rồi chọn resistor có công suất tản nhiệt đủ lớn với hệ số an toàn 1.5-2x.*

```json
{"questions": [{"id": "q1", "type": "mcq", "question": "Một vật khối lượng 2 kg đang chuyển động với vận tốc 6 m/s. Nếu vận tốc tăng gấp đôi lên 12 m/s, động năng thay đổi như thế nào?", "options": ["A. Tăng gấp đôi (từ 36 J lên 72 J)", "B. Tăng gấp 4 lần (từ 36 J lên 144 J)", "C. Tăng gấp 3 lần (từ 36 J lên 108 J)", "D. Tăng gấp đôi (từ 72 J lên 144 J)"], "answer": "B", "explanation": "KE tỷ lệ với v², tăng v gấp đôi → KE tăng gấp 4 lần. KE1=36J, KE2=144J."}, {"id": "q2", "type": "mcq", "question": "Tại vị trí nào của con lắc thì động năng bằng thế năng?", "options": ["A. Tại vị trí cân bằng (đáy)", "B. Tại vị trí cực biên", "C. Tại vị trí có độ cao bằng nửa độ cao cực đại", "D. Không bao giờ bằng nhau"], "answer": "C", "explanation": "Khi KE=PE=E_total/2, suy ra h=h_max/2."}, {"id": "q3", "type": "mcq", "question": "Rotor servo motor I=0.01 kg·m² quay ở 1000 rpm. Động năng quay là?", "options": ["A. 500 J", "B. 274 J", "C. 548 J", "D. 5000 J"], "answer": "C", "explanation": "ω=104.7 rad/s, KE=½×0.01×104.7²≈548 J"}, {"id": "q4", "type": "open", "question": "Trong hệ thống bạn đang thiết kế, mô tả tình huống tính sai động năng gây hỏng hóc và cách áp dụng KE=½mv² để thiết kế an toàn.", "sample_answer": "Ví dụ: tính thiếu KE của rotor trong hệ phanh servo → resistor xả quá tải → không dừng được đúng vị trí. Giải pháp: tính tổng KE tất cả bộ phận quay, chọn resistor với hệ số an toàn 1.5-2x."}]}
```


## Quiz Questions

**Q1:** Một vật khối lượng 2 kg đang chuyển động với vận tốc 6 m/s. Nếu vận tốc tăng gấp đôi lên 12 m/s, động năng thay đổi như thế nào?
- A) A. Tăng gấp đôi (từ 36 J lên 72 J)
- B) B. Tăng gấp 4 lần (từ 36 J lên 144 J)
- C) C. Tăng gấp 3 lần (từ 36 J lên 108 J)
- D) D. Tăng gấp đôi (từ 72 J lên 144 J)

**Correct:** B

**Explanation:** KE tỷ lệ với v², tăng v gấp đôi → KE tăng gấp 4 lần. KE1=36J, KE2=144J.

**Q2:** Tại vị trí nào của con lắc thì động năng bằng thế năng?
- A) A. Tại vị trí cân bằng (đáy)
- B) B. Tại vị trí cực biên
- C) C. Tại vị trí có độ cao bằng nửa độ cao cực đại
- D) D. Không bao giờ bằng nhau

**Correct:** C

**Explanation:** Khi KE=PE=E_total/2, suy ra h=h_max/2.

**Q3:** Rotor servo motor I=0.01 kg·m² quay ở 1000 rpm. Động năng quay là?
- A) A. 500 J
- B) B. 274 J
- C) C. 548 J
- D) D. 5000 J

**Correct:** C

**Explanation:** ω=104.7 rad/s, KE=½×0.01×104.7²≈548 J

**Q4:** Trong hệ thống bạn đang thiết kế, mô tả tình huống tính sai động năng gây hỏng hóc và cách áp dụng KE=½mv² để thiết kế an toàn.

**Correct:** N/A


---
*Exported from Feynman Bot*
