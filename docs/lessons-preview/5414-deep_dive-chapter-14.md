---
lesson_id: 5414
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:04.479105+00:00"
content_hash: 8f97b8a36b5a
chapter_number: 14
chapter_title: Chapter 14
section_number: 2
section_title: 14–1Work
---
# Ôn Tập: Công và Thế Năng — Phân Tích Chuyên Sâu

*Source: Chapter 14 - Chapter 14 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_14.html)*

# Ôn Tập: Công và Thế Năng — Phân Tích Chuyên Sâu

## Tổng Quan Cấu Trúc

Phần ôn tập này kết nối các khái niệm: công → thế năng → bảo toàn năng lượng, từ một chiều đến không gian 3D đầy đủ.

## Bước 1: Từ 1D Đến 3D — Tổng Quát Hóa

**1D**: $W = \int_{x_1}^{x_2} F_x\,dx$

**3D**: $W = \int_1^2 \vec{F}\cdot d\vec{s} = \int_1^2 (F_x\,dx + F_y\,dy + F_z\,dz)$

Đây không chỉ là ký hiệu khác nhau — nó phản ánh thực tế rằng lực là vectơ và chỉ thành phần dọc theo chuyển động mới sinh công.

**Chứng minh từ định luật Newton:**
$$\vec{F} = m\frac{d\vec{v}}{dt} \Rightarrow \vec{F}\cdot\vec{v} = m\vec{v}\cdot\frac{d\vec{v}}{dt} = \frac{d}{dt}\left(\frac{1}{2}mv^2\right)$$

Tích phân: $\int_1^2 \vec{F}\cdot d\vec{s} = \int_1^2 \vec{F}\cdot\vec{v}\,dt = \frac{1}{2}mv_2^2 - \frac{1}{2}mv_1^2$

Định lý công-động năng tổng quát trong 3D.

## Bước 2: Điều Kiện Tồn Tại Thế Năng (Lực Bảo Toàn)

Lực $\vec{F}$ có thế năng $U$ khi và chỉ khi:
$$\vec{F} = -\nabla U = -\left(\frac{\partial U}{\partial x}\hat{i} + \frac{\partial U}{\partial y}\hat{j} + \frac{\partial U}{\partial z}\hat{k}\right)$$

Điều này tương đương với: $\nabla \times \vec{F} = 0$ (curl bằng không).

**Kiểm tra trọng lực**: $\vec{F} = -mg\hat{k}$, $U = mgz$
$$\frac{\partial F_z}{\partial y} - \frac{\partial F_y}{\partial z} = 0 - 0 = 0\quad\checkmark$$

**Kiểm tra lực ma sát**: $\vec{F} = -\mu mg \hat{v}$ (ngược chiều $\vec{v}$) — phụ thuộc vận tốc, không phải vị trí → không có thế năng.

## Bước 3: Thế Năng Và Trường Lực

Biết thế năng $U(x,y,z)$, có thể tính lại lực:
$$\vec{F} = -\nabla U$$

**Ví dụ — Lò xo 2D**: $U = \frac{1}{2}k(x^2 + y^2)$
$$\vec{F} = -\nabla U = -kx\hat{i} - ky\hat{j} = -k\vec{r}$$

Lực luôn hướng vào tâm với độ lớn tỷ lệ với khoảng cách — lực điều hòa 2D.

## Bước 4: Bảo Toàn Năng Lượng — Công Thức Thực Dụng

$$E = \frac{1}{2}mv^2 + U(x,y,z) = \text{const}$$

**Tại điểm dừng ($v=0$)**: $U(x_0,y_0,z_0) = E$ → tìm được mọi điểm dừng của quỹ đạo.

**Tại điểm có $U_{min}$**: $K = E - U_{min}$ → vận tốc cực đại.

## Ứng Dụng Thực Tế: Phân Tích Robot CNC

Robot khắc laser di chuyển đầu laser theo quỹ đạo 3D. Để duy trì tốc độ tiếp xúc không đổi $v_0 = 50\,mm/s$ và lực tiếp xúc $F_0 = 10\,N$:

**Tổng công suất cơ học cần thiết:**
- Công suất do lực: $P_F = F_0 v_0 = 10 \times 0.05 = 0.5\,W$
- Công suất chống trọng lực (khi đi lên): $P_g = m\,g\,v_z$ (tùy vận tốc theo phương z)

**Điểm quan trọng**: Trên phần đường nằm ngang ($v_z = 0$), motor không cần cung cấp công chống trọng lực. Trên phần đường đi xuống, trọng lực hỗ trợ — có thể thu năng lượng qua phanh tái sinh.

Điều khiển thông minh: theo dõi $\partial h/\partial t = v_z$ theo thời gian thực để điều chỉnh mô-men motor — đây là model-predictive control ứng dụng bảo toàn năng lượng.

## Bài Tập Tổng Hợp

**Bài toán**: Cánh tay robot di chuyển tải $m = 2\,kg$ theo quỹ đạo helical:
- $x(t) = 0.3\cos(\pi t)$, $y(t) = 0.3\sin(\pi t)$, $z(t) = 0.1t$ (m), $t \in [0,\,2]$ s

Tính công cần thiết để chống lại trọng lực trong 2 giây.

**Giải:**
- Chỉ thành phần $F_z = mg = 2\times9.8 = 19.6\,N$ sinh công theo $z$
- $\Delta z = 0.1\times2 = 0.2\,m$
- $W_{trọng\,lực} = -mg\Delta z = -19.6\times0.2 = -3.92\,J$ (trọng lực lấy đi năng lượng từ motor)
- Motor phải cung cấp $+3.92\,J$ để thắng trọng lực

**Lưu ý**: Chuyển động tròn trong $xy$ không đóng góp vào công (lực trọng lực vuông góc với $xy$-plane).

## Điểm Mấu Chốt

Công là tích phân đường 3D, phân rã thành 3 tích phân độc lập theo $x,y,z$. Thế năng tồn tại khi lực có curl bằng 0. Gradient của thế năng cho lại lực — quan hệ nghịch đảo hoàn hảo. Mọi phân tích kỹ thuật của hệ cơ học đều bắt đầu từ những công thức này.

---
*Exported from Feynman Bot*
