---
lesson_id: 5465
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:05.690494+00:00"
content_hash: b866f10d98b6
chapter_number: 20
chapter_title: Chapter 20
section_number: 2
section_title: 20–1Torques in three dimensions
---
# ## Moment Động Lượng 3D và Con Quay Hồi Chuyển — Phân tích Chuyên sâu

*Source: Chapter 20 - Chapter 20 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_20.html)*

## Moment Động Lượng 3D và Con Quay Hồi Chuyển — Phân tích Chuyên sâu

### 1. Moment Động Lượng Như Một Vector Trong 3D

Trong 2D, moment động lượng $L = xp_y - yp_x$ là một số (thành phần $z$ của vector 3D). Trong không gian 3D, moment động lượng của một hạt khối lượng $m$ tại vị trí $\mathbf{r} = (x, y, z)$ với vận tốc $\mathbf{v}$ là:

$$\mathbf{L} = \mathbf{r} \times \mathbf{p} = m(\mathbf{r} \times \mathbf{v})$$

Các thành phần:

$$L_x = yp_z - zp_y, \quad L_y = zp_x - xp_z, \quad L_z = xp_y - yp_x$$

Thành phần $L_z = xp_y - yp_x$ chính là moment động lượng trong mặt phẳng $xy$ — kết quả quen thuộc từ 2D. Hai thành phần còn lại $L_x, L_y$ xuất hiện khi chuyển động không nằm trong một mặt phẳng duy nhất.

### 2. Torque 3D — Phân Tích Đầy Đủ

Torque của lực $\mathbf{F}$ tác dụng tại điểm $\mathbf{r}$:

$$\boldsymbol{\tau} = \mathbf{r} \times \mathbf{F}$$

Các thành phần:

$$\tau_x = yF_z - zF_y \quad (\text{mặt phẳng } yz)$$
$$\tau_y = zF_x - xF_z \quad (\text{mặt phẳng } zx)$$
$$\tau_z = xF_y - yF_x \quad (\text{mặt phẳng } xy)$$

Phương trình động lực học vector:

$$\boldsymbol{\tau} = \frac{d\mathbf{L}}{dt}$$

Đây là phương trình vector — ba phương trình vô hướng độc lập:

$$\tau_x = \frac{dL_x}{dt}, \quad \tau_y = \frac{dL_y}{dt}, \quad \tau_z = \frac{dL_z}{dt}$$

### 3. Bất Biến Dưới Phép Quay Tọa Độ

Một tính chất quan trọng: nếu đổi sang hệ tọa độ $(x', y', z')$ quay một góc so với hệ $(x, y, z)$, các thành phần của $\boldsymbol{\tau}$ và $\mathbf{L}$ thay đổi (do tính vật lý của $\mathbf{r} \times \mathbf{F}$), nhưng mối quan hệ $\boldsymbol{\tau} = d\mathbf{L}/dt$ vẫn đúng trong hệ mới. Đây là tính chất covariance (đồng biến) của phương trình vector — tại sao kỹ sư có thể viết phương trình động lực học trong hệ tọa độ thuận tiện nhất (ví dụ: hệ gắn với vật thể — body frame) và kết quả vẫn đúng vật lý.

### 4. Tensor Quán Tính — Tổng Quát Của Moment Quán Tính Trong 3D

Đối với vật thể cứng quay với $\boldsymbol{\omega}$, quan hệ $\mathbf{L} = I\boldsymbol{\omega}$ chỉ đúng nếu $I$ là **tensor quán tính** (inertia tensor) — ma trận $3 \times 3$ đối xứng:

$$\mathbf{L} = \mathbf{I}\boldsymbol{\omega}, \quad \mathbf{I} = \begin{pmatrix} I_{xx} & -I_{xy} & -I_{xz} \\ -I_{xy} & I_{yy} & -I_{yz} \\ -I_{xz} & -I_{yz} & I_{zz} \end{pmatrix}$$

Các phần tử đường chéo: $I_{xx} = \int(y^2+z^2)dm$, tổng quát là "moment quán tính" theo nghĩa thông thường.

Các phần tử ngoài đường chéo: $I_{xy} = \int xy\,dm$ — gọi là "product of inertia" (tích quán tính). Chúng bằng 0 nếu vật có mặt phẳng đối xứng trùng với mặt phẳng tọa độ.

**Trục chính (principal axes):** Luôn tồn tại một hệ tọa độ (gọi là hệ trục chính) trong đó tensor quán tính là ma trận đường chéo. Trong hệ này $\mathbf{L} = I\boldsymbol{\omega}$ đơn giản trở lại: $L_i = I_i\omega_i$. Bài toán tìm trục chính tương đương với bài toán giá trị riêng (eigenvalue problem): $\mathbf{I}\boldsymbol{\omega} = \lambda\boldsymbol{\omega}$.

### 5. Hiện Tượng Tuế Sai (Precession) — Suy Dẫn Định Lượng

Con quay hồi chuyển: rotor khối lượng $M$, moment quán tính $I$, quay với $\omega$ lớn. Trục rotor nằm ngang, được giữ tại một đầu. Trọng lực $Mg$ tạo torque:

$$\tau = Mgr \quad (\text{vuông góc với } \mathbf{L})$$

Theo $\boldsymbol{\tau} = d\mathbf{L}/dt$, trong thời gian $dt$:

$$|d\mathbf{L}| = \tau \, dt = Mgr \, dt$$

Vì $d\mathbf{L} \perp \mathbf{L}$, vector $\mathbf{L}$ quay góc:

$$d\phi = \frac{|d\mathbf{L}|}{|\mathbf{L}|} = \frac{Mgr\,dt}{I\omega}$$

Vận tốc tuế sai:

$$\Omega_p = \frac{d\phi}{dt} = \frac{Mgr}{I\omega}$$

**Nhận xét quan trọng:** $\Omega_p \propto 1/(I\omega)$. Để giảm tuế sai (ổn định tốt hơn): tăng $I$ hoặc tăng $\omega$. Giới hạn thực tế là sức bền vật liệu — tốc độ góc tối đa bị giới hạn bởi ứng suất ly tâm.

### 6. Ứng Dụng Thực Tế: Hệ Đo Lường Quán Tính IMU

**Ring Laser Gyroscope (RLG) trong hệ INS:** Không dùng rotor cơ học, nhưng nguyên lý đo vẫn là moment động lượng — của photon (ánh sáng). Hai chùm tia laser truyền ngược chiều trong vòng quang học. Khi hệ quay, hiệu ứng Sagnac tạo ra hiệu pha giữa hai chùm tỷ lệ với vận tốc góc:

$$\Delta\phi = \frac{4A\omega}{\lambda c}$$

trong đó $A$ là diện tích vòng quang, $\lambda$ là bước sóng, $c$ là tốc độ ánh sáng. Độ nhạy điển hình: $0.001\,°/\text{hr}$, tương đương sai lệch vị trí $\sim 10\,\text{m}$ sau 1 giờ — đủ cho dẫn đường tên lửa hành trình.

**MEMS Gyroscope (Coriolis-based):** Vi cơ điện tử (MEMS) dùng lực Coriolis để đo $\omega$. Một khối rung (proof mass) dao động theo hướng $x$. Khi hệ quay với $\omega$ quanh $z$, lực Coriolis $F_C = 2m\mathbf{v} \times \boldsymbol{\omega}$ tạo ra lực theo $y$, đo bởi capacitive sensor. Độ phân giải: $0.1°/\text{s}/\sqrt{\text{Hz}}$. Ứng dụng: IMU trong đạn pháo thông minh (XM1156 Precision Guidance Kit), drone quân sự.

### 7. Bài Toán Mẫu: Tuế Sai Và Góc Drift Trong Dẫn Đường

**Đề bài:** Gyroscope cơ học trong hệ INS có: $I = 5 \times 10^{-5}\,\text{kg·m}^2$, tốc độ quay $\omega = 3000\,\text{rad/s}$ (~28,648 rpm), trọng tâm rotor lệch khỏi điểm tựa $r = 0.5\,\text{mm}$, khối lượng rotor $M = 20\,\text{g}$.

a) Tính vận tốc tuế sai $\Omega_p$.
b) Sau 1 giờ bay, góc drift của trục gyro là bao nhiêu?
c) Tính sai số vị trí tương ứng nếu tên lửa bay ở tốc độ $v = 300\,\text{m/s}$.

**Lời giải:**

a) Torque trọng lực:
$$\tau = Mgr = 0.020 \times 9.8 \times 0.0005 = 9.8 \times 10^{-5}\,\text{N·m}$$

Moment động lượng:
$$L = I\omega = 5 \times 10^{-5} \times 3000 = 0.15\,\text{kg·m}^2/\text{s}$$

Tuế sai:
$$\Omega_p = \frac{\tau}{L} = \frac{9.8 \times 10^{-5}}{0.15} = 6.53 \times 10^{-4}\,\text{rad/s} \approx 0.037\,°/\text{s}$$

b) Sau $t = 3600\,\text{s}$:
$$\Delta\phi = \Omega_p \times t = 6.53 \times 10^{-4} \times 3600 = 2.35\,\text{rad} \approx 135°$$

Đây là sai số rất lớn! Lý do gyroscope cơ học cần gimbal isolation và torque compensation liên tục.

c) Sai số vị trí (ước lượng đơn giản, giả sử drift tích lũy tuyến tính ban đầu):
$$\Delta x \approx v \times t \times \Delta\phi_{\text{nhỏ}} \approx 300 \times 1 \times 6.53 \times 10^{-4} = 0.196\,\text{m/s sai số góc}$$

Thực tế, error budget trong INS dùng con số drift rate $\,°/\text{hr}$. Gyro này có $\sim 133\,°/\text{hr}$ — quá lớn cho ứng dụng. INS hiện đại dùng RLG/FOG với drift $< 0.01\,°/\text{hr}$, tương đương sai vị trí $< 18\,\text{m/hr}$ — chấp nhận được cho tên lửa hành trình với GPS backup.

**Bài học thiết kế:** Lệch tâm rotor $r$ phải được kiểm soát ở cấp micromet. Với $r = 1\,\mu\text{m}$ thay vì $0.5\,\text{mm}$, drift rate giảm xuống $0.000267\,°/\text{hr}$ — vào vùng RLG chất lượng tốt. Đây là lý do gia công rotor gyroscope yêu cầu độ tròn (roundness) và cân bằng động (dynamic balance) ở cấp độ dưới micromet.

---
*Exported from Feynman Bot*
