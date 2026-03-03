---
lesson_id: 5582
lesson_type: deep_dive
approval_status: pending
exported_at: "2026-03-03T15:33:08.511261+00:00"
content_hash: 31c8deaa88d9
chapter_number: 34
chapter_title: Chapter 34
section_number: 4
section_title: 34–3Synchrotron radiation
---
# ## Bức Xạ Synchrotron: Phân Tích Toán Học Đầy Đủ

*Source: Chapter 34 - Chapter 34 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_34.html)*

## Bức Xạ Synchrotron: Phân Tích Toán Học Đầy Đủ

### 1. Động Học Của Electron Trong Từ Trường Đều

**Phương trình lực:**
$$\mathbf{F} = q\mathbf{v} 	imes \mathbf{B}$$

Lực Lorentz luôn vuông góc với $\mathbf{v}$, không thực hiện công. Do đó $|\mathbf{v}| = 	ext{const}$ và năng lượng động năng không đổi (chỉ nhờ từ trường).

**Suy ra bán kính quỹ đạo:**

Trong khoảng thời gian ngắn $\Delta t$, vector động lượng $\mathbf{p}$ quay một góc $\Delta\phi$:
$$|\Delta\mathbf{p}| = F\Delta t = qvB\Delta t$$

Quãng đường đi: $\Delta s = v\Delta t$

Góc quay: $\Delta\phi = |\Delta\mathbf{p}|/p = qvB\Delta t/p$

Cũng có: $\Delta\phi = \Delta s/R = v\Delta t/R$

So sánh: $qvB/p = v/R$, suy ra:
$$oxed{p = qBR}$$

**Góc cyclotron (angular frequency):**
$$\omega_c = v/R = qvB/p = qB/(\gamma m_e)$$

Đây là tần số cyclotron relativistic. Với electron năng lượng $E$:
$$\gamma = E/(m_e c^2), \quad T_{orbit} = 2\pi R/v pprox 2\pi R/c$$

### 2. Công Suất Bức Xạ: Công Thức Larmor Relativistic

Với electron chuyển động tương đối tính, công thức Larmor tổng quát:

$$P = rac{q^2 c}{6\piarepsilon_0} rac{\gamma^4}{R^2} \cdot rac{v^2}{c^2} pprox rac{q^2 c \gamma^4}{6\piarepsilon_0 R^2}$$

(với $v pprox c$)

Thay $R = p/(qB) = \gamma m_e v/(qB) pprox \gamma m_e c/(qB)$:

$$P = rac{q^4 B^2 c}{6\piarepsilon_0 m_e^2 c^2} \gamma^2 = rac{C_\gamma c}{2\pi} rac{E^4}{(m_e c^2)^4 R^2}$$

Nhận xét quan trọng: **$P \propto \gamma^4$ (hoặc $E^4$)** — công suất tăng rất nhanh theo năng lượng. Đây là lý do các synchrotron electron năng lượng cao mất năng lượng rất nhanh và cần RF cavity bổ sung liên tục.

### 3. Phổ Bức Xạ Synchrotron

Bức xạ synchrotron không phải đơn sắc — nó trải rộng từ sóng vô tuyến đến tia X cứng. Phổ có dạng đặc trưng với tần số tới hạn:

$$\omega_c = rac{3}{2}\gamma^3 rac{c}{R}$$

Phổ tăng tuyến tính với $\omega$ ở vùng $\omega \ll \omega_c$, đạt cực đại gần $\omega_c$, và giảm theo hàm mũ ở $\omega \gg \omega_c$.

**Ví dụ tính toán — Synchrotron ESRF (Grenoble, Pháp):**
- Năng lượng electron: $E = 6$ GeV → $\gamma = 6000/0.511 pprox 11740$
- Bán kính quỹ đạo: $R pprox 57$ m (chu vi 844 m)
- Từ trường bending: $B pprox 0.86$ T

Tần số tới hạn:
$$\omega_c = rac{3}{2} 	imes (11740)^3 	imes rac{3	imes10^8}{57} pprox 4.0 	imes 10^{18} 	ext{ rad/s}$$
$$E_{photon,c} = \hbar\omega_c pprox 19 	ext{ keV} \quad 	ext{(tia X năng lượng cao)}$$

### 4. Collimation Relativistic: Tại Sao Chùm Tia Rất Hẹp?

Trong hệ quy chiếu của electron (rest frame), bức xạ phát theo mọi hướng (như anten dipole). Nhưng trong hệ lab (electron đang chạy nhanh), do **aberration relativistic**, mọi photon phát ra trong một góc $	heta' < \pi/2$ quanh hướng chuyển động trong rest frame sẽ bị nén vào góc nhỏ:

$$\sin	heta_{lab} = rac{\sin	heta'}{\gamma(1 + eta\cos	heta')}$$

Với $\gamma \gg 1$, phần lớn photon tập trung vào góc:
$$	heta_{lab} \lesssim rac{1}{\gamma}$$

**Tính toán thực tế:** Với ESRF, $\gamma pprox 11740$:
$$\Delta	heta pprox 1/\gamma pprox 85 \mu	ext{rad} pprox 0.0049°$$

Đây là chùm tia X cực sáng, cực hẹp — sáng gấp $10^{12}$ lần nguồn tia X thông thường.

### 5. Ứng Dụng Trong Kỹ Thuật Chính Xác

**a) Lithography tia X (X-ray Lithography):**

Bức xạ synchrotron được dùng trong chế tạo MEMS (Micro-Electro-Mechanical Systems) và vi cơ cấu với độ phân giải dưới 100 nm — thấp hơn nhiều so với UV lithography thông thường. Trong sản xuất con quay hồi chuyển (gyroscope) MEMS cho hệ thống dẫn đường quán tính (INS) trong vũ khí, cấu trúc flexure cần dung sai < 1 μm — synchrotron lithography cho phép điều này.

**b) X-ray Diffraction (XRD) và Strain Analysis:**

Bức xạ synchrotron cho phép đo biến dạng (strain) trong vật liệu kết cấu với độ chính xác $\Deltaarepsilon \sim 10^{-5}$ — không thể đạt được với nguồn tia X thông thường. Ứng dụng trong kiểm tra ứng suất dư trong các chi tiết gia công chính xác (barrel của vũ khí, trục của gyroscope).

**c) Tomography 3D:**

Synchrotron CT scan với tia X đơn sắc cho hình ảnh 3D không có beam hardening artifact, phân giải voxel dưới 1 μm. Ứng dụng trong reverse engineering và kiểm tra chất lượng không phá hủy (NDT) cho cụm cơ khí chính xác.

### 6. Bảng So Sánh Thông Số Synchrotron

| Thông số | Cyclotron thông thường | Synchrotron hiện đại |
|----------|----------------------|---------------------|
| Năng lượng electron | < 20 MeV | 1–10 GeV |
| $\gamma$ | ~40 | ~2000–20000 |
| Góc chùm tia | ~1/40 rad (~1.4°) | <0.1 mrad |
| Bước sóng tới hạn | mm → microwave | Å → tia X cứng |
| Ứng dụng | Y học | Vật liệu, lithography, sinh học |

### Kết Luận

Bức xạ synchrotron là nơi giao thoa của cơ học tương đối tính, điện động lực học, và kỹ thuật máy gia tốc. Công thức $p = qBR$ cho phép thiết kế chính xác quỹ đạo electron; quan hệ $P \propto E^4/R^2$ đặt giới hạn thực tế cho máy gia tốc electron; và $\Delta	heta \sim 1/\gamma$ giải thích tại sao nguồn sáng synchrotron vô song về độ sáng và độ định hướng.

---
*Exported from Feynman Bot*
