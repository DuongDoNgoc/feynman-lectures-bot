---
lesson_id: 5477
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-02T15:10:30.496574+00:00"
content_hash: d673f244201a
chapter_number: 22
chapter_title: Chapter 22
section_number: 2
section_title: 22–1Addition and multiplication
---
# ## Công thức Euler và Đại số Phức — Phân tích Chuyên sâu

*Source: Chapter 22 - Chapter 22 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_22.html)*

## Công thức Euler và Đại số Phức — Phân tích Chuyên sâu

### Tại sao kỹ sư cơ điện tử cần đại số phức?

Khi bạn thiết kế một bộ lọc thông thấp cho cảm biến gia tốc trong hệ thống dẫn đường quán tính (INS) của tên lửa dẫn đường, bạn không thể tránh khỏi phải làm việc với số phức. Impedance $Z = R + j\omega L$ của cuộn cảm, hàm truyền $H(j\omega)$ của bộ lọc, góc pha của tín hiệu cảm biến — tất cả đều sống trong không gian số phức. Feynman gọi công thức Euler là "công thức đáng kinh ngạc nhất trong toàn bộ toán học" và ông không hề cường điệu.

### Nền tảng đại số: từ số nguyên đến số phức

Hành trình xây dựng hệ thống số bắt đầu từ những thứ đơn giản nhất. Từ phép đếm, ta định nghĩa phép cộng: bắt đầu từ $a$, đếm thêm $b$ lần, ta được $a + b$. Từ phép cộng lặp lại, ta có phép nhân. Từ phép nhân lặp lại, ta có lũy thừa $a^b$.

Quy tắc cơ bản của đại số (rules of algebra) bao gồm:
- Giao hoán: $a + b = b + a$, $ab = ba$
- Kết hợp: $(a+b)+c = a+(b+c)$
- Phân phối: $a(b+c) = ab + ac$
- Phần tử đơn vị: $a + 0 = a$, $a \cdot 1 = a$

Quy tắc lũy thừa quan trọng:
$$a^s \cdot a^t = a^{s+t}, \quad (a^s)^t = a^{st}$$

Khi muốn giải phương trình $x + a = 0$, ta phát minh số âm. Khi muốn giải $bx = a$, ta phát minh số hữu tỉ. Khi muốn giải $x^2 = 2$, ta phát minh số vô tỉ. Và khi muốn giải $x^2 = -1$, ta buộc phải phát minh **số phức**.

### Công thức Euler: viên ngọc của toán học

Ta định nghĩa $e$ là số cơ sở tự nhiên (natural base), xấp xỉ $2.71828...$, với tính chất:
$$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots$$

Thay $x = i\theta$ vào chuỗi Taylor:
$$e^{i\theta} = 1 + i\theta + \frac{(i\theta)^2}{2!} + \frac{(i\theta)^3}{3!} + \frac{(i\theta)^4}{4!} + \cdots$$

Vì $i^2 = -1$, $i^3 = -i$, $i^4 = 1$, ta thu gọn:
$$e^{i\theta} = \left(1 - \frac{\theta^2}{2!} + \frac{\theta^4}{4!} - \cdots\right) + i\left(\theta - \frac{\theta^3}{3!} + \frac{\theta^5}{5!} - \cdots\right)$$

Nhận ra ngay chuỗi Taylor của $\cos\theta$ và $\sin\theta$:
$$\boxed{e^{i\theta} = \cos\theta + i\sin\theta}$$

Đây là **công thức Euler** (Euler's formula). Khi $\theta = \pi$:
$$e^{i\pi} + 1 = 0$$

Năm hằng số quan trọng nhất toán học ($e$, $i$, $\pi$, $1$, $0$) gặp nhau trong một đẳng thức duy nhất.

### Ý nghĩa hình học

Số phức $z = re^{i\theta}$ biểu diễn một điểm trên mặt phẳng phức (complex plane) với:
- $r$ = modulus (độ lớn), khoảng cách từ gốc đến điểm
- $\theta$ = argument (góc pha), góc với trục thực dương

Phép nhân hai số phức:
$$r_1 e^{i\theta_1} \cdot r_2 e^{i\theta_2} = r_1 r_2 \, e^{i(\theta_1 + \theta_2)}$$

Đây là phép **quay và tỷ lệ** trong mặt phẳng! Nhân với $e^{i\theta}$ đồng nghĩa với xoay vector góc $\theta$.

### Ứng dụng thực tế: Phân tích tín hiệu cảm biến IMU

Trong hệ thống cơ điện tử, cảm biến IMU (Inertial Measurement Unit) trong vũ khí dẫn đường cần đo gia tốc và vận tốc góc với độ chính xác micromet. Tín hiệu đầu ra thường là dạng $A\cos(\omega t + \phi)$.

Thay vì xử lý hàm lượng giác phức tạp, ta viết:
$$A\cos(\omega t + \phi) = \text{Re}\left\{A e^{i(\omega t + \phi)}\right\} = \text{Re}\left\{\hat{A} e^{i\omega t}\right\}$$

Trong đó phasor $\hat{A} = Ae^{i\phi}$ chứa đầy đủ thông tin biên độ và pha. Phép cộng tín hiệu trở thành phép cộng vector trên mặt phẳng phức — đơn giản và trực quan hơn rất nhiều.

### Bài tập mẫu: Tính tổng tín hiệu giao thoa

**Đề bài:** Một hệ đo interferometry laser (laser interferometry) dùng để đo dịch chuyển ở độ phân giải nanomét nhận hai tín hiệu:
- Tín hiệu 1: $x_1(t) = 3\cos(\omega t)$
- Tín hiệu 2: $x_2(t) = 4\cos(\omega t + 90°)$

Tính biên độ và pha của tín hiệu tổng hợp $x(t) = x_1(t) + x_2(t)$.

**Lời giải từng bước:**

**Bước 1:** Chuyển sang dạng phasor
$$\hat{X}_1 = 3e^{i \cdot 0} = 3 + 0i$$
$$\hat{X}_2 = 4e^{i\pi/2} = 4(\cos 90° + i\sin 90°) = 0 + 4i$$

*Ý nghĩa:* Mỗi tín hiệu được biểu diễn bằng một vector trên mặt phẳng phức. Phasor $\hat{X}_1$ nằm trên trục thực, $\hat{X}_2$ nằm trên trục ảo.

**Bước 2:** Cộng hai phasor (cộng vector)
$$\hat{X} = \hat{X}_1 + \hat{X}_2 = (3 + 0i) + (0 + 4i) = 3 + 4i$$

*Ý nghĩa:* Trong không gian phức, phép cộng tín hiệu tương đương phép cộng vector — không cần dùng công thức lượng giác phức tạp.

**Bước 3:** Tính biên độ (modulus)
$$A = |\hat{X}| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$$

**Bước 4:** Tính góc pha
$$\phi = \arctan\left(\frac{4}{3}\right) \approx 53.13°$$

**Kết quả:** $x(t) = 5\cos(\omega t + 53.13°)$

*Ý nghĩa vật lý:* Hai sóng ánh sáng lệch pha 90° với biên độ 3 và 4 (đơn vị tùy ý) khi giao thoa tạo ra sóng kết quả biên độ 5, lệch pha 53.13° so với sóng gốc. Đây chính là định lý Pythagoras trong không gian pha!

### Ứng dụng nâng cao: Phân tích đáp ứng tần số

Trong thiết kế servo drive cho hệ thống định vị micrometer, hàm truyền vòng hở:
$$G(s) = \frac{K}{s(\tau s + 1)}$$

Khi $s = j\omega$ (thay thế Laplace bằng Fourier), $G(j\omega) = |G(j\omega)|e^{i\angle G(j\omega)}$.

Biên độ $|G(j\omega)|$ và pha $\angle G(j\omega)$ là các hàm thực của $\omega$ — chính là nội dung của biểu đồ Bode. Không có số phức, không có điều khiển tự động hiện đại.

**Điểm mấu chốt:**
- Đại số có một hệ quy tắc nhất quán; số phức là mở rộng tự nhiên cuối cùng của hệ thống số.
- Công thức Euler $e^{i\theta} = \cos\theta + i\sin\theta$ kết nối hàm mũ với dao động tuần hoàn.
- Phasor (số phức) biến phép cộng tín hiệu hình sin thành phép cộng vector đơn giản.
- Trong cơ điện tử, số phức không phải là thứ "toán học trừu tượng" — chúng là ngôn ngữ tự nhiên để mô tả mọi hiện tượng dao động và sóng.

---
*Exported from Feynman Bot*
