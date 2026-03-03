---
lesson_id: 5522
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:07.102307+00:00"
content_hash: fda86ce4c9a9
chapter_number: 27
chapter_title: Chapter 27
section_number: 7
section_title: 27–6Aberrations
---
# ## Aberration Trong Quang Học: Phân Tích Chuyên Sâu

*Source: Chapter 27 - Chapter 27 (Section 7) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_27.html)*

## Aberration Trong Quang Học: Phân Tích Chuyên Sâu

### 1. Phân loại aberration theo lý thuyết Seidel

Trong quang học hình học, aberration được phân loại hệ thống theo lý thuyết Seidel (Seidel aberrations). Khi tính toán chính xác hơn bằng cách giữ số hạng bậc ba trong khai triển $\sin\theta = \theta - \theta^3/6 + \ldots$, ta thu được năm loại aberration cơ bản:

1. **Spherical aberration** (quang sai cầu)
2. **Coma** (quang sai coma — ảnh của điểm ngoài trục có dạng hình sao chổi)
3. **Astigmatism** (loạn thị — hai mặt phẳng vuông góc có tiêu điểm khác nhau)
4. **Field curvature** (độ cong trường ảnh — mặt phẳng ảnh thực ra là mặt cong)
5. **Distortion** (méo hình — độ phóng đại thay đổi theo khoảng cách từ trục)

Ngoài ra còn có **Chromatic aberration** — không phải Seidel aberration vì nó phụ thuộc bước sóng, không phải góc.

### 2. Phân tích định lượng spherical aberration

Với thấu kính cầu mỏng chiết suất $n$, tiêu cự cho tia paraxial là $f_0$. Đối với tia đi qua thấu kính ở khoảng cách $h$ từ trục, tiêu cự hiệu dụng là:

$$f(h) = f_0\left(1 - \alpha \frac{h^2}{f_0^2} + \ldots\right)$$

Trong đó $\alpha$ là hệ số spherical aberration phụ thuộc vào hình dạng thấu kính (shape factor) $q = (R_2 + R_1)/(R_2 - R_1)$ và vị trí vật (position factor) $p = (s' - s)/(s' + s)$.

**Độ lệch dọc trục** (*longitudinal spherical aberration*): $\delta f = f(h) - f_0 \propto h^2$

**Độ lệch ngang** (*transverse spherical aberration*): $\delta y = h \cdot \delta f / f_0 \propto h^3$

Đây là lý do gọi là "bậc ba" — aberration bậc ba trong khai triển của $\sin\theta$.

### 3. Chromatic aberration và hệ số Abbe

Chiết suất thuỷ tinh phụ thuộc bước sóng theo công thức Sellmeier:

$$n^2(\lambda) = 1 + \sum_i \frac{B_i \lambda^2}{\lambda^2 - C_i}$$

Trong thực tế, ta đặc trưng dispersion của thuỷ tinh bằng **Abbe number** (số Abbe):

$$V_d = \frac{n_d - 1}{n_F - n_C}$$

Trong đó $n_d$, $n_F$, $n_C$ là chiết suất tại bước sóng vàng (589.3 nm), xanh lam (486.1 nm), và đỏ (656.3 nm) tương ứng.

Sự thay đổi tiêu cự do chromatic aberration:

$$\delta f = -\frac{f}{V_d}$$

Số Abbe $V_d$ lớn → dispersion nhỏ → chromatic aberration nhỏ. Thuỷ tinh crown (như BK7) có $V_d \approx 64$; thuỷ tinh flint có $V_d \approx 36$.

### 4. Thiết kế achromatic doublet

Để khử chromatic aberration cho hai bước sóng (achromat), ta ghép hai thấu kính vật liệu khác nhau:

Điều kiện achromat:
$$\frac{P_1}{V_1} + \frac{P_2}{V_2} = 0$$

Trong đó $P_i = 1/f_i$ là optical power, $V_i$ là số Abbe của từng thấu kính. Kết hợp với yêu cầu tiêu cự tổng $f$:
$$P_1 + P_2 = \frac{1}{f}$$

Giải hệ:
$$P_1 = \frac{V_1}{(V_1 - V_2) f}, \quad P_2 = \frac{-V_2}{(V_1 - V_2) f}$$

Ví dụ: thiết kế achromat $f = 100$ mm dùng BK7 ($V_1 = 64$) và F2 flint ($V_2 = 36$):
$$P_1 = \frac{64}{(64-36) \times 100} = \frac{64}{2800} = 0.02286 \text{ mm}^{-1} \Rightarrow f_1 = 43.75 \text{ mm}$$
$$P_2 = \frac{-36}{2800} = -0.01286 \text{ mm}^{-1} \Rightarrow f_2 = -77.78 \text{ mm}$$

### 5. Giới hạn nhiễu xạ: kết nối với vật lý sóng

Feynman chỉ ra rằng nguyên lý thời gian cực tiểu chỉ là xấp xỉ. Ánh sáng là sóng điện từ với tần số $\nu$ và chu kỳ $T = 1/\nu = \lambda/c$.

**Tiêu chí Rayleigh cho hệ quang học hoàn hảo:** Nếu sai lệch thời gian $\delta t$ giữa tia biên và tia trục thoả mãn:
$$\delta t < T = \frac{1}{\nu} = \frac{\lambda}{c}$$

Thì hệ quang học đã đạt chất lượng nhiễu xạ giới hạn (*diffraction-limited*). Không cần cải thiện thêm.

Đây tương đương với **tiêu chí Rayleigh**: OPD (optical path difference) $< \lambda/4$.

Kích thước điểm hội tụ nhỏ nhất (Airy disk radius):
$$r_{Airy} = 1.22 \frac{\lambda}{D/f} = 1.22 \frac{\lambda f}{D} = 1.22 \frac{\lambda}{2 NA}$$

Trong đó $NA = n \sin\theta_{max}$ là numerical aperture.

### 6. Ứng dụng thực tế: Thiết kế optical probe cho CMM (Coordinate Measuring Machine)

Trong thiết kế đầu đo quang học cho máy đo toạ độ (CMM) chính xác micromet, kỹ sư cơ điện tử phải cân bằng nhiều yếu tố:

**Yêu cầu:** Working distance 10 mm, spot size $\leq 2$ μm, ánh sáng LED 530 nm

**Bước 1 — Tính NA cần thiết:**
$$NA \geq 1.22 \times \frac{530 \times 10^{-9}}{2 \times 10^{-6}} = 0.323$$

**Bước 2 — Xét spherical aberration:** Với $NA = 0.323$ ($\sin\theta \approx 0.33$, $\theta \approx 19°$), xấp xỉ paraxial không đủ chính xác. Cần dùng thấu kính aspheric hoặc thiết kế multi-element objective.

**Bước 3 — Xét chromatic aberration:** LED 530 nm có bandwidth $\Delta\lambda \approx 30$ nm. Với BK7, $\delta n/\delta\lambda \approx -0.0001$ nm$^{-1}$, dẫn đến $\delta f/f \approx 0.3\%$, tức $\delta f \approx 30$ μm tại $f = 10$ mm — vượt quá yêu cầu. Cần dùng achromatic doublet.

**Bước 4 — Thiết kế doublet:** Dùng công thức achromat với BK7 và SF11 flint ($V_2 = 25$), tính $f_1$, $f_2$, sau đó dùng ray-tracing software để tối ưu $R_1$, $R_2$, $R_3$, $R_4$ của cặp thấu kính.

**Kết quả:** Hệ 4 bề mặt (doublet) đạt chromatic aberration $< 0.1$ μm, spherical aberration $< 0.05$ μm — đủ cho đo lường micromet.

### 7. Phương pháp ray tracing hiện đại

Với hệ nhiều bề mặt phức tạp, kỹ sư dùng phần mềm ray-tracing (Zemax, CODE V, OpticStudio) để:

1. Nhập thông số hình học và vật liệu mỗi bề mặt
2. Máy tính trace hàng nghìn tia, áp dụng Snell's law chính xác (không xấp xỉ)
3. Phân tích wavefront error, spot diagram, MTF (Modulation Transfer Function)
4. Tối ưu hoá tự động (optimization) các tham số thiết kế

Đây chính xác là điều Feynman đề cập: "today, with computing machines, it is the right way to do it."

### Tóm tắt

- Năm Seidel aberration xuất hiện từ số hạng bậc ba trong khai triển $\sin\theta$
- Spherical aberration tỉ lệ với $h^3$ (transverse) hoặc $h^2$ (longitudinal)
- Chromatic aberration đặc trưng bởi Abbe number $V_d = (n_d-1)/(n_F-n_C)$
- Achromatic doublet khử chromatic aberration cho 2 bước sóng
- Giới hạn nhiễu xạ: $r_{Airy} = 1.22\lambda/(2NA)$ — không thể vượt qua bằng quang học thông thường
- Thiết kế thực tế cần ray-tracing software với Snell's law chính xác

---
*Exported from Feynman Bot*
