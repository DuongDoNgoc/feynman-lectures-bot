---
lesson_id: 5402
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-02T15:10:28.506871+00:00"
content_hash: c0ad739caa1f
chapter_number: 12
chapter_title: Chapter 12
section_number: 6
section_title: 12–5Pseudo forces
---
# Lực Giả — Phân Tích Chuyên Sâu

*Source: Chapter 12 - Chapter 12 (Section 6) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_12.html)*

# Lực Giả — Phân Tích Chuyên Sâu

## Thiết Lập Bài Toán: Hệ Quy Chiếu Phi Quán Tính

Để hiểu lực giả một cách thấu đáo, hãy bắt đầu từ nền tảng toán học. Xét hai hệ quy chiếu: Joe đứng yên (hệ S) và Moe đang chuyển động với gia tốc $a$ (hệ S').

Mối quan hệ tọa độ: $x' = x - s(t)$, trong đó $s(t)$ là vị trí của hệ S' so với S.

Khi lấy đạo hàm hai lần theo thời gian:
$$\frac{d^2x'}{dt^2} = \frac{d^2x}{dt^2} - \frac{d^2s}{dt^2}$$

Định luật Newton trong hệ quán tính S: $F = m\frac{d^2x}{dt^2}$

Suy ra trong hệ S':
$$m\frac{d^2x'}{dt^2} = F - m\frac{d^2s}{dt^2} = F - ma$$

Số hạng $-ma$ chính là **lực giả** — một lực xuất hiện thuần túy do sự chọn hệ quy chiếu, không phải do tương tác vật lý thực sự.

## Ví Dụ Từng Bước: Xe Tăng Tăng Tốc

Xét xe tăng quân sự đang tăng tốc $a = 3\ m/s^2$ về phía trước. Bên trong, một quả cầu treo dây.

**Phân tích từ mặt đất (hệ quán tính):**
- Lực tác dụng lên quả cầu: căng dây $T$ và trọng lực $mg$
- Quả cầu gia tốc cùng xe: $T\sin\theta = ma$, $T\cos\theta = mg$
- $\tan\theta = a/g = 3/9.8 \approx 0.306$, góc $\theta \approx 17°$

**Phân tích từ hệ quy chiếu xe (hệ phi quán tính):**
- Người quan sát trong xe thấy quả cầu đứng yên
- Để Newton đúng, phải thêm lực giả $F_{\text{giả}} = -ma$ (hướng ra sau)
- Cân bằng: căng dây + trọng lực + lực giả = 0
- Kết quả góc lệch giống hệt: $\theta \approx 17°$

Cả hai phân tích cho kết quả vật lý giống nhau — đây là tính nhất quán của cơ học.

## Ví Dụ Thực Tế: Hệ Thống Dẫn Đường Quán Tính (INS)

Trong hệ thống dẫn đường tên lửa và máy bay quân sự, **Inertial Navigation System (INS)** sử dụng accelerometer để đo gia tốc. Nhưng accelerometer đo gì chính xác?

**Accelerometer đo lực giả!**

Khi tên lửa gia tốc với $a$ trong không gian quán tính, accelerometer trong hệ tên lửa (hệ phi quán tính) đo lực biểu kiến $-ma$ tác dụng lên khối lượng thử nghiệm. Từ đó tính ngược lại gia tốc $a$.

Tuy nhiên, có một vấn đề tinh tế: **trọng lực cũng là "lực giả"!** Theo Einstein, một vật rơi tự do ở trong hệ quy chiếu quán tính — không cảm nhận trọng lực. Accelerometer trên mặt đất đo $g = 9.8\ m/s^2$ không phải vì Trái Đất kéo nó xuống, mà vì mặt đất đẩy nó lên!

INS trên máy bay cần tách biệt gia tốc do động cơ và gia tốc do trọng lực — đây là bài toán kỹ thuật phức tạp trong thiết kế hệ thống điều hướng.

## Lực Coriolis: Lực Giả Trong Hệ Quay

Khi hệ quy chiếu không chỉ tịnh tiến mà còn quay với vận tốc góc $\omega$, xuất hiện thêm lực giả:

1. **Lực ly tâm**: $\vec{F}_{\text{ly tâm}} = m\omega^2 r$ (hướng ra ngoài)
2. **Lực Coriolis**: $\vec{F}_{\text{Cor}} = -2m\vec{\omega} \times \vec{v}'$

**Ứng dụng trong cơ khí chính xác**: Máy tiện CNC quay với tốc độ cao. Khi dao cắt di chuyển theo hướng kính, lực Coriolis tác dụng theo hướng tiếp tuyến — gây ra sai số gia công nếu không được bù. Trong máy tiện chính xác gia công chi tiết micrometer, lực Coriolis phải được tính vào thuật toán điều khiển bù lực.

## Tính Tỷ Lệ Với Khối Lượng — Manh Mối Về Trọng Lực

Đặc tính quan trọng nhất của lực giả: **tỷ lệ với khối lượng $m$**.

Trọng lực cũng tỷ lệ với $m$: $F = mg$.

Đây không phải trùng hợp! Einstein nhận ra điều này năm 1907 — **Nguyên lý Tương Đương**: không thể phân biệt được trọng lực và lực quán tính (lực giả) bằng thí nghiệm cơ học thuần túy.

Thí nghiệm thang máy kinh điển:
- Thang máy rơi tự do: bạn cảm thấy weightless (như hệ quán tính không có trọng lực)
- Thang máy tăng tốc lên: bạn cảm thấy nặng hơn (như trọng lực tăng)

Đây là nền tảng dẫn đến Thuyết Tương Đối Rộng — trọng lực được mô tả là độ cong của không-thời gian, không phải lực thực sự.

## Bài Tập Có Hướng Dẫn

**Bài toán**: Robot công nghiệp có cánh tay quay với gia tốc góc $\alpha = 5\ rad/s^2$ và vận tốc góc tức thời $\omega = 3\ rad/s$. Tại đầu cánh tay (cách tâm $r = 0.5\ m$) có cảm biến lực $m = 0.1\ kg$.

Tính lực giả tác dụng lên cảm biến.

**Giải:**
1. Gia tốc hướng tâm (ly tâm): $a_c = \omega^2 r = 9 \times 0.5 = 4.5\ m/s^2$
   → Lực ly tâm: $F_{\text{lt}} = ma_c = 0.1 \times 4.5 = 0.45\ N$

2. Gia tốc tiếp tuyến: $a_t = \alpha r = 5 \times 0.5 = 2.5\ m/s^2$
   → Lực quán tính tiếp tuyến: $F_{\text{qt}} = ma_t = 0.1 \times 2.5 = 0.25\ N$

3. Lực giả tổng hợp: $F_{\text{tổng}} = \sqrt{0.45^2 + 0.25^2} \approx 0.515\ N$

Cảm biến lực phải được hiệu chỉnh để trừ đi các lực giả này — nếu không, kết quả đo lực tương tác thực sẽ bị sai số đáng kể trong môi trường động.

## Điểm Mấu Chốt

Lực giả là công cụ toán học hợp lệ cho phép áp dụng Newton trong hệ phi quán tính, nhưng bản chất vật lý của chúng là biểu hiện của việc chọn hệ quy chiếu không phù hợp. Trong kỹ thuật: accelerometer trong INS đo lực giả để suy ra gia tốc thực; robot cần bù lực giả Coriolis và ly tâm để đạt độ chính xác; và điều kỳ diệu nhất — trọng lực có thể chỉ là lực giả vũ trụ lớn nhất mà chúng ta biết.

---
*Exported from Feynman Bot*
