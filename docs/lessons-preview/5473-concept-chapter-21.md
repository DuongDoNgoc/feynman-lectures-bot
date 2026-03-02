---
lesson_id: 5473
lesson_type: concept
approval_status: approved
exported_at: "2026-03-02T15:10:30.369340+00:00"
content_hash: 4446b2bccf13
chapter_number: 21
chapter_title: Chapter 21
section_number: 4
section_title: 21–3Harmonic motion and circular motion
---
# ## Dao Động Điều Hòa và Chuyển Động Tròn — Mối Liên Hệ Bí Ẩn

*Source: Chapter 21 - Chapter 21 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_21.html)*

## Dao Động Điều Hòa và Chuyển Động Tròn — Mối Liên Hệ Bí Ẩn

Bạn đã bao giờ nhìn một bánh xe quay và chú ý đến bóng của một điểm trên vành xe chiếu lên tường không? Bóng đó không quay cùng bánh xe — nó **dao động lên xuống** theo nhịp sin hoàn hảo. Đây không phải trùng hợp: dao động điều hòa và chuyển động tròn đều là **hai mặt của cùng một hiện tượng toán học**.

### Hình Chiếu của Chuyển Động Tròn

Xét một hạt chuyển động tròn đều trên vòng tròn bán kính $R$ với tốc độ góc $\omega_0$ (rad/s). Tọa độ của hạt theo thời gian:

$$x(t) = R\cos(\omega_0 t), \qquad y(t) = R\sin(\omega_0 t)$$

Bây giờ, hãy tính **gia tốc** theo trục $x$:

$$a_x = \frac{d^2x}{dt^2} = -R\omega_0^2\cos(\omega_0 t) = -\omega_0^2 x$$

Kết quả: $a_x = -\omega_0^2 x$ — chính xác là phương trình của **harmonic oscillator**! Hình chiếu của chuyển động tròn đều lên một trục bất kỳ chính là nghiệm của phương trình harmonic oscillator.

Đây là sự kiện toán học đẹp đẽ: thay vì giải phương trình vi phân phức tạp, ta có thể **hình dung** hạt đang chuyển động tròn trong không gian ảo, và chỉ quan sát hình chiếu của nó lên trục thực. Phương pháp này cực kỳ mạnh mẽ và dẫn đến kỹ thuật số phức trong chương tiếp theo.

### Gia Tốc Hướng Tâm và Phương Trình Dao Động

Chuyển động tròn đều có gia tốc hướng vào tâm với độ lớn:

$$a = \frac{v^2}{R} = \omega_0^2 R$$

Thành phần $x$ của gia tốc này là $-a\cos\theta = -\omega_0^2 R\cos\theta = -\omega_0^2 x$.

Bằng cách đặt $\theta = \omega_0 t$ và $d\theta/dt = \omega_0 = v/R$, ta kết nối hoàn toàn giữa tốc độ góc, vận tốc dài, và tần số dao động. Đây không chỉ là kỹ thuật tính toán — nó tiết lộ cấu trúc hình học sâu sắc bên dưới.

### Biên Độ và Pha — Điều Kiện Đầu Quyết Định Tất Cả

Nghiệm tổng quát của harmonic oscillator:
$$x(t) = A\cos(\omega_0 t) + a\sin(\omega_0 t)$$

Hay tương đương: $x(t) = C\cos(\omega_0 t + \phi)$

Các hằng số $A$ và $a$ (hay $C$ và $\phi$) được xác định bởi **điều kiện đầu** — cách ta bắt đầu chuyển động:
- Chỉ kéo lệch rồi thả: $x(0) = x_0 \neq 0$, $\dot{x}(0) = 0$ → thuần cosine $x(t) = x_0\cos(\omega_0 t)$
- Bắt đầu từ trung tâm với vận tốc ban đầu: $x(0) = 0$, $\dot{x}(0) = v_0$ → thuần sine $x(t) = (v_0/\omega_0)\sin(\omega_0 t)$
- Kết hợp cả hai: kết quả là tổ hợp tuyến tính

Trong không gian tròn ảo: điều kiện đầu xác định vị trí ban đầu của hạt trên vòng tròn (pha $\phi$) và bán kính (biên độ $C$).

### Ẩn Dụ Kỹ Thuật: Phân Tích Fourier và Encoder Quay

Với kỹ sư cơ điện tử làm việc với encoder quay (rotary encoder) trong servo system, mối liên hệ tròn-dao động không chỉ là lý thuyết — nó là nền tảng của **phân tích Fourier** (Fourier analysis).

Encoder incremental phát ra hai tín hiệu vuông lệch pha 90° (quadrature signals): channel A là $\cos(N\theta)$ và channel B là $\sin(N\theta)$, với $N$ là số xung mỗi vòng và $\theta$ là góc quay. Đây chính xác là hai thành phần tọa độ $x$ và $y$ của chuyển động tròn!

Khi xử lý tín hiệu rung động từ một cảm biến gia tốc, kỹ thuật FFT (Fast Fourier Transform) phân tích tín hiệu phức tạp thành tổng vô hạn của các hàm sin/cos — tức là thành tổng của vô số harmonic oscillator với các tần số và biên độ khác nhau. Tần số cộng hưởng xuất hiện như các đỉnh nhọn trong phổ Fourier.

Tương tự, trong thiết kế bộ giải mã góc (angle resolver) cho servo motor pháo, tín hiệu sin và cos được xử lý để xác định góc quay chính xác. Nhiễu điện từ (EMI) từ vũ khí làm méo tín hiệu, nhưng nếu hiểu tín hiệu là hình chiếu của chuyển động tròn, ta có thể dùng thuật toán CORDIC để phục hồi góc ngay cả khi tín hiệu bị nhiễu.

### Tại Sao Sự Liên Hệ Này Quan Trọng?

Việc hiểu dao động điều hòa qua lăng kính chuyển động tròn mở ra một công cụ mạnh mẽ: **số phức** (complex numbers). Thay vì theo dõi $x$ và $y$ riêng rẽ, ta gói chúng vào một số phức $z = x + iy = Re^{i\omega_0 t}$. Khi đó phép vi phân trở thành phép nhân:
$$\dot{z} = i\omega_0 z$$

Đây là lý do tại sao kỹ sư điện tử dùng **impedance phức** ($Z = R + j\omega L + 1/j\omega C$) — họ đang khai thác chính xác mối liên hệ giữa dao động và chuyển động tròn trong mặt phẳng phức. Mạch lọc RC, LC, và PID controller đều được phân tích trong không gian phức vì nó đơn giản hóa toán học một cách kỳ diệu.

**Điểm mấu chốt:**
- Hình chiếu của chuyển động tròn đều lên một trục = nghiệm của harmonic oscillator: $a_x = -\omega_0^2 x$.
- Tần số góc tự nhiên $\omega_0 = v/R = d\theta/dt$ liên hệ tốc độ dài, tốc độ góc, và tần số dao động.
- Biên độ $C$ và pha ban đầu $\phi$ hoàn toàn xác định bởi điều kiện đầu (vị trí và vận tốc ban đầu).
- Mối liên hệ tròn-dao động là nền tảng của phân tích Fourier, số phức, và phân tích mạch trong miền tần số — tất cả các công cụ thiết yếu của kỹ sư cơ điện tử hiện đại.

---
*Exported from Feynman Bot*
