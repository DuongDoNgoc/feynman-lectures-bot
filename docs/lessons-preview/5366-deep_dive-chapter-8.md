---
lesson_id: 5366
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:00.509317+00:00"
content_hash: ff443e423d1d
chapter_number: 8
chapter_title: Chapter 8
section_number: 4
section_title: 8–3Speed as a derivative
---
# ## Ký Hiệu Vi Tích Phân và Đạo Hàm — Phân tích Chuyên sâu

*Source: Chapter 8 - Chapter 8 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_08.html)*

## Ký Hiệu Vi Tích Phân và Đạo Hàm — Phân tích Chuyên sâu

### Xây dựng định nghĩa đạo hàm từ đầu

Feynman dẫn dắt người đọc qua quá trình phát minh ra ký hiệu vi phân bằng cách bắt đầu từ bài toán cụ thể: tính vận tốc tức thời từ hàm vị trí $s(t)$.

**Bước 1: Vận tốc trung bình**

Giữa hai thời điểm $t$ và $t + \Delta t$:

$$\bar{v} = \frac{s(t + \Delta t) - s(t)}{\Delta t}$$

**Bước 2: Thu hẹp khoảng**

Khi $\Delta t$ ngày càng nhỏ, $\bar{v}$ tiến gần đến một giá trị xác định — đó là **đạo hàm**:

$$v(t) = \lim_{\Delta t \to 0} \frac{s(t + \Delta t) - s(t)}{\Delta t} \equiv \frac{ds}{dt}$$

**Bước 3: Ký hiệu**

Feynman giải thích: ký hiệu $ds/dt$ trông như một phân số nhưng thực ra là **ký hiệu tắt của giới hạn**. Ta viết $ds$ và $dt$ (thay vì $\Delta s$ và $\Delta t$) để nhắc nhở rằng ta đã lấy giới hạn khi $\Delta t \to 0$.

---

### Ví dụ tính đạo hàm từ định nghĩa: Trường hợp $s = t^2$

$$\frac{ds}{dt} = \lim_{\Delta t \to 0} \frac{(t+\Delta t)^2 - t^2}{\Delta t}$$

Khai triển tử số:

$$(t+\Delta t)^2 - t^2 = t^2 + 2t\Delta t + (\Delta t)^2 - t^2 = 2t\Delta t + (\Delta t)^2$$

Chia cho $\Delta t$:

$$\frac{2t\Delta t + (\Delta t)^2}{\Delta t} = 2t + \Delta t$$

Khi $\Delta t \to 0$:

$$\frac{d(t^2)}{dt} = 2t$$

Đây là cơ chế tổng quát cho quy tắc lũy thừa $d(t^n)/dt = nt^{n-1}$.

---

### Ứng dụng trong đo lường chính xác quân sự: Radar theo dõi mục tiêu

**Bài toán:** Hệ thống radar theo dõi đạn đạo đo khoảng cách $r(t)$ mỗi $T_s = 5\,\text{ms}$. Từ dữ liệu thô, cần ước lượng vận tốc $v$ và gia tốc $a$ để dự đoán vị trí mục tiêu 100 ms tới.

**Phương pháp sai phân:**

Vận tốc (sai phân trung tâm, sai số $O(\Delta t^2)$):

$$v(t_k) \approx \frac{r(t_{k+1}) - r(t_{k-1})}{2T_s}$$

Gia tốc (sai phân bậc 2):

$$a(t_k) \approx \frac{r(t_{k+1}) - 2r(t_k) + r(t_{k-1})}{T_s^2}$$

**Vấn đề khuếch đại nhiễu:**

Nếu nhiễu đo của radar là $\sigma_r = 1\,\text{m}$ (rms), thì:

$$\sigma_v = \frac{\sqrt{2}\,\sigma_r}{2T_s} = \frac{\sqrt{2} \times 1}{2 \times 0.005} \approx 141\,\text{m/s}$$

$$\sigma_a = \frac{\sqrt{6}\,\sigma_r}{T_s^2} = \frac{\sqrt{6} \times 1}{(0.005)^2} \approx 97980\,\text{m/s}^2$$

Gia tốc nhiễu gần $10^4\,\text{m/s}^2$ — không thể dùng trực tiếp! Đây là lý do tại sao bộ lọc Kalman (tích hợp mô hình động học + đo lường) cần thiết: nó dùng $d/dt$ từ mô hình vật lý thay vì sai phân số thô.

---

### Bài tập có lời giải

**Bài toán:** Sensor gia tốc kế trong hệ dẫn đường quán tính đo gia tốc $a(t) = 6t - 4$ (m/s², $t$ tính bằng giây). Điều kiện ban đầu: $v(0) = 2\,\text{m/s}$, $x(0) = 0$.

(a) Tìm $v(t)$ và $x(t)$ bằng tích phân.
(b) Tính khoảng cách đi được trong 3 giây đầu.

**Lời giải:**

(a) Tích phân gia tốc:

$$v(t) = \int a(t)\,dt = \int (6t - 4)\,dt = 3t^2 - 4t + C$$

Áp dụng $v(0) = 2$: $C = 2$, nên $v(t) = 3t^2 - 4t + 2$.

Tích phân vận tốc:

$$x(t) = \int v(t)\,dt = \int (3t^2 - 4t + 2)\,dt = t^3 - 2t^2 + 2t + D$$

Áp dụng $x(0) = 0$: $D = 0$, nên $x(t) = t^3 - 2t^2 + 2t$.

(b) $x(3) = 27 - 18 + 6 = 15\,\text{m}$.

Kiểm tra: $v(3) = 27 - 12 + 2 = 17\,\text{m/s}$ (dương — vật không đổi chiều trong $[0,3]$, nên khoảng cách = độ dịch chuyển = 15 m).

---

**Điểm mấu chốt:**

- Đạo hàm là giới hạn của tỉ số sai phân khi bước thời gian tiến về 0 — không phải "chia cho số vô cùng nhỏ".
- Ký hiệu $\Delta$ (hữu hạn) vs $d$ (giới hạn) phản ánh hai cấp độ tính toán khác nhau.
- Sai phân số khuếch đại nhiễu theo $1/\Delta t$ — điều này giới hạn tần số lấy mẫu hữu ích và là lý do cần bộ lọc.
- Tích phân = phép ngược của vi phân; điều kiện đầu xác định hằng số tích phân.


---
*Exported from Feynman Bot*
