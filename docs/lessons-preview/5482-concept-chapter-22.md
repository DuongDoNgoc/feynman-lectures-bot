---
lesson_id: 5482
lesson_type: concept
approval_status: approved
exported_at: "2026-03-03T15:33:06.154374+00:00"
content_hash: 5874c20b7cf2
chapter_number: 22
chapter_title: Chapter 22
section_number: 6
section_title: 22–5Complex numbers
---
# ## Số Phức và Đơn vị Ảo $i$ — Khi Toán Học Mở Rộng Thế Giới Số

*Source: Chapter 22 - Chapter 22 (Section 6) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_22.html)*

## Số Phức và Đơn vị Ảo $i$ — Khi Toán Học Mở Rộng Thế Giới Số

### Câu hỏi mở đầu: Tại sao bình phương mọi số đều dương?

Khi bạn đo ứng suất cơ học trong vỏ súng bằng strain gauge, bình phương của bất kỳ điện áp đầu ra nào cũng dương — $(-5V)^2 = 25V^2 > 0$. Điều này có vẻ là quy luật bất biến của tự nhiên. Nhưng điều gì xảy ra khi phương trình $x^2 = -1$ xuất hiện trong tính toán kỹ thuật? Đây không phải câu hỏi học thuật — bất kỳ kỹ sư nào làm việc với mạch điện AC, xử lý tín hiệu, hay điều khiển tự động đều gặp câu hỏi này hàng ngày.

### Phát minh đơn vị ảo $i$

Ta định nghĩa một ký hiệu mới:
$$i^2 = -1 \quad \Leftrightarrow \quad i = \sqrt{-1}$$

Đây là sự **mở rộng định nghĩa** — không phải "số mới xuất hiện trong tự nhiên", mà là ta *phát minh* ra một công cụ toán học mới. Lưu ý rằng $-i$ cũng là một nghiệm vì $(-i)^2 = i^2 = -1$. Điều này có nghĩa: phương trình $x^2 = -1$ có hai nghiệm là $i$ và $-i$, hoàn toàn đối xứng.

Phép lấy liên hợp phức (complex conjugate): đổi dấu của $i$ ở mọi nơi trong một biểu thức. Mọi đẳng thức đều vẫn đúng khi lấy liên hợp phức — tính chất đối xứng này là nền tảng của nhiều định lý quan trọng.

### Số phức: Dạng tổng quát

Khi ta thực hiện mọi phép toán đại số với $i$ (cộng, trừ, nhân, chia), kết quả luôn có dạng:
$$z = p + iq$$

Trong đó $p$ (phần thực, real part) và $q$ (phần ảo, imaginary part) là các số thực thông thường. Ví dụ phép nhân:
$$(r + is)(p + iq) = (rp - sq) + i(rq + sp)$$

Chỉ cần nhớ $i^2 = -1$ và áp dụng quy tắc phân phối thông thường.

**Định lý kỳ diệu:** Với số phức $i$, *mọi* phương trình đại số $a_n z^n + \cdots + a_1 z + a_0 = 0$ đều có nghiệm. Không cần phát minh thêm bất kỳ loại số mới nào! Đây là Định lý Cơ bản của Đại số (Fundamental Theorem of Algebra).

### Phép so sánh với kỹ sư cơ điện tử

Hãy nghĩ đến hệ tọa độ 2D trong không gian làm việc của robot 6 bậc tự do trong hệ thống lắp ráp vũ khí tự động. Để mô tả vị trí của end-effector, bạn cần hai số: tọa độ $x$ và $y$. Số phức $z = x + iy$ chính xác là một điểm trong mặt phẳng 2D:
- Phần thực $p$ = tọa độ trục hoành
- Phần ảo $q$ = tọa độ trục tung

Phép nhân số phức không chỉ là phép nhân số — nó là phép **quay và tỷ lệ** trong mặt phẳng. Khi bạn nhân $z$ với $e^{i\theta}$, bạn đang xoay điểm $z$ một góc $\theta$ quanh gốc tọa độ. Đây chính xác là phép biến đổi tọa độ mà bạn cần trong robot kinematics.

### Dạng cực và công thức Euler

Số phức $z = p + iq$ có thể viết ở dạng cực:
$$z = re^{i\theta}$$

Trong đó:
- $r = |z| = \sqrt{p^2 + q^2}$ (modulus — biên độ)
- $\theta = \arg(z) = \arctan(q/p)$ (argument — góc pha)

Công thức Euler kết nối hai dạng:
$$e^{i\theta} = \cos\theta + i\sin\theta$$

Khi nhân $z_1 \cdot z_2$: biên độ nhân với biên độ, góc pha cộng với góc pha:
$$r_1 e^{i\theta_1} \cdot r_2 e^{i\theta_2} = r_1 r_2 \, e^{i(\theta_1+\theta_2)}$$

Đây là lý do phasor cực kỳ mạnh mẽ trong phân tích mạch AC: nhân impedance chỉ là nhân biên độ và cộng pha.

### Ứng dụng: Impedance và mạch RLC

Trong thiết kế mạch lọc cho cảm biến gia tốc MEMS (dùng trong đầu đạn dẫn đường), impedance của tụ điện và cuộn cảm là số phức:
$$Z_C = \frac{1}{j\omega C} = -\frac{j}{\omega C} \quad (\text{thuần ảo, âm})$$
$$Z_L = j\omega L \quad (\text{thuần ảo, dương})$$

Tổng trở của mạch RLC nối tiếp:
$$Z_{total} = R + j\omega L + \frac{1}{j\omega C} = R + j\left(\omega L - \frac{1}{\omega C}\right)$$

Tại tần số cộng hưởng $\omega_0 = 1/\sqrt{LC}$, phần ảo triệt tiêu, $Z_{total} = R$ (thuần thực, biên độ nhỏ nhất). Không có số phức, không thể hiểu được cộng hưởng!

**Điểm mấu chốt:**
- Số $i = \sqrt{-1}$ không phải "số tưởng tượng" hay "không tồn tại" — đây là phát minh toán học tất yếu để giải mọi phương trình đại số.
- Số phức $z = p + iq$ biểu diễn điểm (hoặc vector) trong mặt phẳng 2D — phép nhân số phức là phép quay + tỷ lệ.
- Dạng cực $z = re^{i\theta}$ thuận tiện cho phép nhân/chia; dạng Đề-các $p + iq$ thuận tiện cho phép cộng/trừ.
- Trong kỹ thuật điện tử và cơ điện tử, số phức là ngôn ngữ tự nhiên của mọi hiện tượng dao động, sóng, và mạch AC.

---
*Exported from Feynman Bot*
