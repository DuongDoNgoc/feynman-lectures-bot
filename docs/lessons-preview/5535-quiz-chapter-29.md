---
lesson_id: 5535
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:07.358471+00:00"
content_hash: b19fb9a4f47a
chapter_number: 29
chapter_title: Chapter 29
section_number: 5
section_title: 29–4Two dipole radiators
---
# ## Kiểm Tra: Giao Thoa Hai Nguồn và Phép Tổng Hợp Sóng

*Source: Chapter 29 - Chapter 29 (Section 5) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_29.html)*

## Kiểm Tra: Giao Thoa Hai Nguồn và Phép Tổng Hợp Sóng

**Câu 1:** Hai nguồn bức xạ cùng biên độ $A$, pha lệch nhau $\Delta\phi = 2\pi/3$ (120°). Biên độ của sóng tổng hợp là:

A) $2A$
B) $A\sqrt{3}$
C) $A$
D) $A/2$

**Đáp án: C**
Giải thích: Dùng công thức $R_A = 2A\cos(\Delta\phi/2) = 2A\cos(\pi/3) = 2A \times 0.5 = A$. Có thể kiểm tra bằng phasor: tổng của hai vector đơn vị lệch nhau 120° trong mặt phẳng phức có độ dài bằng 1 (hình tam giác đều). Cũng có thể tính $R_A^2 = A^2 + A^2 + 2A^2\cos(2\pi/3) = 2A^2 + 2A^2(-0.5) = A^2$, nên $R_A = A$.

---

**Câu 2:** Phương pháp phasor (số phức) ưu việt hơn phương pháp lượng giác khi tổng hợp sóng vì:

A) Phasor cho kết quả chính xác hơn về mặt toán học
B) Với N nguồn bất kỳ, phasor đơn giản thành bài toán cộng N vector phức, không cần nhớ công thức lượng giác phức tạp
C) Phasor chỉ áp dụng được với biên độ bằng nhau
D) Phasor tính được cả biên độ lẫn tần số của sóng kết quả

**Đáp án: B**
Giải thích: Phương pháp lượng giác đòi hỏi các công thức như $\cos A + \cos B = 2\cos(\frac{A+B}{2})\cos(\frac{A-B}{2})$ và nhanh chóng trở nên phức tạp khi có 3 nguồn trở lên. Phasor biến bài toán thành cộng vector phức: $\tilde{R} = \sum_n A_n e^{i\phi_n}$, áp dụng được cho N nguồn bất kỳ với biên độ và pha bất kỳ. Lưu ý: phasor không tính được tần số — đó là thông số đầu vào đã biết trước.

---

**Câu 3:** Hai nguồn có biên độ $A_1 = 3$ và $A_2 = 4$ (đơn vị tùy ý), dao động cùng pha ($\Delta\phi = 0$). Cường độ tổng hợp bằng bao nhiêu lần cường độ của nguồn 1 đơn lẻ?

A) $16/9$
B) $7/3$
C) $49/9$
D) $25/9$

**Đáp án: C**
Giải thích: Cùng pha nên $R_A = A_1 + A_2 = 3 + 4 = 7$. Cường độ $I \propto R_A^2 = 49$. Cường độ nguồn 1 đơn lẻ $I_1 \propto A_1^2 = 9$. Tỉ số $I/I_1 = 49/9 \approx 5.44$. Chú ý: nếu tính nhầm $I \propto I_1 + I_2 = 9 + 16 = 25$ (bỏ qua interference term), kết quả sai. Phải tổng hợp *trường* trước, rồi mới bình phương để tính cường độ.

---

**Câu 4 (Tự luận):** Trong hệ thống đo vị trí laser interferometry mà bạn sử dụng cho điều khiển micro-mét, chùm laser được chia thành hai: một chùm reference (chiều dài cố định $L_{ref}$) và một chùm đo (chiều dài thay đổi $L_{meas}$ theo vị trí bàn máy). Hai chùm gặp nhau tại photodetector.

a) Viết biểu thức cho tín hiệu tại detector theo hiệu đường đi $\Delta L = L_{meas} - L_{ref}$, giả sử biên độ hai chùm bằng nhau là $A$ và bước sóng laser $\lambda = 633$ nm (HeNe).

b) Khi bàn máy di chuyển $d = 1$ µm, tín hiệu tại detector thay đổi bao nhiêu vân (fringe)? 

c) Tại sao hệ thống interferometry có thể đạt độ phân giải tốt hơn nhiều so với $\lambda/2$, và điều này liên hệ thế nào với bài toán tổng hợp hai sóng?

**Hướng dẫn trả lời:**

a) Hiệu đường đi $\Delta L$ gây ra hiệu pha $\Delta\phi = 2\pi \cdot 2\Delta L / \lambda$ (nhân 2 vì ánh sáng đi và về). Tín hiệu:
$$I = I_0\left[1 + \cos\left(\frac{4\pi\Delta L}{\lambda}\right)\right] = 2I_0\cos^2\left(\frac{2\pi\Delta L}{\lambda}\right)$$
Tín hiệu dao động giữa $0$ và $4A^2 \cdot \varepsilon_0 c$ (min và max cường độ).

b) Mỗi vân (fringe) tương ứng $\Delta L = \lambda/2 = 316.5$ nm. Với $d = 1$ µm = 1000 nm:
$$n_{fringes} = 2d/\lambda = 2000/633 \approx 3.16 \text{ vân}$$

c) Hệ thống interpolate (nội suy) giữa các vân bằng cách phân tích hình dạng tín hiệu sine. Với ADC 12-bit và xử lý tín hiệu số, người ta phân giải 1/1000 vân, tương đương $\lambda/2000 \approx 0.3$ nm. Đây là ứng dụng trực tiếp của phasor: biên độ và pha của tín hiệu sine $I(\Delta L)$ cho biết đầy đủ thông tin về vị trí.


---
*Exported from Feynman Bot*
