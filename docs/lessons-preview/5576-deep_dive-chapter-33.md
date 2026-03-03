---
lesson_id: 5576
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:08.339959+00:00"
content_hash: dbff4711c275
chapter_number: 33
chapter_title: Chapter 33
section_number: 8
section_title: 33–7Anomalous refraction
---
# ## Khúc xạ Bất thường và Lưỡng Chiết — Phân tích Chuyên sâu

*Source: Chapter 33 - Chapter 33 (Section 8) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_33.html)*

## Khúc xạ Bất thường và Lưỡng Chiết — Phân tích Chuyên sâu

### Nền tảng điện từ học: Tensor điện môi

Trong vật liệu đẳng hướng, $\mathbf{D} = arepsilon_0arepsilon_r\mathbf{E}$ — quan hệ vô hướng đơn giản. Trong vật liệu dị hướng (như calcite $	ext{CaCO}_3$), độ cảm điện (susceptibility) là tensor:

$$D_i = arepsilon_0\sum_jarepsilon_{ij}E_j$$

Với hệ tọa độ trùng với trục chính của tinh thể (principal axes), tensor chéo hóa:

$$[arepsilon_{ij}] = egin{pmatrix}arepsilon_x & 0 & 0\0 & arepsilon_y & 0\0 & 0 & arepsilon_z\end{pmatrix}$$

Với tinh thể có đối xứng đơn trục (uniaxial crystal) như calcite: $arepsilon_x = arepsilon_y = arepsilon_\perp$ và $arepsilon_z = arepsilon_\parallel$ (trục $z$ là trục quang học). Điều này dẫn đến hai chỉ số khúc xạ:

$$n_o = \sqrt{arepsilon_\perp}, \quad n_e = \sqrt{arepsilon_\parallel}$$

---

### Phương trình sóng trong tinh thể đơn trục

Đối với sóng phẳng $\mathbf{E} = \mathbf{E}_0 e^{i(\mathbf{k}\cdot\mathbf{r} - \omega t)}$, phương trình Maxwell dẫn đến phương trình Fresnel:

$$\sum_i rac{k_i^2}{rac{\omega^2}{c^2}arepsilon_i - k^2} = 0$$

Giải phương trình này cho hai nghiệm — hai mặt sóng (wave surfaces):

**Mặt cầu** (ordinary wave): $k = \omega n_o/c$ — tốc độ pha độc lập với hướng truyền sóng.

**Mặt elipsoid** (extraordinary wave): Tốc độ pha phụ thuộc góc $\phi$ giữa $\mathbf{k}$ và trục quang học:

$$rac{1}{n_e(\phi)^2} = rac{\cos^2\phi}{n_o^2} + rac{\sin^2\phi}{n_e^2}$$

với $n_e(\phi)$ là chỉ số khúc xạ hiệu dụng.

---

### Hướng năng lượng vs. hướng pha: Sự tách biệt của tia bất thường

Điểm quan trọng nhất về tia bất thường: **hướng truyền năng lượng (tia sáng, Poynting vector) khác với hướng truyền pha (vector sóng k)**!

Đối với tia thường: $\mathbf{S} \parallel \mathbf{k}$ (như trong vật liệu đẳng hướng).

Đối với tia bất thường: góc giữa $\mathbf{S}$ và $\mathbf{k}$ là:

$$	anlpha = rac{n_o^2 - n_e^2}{2n_o^2 n_e^2}\sin(2\phi) \cdot rac{n_e(\phi)^2}{1}$$

(công thức rút gọn — giá trị chính xác phức tạp hơn)

Điều này giải thích tại sao tia bất thường trong tinh thể đi theo đường "kỳ lạ" — hướng năng lượng bị lệch so với mặt sóng.

---

### Tính toán định lượng cho calcite tại $\lambda = 589\,	ext{nm}$

$$n_o = 1.6584, \quad n_e = 1.4864$$

Độ lưỡng chiết: $\Delta n = n_o - n_e = 0.1720$

**Bản bước sóng $\lambda/4$** từ calcite: cần hiệu pha $\delta = \pi/2$:

$$d = rac{\lambda}{4\Delta n} = rac{589\,	ext{nm}}{4 	imes 0.172} = rac{589}{0.688}\,	ext{nm} pprox 856\,	ext{nm} pprox 0.856\,\mu	ext{m}$$

Bản calcite chỉ dày chưa đến $1\,\mu	ext{m}$ đã tạo được bản $\lambda/4$! Trong thực tế dùng bản dày hơn để dễ chế tạo, nhưng phải là bội số lẻ của $\lambda/4$.

---

### Ứng dụng thực tế: Hệ đo ellipsometry trong kiểm tra màng mỏng

**Ellipsometry** là kỹ thuật đo lường đặc tính quang học của màng mỏng (< 1 nm đến vài µm) bằng cách phân tích sự thay đổi trạng thái phân cực ánh sáng phản xạ. Đây là công cụ thiết yếu trong sản xuất linh kiện quân sự và vi điện tử.

**Nguyên lý**: Ánh sáng phân cực elip chiếu vào bề mặt mẫu. Sau phản xạ, trạng thái phân cực thay đổi — đặc trưng bởi hai tham số ellipsometry:

$$	an\Psi \cdot e^{i\Delta} = rac{r_p}{r_s}$$

với $r_p$ và $r_s$ là hệ số phản xạ Fresnel cho phân cực $p$ và $s$, $\Psi$ là góc biên độ, $\Delta$ là hiệu pha.

Từ $\Psi$ và $\Delta$ đo được, giải phương trình Fresnel ngược lại để tìm: chiều dày màng $d$, chỉ số khúc xạ $n$, hệ số tắt dần $\kappa$.

**Ví dụ**: Đo màng SiO$_2$ trên Si (lớp cách điện trong vi mạch quân sự). Độ phân giải độ dày: < 0.1 nm — tức là dưới nửa bán kính nguyên tử!

---

### Bài tập mẫu: Tính độ dày màng từ đo ellipsometry

**Đề bài**: Một màng MgF$_2$ ($n_{film} = 1.38$) phủ trên thủy tinh ($n_{glass} = 1.52$) dùng làm lớp chống phản xạ (AR coating) cho cửa sổ quan học vũ khí. Đo ellipsometry cho $\Delta = 90°$ tại $\lambda = 550\,	ext{nm}$. Với $\Delta pprox rac{4\pi n_{film} d\cos	heta_t}{\lambda}$ và góc khúc xạ $	heta_t = 0°$ (chiếu thẳng đứng), tính độ dày màng $d$ tối ưu.

**Lời giải**:

Bước 1: Điều kiện AR coating tốt nhất: $\Delta = 180°$ (nửa bước sóng quang trình trong màng). Nhưng bài cho $\Delta = 90°$ tương ứng bản $\lambda/4$:

$$d = rac{\lambda}{4n_{film}} = rac{550\,	ext{nm}}{4 	imes 1.38} = rac{550}{5.52} pprox 99.6\,	ext{nm} pprox 100\,	ext{nm}$$

Bước 2: Kiểm tra điều kiện phản xạ cực tiểu cho AR coating: $n_{film} = \sqrt{n_{air} \cdot n_{glass}} = \sqrt{1 	imes 1.52} = 1.233$. Nhận xét: $n_{film} = 1.38 
eq 1.233$ — MgF$_2$ không phải tối ưu tuyệt đối nhưng là vật liệu thực tế tốt nhất (fluoride chịu nhiệt, cứng, bền cho ứng dụng quân sự).

Bước 3: Phản xạ dư: $R = \left(rac{n_{film}^2 - n_{air}n_{glass}}{n_{film}^2 + n_{air}n_{glass}}ight)^2 = \left(rac{1.38^2 - 1.52}{1.38^2 + 1.52}ight)^2 = \left(rac{1.9044 - 1.52}{1.9044 + 1.52}ight)^2 = \left(rac{0.3844}{3.4244}ight)^2 pprox 0.013 = 1.3\%$

Kết quả: màng MgF$_2$ dày $100\,	ext{nm}$ giảm phản xạ từ ~4% (không có màng) xuống còn ~1.3%. Trong ứng dụng quân sự, phản xạ cần < 1% để đảm bảo không lộ vị trí thiết bị qua tín hiệu phản xạ.

---

### Điểm mấu chốt

- Trong tinh thể đơn trục: tensor điện môi dẫn đến hai mặt sóng — mặt cầu (tia $o$) và elipsoid (tia $e$)
- Tia bất thường: hướng truyền năng lượng (Poynting vector) **lệch** so với hướng pha ($\mathbf{k}$) — đây là nguồn gốc của "sự bất thường"
- Bản bước sóng dùng $\Delta n$ của vật liệu để tích lũy hiệu pha — calcite $\Delta n = 0.172$ tạo bản $\lambda/4$ chỉ dày $\sim 1\,\mu	ext{m}$
- Ellipsometry — kỹ thuật đo màng mỏng chính xác nhất hiện nay (< 0.1 nm) — dựa hoàn toàn vào phân tích thay đổi trạng thái phân cực ánh sáng phản xạ từ bề mặt

---
*Exported from Feynman Bot*
