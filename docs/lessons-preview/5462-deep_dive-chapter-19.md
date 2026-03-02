---
lesson_id: 5462
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-02T15:10:30.043795+00:00"
content_hash: f7021792b1ec
chapter_number: 19
chapter_title: Chapter 19
section_number: 5
section_title: 19–4Rotational kinetic energy
---
# ## Động Năng Quay và Bảo Toàn Moment Động Lượng — Phân tích Chuyên sâu

*Source: Chapter 19 - Chapter 19 (Section 5) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_19.html)*

## Động Năng Quay và Bảo Toàn Moment Động Lượng — Phân tích Chuyên sâu

### 1. Suy Dẫn Động Năng Quay Từ Nguyên Lý Đầu

Xét vật thể cứng (rigid body) quay với vận tốc góc $\omega$ quanh trục cố định. Hệ gồm $N$ phần tử khối lượng $m_i$ tại khoảng cách $r_i$ từ trục. Vận tốc dài của phần tử $i$:

$$v_i = \omega r_i$$

Tổng động năng:

$$T = \sum_{i=1}^N \frac{1}{2}m_i v_i^2 = \sum_{i=1}^N \frac{1}{2}m_i (\omega r_i)^2 = \frac{1}{2}\omega^2 \underbrace{\sum_{i=1}^N m_i r_i^2}_{\equiv I}$$

$$\boxed{T = \frac{1}{2}I\omega^2}$$

Moment quán tính $I = \sum m_i r_i^2$ (hoặc $I = \int r^2\,dm$ cho vật liên tục) không phụ thuộc $\omega$ — đây là tính chất hình học-khối lượng thuần túy của vật thể.

### 2. Công Thức Moment Quán Tính Cho Các Hình Dạng Thông Dụng

| Hình dạng | Trục quay | $I$ |
|---|---|---|
| Trụ đặc (R) | Tâm | $\frac{1}{2}MR^2$ |
| Trụ rỗng ($R_1, R_2$) | Tâm | $\frac{1}{2}M(R_1^2+R_2^2)$ |
| Cầu đặc (R) | Đường kính | $\frac{2}{5}MR^2$ |
| Thanh dài (L) | Trung điểm, vuông góc | $\frac{1}{12}ML^2$ |
| Thanh dài (L) | Đầu mút, vuông góc | $\frac{1}{3}ML^2$ |

### 3. Moment Động Lượng và Định Luật Newton Dạng Quay

Moment động lượng:

$$L = I\omega$$

Phương trình Newton dạng quay:

$$\tau = \frac{dL}{dt} = I\frac{d\omega}{dt} = I\alpha$$

Khi $\tau_{\text{ext}} = 0$: $\dfrac{dL}{dt} = 0 \Rightarrow L = \text{const} \Rightarrow I_1\omega_1 = I_2\omega_2$.

### 4. Phân Tích Năng Lượng Khi Moment Quán Tính Thay Đổi

Khảo sát bảo toàn moment động lượng khi $I$ thay đổi từ $I_1$ sang $I_2$ (không có torque ngoài, ví dụ: vận động viên thu tay):

$$I_1\omega_1 = I_2\omega_2 \Rightarrow \omega_2 = \frac{I_1}{I_2}\omega_1$$

Động năng ban đầu và sau:

$$T_1 = \frac{1}{2}I_1\omega_1^2, \quad T_2 = \frac{1}{2}I_2\omega_2^2 = \frac{1}{2}I_2\left(\frac{I_1}{I_2}\right)^2\omega_1^2 = \frac{I_1^2\omega_1^2}{2I_2} = \frac{L^2}{2I_2}$$

Tỷ số: $\dfrac{T_2}{T_1} = \dfrac{I_1}{I_2}$. Nếu $I_2 < I_1$ (thu vào), $T_2 > T_1$: động năng tăng! Năng lượng này đến từ **công cơ học** do cơ bắp (hoặc cơ cấu) thực hiện khi dịch chuyển khối lượng vào gần trục — không vi phạm bảo toàn năng lượng.

### 5. Ứng Dụng Thực Tế: Hệ Servo và Đo Lường Chính Xác

**Ly hợp điện từ (electromagnetic clutch) trong máy đo CMM:** Khi đầu đo quay (rotary probe) cần chuyển từ tốc độ quét nhanh sang dừng đột ngột, ly hợp kích hoạt. Hai đĩa có $I_1, \omega_1$ và $I_2 = 0, \omega_2 = 0$ kết hợp lại:

$$\omega_f = \frac{I_1\omega_1 + 0}{I_1 + I_2} = \frac{I_1\omega_1}{I_1 + I_2}$$

Năng lượng nhiệt tỏa ra trong ly hợp:

$$\Delta E = T_1 - T_f = \frac{1}{2}I_1\omega_1^2 - \frac{1}{2}(I_1+I_2)\omega_f^2 = \frac{I_1 I_2 \omega_1^2}{2(I_1+I_2)}$$

Thông số $\Delta E$ quyết định yêu cầu tản nhiệt cho ly hợp.

**Con quay hồi chuyển MEMS trong hệ IMU:** Trong IMU (Inertial Measurement Unit) dùng cho drone quân sự hoặc đạn dẫn đường thông minh, MEMS gyroscope không dùng rotor quay cơ học mà dùng nguyên lý Coriolis — nhưng phân tích moment động lượng vẫn là nền tảng hiệu chỉnh (calibration). Noise floor của MEMS gyro hiện đại: ~$0.003\,°/\sqrt{\text{hr}}$, tương đương sai lệch vị trí ~$0.5\,\text{m}$ sau 1 giờ bay.

### 6. Bài Toán Mẫu: Servo Drive Với Tải Thay Đổi Moment Quán Tính

**Đề bài:** Một servo motor điều khiển cánh tay robot. Ban đầu cánh tay duỗi thẳng, $I_1 = 0.08\,\text{kg·m}^2$, quay với $\omega_1 = 10\,\text{rad/s}$. Cánh tay thu lại, $I_2 = 0.02\,\text{kg·m}^2$. Giả sử không có torque ngoài trong thời gian chuyển tiếp:

a) Tính $\omega_2$.
b) Tính sự thay đổi động năng.
c) Nếu motor cần duy trì $\omega_2 = \omega_1 = 10\,\text{rad/s}$ (không cho tăng tốc), motor phải tạo torque hãm bao nhiêu để hấp thụ năng lượng dư?

**Lời giải:**

a) Bảo toàn $L$:
$$\omega_2 = \frac{I_1\omega_1}{I_2} = \frac{0.08 \times 10}{0.02} = 40\,\text{rad/s}$$

b) Thay đổi động năng:
$$T_1 = \frac{1}{2}(0.08)(10^2) = 4\,\text{J}$$
$$T_2 = \frac{1}{2}(0.02)(40^2) = 16\,\text{J}$$
$$\Delta T = +12\,\text{J} \text{ (năng lượng do cơ cấu thu tay thực hiện công)}$$

c) Nếu muốn duy trì $\omega = 10\,\text{rad/s}$ sau khi $I$ giảm còn $I_2 = 0.02$:
- Năng lượng cần thoát: $T_2(\omega=10) = \frac{1}{2}(0.02)(10^2) = 1\,\text{J}$
- Thực ra, năng lượng dư từ việc thu tay ($+12\,\text{J}$) cần được hấp thụ bởi motor (tái sinh - regenerative braking)
- Moment hãm trung bình nếu quá trình thu tay mất $\Delta t = 0.1\,\text{s}$:
$$\tau_{\text{hãm}} = \frac{\Delta E / \Delta t}{\omega_{\text{tb}}} \approx \frac{12/0.1}{25} = 4.8\,\text{N·m}$$

**Ý nghĩa kỹ thuật:** Trong robot công nghiệp, hiện tượng này gọi là "inertia mismatch" — khi $I$ thay đổi đột ngột, bộ điều khiển PID cần thích nghi nhanh. Các hệ cao cấp dùng thuật toán feedforward với model $I(\theta)$ theo góc khớp để bù trước, đạt độ chính xác vị trí ở cấp độ arcsecond (tương đương vài micromet ở đầu cánh tay dài 1m).

---
*Exported from Feynman Bot*
