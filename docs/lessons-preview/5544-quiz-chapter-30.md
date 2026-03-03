---
lesson_id: 5544
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:07.576126+00:00"
content_hash: 0bc01102d3e7
chapter_number: 30
chapter_title: Chapter 30
section_number: 3
section_title: 30–2The diffraction grating
---
# ## Kiểm Tra: Cách Tử Nhiễu Xạ và Tán Sắc

*Source: Chapter 30 - Chapter 30 (Section 3) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_30.html)*

## Kiểm Tra: Cách Tử Nhiễu Xạ và Tán Sắc

**Câu 1 (Trắc nghiệm):** Một cách tử nhiễu xạ có $N = 5000$ vạch, dùng ở bậc $m = 2$. Khả năng phân giải bước sóng (resolving power) $R$ của cách tử này là:

A) $R = 2500$
B) $R = 5000$
C) $R = 10000$
D) $R = 25000000$

**Đáp án: C**

*Giải thích:* $R = mN = 2 \times 5000 = 10000$. Điều này có nghĩa: cách tử phân biệt được hai bước sóng cách nhau tối thiểu $\delta\lambda = \lambda/R = 500/10000 = 0.05$ nm tại $\lambda = 500$ nm. Đây là lý do dùng bậc cao hơn khi cần phân giải tốt hơn mà không cần tăng số vạch.

---

**Câu 2 (Trắc nghiệm):** Ánh sáng trắng ($\lambda = 400$–$700$ nm) chiếu vuông góc vào cách tử có $d = 600$ nm. Bậc nhiễu xạ tối đa có thể quan sát được là:

A) $m_{max} = 1$
B) $m_{max} = 2$
C) $m_{max} = 3$
D) $m_{max} = 4$

**Đáp án: A**

*Giải thích:* Điều kiện tồn tại: $\sin\theta = m\lambda/d \leq 1$, tức $m \leq d/\lambda$. Với $\lambda_{min} = 400$ nm: $m_{max} = \lfloor 600/400 \rfloor = 1$. Với $\lambda_{max} = 700$ nm: $m_{max} = \lfloor 600/700 \rfloor = 0$ — bậc 1 không tồn tại với đỏ! Thực ra với $d = 600$ nm, chỉ tồn tại bậc 1 cho $\lambda < 600$ nm (xanh lam đến tím). Đây là một ràng buộc thiết kế quan trọng: $d$ phải đủ lớn so với $\lambda$ để dùng được bậc mong muốn.

---

**Câu 3 (Trắc nghiệm):** Trong thiết kế cách tử nhiễu xạ (blazed grating), mục đích của việc mài nghiêng từng vạch với góc blaze $\theta_B$ là:

A) Tăng số vạch $N$ trên một mm để cải thiện resolving power
B) Chuyển năng lượng từ bậc 0 (phản xạ thẳng) sang bậc nhiễu xạ mong muốn để tăng hiệu suất
C) Giảm góc nhiễu xạ để thiết bị nhỏ gọn hơn
D) Tạo ra phân cực tuyến tính cho ánh sáng nhiễu xạ

**Đáp án: B**

*Giải thích:* Cách tử thường lãng phí $50$–$70\%$ năng lượng vào bậc 0 vô dụng. Blazed grating định hướng phản xạ Fresnel của mỗi facet (mặt vạch) vào đúng bậc nhiễu xạ cần dùng. Tại bước sóng blaze $\lambda_B$, hiệu suất đạt $70$–$90\%$. Đây là nguyên tắc thiết kế của hầu hết cách tử trong spectrometer thương mại.

---

**Câu 4 (Tự luận):** Trong hệ thống LiDAR quân sự phát hiện mục tiêu, cần phân biệt hai mục tiêu cách nhau $\Delta r = 15$ cm theo chiều sâu. Hệ thống dùng laser xung ngắn với coherence length $L_c = 10$ cm và bộ phân tích phổ dùng cách tử.

(a) Tại sao $\Delta r < L_c$ lại gây ra vấn đề trong phân tích giao thoa?
(b) Để đo khoảng cách bằng spectral interferometry (giao thoa phổ), cần resolving power $R$ tối thiểu là bao nhiêu? Biết rằng tiêu chí là $R \geq \lambda/\delta\lambda$ với $\delta\lambda = \lambda^2/(2L_c)$ và $\lambda = 1550$ nm.
(c) Với cách tử 1200 vạch/mm và $m = 1$, cần chiều rộng tối thiểu bao nhiêu?

**Gợi ý đáp án:**

(a) Coherence length $L_c$ xác định độ dài đường đi tối đa mà hai sóng vẫn có thể giao thoa. Khi $\Delta r < L_c = 10$ cm, hai echo từ hai mục tiêu CÙNG giao thoa với nhau — không phân biệt được trực tiếp bằng time-of-flight. Cần dùng phân tích phổ để "giải mã" thông tin khoảng cách từ pattern giao thoa.

(b) $\delta\lambda = \lambda^2/(2L_c) = (1550 \times 10^{-9})^2/(2 \times 0.1) = 1.20 \times 10^{-14}/0.2 = 6.0 \times 10^{-14}$ m $= 6.0 \times 10^{-5}$ nm. Quá nhỏ! Thực ra công thức đúng cho two-target separation: $\delta\lambda = \lambda^2/(2n\Delta r)$ với $n=1$ không khí:
$\delta\lambda = (1550)^2/(2 \times 150 \times 10^6) = 2.4025 \times 10^6 / (3 \times 10^8) = 8.0 \times 10^{-3}$ nm.
$R = \lambda/\delta\lambda = 1550/0.008 = 193750$.

(c) $N = R/m = 193750$ vạch. $L = N/1200 = 161.5$ mm. Cần cách tử rộng 16 cm chiếu sáng hoàn toàn — rất lớn! Trong thực tế, dùng cách tử Echelle (bậc $m = 50$–$100$) để giảm $N$ và $L$ xuống còn vài mm, đây là cách thiết kế của các spectrometer compact dùng trong FMCW LiDAR hiện đại.


---
*Exported from Feynman Bot*
