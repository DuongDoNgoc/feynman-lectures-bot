---
lesson_id: 5464
lesson_type: concept
approval_status: approved
exported_at: "2026-03-02T15:10:30.117929+00:00"
content_hash: 99289bbeaf0c
chapter_number: 20
chapter_title: Chapter 20
section_number: 2
section_title: 20–1Torques in three dimensions
---
# ## Moment Động Lượng 3D và Con Quay Hồi Chuyển (Gyroscope)

*Source: Chapter 20 - Chapter 20 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_20.html)*

## Moment Động Lượng 3D và Con Quay Hồi Chuyển (Gyroscope)

Tại sao một con quay hồi chuyển (gyroscope) lại không ngã khi trục của nó bị nghiêng? Tại sao đầu đạn xoắn (spin-stabilized bullet) lại bay thẳng hơn đầu đạn không xoắn? Tại sao xe đạp dễ giữ thăng bằng hơn khi bánh xe quay nhanh? Tất cả những hiện tượng kỳ lạ này đều xuất phát từ một thực tế đơn giản nhưng sâu sắc: **moment động lượng là một vector**, và vector đó có xu hướng mạnh mẽ để duy trì hướng của mình.

### Moment Động Lượng Trong Không Gian 3D

Trong hai chiều, moment động lượng là một số vô hướng $L = I\omega$. Trong ba chiều, mọi thứ phức tạp hơn: vật thể có thể quay quanh bất kỳ trục nào, và moment động lượng phải mô tả cả độ lớn lẫn hướng của sự quay đó.

Moment động lượng của một hạt tại vị trí $\mathbf{r}$ với động lượng $\mathbf{p}$ là:

$$\mathbf{L} = \mathbf{r} \times \mathbf{p}$$

Tích có hướng (cross product) này cho ta một vector vuông góc với cả $\mathbf{r}$ lẫn $\mathbf{p}$, có độ lớn $|\mathbf{L}| = rp\sin\theta$. Đối với một hạt chuyển động tròn, $\mathbf{L}$ hướng dọc theo trục quay theo quy tắc bàn tay phải.

Định lý quan trọng vẫn đúng trong 3D: torque ngoại tác bằng tốc độ thay đổi của moment động lượng:

$$\boldsymbol{\tau} = \frac{d\mathbf{L}}{dt}$$

Đây là phát biểu vector đầy đủ — cả hướng lẫn độ lớn của $\mathbf{L}$ có thể thay đổi.

### Torque Trong Không Gian 3D

Trong 2D, ta chỉ có một mặt phẳng quay $xy$ và torque là $\tau_{xy} = xF_y - yF_x$. Trong 3D, có ba mặt phẳng quay: $xy$, $yz$, $zx$. Ứng với mỗi mặt phẳng là một thành phần torque:

- $\tau_{xy} = xF_y - yF_x$ (quay trong mặt $xy$, quanh trục $z$)
- $\tau_{yz} = yF_z - zF_y$ (quay trong mặt $yz$, quanh trục $x$)
- $\tau_{zx} = zF_x - xF_z$ (quay trong mặt $zx$, quanh trục $y$)

Ba thành phần này chính là ba thành phần của vector tích có hướng $\boldsymbol{\tau} = \mathbf{r} \times \mathbf{F}$:

$$\boldsymbol{\tau} = \mathbf{r} \times \mathbf{F} = \begin{vmatrix} \mathbf{\hat{x}} & \mathbf{\hat{y}} & \mathbf{\hat{z}} \\ x & y & z \\ F_x & F_y & F_z \end{vmatrix}$$

**Phép loại suy kỹ thuật:** Trong hệ gimbal ba trục (three-axis gimbal) dùng cho hệ ổn định quang học của tên lửa hay drone, ba cụm encoder đo ba thành phần góc quay tương ứng với ba mặt phẳng $xy$, $yz$, $zx$. Mỗi servo motor điều khiển một trục, tạo ra torque vector $\boldsymbol{\tau}$ để bù cho chuyển động của thân phương tiện. Việc phân tích torque trong từng mặt phẳng riêng biệt — rồi tổng hợp — cho phép kỹ sư thiết kế bộ điều khiển cascade (tầng) đơn giản hơn.

### Hiện Tượng Tuế Sai (Precession) — Trái Tim Của Con Quay Hồi Chuyển

Hiện tượng kỳ diệu nhất của moment động lượng 3D là **tuế sai** (precession). Hãy tưởng tượng một con quay hồi chuyển quay nhanh với $\mathbf{L}$ hướng ngang. Trọng lực tác dụng lên con quay tạo ra torque $\boldsymbol{\tau}$ hướng vuông góc với $\mathbf{L}$.

Theo $\boldsymbol{\tau} = d\mathbf{L}/dt$, torque không làm thay đổi *độ lớn* của $\mathbf{L}$ mà chỉ thay đổi *hướng*. Kết quả: $\mathbf{L}$ quay xung quanh trục thẳng đứng với vận tốc góc tuế sai:

$$\Omega_{\text{tuế sai}} = \frac{\tau}{L} = \frac{mgr}{I\omega}$$

Đây là lý do con quay không ngã: thay vì đổ xuống, nó "lảo đảo" quanh trục thẳng đứng. Và khi $\omega$ (tốc độ quay của rotor) càng lớn thì $\Omega_{\text{tuế sai}}$ càng nhỏ — con quay quay chậm lại quanh trục đứng, hướng trục ổn định hơn.

### Ứng Dụng Trong Hệ Dẫn Đường và Vũ Khí

**Đầu đạn xoắn (spin-stabilized projectile):** Rãnh xoắn (rifling) trong nòng súng làm đầu đạn quay với $\omega$ lớn. $\mathbf{L}$ lớn giúp đầu đạn chống lại torque khí động học làm lật đạn — cơ chế gyroscopic stability. Tuy nhiên, tuế sai do trọng lực gây ra hiệu ứng drift ngang (gyroscopic drift), cần hiệu chỉnh trong bắn tầm xa.

**Hệ INS (Inertial Navigation System):** Gyroscope cơ học trong INS thế hệ cũ duy trì hướng ổn định trong không gian quán tính nhờ $L = I\omega$ lớn. Gimbal cách ly rotor khỏi chuyển động của thân phương tiện, encoder đo góc lệch giữa hai hệ quy chiếu.

**Điểm mấu chốt:**
- Moment động lượng trong 3D là vector: $\mathbf{L} = \mathbf{r} \times \mathbf{p}$, hướng theo quy tắc bàn tay phải.
- Phương trình cơ bản: $\boldsymbol{\tau} = d\mathbf{L}/dt$ — torque thay đổi hướng và/hoặc độ lớn của $\mathbf{L}$.
- Torque vuông góc với $\mathbf{L}$ không làm thay đổi tốc độ quay mà làm trục quay xoay sang hướng khác — đây là hiện tượng tuế sai.
- Tuế sai gyroscopic là nền tảng của con quay hồi chuyển, đầu đạn xoắn, và hệ ổn định quán tính trong vũ khí/phương tiện dẫn đường.

---
*Exported from Feynman Bot*
