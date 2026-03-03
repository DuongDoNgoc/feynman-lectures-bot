---
lesson_id: 5381
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:03.619452+00:00"
content_hash: f6d029d38a53
chapter_number: 10
chapter_title: Chapter 10
section_number: 5
section_title: 10–4Momentum and energy
---
# ## Va Chạm Đàn Hồi — Phân tích Chuyên sâu

*Source: Chapter 10 - Chapter 10 (Section 5) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_10.html)*

## Va Chạm Đàn Hồi — Phân tích Chuyên sâu

### Thiết lập phương trình và giải hệ

Xét va chạm đàn hồi 1D: vật 1 ($m_1$, $v_1$) và vật 2 ($m_2$, $v_2$), tìm $v_1'$ và $v_2'$ sau va chạm.

**Hai phương trình:**

Bảo toàn động lượng:
$$m_1 v_1 + m_2 v_2 = m_1 v_1' + m_2 v_2' \quad (1)$$

Bảo toàn động năng:
$$\frac{1}{2}m_1 v_1^2 + \frac{1}{2}m_2 v_2^2 = \frac{1}{2}m_1 v_1'^2 + \frac{1}{2}m_2 v_2'^2 \quad (2)$$

**Biến đổi phương trình (2):**

$$m_1(v_1^2 - v_1'^2) = m_2(v_2'^2 - v_2^2)$$
$$m_1(v_1 - v_1')(v_1 + v_1') = m_2(v_2' - v_2)(v_2' + v_2) \quad (2')$$

Từ (1): $m_1(v_1 - v_1') = m_2(v_2' - v_2) \quad (1')$

Chia (2') cho (1'):

$$v_1 + v_1' = v_2' + v_2$$

$$v_1 - v_2 = v_2' - v_1' = -(v_1' - v_2') \quad (3)$$

Phương trình (3) có ý nghĩa vật lý đẹp: **tốc độ tiếp cận trước va chạm bằng tốc độ phân ly sau va chạm** (hệ số phục hồi $e = 1$ cho va chạm hoàn toàn đàn hồi).

Giải hệ (1) và (3):

$$v_1' = \frac{m_1 - m_2}{m_1 + m_2}v_1 + \frac{2m_2}{m_1 + m_2}v_2$$

$$v_2' = \frac{2m_1}{m_1 + m_2}v_1 + \frac{m_2 - m_1}{m_1 + m_2}v_2$$

---

### Hệ số phục hồi đàn hồi (Coefficient of Restitution)

Trong thực tế, va chạm không hoàn toàn đàn hồi. Hệ số phục hồi:

$$e = \frac{v_2' - v_1'}{v_1 - v_2} \in [0, 1]$$

- $e = 1$: hoàn toàn đàn hồi (lý tưởng)
- $e = 0$: hoàn toàn không đàn hồi (dính vào nhau)
- Thép trên thép: $e \approx 0.9$–$0.95$
- Cao su trên thép: $e \approx 0.7$–$0.8$
- Đạn chì trên mục tiêu mềm: $e \approx 0.05$–$0.2$

Nghiệm tổng quát (kết hợp bảo toàn $p$ và hệ số $e$):

$$v_1' = \frac{m_1 v_1 + m_2 v_2 - m_2 e(v_1 - v_2)}{m_1 + m_2}$$
$$v_2' = \frac{m_1 v_1 + m_2 v_2 + m_1 e(v_1 - v_2)}{m_1 + m_2}$$

---

### Ứng dụng: Kiểm tra vật liệu đầu đạn và áo giáp

**Bài toán:** Đạn xuyên giáp ($m_b = 10\,\text{g}$, $v_b = 900\,\text{m/s}$) va chạm với tấm giáp composite dày ($M = 5\,\text{kg}$, đứng yên). Hệ số phục hồi $e = 0.05$ (gần không đàn hồi).

**Tính vận tốc sau:**

$$V_{armor} = \frac{m_b v_b + M \times 0 + m_b e(v_b - 0)}{m_b + M} = \frac{m_b v_b(1 + e)}{m_b + M}$$

$$V_{armor} = \frac{0.01 \times 900 \times 1.05}{0.01 + 5} = \frac{9.45}{5.01} = 1.89\,\text{m/s}$$

$$v_b' = \frac{m_b v_b - M e(v_b)}{m_b + M} = \frac{0.01 \times 900 - 5 \times 0.05 \times 900}{5.01} \approx \frac{9 - 225}{5.01} = -43\,\text{m/s}$$

Vận tốc âm: đạn bị bật ngược. Điều này cho thấy giáp đã hấp thụ đủ năng lượng để đẩy đạn trở lui — tiêu chí đánh giá hiệu quả áo giáp.

**Năng lượng hấp thụ bởi giáp:**

$$\Delta KE = \frac{1}{2}m_b v_b^2 - \frac{1}{2}m_b v_b'^2 - \frac{1}{2}M V_{armor}^2$$

$$= \frac{1}{2}(0.01)(900)^2 - \frac{1}{2}(0.01)(43)^2 - \frac{1}{2}(5)(1.89)^2$$

$$= 4050 - 9.25 - 8.93 = 4031.8\,\text{J}$$

Giáp hấp thụ 99.5% động năng đạn — hiệu quả cao.

---

### Ứng dụng đo lường: Xác định $e$ bằng thí nghiệm nảy bóng

Thả vật từ độ cao $H$, đo độ cao nảy lại $h$:

$$e = \sqrt{\frac{h}{H}}$$

**Ví dụ:** Bi thép nảy từ $H = 1.000\,\text{m}$, nảy lại $h = 0.812\,\text{m}$:

$$e = \sqrt{0.812} = 0.901$$

Phương pháp này dùng trong kiểm tra chất lượng vật liệu và thiết kế giảm chấn.

---

### Bài tập có lời giải

**Bài toán:** Bi cầu A ($m_1 = 0.3\,\text{kg}$, $v_1 = 2.0\,\text{m/s}$) va chạm đàn hồi với bi cầu B ($m_2 = 0.5\,\text{kg}$, $v_2 = -0.5\,\text{m/s}$, đang đến ngược chiều).

(a) Tính $v_1'$ và $v_2'$.
(b) Kiểm tra bảo toàn động năng.

**Lời giải:**

(a) $\mu_1 = m_1/(m_1+m_2) = 0.3/0.8 = 0.375$, $\mu_2 = 0.5/0.8 = 0.625$

$$v_1' = \frac{m_1-m_2}{m_1+m_2}v_1 + \frac{2m_2}{m_1+m_2}v_2 = \frac{-0.2}{0.8}(2.0) + \frac{1.0}{0.8}(-0.5) = -0.5 - 0.625 = -1.125\,\text{m/s}$$

$$v_2' = \frac{2m_1}{m_1+m_2}v_1 + \frac{m_2-m_1}{m_1+m_2}v_2 = \frac{0.6}{0.8}(2.0) + \frac{0.2}{0.8}(-0.5) = 1.5 - 0.125 = 1.375\,\text{m/s}$$

(b) $KE_i = \frac{1}{2}(0.3)(2.0)^2 + \frac{1}{2}(0.5)(0.5)^2 = 0.600 + 0.0625 = 0.6625\,\text{J}$

$KE_f = \frac{1}{2}(0.3)(1.125)^2 + \frac{1}{2}(0.5)(1.375)^2 = 0.1898 + 0.4727 = 0.6625\,\text{J}$ ✓

---

**Điểm mấu chốt:**

- Va chạm đàn hồi: hai ẩn số ($v_1'$, $v_2'$), hai phương trình (bảo toàn $p$ và $KE$) → hệ giải được.
- Hệ số phục hồi $e = 1$ (đàn hồi lý tưởng) đến $e = 0$ (dính hoàn toàn).
- Điều kiện $e$: tốc độ phân ly / tốc độ tiếp cận — đơn giản để đo thực nghiệm.
- Ứng dụng quân sự: $e$ của đạn-giáp quyết định xuyên giáp hay bật — thông số thiết kế quan trọng.


---
*Exported from Feynman Bot*
