---
lesson_id: 5516
lesson_type: deep_dive
approval_status: pending
exported_at: "2026-03-02T15:10:31.517529+00:00"
content_hash: 4ff0e2374e21
chapter_number: 27
chapter_title: Chapter 27
section_number: 2
section_title: 27–1Introduction
---
# ## Quang Học Hình Học và Phương Trình Ảnh Gaussian — Phân tích Chuyên sâu

*Source: Chapter 27 - Chapter 27 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_27.html)*

## Quang Học Hình Học và Phương Trình Ảnh Gaussian — Phân tích Chuyên sâu

### Bối Cảnh: Tại Sao Quang Học Hình Học Vừa Đơn Giản Vừa Phức Tạp?

Feynman đặt ra một nhận xét sắc sảo: quang học hình học (geometrical optics) là môn học "hoặc rất đơn giản hoặc rất phức tạp". Ở cấp độ nhập môn, ta dùng quy tắc vẽ tia đơn giản. Ở cấp độ thiết kế thực sự (tính aberration, profile tối ưu), bài toán vượt ra ngoài phạm vi bài giảng cơ bản. Giải pháp thực tế hiện đại: ray tracing bằng máy tính — tính toán từng tia qua từng bề mặt quang học. Đây là cách thiết kế thấu kính trong công nghiệp, và không có gì huyền bí hơn: áp dụng định luật Snell liên tục.

### Công Thức Hình Học Nền Tảng: Xấp Xỉ Paraxial

Tất cả quang học hình học paraxial bắt đầu từ một bài toán hình học đơn giản: xét tam giác với đáy dài $d$, chiều cao nhỏ $h$, và cạnh huyền $s$.

**Bước 1:** Áp dụng định lý Pythagoras:
$$s^2 = d^2 + h^2 \Rightarrow s^2 - d^2 = h^2$$

**Bước 2:** Phân tích:
$$(s-d)(s+d) = h^2$$

**Bước 3:** Trong gần đúng paraxial ($h \ll d$), ta có $s \approx d$, nên $s + d \approx 2s$:
$$(s-d) \cdot 2s \approx h^2 \Rightarrow s - d = \Delta \approx \frac{h^2}{2s}$$

Vậy:
$$\boxed{\Delta \approx \frac{h^2}{2s}}$$

Đây là công thức duy nhất cần thiết để phân tích toàn bộ quang học hình học paraxial! Ý nghĩa vật lý: sự chênh lệch giữa đường huyền và đáy tỉ lệ với bình phương chiều cao — nên gần đúng paraxial càng tốt khi tia sáng càng gần trục.

### Phân Tích Bề Mặt Khúc Xạ Đơn: Suy Ra Phương Trình Gaussian

Xét bề mặt cầu bán kính $R$ ngăn cách không khí (chiết suất $1$) và môi trường chiết suất $n$. Vật điểm $O$ ở khoảng cách $s$ phía trái bề mặt. Điểm ảnh $O'$ ở khoảng cách $s'$ phía phải.

Tia từ $O$ đến điểm $P$ trên bề mặt (cao $h$ so với trục), rồi khúc xạ đến $O'$. Điều kiện Fermat: thời gian đi theo mọi tia phải bằng nhau.

**Tính optical path length:**

Đường từ $O$ đến $P$ trong không khí:
$$OP = \sqrt{s^2 + h^2} \approx s + \frac{h^2}{2s}$$

Đường từ $P$ đến $O'$ trong môi trường $n$:
$$PO' = \sqrt{s'^2 + h^2} \approx s' + \frac{h^2}{2s'}$$

Tuy nhiên, bề mặt cầu có độ lồi: điểm $P$ lệch một lượng $\delta$ so với mặt phẳng đỉnh:
$$\delta \approx \frac{h^2}{2R}$$

(Cùng công thức $\Delta = h^2/2s$ với $s = R$)

OPL tổng (tính từ $O$ qua $P$ đến $O'$, kể đến độ lồi bề mặt):
$$\text{OPL} = OP + n \cdot PO' = \left(s + \frac{h^2}{2s}\right) - \delta + n\left(s' + \frac{h^2}{2s'}\right) + n\delta$$

Điều kiện Fermat: OPL độc lập với $h$ (không phụ thuộc vào vị trí của $P$), tức là hệ số của $h^2$ bằng 0:
$$\frac{1}{2s} - \frac{1}{2R} + \frac{n}{2s'} + \frac{n}{2R} = 0$$

Sau khi nhân $2$ và sắp xếp:
$$\frac{1}{s} + \frac{n}{s'} = \frac{n-1}{R}$$

Hoặc dưới dạng quy ước ký hiệu chuẩn (với $s$ âm nếu vật ở phía trái):
$$\boxed{\frac{n}{s'} - \frac{1}{s} = \frac{n-1}{R}}$$

Đây là **phương trình Gaussian cho bề mặt khúc xạ đơn** — kết quả quan trọng nhất của quang học paraxial!

**Ý nghĩa vật lý từng hạng tử:**
- $1/s$: "độ phân kỳ" của tia từ vật
- $n/s'$: "độ hội tụ" tia đến ảnh, nhân với chiết suất
- $(n-1)/R$: "lực hội tụ" (power) của bề mặt, phụ thuộc độ cong và độ chênh chiết suất

### Ứng Dụng Trực Tiếp: Thiết Kế Thấu Kính Mỏng

Thấu kính mỏng gồm hai bề mặt cầu. Áp dụng phương trình Gaussian cho từng bề mặt và kết hợp:

$$\frac{1}{f} = (n-1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right)$$

Đây là **công thức lensmaker** (công thức nhà chế tạo thấu kính). Với vật ở vô cực ($s \to \infty$):
$$\frac{1}{s'} = \frac{1}{f} \Rightarrow s' = f$$

Tia song song hội tụ tại tiêu điểm $f$ — kết quả ai cũng biết, nhưng giờ ta biết nó xuất phát từ đâu.

**Phương trình ảnh tổng quát:**
$$\frac{1}{s'} - \frac{1}{s} = \frac{1}{f}$$

### Bài Tập Mẫu: Thiết Kế Objective Lens cho Cảm Biến Laser

**Đề bài:** Thiết kế thấu kính objective để hội tụ chùm laser song song (vật ở vô cực) về tiêu điểm $f = 25\,\text{mm}$. Thấu kính làm bằng kính N-BK7 ($n = 1.517$). Chọn thiết kế plano-convex ($R_2 = \infty$). Tính $R_1$.

**Lời giải:**

*Bước 1:* Áp dụng công thức lensmaker với $R_2 = \infty$:
$$\frac{1}{f} = (n-1)\left(\frac{1}{R_1} - \frac{1}{\infty}\right) = \frac{n-1}{R_1}$$

*Bước 2:* Tính $R_1$:
$$R_1 = f(n-1) = 25 \times (1.517 - 1) = 25 \times 0.517 = 12.925\,\text{mm}$$

*Bước 3:* Kiểm tra — bề mặt lồi với bán kính $12.9\,\text{mm}$, bề mặt phẳng hướng vào chùm tia (thiết kế đúng để giảm spherical aberration với vật ở vô cực).

*Bước 4:* Đánh giá aberration: với $h = 3\,\text{mm}$ (tia cận rìa), spherical aberration $\approx h^4/(8n f^3) \approx 0.5\,\mu\text{m}$ — chấp nhận được cho ứng dụng đo lường $\sim 10\,\mu\text{m}$.

### Ứng Dụng: Ray Tracing trong Thiết Kế Hệ Thống Đo Lường Chính Xác

Trong hệ thống laser tracker hay confocal displacement sensor:

1. **Objective lens:** Hội tụ chùm laser xuống $\sim 1\,\mu\text{m}$ spot. Phương trình Gaussian cho thiết kế ban đầu; ray tracing số học để tối ưu.

2. **Collimating optics:** Chuẩn hóa chùm phản xạ về chùm song song để đưa vào interferometer. Sai số collimation $\delta\theta$ gây sai số OPL $\propto \delta\theta^2$.

3. **Beam splitter:** Chia chùm tia cho reference arm và measurement arm. Độ dày và chiết suất ảnh hưởng đến OPL mỗi nhánh — cần cân bằng chính xác.

**Quy trình thiết kế thực tế:**
1. Xác định tiêu chí: NA (numerical aperture), f/#, wavelength, field size
2. Dùng phương trình Gaussian để chọn loại thấu kính và tiêu cự sơ bộ
3. Ray tracing bằng phần mềm (Zemax, Code V) để tối ưu bề mặt
4. Tính toán tolerance và sensitivity để đảm bảo khả năng sản xuất

### Di Sản Hamilton và Liên Kết với Cơ Học Giải Tích

Lý thuyết quang học Hamilton sử dụng khái niệm **hàm đặc trưng** $W(x, y, z; x', y', z')$ — optical path length theo đường Fermat — để mô tả hoàn toàn hệ quang học. Gradient của $W$ cho hướng tia sáng:
$$\vec{p} = n\hat{u} = \nabla W$$

Đây chính xác là cấu trúc của cơ học Hamilton: hàm $S$ (action) và momentum $p = \partial S/\partial q$. Phương trình Hamilton-Jacobi:
$$H(q, \nabla S) = E$$

trong quang học tương ứng với phương trình eikonal:
$$|\nabla W|^2 = n^2$$

Sự đồng cấu (isomorphism) giữa quang học và cơ học này là nền tảng lý thuyết của cơ học sóng de Broglie và cơ học lượng tử Schrödinger. Một phương trình hình học đơn giản $\Delta = h^2/2s$ mở ra cả một thế giới kết nối.

---
*Exported from Feynman Bot*
