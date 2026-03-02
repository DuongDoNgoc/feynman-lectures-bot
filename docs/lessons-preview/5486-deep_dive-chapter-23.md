---
lesson_id: 5486
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-02T15:10:30.807628+00:00"
content_hash: 527a5e51dbd8
chapter_number: 23
chapter_title: Chapter 23
section_number: 2
section_title: 23–1Complex numbers and harmonic motion
---
# ## Dao động Điều hòa Cưỡng bức — Phân tích Chuyên sâu bằng Số Phức

*Source: Chapter 23 - Chapter 23 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_23.html)*

## Dao động Điều hòa Cưỡng bức — Phân tích Chuyên sâu bằng Số Phức

### Mục tiêu: Giải phương trình vi phân bằng đại số phức

Phương trình dao động cưỡng bức là bài toán cốt lõi của mọi hệ cơ học dao động — từ hệ thống giảm rung trong xe thiết giáp đến bộ ổn định quang học trong kính ngắm laser:
$$\frac{d^2x}{dt^2} + \frac{k}{m}x = \frac{F_0}{m}\cos\omega t$$

Ký hiệu $\omega_0^2 = k/m$ (tần số tự nhiên). Phương trình trở thành:
$$\ddot{x} + \omega_0^2 x = \frac{F_0}{m}\cos\omega t$$

Giải trực tiếp bằng phép thử nghiệm hàm $x = A\cos\omega t + B\sin\omega t$ cần thao tác lượng giác rườm rà. Phương pháp số phức cho lời giải thanh lịch hơn nhiều.

### Bước 1: Biểu diễn số phức của lực cưỡng bức

Vì $\cos\omega t = \text{Re}\{e^{i\omega t}\}$, ta thay bài toán thực bằng bài toán phức:
$$\ddot{\hat{x}} + \omega_0^2 \hat{x} = \frac{F_0}{m}e^{i\omega t}$$

Nghiệm thực $x(t) = \text{Re}\{\hat{x}(t)\}$.

*Ý nghĩa:* Phương trình với $e^{i\omega t}$ ở vế phải dễ giải hơn vì $e^{i\omega t}$ là hàm riêng của toán tử đạo hàm.

### Bước 2: Giả sử dạng nghiệm

Ta thử nghiệm: $\hat{x}(t) = \hat{C} e^{i\omega t}$, trong đó $\hat{C}$ là số phức cần tìm (chứa biên độ và pha).

Tính đạo hàm:
$$\dot{\hat{x}} = i\omega \hat{C} e^{i\omega t}$$
$$\ddot{\hat{x}} = (i\omega)^2 \hat{C} e^{i\omega t} = -\omega^2 \hat{C} e^{i\omega t}$$

*Ý nghĩa:* Phép đạo hàm biến thành phép nhân với $i\omega$ — đây là lý do hàm mũ phức cực kỳ mạnh mẽ trong phân tích hệ tuyến tính.

### Bước 3: Thay vào phương trình

Thay $\hat{x} = \hat{C}e^{i\omega t}$ và $\ddot{\hat{x}} = -\omega^2 \hat{C}e^{i\omega t}$:
$$-\omega^2 \hat{C} e^{i\omega t} + \omega_0^2 \hat{C} e^{i\omega t} = \frac{F_0}{m}e^{i\omega t}$$

Hủy $e^{i\omega t} \neq 0$ hai vế:
$$\hat{C}(\omega_0^2 - \omega^2) = \frac{F_0}{m}$$

$$\boxed{\hat{C} = \frac{F_0/m}{\omega_0^2 - \omega^2}}$$

*Ý nghĩa:* Đây là số thực! (Không có phần ảo.) Điều này có nghĩa nghiệm ổn định đồng pha với lực khi $\omega < \omega_0$ và ngược pha 180° khi $\omega > \omega_0$.

### Bước 4: Nghiệm thực và phân tích

$$x(t) = \text{Re}\{\hat{C} e^{i\omega t}\} = \hat{C} \cos\omega t = \frac{F_0/m}{\omega_0^2 - \omega^2} \cos\omega t$$

**Trường hợp cộng hưởng $\omega \to \omega_0$:**
Mẫu số $\omega_0^2 - \omega^2 \to 0$, biên độ $|\hat{C}| \to \infty$. Trong thực tế (có lực cản), biên độ rất lớn nhưng hữu hạn — đây là cộng hưởng (resonance).

### Bước 5: Hàm truyền tần số (Frequency Response Function)

Tỉ số phasor đáp ứng trên phasor lực:
$$H(\omega) = \frac{\hat{C}}{F_0/m} = \frac{1}{\omega_0^2 - \omega^2}$$

Trong trường hợp có lực cản (damping coefficient $\gamma$), phương trình đầy đủ:
$$\ddot{x} + \gamma\dot{x} + \omega_0^2 x = \frac{F_0}{m}e^{i\omega t}$$

Thay $\hat{x} = \hat{C}e^{i\omega t}$:
$$(-\omega^2 + i\gamma\omega + \omega_0^2)\hat{C} = \frac{F_0}{m}$$

$$\hat{C} = \frac{F_0/m}{(\omega_0^2 - \omega^2) + i\gamma\omega}$$

Đây là **số phức thực sự**! Biên độ:
$$|\hat{C}| = \frac{F_0/m}{\sqrt{(\omega_0^2-\omega^2)^2 + \gamma^2\omega^2}}$$

Góc pha:
$$\phi = -\arctan\frac{\gamma\omega}{\omega_0^2-\omega^2}$$

### Ví dụ thực tế: Ổn định quang học trong kính ngắm laser

Kính ngắm laser trên xe thiết giáp M1A2 Abrams có hệ thống ổn định con quay để duy trì hướng nhắm khi xe chạy địa hình gồ ghề. Bệ kính ngắm là hệ dao động cưỡng bức với:
- Khối lượng hệ quang học: $m = 2.5$ kg
- Độ cứng lò xo kết cấu: $k = 1000$ N/m → $\omega_0 = \sqrt{k/m} = 20$ rad/s ≈ 3.18 Hz
- Hệ số cản: $\gamma = 8$ rad/s (tỉ số cản $\zeta = \gamma/(2\omega_0) = 0.2$)

Khi xe chạy qua gờ đường, lực cưỡng bức tại $\omega = 15$ rad/s với biên độ $F_0 = 50$ N:
$$\hat{C} = \frac{50/2.5}{(400 - 225) + i(8)(15)} = \frac{20}{175 + 120i}$$

Biên độ dao động:
$$|\hat{C}| = \frac{20}{\sqrt{175^2 + 120^2}} = \frac{20}{\sqrt{30625 + 14400}} = \frac{20}{\sqrt{45025}} \approx \frac{20}{212.2} \approx 0.094 \text{ m}$$

*Quá lớn!* Kỹ sư cần tăng hệ số cản $\gamma$ hoặc thay đổi $\omega_0$ để giảm biên độ xuống dưới ngưỡng cho phép (thường < 1mm cho kính ngắm laser).

### Bài tập mẫu: Thiết kế bộ hấp thụ dao động

**Đề bài:** Cảm biến lực 6 bậc tự do (6-axis force/torque sensor) dùng trong robot lắp ráp vũ khí có tần số tự nhiên $\omega_0 = 200$ rad/s (31.8 Hz), hệ số cản $\gamma = 20$ rad/s. Lực rung từ động cơ servo tần số $\omega = 190$ rad/s với biên độ $F_0 = 0.1$ N, $m = 0.5$ kg. Tính biên độ rung động của cảm biến.

**Lời giải từng bước:**

**Bước 1:** Tính các thông số.
$$\omega_0^2 = 200^2 = 40000 \text{ rad}^2/\text{s}^2$$
$$\omega^2 = 190^2 = 36100 \text{ rad}^2/\text{s}^2$$
$$F_0/m = 0.1/0.5 = 0.2 \text{ m/s}^2$$

*Ý nghĩa:* $\omega < \omega_0$ (dưới tần số cộng hưởng), hệ thống chưa vào cộng hưởng.

**Bước 2:** Tính mẫu số phức.
$$D = (\omega_0^2 - \omega^2) + i\gamma\omega = (40000 - 36100) + i(20)(190)$$
$$D = 3900 + 3800i$$

*Ý nghĩa vật lý:* Phần thực là lực đàn hồi hiệu quả, phần ảo là lực cản hiệu quả tại tần số này.

**Bước 3:** Tính modulus của mẫu số.
$$|D| = \sqrt{3900^2 + 3800^2} = \sqrt{15210000 + 14440000} = \sqrt{29650000} \approx 5445 \text{ rad}^2/\text{s}^2$$

**Bước 4:** Tính biên độ dao động.
$$|\hat{C}| = \frac{F_0/m}{|D|} = \frac{0.2}{5445} \approx 3.67 \times 10^{-5} \text{ m} = 36.7 \mu\text{m}$$

*Ý nghĩa kỹ thuật:* Biên độ rung 36.7 micromet — vượt qua ngưỡng chấp nhận (thường < 1 micromet) cho cảm biến lực độ chính xác cao. Cần tăng $\gamma$ (thêm vật liệu cản nhớt) hoặc dùng bộ cách ly rung (vibration isolator) để giảm $F_0$ truyền vào.

**Bước 5:** Tính góc pha (thông tin về thời gian trễ).
$$\phi = -\arctan\frac{3800}{3900} = -\arctan(0.974) \approx -44.2°$$

Đáp ứng trễ pha 44.2° so với lực kích thích — thông tin quan trọng cho kỹ sư điều khiển bù pha feedforward.

**Điểm mấu chốt:**
- Phương pháp số phức biến phương trình vi phân thành phương trình đại số: $(-\omega^2 + i\gamma\omega + \omega_0^2)\hat{C} = F_0/m$.
- Hàm truyền tần số $H(\omega) = 1/[(\omega_0^2-\omega^2) + i\gamma\omega]$ là số phức — modulus cho biên độ, argument cho góc pha.
- Cộng hưởng xảy ra khi $\omega \approx \omega_0$, mẫu số gần bằng không, biên độ cực đại.
- Trong thiết kế cơ điện tử độ chính xác cao, tính biên độ rung và so sánh với ngưỡng micro/nanomét là bước bắt buộc trước khi chế tạo.

---
*Exported from Feynman Bot*
