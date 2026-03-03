---
lesson_id: 5543
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:07.551944+00:00"
content_hash: df414780b06a
chapter_number: 30
chapter_title: Chapter 30
section_number: 3
section_title: 30–2The diffraction grating
---
# ## Cách Tử Nhiễu Xạ và Tán Sắc Ánh Sáng — Phân tích Chuyên sâu

*Source: Chapter 30 - Chapter 30 (Section 3) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_30.html)*

## Cách Tử Nhiễu Xạ và Tán Sắc Ánh Sáng — Phân tích Chuyên sâu

### Nguyên lý vật lý của cách tử

Một cách tử nhiễu xạ gồm $N$ vạch song song cách đều nhau với khoảng cách $d$ (grating period). Khi sóng phẳng chiếu thẳng góc vào cách tử, mỗi vạch tán xạ lại như một nguồn điểm (Huygens). Bài toán trở thành: tính biên độ tổng hợp từ $N$ nguồn cách đều, đồng pha, quan sát ở góc $\theta$.

**Hiệu pha giữa hai vạch liên tiếp:**
$$\phi = \frac{2\pi d\sin\theta}{\lambda}$$

**Biên độ tổng hợp (từ công thức N nguồn):**
$$A_R(\theta) = A_0 \cdot \frac{\sin(N\phi/2)}{\sin(\phi/2)} = A_0 \cdot \frac{\sin(N\pi d\sin\theta/\lambda)}{\sin(\pi d\sin\theta/\lambda)}$$

**Cường độ:**
$$I(\theta) = I_0 \cdot \left[\frac{\sin(N\pi d\sin\theta/\lambda)}{\sin(\pi d\sin\theta/\lambda)}\right]^2$$

**Cực đại chính** (principal maxima) tại:
$$d\sin\theta_m = m\lambda \quad (m = 0, \pm 1, \pm 2, ...)$$

Tại các cực đại này, $I_{max} = N^2 I_0$ — cường độ tăng tỷ lệ $N^2$, không phải $N$!

### Góc tán sắc (Angular Dispersion)

Tán sắc là khả năng phân tách các bước sóng khác nhau về góc. Lấy đạo hàm điều kiện cực đại theo $\lambda$:
$$d\cos\theta \cdot d\theta = m \cdot d\lambda$$

**Góc tán sắc (Angular Dispersion):**
$$\frac{d\theta}{d\lambda} = \frac{m}{d\cos\theta_m}$$

Để tăng tán sắc: dùng bậc $m$ cao hơn, hoặc giảm $d$ (tăng mật độ vạch). Nhưng có giới hạn: nếu $d < \lambda$, bậc 1 không tồn tại ($\sin\theta_1 = \lambda/d > 1$).

**Tán sắc tuyến tính (Linear Dispersion)** trên mặt phẳng tiêu cự cách cách tử $f$:
$$\frac{dx}{d\lambda} = f\frac{d\theta}{d\lambda} = \frac{fm}{d\cos\theta_m}$$

Đây là thông số quan trọng để thiết kế spectrometer: với $f = 500$ mm, $m = 1$, $d = 833$ nm, $\theta \approx 40°$:
$$\frac{dx}{d\lambda} = \frac{500 \times 1}{0.833 \times 10^{-3} \times \cos(40°)} \approx 780 \text{ mm/nm}$$

Nghĩa là hai bước sóng cách nhau 1 nm sẽ tách nhau 780 μm trên cảm biến — dễ dàng phân biệt bằng CCD pixel 5 μm.

### Blazed Grating: Cách tử nghiêng để tăng hiệu suất

Một vấn đề với cách tử đơn giản: phần lớn năng lượng đi vào bậc 0 (phản xạ thẳng) — lãng phí. **Blazed grating** (cách tử nghiêng) giải quyết điều này.

Bằng cách mài nghiêng từng vạch với góc blaze $\theta_B$, hướng phản xạ specular (gương) của từng vạch được hướng vào đúng bậc nhiễu xạ cần thiết (thường bậc 1). Hiệu suất đạt $70$–$90\%$ tại bước sóng blaze $\lambda_B = 2d\sin\theta_B$ (trong configuration Littrow: $\theta_{in} = \theta_{out} = \theta_B$).

### Độ phân giải bước sóng (Spectral Resolution)

**Tiêu chuẩn Rayleigh:** Hai vạch phổ phân biệt được khi cực đại của vạch này rơi đúng vào cực tiểu đầu tiên của vạch kia.

Cực tiểu đầu tiên của vạch bậc $m$ xuất hiện khi tổng pha lệch $2\pi/N$ khỏi điều kiện cực đại:
$$N\Delta\phi = 2\pi \implies N \cdot \frac{2\pi d\cos\theta}{\lambda}\Delta\theta = 2\pi$$
$$\Delta\theta_{min} = \frac{\lambda}{Nd\cos\theta} = \frac{\lambda}{L\cos\theta}$$

Trong đó $L = Nd$ là tổng chiều dài cách tử chiếu sáng.

**Độ phân giải bước sóng $\delta\lambda$** tương ứng với $\Delta\theta_{min}$:
$$\delta\lambda = \frac{\Delta\theta_{min}}{d\theta/d\lambda} = \frac{\lambda/(L\cos\theta)}{m/(d\cos\theta)} = \frac{\lambda d}{mL} = \frac{\lambda}{mN}$$

**Resolving power (khả năng phân giải):**
$$R = \frac{\lambda}{\delta\lambda} = mN$$

Kết quả đẹp: **Khả năng phân giải bằng bậc nhiễu xạ nhân với tổng số vạch.**

### Ví dụ thực tế: Spectrometer cho kiểm tra laser diode

Trong hệ thống cảm biến laser của bạn (LiDAR, interferometer), chất lượng laser diode là tối quan trọng. Spectrometer dùng để kiểm tra:
- Bước sóng trung tâm (center wavelength): cần chính xác ±0.1 nm
- Linewidth (độ rộng vạch): ảnh hưởng coherence length của laser
- Mode structure: single-mode hay multi-mode

**Thiết kế spectrometer:**

Yêu cầu: phân giải $\delta\lambda = 0.05$ nm tại $\lambda = 780$ nm (laser diode phổ biến)

Required resolving power: $R = 780/0.05 = 15600$

Chọn bậc $m = 1$: cần $N = R/m = 15600$ vạch. Với $d = 1200$ vạch/mm, cần:
$$L = N/1200 = 15600/1200 = 13 \text{ mm}$$

Một cách tử rộng 13 mm, mật độ 1200 vạch/mm là hoàn toàn thực tế (Thorlabs, Newport, Edmund Optics đều cung cấp). Tiêu cự $f = 150$ mm cho tán sắc tuyến tính:
$$\frac{dx}{d\lambda} = \frac{150 \times 1}{(1/1200) \times 10^{-3} \times \cos(\theta_1)}$$

Với $\sin\theta_1 = 0.780 \times 1200 \times 10^{-6} / 10^{-3} = 0.936 \implies \theta_1 = 69.4°$, $\cos\theta_1 = 0.351$:
$$\frac{dx}{d\lambda} = \frac{150}{8.33 \times 10^{-4} \times 0.351} \approx 513 \text{ mm/nm}$$

Hai bước sóng cách 0.05 nm tách nhau 25.6 μm — vừa đủ để CCD pixel 5–10 μm phân biệt.

### Bài tập mẫu: Phân giải hai laser

**Đề bài:** Cần phân biệt hai laser diode có bước sóng $\lambda_1 = 852.1$ nm và $\lambda_2 = 852.3$ nm (ứng dụng: spectroscopy rubidium trong atomic clock). Dùng cách tử $N = 1800$ vạch/mm, bậc $m = 1$. Hỏi:

(a) Chiều rộng cách tử tối thiểu cần chiếu sáng?
(b) Góc tách giữa hai vạch?

**Giải:**

(a) $\delta\lambda = 0.2$ nm, $R_{min} = 852.2/0.2 = 4261$. $N_{min} = 4261/1 = 4261$ vạch. $L_{min} = 4261/1800 = 2.37$ mm. Chỉ cần chiếu sáng hơn 2.4 mm của cách tử là đủ!

(b) $d = 1/1800$ mm = 556 nm. $\sin\theta = \lambda/d$. Tại $\lambda = 852$ nm: $\sin\theta = 852/556 = 1.53 > 1$ — **bậc 1 không tồn tại!** Cần dùng cách tử thưa hơn hoặc bậc khác.

Kiểm tra: với $d = 1200$ vạch/mm: $\sin\theta_1 = 852/833 = 1.023 > 1$ — vẫn không tồn tại! Thực ra, với $\lambda = 852$ nm, cần $d > \lambda = 852$ nm, tức mật độ vạch $< 1175$ vạch/mm. Dùng $d = 1200$ nm (833 vạch/mm): $\sin\theta_1 = 852/1200 = 0.71 \implies \theta_1 = 45.2°$. $R = mN = 1 \times (W \times 833)$ — với $W = 10$ mm: $R = 8330 > 4261$. Góc tách: $\Delta\theta = (d\theta/d\lambda) \times \Delta\lambda = \frac{m}{d\cos\theta} \times 0.2 = \frac{1}{1200 \times 10^{-9} \times 0.704} \times 0.2 \times 10^{-9} = 2.37 \times 10^{-4}$ rad $= 0.0136°$.

### Tổng kết

Cách tử nhiễu xạ kết hợp ba nguyên lý: (1) tán xạ Huygens từ mỗi vạch, (2) giao thoa tăng cường tại các cực đại chính, (3) độ phân giải tăng theo $N$. Trong kỹ thuật đo lường chính xác, cách tử là trái tim của spectrometer và encoder quang học — hai thiết bị không thể thiếu trong mọi hệ thống kiểm tra và điều khiển chính xác cấp micrometer-nanometer.

---
*Exported from Feynman Bot*
