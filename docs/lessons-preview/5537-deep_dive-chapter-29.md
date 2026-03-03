---
lesson_id: 5537
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:07.401806+00:00"
content_hash: 572def1e942b
chapter_number: 29
chapter_title: Chapter 29
section_number: 6
section_title: 29–5The mathematics of interference
---
# ## Cộng Hai Sóng Có Pha Khác Nhau — Phân tích Chuyên sâu

*Source: Chapter 29 - Chapter 29 (Section 6) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_29.html)*

## Cộng Hai Sóng Có Pha Khác Nhau — Phân tích Chuyên sâu

### Bài toán tổng quát

Khi bạn thiết kế một hệ thống anten phased-array (dàn anten điều khiển pha) cho radar hoặc hệ thống dẫn đường, bạn luôn phải đối mặt với câu hỏi cốt lõi: **làm thế nào để tính biên độ và pha của tín hiệu tổng hợp từ nhiều nguồn phát có pha khác nhau?** Đây chính là bài toán mà chúng ta sẽ phân tích chi tiết hôm nay.

Xét trường hợp tổng quát nhất: hai nguồn dao động có biên độ $A_1$, $A_2$ và pha ban đầu $\phi_1$, $\phi_2$ khác nhau. Tổng trường tại một điểm quan sát là:

$$R = A_1 \cos(\omega t + \phi_1) + A_2 \cos(\omega t + \phi_2)$$

Hiệu pha $\phi_1 - \phi_2$ được tạo thành từ hai thành phần:
1. **Pha hình học** — do sự chênh lệch khoảng cách từ hai nguồn tới điểm quan sát: $\Delta\phi_{geo} = 2\pi d \sin\theta / \lambda$
2. **Pha nội tại** — pha riêng của từng nguồn dao động: $\alpha$

### Phương pháp 1: Lượng giác

Trường hợp đơn giản nhất khi $A_1 = A_2 = A$, ta áp dụng công thức lượng giác:

$$\cos A + \cos B = 2\cos\frac{A+B}{2}\cos\frac{A-B}{2}$$

Áp dụng vào bài toán với $A = \omega t + \phi_1$ và $B = \omega t + \phi_2$:

$$R = 2A\cos\left(\frac{\phi_1 - \phi_2}{2}\right)\cos\left(\omega t + \frac{\phi_1 + \phi_2}{2}\right)$$

**Ý nghĩa vật lý của từng thành phần:**
- $2A\cos\left(\frac{\phi_1 - \phi_2}{2}\right)$: Đây là **biên độ hợp** $A_R$. Giá trị này phụ thuộc hoàn toàn vào hiệu pha giữa hai nguồn, không phụ thuộc vào thời gian.
- $\cos\left(\omega t + \frac{\phi_1 + \phi_2}{2}\right)$: Sóng hợp dao động với **pha trung bình** của hai sóng thành phần.

**Khi nào giao thoa tăng cường?** Khi $\phi_1 - \phi_2 = 0$ (hai sóng cùng pha): $A_R = 2A$ — biên độ tối đa.
**Khi nào giao thoa triệt tiêu?** Khi $\phi_1 - \phi_2 = \pi$ (hai sóng ngược pha): $A_R = 0$.

### Phương pháp 2: Phép cộng vectơ quay (Phasor)

Đây là phương pháp mạnh mẽ hơn, dùng được cho cả trường hợp $A_1 \neq A_2$.

**Nguyên tắc:** Bất kỳ hàm $A\cos(\omega t + \phi)$ nào đều có thể biểu diễn như hình chiếu theo trục ngang của một vectơ quay (phasor) có độ dài $A$ và góc $\phi$ so với trục chuẩn.

Cụ thể:
- Phasor 1: vectơ $\vec{A}_1$ có độ dài $A_1$, góc $\phi_1$
- Phasor 2: vectơ $\vec{A}_2$ có độ dài $A_2$, góc $\phi_2$

Toàn bộ hệ quay với vận tốc góc $\omega$, nhưng **vị trí tương đối của hai phasor cố định** (hệ cứng quay), vì chúng cùng tần số. Tổng hợp theo quy tắc hình bình hành:

$$A_R^2 = A_1^2 + A_2^2 + 2A_1 A_2 \cos(\phi_1 - \phi_2)$$

$$\tan\phi_R = \frac{A_1\sin\phi_1 + A_2\sin\phi_2}{A_1\cos\phi_1 + A_2\cos\phi_2}$$

Phương pháp phasor đặc biệt hữu ích vì:
- Không cần nhớ công thức lượng giác phức tạp
- Dễ mở rộng cho $n$ nguồn (thêm $n$ phasor nối tiếp đầu-đuôi)
- Trực quan về mặt hình học

### Ứng dụng thực tế: Hệ thống Phased Array Radar

Trong kỹ thuật cơ điện tử và vũ khí, phased array radar sử dụng mảng anten để định hướng chùm tia điện từ mà không cần xoay cơ học. Đây là ứng dụng trực tiếp của lý thuyết cộng sóng.

**Bài toán cụ thể:** Một dàn radar gồm 2 anten cách nhau $d = 5$ cm, phát sóng tần số $f = 10$ GHz (bước sóng $\lambda = 3$ cm). Chúng ta muốn định hướng chùm tia về góc $\theta = 30°$ so với phương thẳng đứng.

**Giải:**

Bước 1: Tính hiệu lộ trình hình học tới một điểm xa ở góc $\theta$:
$$\Delta L = d\sin\theta = 5 \times \sin 30° = 2.5 \text{ cm}$$

Bước 2: Tính pha hình học tương ứng:
$$\Delta\phi_{geo} = \frac{2\pi \Delta L}{\lambda} = \frac{2\pi \times 2.5}{3} \approx 5.24 \text{ rad}$$

Bước 3: Để chùm tia cực đại về phía $\theta = 30°$, ta cần giao thoa tăng cường tại đó, tức là hiệu pha tổng phải bằng $0$ (hoặc $2\pi m$). Do pha hình học là $5.24$ rad, ta cần **bù pha nội tại** $\alpha = -5.24$ rad (hay tương đương $+\Delta\phi_{drive}$ điều khiển qua mạch điện tử).

Bước 4: Biên độ tại góc $\theta = 30°$:
$$A_R = 2A\cos\left(\frac{0}{2}\right) = 2A$$

**Thực tế:** Các hệ thống phased array hiện đại (như AN/APG-81 trên F-35) có hàng ngàn phần tử anten, mỗi phần tử được điều khiển pha độc lập bởi vi mạch T/R module, cho phép quét chùm tia trong vài microsecond.

### Bài tập mẫu có lời giải

**Đề bài:** Hai nguồn sóng siêu âm (dùng trong đo lường chính xác vị trí) phát sóng tần số $f = 40$ kHz (bước sóng trong không khí $\lambda = 8.5$ mm), biên độ bằng nhau $A = 1$ V. Nguồn 1 tại $x = 0$, nguồn 2 tại $x = 10$ mm. Hai nguồn đồng pha ($\alpha = 0$). Tính biên độ tổng hợp tại điểm $P$ nằm trên trục vuông góc tại $x = 5$ mm, cách đường nối hai nguồn $y = 100$ mm.

**Lời giải từng bước:**

Bước 1 — Tính khoảng cách từ mỗi nguồn đến P:
$$r_1 = \sqrt{5^2 + 100^2} = \sqrt{10025} \approx 100.12 \text{ mm}$$
$$r_2 = \sqrt{5^2 + 100^2} = \sqrt{10025} \approx 100.12 \text{ mm}$$

Bước 2 — Hiệu khoảng cách:
$$\Delta r = r_1 - r_2 = 0 \text{ mm}$$

Bước 3 — Hiệu pha:
$$\Delta\phi = \frac{2\pi \Delta r}{\lambda} + \alpha = 0 + 0 = 0$$

Bước 4 — Biên độ hợp:
$$A_R = 2A\cos\left(\frac{\Delta\phi}{2}\right) = 2 \times 1 \times \cos(0) = 2 \text{ V}$$

**Nhận xét:** Điểm P nằm trên đường đối xứng, hai nguồn cách đều nhau, nên giao thoa tăng cường hoàn toàn. Đây là nguyên lý hoạt động của cảm biến siêu âm mảng (ultrasonic phased array) dùng trong kiểm tra không phá hủy (NDT — Non-Destructive Testing).

### Mở rộng: Biểu diễn số phức

Trong kỹ thuật, người ta thường dùng ký hiệu số phức cho phasor:
$$\tilde{A}_1 = A_1 e^{j\phi_1}, \quad \tilde{A}_2 = A_2 e^{j\phi_2}$$
$$\tilde{R} = \tilde{A}_1 + \tilde{A}_2$$
$$A_R = |\tilde{R}|, \quad \phi_R = \arg(\tilde{R})$$

Cách này đặc biệt tiện lợi khi lập trình DSP (Digital Signal Processing) hoặc phân tích mạch RF với phần mềm MATLAB/Python.

### Tổng kết

Phương pháp phasor là công cụ bất biến trong kỹ thuật điện tử và cơ điện tử: từ thiết kế bộ lọc tín hiệu, mạch khuếch đại vi sai, cho đến điều khiển pha trong radar và sonar. Hiểu sâu nguyên lý cộng sóng bằng phasor cho phép bạn thiết kế các hệ thống can thiệp sóng một cách có chủ đích, không chỉ áp dụng công thức một cách mù quáng.

---
*Exported from Feynman Bot*
