---
lesson_id: 5492
lesson_type: deep_dive
approval_status: pending
exported_at: "2026-03-02T15:10:30.979957+00:00"
content_hash: 54660aee38de
chapter_number: 24
chapter_title: Chapter 24
section_number: 2
section_title: 24–1The energy of an oscillator
---
# ## Bài Giảng Chuyên Sâu: Quá Độ, Năng Lượng, và Phân Tích Hệ Dao Động Tắt Dần

*Source: Chapter 24 - Chapter 24 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_24.html)*

## Bài Giảng Chuyên Sâu: Quá Độ, Năng Lượng, và Phân Tích Hệ Dao Động Tắt Dần

### 1. Cấu Trúc Toán Học Của Nghiệm Tổng Quát

Phương trình dao động cưỡng bức có cản:
$$m\ddot{x} + m\gamma\dot{x} + m\omega_0^2 x = F_0\cos(\omega t)$$

Nghiệm tổng quát gồm hai phần:
$$x(t) = \underbrace{C_1 e^{-\gamma t/2}\cos(\omega_1 t) + C_2 e^{-\gamma t/2}\sin(\omega_1 t)}_{x_{transient}} + \underbrace{A\cos(\omega t + \phi)}_{x_{steady}}$$

Trong đó:
$$\omega_1 = \sqrt{\omega_0^2 - \left(\frac{\gamma}{2}\right)^2}$$

$C_1, C_2$ được xác định từ điều kiện đầu $x(0)$ và $\dot{x}(0)$.

Phần transient *luôn tắt dần* khi $t \to \infty$ nhờ hệ số $e^{-\gamma t/2}$, với thời gian hằng $\tau = 2/\gamma$. Sau $t \gg \tau$, chỉ còn phần steady-state tồn tại.

---

### 2. Cạm Bẫy Của Số Phức Khi Tính Năng Lượng

Đây là điểm Feynman nhấn mạnh đặc biệt. Giả sử đại lượng vật lý $A$ được biểu diễn phức:
$$A_{phức} = \hat{A}e^{i\omega t}, \quad \hat{A} = A_0 e^{i\Delta}$$

Giá trị vật lý thực là $A_{real} = \text{Re}[A_{phức}] = A_0\cos(\omega t + \Delta)$.

**Bình phương vật lý:**
$$A_{real}^2 = A_0^2\cos^2(\omega t + \Delta) = \frac{A_0^2}{2}[1 + \cos(2\omega t + 2\Delta)]$$

**Bình phương số phức (SAI):**
$$\text{Re}[(A_{phức})^2] = \text{Re}[\hat{A}^2 e^{2i\omega t}] = A_0^2\cos(2\omega t + 2\Delta)$$

Hai kết quả *khác nhau hoàn toàn* — bình phương số phức cho hàm dao động ở tần số $2\omega$, không có thành phần DC!

**Công thức đúng** để tính giá trị trung bình bình phương:
$$\langle A_{real}^2 \rangle = \frac{1}{2}\text{Re}[\hat{A} \cdot \hat{A}^*] = \frac{1}{2}|\hat{A}|^2 = \frac{A_0^2}{2}$$

Hoặc tổng quát hơn, với hai đại lượng $A$ và $B$:
$$\langle A_{real} B_{real} \rangle = \frac{1}{2}\text{Re}[\hat{A}\hat{B}^*]$$

---

### 3. Công Suất Phức và Hệ Số Công Suất

Trong mạch điện AC, điện áp và dòng điện phức $\hat{V} = V_0 e^{i\phi_V}$, $\hat{I} = I_0 e^{i\phi_I}$:

**Công suất tức thời trung bình (active power):**
$$\langle P \rangle = \frac{1}{2}\text{Re}[\hat{V}\hat{I}^*] = \frac{V_0 I_0}{2}\cos(\phi_V - \phi_I)$$

**Công suất biểu kiến (apparent power):** $S = V_{RMS} I_{RMS} = V_0 I_0 / 2$

**Hệ số công suất (power factor):** $PF = \cos\theta$ với $\theta = \phi_V - \phi_I$ là góc lệch pha.

Mạch RLC ở cộng hưởng: $\theta = 0$, $PF = 1$ — toàn bộ công suất biểu kiến là công suất thực, hiệu quả nhất.

---

### 4. Ba Chế Độ Dao Động Tắt Dần

Tùy theo quan hệ giữa $\gamma$ và $\omega_0$:

**a) Underdamping (Cản dưới tới hạn):** $\gamma < 2\omega_0$, $Q > 1/2$
$$x(t) = A e^{-\gamma t/2}\cos(\omega_1 t + \phi)$$
Dao động tắt dần với tần số $\omega_1 = \sqrt{\omega_0^2 - \gamma^2/4}$. Oscilloscope cho thấy đường sin tắt dần.

**b) Critical damping (Cản tới hạn):** $\gamma = 2\omega_0$, $Q = 1/2$
$$x(t) = (A + Bt)e^{-\omega_0 t}$$
Không dao động, về 0 nhanh nhất trong các trường hợp không dao động. Lý tưởng cho thiết kế cơ cấu đo (galvanometer, cân điện tử).

**c) Overdamping (Cản quá tới hạn):** $\gamma > 2\omega_0$, $Q < 1/2$
$$x(t) = A e^{-\gamma_1 t} + B e^{-\gamma_2 t}$$
Không dao động nhưng về 0 chậm hơn critical damping. Hai hằng số thời gian $1/\gamma_{1,2}$.

Trong thực tế oscilloscope (Hình 24–3 đến 24–6 của Feynman), ta thấy rõ ba chế độ này khi tăng $R$ từ nhỏ đến lớn trong mạch RLC.

---

### 5. Năng Lượng Trong Dao Động Tắt Dần

Năng lượng tổng của hệ underdamped:
$$E(t) = \frac{1}{2}m[\dot{x}^2 + \omega_0^2 x^2] \approx \frac{1}{2}mA^2\omega_0^2 e^{-\gamma t} = E_0 e^{-\gamma t}$$

Năng lượng giảm theo hàm mũ với hằng số thời gian $\tau_E = 1/\gamma = Q/\omega_0$.

Số chu kỳ để năng lượng giảm còn $1/e$:
$$N_e = \frac{1}{\gamma T_0} = \frac{\omega_0}{2\pi\gamma} = \frac{Q}{2\pi}$$

Hệ có $Q = 100$: năng lượng giảm $1/e$ sau khoảng 16 chu kỳ.

**Hệ số Q định nghĩa năng lượng:**
$$Q = \omega_0 \frac{E}{\langle P \rangle} = 2\pi\frac{E}{\Delta E_{chu kỳ}}$$

---

### 6. Phân Tích Fourier Của Xung Transient

Transient tắt dần theo hàm mũ có **phổ Lorentzian** trong miền tần số:
$$|\tilde{x}(\omega)|^2 \propto \frac{1}{(\omega - \omega_0)^2 + (\gamma/2)^2}$$

Băng thông tại $-3\,\text{dB}$: $\Delta\omega = \gamma$. Đây chính là nguyên lý bất định thời gian–tần số:
$$\Delta\omega \cdot \tau \sim 1$$

Xung ngắn (transient tắt nhanh, $\tau$ nhỏ) có phổ rộng. Xung dài (Q cao) có phổ hẹp. Đây là nền tảng cho phổ kế cộng hưởng (resonance spectroscopy) trong NMR, laser spectroscopy.

---

### 7. Điều Kiện Đầu và Sự Khớp Nghiệm

Khi đóng mạch đột ngột tại $t = 0$: $x(0) = 0$, $\dot{x}(0) = 0$. Từ đây tính $C_1, C_2$:

Nghiệm steady-state tại $t = 0$ là $A\cos\phi$. Để $x(0) = 0$: $C_1 = -A\cos\phi$.

Giai đoạn transient ban đầu có thể gây ra *overshoot* (vượt quá giá trị steady-state) nếu góc pha $\phi$ phù hợp. Trong thiết kế PID, overshoot cần được kiểm soát để tránh dao động không mong muốn.

---

### 8. Ứng Dụng: Settling Time Trong Hệ Điều Khiển Chính Xác

Trong hệ servo định vị micrometer, settling time $T_s$ là thời gian để sai số định vị giảm xuống dưới ngưỡng $\epsilon$ sau bước nhảy lệnh. Với hệ underdamped:
$$T_s \approx \frac{4}{\gamma} = \frac{4Q}{\omega_0}$$

Trade-off cơ bản:
- **Q cao** (cản thấp): Tần số cộng hưởng sắc nét, nhạy với nhiễu rung; settling time dài.
- **Q thấp** (cản cao): Settling time ngắn nhưng đáp ứng chậm, có thể bị overdamped.
- **Critical damping** ($Q = 0.5$): Tốt nhất cho settling time ngắn, nhưng phổ tần rộng, dễ bị nhiễu.

Hệ điều khiển thực tế thường chọn $Q \approx 0.7$–$1$ (hơi underdamped) để cân bằng tốc độ và ổn định.

---

### 9. Phân Biệt Transient Cưỡng Bức và Tự Do

**Transient tự do (free transient):** Xảy ra khi kích thích đột ngột rồi tắt. Tần số là $\omega_1 \approx \omega_0$, biên độ tắt dần $e^{-\gamma t/2}$.

**Beat phenomenon (hiện tượng phách):** Khi tần số kích thích $\omega$ gần nhưng không bằng $\omega_0$, trong giai đoạn transient ban đầu có hiện tượng phách (beating) — biên độ dao động lên xuống theo tần số $|\omega - \omega_0|$. Đây là hiện tượng quan sát thấy khi "khởi động" bộ lọc cộng hưởng.

---

### 10. Tóm Tắt

Nghiệm tổng quát = transient + steady-state. Transient tắt với thời hằng $2/\gamma$, xác định bởi điều kiện đầu. Tính năng lượng từ số phức: $\langle A^2 \rangle = |\hat{A}|^2/2$, không bình phương trực tiếp. Ba chế độ tắt dần (under/critical/over damped) với Q là thước đo; critical damping cho settling time tốt nhất. Phổ Lorentzian của transient liên hệ thời gian–băng thông. Đây là nền tảng phân tích đáp ứng quá độ trong điều khiển tự động.

---
*Exported from Feynman Bot*
