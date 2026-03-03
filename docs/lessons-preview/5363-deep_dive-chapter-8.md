---
lesson_id: 5363
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:00.429497+00:00"
content_hash: 3293d57637f9
chapter_number: 8
chapter_title: Chapter 8
section_number: 1
section_title: 8Motion
---
# ## Chuyển Động — Phân tích Chuyên sâu

*Source: Chapter 8 - Chapter 8 (Section 1) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_08.html)*

## Chuyển Động — Phân tích Chuyên sâu

### Từ bảng số đến đạo hàm: Con đường của Feynman

Feynman bắt đầu Chương 8 không phải bằng công thức mà bằng một bảng dữ liệu thực tế: vị trí của một chiếc xe theo từng phút. Cách tiếp cận này phản ánh tư duy kỹ thuật — đo trước, rồi mới mô hình hóa.

**Bảng 8-1 (tóm tắt):**

| $t$ (phút) | $s$ (feet) |
|---|---|
| 0 | 0 |
| 1 | 1200 |
| 2 | 4000 |
| 3 | 4900 |
| 4 | 5100 |
| 5 | 6000 |
| ... | ... |
| 9 | 10200 |

Chỉ nhìn bảng, ta thấy ngay: từ phút 2 đến 3, xe tăng ít (đèn đỏ); từ phút 8 đến 9 xe chậm lại (bị cảnh sát). Nhưng "nhanh bao nhiêu" tại một thời điểm cụ thể — đó là câu hỏi đòi hỏi giới hạn.

---

### Xây dựng khái niệm vận tốc tức thời

**Vận tốc trung bình** trong khoảng $[t, t+\Delta t]$:

$$ar{v} = rac{s(t+\Delta t) - s(t)}{\Delta t}$$

Khi $\Delta t 	o 0$, ta thu được **vận tốc tức thời**:

$$v(t) = \lim_{\Delta t 	o 0} rac{s(t+\Delta t) - s(t)}{\Delta t} = rac{ds}{dt}$$

Đây là định nghĩa đạo hàm — Feynman gọi $\Delta t$ là "một mẩu thêm của $t$", nhấn mạnh rằng $\Delta t$ không phải tích của $\Delta$ và $t$.

**Tương tự**, gia tốc:

$$a(t) = rac{dv}{dt} = rac{d^2s}{dt^2}$$

---

### Ví dụ thực tế: Encoder tuyến tính trong máy đo tọa độ CMM

Giả sử đầu đo của máy CMM chuyển động theo phương $x$ với hàm vị trí:

$$s(t) = A \sin(\omega t)$$

trong đó $A = 50\,	ext{mm}$, $\omega = 2\pi \cdot 0.5\,	ext{rad/s}$ (chu kỳ 2 giây).

**Vận tốc:**
$$v(t) = rac{ds}{dt} = A\omega \cos(\omega t) = 50 	imes \pi 	imes \cos(\pi t) pprox 157\cos(\pi t)\,	ext{mm/s}$$

**Gia tốc:**
$$a(t) = rac{dv}{dt} = -A\omega^2 \sin(\omega t) = -50\pi^2 \sin(\pi t) pprox -493\sin(\pi t)\,	ext{mm/s}^2$$

Khi $t = 0$: vị trí = 0, vận tốc = 157 mm/s (cực đại), gia tốc = 0.
Khi $t = 0.5\,	ext{s}$: vị trí = 50 mm (biên độ), vận tốc = 0, gia tốc = −493 mm/s² (cực đại về độ lớn).

Điều này quan trọng trong thiết kế: gia tốc cực đại quyết định lực quán tính tác động lên đầu đo — ảnh hưởng trực tiếp đến độ chính xác đo ở cấp micromet.

---

### Tính số (phương pháp Euler thuận)

Khi không có dạng giải tích của $s(t)$, ta dùng phương pháp số. Feynman trình bày ý tưởng này trực tiếp:

Biết $s(t)$ và $v(t)$ tại thời điểm $t$, ta ước lượng:

$$v(t + \epsilon) pprox v(t) + a(t) \cdot \epsilon$$
$$s(t + \epsilon) pprox s(t) + v(t) \cdot \epsilon$$

Đây là **phương pháp Euler** — nền tảng của mọi bộ tích phân số trong hệ điều khiển thời gian thực.

**Ví dụ số:** Vật bắt đầu từ $s_0 = 0$, $v_0 = 10\,	ext{mm/s}$, gia tốc hằng $a = -2\,	ext{mm/s}^2$, bước thời gian $\epsilon = 0.1\,	ext{s}$:

| Bước | $t$ (s) | $s$ (mm) | $v$ (mm/s) |
|---|---|---|---|
| 0 | 0.0 | 0.00 | 10.00 |
| 1 | 0.1 | 1.00 | 9.80 |
| 2 | 0.2 | 1.98 | 9.60 |
| 3 | 0.3 | 2.94 | 9.40 |

Sai số tích lũy theo thời gian — đó là lý do tại sao các bộ điều khiển hiện đại dùng phương pháp Runge-Kutta bậc 4 thay vì Euler thuần túy.

---

### Bài tập có lời giải

**Bài toán:** Đầu đo laser trong hệ đo lường quân sự có vị trí: $s(t) = 3t^2 - 12t + 9$ (đơn vị: mm, giây). Tìm:
(a) Vận tốc tại $t = 2\,	ext{s}$
(b) Thời điểm vật đứng yên
(c) Gia tốc (hằng số?)

**Lời giải:**

(a) $v(t) = ds/dt = 6t - 12$. Tại $t = 2$: $v = 6(2) - 12 = 0\,	ext{mm/s}$

(b) Vật đứng yên khi $v = 0$: $6t - 12 = 0 \Rightarrow t = 2\,	ext{s}$. Đây là điểm quay đầu.

(c) $a(t) = dv/dt = 6\,	ext{mm/s}^2$ — gia tốc không đổi, chuyển động thẳng biến đổi đều.

---

**Điểm mấu chốt:**

- Vận tốc tức thời = giới hạn của tỉ số $\Delta s / \Delta t$ khi $\Delta t 	o 0$.
- Gia tốc = đạo hàm bậc 2 của vị trí.
- Phương pháp Euler số hóa quá trình tích phân liên tục thành các bước rời rạc — nền tảng của điều khiển số thời gian thực.
- Trong hệ đo chính xác, gia tốc quyết định lực quán tính và do đó ảnh hưởng đến sai số đo.


---
*Exported from Feynman Bot*
