---
lesson_id: 5452
lesson_type: concept
approval_status: approved
exported_at: "2026-03-02T15:10:29.798451+00:00"
content_hash: 035de8a30bdb
chapter_number: 18
chapter_title: Chapter 18
section_number: 4
section_title: 18–3Angular momentum
---
# ## Moment Động Lượng: Định Luật Bảo Toàn Ẩn Sau Mọi Chuyển Động Quay

*Source: Chapter 18 - Chapter 18 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_18.html)*

## Moment Động Lượng: Định Luật Bảo Toàn Ẩn Sau Mọi Chuyển Động Quay

Bạn có bao giờ ngồi trên ghế xoay và dang tay ra, rồi kéo tay vào? Tốc độ quay tăng vọt. Không có ai đẩy, không có motor — vậy năng lượng từ đâu ra? Câu hỏi này dẫn chúng ta đến một trong những định luật bảo toàn đẹp nhất trong vật lý: **bảo toàn moment động lượng (conservation of angular momentum)**.

### Từ Lực đến Mô-men Xoắn

Chúng ta biết rằng lực ngoại tác tổng hợp bằng tốc độ thay đổi động lượng: $\vec{F}_{\text{ext}} = d\vec{p}/dt$. Feynman chỉ ra một định lý song song cực kỳ đẹp: **mô-men xoắn ngoại tác tổng hợp bằng tốc độ thay đổi moment động lượng**:

$$\vec{\tau}_{\text{ext}} = \frac{d\vec{L}}{dt}$$

Đây không phải ngẫu nhiên — đây là hệ quả trực tiếp từ Newton's laws khi áp dụng cho hệ nhiều hạt, như chúng ta sẽ thấy. Và cũng như lực bằng không dẫn đến bảo toàn động lượng, **mô-men xoắn ngoại tác bằng không dẫn đến bảo toàn moment động lượng** $L = \text{const}$.

### Định Nghĩa Moment Động Lượng

Với một hạt đơn lẻ khối lượng $m$ chuyển động tại vị trí $\vec{r}$, moment động lượng đối với trục quay là:
$$L = xp_y - yp_x$$

trong đó $x, y$ là tọa độ và $p_x, p_y$ là các thành phần động lượng. Nếu hạt chuyển động tròn bán kính $r$ với động lượng $p$, thì $L = rp_{\text{tang}} = p \cdot \text{(cánh tay đòn)}$ — ba công thức tương đương cho cùng đại lượng.

### Tại Sao Điều Này Đúng? Phép So Sánh Kỹ Thuật

Hãy nghĩ về điều khiển PID trong hệ servo. Biến trạng thái của chuyển động tịnh tiến là $(x, v, a)$ — vị trí, vận tốc, gia tốc. Biến điều khiển là lực $F$. Hoàn toàn song song, biến trạng thái của chuyển động quay là $(\theta, \omega, \alpha)$ và biến điều khiển là mô-men xoắn $\tau$. Động lượng $p = mv$ trong chuyển động thẳng tương ứng với moment động lượng $L = I\omega$ trong chuyển động quay.

Bảng song song:
| Tịnh tiến | Quay |
|-----------|------|
| Khối lượng $m$ | Moment quán tính $I$ |
| Lực $F$ | Mô-men xoắn $\tau$ |
| Động lượng $p = mv$ | Moment động lượng $L = I\omega$ |
| $F = dp/dt$ | $\tau = dL/dt$ |

Kỹ sư điều khiển nhận ra ngay: toàn bộ lý thuyết điều khiển cho motor servo — từ PID tuning đến state-space representation — đều dựa trên sự song song hoàn hảo này.

### Chứng Minh Từ Newton's Laws

Feynman dẫn dắt ta chứng minh $\tau = dL/dt$ trực tiếp từ $F = ma$. Với hạt tại $(x, y)$:

Mô-men xoắn: $\tau = xF_y - yF_x$

Thay $F_x = m\ddot{x}$, $F_y = m\ddot{y}$:
$$\tau = m(x\ddot{y} - y\ddot{x})$$

Kiểm tra: $\frac{d}{dt}(x\dot{y} - y\dot{x}) = \dot{x}\dot{y} + x\ddot{y} - \dot{y}\dot{x} - y\ddot{x} = x\ddot{y} - y\ddot{x}$

Vậy $\tau = m\frac{d}{dt}(x\dot{y} - y\dot{x}) = \frac{d}{dt}(xp_y - yp_x) = \frac{dL}{dt}$ ✓

Việc mở rộng cho nhiều hạt hoàn toàn tương tự — nội lực triệt tiêu theo cặp hành động-phản hành động.

### Ví Dụ: Cảm Biến Gyroscope trong Vũ Khí Dẫn Đường

Ring Laser Gyroscope (RLG) trong tên lửa hành trình hoạt động dựa trên hiệu ứng Sagnac — hai chùm sáng truyền ngược chiều nhau tạo ra phase shift tỉ lệ với $\omega$ (tốc độ góc). Nhưng vỏ bọc cơ học của RLG (gimbal) có moment động lượng $L_{\text{gimbal}} = I_{\text{gimbal}}\omega_{\text{Earth}}$ do Trái Đất tự quay ($\omega_{\text{Earth}} = 7.27\times10^{-5}$ rad/s). Kỹ sư phải tính toán $L_{\text{gimbal}}$ này chính xác để hiệu chỉnh drift (sai số tích phân) của INS.

Bảo toàn moment động lượng là nền tảng của **momentum wheel** (bánh đà phản lực) trong vệ tinh: thay vì dùng rocket thruster để điều chỉnh hướng (attitude control), vệ tinh quay bánh đà bên trong để thay đổi $L_{\text{flywheel}}$, buộc vỏ vệ tinh quay ngược chiều nhằm bảo toàn $L_{\text{total}} = 0$ (hoặc $=$ const).

### Khi Mô-men Xoắn Bằng Không

Nếu $\tau_{\text{ext}} = 0$, thì $L = I\omega = \text{const}$. Đây là nguyên lý:
- **Vũ công ballet** kéo tay vào: $I$ giảm $\Rightarrow$ $\omega$ tăng
- **Vệ tinh điều chỉnh hướng** bằng momentum wheel: $L_{\text{total}}$ bảo toàn
- **Gyroscope** kháng lại thay đổi hướng: $L$ lớn $\Rightarrow$ cần $\tau$ lớn để thay đổi hướng $\vec{L}$

**Điểm mấu chốt:**

- Moment động lượng $L = I\omega$ là đại lượng bảo toàn khi không có mô-men xoắn ngoại tác — song song hoàn toàn với bảo toàn động lượng tuyến tính
- Phương trình $\tau = dL/dt$ không phải định nghĩa mới mà là hệ quả trực tiếp từ Newton's laws $F = ma$ áp dụng cho hệ nhiều hạt
- Với kỹ sư cơ điện tử, bảo toàn moment động lượng là nền tảng thiết kế momentum wheel trong attitude control vệ tinh, gyroscope trong INS, và phân tích động lực học của mọi hệ thống quay từ motor servo đến bánh đà
- Moment động lượng phụ thuộc vào chọn trục — giống như mô-men xoắn, phải luôn xác định rõ trục tham chiếu khi tính toán

---
*Exported from Feynman Bot*
