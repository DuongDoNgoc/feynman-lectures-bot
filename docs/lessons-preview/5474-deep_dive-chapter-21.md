---
lesson_id: 5474
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-02T15:10:30.391889+00:00"
content_hash: aa3f73cd5227
chapter_number: 21
chapter_title: Chapter 21
section_number: 4
section_title: 21–3Harmonic motion and circular motion
---
# ## Dao Động Điều Hòa và Chuyển Động Tròn — Phân tích Chuyên sâu

*Source: Chapter 21 - Chapter 21 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_21.html)*

## Dao Động Điều Hòa và Chuyển Động Tròn — Phân tích Chuyên sâu

### 1. Chứng Minh Chặt Chẽ Mối Liên Hệ Tròn-Dao Động

Xét hạt chuyển động tròn đều bán kính $R$, tốc độ góc $\omega_0$ = const. Gọi $\theta(t) = \omega_0 t$ là góc từ trục $x$ dương. Tọa độ:
$$x(t) = R\cos\theta = R\cos(\omega_0 t)$$
$$y(t) = R\sin\theta = R\sin(\omega_0 t)$$

Vận tốc góc: $d\theta/dt = \omega_0 = v/R$ (với $v$ là tốc độ dài).

Gia tốc hướng tâm có độ lớn:
$$a = \frac{v^2}{R} = \omega_0^2 R$$

Gia tốc này hướng vào tâm, tức là ngược chiều vector vị trí. Thành phần $x$:
$$a_x = -a\cos\theta = -\omega_0^2 R\cos\theta = -\omega_0^2 x$$

Vậy: $\frac{d^2x}{dt^2} = -\omega_0^2 x$ — **đây chính là phương trình harmonic oscillator!**

Kiểm tra trực tiếp bằng vi phân:
$$\frac{d}{dt}[R\cos(\omega_0 t)] = -R\omega_0\sin(\omega_0 t)$$
$$\frac{d^2}{dt^2}[R\cos(\omega_0 t)] = -R\omega_0^2\cos(\omega_0 t) = -\omega_0^2 \cdot [R\cos(\omega_0 t)] = -\omega_0^2 x \checkmark$$

### 2. Nghiệm Tổng Quát và Điều Kiện Đầu

Phương trình $\ddot{x} = -\omega_0^2 x$ là bậc 2, cần hai hằng số tích phân. Nghiệm tổng quát:
$$x(t) = A\cos(\omega_0 t) + a\sin(\omega_0 t)$$

Hay dạng biên độ-pha:
$$x(t) = C\cos(\omega_0 t + \phi)$$
với $C = \sqrt{A^2 + a^2}$ (biên độ), $\tan\phi = -a/A$ (pha).

**Xác định hằng số từ điều kiện đầu:**
- $x(0) = A\cos 0 + a\sin 0 = A \Rightarrow A = x_0$
- $\dot{x}(0) = -A\omega_0\sin 0 + a\omega_0\cos 0 = a\omega_0 \Rightarrow a = v_0/\omega_0$

Nghiệm đặc biệt:
$$x(t) = x_0\cos(\omega_0 t) + \frac{v_0}{\omega_0}\sin(\omega_0 t)$$

**Ví dụ 1:** Stylus đầu đo CMM tiếp xúc bề mặt với vận tốc $v_0 = 1$ mm/s và bị nén $x_0 = 0.01$ mm. Với $\omega_0 = 2\pi \times 300$ rad/s:
$$a = v_0/\omega_0 = 0.001/(600\pi) = 5.3 \times 10^{-7} \text{ m} = 0.53 \text{ µm}$$
Biên độ dao động: $C = \sqrt{(0.01 \text{ mm})^2 + (0.53 \text{ µm})^2} \approx 0.01 \text{ mm}$ (pha ban đầu nhỏ).

### 3. Phân Tích Hình Học: Vòng Tròn trong Mặt Phẳng Pha

Mặt phẳng pha (phase plane) vẽ $\dot{x}$ theo $x$:
- $x(t) = C\cos(\omega_0 t + \phi)$
- $\dot{x}(t) = -C\omega_0\sin(\omega_0 t + \phi)$

Nhận thấy: $\left(\frac{x}{C}\right)^2 + \left(\frac{\dot{x}}{C\omega_0}\right)^2 = \cos^2 + \sin^2 = 1$

Quỹ đạo trong mặt phẳng pha là **elipse** (hay vòng tròn nếu dùng tọa độ $(x, \dot{x}/\omega_0)$). Đây là hình chiếu trực tiếp từ chuyển động tròn trong không gian ảo.

**Ý nghĩa kỹ thuật:** Kỹ sư điều khiển dùng phase portrait để phân tích ổn định của hệ phi tuyến. Trong điều khiển servo, vòng tròn trong phase plane tương ứng với dao động ổn định; quỹ đạo xoắn vào tâm là hệ tắt dần; xoắn ra là hệ mất ổn định.

### 4. Kết Nối với Số Phức và Phasor

Biểu diễn vị trí hạt trên vòng tròn bằng số phức:
$$z(t) = x(t) + iy(t) = R\cos(\omega_0 t) + iR\sin(\omega_0 t) = Re^{i\omega_0 t}$$

Đạo hàm: $\dot{z} = i\omega_0 Re^{i\omega_0 t} = i\omega_0 z$
Đạo hàm hai lần: $\ddot{z} = -\omega_0^2 z$

Phần thực của $z$ (tức $x$) thỏa mãn $\ddot{x} = -\omega_0^2 x$ — hoàn toàn nhất quán.

**Phasor trong điện tử:** Điện áp xoay chiều $V(t) = V_0\cos(\omega t + \phi)$ được biểu diễn bằng phasor $\tilde{V} = V_0 e^{i\phi}$. Phép vi phân $d/dt$ trở thành phép nhân với $i\omega$:
$$\frac{dV}{dt} \leftrightarrow i\omega \tilde{V}$$

Đây là lý do impedance của cuộn cảm $Z_L = i\omega L$ và tụ điện $Z_C = 1/(i\omega C)$ — kỹ thuật số phức biến hệ phương trình vi phân thành hệ đại số tuyến tính, đơn giản hóa toàn bộ phân tích mạch.

### 5. Ứng Dụng: Lock-in Amplifier trong Đo Lường Chính Xác

**Lock-in amplifier** là công cụ đo lường cực kỳ chính xác dựa trực tiếp trên tính chất của harmonic oscillator và chuyển động tròn.

Nguyên lý: tín hiệu cần đo $V_s(t) = A\cos(\omega_0 t + \phi)$ được nhân với tín hiệu tham chiếu $\cos(\omega_0 t)$:
$$V_s \cdot \cos(\omega_0 t) = \frac{A}{2}[\cos(\phi) + \cos(2\omega_0 t + \phi)]$$

Sau lọc thông thấp (low-pass filter) loại thành phần $2\omega_0$:
$$\text{Output}_X = \frac{A}{2}\cos\phi$$

Tương tự nhân với $\sin(\omega_0 t)$:
$$\text{Output}_Y = \frac{A}{2}\sin\phi$$

Từ hai thành phần này: $A = 2\sqrt{X^2 + Y^2}$ và $\phi = \arctan(Y/X)$ — đây chính xác là chuyển đổi từ tọa độ Cartesian sang cực trên mặt phẳng phức!

Lock-in amplifier có thể đo tín hiệu yếu hơn noise **1000 lần** nhờ kỹ thuật này. Ứng dụng trong đo lường micro-mét: cảm biến laser interferometer dùng lock-in để đo dịch chuyển với độ phân giải picometer trong môi trường nhiều nhiễu.

### 6. Ứng Dụng: Resolver trong Servo Motor Vũ Khí

**Resolver** (bộ giải mã góc analog) trong servo motor của hệ thống điều khiển pháo phát ra:
- $V_{\sin} = V_0\sin(\omega t)\sin\theta$ (winding sin)
- $V_{\cos} = V_0\sin(\omega t)\cos\theta$ (winding cos)

Với $\theta$ là góc cơ học cần đo. Mạch R/D converter (Resolver-to-Digital) trích xuất:
$$\theta = \arctan\left(\frac{V_{\sin}}{V_{\cos}}\right)$$

Thực chất đây là tính góc pha của vector trong mặt phẳng phức — cùng phép tính như trong mối liên hệ tròn-dao động. Độ phân giải góc đạt 16-bit (±0.005°) nhờ kỹ thuật này, đủ để điều khiển pháo với độ chính xác milli-radian.

### 7. Bài Tập Mẫu — Lock-in Amplifier

**Bài toán:** Một interferometer đo dịch chuyển tạo ra tín hiệu $V_s(t) = 50\mu V \cdot \cos(2\pi \times 1000 \cdot t + 0.785)$ trong môi trường nhiễu $\sigma_{\text{noise}} = 10$ mV rms (SNR = -46 dB). Sử dụng lock-in với tham chiếu $\omega_0 = 2\pi \times 1000$ rad/s. Tính biên độ $A$ và pha $\phi$.

**Giải:**

Bước 1: Output X (nhân với $\cos(\omega_0 t)$, lọc thấp):
$$X = \frac{A}{2}\cos\phi = \frac{50\mu V}{2}\cos(0.785) = 25\mu V \times 0.707 = 17.68 \mu V$$

Bước 2: Output Y (nhân với $\sin(\omega_0 t)$, lọc thấp):
$$Y = \frac{A}{2}\sin\phi = 25\mu V \times \sin(0.785) = 25\mu V \times 0.707 = 17.68 \mu V$$

Bước 3: Phục hồi biên độ:
$$A = 2\sqrt{X^2 + Y^2} = 2\sqrt{(17.68)^2 + (17.68)^2} \mu V = 2 \times 17.68\sqrt{2} \mu V = 50 \mu V \checkmark$$

Bước 4: Phục hồi pha:
$$\phi = \arctan(Y/X) = \arctan(1) = \pi/4 = 0.785 \text{ rad} \checkmark$$

**Kết quả:** Lock-in amplifier phục hồi chính xác tín hiệu 50 µV từ trong nhiễu 10 mV — một phép màu kỹ thuật được tạo ra bởi toán học của harmonic oscillator và chuyển động tròn.

**Điểm mấu chốt:**
- $a_x = -\omega_0^2 x$ trong chuyển động tròn ↔ phương trình harmonic oscillator: hai hiện tượng là một.
- Vận tốc góc $\omega_0 = v/R = d\theta/dt$ là nối cầu giữa chuyển động tròn và dao động.
- Biểu diễn phức $z = Re^{i\omega_0 t}$ thống nhất cả hai, dẫn đến phasor và impedance phức — công cụ thiết yếu của kỹ sư điện tử.
- Lock-in amplifier và resolver là các ứng dụng kỹ thuật trực tiếp của mối liên hệ tròn-dao động, cho phép đo lường cực kỳ chính xác trong môi trường nhiễu.

---
*Exported from Feynman Bot*
