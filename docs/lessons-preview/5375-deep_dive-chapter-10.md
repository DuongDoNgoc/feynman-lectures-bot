---
lesson_id: 5375
lesson_type: deep_dive
approval_status: pending
exported_at: "2026-02-28T14:09:00.087565+00:00"
content_hash: 5d4341bd20ef
chapter_number: 10
chapter_title: Chapter 10
section_number: 1
section_title: 10Conservation of Momentum
---
# ## Bảo Toàn Động Lượng — Phân tích Chuyên sâu

*Source: Chapter 10 - Chapter 10 (Section 1) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_10.html)*

## Bảo Toàn Động Lượng — Phân tích Chuyên sâu

### Chứng minh từ Định luật Newton III

**Xét hệ hai vật** với nội lực $\mathbf{F}_{12}$ (lực của vật 2 lên vật 1) và $\mathbf{F}_{21}$ (lực của vật 1 lên vật 2).

Định luật Newton II cho từng vật:

$$m_1 \frac{d\mathbf{v}_1}{dt} = \mathbf{F}_{12} + \mathbf{F}_{ext,1}$$

$$m_2 \frac{d\mathbf{v}_2}{dt} = \mathbf{F}_{21} + \mathbf{F}_{ext,2}$$

Cộng hai phương trình:

$$\frac{d}{dt}(m_1\mathbf{v}_1 + m_2\mathbf{v}_2) = \underbrace{(\mathbf{F}_{12} + \mathbf{F}_{21})}_{= 0 \text{ (Newton III)}} + \mathbf{F}_{ext,1} + \mathbf{F}_{ext,2}$$

Nếu không có ngoại lực:

$$\frac{d\mathbf{P}_{total}}{dt} = 0 \quad \Rightarrow \quad \mathbf{P}_{total} = \text{const}$$

---

### Loại va chạm: Hoàn toàn không đàn hồi vs. Đàn hồi

**Va chạm hoàn toàn không đàn hồi** (hai vật dính vào nhau):

$$m_1 v_1 + m_2 v_2 = (m_1 + m_2)V$$

$$V = \frac{m_1 v_1 + m_2 v_2}{m_1 + m_2}$$

Động năng bị mất: $\Delta KE = \frac{1}{2}m_1v_1^2 + \frac{1}{2}m_2v_2^2 - \frac{1}{2}(m_1+m_2)V^2 > 0$.

**Va chạm đàn hồi** (bảo toàn cả động năng):

$$m_1 v_1 + m_2 v_2 = m_1 v_1' + m_2 v_2'$$
$$\frac{1}{2}m_1 v_1^2 + \frac{1}{2}m_2 v_2^2 = \frac{1}{2}m_1 v_1'^2 + \frac{1}{2}m_2 v_2'^2$$

Nghiệm đại số:

$$v_1' = \frac{m_1 - m_2}{m_1 + m_2}v_1 + \frac{2m_2}{m_1 + m_2}v_2$$

$$v_2' = \frac{2m_1}{m_1 + m_2}v_1 + \frac{m_2 - m_1}{m_1 + m_2}v_2$$

---

### Ứng dụng quân sự: Phân tích giật súng và thiết kế bộ giảm giật

**Bài toán:** Súng máy hạng nhẹ bắn liên thanh ở tốc độ 600 phát/phút. Mỗi viên đạn: $m_b = 8\,\text{g}$, $v_0 = 870\,\text{m/s}$. Khối lượng súng + khóa nòng: $M = 4\,\text{kg}$.

**Phân tích mỗi phát:**

Động lượng đạn: $p_b = 0.008 \times 870 = 6.96\,\text{kg·m/s}$

Vận tốc giật của khóa nòng (trước khi lò xo hãm):

$$V_{bolt} = \frac{p_b}{M_{bolt}} = \frac{6.96}{0.4} = 17.4\,\text{m/s}$$

(Giả sử khối lượng bộ phận chuyển động $M_{bolt} = 0.4\,\text{kg}$.)

**Bộ giảm giật lò xo:**

Năng lượng cần hấp thụ mỗi chu kỳ:

$$E = \frac{1}{2}M_{bolt}V_{bolt}^2 = \frac{1}{2}(0.4)(17.4)^2 = 60.5\,\text{J}$$

Với hành trình $d = 80\,\text{mm}$, lực lò xo trung bình:

$$F_{spring,avg} = E/d = 60.5/0.08 = 756\,\text{N}$$

Tần số bắn 600 phát/phút = 10 Hz → chu kỳ $T = 100\,\text{ms}$. Lò xo cần hoàn thành một chu kỳ nén-giãn trong 100 ms → tần số tự nhiên bộ phận chuyển động phải $> 10\,\text{Hz}$, thực tế thiết kế $f_n \approx 30\text{–}50\,\text{Hz}$.

---

### Ứng dụng đo lường: Va chạm trong cân bằng con lắc đạn

**Nguyên lý cân bằng con lắc đạn** (ballistic pendulum): đo vận tốc đạn thông qua bảo toàn động lượng + năng lượng.

Đạn ($m$, $v_0$) bắn vào con lắc ($M$, đứng yên), dính vào con lắc:

$$mv_0 = (m + M)V \quad \Rightarrow \quad V = \frac{mv_0}{m+M}$$

Con lắc nâng lên độ cao $h$:

$$\frac{1}{2}(m+M)V^2 = (m+M)gh \quad \Rightarrow \quad V = \sqrt{2gh}$$

Kết hợp:

$$v_0 = \frac{(m+M)\sqrt{2gh}}{m}$$

**Ví dụ:** $m = 5\,\text{g}$, $M = 2\,\text{kg}$, $h = 8\,\text{cm}$:

$$v_0 = \frac{2.005 \times \sqrt{2 \times 9.81 \times 0.08}}{0.005} = \frac{2.005 \times 1.252}{0.005} = 502\,\text{m/s}$$

Đây là phương pháp đo vận tốc đạn chính xác không cần sensor điện tử — dùng trong thử nghiệm đạn dược từ thế kỷ 18 đến nay.

---

**Điểm mấu chốt:**

- Bảo toàn động lượng = hệ quả trực tiếp của Newton III, không phụ thuộc dạng lực bên trong.
- Va chạm hoàn toàn không đàn hồi: bảo toàn $p$, mất một phần $KE$.
- Va chạm đàn hồi: bảo toàn cả $p$ và $KE$ → hệ phương trình có nghiệm duy nhất.
- Cân bằng con lắc đạn: ứng dụng lịch sử kết hợp bảo toàn $p$ và $KE$ để đo vận tốc đạn.


---
*Exported from Feynman Bot*
