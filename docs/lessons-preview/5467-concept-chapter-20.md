---
lesson_id: 5467
lesson_type: concept
approval_status: approved
exported_at: "2026-03-03T15:33:05.741614+00:00"
content_hash: c32caf6a8180
chapter_number: 20
chapter_title: Chapter 20
section_number: 3
section_title: 20–2The rotation equations using cross products
---
# ## Moment Xoắn, Động Lượng Góc và Tích Vector

*Source: Chapter 20 - Chapter 20 (Section 3) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_20.html)*

## Moment Xoắn, Động Lượng Góc và Tích Vector

Bạn đã từng thắc mắc tại sao một con quay hồi chuyển (gyroscope) lại không bị đổ ngã khi đang quay nhanh, mặc dù lực hấp dẫn kéo nó xuống? Hay tại sao hệ thống dẫn đường quán tính (INS) trên tên lửa hành trình lại có thể duy trì hướng bay chính xác đến từng micro-radian trong hàng giờ liền? Câu trả lời nằm ở một khái niệm vật lý cực kỳ mạnh mẽ: **moment xoắn (torque)** và **động lượng góc (angular momentum)** — được mô tả hoàn hảo thông qua tích có hướng (cross product) của các vector.

### Torque và Angular Momentum — Hai Công Thức Cốt Lõi

Khi bạn vặn một con vít bằng cờ lê, lực tay bạn tạo ra một moment xoắn. Trong không gian ba chiều, moment xoắn không chỉ có độ lớn mà còn có **hướng** — và đó chính là nơi tích vector phát huy sức mạnh:

$$\boldsymbol{\tau} = \mathbf{r} \times \mathbf{F}$$

Trong đó $\mathbf{r}$ là vector vị trí từ trục quay đến điểm đặt lực, $\mathbf{F}$ là lực tác dụng. Hướng của $\boldsymbol{\tau}$ vuông góc với cả $\mathbf{r}$ và $\mathbf{F}$, tuân theo quy tắc bàn tay phải. Đây không chỉ là ký hiệu toán học — nó nói lên trục mà vật thể sẽ quay.

Tương tự, **động lượng góc (angular momentum)** $\mathbf{L}$ của một hạt được định nghĩa:

$$\mathbf{L} = \mathbf{r} \times \mathbf{p}$$

Với $\mathbf{p} = m\mathbf{v}$ là động lượng thẳng. Angular momentum là "bộ nhớ" của hệ về trạng thái quay: nó ghi nhớ không chỉ tốc độ quay mà cả hướng của trục quay.

### Định Luật Thứ Hai cho Chuyển Động Quay

Sự tương tự với định luật Newton rất thanh lịch. Thay vì $\mathbf{F} = d\mathbf{p}/dt$, đối với chuyển động quay ta có:

$$\boldsymbol{\tau}_{\text{ext}} = \frac{d\mathbf{L}_{\text{tot}}}{dt}$$

Nếu tổng moment xoắn ngoại lực bằng không ($\boldsymbol{\tau}_{\text{ext}} = 0$), thì $\mathbf{L}_{\text{tot}}$ là một hằng số — đây chính là **bảo toàn động lượng góc (conservation of angular momentum)**.

### Ẩn Dụ Kỹ Thuật: Gyroscope trong Hệ Dẫn Đường Quán Tính

Với một kỹ sư cơ điện tử làm việc với hệ thống dẫn đường quán tính (INS) độ chính xác cao, angular momentum chính là nền tảng hoạt động của **gyroscope**. Một gyroscope quay nhanh có angular momentum $\mathbf{L}$ lớn và có hướng cố định trong không gian quán tính. Khi bệ phóng tên lửa thay đổi hướng, $\mathbf{L}$ của gyro vẫn giữ nguyên phương — do không có moment xoắn ngoại lực đáng kể tác dụng lên trục quay — và bộ cảm biến đo góc lệch giữa bệ và trục gyro để xác định orientation chính xác.

Hiện tượng **precession** (tiến động) của gyroscope cũng là hệ quả trực tiếp: khi có torque ngoại lực (ví dụ trọng lực), thay vì đổ ngã, trục gyro quay chậm theo một hướng vuông góc với cả $\mathbf{L}$ và $\boldsymbol{\tau}$. Điều này giải thích tại sao gyroscope cơ học trong hệ INS cũ có thể duy trì hướng ổn định ngay cả khi phương tiện chịu gia tốc mạnh.

Hãy nghĩ đến encoder phản hồi trong servo motor của bạn: encoder đo góc quay $\theta$, tốc độ góc $\omega$, nhưng angular momentum $\mathbf{L} = I\boldsymbol{\omega}$ (với $I$ là moment quán tính) mới là đại lượng quyết định khả năng "chống lại" sự thay đổi hướng quay của rotor. Đây là lý do motor flywheel trong hệ thống ổn định gimbal hoạt động hiệu quả.

### Lực Coriolis — Ứng Dụng Khác của Tích Vector

Một ứng dụng thú vị khác: **lực Coriolis** trong hệ tọa độ quay:

$$\mathbf{F}_c = 2m\mathbf{v} \times \boldsymbol{\omega}$$

Khi bạn thiết kế hệ đo lường trên bệ quay (ví dụ radar tracking trên xe tăng), lực giả Coriolis sẽ ảnh hưởng đến quỹ đạo đạn và độ chính xác nhắm bắn. Các hệ thống điều khiển hỏa lực hiện đại phải bù trừ chính xác cho lực này.

### Tại Sao Tích Vector Là Công Cụ Thiết Yếu?

Tích vector $\mathbf{A} \times \mathbf{B}$ tạo ra một vector **vuông góc** với cả hai vector đầu vào, với độ lớn $|A||B|\sin\theta$. Đây không chỉ là công thức — đây là ngôn ngữ tự nhiên của tự nhiên để mô tả các hiện tượng quay. Ba phương trình thành phần $\tau_x = yF_z - zF_y$, $\tau_y = zF_x - xF_z$, $\tau_z = xF_y - yF_x$ được gói gọn trong một phương trình vector duy nhất $\boldsymbol{\tau} = \mathbf{r} \times \mathbf{F}$ — đó là sức mạnh của ngôn ngữ vector.

**Điểm mấu chốt:**
- **Torque** $\boldsymbol{\tau} = \mathbf{r} \times \mathbf{F}$ và **angular momentum** $\mathbf{L} = \mathbf{r} \times \mathbf{p}$ là các vector 3D, mang thông tin cả về độ lớn lẫn hướng của hiệu ứng quay.
- Định luật $\boldsymbol{\tau}_{\text{ext}} = d\mathbf{L}_{\text{tot}}/dt$ là analog hoàn hảo của định luật Newton cho chuyển động quay.
- Khi $\boldsymbol{\tau}_{\text{ext}} = 0$: **bảo toàn angular momentum** — nguyên lý vận hành của gyroscope và hệ dẫn đường quán tính.
- Lực Coriolis $\mathbf{F}_c = 2m\mathbf{v} \times \boldsymbol{\omega}$ là lực giả trong hệ tọa độ quay, cần bù trừ trong các hệ đo lường và điều khiển hỏa lực chính xác.

---
*Exported from Feynman Bot*
