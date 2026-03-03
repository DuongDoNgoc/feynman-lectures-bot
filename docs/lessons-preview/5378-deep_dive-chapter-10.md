---
lesson_id: 5378
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:03.566088+00:00"
content_hash: 85d9a099d83a
chapter_number: 10
chapter_title: Chapter 10
section_number: 4
section_title: 10–3Momentumisconserved!
---
# ## Kiểm Nghiệm Thực Nghiệm Bảo Toàn Động Lượng — Phân tích Chuyên sâu

*Source: Chapter 10 - Chapter 10 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_10.html)*

## Kiểm Nghiệm Thực Nghiệm Bảo Toàn Động Lượng — Phân tích Chuyên sâu

### Thiết kế thực nghiệm: Đo vận tốc trên máng khí

**Thách thức đo lường:** Để kiểm tra $p_i = p_f$, cần đo vận tốc trước và sau va chạm với độ chính xác cao. Phương pháp đơn giản nhất: đặt cổng quang (photogate) tại hai vị trí, đo thời gian xe đi qua — từ đó tính vận tốc.

Giả sử xe rộng $d = 10\,\text{cm}$:

$$v = \frac{d}{\Delta t}$$

Nếu cổng quang có độ phân giải thời gian $1\,\mu\text{s}$, và xe qua trong $\Delta t = 50\,\text{ms}$: sai số vận tốc $\approx \pm 0.04\,\text{mm/s}$, hay $\pm 0.002\%$ — rất chính xác.

---

### Các trường hợp bảo toàn động lượng trên máng khí

**Trường hợp 1: Nổ từ trạng thái đứng yên**

Hai xe $m$ và $m$ đứng yên, nổ tách ra với vận tốc $v_1$ và $v_2$.

Bảo toàn: $0 = mv_1 + m(-v_2) \Rightarrow v_1 = v_2$

Thực nghiệm đo: $v_1 = 0.312\,\text{m/s}$, $v_2 = 0.309\,\text{m/s}$ — sai lệch 1% do ma sát nhỏ còn lại.

**Trường hợp 2: Va chạm không đàn hồi, $m_1 = m_2 = m$**

Xe 1 tới với $v$, xe 2 đứng yên:

$$V = \frac{mv}{2m} = \frac{v}{2}$$

**Trường hợp 3: Va chạm không đàn hồi, $m_1 = m$, $m_2 = 2m$**

$$V = \frac{mv}{3m} = \frac{v}{3}$$

**Trường hợp 4: Nổ, $m_1 = m$, $m_2 = 2m$**

$$0 = mv_1 + 2m(-v_2) \Rightarrow v_1 = 2v_2$$

Xe nhẹ hơn bay nhanh gấp đôi — kiểm tra khối lượng tỉ lệ nghịch với vận tốc.

---

### Phân tích không chắc chắn (Uncertainty Analysis) trong đo lường thực nghiệm

**Nguồn sai số:**
1. Ma sát không khí còn lại: $\approx 0.1\,\text{mN}$ — tạo gia tốc $\sim 0.1\,\text{mm/s}^2$. Trong 1 m máng, gây sai số vận tốc $\sim 0.01\,\%$.
2. Sai số đo thời gian cổng quang: $\pm 1\,\mu\text{s}$ → $\pm 0.002\,\%$ ở $v = 0.3\,\text{m/s}$.
3. Không đồng nhất khối lượng xe: $\pm 0.1\,\text{g}$ trên $200\,\text{g}$ → $\pm 0.05\,\%$.

**Tổng sai số kết hợp** (cộng bình phương): $\sqrt{0.01^2 + 0.002^2 + 0.05^2} \approx 0.051\,\%$

Với độ chính xác này, bảo toàn động lượng được xác nhận ở mức $\pm 0.1\%$ — đủ để kết luận nguyên lý đúng.

---

### Ứng dụng đo lường: Ballistic chronograph trong thử đạn

**Nguyên lý:** Đo vận tốc đạn bằng hai cổng quang cách nhau khoảng cách $L$ đã biết chính xác.

$$v_0 = \frac{L}{\Delta t}$$

Với $L = 1.000\,\text{m}$ (đo bằng thước chuẩn, độ chính xác $\pm 0.05\,\text{mm}$) và $\Delta t$ đo bằng đồng hồ quartz $\pm 1\,\mu\text{s}$:

Tại $v_0 = 900\,\text{m/s}$: $\Delta t \approx 1.11\,\text{ms}$

$$\frac{\delta v}{v} = \sqrt{\left(\frac{\delta L}{L}\right)^2 + \left(\frac{\delta t}{\Delta t}\right)^2} = \sqrt{\left(\frac{0.05}{1000}\right)^2 + \left(\frac{0.001}{1.11}\right)^2} \approx 0.09\,\%$$

Sai số vận tốc tuyệt đối: $\pm 0.81\,\text{m/s}$ — đạt yêu cầu kiểm tra đạn dược quân sự.

---

### Bài tập có lời giải

**Bài toán:** Trên máng khí, xe A ($m_A = 300\,\text{g}$, $v_A = 0.50\,\text{m/s}$ sang phải) va chạm với xe B ($m_B = 200\,\text{g}$, $v_B = 0.30\,\text{m/s}$ sang trái). Sau va chạm chúng dính vào nhau.

(a) Tìm vận tốc sau va chạm $V$.
(b) Tính phần trăm động năng bị mất.

**Lời giải:**

(a) Chọn chiều dương là sang phải.

$$V = \frac{m_A v_A + m_B v_B}{m_A + m_B} = \frac{0.3(0.50) + 0.2(-0.30)}{0.3 + 0.2} = \frac{0.15 - 0.06}{0.5} = \frac{0.09}{0.5} = 0.18\,\text{m/s}$$

(sang phải)

(b) Động năng ban đầu:

$$KE_i = \frac{1}{2}(0.3)(0.50)^2 + \frac{1}{2}(0.2)(0.30)^2 = 0.0375 + 0.009 = 0.0465\,\text{J}$$

Động năng sau:

$$KE_f = \frac{1}{2}(0.5)(0.18)^2 = 0.0081\,\text{J}$$

Phần trăm mất: $\frac{0.0465 - 0.0081}{0.0465} \times 100\% = 82.6\%$

---

**Điểm mấu chốt:**

- Máng khí tạo điều kiện thực nghiệm lý tưởng (ma sát $\approx 0$) để kiểm tra bảo toàn $p$.
- Phân tích không chắc chắn là bắt buộc khi báo cáo kết quả thực nghiệm — mọi số đo đều có sai số.
- Ballistic chronograph là ứng dụng đo lường trực tiếp: $v = L/\Delta t$, đạt $\pm 0.1\%$ với thiết bị đơn giản.
- Va chạm không đàn hồi mất phần lớn động năng (biến thành nhiệt, biến dạng) — nhưng động lượng luôn được bảo toàn.


---
*Exported from Feynman Bot*
