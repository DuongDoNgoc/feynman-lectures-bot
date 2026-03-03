---
lesson_id: 5612
lesson_type: deep_dive
approval_status: pending
exported_at: "2026-03-03T15:33:09.068165+00:00"
content_hash: 52682359ebef
chapter_number: 36
chapter_title: Chapter 36
section_number: 6
section_title: 36–5Other eyes
---
# ## Deep Dive: Vật Lý và Toán Học của Mắt Kép — Từ Lateral Inhibition đến Neural 

*Source: Chapter 36 - Chapter 36 (Section 6) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_36.html)*

## Deep Dive: Vật Lý và Toán Học của Mắt Kép — Từ Lateral Inhibition đến Neural Coding

### 1. Mã Hóa Thần Kinh: Toán Học của Pulse-Rate Modulation

Tín hiệu thần kinh được mã hóa qua tần số spike $f$ (spikes/giây). Quan hệ giữa cường độ kích thích $I$ và tần số spike thường tuân theo hàm logarithm (định luật Weber-Fechner):

$$f = k \cdot \log\left(\frac{I}{I_0}\right)$$

Trong đó:
- $k$ = hệ số độ nhạy của sợi thần kinh (phụ thuộc loại neuron)
- $I_0$ = ngưỡng kích thích tối thiểu (threshold intensity)
- $f$ tính bằng spikes/giây

Đây là lý do cảm nhận cường độ âm thanh và ánh sáng của con người có thang đo logarithm (dB, EV trong nhiếp ảnh) — hệ thần kinh tự động "linearize" input log-scale thành output tần số tuyến tính.

**Giới hạn tần số spike**: Do thời gian trơ (absolute refractory period) $\tau_r \approx 1-2$ ms, tần số spike tối đa:
$$f_{max} = \frac{1}{\tau_r} \approx 500 - 1000 \text{ spike/s}$$

Đây tương tự sampling theorem trong kỹ thuật số: tần số tối đa của encoder bị giới hạn bởi tốc độ đọc (readout rate) của counter.

### 2. Lateral Inhibition: Hệ Phương Trình Coupled Oscillators

Gọi $r_p$ là tần số spike của ommatidium $p$, $e_p$ là kích thích quang học nhận được, hệ phương trình lateral inhibition tuyến tính hóa:

$$r_p = e_p - \sum_{q \neq p, |q-p| \leq n} K(|q-p|) \cdot r_q \ \text{ nếu } r_p > 0$$

Với kernel ức chế:
$$K(d) = K_0 \cdot e^{-d/\lambda_{inh}}$$

Trong đó $d$ là khoảng cách giữa hai ommatidia và $\lambda_{inh}$ là "chiều dài ức chế" (inhibitory length constant).

Viết dạng ma trận:
$$\mathbf{r} = \mathbf{e} - \mathbf{K} \cdot \mathbf{r}$$
$$(\mathbf{I} + \mathbf{K}) \mathbf{r} = \mathbf{e}$$
$$\mathbf{r} = (\mathbf{I} + \mathbf{K})^{-1} \mathbf{e}$$

Ma trận $(\mathbf{I} + \mathbf{K})$ là ma trận Toeplitz với phần tử đường chéo bằng 1 và các phần tử ngoài đường chéo âm (ức chế). Nghịch đảo của nó tương ứng bộ lọc **high-pass không gian** (spatial high-pass filter).

### 3. Phân Tích Fourier: Lateral Inhibition như High-Pass Filter

Trong miền tần số không gian (spatial frequency domain), kernel ức chế $K(d)$ có biến đổi Fourier:

$$\hat{K}(\nu) = \frac{2 K_0 \lambda_{inh}}{1 + (2\pi \nu \lambda_{inh})^2}$$

Hàm truyền của hệ lateral inhibition:
$$H(\nu) = \frac{1}{1 + \hat{K}(\nu)} = \frac{1 + (2\pi \nu \lambda_{inh})^2}{1 + (2\pi \nu \lambda_{inh})^2 + 2 K_0 \lambda_{inh}}$$

Tại tần số không gian thấp ($\nu \to 0$):
$$H(0) = \frac{1}{1 + 2K_0 \lambda_{inh}} < 1$$

Tại tần số không gian cao ($\nu \to \infty$):
$$H(\infty) \to 1$$

Đây chính là đặc tính **high-pass filter** — thành phần DC (nền đồng đều) bị suy giảm, tần số cao (biên cạnh, chi tiết) được giữ nguyên hoặc khuếch đại.

### 4. Hiện Tượng Mach Band: Hệ Quả Vật Lý Có Thể Tính

Hiện tượng Mach band là hậu quả trực tiếp của lateral inhibition: tại ranh giới giữa vùng sáng và vùng tối, mắt người thấy một dải sáng giả tạo ở phía sáng và một dải tối giả tạo ở phía tối.

Xét phân bố cường độ bậc thang (step function): $e(x) = I_1$ với $x < 0$ và $e(x) = I_2$ với $x > 0$ ($I_2 > I_1$).

Sau lateral inhibition với kernel Gaussian $K(d) = K_0 e^{-d^2/2\sigma^2}$:

$$r(x) = e(x) - K_0 \int_{-\infty}^{+\infty} e^{-(x-x')^2/2\sigma^2} r(x') dx'$$

Giải gần đúng cho trường hợp ức chế yếu ($K_0 \ll 1$):
$$r(x) \approx e(x) - K_0 \int e^{-(x-x')^2/2\sigma^2} e(x') dx'$$

Đạo hàm của $r(x)$ có cực đại và cực tiểu ở gần vị trí ranh giới — đây chính là Mach band nhìn thấy. Biên độ Mach band:
$$\Delta r_{Mach} \approx K_0 \sqrt{\pi/2} \cdot \sigma \cdot (I_2 - I_1)$$

**Ứng dụng kỹ thuật**: Trong hệ thống AOI, Mach band artifact có thể gây false positive tại biên cạnh bình thường của chip. Kỹ sư cần filter bổ sung để loại bỏ ring artifact này khi dùng high-pass spatial filter mạnh.

### 5. Diffraction Limit của Mắt Kép: Compromise Kỹ Thuật

Mỗi ommatidium trong mắt kép có hai giới hạn cạnh tranh:

**Giới hạn nhiễu xạ**: Phân giải góc tốt hơn khi facet lớn hơn:
$$\Delta \phi_{diff} = 1.22 \frac{\lambda}{D}$$

**Giới hạn lấy mẫu**: Phân giải không gian tốt hơn khi ommatidia nhỏ hơn và dày đặc hơn — yêu cầu góc giữa các ommatidia $\Delta \phi_{samp}$ nhỏ.

Điều kiện tối ưu (Nyquist-Rayleigh matching):
$$\Delta \phi_{diff} = \Delta \phi_{samp}$$
$$1.22 \frac{\lambda}{D} = \frac{D}{2R}$$

Trong đó $R$ là bán kính cong của mắt kép. Giải ra đường kính facet tối ưu:
$$D_{opt} = \sqrt{\frac{2.44 \lambda R}{1}} = \sqrt{2.44 \lambda R}$$

Với ong mật: $R \approx 1$ mm, $\lambda = 500$ nm:
$$D_{opt} = \sqrt{2.44 \times 500 \times 10^{-9} \times 10^{-3}} \approx 35 \text{ μm}$$

Thực tế ong mật có $D \approx 25-35$ μm — rất gần với giá trị tối ưu lý thuyết! Điều này chứng tỏ tiến hóa đã "tìm ra" nghiệm của bài toán tối ưu kỹ thuật quang học.

### 6. Phân Tích Thông Tin: Compound Eye vs. Camera

Băng thông thông tin (information bandwidth) của mắt kép:
- $N_{facets}$ = số ommatidia
- Mỗi ommatidium có dải động (dynamic range) $D_R$ bit
- Tần số frame $f_{frame}$

$$B_{compound} = N_{facets} \times D_R \times f_{frame}$$

Ong mật: $N = 6000$, $D_R \approx 10$ bit, $f_{frame} \approx 100$ Hz:
$$B_{ong\ mat} \approx 6 \times 10^6 \text{ bit/s} = 6 \text{ Mbit/s}$$

Con người (fovea): $N_{cones} \approx 6 \times 10^6$, $D_R \approx 8$ bit, $f_{frame} \approx 30$ Hz:
$$B_{người} \approx 1.44 \times 10^9 \text{ bit/s} = 1.44 \text{ Gbit/s}$$

Nhưng sau lateral inhibition và compression ở retina, tín hiệu ra khỏi dây thần kinh thị giác chỉ còn khoảng $\sim 10$ Mbit/s — tỷ lệ nén $\sim 100:1$. Đây là lý do JPEG và H.264 dùng "perceptual coding" bắt chước các đặc điểm xử lý thông tin của mắt người!

### 7. Ứng Dụng Kỹ Thuật: Event Camera và Neuromorphic Vision

Dựa trên nguyên lý biological neural coding, **Event camera (Dynamic Vision Sensor — DVS)** là cảm biến thị giác thế hệ mới:
- Mỗi pixel độc lập, chỉ phát tín hiệu khi thay đổi log-intensity vượt ngưỡng $\Delta L = \pm C$
- Không có frame rate cố định — sự kiện phát sinh không đồng bộ với độ trễ $< 1$ μs
- Băng thông thực tế: chỉ xử lý thông tin thay đổi, giảm 1000x so với frame camera

**Ứng dụng trong cơ điện tử chính xác**:
- Đo lường rung (vibration measurement) với bandwidth MHz mà frame camera không thể đạt
- Tracking tốc độ cao (projectile tracking) cho ứng dụng quân sự
- Kiểm soát robot tốc độ cao (reaction time < 1 ms)

Đây là một ví dụ tiêu biểu của **neuromorphic engineering** — thiết kế phần cứng mô phỏng nguyên lý thần kinh học để đạt hiệu năng vượt trội so với kiến trúc von Neumann truyền thống.

---
*Exported from Feynman Bot*
