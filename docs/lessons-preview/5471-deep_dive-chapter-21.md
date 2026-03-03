---
lesson_id: 5471
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:05.834170+00:00"
content_hash: 573da88d9f85
chapter_number: 21
chapter_title: Chapter 21
section_number: 2
section_title: 21–1Linear differential equations
---
# ## Bộ Dao Động Điều Hòa — Phân tích Chuyên sâu

*Source: Chapter 21 - Chapter 21 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_21.html)*

## Bộ Dao Động Điều Hòa — Phân tích Chuyên sâu

### 1. Phương Trình Vi Phân và Nguồn Gốc Vật Lý

Xét hệ lò xo-khối lượng lý tưởng (Fig. 21-1): khối lượng $m$ treo trên lò xo có hệ số đàn hồi $k$, dao động theo phương thẳng đứng. Gọi $x$ là độ lệch khỏi vị trí cân bằng (dương hướng lên).

Lực hồi phục của lò xo tuyến tính: $F = -kx$

Áp dụng định luật Newton thứ hai:
$$m\frac{d^2x}{dt^2} = -kx$$

Đặt $\omega_0^2 = k/m$ (tần số góc tự nhiên, đơn vị rad/s):

$$\frac{d^2x}{dt^2} = -\omega_0^2 x \quad \text{...(1)}$$

Đây là **phương trình vi phân tuyến tính bậc 2 thuần nhất** với hệ số hằng. Đặc điểm: nghiệm là hàm mà đạo hàm bậc 2 tỉ lệ ngược chiều với chính nó — chỉ có hàm sin và cos thỏa mãn tính chất này.

### 2. Giải Phương Trình — Phương Pháp Thử Nghiệm

**Thử nghiệm:** Đặt $x(t) = A\cos(\omega t + \phi)$

$$\dot{x} = -A\omega\sin(\omega t + \phi)$$
$$\ddot{x} = -A\omega^2\cos(\omega t + \phi) = -\omega^2 x$$

Thay vào (1): $-\omega^2 x = -\omega_0^2 x$ — thỏa mãn khi $\omega = \omega_0$.

**Nghiệm tổng quát:**
$$x(t) = A\cos(\omega_0 t) + B\sin(\omega_0 t)$$

Hay tương đương:
$$x(t) = C\cos(\omega_0 t + \phi)$$

Với $C = \sqrt{A^2 + B^2}$ (biên độ) và $\tan\phi = -B/A$ (pha ban đầu).

Hai hằng số $A$, $B$ (hay $C$, $\phi$) được xác định bởi **điều kiện đầu**: $x(0) = x_0$ và $\dot{x}(0) = v_0$:
$$A = x_0, \quad B = v_0/\omega_0$$

### 3. Tính Phổ Quát: Cùng Phương Trình, Nhiều Hệ Thống

**Mạch LC điện tử:**
Phương trình KVL cho mạch LC nối tiếp:
$$L\frac{d^2q}{dt^2} + \frac{q}{C} = 0 \quad \Rightarrow \quad \frac{d^2q}{dt^2} = -\frac{1}{LC}q$$

Hoàn toàn tương đồng với (1), với $\omega_0 = 1/\sqrt{LC}$:
- $q$ (điện tích) ↔ $x$ (vị trí)
- $L$ (inductance) ↔ $m$ (khối lượng)  
- $1/C$ (độ cứng điện) ↔ $k$ (độ cứng lò xo)

**Con lắc đơn (góc nhỏ $\theta < 10°$):**
$$\frac{d^2\theta}{dt^2} = -\frac{g}{l}\theta, \quad \omega_0 = \sqrt{g/l}$$

### 4. Phân Tích Năng Lượng

Năng lượng của harmonic oscillator:
- Động năng: $T = \frac{1}{2}m\dot{x}^2 = \frac{1}{2}mC^2\omega_0^2\sin^2(\omega_0 t + \phi)$
- Thế năng: $U = \frac{1}{2}kx^2 = \frac{1}{2}kC^2\cos^2(\omega_0 t + \phi)$
- Tổng: $E = T + U = \frac{1}{2}kC^2 = \frac{1}{2}m\omega_0^2 C^2 = \text{const}$

Năng lượng bảo toàn và chuyển đổi liên tục giữa động năng và thế năng, giống như trong mạch LC (năng lượng chuyển đổi giữa cuộn cảm và tụ điện).

### 5. Ứng Dụng Thực Tế: Cảm Biến và Đo Lường Chính Xác

**Đầu đo tiếp xúc (contact probe) trong CMM:**
Đầu đo Renishaw TP20 trong máy đo CMM có cấu trúc lò xo-khối lượng: stylus (đầu dò) kết nối với kinematic mount qua lò xo lá. Khi stylus tiếp xúc bề mặt, hệ dao động với $\omega_0 \approx 200-500$ Hz. Để đo chính xác ở mức micro-mét, trigger signal phải được ghi nhận **trước** khi dao động ảnh hưởng đến kết quả. Thời gian settling $t_s \approx 5/\omega_0$ quyết định tốc độ đo tối đa.

**Cảm biến gia tốc MEMS (accelerometer):**
Proof mass treo trên suspension springs với $k_{\text{eff}}$ và $m_{\text{proof}}$, cho tần số cộng hưởng:
$$f_0 = \frac{1}{2\pi}\sqrt{\frac{k_{\text{eff}}}{m_{\text{proof}}}}$$
Thiết kế accelerometer dải rộng (DC đến 1 kHz): cần $f_0 > 10$ kHz để đường đáp ứng phẳng trong dải làm việc. Tăng $k_{\text{eff}}$ hoặc giảm $m_{\text{proof}}$ đều tăng $f_0$ — nhưng đồng thời giảm độ nhạy $S = m/k_{\text{eff}}$ (nm/g). Đây là sự đánh đổi cơ bản trong thiết kế MEMS.

**Bộ giảm xóc trong bệ gá vũ khí:**
Súng máy trên xe thiết giáp gắn qua isolator gồm cao su (lò xo) và hệ số giảm xóc $c$. Phương trình đầy đủ:
$$m\ddot{x} + c\dot{x} + kx = F_{\text{recoil}}(t)$$
Với $c = 2\zeta\sqrt{km}$, $\zeta$ là hệ số giảm xóc (damping ratio). Mục tiêu thiết kế: $\zeta = 0.6-0.8$ (underdamped nhẹ) để nhanh trở về vị trí cân bằng giữa các phát bắn mà không rung lắc quá mức.

### 6. Liên Hệ với Chuyển Động Tròn

Một hạt chuyển động tròn đều bán kính $R$ với tốc độ góc $\omega_0$:
- Vị trí: $x = R\cos(\omega_0 t)$, $y = R\sin(\omega_0 t)$
- Gia tốc hướng tâm: $a_x = -\omega_0^2 R\cos(\omega_0 t) = -\omega_0^2 x$

Nghiệm của harmonic oscillator chính là **hình chiếu** của chuyển động tròn đều lên một trục! Đây là cầu nối quan trọng để dùng số phức trong chương tiếp theo.

### 7. Bài Tập Mẫu — Thiết Kế Cảm Biến Accelerometer MEMS

**Bài toán:** Một accelerometer MEMS dùng trong hệ IMU của UAV cần đo gia tốc trong dải $0-500$ Hz với độ chính xác $\pm 0.1\%$. Proof mass $m = 1$ µg. Tính hệ số đàn hồi $k$ tối thiểu của suspension spring để đáp ứng phẳng (flat response) trong dải đo.

**Giải:**

Bước 1: Để đáp ứng phẳng trong dải $f_{\text{max}} = 500$ Hz, cần tần số cộng hưởng:
$$f_0 > 3 \times f_{\text{max}} = 1500 \text{ Hz}$$
(ngưỡng an toàn kỹ thuật cho flat response ±0.1%)

Bước 2: Từ $f_0 = \frac{1}{2\pi}\sqrt{k/m}$:
$$k = m(2\pi f_0)^2 = 1 \times 10^{-9} \times (2\pi \times 1500)^2$$

Bước 3: Tính:
$$k = 10^{-9} \times (9424.8)^2 = 10^{-9} \times 8.88 \times 10^7 = 0.0888 \text{ N/m}$$

Bước 4: Độ nhạy tĩnh:
$$S = m/k = 10^{-9}/0.0888 = 1.13 \times 10^{-8} \text{ m/m·s}^{-2} = 11.3 \text{ pm/g}$$

**Nhận xét:** Độ nhạy rất thấp (picometer/g) — cần capacitive readout có độ phân giải zeptometer để đo được. Đây là lý do accelerometer độ nhạy cao thường có $f_0$ thấp hơn (vài trăm Hz) và dùng electrostatic force feedback.

**Điểm mấu chốt:**
- Phương trình $d^2x/dt^2 = -\omega_0^2 x$ là nền tảng của vô số hệ thống từ MEMS sensor đến mạch LC, từ con lắc đến sóng điện từ.
- Nghiệm $x(t) = A\cos(\omega_0 t) + B\sin(\omega_0 t)$ hoàn toàn xác định bởi điều kiện đầu.
- Tần số tự nhiên $\omega_0 = \sqrt{k/m}$ là thông số thiết kế then chốt: quá thấp → cộng hưởng trong dải làm việc; quá cao → độ nhạy giảm.
- Sự tương đồng giữa các hệ thống (cơ-điện-âm) cho phép áp dụng chéo các phương pháp phân tích và thiết kế.

---
*Exported from Feynman Bot*
