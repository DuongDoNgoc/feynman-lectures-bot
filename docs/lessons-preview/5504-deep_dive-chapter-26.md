---
lesson_id: 5504
lesson_type: deep_dive
approval_status: pending
exported_at: "2026-03-02T15:10:31.258391+00:00"
content_hash: d55e5c1ecf23
chapter_number: 26
chapter_title: Chapter 26
section_number: 2
section_title: 26–1Light
---
# ## Phân Tích Sâu: Phổ Điện Từ và Các Chế Độ Xấp Xỉ Trong Quang Học

*Source: Chapter 26 - Chapter 26 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_26.html)*

## Phân Tích Sâu: Phổ Điện Từ và Các Chế Độ Xấp Xỉ Trong Quang Học

### 1. Bức xạ điện từ: Bản chất thống nhất

Ánh sáng nhìn thấy, sóng radio, tia X và tia gamma đều là biểu hiện của cùng một hiện tượng: **bức xạ điện từ** (electromagnetic radiation). Về mặt cơ bản, tất cả đều là sóng của trường điện và từ dao động vuông góc nhau và vuông góc với hướng truyền sóng.

Quan hệ cơ bản:
$$c = \lambda \nu$$

trong đó $c = 3 \times 10^8$ m/s là tốc độ ánh sáng trong chân không, $\lambda$ là bước sóng, $\nu$ là tần số.

Về lượng tử, mỗi photon mang năng lượng:
$$E = h\nu = \frac{hc}{\lambda}$$

trong đó $h = 6.626 \times 10^{-34}$ J·s là hằng số Planck.

### 2. Phổ điện từ đầy đủ - Phân tích định lượng

| Vùng phổ | Bước sóng tiêu biểu | Tần số | Năng lượng photon | Ứng dụng kỹ thuật |
|---|---|---|---|---|
| Sóng radio (AM) | 300 m | 1 MHz | $4 \times 10^{-9}$ eV | Truyền thông |
| Sóng radio (FM) | 3 m | 100 MHz | $4 \times 10^{-7}$ eV | Truyền thông |
| Radar (X-band) | 3 cm | 10 GHz | $4 \times 10^{-5}$ eV | Radar, thiết bị quân sự |
| Radar (Ka-band) | 8 mm | 35 GHz | $1.4 \times 10^{-4}$ eV | Radar mm-wave, cảm biến xe hơi |
| Hồng ngoại xa | 10 μm | 30 THz | 0.12 eV | Camera nhiệt quân sự |
| Hồng ngoại gần | 1 μm | 300 THz | 1.2 eV | Laser Nd:YAG, LIDAR |
| Ánh sáng đỏ | 700 nm | 430 THz | 1.8 eV | Laser He-Ne |
| Ánh sáng xanh | 400 nm | 750 THz | 3.1 eV | Laser diode GaN |
| UV-C | 200 nm | 1.5 PHz | 6.2 eV | Khử trùng |
| Tia X mềm | 10 nm | 30 PHz | 124 eV | X-quang chẩn đoán |
| Tia X cứng | 0.1 nm | 3 EHz | 12.4 keV | NDT công nghiệp |
| Tia gamma | 0.001 nm | 300 EHz | 1.24 MeV | Kiểm tra hạt nhân |

### 3. Ba chế độ xấp xỉ - Phân tích điều kiện áp dụng

**Chế độ 1: Quang học hình học (Geometrical Optics)**

Điều kiện: $\lambda \ll d$ và $E_{photon} \ll$ độ nhạy thiết bị

Trong giới hạn này, ta bỏ qua:
- Tính chất sóng (không có nhiễu xạ, giao thoa)
- Tính chất lượng tử (không cần đếm photon)

Ánh sáng được mô tả bằng **tia sáng** (light ray) - đường thẳng vuông góc với mặt sóng.

Công cụ toán học: Định luật Snell-Descartes $n_1 \sin\theta_1 = n_2 \sin\theta_2$, ma trận truyền tia (ray transfer matrix), nguyên lý Fermat.

**Chế độ 2: Quang học sóng (Wave Optics / Physical Optics)**

Điều kiện: $\lambda \sim d$

Phải dùng phương trình sóng đầy đủ. Các hiện tượng quan trọng:
- **Nhiễu xạ** (diffraction): sóng uốn quanh vật cản, giới hạn độ phân giải không gian $\Delta x \geq \lambda/(2 N.A.)$
- **Giao thoa** (interference): hai nguồn kết hợp tạo vân sáng tối
- **Phân cực** (polarization): hướng dao động của vector $\vec{E}$

Đây là cơ sở của **interferometer** dùng trong đo lường nano/micrometer của bạn.

**Chế độ 3: Quang học lượng tử (Quantum Optics)**

Điều kiện: $\lambda \ll d$ nhưng $E_{photon}$ lớn

Mỗi photon là một hạt. Quan trọng khi:
- Tia X và gamma: photon có đủ năng lượng để ion hóa nguyên tử
- Phát hiện photon đơn (SPAD, SNSPD)
- Hiệu ứng quang điện, laser

### 4. Ứng dụng thực tế trong thiết bị đo lường độ chính xác

**Interferometer laser (Laser Interferometry):**

Trong đo lường vị trí micrometer, bạn có thể dùng interferometer He-Ne ($\lambda = 632.8$ nm). Độ phân giải lý thuyết:
$$\Delta x = \frac{\lambda}{2} = 316 \text{ nm}$$

Với kỹ thuật nội suy tín hiệu, có thể đạt độ phân giải $\lambda/1024 \approx 0.6$ nm - đây là quang học sóng hoàn toàn, không phải hình học.

**Camera nhiệt (Thermal Imaging - FLIR):**

Bước sóng hồng ngoại $\lambda \approx 3-12$ μm. Với ống kính đường kính $d = 50$ mm:
- $\lambda/d \approx 120 \times 10^{-6}$ - quang học hình học khá hợp lệ
- Nhưng nhiễu xạ giới hạn độ phân giải góc: $\theta_{min} = 1.22\lambda/d \approx 0.15$ mrad
- Điều này ảnh hưởng đến NETD (Noise Equivalent Temperature Difference) của camera

**Radar mảng pha (Phased Array Radar):**

Với radar X-band ($\lambda = 3$ cm), mảng anten kích thước $D = 1$ m:
- Độ phân giải góc chùm tia: $\Delta\theta \approx \lambda/D = 30$ mrad ≈ 1.7°
- Đây là quang học sóng: kích thước anten tương đương nhiều bước sóng, nhưng hiệu ứng nhiễu xạ vẫn chi phối độ phân giải

### 5. Tại sao quang học hình học là xấp xỉ phải "học lại"?

Feynman cảnh báo đây là chương phải "unlearn" sau này vì:

1. **Nhiễu xạ luôn tồn tại:** Dù $\lambda \ll d$, nhiễu xạ vẫn giới hạn độ phân giải. Giới hạn Abbe trong kính hiển vi: $\delta = \lambda/(2 n\sin\theta)$.

2. **Tia sáng chỉ là xấp xỉ:** Thực chất ánh sáng truyền theo tất cả các đường - nguyên lý Feynman về tích phân đường (path integral) mới là mô tả đầy đủ.

3. **Chiết suất phụ thuộc bước sóng (dispersion):** Thấu kính thực gây sắc sai (chromatic aberration) vì $n(\lambda)$ khác nhau cho các màu khác nhau.

4. **Tán sắc trong sợi quang:** Ảnh hưởng đến băng thông hệ thống thông tin quang.

**Kết luận:** Quang học hình học là công cụ thiết kế nhanh hiệu quả cho hệ thống có kích thước lớn hơn nhiều bước sóng. Nhưng kỹ sư quang học chính xác luôn phải kiểm tra xem hiệu ứng sóng (nhiễu xạ, giao thoa) có đáng kể không. Ranh giới thực tế: khi $d/\lambda > 100$, quang học hình học đủ tốt cho hầu hết mục đích thiết kế.

---
*Exported from Feynman Bot*
