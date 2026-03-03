---
lesson_id: 5371
lesson_type: concept
approval_status: approved
exported_at: "2026-03-03T15:33:00.673102+00:00"
content_hash: 8763a43291ac
chapter_number: 9
chapter_title: Chapter 9
section_number: 6
section_title: 9–5Meaning of the dynamical equations
---
# ## Giải Phương Trình Chuyển Động Từng Bước — Tích Phân Số

*Source: Chapter 9 - Chapter 9 (Section 6) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_09.html)*

## Giải Phương Trình Chuyển Động Từng Bước — Tích Phân Số

Bạn viết firmware cho bộ điều khiển motor: mỗi 1 ms, bạn đọc encoder, tính sai số, cập nhật tín hiệu PWM. Đây chính xác là tư duy mà Feynman dạy trong chương này: **giải phương trình vật lý từng bước nhỏ theo thời gian**, thay vì tìm nghiệm giải tích.

---

### Ý tưởng cốt lõi: Dự đoán trạng thái tiếp theo

Feynman lấy ví dụ kinh điển: vật chịu lực hồi phục $F = -kx$ (dao động điều hòa). Phương trình Newton:

$$m\ddot{x} = -kx \quad \Rightarrow \quad a(t) = -\frac{k}{m}x(t)$$

Ta không cần giải tích phân để tìm $\sin$ và $\cos$ — ta chỉ cần biết: **nếu biết $x$ và $v$ lúc $t$, thì $x$ và $v$ lúc $t + \epsilon$ là gì?**

$$v(t+\epsilon) \approx v(t) + a(t)\cdot\epsilon$$
$$x(t+\epsilon) \approx x(t) + v(t)\cdot\epsilon$$

Lặp đi lặp lại — ta có toàn bộ quỹ đạo.

---

### Điều kiện đầu là chìa khóa

Bài toán dao động: $k/m = 1$, bắt đầu từ $x(0) = 1$, $v(0) = 0$.

Feynman chỉ ra: chọn $\epsilon$ đủ nhỏ thì nghiệm số gần đúng với $x(t) = \cos(t)$ — nhưng không bao giờ **bằng** (do sai số tích lũy). Giảm $\epsilon$ thì độ chính xác tăng, nhưng tốn thêm tính toán.

---

### Phép so sánh: Bộ lọc số IIR trong xử lý tín hiệu

Bộ lọc IIR (Infinite Impulse Response) có dạng:

$$y[n] = b_0 x[n] + b_1 x[n-1] - a_1 y[n-1]$$

Đây chính là dạng số hóa của phương trình vi phân bậc 1. Khi thiết kế bộ lọc Butterworth cho hệ đo, bạn thực chất đang chuyển phương trình vi phân liên tục (mô tả đặc tính lọc) sang phương trình sai phân rời rạc — đúng tinh thần Feynman mô tả.

---

### Tại sao cần điều này nếu đã có nghiệm giải tích?

Trong thực tế, hầu hết bài toán kỹ thuật **không** có nghiệm giải tích:
- Robot 6 bậc tự do với ma sát, backlash
- Đạn đạo trong khí quyển (lực cản phi tuyến)
- Hệ đo rung với nhiều mode tần số

Phương pháp số là công cụ **phổ quát** — nó hoạt động cho mọi dạng $F = ma$.

---

**Điểm mấu chốt:**

- Phương trình Newton $F = ma$ có thể giải số bằng cách tịnh tiến từng bước nhỏ $\epsilon$ theo thời gian.
- Công thức Euler: $v_{n+1} = v_n + a_n \epsilon$, $x_{n+1} = x_n + v_n \epsilon$.
- Điều kiện đầu ($x_0$, $v_0$) hoàn toàn xác định nghiệm.
- Bước thời gian nhỏ hơn → chính xác hơn nhưng tốn tài nguyên tính toán hơn.
- Mọi bộ mô phỏng cơ học, bộ điều khiển số, và bộ lọc IIR đều dựa trên nguyên lý này.


---
*Exported from Feynman Bot*
