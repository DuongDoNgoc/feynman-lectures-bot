---
lesson_id: 5459
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-02T15:10:29.962574+00:00"
content_hash: b0f03e5c07de
chapter_number: 19
chapter_title: Chapter 19
section_number: 3
section_title: 19–2Locating the center of mass
---
# ## Định Lý Pappus và Moment Quán Tính — Phân tích Chuyên sâu

*Source: Chapter 19 - Chapter 19 (Section 3) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_19.html)*

## Định Lý Pappus và Moment Quán Tính — Phân tích Chuyên sâu

### 1. Định Lý Pappus: Nền Tảng Lý Thuyết

Định lý Pappus-Guldinus (thế kỷ IV SCN) kết nối hình học vi phân với cơ học: *thể tích của khối tròn xoay bằng diện tích tiết diện nhân với quãng đường khối tâm di chuyển*.

**Chứng minh:** Xét diện tích $A$ quay quanh trục $z$ (trục nằm trong cùng mặt phẳng nhưng không cắt hình). Chia $A$ thành các dải nhỏ có diện tích $dA$ tại khoảng cách $x$ từ trục. Khi quay một vòng, dải $dA$ quét ra thể tích:

$$dV = 2\pi x \, dA$$

Tích phân toàn hình:

$$V = \int 2\pi x \, dA = 2\pi \int x \, dA$$

Theo định nghĩa khối tâm: $x_{\text{CM}} = \dfrac{\int x \, dA}{A}$, suy ra $\int x \, dA = A \cdot x_{\text{CM}}$. Vậy:

$$\boxed{V = 2\pi x_{\text{CM}} \cdot A}$$

Tương tự cho diện tích bề mặt của vật tròn xoay từ đường cong có độ dài $L$: $S = 2\pi y_{\text{CM}} \cdot L$.

### 2. Ứng Dụng Định Lý Pappus — Bài Toán Nón và Bán Cầu

**Ví dụ 1 — Thể tích hình nón:** Tam giác vuông cạnh $H$ (chiều cao) và $D/2$ (bán kính đáy), diện tích $A = \tfrac{1}{2} \cdot H \cdot \tfrac{D}{2} = \tfrac{HD}{4}$... 

*Lưu ý:* Dùng tam giác vuông với hai cạnh góc vuông $H$ và $D$ (đường kính) đặt dọc trục, diện tích $A = \tfrac{1}{2}HD$. Khối tâm cách trục $x = D/3$ (từ đỉnh góc vuông). Áp dụng:

$$V = 2\pi \cdot \frac{D}{3} \cdot \frac{1}{2}HD = \frac{\pi D^2 H}{3}$$

Kết quả: $V = \frac{1}{3}\pi r^2 h$ (đặt $r = D/2$, $h = H$). Chính xác!

**Ví dụ 2 — Tìm khối tâm nửa hình tròn:** Nửa đĩa tròn bán kính $r$, diện tích $A = \frac{\pi r^2}{2}$. Khi quay 360° tạo hình cầu, $V_{\text{cầu}} = \frac{4}{3}\pi r^3$. Từ định lý Pappus:

$$\frac{4}{3}\pi r^3 = 2\pi x_{\text{CM}} \cdot \frac{\pi r^2}{2}$$
$$x_{\text{CM}} = \frac{\frac{4}{3}\pi r^3}{\pi^2 r^2} = \frac{4r}{3\pi} \approx 0.4244r$$

Đây là vị trí khối tâm của nửa đĩa tròn — kết quả thu được *không cần tích phân trực tiếp*.

### 3. Moment Quán Tính: Suy Dẫn Đầy Đủ

Moment quán tính $I$ của một vật thể liên tục quay quanh trục $z$:

$$I = \int r^2 \, dm$$

trong đó $r$ là khoảng cách từ phần tử $dm$ đến trục quay, và $dm = \rho \, dV$ với $\rho$ là mật độ khối lượng.

**Moment quán tính hình trụ đặc** (bán kính $R$, khối lượng $M$, chiều dài $L$):

Mật độ dài: $\lambda = M/L$. Chia thành các vành tròn bán kính $r$, bề dày $dr$:

$$dm = \rho \cdot 2\pi r L \, dr = \frac{M}{\pi R^2 L} \cdot 2\pi r L \, dr = \frac{2M}{R^2} r \, dr$$

$$I = \int_0^R r^2 \cdot \frac{2M}{R^2} r \, dr = \frac{2M}{R^2} \cdot \frac{R^4}{4} = \frac{1}{2}MR^2$$

**Moment quán tính hình trụ rỗng** (bán kính trong $R_1$, ngoài $R_2$):

$$I = \frac{1}{2}M(R_1^2 + R_2^2)$$

### 4. Định Lý Trục Song Song (Steiner's Theorem)

Nếu biết $I_{\text{CM}}$ và trục mới song song cách khối tâm $d$:

$$I = I_{\text{CM}} + Md^2$$

**Chứng minh:** Đặt hệ tọa độ tại khối tâm. Trục mới cách $d$ theo hướng $x$. Với phần tử $dm$ tại $(x, y)$:

$$I = \int [(x-d)^2 + y^2]\,dm = \int (x^2+y^2)\,dm - 2d\int x\,dm + d^2\int dm$$

Số hạng đầu là $I_{\text{CM}}$, số hạng giữa bằng 0 (vì $\int x\,dm = M x_{\text{CM}} = 0$ khi tính từ khối tâm), số hạng cuối là $Md^2$. Suy ra $I = I_{\text{CM}} + Md^2$.

### 5. Ứng Dụng Thực Tế Trong Cơ Điện Tử và Đo Lường Chính Xác

**Bánh đà trong servo drive:** Hệ servo của máy CNC cần ổn định tốc độ trong khi cắt gọt. Bánh đà (flywheel) kép — trụ rỗng thay vì trụ đặc — cùng khối lượng nhưng $I$ lớn hơn do $I \propto R_1^2 + R_2^2$. Thiết kế trụ rỗng $R_1 = 0.7R_2$ cho $I$ lớn hơn 49% so với trụ đặc cùng khối lượng, giúp servo "lọc" rung động cắt gọt hiệu quả hơn.

**Hệ gimbal con quay hồi chuyển (gyroscope stabilizer):** Trong hệ ổn định hướng cho camera vũ khí hoặc đầu dò tên lửa, rotor con quay hồi chuyển cần $I$ lớn nhất có thể để duy trì moment động lượng $L = I\omega$ ổn định trước các nhiễu động cơ học. Kỹ sư thiết kế rotor dạng vành (annular ring) để tập trung khối lượng ở bán kính lớn nhất.

### 6. Bài Toán Mẫu Có Lời Giải

**Đề bài:** Một encoder dạng đĩa quang (optical encoder disk) trong hệ đo góc chính xác có: khối lượng $M = 50\,\text{g}$, bán kính ngoài $R_2 = 40\,\text{mm}$, bán kính trong (phần khoét) $R_1 = 25\,\text{mm}$. Trục motor gắn vào tâm đĩa. Sau đó, kỹ sư gắn thêm đối trọng nhỏ khối lượng $m = 5\,\text{g}$ tại bán kính $r = 35\,\text{mm}$ để cân bằng. Tính tổng moment quán tính hệ.

**Lời giải:**

Bước 1 — Moment quán tính đĩa rỗng:
$$I_{\text{đĩa}} = \frac{1}{2}M(R_1^2 + R_2^2) = \frac{1}{2}(0.05)(0.025^2 + 0.040^2)$$
$$= 0.025 \times (6.25 \times 10^{-4} + 1.6 \times 10^{-3}) = 0.025 \times 2.225 \times 10^{-3}$$
$$= 5.5625 \times 10^{-5}\,\text{kg·m}^2$$

Bước 2 — Moment quán tính đối trọng (coi như điểm khối lượng):
$$I_{\text{đối trọng}} = m r^2 = 0.005 \times (0.035)^2 = 0.005 \times 1.225 \times 10^{-3} = 6.125 \times 10^{-6}\,\text{kg·m}^2$$

Bước 3 — Tổng:
$$I_{\text{tổng}} = 5.5625 \times 10^{-5} + 6.125 \times 10^{-6} \approx 6.175 \times 10^{-5}\,\text{kg·m}^2$$

Bước 4 — Ý nghĩa kỹ thuật: với motor tạo torque $\tau = 0.01\,\text{N·m}$, gia tốc góc:
$$\alpha = \frac{\tau}{I} = \frac{0.01}{6.175 \times 10^{-5}} \approx 162\,\text{rad/s}^2$$

Thời gian đạt tốc độ $\omega = 1000\,\text{rpm} \approx 104.7\,\text{rad/s}$:
$$t = \frac{\omega}{\alpha} = \frac{104.7}{162} \approx 0.65\,\text{s}$$

Thông số này quan trọng để kỹ sư điều khiển chỉnh định PID cho vòng lặp tốc độ của hệ servo encoder.

---
*Exported from Feynman Bot*
