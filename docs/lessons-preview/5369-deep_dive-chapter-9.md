---
lesson_id: 5369
lesson_type: deep_dive
approval_status: pending
exported_at: "2026-02-28T14:08:59.887167+00:00"
content_hash: a9d60c477844
chapter_number: 9
chapter_title: Chapter 9
section_number: 1
section_title: 9Newton’s Laws of Dynamics
---
# ## Các Định Luật Động Lực Học Newton — Phân tích Chuyên sâu

*Source: Chapter 9 - Chapter 9 (Section 1) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_09.html)*

## Các Định Luật Động Lực Học Newton — Phân tích Chuyên sâu

### Phương trình vi phân của chuyển động

Định luật II Newton $\mathbf{F} = m\mathbf{a}$ là phương trình vi phân bậc 2:

$$m\frac{d^2\mathbf{r}}{dt^2} = \mathbf{F}(\mathbf{r}, \dot{\mathbf{r}}, t)$$

trong đó $\mathbf{r} = (x, y, z)$ là vectơ vị trí, $\dot{\mathbf{r}} = d\mathbf{r}/dt$ là vận tốc. Lực có thể phụ thuộc vào vị trí (lò xo), vận tốc (ma sát nhớt), thời gian (ngoại lực), hoặc tổ hợp cả ba.

**Tách thành 3 phương trình độc lập:**

$$m\ddot{x} = F_x(x, y, z, \dot{x}, \dot{y}, \dot{z}, t)$$
$$m\ddot{y} = F_y(x, y, z, \dot{x}, \dot{y}, \dot{z}, t)$$
$$m\ddot{z} = F_z(x, y, z, \dot{x}, \dot{y}, \dot{z}, t)$$

---

### Ví dụ thực tế: Hệ thống dẫn đường quán tính (INS) trong tên lửa

**Mô hình đơn giản hóa (1D):**

Tên lửa có khối lượng $m(t)$ thay đổi do tiêu hao nhiên liệu. Lực đẩy $F_{thrust}$ và lực cản không khí $F_{drag} = -kv^2$:

$$m(t)\frac{dv}{dt} = F_{thrust} - kv^2 - m(t)g$$

Đây là phương trình Newton cho chuyển động thẳng đứng. Vì $m(t)$ thay đổi, không có nghiệm giải tích đơn giản — phải giải số.

**Giải số bằng phương pháp Euler cải tiến (Heun):**

$$k_1 = \frac{F(t_n, v_n)}{m(t_n)}$$
$$k_2 = \frac{F(t_n + h, v_n + h\cdot k_1)}{m(t_n + h)}$$
$$v_{n+1} = v_n + \frac{h}{2}(k_1 + k_2)$$

Phương pháp này có sai số $O(h^2)$ thay vì $O(h)$ của Euler thuần, giảm đáng kể sai số tích lũy trong mô phỏng quỹ đạo dài.

---

### Ứng dụng: Lực giật (Recoil) trong súng

**Bài toán:** Súng bộ binh bắn đạn khối lượng $m = 7.9\,\text{g}$ với vận tốc đầu nòng $v_0 = 900\,\text{m/s}$ trong thời gian $t_0 = 1.5\,\text{ms}$. Khối lượng súng $M = 3.5\,\text{kg}$.

**Phân tích bằng định luật III Newton:**

Lực trung bình tác dụng lên đạn:

$$F_{avg} = \frac{m \cdot v_0}{t_0} = \frac{0.0079 \times 900}{0.0015} = 4740\,\text{N}$$

Theo định luật III, súng chịu lực ngược chiều tương đương 4740 N trong 1.5 ms. Gia tốc giật của súng:

$$a_{recoil} = \frac{F_{avg}}{M} = \frac{4740}{3.5} = 1354\,\text{m/s}^2$$

Vận tốc giật ban đầu của súng:

$$V_{recoil} = a_{recoil} \times t_0 = 1354 \times 0.0015 = 2.03\,\text{m/s}$$

(Kiểm tra bằng bảo toàn động lượng: $M \cdot V = m \cdot v_0 \Rightarrow V = 0.0079 \times 900 / 3.5 = 2.03\,\text{m/s}$ ✓)

Thiết kế bộ giảm giật (recoil buffer) cần hấp thụ năng lượng $E = \frac{1}{2}MV^2 = \frac{1}{2}(3.5)(2.03)^2 = 7.2\,\text{J}$ trong hành trình ~50 mm.

---

### Bài tập có lời giải

**Bài toán:** Đầu đo CMM có khối lượng $m = 0.5\,\text{kg}$ chịu lực đàn hồi từ lò xo $F = -k(x - x_0)$ với $k = 200\,\text{N/m}$, $x_0 = 0$ (vị trí cân bằng), và lực cản nhớt $F_{damp} = -c\dot{x}$ với $c = 2\,\text{N·s/m}$.

(a) Viết phương trình vi phân chuyển động.
(b) Tính tần số tự nhiên $\omega_n$ và tỉ số tắt dần $\zeta$.
(c) Nhận xét về ảnh hưởng đến độ chính xác đo.

**Lời giải:**

(a) $m\ddot{x} = -kx - c\dot{x}$, hay: $0.5\ddot{x} + 2\dot{x} + 200x = 0$.

(b)

$$\omega_n = \sqrt{\frac{k}{m}} = \sqrt{\frac{200}{0.5}} = 20\,\text{rad/s} \approx 3.18\,\text{Hz}$$

$$\zeta = \frac{c}{2\sqrt{km}} = \frac{2}{2\sqrt{200 \times 0.5}} = \frac{2}{2 \times 10} = 0.1$$

(c) $\zeta = 0.1$ là underdamped — đầu đo sẽ dao động ~3 Hz khi chạm vào bề mặt. Thời gian tắt dần $\tau = 1/(\zeta\omega_n) = 1/(0.1 \times 20) = 0.5\,\text{s}$. Hệ thống đo cần chờ ít nhất $3\tau = 1.5\,\text{s}$ để ổn định trước khi ghi số — điều này ảnh hưởng trực tiếp đến năng suất đo.

---

**Điểm mấu chốt:**

- Định luật Newton II là phương trình vi phân bậc 2 — nghiệm phụ thuộc vào điều kiện đầu và dạng lực.
- Lực phụ thuộc vị trí (lò xo) → dao động; phụ thuộc vận tốc (ma sát) → tắt dần.
- Phương pháp số (Euler, Heun, RK4) cho phép giải bất kỳ hệ $F = ma$ nào khi không có nghiệm giải tích.
- Trong thiết kế cơ khí chính xác, tần số tự nhiên và tỉ số tắt dần quyết định thời gian ổn định và do đó tốc độ đo.


---
*Exported from Feynman Bot*
