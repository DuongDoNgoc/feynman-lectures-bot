---
lesson_id: 5453
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:05.398985+00:00"
content_hash: 252272cc70b6
chapter_number: 18
chapter_title: Chapter 18
section_number: 4
section_title: 18–3Angular momentum
---
# ## Moment Động Lượng và Định Luật Bảo Toàn — Phân tích Chuyên sâu

*Source: Chapter 18 - Chapter 18 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_18.html)*

## Moment Động Lượng và Định Luật Bảo Toàn — Phân tích Chuyên sâu

### 1. Từ Lực-Động Lượng đến Mô-men Xoắn-Moment Động Lượng

Feynman mở đầu với quan sát sâu sắc: nếu lực là tốc độ thay đổi động lượng, liệu có một đại lượng "xoắn" nào là tốc độ thay đổi của một đại lượng "moment" tương tự? Câu trả lời là có, và chứng minh xuất phát trực tiếp từ Newton's laws.

Xét hạt khối lượng $m$ tại tọa độ $(x, y)$, chịu lực $(F_x, F_y)$. **Mô-men xoắn** (torque) đối với trục $O$ qua gốc:
$$\tau = xF_y - yF_x$$

Thay Newton's second law $F_x = m\ddot{x}$, $F_y = m\ddot{y}$:
$$\tau = m(x\ddot{y} - y\ddot{x})$$

Bây giờ xét đạo hàm của $L = m(x\dot{y} - y\dot{x})$:
$$\frac{dL}{dt} = m(\dot{x}\dot{y} + x\ddot{y} - \dot{y}\dot{x} - y\ddot{x}) = m(x\ddot{y} - y\ddot{x}) = \tau$$

Vậy ta chứng minh được:
$$\tau = \frac{dL}{dt}$$

Đây không phải định nghĩa — đây là định lý, hệ quả tất yếu của Newton's laws.

### 2. Mở Rộng cho Hệ Nhiều Hạt

Với hệ $N$ hạt, lực tác dụng lên hạt $i$ gồm:
- Ngoại lực $\vec{F}_i^{\text{ext}}$ từ bên ngoài
- Nội lực $\vec{F}_{ij}$ từ hạt $j$ tác dụng lên $i$

Mô-men xoắn tổng hợp:
$$\tau_{\text{total}} = \sum_i \tau_i^{\text{ext}} + \sum_{i\neq j} \tau_{ij}$$

**Định lý:** Tổng mô-men xoắn nội lực bằng không.

Chứng minh: Theo Newton 3, $\vec{F}_{ij} = -\vec{F}_{ji}$. Mô-men xoắn của cặp:
$$\tau_{ij} + \tau_{ji} = \vec{r}_i \times \vec{F}_{ij} + \vec{r}_j \times \vec{F}_{ji} = (\vec{r}_i - \vec{r}_j) \times \vec{F}_{ij}$$

Nếu lực nội lực dọc theo đường nối hai hạt (central forces — đúng với hầu hết lực trong tự nhiên): $(\vec{r}_i - \vec{r}_j) \parallel \vec{F}_{ij}$, tích có hướng bằng không.

Kết quả: **chỉ mô-men xoắn ngoại lực mới thay đổi moment động lượng tổng**:
$$\tau_{\text{ext}} = \frac{dL_{\text{total}}}{dt}$$

Và nếu $\tau_{\text{ext}} = 0$: $L_{\text{total}} = \text{const}$ — **bảo toàn moment động lượng**.

### 3. Ba Công Thức Tương Đương cho Angular Momentum

Với hạt chuyển động trong mặt phẳng:

$$L = xp_y - yp_x$$

Nếu quỹ đạo tròn bán kính $r$, động lượng tiếp tuyến $p_{\text{tang}}$:
$$L = rp_{\text{tang}}$$

Tổng quát — cánh tay đòn động lượng (perpendicular distance):
$$L = p \cdot d_{\perp}$$

trong đó $d_{\perp}$ là khoảng cách vuông góc từ trục đến đường thẳng chứa vector vận tốc.

### 4. Ví Dụ Thực Tế: Momentum Wheel trong Attitude Control Vệ Tinh

Vệ tinh quan sát Trái Đất cần điều chỉnh hướng (attitude control) với độ chính xác góc milli-radian, không thể dùng thruster liên tục (tốn nhiên liệu). Giải pháp: **reaction wheel** hay **momentum wheel** — bánh đà điện từ bên trong vệ tinh.

**Nguyên lý:** Toàn bộ hệ vệ tinh + bánh đà không có mô-men xoắn ngoại tác trong không gian (bỏ qua gravity gradient):
$$L_{\text{total}} = L_{\text{satellite}} + L_{\text{wheel}} = \text{const}$$

Khi motor quay bánh đà theo chiều dương với $\Delta L_{\text{wheel}} > 0$, vỏ vệ tinh phải quay theo chiều âm:
$$\Delta L_{\text{satellite}} = -\Delta L_{\text{wheel}}$$

Thay đổi $\omega_{\text{satellite}}$:
$$I_{\text{sat}} \Delta\omega_{\text{sat}} = -I_{\text{wheel}} \Delta\omega_{\text{wheel}}$$

**Tính toán cụ thể:**
- Vệ tinh: $I_{\text{sat}} = 100$ kg·m², cần xoay $\theta = 5°$ trong $t = 10$ s
- $\omega_{\text{sat}} = \theta/t_{\text{ramp}}$ (trapezoidal profile)
- $\Delta\omega_{\text{wheel}}$ cần thiết: $100 \times \omega_{\text{sat}} / I_{\text{wheel}}$

Nếu $I_{\text{wheel}} = 0.5$ kg·m², $\omega_{\text{sat}} = 0.087$ rad/s:
$$\Delta\omega_{\text{wheel}} = 100 \times 0.087 / 0.5 = 17.4 \text{ rad/s} \approx 166 \text{ RPM}$$

Đây là thay đổi tốc độ bánh đà cần thiết — hoàn toàn trong tầm của motor DC nhỏ.

### 5. Ứng Dụng Khác: Precession của Gyroscope

Khi gyroscope có $L = I\omega$ lớn, chịu mô-men xoắn ngoại tác $\tau$ (ví dụ trọng lực), moment động lượng **tiến động** (precess) theo:
$$\vec{\tau} = \frac{d\vec{L}}{dt} = \vec{\Omega}_{\text{prec}} \times \vec{L}$$

Tốc độ tiến động:
$$\Omega_{\text{prec}} = \frac{\tau}{L} = \frac{\tau}{I\omega}$$

Đây là nguyên lý Mechanical Gyroscope trong INS: $L$ lớn $\Rightarrow$ $\Omega_{\text{prec}}$ nhỏ $\Rightarrow$ gyroscope "cứng" trong không gian, ít bị ảnh hưởng bởi nhiễu động.

### 6. Bài Tập Mẫu: Tính Angular Momentum của Hệ Robot

**Bài toán:** Robot arm gồm:
- Link 1: thanh đồng nhất, $M_1 = 3$ kg, $L_1 = 0.5$ m, quay quanh đầu gốc với $\omega_1 = 2$ rad/s
- Khớp 1 ở gốc, Link 2: $M_2 = 1$ kg coi là hạt điểm ở đầu Link 1

Tính angular momentum tổng đối với trục qua gốc, vuông góc mặt phẳng quay.

**Bước 1:** Moment quán tính Link 1 (thanh quay quanh một đầu).
$$I_1 = \frac{1}{3}M_1 L_1^2 = \frac{1}{3}(3)(0.5)^2 = 0.25 \text{ kg·m}^2$$

*Ý nghĩa:* Hệ số 1/3 (không phải 1/2) vì quay quanh đầu, không quanh tâm.

**Bước 2:** Moment quán tính Link 2 (hạt điểm ở $r = L_1 = 0.5$ m).
$$I_2 = M_2 L_1^2 = (1)(0.5)^2 = 0.25 \text{ kg·m}^2$$

**Bước 3:** Tổng moment quán tính.
$$I_{\text{total}} = I_1 + I_2 = 0.25 + 0.25 = 0.5 \text{ kg·m}^2$$

**Bước 4:** Angular momentum.
$$L = I_{\text{total}} \cdot \omega_1 = 0.5 \times 2 = 1.0 \text{ kg·m}^2/\text{s}$$

*Ý nghĩa:* Để dừng robot arm này trong $\Delta t = 0.1$ s, cần mô-men xoắn hãm:
$$\tau = \Delta L / \Delta t = 1.0 / 0.1 = 10 \text{ N·m}$$

Đây là thông số tối thiểu cho brake system.

**Bước 5:** Kiểm tra bằng năng lượng.
$$K = \frac{1}{2}I\omega^2 = \frac{1}{2}(0.5)(2)^2 = 1.0 \text{ J}$$

Nếu hãm trong 0.1 s: công suất hãm $P = K/t = 10$ W — nhất quán với $P = \tau \cdot \omega = 10 \times 2 = 20$ W (trung bình 10 W, hợp lý khi $\omega$ giảm từ 2 về 0).

### 7. Liên Hệ: Encoder Absolute vs. Incremental

Khi đo vị trí góc trong hệ thống servo độ chính xác cao, encoder absolute cho biết $\theta$ tuyệt đối ngay khi bật nguồn, còn encoder incremental chỉ đo $\Delta\theta$. Tốc độ $\omega = d\theta/dt$ tính từ xung encoder. Angular momentum $L = I\omega$ được tính real-time trong firmware điều khiển, làm cơ sở cho feedforward control — bù mô-men xoắn cần thiết trước khi sai số xuất hiện, thay vì chờ feedback.

---
*Exported from Feynman Bot*
