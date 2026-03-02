---
lesson_id: 5468
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-02T15:10:30.245911+00:00"
content_hash: e141e811322f
chapter_number: 20
chapter_title: Chapter 20
section_number: 3
section_title: 20–2The rotation equations using cross products
---
# ## Moment Xoắn, Động Lượng Góc và Tích Vector — Phân tích Chuyên sâu

*Source: Chapter 20 - Chapter 20 (Section 3) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_20.html)*

## Moment Xoắn, Động Lượng Góc và Tích Vector — Phân tích Chuyên sâu

### 1. Nền Tảng Toán Học: Tích Có Hướng (Cross Product)

Tích vector (cross product) $\mathbf{A} \times \mathbf{B}$ được định nghĩa:

$$\mathbf{A} \times \mathbf{B} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ A_x & A_y & A_z \\ B_x & B_y & B_z \end{vmatrix} = (A_yB_z - A_zB_y)\hat{i} - (A_xB_z - A_zB_x)\hat{j} + (A_xB_y - A_yB_x)\hat{k}$$

Tích vector **không giao hoán**: $\mathbf{A} \times \mathbf{B} = -(\mathbf{B} \times \mathbf{A})$. Đây là đặc tính quan trọng — hướng của torque phụ thuộc vào thứ tự của $\mathbf{r}$ và $\mathbf{F}$, phản ánh thực tế vật lý là chiều quay phụ thuộc vào chiều lực.

### 2. Moment Xoắn (Torque) — Phân Tích Đầy Đủ

**Định nghĩa:** Moment xoắn của lực $\mathbf{F}$ tác dụng tại điểm có vector vị trí $\mathbf{r}$ (từ điểm tham chiếu):

$$\boldsymbol{\tau} = \mathbf{r} \times \mathbf{F}$$

Vi phân thành phần:
- $\tau_x = yF_z - zF_y$
- $\tau_y = zF_x - xF_z$
- $\tau_z = xF_y - yF_x$

Độ lớn: $|\boldsymbol{\tau}| = rF\sin\alpha$, với $\alpha$ là góc giữa $\mathbf{r}$ và $\mathbf{F}$.

**Ý nghĩa vật lý:** $\sin\alpha$ cho thấy chỉ thành phần lực **vuông góc** với cánh tay đòn mới tạo torque. Khi lực song song với $\mathbf{r}$ ($\alpha = 0$), torque bằng không — đây là lý do không thể vặn vít bằng cách kéo theo trục vít.

### 3. Angular Momentum và Định Luật Thứ Hai cho Quay

**Angular momentum** của một hạt:
$$\mathbf{L} = \mathbf{r} \times \mathbf{p} = \mathbf{r} \times m\mathbf{v}$$

**Chứng minh** $\boldsymbol{\tau} = d\mathbf{L}/dt$:

$$\frac{d\mathbf{L}}{dt} = \frac{d}{dt}(\mathbf{r} \times \mathbf{p}) = \dot{\mathbf{r}} \times \mathbf{p} + \mathbf{r} \times \dot{\mathbf{p}}$$

Vì $\dot{\mathbf{r}} = \mathbf{v}$ và $\dot{\mathbf{r}} \times \mathbf{p} = \mathbf{v} \times m\mathbf{v} = m(\mathbf{v} \times \mathbf{v}) = 0$ (tích vector của vector với chính nó bằng 0), ta còn lại:

$$\frac{d\mathbf{L}}{dt} = \mathbf{r} \times \dot{\mathbf{p}} = \mathbf{r} \times \mathbf{F} = \boldsymbol{\tau}$$

**Mở rộng cho hệ nhiều hạt:** Khi tổng hợp qua tất cả hạt, các lực nội lực (internal forces) triệt tiêu nhau (theo định luật Newton III), chỉ còn:

$$\boldsymbol{\tau}_{\text{ext}} = \frac{d\mathbf{L}_{\text{tot}}}{dt}$$

**Bảo toàn angular momentum:** Nếu $\boldsymbol{\tau}_{\text{ext}} = 0$ thì $\mathbf{L}_{\text{tot}} = \text{const}$.

### 4. Angular Velocity là Vector — Phân Tích

Angular velocity $\boldsymbol{\omega}$ **là vector**: hướng dọc theo trục quay, chiều theo quy tắc bàn tay phải. Vận tốc của một điểm trên vật rắn quay:

$$\mathbf{v} = \boldsymbol{\omega} \times \mathbf{r}$$

Angular velocity **có tính cộng vector**: các phép quay nhỏ quanh các trục khác nhau có thể cộng vector. Tuy nhiên, **các phép quay hữu hạn không tuân thủ quy tắc cộng vector** — đây là điểm tinh tế thường gây nhầm lẫn.

### 5. Ứng Dụng Thực Tế: Cảm Biến và Hệ Cơ Điện Tử

**Gyroscope MEMS trong hệ IMU (Inertial Measurement Unit):**
Gyroscope MEMS hoạt động dựa trên **hiệu ứng Coriolis**. Khi khối mass dao động theo phương $x$ với vận tốc $v_x$, và hệ quay với $\omega_z$, lực Coriolis:
$$\mathbf{F}_c = 2m\mathbf{v} \times \boldsymbol{\omega}$$
Tạo ra độ lệch theo phương $y$, được đo bởi capacitive sense electrodes. Độ nhạy đạt $\sim 0.01°/s/\sqrt{Hz}$ trong các MEMS gyro hiện đại (ví dụ ICM-42688-P của InvenSense).

**Reaction Wheel trong hệ điều khiển tư thế:**
Tên lửa và vệ tinh sử dụng reaction wheels (bánh đà phản lực) để điều khiển orientation mà không cần thruster. Khi motor quay bánh đà tăng tốc, angular momentum của bánh đà tăng, angular momentum của thân vệ tinh phải giảm (bảo toàn $\mathbf{L}_{\text{tot}}$), tạo ra torque điều khiển.

**Điều khiển gimbal trong hệ quan sát/vũ khí:**
Hệ thống ổn định camera/vũ khí trên xe quân sự sử dụng torque motors và IMU để bù trừ rung động. Controller tính toán torque cần thiết: $\boldsymbol{\tau}_{\text{control}} = I\dot{\boldsymbol{\omega}}_{\text{required}}$.

### 6. Lực Coriolis — Chi Tiết Kỹ Thuật

Trong hệ tọa độ quay với angular velocity $\boldsymbol{\omega}$, gia tốc của một vật có vận tốc $\mathbf{v}'$ (trong hệ quay) bao gồm:
- Gia tốc ly tâm: $-\boldsymbol{\omega} \times (\boldsymbol{\omega} \times \mathbf{r})$
- Gia tốc Coriolis: $-2\boldsymbol{\omega} \times \mathbf{v}'$

Đối với đạn bay từ pháo trên mặt đất ở vĩ độ $\phi$, angular velocity Trái Đất $\Omega = 7.27 \times 10^{-5}$ rad/s. Độ lệch ngang của đạn bay với vận tốc $v_0$ và tầm xa $R$:
$$\delta y \approx \frac{2\Omega \sin\phi \cdot R^2}{v_0}$$
Hệ điều khiển hỏa lực phải bù cho hiệu ứng này.

### 7. Bài Tập Mẫu — Tính Torque trong Hệ Robot

**Bài toán:** Cánh tay robot có khớp quay tại gốc tọa độ. Đầu tay robot cầm một công cụ tại vị trí $\mathbf{r} = (0.3, 0.4, 0.0)$ m. Lực cắt của công cụ tác dụng là $\mathbf{F} = (50, 0, -30)$ N. Tính torque tác dụng lên khớp.

**Giải:**

$$\boldsymbol{\tau} = \mathbf{r} \times \mathbf{F} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 0.3 & 0.4 & 0.0 \\ 50 & 0 & -30 \end{vmatrix}$$

Tính từng thành phần:
- $\tau_x = (0.4)(-30) - (0.0)(0) = -12$ N·m
- $\tau_y = (0.0)(50) - (0.3)(-30) = +9$ N·m  
- $\tau_z = (0.3)(0) - (0.4)(50) = -20$ N·m

Kết quả: $\boldsymbol{\tau} = (-12, 9, -20)$ N·m

Độ lớn: $|\boldsymbol{\tau}| = \sqrt{144 + 81 + 400} = \sqrt{625} = 25$ N·m

**Ý nghĩa kỹ thuật:** Thành phần $\tau_z = -20$ N·m là torque chống lại chiều dương quay quanh trục z, yêu cầu motor khớp phải tạo ra ít nhất 20 N·m để giữ vị trí. Đây là thông số quan trọng để chọn servo motor và thiết kế hộp giảm tốc.

**Điểm mấu chốt:**
- Cross product là ngôn ngữ tự nhiên cho mọi hiện tượng quay trong vật lý 3D.
- $\boldsymbol{\tau} = d\mathbf{L}/dt$ là định luật Newton cho chuyển động quay — nền tảng của điều khiển gimbal, gyroscope và robot.
- Bảo toàn angular momentum giải thích hoạt động của gyroscope INS và reaction wheel.
- Lực Coriolis $2m\mathbf{v} \times \boldsymbol{\omega}$ ảnh hưởng đến cảm biến MEMS và đạn đạo vũ khí, cần bù trừ trong hệ điều khiển chính xác.

---
*Exported from Feynman Bot*
