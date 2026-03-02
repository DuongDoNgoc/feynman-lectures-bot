---
lesson_id: 5404
lesson_type: concept
approval_status: approved
exported_at: "2026-03-02T15:10:28.563610+00:00"
content_hash: f9e02977f4d7
chapter_number: 13
chapter_title: Chapter 13
section_number: 1
section_title: 13Work and Potential Energy (A)
---
# Công và Thế Năng

*Source: Chapter 13 - Chapter 13 (Section 1) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_13.html)*

# Công và Thế Năng

## Câu Hỏi Mở Đầu

Tại sao một chiếc lò xo nén có thể bắn viên đạn, nhưng khi bạn nắm lò xo đứng yên, nó không làm bạn di chuyển? Năng lượng ẩn ở đâu trong lò xo, và cơ học giải thích hiện tượng này thế nào?

## Công — Thước Đo Trao Đổi Năng Lượng

Khi lực $ec{F}$ tác dụng lên vật di chuyển đoạn $dec{s}$, **công** được thực hiện là:
$$W = \int_1^2 ec{F} \cdot dec{s}$$

Điều quan trọng: chỉ thành phần lực **dọc theo chiều chuyển động** mới thực hiện công. Lực vuông góc với chuyển động không sinh công — đây là lý do lực ly tâm không làm thay đổi tốc độ của vật chuyển động tròn đều.

Định lý công-động năng: công thực hiện bằng sự thay đổi động năng:
$$W = \Delta\left(rac{1}{2}mv^2ight)$$

## Thế Năng — Năng Lượng Tích Trữ Theo Vị Trí

Với lực bảo toàn (như trọng lực, lực đàn hồi), công thực hiện **không phụ thuộc vào đường đi**, chỉ phụ thuộc vào điểm đầu và điểm cuối. Ta định nghĩa **thế năng** $U$ sao cho:

$$W = U(1) - U(2)$$

Công của lực bảo toàn bằng độ giảm thế năng.

**Thế năng trọng lực**: $U(h) = mgh$
**Thế năng hấp dẫn** (khoảng cách $r$ từ tâm Trái Đất): $U(r) = -rac{GM_\oplus m}{r}$

Dấu âm trong $U(r)$ có ý nghĩa: càng xa Trái Đất, thế năng càng tăng (ít âm hơn) — cần cung cấp năng lượng để bay ra xa.

## Phép So Sánh Với Cơ Điện Tử

Hãy nghĩ đến tụ điện trong mạch điện: tụ điện tích trữ **năng lượng điện trường** khi bị nạp, giống như lò xo tích trữ **thế năng đàn hồi** khi bị nén. Cả hai đều:
- Tích trữ năng lượng theo "cấu hình" (điện tích/biến dạng)
- Giải phóng năng lượng khi "thả ra"
- Có thể tính năng lượng qua tích phân lực/điện áp theo chuyển vị/điện tích

Trong robot cơ điện tử: khi động cơ servo di chuyển cánh tay lên cao, nó thực hiện công chống lại trọng lực — công này được tích trữ dưới dạng thế năng. Khi cánh tay hạ xuống (có điều khiển), thế năng chuyển thành động năng, và bộ điều khiển cần tính đến điều này để tránh overshooting.

## Thế Năng Điện — Ứng Dụng Trong Đo Lường

Với tụ phẳng có mật độ điện tích $\sigma$ trên mỗi diện tích, điện trường $E = \sigma/\epsilon_0$. Lực lên điện tích $q$: $ec{F} = qec{E}$. Thế năng điện của điện tích trong tụ tỷ lệ với vị trí — đây là nguyên lý hoạt động của cảm biến điện dung đo vị trí với độ chính xác micrometer.

Trong thiết bị đo chính xác của bạn: cảm biến điện dung đo khoảng cách $d$ bằng cách đo điện dung $C = \epsilon_0 A/d$. Sự thay đổi $\Delta d$ ở mức micrometer tương ứng với sự thay đổi $\Delta C$ đo được — bản chất là đo sự thay đổi thế năng điện.

## Điểm Mấu Chốt

Công là thước đo trao đổi năng lượng giữa lực và chuyển động. Thế năng là năng lượng ẩn trong cấu hình vị trí — nó chờ đợi để được giải phóng. Lực bảo toàn "nhớ" lịch sử không gian, không phải lịch sử thời gian — đây là điều làm cho thế năng có ý nghĩa và bảo toàn năng lượng thành định luật mạnh mẽ nhất trong vật lý.

---
*Exported from Feynman Bot*
