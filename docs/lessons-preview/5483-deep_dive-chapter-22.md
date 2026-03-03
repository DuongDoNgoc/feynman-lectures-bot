---
lesson_id: 5483
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:06.188836+00:00"
content_hash: cc91ad52feb2
chapter_number: 22
chapter_title: Chapter 22
section_number: 6
section_title: 22–5Complex numbers
---
# ## Số Phức và Đại số Phức — Phân tích Chuyên sâu

*Source: Chapter 22 - Chapter 22 (Section 6) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_22.html)*

## Số Phức và Đại số Phức — Phân tích Chuyên sâu

### Tại sao $x^2 = -1$ không có nghiệm thực?

Trong hệ số thực, bình phương của mọi số đều không âm: $x^2 \geq 0$ với mọi $x \in \mathbb{R}$. Phương trình $x^2 = -1$ không có nghiệm thực — đây là sự thật hiển nhiên, không phải giới hạn của trí tưởng tượng. Để giải phương trình này, ta *phải* mở rộng tập số.

### Định nghĩa và tính chất của $i$

Ta đặt $i$ là một nghiệm của $x^2 + 1 = 0$, tức là $i^2 = -1$. Từ đây:
$$i^1 = i, \quad i^2 = -1, \quad i^3 = -i, \quad i^4 = 1, \quad i^5 = i, \ldots$$

Lũy thừa của $i$ tuần hoàn với chu kỳ 4. Kỳ diệu hơn: $-i$ cũng là nghiệm vì $(-i)^2 = (-1)^2 \cdot i^2 = 1 \cdot (-1) = -1$.

**Liên hợp phức (complex conjugate):** Với $z = p + iq$, ta định nghĩa $\bar{z} = p - iq$. Quan trọng: $z \cdot \bar{z} = (p+iq)(p-iq) = p^2 + q^2 = |z|^2$ — luôn dương, luôn thực.

### Phép nhân số phức: Chứng minh từng bước

Gọi hai số phức $z_1 = r + is$ và $z_2 = p + iq$. Ta tính:

$$z_1 \cdot z_2 = (r + is)(p + iq)$$

**Bước 1:** Phân phối (giống nhân nhị thức):
$$(r + is)(p + iq) = r \cdot p + r \cdot (iq) + (is) \cdot p + (is) \cdot (iq)$$

**Bước 2:** Áp dụng tính kết hợp và giao hoán:
$$= rp + i(rq) + i(sp) + i^2(sq)$$

**Bước 3:** Thay $i^2 = -1$:
$$= rp + i(rq) + i(sp) - sq$$

**Bước 4:** Nhóm phần thực và phần ảo:
$$= (rp - sq) + i(rq + sp)$$

*Ý nghĩa:* Kết quả vẫn có dạng $a + ib$ — tập số phức đóng dưới phép nhân. Không có số mới nào xuất hiện.

### Định lý cơ bản của đại số

**Phát biểu:** Mọi phương trình đa thức $a_n z^n + a_{n-1}z^{n-1} + \cdots + a_1 z + a_0 = 0$ (với $a_n \neq 0$ và các hệ số là số phức) đều có ít nhất một nghiệm phức.

Hệ quả: phương trình bậc $n$ có đúng $n$ nghiệm (kể cả nghiệm bội và nghiệm phức) trong tập số phức $\mathbb{C}$.

Đây là lý do Feynman gọi số phức là "phát minh cuối cùng" — không cần mở rộng thêm nữa. Mọi phương trình đại số đều giải được trong $\mathbb{C}$.

### Lũy thừa phức của số phức

Ta muốn tính $10^{r+is}$ (mũ phức). Dùng quy tắc lũy thừa:
$$10^{r+is} = 10^r \cdot 10^{is}$$

$10^r$ — đã biết cách tính (lũy thừa thực).

$10^{is}$ — cần tính lũy thừa ảo. Ta biết $10 = e^{\ln 10}$, nên:
$$10^{is} = e^{is \ln 10} = \cos(s \ln 10) + i\sin(s \ln 10)$$

(dùng công thức Euler). Vậy:
$$\boxed{10^{r+is} = 10^r[\cos(s\ln 10) + i\sin(s\ln 10)]}$$

Phần thực và phần ảo đều xác định — không có gì "ảo" cả!

### Biểu diễn hình học: Mặt phẳng phức

Số phức $z = x + iy$ là một điểm trong mặt phẳng 2D (mặt phẳng Argand hay mặt phẳng phức):
- Trục hoành (real axis): phần thực $x$
- Trục tung (imaginary axis): phần ảo $y$

Dạng cực: $z = re^{i\theta}$, với $r = \sqrt{x^2+y^2}$ và $\theta = \arctan(y/x)$.

Phép nhân hình học:
$$z_1 \cdot z_2 = r_1 e^{i\theta_1} \cdot r_2 e^{i\theta_2} = r_1 r_2 \, e^{i(\theta_1+\theta_2)}$$

Biên độ nhân, góc pha cộng — đây là phép quay + tỷ lệ trong mặt phẳng.

### Ví dụ thực tế: Phân tích tín hiệu cảm biến rung động

Trong hệ thống giám sát rung động (vibration monitoring) của máy CNC độ chính xác cao (dùng gia công chi tiết micro ở cấp micromet), cảm biến accelerometer MEMS đầu ra tín hiệu:
$$a(t) = A_1\cos(\omega_1 t + \phi_1) + A_2\cos(\omega_2 t + \phi_2)$$

Để phân tích biên độ và pha của từng thành phần, ta dùng biến đổi Fourier rời rạc (DFT). Hệ số DFT:
$$X[k] = \sum_{n=0}^{N-1} x[n] e^{-j2\pi kn/N}$$

Đây là một số phức $X[k] = |X[k]|e^{i\angle X[k]}$ — biên độ $|X[k]|$ cho biết cường độ rung động ở tần số $f_k$, còn pha $\angle X[k]$ cho biết thời điểm bắt đầu của rung động.

Nếu $|X[k_1]|$ tăng đột biến, hệ thống phát hiện được cộng hưởng bất thường — dấu hiệu mòn vòng bi hay mất cân bằng. Không có số phức (cụ thể là $e^{-j2\pi kn/N}$), không thể thực hiện DFT.

### Ứng dụng: Điều khiển vị trí sub-micromet

Trong hệ thống servo của máy đo tọa độ (CMM — Coordinate Measuring Machine) với độ phân giải nanomét, hàm truyền vòng kín:
$$G_{cl}(s) = \frac{G(s)}{1 + G(s)H(s)}$$

Cực (poles) của $G_{cl}(s)$ là nghiệm phức của $1 + G(s)H(s) = 0$. Vị trí cực trong mặt phẳng phức xác định:
- Phần thực âm: hệ thống ổn định
- Phần ảo: tần số dao động
- Khoảng cách đến trục ảo: hệ số tắt dần

Kỹ sư điều khiển "thiết kế" vị trí cực trong mặt phẳng phức — đây là ngôn ngữ hàng ngày của họ.

### Bài tập mẫu: Tìm căn bậc hai của số phức

**Đề bài:** Tính $\sqrt{i}$ (căn bậc hai của đơn vị ảo).

**Lời giải từng bước:**

**Bước 1:** Đặt $\sqrt{i} = a + ib$ (giả sử nghiệm có dạng số phức tổng quát).

**Bước 2:** Bình phương hai vế:
$$(a + ib)^2 = i$$
$$a^2 - b^2 + 2abi = 0 + 1\cdot i$$

*Ý nghĩa:* Phần thực bằng phần thực, phần ảo bằng phần ảo.

**Bước 3:** Đồng nhất hệ số:
$$a^2 - b^2 = 0 \quad \Rightarrow \quad a^2 = b^2 \quad \Rightarrow \quad a = \pm b$$
$$2ab = 1 \quad \Rightarrow \quad ab = \frac{1}{2}$$

**Bước 4:** Giải hệ:
Nếu $a = b$: $a^2 = 1/2 \Rightarrow a = \pm 1/\sqrt{2}$.
Vậy hai nghiệm là $\frac{1+i}{\sqrt{2}}$ và $-\frac{1+i}{\sqrt{2}}$.

**Bước 5:** Kiểm tra bằng dạng cực.
$i = e^{i\pi/2}$. Vậy $\sqrt{i} = e^{i\pi/4} = \cos(45°) + i\sin(45°) = \frac{1}{\sqrt{2}} + \frac{i}{\sqrt{2}} = \frac{1+i}{\sqrt{2}}$ ✓

*Ý nghĩa kỹ thuật:* Trong phân tích tín hiệu, căn bậc hai của số phức xuất hiện khi tính biên độ và pha từ tín hiệu IQ (in-phase/quadrature) trong radar và thông tin vô tuyến — kỹ thuật cốt lõi trong vũ khí dẫn đường hiện đại.

**Điểm mấu chốt:**
- $i^2 = -1$ là định nghĩa mở rộng hợp lý — không mâu thuẫn với đại số đã có.
- Phép nhân $(r+is)(p+iq) = (rp-sq) + i(rq+sp)$ tuân thủ đúng quy tắc phân phối với $i^2=-1$.
- Định lý cơ bản đại số: số phức là đủ — không cần phát minh thêm.
- Lũy thừa phức: $10^{r+is} = 10^r(\cos(s\ln 10) + i\sin(s\ln 10))$ kết hợp exponential với dao động tuần hoàn.

---
*Exported from Feynman Bot*
