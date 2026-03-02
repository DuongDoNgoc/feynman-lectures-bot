---
lesson_id: 5417
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-02T15:10:28.914086+00:00"
content_hash: d9374ef56fce
chapter_number: 14
chapter_title: Chapter 14
section_number: 4
section_title: 14–3Conservative forces
---
# Lực Bảo Toàn — Phân Tích Chuyên Sâu

*Source: Chapter 14 - Chapter 14 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_14.html)*

# Lực Bảo Toàn — Phân Tích Chuyên Sâu

## Bước 1: Chứng Minh Sự Tương Đương Của Các Định Nghĩa

Có ba định nghĩa tương đương của lực bảo toàn:

**Định nghĩa A**: $\oint \vec{F}\cdot d\vec{s} = 0$ (tích phân đường kín)

**Định nghĩa B**: $W_{A\to B}$ không phụ thuộc đường đi (chỉ phụ thuộc A và B)

**Định nghĩa C**: Tồn tại $U$ sao cho $\vec{F} = -\nabla U$

**A ↔ B**: Xét hai đường $C_1$ và $C_2$ từ A đến B. Đường kín = $C_1$ rồi $C_2$ ngược chiều:
$$\oint = \int_{C_1} - \int_{C_2} = 0 \Leftrightarrow \int_{C_1} = \int_{C_2}$$

**B → C**: Định nghĩa $U(P) = -\int_O^P \vec{F}\cdot d\vec{s}$ (O là điểm gốc). Vì B đúng, $U$ xác định tốt. Tính gradient bằng định lý cơ bản của giải tích:
$$\frac{\partial U}{\partial x} = -\lim_{\Delta x \to 0}\frac{\int_P^{P+\Delta x\hat{i}}\vec{F}\cdot d\vec{s}}{\Delta x} = -F_x$$

## Bước 2: Điều Kiện Curl = 0

Từ $\vec{F} = -\nabla U$:
$$\nabla\times\vec{F} = \nabla\times(-\nabla U) = 0$$

(vì curl của gradient luôn bằng 0 — đây là định lý vi phân ngoài)

Điều kiện thực tế để kiểm tra:
$$\frac{\partial F_z}{\partial y} = \frac{\partial F_y}{\partial z},\quad \frac{\partial F_x}{\partial z} = \frac{\partial F_z}{\partial x},\quad \frac{\partial F_y}{\partial x} = \frac{\partial F_x}{\partial y}$$

**Ví dụ**: Lực từ $\vec{F}_{từ} = q\vec{v}\times\vec{B}$ phụ thuộc vận tốc $\vec{v}$ — không thể là gradient của thế năng vị trí $U(x,y,z)$. Lực từ không bảo toàn theo nghĩa thông thường, nhưng không sinh công (vuông góc với $\vec{v}$).

## Bước 3: Lực Hấp Dẫn — Chứng Minh Bảo Toàn

$\vec{F} = -\frac{GMm}{r^2}\hat{r} = -GMm\frac{\vec{r}}{r^3}$

Kiểm tra curl (tọa độ cầu):
$$(\nabla\times\vec{F})_\phi = \frac{1}{r}\left(\frac{\partial F_r}{\partial\theta}\right) = \frac{1}{r}\frac{\partial}{\partial\theta}\left(-\frac{GMm}{r^2}\right) = 0$$

Vì $F_r$ không phụ thuộc $\theta, \phi$ → curl = 0 → lực hấp dẫn bảo toàn.

Thế năng: $U = -\int_\infty^r F_r\,dr = -\int_\infty^r\left(-\frac{GMm}{r^2}\right)dr = -\frac{GMm}{r}$

## Bước 4: Ứng Dụng Trong Thiết Kế Hệ Thống Đàn Hồi

**Bài toán thực tế**: Tay máy robot có khớp đàn hồi (spring-loaded joint) với $k = 500\,N\cdot m/rad$. Thế năng đàn hồi: $U_{lx} = \frac{1}{2}k\theta^2$.

Lực khớp (mô-men): $\tau = -\frac{\partial U_{lx}}{\partial\theta} = -k\theta$

**Thiết kế hệ thống bù mềm (compliance control)**:
- Motor cung cấp mô-men $\tau_{motor}$
- Lò xo cung cấp mô-men đàn hồi $-k\theta$
- Tổng: $\tau_{eff} = \tau_{motor} - k\theta$

Khi robot chạm vào bề mặt và bị dừng đột ngột, lò xo hấp thụ năng lượng: $U_{lx} = \frac{1}{2}k\theta^2$ — bảo vệ robot và bề mặt.

## Bài Tập: Thiết Kế Cơ Cấu Nhả Năng Lượng

**Cơ cấu bắn đạn lò xo trong thiết bị thử nghiệm**:
- Lò xo $k = 5000\,N/m$, nén $x_0 = 8\,cm = 0.08\,m$
- Viên đạn $m = 50\,g = 0.05\,kg$

Thế năng ban đầu: $U_0 = \frac{1}{2}\times5000\times0.08^2 = 16\,J$

Vận tốc khi rời nòng: $v = \sqrt{2U_0/m} = \sqrt{2\times16/0.05} = \sqrt{640} \approx 25.3\,m/s$

**Phần mở rộng**: Nếu nòng nghiêng $\theta = 30°$ và dài $L = 0.3\,m$, lực ma sát $f = 2\,N$ trong nòng. Thế năng bị mất do ma sát: $W_{ma\,sat} = f\cdot L = 0.6\,J$. Năng lượng còn lại: $15.4\,J$. Vận tốc ra: $v = \sqrt{2\times15.4/0.05} \approx 24.8\,m/s$.

## Điểm Mấu Chốt

Lực bảo toàn được đặc trưng bởi curl = 0, tương đương với tồn tại thế năng. Trong kỹ thuật: lò xo, trọng lực, lực điện đều bảo toàn — có thể tích trữ và trả lại năng lượng. Thiết kế hệ thống lò xo-khớp đàn hồi sử dụng trực tiếp tính chất bảo toàn để tính năng lượng và lực.

---
*Exported from Feynman Bot*
