---
lesson_id: 5546
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:07.626976+00:00"
content_hash: 657f6dc850eb
chapter_number: 30
chapter_title: Chapter 30
section_number: 4
section_title: 30–3Resolving power of a grating
---
# ## Độ Phân Giải Cách Tử và Nguyên Lý Bất Định Thời Gian-Tần Số — Phân tích Chuyê

*Source: Chapter 30 - Chapter 30 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_30.html)*

## Độ Phân Giải Cách Tử và Nguyên Lý Bất Định Thời Gian-Tần Số — Phân tích Chuyên sâu

### Bài toán phân giải bước sóng

Xét cách tử nhiễu xạ $N$ vạch, khoảng cách $d$, chiếu sáng bởi ánh sáng đơn sắc bậc $m$. Ta muốn biết: **hai bước sóng $\lambda$ và $\lambda' = \lambda + \Delta\lambda$ tối thiểu cách nhau bao nhiêu để cách tử phân biệt được?**

### Dẫn xuất chi tiết theo tiêu chuẩn Rayleigh

**Bước 1 — Điều kiện cực đại bậc $m$ của $\lambda'$:**

Tổng hiệu đường đi của $N$ vạch phải bằng $mN\lambda'$. Tại góc $\theta$:
$$Nd\sin\theta = mN\lambda'$$

**Bước 2 — Điều kiện cực tiểu đầu tiên của $\lambda$:**

Cực tiểu đầu tiên xảy ra khi tổng phasor khép vòng, tức $N$ phasor tạo đa giác đều, tổng pha $= 2\pi$. Điều này tương đương: tổng hiệu đường đi lệch $\lambda$ khỏi cực đại:
$$Nd\sin\theta = mN\lambda + \lambda = (mN+1)\lambda$$

**Bước 3 — Áp dụng tiêu chuẩn Rayleigh:**

Đặt hai điều kiện trên bằng nhau:
$$mN\lambda' = (mN+1)\lambda$$
$$mN(\lambda'-\lambda) = \lambda$$
$$mN\cdot\Delta\lambda = \lambda$$

$$\boxed{R = \frac{\lambda}{\Delta\lambda} = mN}$$

**Ý nghĩa vật lý:** $mN$ là tổng số bước sóng trong hiệu đường đi cực đại giữa tia đi qua vạch đầu tiên và vạch cuối cùng, ở bậc $m$. Phân giải tốt nghĩa là phải sử dụng tất cả $N$ vạch hiệu quả — ánh sáng phải chiếu đủ rộng.

### Nguyên lý phổ quát: $\Delta\nu = 1/T$

Đây là phần sâu sắc nhất của bài học. Feynman chỉ ra rằng công thức $R = mN$ chỉ là trường hợp đặc biệt của nguyên lý tổng quát:

$$\Delta\nu_{min} = \frac{1}{T_{max}}$$

Trong đó $T_{max}$ là **hiệu thời gian truyền** giữa tia cực trị đầu và tia cực trị cuối được phép giao thoa.

**Áp dụng cho cách tử:**

Hiệu đường đi tối đa (giữa vạch 1 và vạch $N$) theo phương nhiễu xạ bậc $m$:
$$\delta L = (N-1)d\sin\theta_m \approx Nd\sin\theta_m = Nd \cdot m\lambda/d = mN\lambda$$

Hiệu thời gian:
$$T = \delta L / c = mN\lambda/c$$

Hiệu tần số tối thiểu phân giải:
$$\Delta\nu = 1/T = c/(mN\lambda)$$

Chuyển sang $\Delta\lambda$:
$$\Delta\lambda = \frac{\lambda^2}{c}\Delta\nu = \frac{\lambda^2 c}{c \cdot mN\lambda} = \frac{\lambda}{mN}$$

Khớp hoàn toàn! Nhưng quan trọng hơn: **nguyên lý $\Delta\nu = 1/T$ áp dụng cho mọi hệ thống quang học, không chỉ cách tử.**

### Áp dụng cho các hệ thống khác

**Fabry-Perot Etalon:**

Gương phẳng song song cách nhau $l$, hệ số phản xạ $R$. Ánh sáng bounces $\bar{n} = 1/(1-R)$ lần trung bình. Hiệu thời gian hiệu quả:
$$T_{eff} = \bar{n} \cdot 2l/c = \frac{2l}{c(1-R)}$$

Độ phân giải tần số:
$$\Delta\nu_{FP} = \frac{c(1-R)}{2l} = \frac{FSR}{\mathcal{F}}$$

Trong đó $FSR = c/(2l)$ là Free Spectral Range và $\mathcal{F} = \pi\sqrt{R}/(1-R)$ là Finesse. Với $R = 99.5\%$ và $l = 10$ cm:
$$\Delta\nu_{FP} = \frac{3\times10^8 \times 0.005}{2 \times 0.1} = 7.5 \text{ MHz}$$

So sánh: cách tử $mN = 30000$ tại $\lambda = 780$ nm cho:
$$\Delta\nu_{grating} = c\Delta\lambda/\lambda^2 = 3\times10^8 \times (780/30000 \times 10^{-9})/(780 \times 10^{-9})^2 = 3.9 \text{ GHz}$$

Fabry-Perot tốt hơn cách tử hàng trăm lần về phân giải tần số — đây là lý do dùng etalon cho spectroscopy laser độ phân giải cao.

**Michelson Interferometer:**

Arm length $L_{arm}$. Hiệu đường đi tối đa khi quét gương: $\delta L_{max} = 2L_{arm}$. $T = 2L_{arm}/c$.
$$\Delta\nu_{Michelson} = c/(2L_{arm})$$

Đây là nguyên lý của **Fourier Transform Spectrometer (FTS):** quét gương một đoạn $L_{arm}$ lớn để đạt phân giải cao. Với $L_{arm} = 1$ m:
$$\Delta\nu_{FTS} = 3\times10^8/(2\times1) = 150 \text{ MHz}$$

Tốt hơn cách tử 26 lần, nhưng chậm hơn (cần quét cơ học). Đây chính là trade-off mà kỹ sư phải chọn tùy ứng dụng.

### Phân giải góc của kính thiên văn mảng

Nguyên lý tương tự áp dụng cho **radio telescope array** (mảng kính thiên văn radio). Nhiều anten đặt cách nhau baseline $B$, tín hiệu tổng hợp qua correlator (bộ tương quan).

Hiệu thời gian đến giữa hai anten xa nhất đối với nguồn nghiêng góc $\theta$ khỏi trục:
$$T = B\sin\theta/c \approx B\theta/c \quad (\theta \text{ nhỏ})$$

Độ phân giải góc (tiêu chuẩn Rayleigh):
$$\Delta\theta_{min} = \frac{\lambda}{B}$$

Trong đó $\lambda$ là bước sóng radio và $B$ là baseline (khoảng cách tối đa giữa các anten). Với Very Long Baseline Interferometry (VLBI), $B$ có thể bằng đường kính Trái Đất ($B \approx 10^7$ m). Ở $\lambda = 1$ mm:
$$\Delta\theta_{VLBI} = 10^{-3}/10^7 = 10^{-10} \text{ rad} = 20 \mu\text{arcsec}$$

Sắc nét hơn kính thiên văn quang học (Hubble) gần 1000 lần!

### Ứng dụng kỹ thuật: Phân tích tần số trong điều khiển chính xác

Nguyên lý $\Delta\nu = 1/T$ xuất hiện trực tiếp trong kỹ thuật đo lường và điều khiển:

**FFT Spectrum Analyzer cho servo motor:**

Khi phân tích rung động (vibration) của bàn trượt chính xác, dùng FFT với cửa sổ $T$ giây:
$$\Delta f_{FFT} = 1/T$$

Để phân biệt hai mode rung động cách nhau $\Delta f = 5$ Hz, cần $T \geq 1/5 = 200$ ms. Đây là ràng buộc thiết kế: sampling window phải đủ dài!

**Phase-locked loop (PLL) trong encoder:**

PLL dùng để theo dõi pha tín hiệu encoder. Bandwidth của PLL ($f_{BW}$) xác định tốc độ phản ứng. Nhưng $f_{BW}$ cũng giới hạn phân giải tần số: $\Delta f_{PLL} \geq f_{BW}$. Giảm bandwidth để tăng phân giải pha, nhưng phản ứng chậm hơn — trade-off cổ điển.

### Bài tập mẫu: Thiết kế spectrometer cho kiểm tra laser

**Đề bài:** Kiểm tra linewidth của laser diode dùng trong LiDAR. Laser có linewidth (FWHM) $\Delta\nu = 50$ MHz tại $\lambda = 1064$ nm. Thiết kế spectrometer cách tử để đo linewidth này.

**Yêu cầu:** Resolving power $R \geq \nu/\Delta\nu = c/(\lambda \Delta\nu)$

**Giải:**

Bước 1 — Tính $R$ cần thiết:
$$R = \frac{\nu}{\Delta\nu} = \frac{c/\lambda}{\Delta\nu} = \frac{3\times10^8/1064\times10^{-9}}{50\times10^6} = \frac{2.82\times10^{14}}{5\times10^7} = 5.6\times10^6$$

Bước 2 — Chọn bậc và số vạch:
Với bậc $m=1$: $N = R/m = 5.6\times10^6$ vạch — **không khả thi!** (cần cách tử dài hàng km)

Bước 3 — Thực tế: Cách tử KHÔNG phù hợp cho linewidth 50 MHz. Cần dùng Fabry-Perot etalon:
$$l_{min} = c/(2\Delta\nu) = 3\times10^8/(2\times5\times10^7) = 3 \text{ m}$$

Hoặc dùng scanning Fabry-Perot với finesse $\mathcal{F} = 100$ và $l = 3$ cm: $\Delta\nu = c(1-R)/(2l\pi\sqrt{R})$. Giải ra $R_{mirror} = 99\%$, $l = 3$ m/100 = 3 cm — khả thi!

**Kết luận thiết kế:** Cách tử chỉ dùng được cho linewidth $> $ vài GHz (phổ rộng). Laser linewidth MHz cần Fabry-Perot. Nguyên lý $\Delta\nu = 1/T$ giúp ta chọn đúng công cụ ngay từ đầu mà không cần thử-sai.

### Tổng kết

Nguyên lý $\Delta\nu = 1/T$ là **định luật vàng của quang học phân giải**:
- Áp dụng thống nhất cho cách tử ($T = mNd/c$), Fabry-Perot ($T = 2l\mathcal{F}/c$), Michelson ($T = 2L/c$), và antenna array ($T = B\sin\theta/c$)
- Kỹ sư cơ điện tử nhận ra ngay: đây chính là nguyên lý bất định thời gian-tần số của xử lý tín hiệu số
- Chọn đúng công cụ phân tích phổ dựa trên $T$ cần thiết là bước thiết kế đầu tiên và quan trọng nhất
- Trong đo lường chính xác, từ encoder quang đến LiDAR đến spectrometer — tất cả đều bị giới hạn bởi nguyên lý này, không có ngoại lệ

---
*Exported from Feynman Bot*
