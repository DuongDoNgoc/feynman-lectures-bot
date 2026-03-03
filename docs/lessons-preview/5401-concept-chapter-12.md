---
lesson_id: 5401
lesson_type: concept
approval_status: approved
exported_at: "2026-03-03T15:33:04.125181+00:00"
content_hash: 3da23d822f5a
chapter_number: 12
chapter_title: Chapter 12
section_number: 6
section_title: 12–5Pseudo forces
---
# ## Lực Giả (Pseudo Forces) và Hệ Quy Chiếu Phi Quán Tính

*Source: Chapter 12 - Chapter 12 (Section 6) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_12.html)*

## Lực Giả (Pseudo Forces) và Hệ Quy Chiếu Phi Quán Tính

Khi ngồi trên ô tô đang tăng tốc, bạn cảm thấy bị "đẩy" về phía sau. Nhưng thực ra không có ai hay vật nào tác dụng lực đó lên bạn — đây là **lực giả** (pseudo force hay fictitious force), xuất hiện vì bạn đang quan sát từ một **hệ quy chiếu phi quán tính** (đang gia tốc).

### Hệ Quy Chiếu Quán Tính và Phi Quán Tính

**Hệ quán tính (inertial frame):** Đứng yên hoặc chuyển động thẳng đều. Định luật Newton đúng chính xác: nếu tổng lực = 0 thì gia tốc = 0.

**Hệ phi quán tính (non-inertial frame):** Đang gia tốc. Định luật Newton **không áp dụng trực tiếp** — cần thêm "lực giả" để phương trình chuyển động đúng.

### Suy Dẫn Toán Học

Gọi Joe (hệ quán tính) và Moe (hệ phi quán tính, chuyển động với gia tốc $a_0$ so với Joe). Vị trí hạt theo hai người:

$$x = x' + s(t)$$

Với $s(t) = \frac{1}{2}a_0 t^2$ (Moe gia tốc đều):

$$\frac{dx}{dt} = \frac{dx'}{dt} + a_0 t$$

$$\frac{d^2x}{dt^2} = \frac{d^2x'}{dt^2} + a_0$$

Theo Joe: $m\ddot{x} = F$ (định luật Newton đúng)

Theo Moe: $m\ddot{x}' = F - ma_0$

Moe thấy hạt chịu thêm lực $-ma_0$ — đây là **lực giả** (inertial force hay pseudo force).

### Ý Nghĩa Vật Lý

Lực giả **không có nguồn gốc vật lý thực** — không có vật nào tác dụng lực đó. Nó chỉ xuất hiện vì hệ quy chiếu đang gia tốc. Tuy nhiên, trong hệ phi quán tính, lực giả **thực sự ảnh hưởng** đến chuyển động quan sát được.

Ví dụ quan trọng:
- **Lực quán tính** (xe tăng tốc/phanh)
- **Lực ly tâm** (trong hệ xoay tròn): $F_{cf} = m\omega^2 r$, hướng ra ngoài
- **Lực Coriolis** (Trái Đất tự quay): $\mathbf{F}_{Cor} = -2m\boldsymbol{\omega}\times\mathbf{v}$

### Phép So Sánh: IMU và Hệ Dẫn Đường Quán Tính

**IMU (Inertial Measurement Unit)** trong hệ thống dẫn đường quán tính (INS) đo gia tốc bằng accelerometer. Accelerometer đo **gia tốc so với hệ quán tính** (lực trên khối proof mass):

$$a_{measured} = a_{true} - g$$

Khi máy bay đứng yên trên đường băng, accelerometer đọc $+g$ hướng lên — vì nó đang "gia tốc" ra khỏi hệ quy chiếu tự do rơi (quán tính thực sự).

Trong điều khiển tên lửa, bộ tính toán phải liên tục tích phân gia tốc đo được, trừ đi $g$, để tính gia tốc và vận tốc thực trong hệ quán tính (Earth-Centered Inertial frame).

**Lực Coriolis trong vũ khí tầm xa:** Đạn pháo bay $20$ km cần tính hiệu chỉnh Coriolis:

$$\Delta y = 2\Omega v_0 t^2 \sin(\phi)$$

Với $\Omega = 7.27\times10^{-5}$ rad/s (tốc độ tự quay Trái Đất), $v_0 = 800$ m/s, $t = 25$ s, $\phi = 21°$ (vĩ độ Hà Nội):

$$\Delta y \approx 2 \times 7.27\times10^{-5} \times 800 \times 625 \times 0.36 \approx 26 \text{ m}$$

Hiệu chỉnh ~26 m — đáng kể ở tầm xa!

### Nguyên Lý Tương Đương

Einstein tổng quát hóa ý tưởng này: **không có thực nghiệm cục bộ nào phân biệt được** lực hấp dẫn và lực quán tính. Đây là nền tảng của Thuyết Tương Đối Rộng — từ ý tưởng đơn giản của Feynman về hệ quy chiếu.

### Điểm Mấu Chốt

- **Lực giả** xuất hiện trong hệ phi quán tính — không có nguồn gốc vật lý thực
- **Công thức**: lực giả $= -ma_0$ (với $a_0$ là gia tốc của hệ quy chiếu)
- **Lực ly tâm** và **Coriolis** là lực giả trong hệ xoay — quan trọng cho dẫn đường, cơ khí chính xác
- **IMU** đo gia tốc so với hệ quán tính, cần trừ $g$ để tính gia tốc thực

---
*Exported from Feynman Bot*
