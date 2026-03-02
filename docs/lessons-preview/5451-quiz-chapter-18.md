---
lesson_id: 5451
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-02T15:10:29.779327+00:00"
content_hash: bdbed21fa146
chapter_number: 18
chapter_title: Chapter 18
section_number: 1
section_title: 18Rotation in Two Dimensions
---
# ## Quiz: Động Lực Học Vật Rắn và Chuyển Động Quay

*Source: Chapter 18 - Chapter 18 (Section 1) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_18.html)*

## Quiz: Động Lực Học Vật Rắn và Chuyển Động Quay

### Câu 1 (Trắc nghiệm)

Một đĩa đặc (solid disk) và một vành tròn (thin ring) có cùng khối lượng $M$ và bán kính $R$. Khi chịu cùng mô-men xoắn $\tau$, cái nào đạt gia tốc góc lớn hơn?

A. Vành tròn, vì khối lượng phân bố ở xa trục hơn
B. Đĩa đặc, vì $I_{\text{disk}} = \frac{1}{2}MR^2 < I_{\text{ring}} = MR^2$, nên $\alpha_{\text{disk}} = \tau/I_{\text{disk}}$ lớn hơn
C. Cả hai bằng nhau vì cùng $M$ và $R$
D. Vành tròn, vì tích lũy nhiều năng lượng hơn

**Đáp án: B**

*Giải thích:* Moment quán tính đĩa đặc $I_{\text{disk}} = \frac{1}{2}MR^2$, còn vành tròn $I_{\text{ring}} = MR^2 = 2I_{\text{disk}}$. Theo $\tau = I\alpha$, với cùng $\tau$, đĩa đặc có $I$ nhỏ hơn nên $\alpha$ lớn hơn gấp đôi. Vành tròn tích trữ năng lượng tốt hơn nhưng khó tăng tốc hơn — đây là trade-off trong thiết kế flywheel.

---

### Câu 2 (Trắc nghiệm)

Trong thiết kế robot arm, khi arm duỗi dài thêm $\Delta L$ (payload dịch ra xa joint), moment quán tính $I$ của hệ thay đổi như thế nào?

A. Tăng tuyến tính theo $\Delta L$
B. Giảm vì payload nằm xa trung tâm khối
C. Tăng theo bình phương $\Delta L$ (theo định lý Steiner: $I = I_{\text{CM}} + M(L+\Delta L)^2$)
D. Không thay đổi nếu khối lượng payload không đổi

**Đáp án: C**

*Giải thích:* Theo định lý trục song song (Steiner theorem): $I = I_{\text{CM}} + Md^2$ trong đó $d$ là khoảng cách từ khối tâm đến trục quay. Khi arm duỗi ra thêm $\Delta L$, $d$ tăng và $I$ tăng theo $d^2$. Đây là lý do robot arm ở tư thế duỗi thẳng cần mô-men xoắn motor lớn hơn nhiều so với tư thế gập vào — thông tin quan trọng cho motion planning.

---

### Câu 3 (Trắc nghiệm)

Một bánh đà trong hệ UPS flywheel có $I = 10$ kg·m² quay ở $\omega = 200\pi$ rad/s. Tính động năng tích trữ:

A. $K = 197.4$ kJ
B. $K = 394.8$ kJ
C. $K = 986.8$ kJ
D. $K = 1973.9$ kJ

**Đáp án: D**

*Giải thích:* $K = \frac{1}{2}I\omega^2 = \frac{1}{2}(10)(200\pi)^2 = 5 \times (200\pi)^2 = 5 \times 394784 \approx 1{,}973{,}920$ J $\approx 1973.9$ kJ. Lưu ý $\omega = 200\pi$ rad/s tương ứng 6000 RPM — tốc độ cao điển hình cho flywheel UPS công nghiệp.

---

### Câu 4 (Tự luận)

Bạn đang thiết kế hệ thống định vị micrometer dùng motor servo. Motor có rotor (đĩa đặc, $M_r = 0.3$ kg, $R_r = 2$ cm), kết nối với bàn trượt qua gear ratio $n = 50:1$. Khối lượng bàn trượt $M_s = 5$ kg chuyển động tịnh tiến (tương đương $I_{\text{slide}} = M_s/n^2$ quy về trục motor). Nếu cần gia tốc góc motor $\alpha = 5000$ rad/s² để đạt gia tốc tịnh tiến $a = 2$ m/s² cho bàn trượt, hãy kiểm tra tính nhất quán và tính mô-men xoắn motor cần thiết.

**Gợi ý trả lời:**

Kiểm tra tính nhất quán: với $n = 50$, $\alpha_{\text{slide}} = \alpha_{\text{motor}}/n = 5000/50 = 100$ rad/s². Nếu lead screw pitch $p = 2$ mm/rev = $2\times10^{-3}/(2\pi)$ m/rad, thì $a = \alpha_{\text{slide}} \times p/(2\pi) = 100 \times 3.18\times10^{-4} = 0.0318$ m/s² — không khớp với 2 m/s². Điều này cho thấy cần xem lại thông số gear/lead screw.

Giả sử trực tiếp: $I_{\text{rotor}} = \frac{1}{2}(0.3)(0.02)^2 = 6\times10^{-5}$ kg·m², $I_{\text{slide,motor}} = 5/50^2 = 2\times10^{-3}$ kg·m².

$I_{\text{total}} = 6\times10^{-5} + 2\times10^{-3} = 2.06\times10^{-3}$ kg·m²

$\tau_{\text{motor}} = I_{\text{total}} \times \alpha = 2.06\times10^{-3} \times 5000 = 10.3$ N·m

Ý nghĩa thực tế: phần lớn moment quán tính đến từ bàn trượt (quy về motor), không phải rotor — đây là bài học quan trọng trong sizing motor cho hệ CNC.

```json
{"questions":[{"id":"q1","type":"mcq","question":"Một đĩa đặc và một vành tròn có cùng khối lượng $M$ và bán kính $R$. Khi chịu cùng mô-men xoắn $\\tau$, cái nào đạt gia tốc góc lớn hơn?","options":["A. Vành tròn, vì khối lượng phân bố ở xa trục hơn","B. Đĩa đặc, vì $I_{disk}=MR^2/2 < I_{ring}=MR^2$, nên $\\alpha_{disk}$ lớn hơn","C. Cả hai bằng nhau vì cùng $M$ và $R$","D. Vành tròn, vì tích lũy nhiều năng lượng hơn"],"answer":"B","explanation":"Moment quán tính đĩa đặc nhỏ hơn vành tròn (1/2 MR² vs MR²), nên với cùng mô-men xoắn, đĩa đặc đạt gia tốc góc lớn hơn gấp đôi."},{"id":"q2","type":"mcq","question":"Trong robot arm, khi arm duỗi dài thêm $\\Delta L$ (payload dịch ra xa joint), moment quán tính $I$ thay đổi thế nào?","options":["A. Tăng tuyến tính theo $\\Delta L$","B. Giảm vì payload nằm xa trung tâm khối","C. Tăng theo bình phương $\\Delta L$ theo định lý Steiner","D. Không thay đổi nếu khối lượng payload không đổi"],"answer":"C","explanation":"Theo định lý Steiner: $I = I_{CM} + Md^2$, khi $d$ tăng, $I$ tăng theo $d^2$. Robot arm duỗi thẳng cần mô-men xoắn motor lớn hơn nhiều."},{"id":"q3","type":"mcq","question":"Bánh đà $I = 10$ kg·m² quay ở $\\omega = 200\\pi$ rad/s. Động năng tích trữ là bao nhiêu?","options":["A. 197.4 kJ","B. 394.8 kJ","C. 986.8 kJ","D. 1973.9 kJ"],"answer":"D","explanation":"$K = \\frac{1}{2}I\\omega^2 = \\frac{1}{2}(10)(200\\pi)^2 \\approx 1973.9$ kJ. Omega = 200π rad/s tương ứng 6000 RPM."},{"id":"q4","type":"open","question":"Trong hệ thống motor servo cho bàn trượt định vị micrometer với gear ratio 50:1, tại sao moment quán tính của tải (bàn trượt) thường chiếm ưu thế so với rotor motor khi quy về trục motor? Điều này ảnh hưởng thế nào đến việc chọn motor?","sample_answer":"Moment quán tính tải quy về trục motor: $I_{load,motor} = I_{load}/n^2$. Với $n=50$, hệ số chia là 2500, nhưng tải cơ khí thường có $I$ lớn (bàn trượt kg cấp), trong khi rotor nhẹ. Ví dụ $I_{rotor}=6\\times10^{-5}$ kg·m², $I_{slide,motor}=5/2500=2\\times10^{-3}$ kg·m² — tải chiếm 97% tổng $I$. Kỹ sư phải chọn motor có đủ mô-men xoắn liên tục cho tổng $I$ này, không chỉ dựa vào rotor inertia trong datasheet."}]}
```


## Quiz Questions

**Q1:** Một đĩa đặc và một vành tròn có cùng khối lượng $M$ và bán kính $R$. Khi chịu cùng mô-men xoắn $\tau$, cái nào đạt gia tốc góc lớn hơn?
- A) A. Vành tròn, vì khối lượng phân bố ở xa trục hơn
- B) B. Đĩa đặc, vì $I_{disk}=MR^2/2 < I_{ring}=MR^2$, nên $\alpha_{disk}$ lớn hơn
- C) C. Cả hai bằng nhau vì cùng $M$ và $R$
- D) D. Vành tròn, vì tích lũy nhiều năng lượng hơn

**Correct:** B

**Explanation:** Moment quán tính đĩa đặc nhỏ hơn vành tròn (1/2 MR² vs MR²), nên với cùng mô-men xoắn, đĩa đặc đạt gia tốc góc lớn hơn gấp đôi.

**Q2:** Trong robot arm, khi arm duỗi dài thêm $\Delta L$ (payload dịch ra xa joint), moment quán tính $I$ thay đổi thế nào?
- A) A. Tăng tuyến tính theo $\Delta L$
- B) B. Giảm vì payload nằm xa trung tâm khối
- C) C. Tăng theo bình phương $\Delta L$ theo định lý Steiner
- D) D. Không thay đổi nếu khối lượng payload không đổi

**Correct:** C

**Explanation:** Theo định lý Steiner: $I = I_{CM} + Md^2$, khi $d$ tăng, $I$ tăng theo $d^2$. Robot arm duỗi thẳng cần mô-men xoắn motor lớn hơn nhiều.

**Q3:** Bánh đà $I = 10$ kg·m² quay ở $\omega = 200\pi$ rad/s. Động năng tích trữ là bao nhiêu?
- A) A. 197.4 kJ
- B) B. 394.8 kJ
- C) C. 986.8 kJ
- D) D. 1973.9 kJ

**Correct:** D

**Explanation:** $K = \frac{1}{2}I\omega^2 = \frac{1}{2}(10)(200\pi)^2 \approx 1973.9$ kJ. Omega = 200π rad/s tương ứng 6000 RPM.

**Q4:** Trong hệ thống motor servo cho bàn trượt định vị micrometer với gear ratio 50:1, tại sao moment quán tính của tải (bàn trượt) thường chiếm ưu thế so với rotor motor khi quy về trục motor? Điều này ảnh hưởng thế nào đến việc chọn motor?

**Correct:** N/A


---
*Exported from Feynman Bot*
