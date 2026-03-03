---
lesson_id: 5540
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:07.475383+00:00"
content_hash: 2ffcf4b17aec
chapter_number: 30
chapter_title: Chapter 30
section_number: 2
section_title: 30–1The resultant amplitude due tonnequal oscillators
---
# ## Nhiễu Xạ từ N Nguồn Đều Nhau — Phân tích Chuyên sâu

*Source: Chapter 30 - Chapter 30 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_30.html)*

## Nhiễu Xạ từ N Nguồn Đều Nhau — Phân tích Chuyên sâu

### Thiết lập bài toán

Xét $n$ nguồn dao động đặt cách đều nhau, khoảng cách giữa hai nguồn liên tiếp là $d$. Tất cả có cùng biên độ $A$. Hiệu pha giữa hai nguồn liên tiếp khi quan sát theo hướng $\theta$ là:

$$\phi = \alpha + \frac{2\pi d\sin\theta}{\lambda}$$

Ở đây $\alpha$ là pha nội tại (intrinsic phase difference) do cấp tín hiệu khác pha, và thành phần $2\pi d\sin\theta/\lambda$ là pha hình học (geometric phase) do hiệu đường đi.

Tổng trường tổng hợp:
$$R = A[\cos\omega t + \cos(\omega t + \phi) + \cos(\omega t + 2\phi) + \cdots + \cos(\omega t + (n-1)\phi)]$$

### Phương pháp hình học: Đa giác cung tròn

**Bước 1 — Biểu diễn phasor:**
Mỗi sóng thành phần là một phasor độ dài $A$, mỗi phasor xoay thêm góc $\phi$ so với phasor trước. Tập hợp $n$ phasor nối đầu-đuôi tạo thành một đa giác đều $n$ cạnh nằm trên cung tròn.

**Bước 2 — Tìm bán kính vòng tròn:**
Gọi bán kính vòng tròn là $r$. Mỗi cạnh của đa giác là một dây cung ứng với góc ở tâm $\phi$. Chiều dài dây cung:
$$A = 2r\sin(\phi/2) \implies r = \frac{A}{2\sin(\phi/2)}$$

**Bước 3 — Tính biên độ hợp:**
Biên độ hợp $A_R$ là dây cung ứng với toàn bộ góc $n\phi$ tại tâm:
$$A_R = 2r\sin(n\phi/2) = 2 \cdot \frac{A}{2\sin(\phi/2)} \cdot \sin(n\phi/2)$$

$$\boxed{A_R = A\frac{\sin(n\phi/2)}{\sin(\phi/2)}}$$

**Ý nghĩa vật lý của công thức:**
- Khi $\phi \to 0$: theo L'Hôpital, $A_R \to A \cdot n$ — tất cả phasor thẳng hàng, cộng tối đa
- Khi $n\phi = 2\pi k$ với $k$ nguyên: $\sin(n\phi/2) = 0$ nên $A_R = 0$ — phasor khép vòng tròn kín
- Khi $\phi = 2\pi m$ nhưng $n\phi \neq 2\pi k$: cực đại chính (principal maximum)

### Phân tích cực đại và cực tiểu

**Cực đại chính** tại $\phi = 2\pi m$ ($m = 0, \pm 1, \pm 2, ...$):
$$I_{principal} = n^2 A^2$$

**Cực tiểu đầu tiên** tại $n\phi = 2\pi$, tức $\phi = 2\pi/n$:
$$\Delta\phi_{null} = 2\pi/n \implies \Delta(d\sin\theta) = \lambda/n$$

**Bề rộng góc của cực đại chính** (từ cực đại đến cực tiểu đầu tiên):
$$\Delta\theta \approx \frac{\lambda}{nd\cos\theta} = \frac{\lambda}{L\cos\theta}$$

Trong đó $L = nd$ là **tổng chiều dài array**. Đây là kết quả cực kỳ quan trọng:

> **Độ phân giải góc tỷ lệ nghịch với tổng chiều dài array, không phụ thuộc vào số nguồn $n$**

**Cực đại phụ** (secondary maxima) xuất hiện xấp xỉ tại $n\phi/2 = \pi(2k+1)/2$, tức $\phi = (2k+1)\pi/n$:
$$I_{secondary} = A^2 \frac{1}{\sin^2((2k+1)\pi/(2n))} \approx A^2\frac{4n^2}{\pi^2(2k+1)^2}$$

Cực đại phụ thứ nhất ($k=1$) có cường độ $\approx 4n^2/(9\pi^2) \approx 4.5\%$ của cực đại chính. Đây là lý do tại sao trong thiết kế anten, người ta thường nói "sidelobe level" (mức búp sóng phụ) và cố gắng giảm nó bằng kỹ thuật tapering (điều chế biên độ).

### Liên hệ với cách tử nhiễu xạ

Khi $\alpha = 0$ (tất cả nguồn đồng pha, chiếu thẳng), điều kiện cực đại chính bậc $m$:
$$d\sin\theta_m = m\lambda \quad (m = 0, \pm 1, \pm 2, ...)$$

Mỗi bước sóng $\lambda$ khác nhau cho góc $\theta_m$ khác nhau — đây là cơ sở phân tán sắc. **Góc phân tán** $d\theta/d\lambda$:
$$\frac{d\theta_m}{d\lambda} = \frac{m}{d\cos\theta_m}$$

Nên để tăng khả năng phân tán sắc: hoặc dùng bậc cao $m$, hoặc giảm $d$ (vạch kẻ mau hơn).

### Ví dụ thực tế: Thiết kế Phased Array Lidar cho hệ thống đo xa chính xác

Trong một hệ thống đo khoảng cách dùng Lidar (Light Detection and Ranging) cho robot tự hành hoặc hệ thống dẫn đường, ta cần phân giải góc cao để phân biệt hai vật thể gần nhau.

**Bài toán:** Thiết kế phased array Lidar với bước sóng $\lambda = 1550$ nm (cửa sổ quang học an toàn cho mắt), yêu cầu phân giải góc $\Delta\theta = 0.1°$. Tính:

(a) Tổng chiều dài array $L$ cần thiết
(b) Nếu dùng $d = 10\mu$m (gần $\lambda$), cần bao nhiêu nguồn $n$?

**Giải:**

(a) Từ công thức bề rộng góc ($\theta \approx 0$, $\cos\theta \approx 1$):
$$\Delta\theta = \frac{\lambda}{L} \implies L = \frac{\lambda}{\Delta\theta} = \frac{1550 \times 10^{-9}}{0.1 \times \pi/180}$$
$$L = \frac{1550 \times 10^{-9}}{1.745 \times 10^{-3}} \approx 888 \mu\text{m} \approx 0.9 \text{ mm}$$

Kết quả: Array dài chưa đến 1 mm có thể đạt phân giải 0.1° — đây chính là lợi thế của hệ thống MEMS optical phased array trên chip silicon!

(b) Số nguồn:
$$n = \frac{L}{d} = \frac{888 \mu\text{m}}{10 \mu\text{m}} = 88.8 \approx 89 \text{ nguồn}$$

**Kiểm tra:** Cực đại phụ tại $d\sin\theta = \lambda/2$ khi $d = 10\mu$m:
$$\sin\theta_{alias} = \frac{\lambda}{d} = \frac{1.55}{10} = 0.155 \implies \theta_{alias} \approx 8.9°$$

Ngưỡng $d < \lambda$ để tránh grating lobe (búp sóng ma), nên $d = 10\mu$m với $\lambda = 1550$ nm thỏa mãn tốt.

### Bài tập mẫu

**Đề bài:** Một cách tử nhiễu xạ phản xạ có $N = 1200$ vạch/mm dùng để phân tích phổ laser. Ánh sáng chiếu thẳng góc ($\alpha = 0$). Với bước sóng $\lambda = 532$ nm (laser Nd:YAG frequency-doubled):

(a) Tính góc cực đại bậc 1
(b) Tính bề rộng vân tại cực đại bậc 1 nếu cách tử rộng $W = 25$ mm
(c) Một laser có hai mode cách nhau $\Delta\lambda = 0.01$ nm — cách tử này có phân biệt được không?

**Lời giải:**

(a) $d = 1/1200$ mm $\approx 833$ nm. Cực đại bậc 1: $\sin\theta_1 = \lambda/d = 532/833 = 0.639 \implies \theta_1 = 39.7°$

(b) $n = W/d = 25\text{ mm} / (0.833\mu\text{m}) = 30000$ vạch. Bề rộng góc:
$$\Delta\theta = \frac{\lambda}{W\cos\theta_1} = \frac{532\times10^{-9}}{25\times10^{-3} \times \cos(39.7°)} = 2.75 \times 10^{-5} \text{ rad} = 0.00158°$$

(c) Độ phân giải bước sóng theo Rayleigh:
$$\Delta\lambda_{min} = \frac{\lambda}{mn} = \frac{532}{1 \times 30000} = 0.0177 \text{ nm}$$

Vì $\Delta\lambda = 0.01$ nm $< \Delta\lambda_{min} = 0.0177$ nm, cách tử này **không phân biệt** được hai mode. Cần cách tử rộng hơn hoặc dùng bậc cao hơn.

### Tổng kết

Công thức $A_R = A\sin(n\phi/2)/\sin(\phi/2)$ là nền tảng của toàn bộ lý thuyết anten array và quang học nhiễu xạ. Từ đây suy ra: độ phân giải góc $\propto 1/L$ (chiều dài array), cường độ cực đại $\propto n^2$ (không phải $n$), và hình dạng vân nhiễu xạ hoàn toàn do tích lũy pha mà ra.

---
*Exported from Feynman Bot*
