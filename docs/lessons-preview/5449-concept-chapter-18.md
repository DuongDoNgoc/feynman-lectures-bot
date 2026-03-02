---
lesson_id: 5449
lesson_type: concept
approval_status: approved
exported_at: "2026-03-02T15:10:29.738874+00:00"
content_hash: edcb0de88494
chapter_number: 18
chapter_title: Chapter 18
section_number: 1
section_title: 18Rotation in Two Dimensions
---
# ## Động Lực Học Vật Rắn: Khi Một Điểm Không Còn Đủ

*Source: Chapter 18 - Chapter 18 (Section 1) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_18.html)*

## Động Lực Học Vật Rắn: Khi Một Điểm Không Còn Đủ

Bạn đã bao giờ thắc mắc tại sao một con quay hồi chuyển (gyroscope) lại không đổ xuống dù đầu của nó chỉ tựa vào một điểm? Hay tại sao bánh đà (flywheel) trong động cơ servo của robot hàn lại giúp chuyển động mượt mà hơn dù mô-men xoắn đầu vào dao động mạnh? Câu trả lời nằm ở một lĩnh vực vật lý mà Newton's laws của những điểm vật chất đơn lẻ không thể trả lời trực tiếp: **động lực học vật rắn**.

### Giới Hạn của Cơ Học Điểm

Trong các chương trước, chúng ta xử lý vật thể như những hạt điểm — không kích thước, không hình dạng. Luật Newton $F = ma$ áp dụng hoàn hảo cho viên đạn, hành tinh, hay electron. Nhưng thế giới kỹ thuật không toàn là điểm: motor spindle quay với $50.000$ RPM, robot arm có moment quán tính phức tạp, con quay laser trong hệ dẫn đường quán tính có khối lượng phân bố theo thiết kế chính xác. Chúng ta cần mở rộng Newton's laws cho **vật thể có kích thước** — đây là động lực học vật rắn.

### Ý Tưởng Cốt Lõi: Phân Phối Khối Lượng Quan Trọng Hơn Tổng Khối Lượng

Tưởng tượng hai bánh đà có cùng khối lượng $M = 1$ kg và cùng bán kính $R = 10$ cm, nhưng một bánh tập trung khối lượng ở vành ngoài, bánh kia phân bố đều. Dù $F = Ma$ cho gia tốc tịnh tiến hoàn toàn giống nhau, **gia tốc góc** của chúng khi chịu cùng mô-men xoắn sẽ khác nhau rõ rệt.

Đây là lúc cần **moment quán tính** (moment of inertia) $I$ — đại lượng tương tự khối lượng trong chuyển động tịnh tiến nhưng dành cho chuyển động quay:

$$\tau = I\alpha$$

trong đó $\tau$ là mô-men xoắn (torque), $\alpha$ là gia tốc góc. Tương tự như $F = ma$, nhưng với phép quay. Và giống như $m$ đặc trưng cho mức độ "khó gia tốc" trong chuyển động thẳng, $I$ đặc trưng cho mức độ "khó thay đổi tốc độ quay".

### Phép So Sánh Kỹ Thuật: Điện Trở vs. Moment Quán Tính

Hãy nghĩ về mạch điện RC: tụ điện $C$ tích lũy năng lượng và chống lại sự thay đổi điện áp đột ngột. Tương tự, moment quán tính $I$ tích lũy năng lượng quay và chống lại sự thay đổi tốc độ góc đột ngột. Kỹ sư điều khiển motor biết rõ điều này: một motor servo có tải có $I$ lớn sẽ cần nhiều mô-men xoắn hơn để đạt gia tốc góc tương tự, giống như cần nhiều dòng điện hơn để nạp tụ điện lớn nhanh hơn.

Trong thiết kế hệ thống định vị micrometer dùng motor piezoelectric hay motor DC brushless, kỹ sư phải tính $I$ của toàn bộ cụm cơ khí (shaft + coupling + load) để chọn đúng control gain. Nếu $I$ tính sai ngay cả 5%, vòng điều khiển sẽ bị unstable hoặc overshoot — sai số vị trí vượt quá micrometer.

### Chuyển Động Quay Trong Hai Chiều Trước

Feynman khôn ngoan: ông bắt đầu từ trường hợp đơn giản nhất — **vật rắn quay quanh trục cố định** (plane rotation). Một điểm trên vật ở khoảng cách $r$ từ trục sẽ:
- Vận tốc góc: $\omega$ (rad/s), cùng cho mọi điểm
- Vận tốc dài: $v = r\omega$
- Gia tốc hướng tâm: $a_c = r\omega^2$

Hai đại lượng mô tả trạng thái quay:
- **Góc quay** $\theta$ (tương tự vị trí $x$)
- **Vận tốc góc** $\omega = d\theta/dt$ (tương tự vận tốc $v$)

Không gian toán học của chuyển động quay hoàn toàn song song với chuyển động tịnh tiến — chỉ thay $x \to \theta$, $v \to \omega$, $m \to I$, $F \to \tau$.

### Ứng Dụng: Encoder và Phản Hồi Vị Trí

Trong hệ thống CNC hay robot arm sử dụng encoder quang học (optical encoder), mỗi xung từ encoder tương ứng với góc quay $\Delta\theta$ xác định của trục motor. Tần số xung đo trực tiếp $\omega$. Khi kỹ sư lập trình motion profile (acceleration ramp), thực chất đang điều khiển $\alpha = d\omega/dt$ — và mô-men xoắn cần thiết là $\tau = I\alpha$. Hiểu $I$ của hệ thống không chỉ là vật lý thuần túy mà là thông số thiết kế sống còn.

### Mở Rộng: Từ 2D Đến 3D

Feynman cảnh báo: chuyển động quay ba chiều phức tạp hơn rất nhiều. Một vật quay quanh trục $x$ có thể sinh ra lực gyroscopic dọc theo trục $y$ — hiện tượng precession (tiến động). Đây là nền tảng của hệ dẫn đường quán tính (INS) trong tên lửa và máy bay chiến đấu: con quay hồi chuyển (mechanical gyroscope hoặc ring laser gyroscope) dựa trên tính bảo toàn moment động lượng (angular momentum) để giữ hướng tham chiếu không gian.

**Điểm mấu chốt:**

- Vật rắn không thể mô tả đầy đủ bằng $F = ma$ cho điểm vật chất — cần thêm phương trình cho chuyển động quay: $\tau = I\alpha$
- Moment quán tính $I$ phụ thuộc vào **cách phân bố khối lượng**, không chỉ tổng khối lượng — đây là lý do bánh đà thiết kế tập trung khối lượng ở vành ngoài để tích lũy năng lượng quay hiệu quả hơn
- Chuyển động quay 2D là nền tảng; chuyển động quay 3D dẫn đến hiện tượng gyroscopic — cốt lõi của hệ dẫn đường quán tính trong vũ khí chính xác cao
- Đối với kỹ sư cơ điện tử, việc tính đúng $I$ của toàn bộ cụm cơ khí là điều kiện tiên quyết để thiết kế vòng điều khiển servo ổn định với độ chính xác micrometer

---
*Exported from Feynman Bot*
