---
lesson_id: 5558
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:07.954657+00:00"
content_hash: 3b051f80b4e6
chapter_number: 31
chapter_title: Chapter 31
section_number: 5
section_title: 31–4Absorption
---
# ## Chỉ Số Khúc Xạ Phức và Sự Hấp Thụ Ánh Sáng: Phân Tích Toán Học Chi Tiết

*Source: Chapter 31 - Chapter 31 (Section 5) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_31.html)*

## Chỉ Số Khúc Xạ Phức và Sự Hấp Thụ Ánh Sáng: Phân Tích Toán Học Chi Tiết

### 1. Điểm Xuất Phát: Phương Trình Tán Sắc Với Lực Cản

Phương trình tán sắc tổng quát cho vật liệu có $N$ điện tử/thể tích, mỗi loại có tần số cộng hưởng $\omega_k$, lực cản $\gamma_k$, và cường độ dao động $f_k$ là:

$$n^2 = 1 + \frac{Ne^2}{m\varepsilon_0} \sum_k \frac{f_k}{\omega_k^2 - \omega^2 - i\gamma_k\omega}$$

Số hạng $-i\gamma_k\omega$ trong mẫu số chính là nguyên nhân khiến $n$ trở thành số phức. Vắng mặt lực cản ($\gamma_k = 0$), $n$ là số thực thuần túy và không có hấp thụ.

### 2. Tách Phần Thực và Phần Ảo

Với một tần số cộng hưởng duy nhất $\omega_0$ và lực cản $\gamma$, đặt $n = n' - in''$ (lưu ý dấu trừ để $n'' > 0$). Để tìm $n'$ và $n''$, nhân tử số và mẫu số của phân thức với liên hợp phức:

$$\frac{1}{\omega_0^2 - \omega^2 - i\gamma\omega} = \frac{(\omega_0^2 - \omega^2) + i\gamma\omega}{(\omega_0^2 - \omega^2)^2 + \gamma^2\omega^2}$$

Đặt $D = (\omega_0^2 - \omega^2)^2 + \gamma^2\omega^2$ là mẫu số thực, và $A = Ne^2 f/(2m\varepsilon_0 n'\omega_0)$ là hằng số nhỏ (gần đúng khi $n \approx 1$), ta có:

$$n' \approx 1 + \frac{Ne^2 f}{2m\varepsilon_0} \cdot \frac{\omega_0^2 - \omega^2}{D}$$

$$n'' \approx \frac{Ne^2 f}{2m\varepsilon_0} \cdot \frac{\gamma\omega}{D}$$

### 3. Ý Nghĩa Vật Lý của Từng Phần

**Phần thực $n'$**: Phản ánh sự dịch pha (phase shift) của sóng. Nó thay đổi dấu qua tần số cộng hưởng - đây là hiện tượng **tán sắc bất thường** (anomalous dispersion) quan sát được trong thực nghiệm.

**Phần ảo $n''$**: Có dạng đường cong Lorentzian theo $\omega$, đạt cực đại tại $\omega = \omega_0$. Đây là đặc trưng của **đường cong hấp thụ** (absorption line profile). Độ rộng bán biên $\Delta\omega = \gamma$ chính là độ rộng của vạch phổ hấp thụ.

### 4. Sóng Điện Từ Trong Môi Trường Hấp Thụ

Xét sóng phẳng truyền theo chiều $+z$ trong vật liệu có chỉ số khúc xạ phức $n = n' - in''$:

$$E(z,t) = E_0 e^{i\omega(t - nz/c)} = E_0 e^{i\omega(t - n'z/c)} e^{-\omega n'' z/c}$$

Ta thấy ngay:
- **Tốc độ pha**: $v_\phi = c/n'$ (như thông thường)
- **Biên độ**: giảm dần theo $e^{-\alpha z/2}$ với **hệ số suy giảm** $\alpha = 2\omega n''/c$

**Định luật Beer-Lambert**: Cường độ $I \propto |E|^2$ giảm theo:

$$I(z) = I_0 e^{-\alpha z}$$

Đây chính là định luật Beer-Lambert quen thuộc trong quang học và hóa phân tích! Hệ số $\alpha$ (đơn vị $\text{m}^{-1}$) phụ thuộc vào tần số và đạt cực đại tại cộng hưởng.

### 5. Liên Hệ với Thiết Bị Đo Lường Chính Xác

Trong các hệ thống đo lường quang học chính xác cao:

**Laser interferometry**: Khi ánh sáng laser truyền qua môi trường khí (như trong interferometer đo dịch chuyển micrometer), cả $n'$ và $n''$ đều ảnh hưởng đến phép đo. Nếu có hấp thụ ($n'' \neq 0$), biên độ tín hiệu giảm, làm giảm **contrast** (độ tương phản) của vân giao thoa. Đây là lý do các interferometer chính xác cao thường được đặt trong buồng chân không hoặc khí trơ.

**Optical coherence tomography (OCT)**: Kỹ thuật chụp ảnh 3D dựa trên giao thoa ánh sáng trắng. Hệ số $n''$ của mô sinh học ở các tần số khác nhau cho phép phân biệt các lớp mô - ứng dụng trong kiểm tra vũ khí quang học và cảm biến.

### 6. Quan Hệ Kramers-Kronig

Một kết quả sâu sắc: $n'(\omega)$ và $n''(\omega)$ **không độc lập** với nhau. Chúng liên hệ qua **quan hệ Kramers-Kronig** (phát sinh từ tính nhân quả - causality - của hệ vật lý):

$$n'(\omega) - 1 = \frac{2}{\pi} \mathcal{P}\int_0^\infty \frac{\omega' n''(\omega')}{\omega'^2 - \omega^2} d\omega'$$

Điều này có nghĩa: nếu bạn biết phổ hấp thụ $n''(\omega)$ ở mọi tần số, bạn có thể tính ra hoàn toàn $n'(\omega)$. Trong thực tế kỹ thuật, đây là cơ sở lý thuyết để đo chỉ số khúc xạ thông qua phép đo hấp thụ.

### 7. Ứng Dụng: Cửa Sổ Minh Bạch và Vùng Hấp Thụ

Một vật liệu thực có nhiều tần số cộng hưởng $\omega_k$. Vật liệu trong suốt (transparent) khi $\omega$ nằm xa mọi $\omega_k$, lúc đó $n'' \approx 0$. Thủy tinh SiO$_2$ trong suốt với ánh sáng khả kiến vì các tần số cộng hưởng của Si-O nằm ở vùng UV (xa hơn) và IR.

Vật liệu quang học cho hệ thống vũ khí (như cửa sổ laser CO$_2$ tại $10.6\,\mu\text{m}$) phải được chọn sao cho $n''$ cực kỳ nhỏ ở bước sóng làm việc để tránh hấp thụ năng lượng và tổn thất công suất.

### Tóm Tắt

| Đại lượng | Ký hiệu | Ý nghĩa vật lý |
|-----------|---------|----------------|
| Phần thực | $n'$ | Tốc độ pha, khúc xạ, tán sắc |
| Phần ảo | $n''$ | Hấp thụ, suy giảm biên độ |
| Hệ số suy giảm | $\alpha = 2\omega n''/c$ | Tốc độ suy giảm cường độ theo khoảng cách |
| Chiều dài hấp thụ | $L = 1/\alpha$ | Khoảng cách để cường độ giảm $e$ lần |

Chỉ số khúc xạ phức là một ví dụ điển hình về cách toán học số phức mô tả đồng thời hai hiện tượng vật lý tách biệt - pha và biên độ - trong một công thức duy nhất gọn gàng.

---
*Exported from Feynman Bot*
