---
lesson_id: 5539
lesson_type: concept
approval_status: approved
exported_at: "2026-03-03T15:33:07.449370+00:00"
content_hash: b4d65ab9d446
chapter_number: 30
chapter_title: Chapter 30
section_number: 2
section_title: 30–1The resultant amplitude due tonnequal oscillators
---
# ## Nhiễu Xạ: Khi Giao Thoa Đến Từ Hàng Nghìn Nguồn

*Source: Chapter 30 - Chapter 30 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_30.html)*

## Nhiễu Xạ: Khi Giao Thoa Đến Từ Hàng Nghìn Nguồn

### Câu hỏi mở đầu

Bạn đã bao giờ nhìn vào đĩa CD hay DVD dưới ánh sáng trắng và thấy cầu vồng màu sắc loang loáng chưa? Hay đặt câu hỏi: tại sao kính hiển vi quang học chỉ nhìn thấy những vật có kích thước trên 200 nm, dù bạn dùng thấu kính hoàn hảo đến đâu? Đây không phải giới hạn của thiết bị — đây là **giới hạn của ánh sáng**, và nó xuất phát từ nguyên lý nhiễu xạ mà chúng ta sắp khám phá.

### Từ giao thoa đến nhiễu xạ

Chương trước, chúng ta đã nghiên cứu giao thoa của hai nguồn. Hôm nay, câu hỏi được mở rộng: điều gì xảy ra khi có **n nguồn** dao động cùng biên độ $A$, cách đều nhau, nhưng mỗi nguồn lệch pha $\phi$ so với nguồn kề bên?

Thực ra, ranh giới giữa "giao thoa" (interference) và "nhiễu xạ" (diffraction) chỉ là quy ước ngôn ngữ. Feynman thẳng thắn: *Không ai định nghĩa được sự khác biệt một cách thỏa mãn.* Thông thường, khi chỉ có 2 nguồn, người ta gọi là giao thoa; khi có nhiều nguồn, người ta gọi là nhiễu xạ. Về vật lý, cả hai là một.

Xét $n$ nguồn dao động đều nhau, hiệu pha giữa hai nguồn liên tiếp khi quan sát ở góc $\theta$ là:

$$\phi = \alpha + \frac{2\pi d\sin\theta}{\lambda}$$

Trong đó $d$ là khoảng cách giữa hai nguồn, $\alpha$ là pha nội tại, và $\lambda$ là bước sóng. Bài toán là: tính tổng $n$ sóng này.

### Phép tính hình học: Đa giác đều trong mặt phẳng pha

Thay vì làm toán thuần túy, Feynman dùng hình học. Mỗi sóng thành phần là một phasor (vectơ trong mặt phẳng pha) có độ dài $A$. Mỗi phasor tiếp theo xoay thêm góc $\phi$ so với cái trước.

**Hình dung thế này:** Bạn bước đi $n$ bước, mỗi bước dài $A$, nhưng mỗi bước lại rẽ trái thêm một góc $\phi$ so với bước trước. Điểm cuối cùng của hành trình là tổng hợp $n$ phasor. Quỹ đạo này vẽ ra một cung tròn!

**Phép so sánh với kỹ thuật cơ điện tử:** Hình dung một robot di chuyển với bước không đổi nhưng xoay bánh lái một góc cố định sau mỗi bước — nó sẽ đi thành vòng tròn. Chuỗi phasor hoạt động hoàn toàn như vậy.

Từ hình học của đa giác đều, biên độ tổng hợp là:

$$A_R = A \cdot \frac{\sin(n\phi/2)}{\sin(\phi/2)}$$

**Giải thích từng nhân tử:**
- Tử số $\sin(n\phi/2)$: phụ thuộc vào tổng pha tích lũy của toàn bộ $n$ nguồn
- Mẫu số $\sin(\phi/2)$: phụ thuộc vào hiệu pha giữa hai nguồn liên tiếp

### Hai điều kiện đặc biệt quan trọng

**Điều kiện 1 — Cực đại chính (Principal Maximum):**

Khi $\phi = 0$ (hoặc $2\pi m$), tất cả $n$ phasor cùng hướng, cộng thẳng hàng: $A_R = nA$. Cường độ:
$$I_{max} = n^2 A^2$$

Đây là lý do tại sao mảng anten radar có $n$ phần tử mạnh hơn $n^2$ lần so với một phần tử đơn — không phải $n$ lần! Đây là lợi ích kỳ diệu của coherence (tính kết hợp).

**Điều kiện 2 — Cực tiểu (Minimum/Null):**

Khi $n\phi = 2\pi$ (tức $\phi = 2\pi/n$), $n$ phasor khép kín thành đa giác đều, tổng bằng 0: $A_R = 0$.

Giữa hai cực đại chính là các cực đại phụ (secondary maxima) nhỏ hơn nhiều. Hình dạng này được gọi là **diffraction pattern** (vân nhiễu xạ).

### Ứng dụng thực tế: Cách tử nhiễu xạ và mảng anten

**Cách tử quang học (Diffraction Grating):** Thay vì $n$ dây anten, ta có $n$ vạch khắc trên kính hoặc kim loại, cách đều nhau. Ánh sáng tán xạ từ mỗi vạch đóng vai trò một nguồn mới. Cực đại chính xuất hiện tại:
$$d\sin\theta = m\lambda \quad (m = 0, \pm 1, \pm 2, ...)$$

Mỗi bước sóng khác nhau cho cực đại tại góc khác nhau — đây là nguyên lý phân tích phổ. Máy quang phổ kế (spectrometer) trong phòng lab chế tạo chính xác của bạn hoạt động theo đúng nguyên tắc này.

**Mảng anten (Antenna Array) trong radar:** Đây là hình thức điện từ của cách tử nhiễu xạ. Trong hệ thống vũ khí dẫn đường, mảng anten phased array cho phép định hướng chùm tia tới vị trí mục tiêu với độ phân giải góc cực cao, nhờ tính chất $A_R \propto n$ và vân chính cực kỳ hẹp khi $n$ lớn.

**Điểm mấu chốt:**

- Nhiễu xạ và giao thoa là **cùng một hiện tượng** — chỉ khác số lượng nguồn
- Biên độ hợp của $n$ nguồn cách đều: $A_R = A\sin(n\phi/2)/\sin(\phi/2)$
- Cực đại chính tại $\phi = 2\pi m$: $A_R = nA$, cường độ $I = n^2 A^2$
- Số nguồn càng lớn: cực đại càng hẹp, càng sắc nét — đây là cơ sở của độ phân giải trong quang học và radar
- Hình học phasor (đa giác cung tròn) là công cụ trực quan nhất để "thấy" tại sao công thức có dạng sin/sin

---
*Exported from Feynman Bot*
