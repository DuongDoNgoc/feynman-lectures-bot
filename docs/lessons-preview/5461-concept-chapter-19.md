---
lesson_id: 5461
lesson_type: concept
approval_status: approved
exported_at: "2026-03-03T15:33:05.587300+00:00"
content_hash: 0adc8c725514
chapter_number: 19
chapter_title: Chapter 19
section_number: 5
section_title: 19–4Rotational kinetic energy
---
# ## Động Năng Quay và Bảo Toàn Moment Động Lượng

*Source: Chapter 19 - Chapter 19 (Section 5) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_19.html)*

## Động Năng Quay và Bảo Toàn Moment Động Lượng

Bạn đã bao giờ xem một vận động viên trượt băng nghệ thuật thu tay vào người và quay nhanh hơn đột ngột? Hay tự hỏi tại sao một gyroscope (con quay hồi chuyển) trong hệ dẫn đường quán tính của tên lửa lại có thể duy trì hướng ổn định dù tên lửa đang chịu gia tốc mạnh? Những hiện tượng này đều bắt nguồn từ một trong những định luật bảo toàn sâu sắc nhất của cơ học: **bảo toàn moment động lượng** (conservation of angular momentum).

### Động Năng Quay — Sự Tương Tự Với Tịnh Tiến

Khi một vật thể cứng quay với vận tốc góc $\omega$ quanh một trục cố định, mỗi phần tử khối lượng $m_i$ ở khoảng cách $r_i$ từ trục có vận tốc dài $v_i = \omega r_i$. Tổng động năng:

$$E_{\text{quay}} = \sum_i \frac{1}{2}m_i v_i^2 = \sum_i \frac{1}{2}m_i (\omega r_i)^2 = \frac{1}{2}\omega^2 \sum_i m_i r_i^2 = \frac{1}{2}I\omega^2$$

Đây là kết quả đẹp: công thức $\frac{1}{2}I\omega^2$ hoàn toàn song song với $\frac{1}{2}mv^2$ trong tịnh tiến. Moment quán tính $I$ đóng vai trò của "khối lượng quay", còn $\omega$ là "vận tốc quay".

**Phép loại suy kỹ thuật quan trọng:** Trong hệ truyền động điện, motor servo cung cấp torque $\tau$ và tạo ra gia tốc góc $\alpha$. Năng lượng cần cung cấp để tăng tốc từ $\omega_1$ lên $\omega_2$:

$$\Delta E = \frac{1}{2}I(\omega_2^2 - \omega_1^2)$$

Đây chính là lý do tại sao trong thiết kế servo drive cho máy CNC hay robot công nghiệp, kỹ sư phải tối thiểu hóa moment quán tính $I$ của tải (load inertia) — giảm $I$ giúp motor gia tốc nhanh hơn với cùng công suất, cải thiện thời gian đáp ứng (settling time) từ hàng chục millisecond xuống còn vài millisecond.

### Moment Động Lượng và Định Luật Bảo Toàn

Moment động lượng (angular momentum) của vật thể quay:

$$L = I\omega$$

Khi không có torque ngoại tác ($\tau_{\text{ext}} = 0$), moment động lượng được bảo toàn:

$$L = I_1\omega_1 = I_2\omega_2 = \text{const}$$

Đây là lý do vận động viên trượt băng quay nhanh hơn khi thu tay vào: $I$ giảm (khối lượng tập trung gần trục hơn) dẫn đến $\omega$ tăng để giữ $L$ không đổi.

### Ứng Dụng Trong Hệ Dẫn Đường Quán Tính

Con quay hồi chuyển cơ học (mechanical gyroscope) trong hệ INS (Inertial Navigation System) của tên lửa hoặc vũ khí dẫn đường hoạt động chính xác nhờ bảo toàn moment động lượng. Rotor quay với $\omega$ rất lớn (thường 20,000–40,000 rpm) có $L = I\omega$ rất lớn. Theo bảo toàn, nếu không có torque ngoại tác, trục quay giữ nguyên hướng trong không gian quán tính — ngay cả khi vỏ tên lửa thay đổi hướng. Góc lệch giữa khung vỏ và trục rotor được đo bằng cảm biến điện từ, cung cấp tín hiệu góc chính xác cho hệ điều khiển.

Thực tế hiện đại thay gyroscope cơ học bằng **ring laser gyroscope (RLG)** hay **fiber optic gyroscope (FOG)**, nhưng nguyên lý đo vẫn liên hệ chặt chẽ với bảo toàn moment động lượng qua hiệu ứng Sagnac.

### Bảo Toàn Moment Động Lượng Trong Thiết Kế Cơ Học

Một tình huống thú vị xảy ra trong hệ thống với **khớp nối từ tính** (magnetic clutch) hoặc **phanh điện từ** (electromagnetic brake). Khi ly hợp đột ngột nối hai đĩa quay có $I_1, \omega_1$ và $I_2, \omega_2$, nếu bỏ qua tổn thất ma sát trong thời gian ngắn, tốc độ chung sau khi nối:

$$\omega_f = \frac{I_1\omega_1 + I_2\omega_2}{I_1 + I_2}$$

Đây chính xác là phép va chạm hoàn toàn không đàn hồi (perfectly inelastic collision) trong không gian góc. Năng lượng mất đi chuyển thành nhiệt trong khớp nối — thông số quan trọng để thiết kế tản nhiệt cho clutch trong hệ phanh chính xác.

**Điểm mấu chốt:**
- Động năng quay $E = \frac{1}{2}I\omega^2$ song song hoàn toàn với động năng tịnh tiến $\frac{1}{2}mv^2$: $I$ thay $m$, $\omega$ thay $v$.
- Moment động lượng $L = I\omega$ được bảo toàn khi không có torque ngoại tác — nguyên lý nền tảng của con quay hồi chuyển trong hệ dẫn đường.
- Khi $I$ thay đổi (vật thể co lại hoặc giãn ra), $\omega$ phải thay đổi ngược chiều để bảo toàn $L = I_1\omega_1 = I_2\omega_2$.
- Trong servo drive, tối thiểu hóa $I$ của tải trực tiếp cải thiện thời gian đáp ứng và giảm yêu cầu công suất motor.

---
*Exported from Feynman Bot*
