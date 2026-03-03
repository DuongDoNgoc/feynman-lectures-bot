---
lesson_id: 5416
lesson_type: concept
approval_status: approved
exported_at: "2026-03-03T15:33:04.523110+00:00"
content_hash: 7f7a00bf832f
chapter_number: 14
chapter_title: Chapter 14
section_number: 4
section_title: 14–3Conservative forces
---
# Lực Bảo Toàn — Định Nghĩa Chặt Chẽ và Thế Năng

*Source: Chapter 14 - Chapter 14 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_14.html)*

# Lực Bảo Toàn — Định Nghĩa Chặt Chẽ và Thế Năng

## Câu Hỏi Mở Đầu

Tại sao lực đàn hồi của lò xo có thể tích trữ và trả lại năng lượng hoàn toàn, nhưng lực ma sát thì không? Điều gì làm cho một lực "bảo toàn"?

## Định Nghĩa Chính Xác

Lực $\vec{F}$ là **bảo toàn** nếu công của nó trên mọi đường cong kín bằng không:
$$\oint \vec{F}\cdot d\vec{s} = 0$$

Điều này tương đương với: tồn tại hàm $U(x,y,z)$ sao cho $\vec{F} = -\nabla U$.

Hàm $U$ gọi là **thế năng** (potential energy).

## Thế Năng — Định Nghĩa Không Mơ Hồ

Feynman nhấn mạnh điểm tinh tế: thế năng chỉ xác định đến một hằng số cộng vào. Chọn điểm tham chiếu $P$ tùy ý nơi $U(P) = 0$, thì:
$$U(x,y,z) = -\int_P^{(x,y,z)} \vec{F}\cdot d\vec{s}$$

Giá trị này không phụ thuộc đường tích phân (vì $\vec{F}$ bảo toàn).

**Hệ quả**: Thay điểm tham chiếu từ $P$ sang $P'$ chỉ thêm hằng số $C = -\int_P^{P'}\vec{F}\cdot d\vec{s}$ vào $U$. Vì bảo toàn năng lượng chỉ quan tâm đến $\Delta U$, hằng số này không ảnh hưởng.

## Hai Mệnh Đề Nền Tảng

Feynman trình bày hai mệnh đề song hành:

**(1) Định lý công-động năng**: Công tác dụng = thay đổi động năng
$$W_{1\to2} = \frac{1}{2}mv_2^2 - \frac{1}{2}mv_1^2$$

**(2) Tính chất lực bảo toàn**: Công = giảm thế năng
$$W_{1\to2} = U(1) - U(2)$$

Kết hợp: $\frac{1}{2}mv_2^2 - \frac{1}{2}mv_1^2 = U(1) - U(2)$

Hay: $\frac{1}{2}mv_2^2 + U(2) = \frac{1}{2}mv_1^2 + U(1) = E = \text{const}$

## Phép So Sánh: Lực Bảo Toàn vs. Không Bảo Toàn

| Lực bảo toàn | Lực không bảo toàn |
|---|---|
| Trọng lực, đàn hồi, Coulomb, hấp dẫn | Ma sát động, lực cản không khí, một số lực từ |
| Có thế năng $U$ | Không có thế năng |
| Năng lượng cơ học bảo toàn | Năng lượng cơ học giảm dần |
| Tích phân đường kín = 0 | Tích phân đường kín ≠ 0 |
| Curl $\vec{F}$ = 0 | Curl $\vec{F}$ ≠ 0 |

## Ứng Dụng: Cảm Biến Điện Dung Và Thế Năng Điện

Trong thiết bị đo chính xác của bạn, tụ điện phẳng với điện trường $E = \sigma/\epsilon_0$ có thế năng điện cho điện tích $q$:
$$U_{điện} = qEx$$

Cảm biến điện dung MEMS đo dịch chuyển vi mô $\Delta x$ bằng cách đo sự thay đổi điện dung $\Delta C = \epsilon_0 A/x^2 \cdot \Delta x$. Lực điện (bảo toàn) tác dụng lên màng cảm biến: $F = -\partial U/\partial x = -qE$ — đây là lực bảo toàn.

Tuy nhiên: khi màng dao động và không khí bên trong gây ra lực cản (squeeze film damping), đây là lực không bảo toàn — làm tắt dao động. Phân biệt hai loại lực là quan trọng trong thiết kế MEMS.

## Điểm Mấu Chốt

Lực bảo toàn là lực mà công trên đường kín bằng 0 — tương đương với tồn tại thế năng $U$. Thế năng xác định đến một hằng số — chọn mốc tùy ý nhưng phải nhất quán. Kết hợp hai mệnh đề (công = $\Delta K$ và công = $-\Delta U$) cho bảo toàn năng lượng cơ học.

---
*Exported from Feynman Bot*
