---
lesson_id: 5387
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:03.788586+00:00"
content_hash: ba574afb2917
chapter_number: 11
chapter_title: Chapter 11
section_number: 5
section_title: 11–4Vectors
---
# ## Phân tích Vectơ — Phân tích Chuyên sâu

*Source: Chapter 11 - Chapter 11 (Section 5) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_11.html)*

## Phân tích Vectơ — Phân tích Chuyên sâu

### 1. Bất biến Dưới Phép Xoay Trục

Giả sử hệ tọa độ $(x,y)$ xoay một góc $\phi$ thành $(x',y')$. Quy tắc biến đổi:

$$x' = x\cos\phi + y\sin\phi$$
$$y' = -x\sin\phi + y\cos\phi$$

Một vectơ $\mathbf{A}$ có thành phần $(A_x, A_y)$ trong hệ $(x,y)$ sẽ có thành phần trong hệ mới:

$$A_{x'} = A_x\cos\phi + A_y\sin\phi$$
$$A_{y'} = -A_x\sin\phi + A_y\cos\phi$$

**Kiểm tra bất biến của độ dài:** $|\mathbf{A}|^2 = A_{x'}^2 + A_{y'}^2$?

$$A_{x'}^2 + A_{y'}^2 = (A_x\cos\phi + A_y\sin\phi)^2 + (-A_x\sin\phi + A_y\cos\phi)^2$$
$$= A_x^2(\cos^2\phi + \sin^2\phi) + A_y^2(\sin^2\phi + \cos^2\phi) = A_x^2 + A_y^2 \ \checkmark$$

Độ dài vectơ bất biến — đây là tính chất quan trọng nhất. **Ý nghĩa vật lý:** tốc độ của một vật không phụ thuộc vào cách ta chọn trục tọa độ để đo.

### 2. Tích Vô Hướng — Scalar Bất biến

Cho hai vectơ $\mathbf{a}$ và $\mathbf{b}$. Tích vô hướng trong hệ $(x,y)$:

$$\mathbf{a}\cdot\mathbf{b} = a_x b_x + a_y b_y$$

Trong hệ xoay $(x', y')$:

$$\mathbf{a}\cdot\mathbf{b} = a_{x'}b_{x'} + a_{y'}b_{y'} = (a_x\cos\phi + a_y\sin\phi)(b_x\cos\phi + b_y\sin\phi) + \ldots$$

Khai triển và đơn giản hóa sẽ cho đúng $a_x b_x + a_y b_y$. Tích vô hướng **không thay đổi** khi xoay trục.

**Hình học:** $\mathbf{a}\cdot\mathbf{b} = |\mathbf{a}||\mathbf{b}|\cos\theta$ — đây là độ dài hình chiếu của $\mathbf{b}$ lên $\mathbf{a}$, nhân với độ dài $\mathbf{a}$.

### 3. Ứng Dụng: Phân Tích Sai Số Cosine trong Đo Lường

**Vấn đề kỹ thuật:** Laser interferometer được căn chỉnh để đo dịch chuyển theo trục $x$. Trục thực tế của bàn máy lệch một góc nhỏ $\alpha$ so với trục đo. Tính sai số.

**Giải:**

Dịch chuyển thực của bàn máy: $\mathbf{d} = d(\cos\alpha,\; \sin\alpha)$

Trục đo của laser: $\hat{n} = (1, 0)$

Số đọc laser: $L = \mathbf{d}\cdot\hat{n} = d\cos\alpha$

Sai số tương đối: $\frac{\delta}{d} = 1 - \cos\alpha \approx \frac{\alpha^2}{2}$ (với $\alpha$ nhỏ)

**Kết quả số:** Với $\alpha = 1°= 0.01745$ rad:
$$\delta/d = 1 - \cos(1°) = 1 - 0.99985 = 0.015\%$$

Với yêu cầu đo $100\,mm$ chính xác $\pm 1\,\mu m$ ($10^{-5}$), góc lệch tối đa cho phép:

$$\alpha_{max} = \sqrt{2 \times 10^{-5}} \approx 0.0045\,\text{rad} \approx 0.26°$$

**Ý nghĩa:** Trong đo lường độ chính xác micro-mét, căn chỉnh laser cần chính xác dưới 0.3° — đây là yêu cầu cứng, không phải tùy chọn.

### 4. Tích Có Hướng (Cross Product) — Vuông Góc Tạo Vectơ Mới

Ngoài tích vô hướng, hai vectơ còn tạo ra **tích có hướng** (cross product):

$$\mathbf{a}\times\mathbf{b} = (a_y b_z - a_z b_y,\; a_z b_x - a_x b_z,\; a_x b_y - a_y b_x)$$

Độ lớn: $|\mathbf{a}\times\mathbf{b}| = |\mathbf{a}||\mathbf{b}|\sin\theta$

Hướng: vuông góc với mặt phẳng chứa $\mathbf{a}$ và $\mathbf{b}$ (quy tắc bàn tay phải).

**Ứng dụng:** Lực từ trường lên dây dẫn mang dòng: $\mathbf{F} = I\mathbf{L}\times\mathbf{B}$. Trong motor tuyến tính, phân tích $\mathbf{F}$ theo các thành phần dọc/ngang trục chính là bài toán cross product.

### 5. Bài Tập: Mô-men Lực trong Cánh Tay Robot

**Bài toán:** Cánh tay robot có độ dài $\mathbf{r} = (0.3, 0.4, 0)$ m (từ khớp đến đầu công tác). Lực tác dụng tại đầu công tác $\mathbf{F} = (0, -50, 0)$ N (trọng lực). Tính mô-men lực $\mathbf{\tau} = \mathbf{r}\times\mathbf{F}$ tác dụng lên khớp.

**Giải từng bước:**

$$\tau_x = r_y F_z - r_z F_y = (0.4)(0) - (0)(-50) = 0$$
$$\tau_y = r_z F_x - r_x F_z = (0)(0) - (0.3)(0) = 0$$
$$\tau_z = r_x F_y - r_y F_x = (0.3)(-50) - (0.4)(0) = -15\,\text{N·m}$$

Mô-men: $\mathbf{\tau} = (0, 0, -15)$ N·m — nghĩa là mô-men quay quanh trục $z$, chiều âm (xoay thuận chiều kim đồng hồ nhìn từ trên).

**Ý nghĩa:** Motor tại khớp phải tạo mô-men $+15$ N·m để giữ tay robot cân bằng. Đây là bài toán tính mô-men trực tiếp từ cross product.

### Tóm tắt kỹ thuật

| Phép tính | Công thức | Kết quả | Ứng dụng |
|-----------|-----------|---------|----------|
| Dot product | $a_xb_x+a_yb_y+a_zb_z$ | Scalar | Hình chiếu, sai số cosine |
| Cross product | $(a_yb_z-a_zb_y,\ldots)$ | Vectơ ⊥ | Mô-men lực, lực từ |
| Độ dài | $\sqrt{a_x^2+a_y^2+a_z^2}$ | Scalar | Khoảng cách, tốc độ |

---
*Exported from Feynman Bot*
