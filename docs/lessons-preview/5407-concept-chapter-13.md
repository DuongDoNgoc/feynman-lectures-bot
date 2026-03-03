---
lesson_id: 5407
lesson_type: concept
approval_status: approved
exported_at: "2026-03-03T15:33:04.285948+00:00"
content_hash: 2f0c7bc7c2fe
chapter_number: 13
chapter_title: Chapter 13
section_number: 3
section_title: 13–2Work done by gravity
---
# Bảo Toàn Năng Lượng — Quỹ Đạo Hành Tinh và Vệ Tinh

*Source: Chapter 13 - Chapter 13 (Section 3) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_13.html)*

# Bảo Toàn Năng Lượng — Quỹ Đạo Hành Tinh và Vệ Tinh

## Câu Hỏi Mở Đầu

Tại sao vệ tinh GPS ở quỹ đạo cao lại chuyển động chậm hơn ISS ở quỹ đạo thấp? Và tại sao quỹ đạo hành tinh là hình ellipse chứ không phải hình khác?

## Bảo Toàn Năng Lượng Trong Trường Hấp Dẫn

Trong trường hấp dẫn, tổng năng lượng cơ học được bảo toàn:
$$E = \frac{1}{2}mv^2 - \frac{GMm}{r} = \text{hằng số}$$

Đây là câu trả lời: vệ tinh ở quỹ đạo cao ($r$ lớn) có thế năng lớn hơn (ít âm hơn), nên động năng phải nhỏ hơn → vận tốc nhỏ hơn.

## Tại Sao Tích Phân Trên Đường Kín Bằng Không?

Feynman đặt câu hỏi sắc bén: nếu đi theo một đường kín trong trường hấp dẫn và tổng công khác 0, ta có thể tạo ra năng lượng từ chân không — điều bất khả thi. Vậy phải bằng 0.

Chứng minh bằng phân tích: lực hấp dẫn $\vec{F} = -GMm/r^2 \hat{r}$ chỉ phụ thuộc vào $r$. Khi di chuyển tiếp tuyến (vuông góc với $\hat{r}$), lực không làm công. Khi di chuyển theo hướng kính, công tích lũy phụ thuộc chỉ vào $\int dr/r^2 = -1/r$ — một hàm chỉ của $r$, nên tích phân trên đường kín bằng 0.

## Phép So Sánh Với Mạch Điện

Bảo toàn năng lượng trong trường hấp dẫn giống như bảo toàn điện tích trong mạch điện. Định luật Kirchhoff về điện áp (KVL): tổng điện áp trong mạch kín bằng 0 — đây là hệ quả của tính bảo toàn của lực điện (lực Coulomb). Cả hai đều xuất phát từ cùng nguyên lý sâu xa: **lực bảo toàn có gradient thế năng**.

Trong thiết kế hệ thống servo: nguồn điện áp cung cấp năng lượng cho motor, motor chuyển thành cơ năng — bảo toàn năng lượng (trừ tổn thất nhiệt) là nguyên lý thiết kế cơ bản.

## Ứng Dụng: Vận Tốc Tại Các Điểm Quỹ Đạo

Cho vệ tinh có quỹ đạo ellipse với bán trục lớn $a$. Tại điểm gần nhất ($r_{min}$, vận tốc $v_{max}$) và xa nhất ($r_{max}$, vận tốc $v_{min}$):

Bảo toàn năng lượng:
$$\frac{1}{2}v_{max}^2 - \frac{GM}{r_{min}} = \frac{1}{2}v_{min}^2 - \frac{GM}{r_{max}}$$

Bảo toàn mô men động lượng:
$$r_{min} v_{max} = r_{max} v_{min}$$

Hai phương trình này — cùng với bảo toàn năng lượng — hoàn toàn xác định quỹ đạo. Đây là sức mạnh của định luật bảo toàn: không cần giải phương trình vi phân!

## Điểm Mấu Chốt

Bảo toàn năng lượng trong trường hấp dẫn là hệ quả của tính bảo toàn của lực hấp dẫn (tích phân đường kín bằng 0). Đại lượng $E = \frac{1}{2}mv^2 - GMm/r$ không đổi theo thời gian, cho phép dự đoán vận tốc tại mọi điểm trên quỹ đạo mà không cần biết lịch sử chuyển động.

---
*Exported from Feynman Bot*
