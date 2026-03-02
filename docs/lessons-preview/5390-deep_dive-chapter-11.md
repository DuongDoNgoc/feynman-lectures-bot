---
lesson_id: 5390
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-02T15:10:28.234161+00:00"
content_hash: 9cfcde6c0b5e
chapter_number: 11
chapter_title: Chapter 11
section_number: 7
section_title: 11–6Newton’s laws in vector notation
---
# ## Định luật Newton Dạng Vectơ — Phân tích Chuyên sâu

*Source: Chapter 11 - Chapter 11 (Section 7) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_11.html)*

## Định luật Newton Dạng Vectơ — Phân tích Chuyên sâu

### 1. Suy dẫn Vectơ Gia tốc

Vị trí hạt: $\mathbf{r}(t) = (x(t), y(t), z(t))$

Vận tốc: $\mathbf{v} = \dfrac{d\mathbf{r}}{dt} = \left(\dfrac{dx}{dt}, \dfrac{dy}{dt}, \dfrac{dz}{dt}\right)$

Gia tốc: $\mathbf{a} = \dfrac{d\mathbf{v}}{dt} = \dfrac{d^2\mathbf{r}}{dt^2} = \left(\dfrac{d^2x}{dt^2}, \dfrac{d^2y}{dt^2}, \dfrac{d^2z}{dt^2}\right)$

Đây là **vectơ** vì biến đổi đúng quy tắc khi xoay hệ tọa độ (vì $x, y, z$ biến đổi đúng quy tắc).

Vì $\mathbf{a}$ là vectơ và $\mathbf{F}$ là vectơ, phương trình $m\mathbf{a} = \mathbf{F}$ đúng trong mọi hệ tọa độ — đây là **bằng chứng toán học** của bất biến Newton, không chỉ là tuyên bố.

### 2. Gia tốc Tiếp tuyến và Pháp tuyến

Xét hạt chuyển động trên quỹ đạo cong. Tại hai thời điểm $t_1, t_2$:

$$\Delta\mathbf{v} = \mathbf{v}_2 - \mathbf{v}_1$$

Phân tích $\Delta\mathbf{v}$ thành hai thành phần:

**Tiếp tuyến** (song song với $\mathbf{v}$): thay đổi tốc độ
$$a_\parallel = \frac{dv}{dt} \quad \text{(v = |v|)}$$

**Pháp tuyến** (vuông góc với $\mathbf{v}$, hướng vào tâm cong): thay đổi hướng

Trong thời gian $\Delta t$, vectơ vận tốc quay góc $\Delta\theta$:
$$\Delta v_\perp = v\Delta\theta$$
$$a_\perp = v\frac{d\theta}{dt}$$

Vì $v = R\dfrac{d\theta}{dt}$ (với $R$ là bán kính cong), ta được:
$$a_\perp = v \cdot \frac{v}{R} = \frac{v^2}{R}$$

Đây là **gia tốc hướng tâm** (centripetal acceleration) — luôn hướng vào tâm cong.

### 3. Ví dụ Thực tế: Phân tích Gia tốc Đầu Công Tác Robot

**Tình huống:** Robot SCARA chạy đường tròn bán kính $R = 0.5$ m với tốc độ tiếp tuyến không đổi $v = 1$ m/s.

**Các thành phần gia tốc:**

- $a_\parallel = dv/dt = 0$ (tốc độ không đổi)
- $a_\perp = v^2/R = 1^2/0.5 = 2$ m/s²

Dù tốc độ bằng không, gia tốc $\mathbf{a}$ vẫn có độ lớn 2 m/s², hướng vào tâm quỹ đạo.

**Lực cần thiết:** Nếu tải trọng $m = 5$ kg:
$$F_{centripetal} = ma_\perp = 5 \times 2 = 10 \text{ N}$$

Motor phải liên tục cung cấp lực hướng tâm này. Đây giải thích tại sao chạy đường tròn với tốc độ cao tiêu thụ nhiều điện hơn đường thẳng dù tốc độ như nhau.

### 4. Bài Tập Mẫu: Gia tốc Đầu Phun trong Hệ CMM

**Đề bài:** Đầu đo CMM (Coordinate Measuring Machine) chuyển động theo quỹ đạo parabola $y = x^2/2$ (đơn vị mét) với thành phần vận tốc $v_x = 0.1$ m/s không đổi. Tìm gia tốc tại $x = 0.3$ m.

**Giải từng bước:**

Bước 1: Tính $v_y$
$$y = x^2/2 \implies rac{dy}{dt} = xrac{dx}{dt} = xv_x = 0.3 	imes 0.1 = 0.03 	ext{ m/s}$$

Bước 2: Tính $a_y$ (vì $v_x$ = const, $a_x = 0$)
$$a_y = rac{d}{dt}(xv_x) = v_xrac{dx}{dt} = v_x^2 = 0.01 	ext{ m/s}^2$$

Bước 3: Tổng hợp
$$\mathbf{a} = (0, 0.01, 0) 	ext{ m/s}^2$$

Bước 4: Ý nghĩa vật lý
Gia tốc hoàn toàn theo chiều $y$, ngay cả khi không có thành phần lực theo $x$. Đây là gia tốc pháp tuyến do quỹ đạo cong, không phải do thay đổi tốc độ.

### 5. Tại Sao Quan Trọng: Feed-Forward trong CNC

Trong CNC hiện đại, bộ điều khiển dùng **feed-forward gia tốc**: tính toán trước $m\mathbf{a}$ cần thiết từ quỹ đạo đã biết, sau đó cộng vào tín hiệu điều khiển. Nếu bộ điều khiển chỉ phản hồi (reactive), sai số bám tỷ lệ với gia tốc:

$$\text{Tracking error} \approx \frac{m}{K_v}|\mathbf{a}|$$

với $K_v$ là độ lợi vận tốc. Ở góc cong $R$ nhỏ hoặc tốc độ $v$ cao, $a_\perp = v^2/R$ lớn → sai số lớn → cần feed-forward.

### Bảng Tóm Tắt

| Thành phần gia tốc | Công thức | Gây ra bởi | Ứng dụng |
|-------------------|-----------|------------|---------|
| Tiếp tuyến $a_\parallel$ | $dv/dt$ | Thay đổi tốc độ | Gia tốc/phanh thẳng |
| Pháp tuyến $a_\perp$ | $v^2/R$ | Thay đổi hướng | Feed-forward CNC, lực ly tâm |
| Tổng | $\sqrt{a_\parallel^2 + a_\perp^2}$ | Cả hai | Chọn motor, tính lực |

---
*Exported from Feynman Bot*
