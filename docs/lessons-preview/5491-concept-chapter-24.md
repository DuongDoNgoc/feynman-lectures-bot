---
lesson_id: 5491
lesson_type: concept
approval_status: pending
exported_at: "2026-03-02T15:10:30.955148+00:00"
content_hash: e3d8d6361475
chapter_number: 24
chapter_title: Chapter 24
section_number: 2
section_title: 24–1The energy of an oscillator
---
# ## Bài Giảng: Quá Độ (Transients) và Năng Lượng Trong Dao Động — Khái Niệm Cơ Bả

*Source: Chapter 24 - Chapter 24 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_24.html)*

## Bài Giảng: Quá Độ (Transients) và Năng Lượng Trong Dao Động — Khái Niệm Cơ Bản

### 1. Transient Là Gì?

Khi bạn bật một mạch điện hoặc tác động lực đột ngột lên một hệ cơ học, hệ không ngay lập tức đạt trạng thái ổn định (steady state). Có một giai đoạn "chạy vào" (run-in) trong đó dao động tự nhiên (natural oscillation) và dao động cưỡng bức (forced oscillation) cùng tồn tại và chồng chất lên nhau. Giai đoạn này gọi là **transient** — quá độ.

Về mặt toán học, nghiệm tổng quát của phương trình dao động cưỡng bức là:
$$x(t) = x_{transient}(t) + x_{steady}(t)$$

Phần *transient* là nghiệm thuần nhất (homogeneous solution) của phương trình vi phân — dao động tự nhiên tắt dần. Phần *steady-state* là nghiệm riêng (particular solution) — dao động cưỡng bức bền vững.

---

### 2. Vấn Đề Tính Năng Lượng Bằng Số Phức

Phương pháp số phức rất hiệu quả để tính biên độ và pha của dao động cưỡng bức. Nhưng có một cạm bẫy quan trọng khi tính **năng lượng**: *không thể dùng trực tiếp số phức để tính bình phương!*

Xét đại lượng vật lý $A(t)$ — có thể là vận tốc hoặc dòng điện. Ta viết nó dưới dạng số phức:
$$A = \hat{A} e^{i\omega t}$$

Nhưng giá trị vật lý thực chỉ là phần thực:
$$A_{real}(t) = \text{Re}[\hat{A} e^{i\omega t}] = A_0\cos(\omega t + \Delta)$$

Bình phương vật lý là:
$$A_{real}^2 = A_0^2\cos^2(\omega t + \Delta)$$

Điều này **không bằng** $\text{Re}[(\hat{A} e^{i\omega t})^2] = A_0^2\cos(2\omega t + 2\Delta)$ (là hàm dao động khác tần số!).

Vì vậy, khi cần tính năng lượng, *phải quay về dạng thực* trước khi bình phương.

---

### 3. Bình Phương Trung Bình — Giá Trị RMS

Trong hầu hết ứng dụng kỹ thuật, ta không cần năng lượng tức thời mà cần *năng lượng trung bình* theo thời gian. Vì $A_{real}^2 = A_0^2\cos^2(\omega t + \Delta)$ dao động từ $0$ đến $A_0^2$, giá trị trung bình:
$$\langle A_{real}^2 \rangle = \frac{A_0^2}{2}$$

Đây là nền tảng của khái niệm **RMS (Root Mean Square)** — giá trị hiệu dụng:
$$A_{RMS} = \sqrt{\langle A^2 \rangle} = \frac{A_0}{\sqrt{2}}$$

Trong mạch điện xoay chiều (AC), điện áp $220\,\text{V}$ ghi trên ổ cắm chính là giá trị RMS, ứng với biên độ đỉnh $V_0 = 220\sqrt{2} \approx 311\,\text{V}$.

**Định lý quan trọng:** Nếu $\hat{A}$ là biên độ phức, thì giá trị trung bình bình phương là:
$$\langle A_{real}^2 \rangle = \frac{1}{2}|\hat{A}|^2 = \frac{1}{2}\hat{A}^*\hat{A}$$

Công thức này cho phép tính năng lượng trung bình *từ biên độ phức* mà không cần quay về dạng thực — nhưng phải dùng đúng hệ số $1/2$.

---

### 4. Năng Lượng Trong Dao Động Cưỡng Bức

Áp dụng cho hệ cơ học, động năng trung bình:
$$\langle E_k \rangle = \frac{1}{2}m\langle v^2 \rangle = \frac{1}{4}m|\hat{v}|^2 = \frac{1}{4}m\omega^2|\hat{x}|^2$$

Tại tần số cộng hưởng $\omega = \omega_0$, $|\hat{x}|$ đạt cực đại nên $\langle E_k \rangle$ cũng đạt cực đại.

Năng lượng tiêu tán trung bình trên lực cản:
$$\langle P \rangle = \frac{1}{2}m\gamma|\hat{v}|^2 = \frac{1}{2}m\gamma\omega^2|\hat{x}|^2$$

Tỉ lệ năng lượng tiêu tán và năng lượng tích trữ liên hệ với hệ số Q:
$$Q = \frac{\omega_0 \langle U \rangle}{\langle P \rangle}$$

---

### 5. Từ Dao Động Bền Vững Đến Quá Độ

Một hệ quan trọng là: khi lực kích thích bị tắt đột ngột, hệ không dừng ngay mà tiếp tục dao động với tần số $\omega_0$ và biên độ giảm dần theo hàm mũ:
$$x_{transient}(t) = B e^{-(\gamma/2)t}\cos(\omega_1 t + \phi_0)$$

Trong đó $\omega_1 = \sqrt{\omega_0^2 - (\gamma/2)^2} < \omega_0$ là tần số dao động tắt dần thực tế. Với hệ có Q cao ($Q \gg 1$), $\omega_1 \approx \omega_0$.

---

### 6. Ý Nghĩa Kỹ Thuật

Trong hệ thống tự động hóa và điều khiển chính xác:
- **Step response** (đáp ứng bước nhảy) chứa thành phần transient gây dao động quá độ (overshoot, ringing). Hệ Q cao có transient kéo dài hơn.
- **Settling time** (thời gian ổn định): thời gian để transient tắt xuống dưới ngưỡng cho phép $\propto 1/\gamma = Q/\omega_0$.
- Trong đo lường chính xác, phải đợi transient tắt hẳn trước khi lấy mẫu để tránh sai số.

---

### 7. Tóm Tắt

Transient là giai đoạn quá độ khi dao động tự nhiên và cưỡng bức cùng tồn tại. Khi tính năng lượng từ số phức, phải dùng $\langle A^2 \rangle = |\hat{A}|^2/2$ — không được bình phương trực tiếp số phức. Giá trị RMS là $A_0/\sqrt{2}$, là chuẩn đo lường năng lượng trong AC. Hệ số Q xác định thời gian tắt dần của transient và ảnh hưởng trực tiếp đến settling time trong điều khiển.

---
*Exported from Feynman Bot*
