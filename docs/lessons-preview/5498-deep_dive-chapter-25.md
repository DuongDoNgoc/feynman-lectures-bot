---
lesson_id: 5498
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:06.583935+00:00"
content_hash: 12e94c153d90
chapter_number: 25
chapter_title: Chapter 25
section_number: 2
section_title: 25–1Linear differential equations
---
# ## Phân Tích Sâu: Tính Tuyến Tính, Toán Tử và Nguyên Lý Chồng Chất

*Source: Chapter 25 - Chapter 25 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_25.html)*

## Phân Tích Sâu: Tính Tuyến Tính, Toán Tử và Nguyên Lý Chồng Chất

### 1. Định nghĩa chặt chẽ: Thế nào là hệ tuyến tính?

Điểm xuất phát của chúng ta là phương trình vi phân mô tả dao động có cản và cưỡng bức:

$$m\frac{d^2x}{dt^2} + \gamma m\frac{dx}{dt} + m\omega_0^2 x = F(t)$$

Chúng ta định nghĩa **toán tử tuyến tính** $\mathcal{L}$ như sau:

$$\mathcal{L}(x) \equiv m\frac{d^2x}{dt^2} + \gamma m\frac{dx}{dt} + m\omega_0^2 x$$

Khi đó bài toán trở thành: $\mathcal{L}(x) = F(t)$.

Một toán tử $\mathcal{L}$ được gọi là **tuyến tính** nếu và chỉ nếu thỏa mãn đồng thời:

**Tính cộng:** $\mathcal{L}(x + y) = \mathcal{L}(x) + \mathcal{L}(y)$

**Tính đồng nhất:** $\mathcal{L}(ax) = a\mathcal{L}(x)$ với $a$ là hằng số bất kỳ

Hai tính chất này có thể viết gộp thành một: $\mathcal{L}(\alpha x + \beta y) = \alpha\mathcal{L}(x) + \beta\mathcal{L}(y)$

### 2. Chứng minh toán tử dao động là tuyến tính

Chứng minh tính cộng:

$$\mathcal{L}(x+y) = m\frac{d^2(x+y)}{dt^2} + \gamma m\frac{d(x+y)}{dt} + m\omega_0^2(x+y)$$

Vì vi phân là phép toán tuyến tính: $\frac{d(x+y)}{dt} = \frac{dx}{dt} + \frac{dy}{dt}$, ta có:

$$= \left(m\frac{d^2x}{dt^2} + \gamma m\frac{dx}{dt} + m\omega_0^2 x\right) + \left(m\frac{d^2y}{dt^2} + \gamma m\frac{dy}{dt} + m\omega_0^2 y\right) = \mathcal{L}(x) + \mathcal{L}(y)$$

Chứng minh tính đồng nhất:

$$\mathcal{L}(ax) = m\frac{d^2(ax)}{dt^2} + \gamma m\frac{d(ax)}{dt} + m\omega_0^2(ax) = a\left(m\frac{d^2x}{dt^2} + \gamma m\frac{dx}{dt} + m\omega_0^2 x\right) = a\mathcal{L}(x)$$

**Lưu ý quan trọng:** Điều kiện để toán tử vi phân là tuyến tính là các hệ số (ở đây là $m$, $\gamma m$, $m\omega_0^2$) phải là **hằng số** hoặc **hàm của t**, không được phụ thuộc vào $x$. Nếu phương trình có dạng $x\frac{dx}{dt}$ hay $x^2$, toán tử đó không còn tuyến tính nữa.

### 3. Cấu trúc nghiệm của phương trình tuyến tính

**Bước 1: Giải phương trình thuần nhất**

Xét $\mathcal{L}(x) = 0$. Nếu ta tìm được hai nghiệm độc lập tuyến tính $x_1(t)$ và $x_2(t)$, thì:

- $ax_1$ là nghiệm (do tính đồng nhất)
- $x_1 + x_2$ là nghiệm (do tính cộng)
- Do đó $C_1 x_1 + C_2 x_2$ là nghiệm tổng quát của phương trình thuần nhất

Với phương trình dao động điều hòa tắt dần, nghiệm $x = e^{i\omega t}$ cho ta hai nghiệm:

$$x_1 = e^{i\omega_+ t}, \quad x_2 = e^{i\omega_- t}$$

với $\omega_\pm = -i\frac{\gamma}{2} \pm \sqrt{\omega_0^2 - \gamma^2/4}$

**Bước 2: Tìm nghiệm riêng**

Nếu $\mathcal{L}(x_p) = F(t)$, thì $x_p$ là một nghiệm riêng (particular solution).

**Bước 3: Nghiệm tổng quát**

$$x(t) = C_1 x_1(t) + C_2 x_2(t) + x_p(t)$$

Chứng minh: $\mathcal{L}(C_1 x_1 + C_2 x_2 + x_p) = C_1\mathcal{L}(x_1) + C_2\mathcal{L}(x_2) + \mathcal{L}(x_p) = 0 + 0 + F(t) = F(t)$

### 4. Nguyên lý chồng chất và ứng dụng với nhiều nguồn kích thích

Đây là hệ quả mạnh nhất của tính tuyến tính. Giả sử hệ chịu hai ngoại lực đồng thời: $F(t) = F_1(t) + F_2(t)$.

Nếu $\mathcal{L}(x_1) = F_1(t)$ và $\mathcal{L}(x_2) = F_2(t)$, thì:

$$\mathcal{L}(x_1 + x_2) = \mathcal{L}(x_1) + \mathcal{L}(x_2) = F_1(t) + F_2(t) = F(t)$$

Tức là ta chỉ cần giải bài toán riêng với từng lực, rồi cộng kết quả!

**Ví dụ thực tế - Hệ đo lường độ chính xác cao:**

Trong một máy đo tọa độ CMM (Coordinate Measuring Machine) mà bạn tích hợp, đầu dò chịu đồng thời:
- Rung động từ nền nhà ở tần số $f_1 = 50$ Hz
- Rung động từ motor servo ở $f_2 = 200$ Hz
- Rung động âm thanh môi trường ở dải $f_3 = 20$-$2000$ Hz

Do hệ cơ học là tuyến tính, đáp ứng tổng = tổng các đáp ứng riêng. Ta có thể thiết kế bộ lọc (filter) độc lập cho từng tần số rồi ghép lại. Nếu hệ phi tuyến, ta buộc phải giải bài toán tổng hợp phức tạp hơn nhiều.

### 5. Phân tích Fourier - Hệ quả mạnh nhất của tính tuyến tính

Bất kỳ tín hiệu tuần hoàn nào cũng có thể khai triển thành chuỗi Fourier:

$$F(t) = \sum_n F_n e^{in\omega t}$$

Do tính tuyến tính, đáp ứng của hệ sẽ là:

$$x(t) = \sum_n x_n(t)$$

trong đó mỗi $x_n$ là đáp ứng riêng với thành phần $F_n e^{in\omega t}$. Đây là nền tảng của **phân tích tần số** trong kỹ thuật điều khiển - một công cụ không thể thiếu trong thiết kế hệ servo của bạn!

Hàm truyền (transfer function) $H(\omega)$ chính xác là tỉ số giữa đầu ra và đầu vào ở từng tần số, và nó có ý nghĩa nhờ nguyên lý chồng chất:

$$x_n = H(n\omega) \cdot F_n$$

### 6. Khi nào tính tuyến tính bị phá vỡ?

Trong thực tế, hầu hết các hệ vật lý đều phi tuyến ở biên độ lớn:
- Lò xo thực tế: $F = -kx - k_3 x^3$ (phi tuyến bậc 3)
- Ma sát Coulomb: lực ma sát không đổi, đảo chiều theo chiều chuyển động
- Vùng bão hòa từ trong lõi biến áp hay motor

Khi hệ phi tuyến: superposition không còn đúng. Trong motor điều khiển độ chính xác cao, hiệu ứng phi tuyến của ma sát tĩnh (stiction) gây ra hiện tượng "stick-slip" - một vấn đề kinh điển trong điều khiển vị trí micrometer mà bạn chắc hẳn đã gặp.

**Tóm tắt cấu trúc kiến thức:**
- Tuyến tính = tính cộng + tính đồng nhất
- Nguyên lý superposition cho phép phân tích từng thành phần độc lập
- Chuỗi Fourier và hàm truyền là ứng dụng trực tiếp
- Thực tế luôn có phi tuyến, nhưng tuyến tính hóa là xấp xỉ cực kỳ hữu ích trong vùng làm việc nhỏ

---
*Exported from Feynman Bot*
