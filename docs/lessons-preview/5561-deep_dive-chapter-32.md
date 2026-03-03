---
lesson_id: 5561
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:08.025370+00:00"
content_hash: 825a76c53320
chapter_number: 32
chapter_title: Chapter 32
section_number: 1
section_title: 32Radiation Damping. Light Scattering
---
# ## Trở Kháng Bức Xạ và Công Suất Bức Xạ: Phân Tích Định Lượng

*Source: Chapter 32 - Chapter 32 (Section 1) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_32.html)*

## Trở Kháng Bức Xạ và Công Suất Bức Xạ: Phân Tích Định Lượng

### 1. Năng Lượng Bức Xạ Từ Một Điện Tích Dao Động

Khi điện tích $q$ dao động với gia tốc $a$, công suất tức thời bức xạ theo công thức Larmor:

$$P = \frac{q^2 a^2}{6\pi\varepsilon_0 c^3}$$

Với dao động điều hòa $x(t) = x_0 \cos(\omega_0 t)$, gia tốc là $a(t) = -\omega_0^2 x_0 \cos(\omega_0 t)$, và $\langle a^2 \rangle = \omega_0^4 x_0^2/2$. Do đó công suất bức xạ trung bình:

$$\langle P \rangle = \frac{q^2 \omega_0^4 x_0^2}{12\pi\varepsilon_0 c^3}$$

Đây là kết quả quan trọng: **công suất bức xạ tỉ lệ với $\omega_0^4$**, lũy thừa bậc 4 của tần số.

### 2. Định Nghĩa Trở Kháng Bức Xạ

Để kết nối với lý thuyết mạch điện, ta định nghĩa trở kháng bức xạ $R_{\text{rad}}$ sao cho:

$$\langle P \rangle = \frac{1}{2} I_0^2 R_{\text{rad}}$$

Vì dòng điện trong anten là $I = q\dot{x}/L$ (với $L$ là nửa chiều dài anten lưỡng cực), ta có thể tính $R_{\text{rad}}$ tường minh. Với anten lưỡng cực ngắn (short dipole, $L \ll \lambda$):

$$R_{\text{rad}} = \frac{\mu_0 c}{6\pi} \left(\frac{2\pi L}{\lambda}\right)^2 = 790\,\Omega \cdot \left(\frac{L}{\lambda}\right)^2$$

Ví dụ cụ thể: Anten lưỡng cực nửa sóng ($L = \lambda/2$) có $R_{\text{rad}} \approx 73\,\Omega$ - đây là lý do tại sao hầu hết các hệ thống RF dùng trở kháng đặc trưng $50\,\Omega$ hoặc $75\,\Omega$!

### 3. Hệ Số Phẩm Chất Q và Sự Tắt Dần Do Bức Xạ

Hệ số Q định nghĩa bởi:

$$Q = -\frac{\omega W}{dW/dt} = \frac{\omega W}{P_{\text{rad}}}$$

Năng lượng toàn phần của dao động tử hòa với biên độ $x_0$:

$$W = \frac{1}{2} m \omega_0^2 x_0^2$$

Thay vào, sử dụng $P_{\text{rad}} = q^2\omega_0^4 x_0^2 / (12\pi\varepsilon_0 c^3)$:

$$Q_{\text{rad}} = \frac{\omega_0 \cdot \frac{1}{2}m\omega_0^2 x_0^2}{q^2\omega_0^4 x_0^2 / (12\pi\varepsilon_0 c^3)} = \frac{6\pi\varepsilon_0 m c^3}{q^2 \omega_0^2}$$

Với electron ($m = m_e = 9.11\times10^{-31}\,\text{kg}$, $q = e = 1.6\times10^{-19}\,\text{C}$) ở tần số ánh sáng khả kiến ($\omega_0 \sim 3\times10^{15}\,\text{rad/s}$):

$$Q_{\text{rad}} \approx \frac{6\pi \times 8.85\times10^{-12} \times 9.11\times10^{-31} \times (3\times10^8)^3}{(1.6\times10^{-19})^2 \times (3\times10^{15})^2} \approx 10^8$$

Đây là Q rất cao! Điện tử trong nguyên tử bức xạ năng lượng rất chậm - cần khoảng $10^8$ chu kỳ dao động mới mất đi phần đáng kể năng lượng.

### 4. Thời Gian Sống Của Trạng Thái Nguyên Tử

Năng lượng dao động tử giảm theo:

$$W(t) = W_0 e^{-\omega_0 t/Q}$$

Thời gian sống (lifetime) của trạng thái kích thích:

$$\tau = Q/\omega_0 = \frac{6\pi\varepsilon_0 m_e c^3}{e^2 \omega_0^2}$$

Với ánh sáng khả kiến, $\tau \sim 10^{-8}\,\text{s} = 10\,\text{ns}$. Đây chính xác là thời gian sống đo được của nhiều trạng thái kích thích nguyên tử trong thực nghiệm! Một thành công lớn của lý thuyết điện động học cổ điển.

### 5. Lực Bức Xạ Phản Ứng (Radiation Reaction Force)

Nếu điện tích mất năng lượng do bức xạ, phải có một lực nào đó làm chậm dao động. Lực này gọi là **lực bức xạ phản ứng** (radiation reaction force hay Abraham-Lorentz force):

$$F_{\text{rad}} = \frac{q^2}{6\pi\varepsilon_0 c^3} \dot{a} = \frac{q^2}{6\pi\varepsilon_0 c^3} \dddot{x}$$

Với dao động điều hòa $x = x_0 e^{i\omega t}$, $\dddot{x} = -i\omega^3 x_0 e^{i\omega t} = -i\omega^2 \dot{x}$, nên:

$$F_{\text{rad}} = -\frac{q^2\omega^2}{6\pi\varepsilon_0 c^3} \cdot i\dot{x} = -\gamma_{\text{rad}} \dot{x}$$

Với $\gamma_{\text{rad}} = q^2\omega^2/(6\pi\varepsilon_0 m c^3)$ là **hệ số tắt dần bức xạ**. Đây là nguồn gốc của lực cản trong phương trình tán sắc!

### 6. Ứng Dụng Thực Tế: Thiết Kế Anten Radar

Trong thiết kế radar quân sự, hiểu $R_{\text{rad}}$ là thiết yếu:

**Phối hợp trở kháng (impedance matching)**: Để công suất truyền từ máy phát đến anten là cực đại, trở kháng nguồn phải bằng liên hợp phức của trở kháng anten: $Z_{source} = Z_{ant}^*$. Trở kháng anten bao gồm $R_{\text{rad}}$ và các phần kháng.

**Băng thông (bandwidth)**: Q cao ($Q = \omega_0 L / R_{\text{rad}}$) nghĩa là băng thông hẹp $\Delta f = f_0/Q$. Radar pulse thường cần băng thông rộng, đòi hỏi Q thấp, nghĩa là $R_{\text{rad}}$ phải lớn so với điện kháng.

**Cường độ trường bức xạ**: Giản đồ bức xạ (radiation pattern) của lưỡng cực ngắn có dạng $\propto \sin^2\theta$ với $\theta$ là góc so với trục anten. Cường độ bức xạ bằng 0 dọc theo trục, cực đại ở mặt phẳng xích đạo - đây là lý do radar thường có anten mảng (phased array) để điều hướng búp sóng.

### Tóm Tắt Các Công Thức Chính

| Đại lượng | Công thức |
|-----------|----------|
| Công suất bức xạ | $P = q^2\omega_0^4 x_0^2 / (12\pi\varepsilon_0 c^3)$ |
| Trở kháng bức xạ (dipole ngắn) | $R_{\text{rad}} = 790(L/\lambda)^2\,\Omega$ |
| Hệ số Q bức xạ | $Q = 6\pi\varepsilon_0 m c^3 / (q^2\omega_0^2)$ |
| Thời gian sống | $\tau = Q/\omega_0$ |
| Hệ số tắt dần | $\gamma_{\text{rad}} = q^2\omega_0^2/(6\pi\varepsilon_0 mc^3)$ |

---
*Exported from Feynman Bot*
