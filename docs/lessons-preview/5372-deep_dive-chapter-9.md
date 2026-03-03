---
lesson_id: 5372
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:00.709064+00:00"
content_hash: c0daa38e68e2
chapter_number: 9
chapter_title: Chapter 9
section_number: 6
section_title: 9–5Meaning of the dynamical equations
---
# ## Giải Phương Trình Chuyển Động Số — Phân tích Chuyên sâu

*Source: Chapter 9 - Chapter 9 (Section 6) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_09.html)*

## Giải Phương Trình Chuyển Động Số — Phân tích Chuyên sâu

### Phương pháp Euler và giới hạn của nó

Feynman trình bày phương pháp Euler thuận để giải $m\ddot{x} = F(x, \dot{x}, t)$:

**Hệ phương trình bậc 1:**

$$\frac{dv}{dt} = \frac{F(x, v, t)}{m}, \quad \frac{dx}{dt} = v$$

**Cập nhật Euler:**

$$v_{n+1} = v_n + \frac{F(x_n, v_n, t_n)}{m} \cdot h$$
$$x_{n+1} = x_n + v_n \cdot h$$

trong đó $h = \epsilon$ là bước thời gian.

**Vấn đề:** Euler sử dụng $v_n$ (đầu bước) để cập nhật $x$, nhưng thực ra $x$ thay đổi theo $v$ trong suốt bước — gây sai số tích lũy.

---

### Cải tiến: Phương pháp Euler giữa bước (Leap-Frog)

Feynman đề xuất một mẹo hay: tính $v$ ở **nửa bước lệch** so với $x$:

$$v_{n+1/2} = v_{n-1/2} + a(x_n) \cdot h$$
$$x_{n+1} = x_n + v_{n+1/2} \cdot h$$

Phương pháp leap-frog bảo toàn năng lượng tốt hơn và có sai số $O(h^2)$. Đây là lý do tại sao các mô phỏng động lực học phân tử và orbital mechanics dùng leap-frog thay vì Euler thuần.

---

### Ứng dụng: Mô phỏng dao động trong cơ cấu truyền động vũ khí

**Bài toán:** Cơ cấu trượt-quay trong súng máy có:
- Khối lượng bộ phận chuyển động: $m = 0.8\,\text{kg}$
- Lực lò xo hồi: $F_{spring} = -800x$ (N, m)
- Lực cản khí: $F_{gas} = 2000\,\text{N}$ trong $t \in [0, 2\,\text{ms}]$, sau đó $= 0$
- Điều kiện đầu: $x(0) = 0$, $v(0) = 0$

**Giải số với $h = 0.5\,\text{ms}$:**

Bước 0: $t = 0$, $x = 0$, $v = 0$, $a = (2000 - 800\times0)/0.8 = 2500\,\text{m/s}^2$

Bước 1: $t = 0.5\,\text{ms}$
$v_1 = 0 + 2500 \times 0.0005 = 1.25\,\text{m/s}$
$x_1 = 0 + 0 \times 0.0005 = 0\,\text{m}$

Bước 2: $t = 1.0\,\text{ms}$
$a_1 = (2000 - 800\times0)/0.8 = 2500\,\text{m/s}^2$
$v_2 = 1.25 + 2500 \times 0.0005 = 2.50\,\text{m/s}$
$x_2 = 0 + 1.25 \times 0.0005 = 0.000625\,\text{m} = 0.625\,\text{mm}$

Bước 3: $t = 1.5\,\text{ms}$
$a_2 = (2000 - 800\times0.000625)/0.8 = (2000 - 0.5)/0.8 \approx 2499.4\,\text{m/s}^2$
$v_3 = 2.50 + 2499.4 \times 0.0005 = 3.75\,\text{m/s}$
$x_3 = 0.000625 + 2.50 \times 0.0005 = 0.001875\,\text{m} = 1.875\,\text{mm}$

Bước 4: $t = 2.0\,\text{ms}$ (hết lực khí)
$v_4 \approx 4.99\,\text{m/s}$, $x_4 \approx 3.75\,\text{mm}$

Sau $t = 2\,\text{ms}$, lực khí tắt — chỉ còn lò xo. Hệ dao động với $\omega_n = \sqrt{800/0.8} = \sqrt{1000} \approx 31.6\,\text{rad/s}$, $T = 0.2\,\text{s}$.

---

### Phân tích sai số và chọn bước thời gian

Tiêu chí ổn định Euler: $h < \frac{2}{\omega_n}$. Với $\omega_n = 31.6\,\text{rad/s}$:

$$h_{max} = \frac{2}{31.6} \approx 0.063\,\text{s}$$

Bước $h = 0.5\,\text{ms}$ an toàn hơn 100 lần so với giới hạn — kết quả đáng tin cậy.

Quy tắc thực tế: chọn $h \leq T_{min}/20$ (trong đó $T_{min}$ là chu kỳ của mode nhanh nhất trong hệ). Với 20 bước mỗi chu kỳ, sai số Euler ≈ 2.5%.

---

### Bài tập có lời giải

**Bài toán:** Con lắc đơn (góc nhỏ): $\ddot{\theta} = -(g/L)\theta$ với $g = 9.81\,\text{m/s}^2$, $L = 0.25\,\text{m}$.

Điều kiện đầu: $\theta(0) = 0.1\,\text{rad}$, $\dot\theta(0) = 0$.

Dùng Euler với $h = 0.01\,\text{s}$, tính 3 bước đầu.

**Lời giải:**

$\omega_n^2 = g/L = 9.81/0.25 = 39.24\,\text{rad}^2/\text{s}^2$

Bước 0: $\theta_0 = 0.1$, $\omega_0 = 0$, $\alpha_0 = -39.24 \times 0.1 = -3.924\,\text{rad/s}^2$

Bước 1 ($t = 0.01$):
$\omega_1 = 0 + (-3.924)(0.01) = -0.03924\,\text{rad/s}$
$\theta_1 = 0.1 + 0 \times 0.01 = 0.1\,\text{rad}$

Bước 2 ($t = 0.02$):
$\alpha_1 = -39.24 \times 0.1 = -3.924\,\text{rad/s}^2$
$\omega_2 = -0.03924 + (-3.924)(0.01) = -0.07848\,\text{rad/s}$
$\theta_2 = 0.1 + (-0.03924)(0.01) = 0.09961\,\text{rad}$

Bước 3 ($t = 0.03$):
$\alpha_2 = -39.24 \times 0.09961 = -3.908\,\text{rad/s}^2$
$\omega_3 = -0.07848 + (-3.908)(0.01) = -0.11757\,\text{rad/s}$
$\theta_3 = 0.09961 + (-0.07848)(0.01) = 0.09882\,\text{rad}$

Nghiệm giải tích: $\theta(0.03) = 0.1\cos(6.264 \times 0.03) = 0.1\cos(0.1879) = 0.1 \times 0.9824 = 0.09824\,\text{rad}$. Sai số Euler: $(0.09882 - 0.09824)/0.09824 = 0.59\%$ — chấp nhận được.

---

**Điểm mấu chốt:**

- Phương pháp Euler: đơn giản nhưng tích lũy sai số bậc $O(h)$.
- Leap-frog: bảo toàn năng lượng tốt hơn, phù hợp mô phỏng dao động dài hạn.
- Tiêu chí chọn bước: $h \leq T_{min}/20$ để cân bằng chính xác và tốc độ tính toán.
- Mọi bộ mô phỏng cơ học số, từ CAD/FEA đến firmware điều khiển, đều là biểu hiện của nguyên lý này.


---
*Exported from Feynman Bot*
