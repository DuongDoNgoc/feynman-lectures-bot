---
lesson_id: 5456
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:05.468129+00:00"
content_hash: 6f3ef715850b
chapter_number: 19
chapter_title: Chapter 19
section_number: 2
section_title: 19–1Properties of the center of mass
---
# ## Trung Tâm Khối và Động Lực Học Hệ Hạt — Phân tích Chuyên sâu

*Source: Chapter 19 - Chapter 19 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_19.html)*

## Trung Tâm Khối và Động Lực Học Hệ Hạt — Phân tích Chuyên sâu

### 1. Chứng Minh Phương Trình Chuyển Động của CM

Xét hệ $N$ hạt với khối lượng $m_i$ và vị trí $\vec{r}_i$. Phương trình Newton cho hạt $i$:
$$\vec{F}_i^{\text{ext}} + \sum_{j\neq i}\vec{F}_{ij} = m_i \ddot{\vec{r}}_i$$

trong đó $\vec{F}_{ij}$ là lực từ hạt $j$ lên hạt $i$ (nội lực). Lấy tổng trên toàn bộ hệ:
$$\sum_i \vec{F}_i^{\text{ext}} + \sum_i\sum_{j\neq i}\vec{F}_{ij} = \sum_i m_i \ddot{\vec{r}}_i$$

Theo Newton 3: $\vec{F}_{ij} = -\vec{F}_{ji}$, nên tổng đôi nội lực triệt tiêu:
$$\sum_i\sum_{j\neq i}\vec{F}_{ij} = 0$$

Định nghĩa tổng khối lượng $M = \sum_i m_i$ và vị trí CM:
$$\vec{R}_{\text{CM}} = \frac{\sum_i m_i \vec{r}_i}{M}$$

Suy ra:
$$M\ddot{\vec{R}}_{\text{CM}} = \vec{F}_{\text{ext}}$$

Đây là kết quả cốt lõi: **trung tâm khối chuyển động như thể toàn bộ khối lượng $M$ tập trung tại đó và chịu tổng ngoại lực**. Nội lực (dù phức tạp đến đâu) không ảnh hưởng đến chuyển động CM.

### 2. Tính Toán Vị Trí CM: Từ Rời Rạc đến Liên Tục

**Hệ rời rạc** (hữu hạn số hạt):
$$X_{\text{CM}} = \frac{\sum_i m_i x_i}{\sum_i m_i}$$

**Vật thể liên tục** (phân phối khối lượng liên tục):
$$X_{\text{CM}} = \frac{\int x \, dm}{\int dm} = \frac{\int x \rho(x,y,z) \, dV}{M}$$

trong đó $\rho(x,y,z)$ là mật độ khối lượng tại điểm $(x,y,z)$.

### 3. Tính CM cho Các Hình Dạng Cơ Bản

**Thanh đồng nhất** chiều dài $L$, tỉ lệ dọc theo $x$ từ $0$ đến $L$:
$$X_{\text{CM}} = \frac{\int_0^L x \cdot (\rho A) dx}{\rho A L} = \frac{L/2 \cdot \rho A L}{\rho A L} = \frac{L}{2}$$

CM ở chính giữa — điều hiển nhiên theo đối xứng.

**Hình tam giác** đồng nhất chiều cao $h$:
$$X_{\text{CM}} = \frac{h}{3} \text{ từ đáy}$$

Chú ý: không phải $h/2$ vì phân phối khối lượng không đều theo chiều cao.

**Bán cầu đặc** bán kính $R$:
$$Z_{\text{CM}} = \frac{3R}{8} \text{ từ đáy phẳng}$$

### 4. Định Lý Cộng của CM

Nếu hệ gồm hai phần $A$ và $B$ với khối lượng $M_A$, $M_B$ và CM tại $\vec{R}_A$, $\vec{R}_B$:
$$M_{\text{total}} \vec{R}_{\text{CM}} = M_A \vec{R}_A + M_B \vec{R}_B$$

Hệ quả mạnh mẽ: **có thể "trừ" lỗ hổng (cavity)**. CM của hình tròn đặc có lỗ tròn:
$$X_{\text{CM}} = \frac{M_{\text{full}} X_{\text{full}} - M_{\text{hole}} X_{\text{hole}}}{M_{\text{full}} - M_{\text{hole}}}$$

Kỹ thuật này thường dùng trong tính toán CM của chi tiết cơ khí phức tạp có lỗ khoan, rãnh.

### 5. Ví Dụ Thực Tế: Centroid Detection trong Cảm Biến Quang Học Độ Chính Xác Cao

Trong hệ thống đo lường quang học (laser triangulation, structured light, interferometry), vị trí vật đo được xác định từ phân phối cường độ trên detector CCD/CMOS. Thuật toán **centroid detection** áp dụng trực tiếp công thức CM:

$$x_{\text{centroid}} = \frac{\sum_{j} I_j \cdot x_j}{\sum_{j} I_j}$$

trong đó $I_j$ là cường độ pixel $j$ và $x_j$ là vị trí pixel. Đây chính xác là công thức CM với $m_i \to I_j$.

**Ưu điểm:** Cho phép xác định vị trí với độ chính xác **sub-pixel** (dưới 1/10 pixel), tức là dưới micrometer với optical magnification phù hợp.

**Ví dụ tính toán:** Camera có pixel size $5.5$ µm/pixel, optical magnification $10\times$, mỗi pixel tương đương $0.55$ µm trên vật. Centroid detection đạt $\sigma = 0.02$ pixel $= 0.011$ µm độ lặp lại đo lường.

**Ảnh hưởng của nhiễu:** Nhiễu ngẫu nhiên (shot noise, read noise) làm $I_j$ dao động, gây sai số centroid:
$$\sigma_{\text{centroid}} = \frac{\sigma_{\text{noise}}}{\text{SNR}} \cdot \sigma_{\text{spot}}$$

Kỹ sư tối ưu hóa bằng cách: (1) tăng cường độ ánh sáng (tăng SNR), (2) lọc vùng quan tâm (ROI) để chỉ tính centroid trong vùng có tín hiệu, (3) áp dụng trọng số Gaussian thay vì tuyến tính.

### 6. Bài Tập Mẫu: Tính CM của Cụm Cảm Biến

**Bài toán:** Cụm cảm biến IMU gồm:
- Vỏ nhôm: hình hộp chữ nhật rỗng, xem như 4 tấm nhôm: 2 tấm đầu ($M = 0.05$ kg mỗi tấm, tâm ở $x = 0$ và $x = 10$ cm), 2 tấm bên (bỏ qua đối xứng).
- PCB (mạch in): $M_P = 0.08$ kg, tại $x_P = 5$ cm
- Battery: $M_B = 0.12$ kg, tại $x_B = 3$ cm
- Sensor module: $M_S = 0.04$ kg, tại $x_S = 7$ cm

Tính CM theo trục $x$.

**Bước 1:** Liệt kê các thành phần.

| Thành phần | Khối lượng (kg) | Vị trí $x$ (cm) | $m_i x_i$ (kg·cm) |
|-----------|----------------|-----------------|-------------------|
| Tấm đầu 1 | 0.05 | 0 | 0 |
| Tấm đầu 2 | 0.05 | 10 | 0.5 |
| PCB | 0.08 | 5 | 0.4 |
| Battery | 0.12 | 3 | 0.36 |
| Sensor | 0.04 | 7 | 0.28 |

*Ý nghĩa:* Bước này giống như lập bảng signal × weight trong xử lý tín hiệu.

**Bước 2:** Tổng khối lượng.
$$M = 0.05 + 0.05 + 0.08 + 0.12 + 0.04 = 0.34 \text{ kg}$$

**Bước 3:** Tổng moment khối lượng.
$$\sum m_i x_i = 0 + 0.5 + 0.4 + 0.36 + 0.28 = 1.54 \text{ kg·cm}$$

**Bước 4:** Vị trí CM.
$$X_{\text{CM}} = \frac{1.54}{0.34} = 4.53 \text{ cm}$$

*Ý nghĩa:* CM lệch về phía battery (3 cm) vì battery nặng nhất (0.12 kg). Để cân bằng CM tại $x = 5$ cm (tâm hình học), cần dịch battery ra $x_B = 5 + (5 - 4.53) \times 0.34/0.12 = 5 + 1.33 = 6.33$ cm.

**Bước 5:** Kiểm tra với CM mới.
$$\sum m_i x_i = 0 + 0.5 + 0.4 + 0.12 \times 6.33 + 0.28 = 1.54 - 0.36 + 0.76 = 1.94 - 0.24 = 1.70 \text{ kg·cm}$$
$$X_{\text{CM,new}} = 1.70/0.34 = 5.0 \text{ cm} \checkmark$$

### 7. Liên Hệ: Cân Bằng Động và Vibration Analysis

Khi rotor motor servo có CM lệch trục quay $e = 10$ µm ($= 10^{-5}$ m), ở $\omega = 3000$ RPM $= 314$ rad/s:
$$F_{\text{unbalance}} = M \omega^2 e = 0.5 \times 314^2 \times 10^{-5} = 0.49 \text{ N}$$

Lực không cân bằng 0.49 N tại tần số 50 Hz này truyền qua vòng bi đến khung máy, gây rung động và sai số vị trí. Trong hệ thống gia công micrometer, yêu cầu $F_{\text{unbalance}} < 0.01$ N, tức $e < 0.2$ µm — đây là lý do balancing machine cho spindle tốc độ cao phải đạt độ phân giải đo CM ở cấp sub-micrometer, áp dụng chính xác thuật toán centroid detection mà chúng ta vừa phân tích.

---
*Exported from Feynman Bot*
