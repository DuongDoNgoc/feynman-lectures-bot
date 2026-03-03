---
lesson_id: 5450
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:05.338269+00:00"
content_hash: b6a7ff0f9082
chapter_number: 18
chapter_title: Chapter 18
section_number: 1
section_title: 18Rotation in Two Dimensions
---
# ## Động Lực Học Vật Rắn và Chuyển Động Quay — Phân tích Chuyên sâu

*Source: Chapter 18 - Chapter 18 (Section 1) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_18.html)*

## Động Lực Học Vật Rắn và Chuyển Động Quay — Phân tích Chuyên sâu

### 1. Từ Newton's Laws cho Điểm đến Vật Rắn

Khi xét một hệ gồm nhiều hạt, Newton's law cho từng hạt $i$:
$$\vec{F}_i = \frac{d^2(m_i \vec{r}_i)}{dt^2}$$

Lấy tổng trên toàn bộ hệ:
$$\vec{F}_{\text{ext}} = \sum_i \vec{F}_i = \frac{d^2}{dt^2}\sum_i m_i \vec{r}_i$$

Nội lực triệt tiêu theo Newton 3, chỉ còn ngoại lực. Định nghĩa tổng khối lượng $M = \sum_i m_i$ và vị trí trung tâm khối:
$$\vec{R}_{\text{CM}} = \frac{\sum_i m_i \vec{r}_i}{M}$$

Phương trình chuyển động của vật rắn chia thành hai phần độc lập:
- **Tịnh tiến:** $\vec{F}_{\text{ext}} = M\vec{a}_{\text{CM}}$
- **Quay:** $\vec{\tau}_{\text{ext}} = \frac{d\vec{L}}{dt}$

Đây là nền tảng để phân tích mọi chuyển động của vật rắn.

### 2. Chuyển Động Quay Phẳng (Plane Rotation)

Xét vật rắn quay quanh trục cố định. Mỗi phần tử khối lượng $\Delta m_i$ ở bán kính $r_i$:
- Vận tốc: $v_i = r_i \omega$ (tất cả cùng $\omega$)
- Động năng quay: $\frac{1}{2}\Delta m_i v_i^2 = \frac{1}{2}\Delta m_i r_i^2 \omega^2$

Tổng động năng quay:
$$K_{\text{rot}} = \frac{1}{2}\left(\sum_i \Delta m_i r_i^2\right)\omega^2 = \frac{1}{2}I\omega^2$$

trong đó **moment quán tính**:
$$I = \sum_i m_i r_i^2 = \int r^2 \, dm$$

Phương trình động lực học quay:
$$\tau = I\alpha \quad \text{với } \alpha = \frac{d\omega}{dt}$$

Song song hoàn toàn với $F = ma$ trong chuyển động tịnh tiến.

### 3. Tính Moment Quán Tính cho Các Hình Dạng Phổ Biến

**Đĩa đặc** (solid disk) bán kính $R$, khối lượng $M$:
$$I_{\text{disk}} = \frac{1}{2}MR^2$$

**Vòng** (thin ring) bán kính $R$:
$$I_{\text{ring}} = MR^2$$

**Thanh** (rod) dài $L$ quay quanh tâm:
$$I_{\text{rod}} = \frac{1}{12}ML^2$$

Nhận xét kỹ thuật: $I_{\text{ring}} = 2 I_{\text{disk}}$ với cùng $M$ và $R$. Vành bánh đà (flywheel rim) tích năng lượng hiệu quả hơn đĩa đặc gấp đôi — đây là lý do flywheel trong UPS (uninterruptible power supply) và energy storage systems luôn thiết kế khối lượng tập trung ở ngoài.

### 4. Định Lý Steiner (Parallel Axis Theorem)

Nếu biết $I_{\text{CM}}$ quanh trục qua tâm khối, moment quán tính quanh trục song song cách $d$:
$$I = I_{\text{CM}} + Md^2$$

**Ý nghĩa vật lý:** Dịch chuyển trục quay làm tăng $I$ — vật khó quay hơn. Ứng dụng trực tiếp trong thiết kế robot arm: khi robot arm duỗi ra (tăng $d$ của payload so với joint), moment quán tính tăng theo $Md^2$, motor cần mô-men xoắn lớn hơn để đạt cùng gia tốc góc.

### 5. Năng Lượng Quay và Bảo Toàn

Tương tự động lượng tịnh tiến $\vec{p} = M\vec{v}$, **angular momentum**:
$$L = I\omega$$

Bảo toàn angular momentum khi $\tau_{\text{ext}} = 0$: vũ công ballet kéo tay vào người (giảm $I$) sẽ quay nhanh hơn (tăng $\omega$) để giữ $L = I\omega = \text{const}$.

### 6. Ví Dụ Thực Tế: Motor Servo trong Robot Hàn Micrometer

Xét joint robot hàn laser với:
- Motor rotor: đĩa thép, $M_r = 0.5$ kg, $R_r = 3$ cm
- Gear reducer: tỉ số $n = 100:1$
- Arm: thanh nhôm, $M_a = 2$ kg, $L_a = 40$ cm
- Payload (đầu hàn): $M_p = 0.3$ kg ở đầu arm

**Tính $I$ quy về trục motor:**

$I_{\text{rotor}} = \frac{1}{2}(0.5)(0.03)^2 = 2.25 \times 10^{-4}$ kg·m²

$I_{\text{arm}}$ (thanh quay quanh một đầu) $= \frac{1}{3}M_a L_a^2 = \frac{1}{3}(2)(0.4)^2 = 0.107$ kg·m²

$I_{\text{payload}} = M_p L_a^2 = (0.3)(0.4)^2 = 0.048$ kg·m²

Quy về trục motor qua gear ratio $n$:
$$I_{\text{total,motor}} = I_{\text{rotor}} + \frac{I_{\text{arm}} + I_{\text{payload}}}{n^2}$$
$$= 2.25\times10^{-4} + \frac{0.107 + 0.048}{100^2} = 2.25\times10^{-4} + 1.55\times10^{-5} = 2.4\times10^{-4} \text{ kg·m}^2$$

Để đạt gia tốc góc $\alpha_{\text{motor}} = 1000$ rad/s² (tương ứng $\alpha_{\text{joint}} = 10$ rad/s²):
$$\tau_{\text{motor}} = I_{\text{total}} \cdot \alpha = 2.4\times10^{-4} \times 1000 = 0.24 \text{ N·m}$$

Đây là mô-men xoắn motor cần đạt — thông số chọn motor.

### 7. Bài Tập Mẫu: Bánh Đà trong Hệ Tích Trữ Năng Lượng

**Bài toán:** Một bánh đà vành thép (thin ring) có $M = 50$ kg, $R = 0.5$ m, quay ở $\omega_0 = 3000$ RPM. Tính: (a) Động năng tích trữ, (b) Mô-men xoắn cần để hãm dừng trong $t = 30$ s.

**Bước 1:** Đổi đơn vị.
$$\omega_0 = 3000 \times \frac{2\pi}{60} = 100\pi \approx 314.16 \text{ rad/s}$$

**Bước 2:** Moment quán tính (vành tròn).
$$I = MR^2 = 50 \times (0.5)^2 = 12.5 \text{ kg·m}^2$$

*Ý nghĩa:* $I = 12.5$ kg·m² có nghĩa là vật phân bố khối lượng tương đương như thể tất cả 50 kg đặt ở bán kính 0.5 m — tối ưu cho tích trữ năng lượng.

**Bước 3:** Động năng tích trữ.
$$K = \frac{1}{2}I\omega^2 = \frac{1}{2}(12.5)(314.16)^2 = 617{,}000 \text{ J} \approx 617 \text{ kJ}$$

*Ý nghĩa:* 617 kJ đủ để cấp điện cho tải 6 kW trong khoảng 103 giây — đây là nguyên lý UPS flywheel.

**Bước 4:** Gia tốc góc khi hãm.
$$\alpha = \frac{\Delta\omega}{\Delta t} = \frac{0 - 314.16}{30} = -10.47 \text{ rad/s}^2$$

**Bước 5:** Mô-men xoắn hãm.
$$|\tau| = I|\alpha| = 12.5 \times 10.47 = 130.9 \text{ N·m}$$

*Ý nghĩa:* Hệ thống hãm (electromagnetic brake) cần cung cấp ít nhất 131 N·m mô-men xoắn liên tục trong 30 giây để dừng bánh đà an toàn.

### 8. Liên Hệ: Gyroscope trong Hệ Dẫn Đường Quán Tính

Within dẫn đường quán tính (INS) của tên lửa hành trình, ring laser gyroscope (RLG) đo $\omega$ quanh ba trục. Tuy nhiên, cụm cơ khí gá lắp (gimbal assembly) có moment quán tính $I_{\text{gimbal}}$ nhất định. Bất kỳ rung động cơ học nào (từ động cơ tên lửa) gây ra $\tau_{\text{disturb}}$ sẽ tạo ra $\alpha = \tau/I$ — sai số góc tích phân theo thời gian thành sai số vị trí. Kỹ sư thiết kế tối ưu hóa $I$ của gimbal để giảm nhạy cảm với rung động trong dải tần nguy hiểm.

---
*Exported from Feynman Bot*
