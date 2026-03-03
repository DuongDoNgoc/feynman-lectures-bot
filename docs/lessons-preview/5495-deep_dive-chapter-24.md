---
lesson_id: 5495
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:06.514603+00:00"
content_hash: 4370dbd1bc27
chapter_number: 24
chapter_title: Chapter 24
section_number: 4
section_title: 24–3Electrical transients
---
# ## Bài Giảng Chuyên Sâu: Quá Độ Điện — Phân Tích Toán Học Và Kỹ Thuật Đo Lường

*Source: Chapter 24 - Chapter 24 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_24.html)*

## Bài Giảng Chuyên Sâu: Quá Độ Điện — Phân Tích Toán Học Và Kỹ Thuật Đo Lường

### 1. Phương Trình Quá Độ Điện Từ Đầu Đến Cuối

Xét mạch RLC nối tiếp với nguồn $V_0$ DC đóng vào tại $t = 0$ qua công tắc $S$. Phương trình Kirchhoff:
$$L\frac{dI}{dt} + RI + \frac{q}{C} = V_0 \quad (t > 0)$$

Với $I = dq/dt$, viết lại:
$$L\ddot{q} + R\dot{q} + \frac{q}{C} = V_0$$

Nghiệm tổng quát = nghiệm riêng (steady-state) + nghiệm thuần nhất (transient):
$$q(t) = CV_0 + q_{transient}(t)$$

Phần transient thỏa phương trình thuần nhất:
$$L\ddot{q}_T + R\dot{q}_T + \frac{q_T}{C} = 0$$

Đặc trưng bởi hàm mũ $q_T \sim e^{st}$, phương trình đặc trưng:
$$Ls^2 + Rs + \frac{1}{C} = 0 \implies s_{1,2} = -\frac{R}{2L} \pm \sqrt{\left(\frac{R}{2L}\right)^2 - \frac{1}{LC}}$$

Đặt $\alpha = R/(2L)$ (damping coefficient) và $\omega_0 = 1/\sqrt{LC}$:
$$s_{1,2} = -\alpha \pm \sqrt{\alpha^2 - \omega_0^2}$$

---

### 2. Ba Trường Hợp Của Căn Số

**Underdamped ($\alpha < \omega_0$, $Q > 1/2$):**
$$s_{1,2} = -\alpha \pm i\omega_d, \quad \omega_d = \sqrt{\omega_0^2 - \alpha^2}$$
$$q_T(t) = e^{-\alpha t}(A\cos\omega_d t + B\sin\omega_d t)$$

Điện áp trên $L$ (mà oscilloscope đo):
$$V_L = L\frac{dI}{dt} = L\ddot{q}$$

Tính toán ra:
$$V_L(t) = V_0 e^{-\alpha t}\left[\cos\omega_d t - \frac{\alpha}{\omega_d}\sin\omega_d t\right] = \frac{V_0\omega_0}{\omega_d}e^{-\alpha t}\cos(\omega_d t + \theta)$$

Trong đó $\theta = \arctan(\alpha/\omega_d)$.

**Critically damped ($\alpha = \omega_0$, $Q = 1/2$):**
$$q_T(t) = (A + Bt)e^{-\alpha t}$$
$$V_L(t) = V_0(1 - \alpha t)e^{-\alpha t}$$

**Overdamped ($\alpha > \omega_0$, $Q < 1/2$):**
$$s_{1,2} = -\alpha \pm \beta, \quad \beta = \sqrt{\alpha^2 - \omega_0^2} \in \mathbb{R}$$
$$V_L(t) = \frac{V_0\omega_0^2}{2\beta\omega_0}\left[e^{-(\alpha-\beta)t} - e^{-(\alpha+\beta)t}\right]$$

---

### 3. Điều Kiện Đầu Và Nghiệm Đầy Đủ

Với $q(0) = 0$ (tụ chưa nạp) và $I(0) = 0$ (cuộn cảm chưa có dòng):

Từ $q(0) = CV_0 + A = 0$: $A = -CV_0$
Từ $\dot{q}(0) = I(0) = 0$: $-\alpha A + B\omega_d = 0$, nên $B = \alpha A/\omega_d = -\alpha CV_0/\omega_d$

Nghiệm hoàn chỉnh (underdamped):
$$q(t) = CV_0\left[1 - e^{-\alpha t}\left(\cos\omega_d t + \frac{\alpha}{\omega_d}\sin\omega_d t\right)\right]$$

$$I(t) = \frac{V_0}{\omega_d L}e^{-\alpha t}\sin\omega_d t = \frac{V_0\omega_0^2}{\omega_d\omega_0 L}e^{-\alpha t}\sin\omega_d t$$

Đây là đường cong sinusoidal tắt dần đúng như oscilloscope hiển thị.

---

### 4. Đo Q Từ Dạng Sóng Oscilloscope

**Phương pháp 1 — Logarithmic decrement (giảm lũy thừa logarithm):**

Hai đỉnh liên tiếp $A_n$ và $A_{n+1}$ của dạng sóng cách nhau chu kỳ $T_d = 2\pi/\omega_d$:
$$\frac{A_{n+1}}{A_n} = e^{-\alpha T_d}$$

$$\delta = \ln\frac{A_n}{A_{n+1}} = \alpha T_d = \frac{\alpha \cdot 2\pi}{\omega_d} = \frac{\pi}{\sqrt{Q^2 - 1/4}} \approx \frac{\pi}{Q} \quad (Q \gg 1)$$

Từ đó: $Q \approx \pi/\delta$.

**Phương pháp 2 — Đếm chu kỳ:**
Nếu biên độ giảm còn $1/e$ sau $N$ chu kỳ:
$$Q = \pi N$$

Ví dụ: Hình 24–3 biên độ giảm $1/e$ sau ~5 chu kỳ: $Q \approx 15.7$.

**Phương pháp 3 — Phân tích FFT:**
Biến đổi Fourier của transient cho phổ Lorentzian với đỉnh tại $\omega_0$ và băng thông $\Delta\omega = 2\alpha = R/L$. $Q = \omega_0/\Delta\omega$.

---

### 5. Biến Đổi Laplace — Cách Nhìn Hệ Thống

Phương pháp Laplace cho phép giải phương trình vi phân *kể cả điều kiện đầu* bằng đại số:

$$s^2 LQ(s) - sLq(0) - L\dot{q}(0) + sRQ(s) - Rq(0) + \frac{Q(s)}{C} = \frac{V_0}{s}$$

Với $q(0) = \dot{q}(0) = 0$:
$$Q(s) = \frac{V_0/s}{Ls^2 + Rs + 1/C} = \frac{V_0}{L} \cdot \frac{1}{s(s^2 + 2\alpha s + \omega_0^2)}$$

Hàm truyền của mạch (từ $V_{input}$ đến $V_L$):
$$H(s) = \frac{V_L(s)}{V_{in}(s)} = \frac{s^2 L}{Ls^2 + Rs + 1/C} = \frac{s^2}{s^2 + 2\alpha s + \omega_0^2}$$

Đây là bộ lọc thông cao bậc 2 (second-order high-pass filter). Cực (poles) của $H(s)$ chính là $s_{1,2} = -\alpha \pm i\omega_d$ — vị trí cực trên mặt phẳng $s$ hoàn toàn xác định đặc tính transient.

---

### 6. Sơ Đồ Cực–Không (Pole-Zero Diagram)

Trên mặt phẳng $s$:
- Hai cực (poles) tại $s_{1,2} = -\alpha \pm i\omega_d$: nằm đối xứng qua trục thực, về phía trái trục ảo (half-plane trái đảm bảo ổn định).
- Khoảng cách từ gốc đến cực: $|s_{1,2}| = \omega_0$.
- Góc từ trục âm thực đến cực: $\cos\theta = \alpha/\omega_0 = 1/(2Q) = \zeta$ (damping ratio).

Khi Q tăng ($\zeta$ giảm), cực di chuyển về trục ảo (lên trên trong nửa phẳng trên) — tần số dao động $\omega_d$ tăng, thời gian tắt dần $1/\alpha$ kéo dài.

Critical damping: cực trùng nhau trên trục thực tại $s = -\omega_0$.
Overdamped: hai cực thực âm riêng biệt.

---

### 7. Ứng Dụng Nâng Cao Trong Hệ Điều Khiển

**Bộ lọc tích cực Sallen-Key bậc 2:** Dùng op-amp để thực hiện bộ lọc với Q và $\omega_0$ tùy chỉnh, không cần cuộn cảm cồng kềnh.

**Bộ điều khiển PID và transient:**
Hệ vòng kín với PID có hàm truyền vòng kín tương đương bộ lọc bậc 2. Chỉnh K_P, K_I, K_D tương đương điều chỉnh $\omega_0$ và $\alpha$ của hệ quá độ.

**Đo thông số cơ học qua phương pháp điện:**
Bộ khuếch đại đo (lock-in amplifier) kích thích cộng hưởng cơ và đo đáp ứng: từ tần số cộng hưởng và băng thông, xác định $k$ (độ cứng) và $m$ (khối lượng) của MEMS sensor với độ chính xác pg (picogram).

---

### 8. Biên Giới Giữa Mô Hình Lý Tưởng Và Thực Tế

Trong thực nghiệm, dạng sóng oscilloscope khác lý thuyết vì:
1. **Inductance ký sinh** của dây kết nối làm tăng $L_{eff}$
2. **Điện trở dây quấn** cuộn cảm (DCR) làm tăng $R_{eff}$
3. **ESR của tụ** thêm điện trở nối tiếp
4. **Bandwidth oscilloscope** giới hạn: nếu $\omega_d > 2\pi f_{BW}$, dạng sóng bị biến dạng
5. **Ground loops** gây nhiễu ảnh hưởng đến đo dạng sóng biên độ nhỏ

Kỹ sư thực nghiệm phải nhận biết và loại bỏ các yếu tố này để lấy $Q$ và $\omega_0$ chính xác.

---

### 9. Mô Hình Điện Tương Đương Cho Cơ Học

Bảng ký hiệu:

| Cơ học | Điện học |
|--------|----------|
| $m = 100\,\text{g}$ | $L = 100\,\text{mH}$ |
| $k = 10^4\,\text{N/m}$ | $1/C = 10^4 \to C = 100\,\mu\text{F}$ |
| $b = 2\,\text{Ns/m}$ | $R = 2\,\Omega$ |

Mạch điện tương đương cho phép mô phỏng và đo nhanh bằng oscilloscope, điều chỉnh tham số bằng biến trở — tiết kiệm thời gian và chi phí so với thực nghiệm cơ học.

---

### 10. Tóm Tắt

Phân tích Laplace của mạch RLC cho nghiệm đầy đủ kể cả điều kiện đầu. Ba chế độ xác định bởi cực trên mặt phẳng s: underdamped (cực phức), critically damped (cực thực kép), overdamped (cực thực đơn). Đo Q từ oscilloscope qua logarithmic decrement hoặc FFT. Pole-zero diagram là công cụ tư duy mạnh cho thiết kế bộ lọc và bộ điều khiển. Mô hình điện tương đương giúp nhanh chóng prototype và kiểm tra ý tưởng thiết kế cơ học.

---
*Exported from Feynman Bot*
