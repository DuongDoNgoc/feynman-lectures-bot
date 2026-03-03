---
lesson_id: 5598
lesson_type: quiz
approval_status: pending
exported_at: "2026-03-03T15:33:08.852417+00:00"
content_hash: 5cea70d10ce0
chapter_number: 35
chapter_title: Chapter 35
section_number: 5
section_title: 35–4The chromaticity diagram
---
# ### Bài kiểm tra: Sơ Đồ Màu Sắc và Phép Trộn Màu

*Source: Chapter 35 - Chapter 35 (Section 5) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_35.html)*

### Bài kiểm tra: Sơ Đồ Màu Sắc và Phép Trộn Màu

**Câu 1:** Trên sơ đồ chromaticity (CIE 1931), tọa độ $x$ và $y$ được tính từ hệ số ba màu cơ bản $a$, $b$, $c$ theo công thức nào?

A. $x = a$, $y = b$

B. $x = \frac{a}{a+b+c}$, $y = \frac{b}{a+b+c}$

C. $x = \frac{a}{a+b}$, $y = \frac{b}{b+c}$

D. $x = \frac{a-b}{a+b+c}$, $y = \frac{b-c}{a+b+c}$

**Đáp án: B.** Tọa độ chromaticity là tỉ phần của từng thành phần so với tổng, để loại bỏ ảnh hưởng của độ sáng tuyệt đối. Khi nhân $a$, $b$, $c$ với cùng hệ số $k$, các giá trị $x$, $y$ không đổi.

---

**Câu 2:** Hai màu $P_1 = (0.2, 0.7)$ và $P_2 = (0.6, 0.1)$ trên sơ đồ chromaticity được trộn với tỉ lệ bằng nhau (50-50). Tọa độ màu hỗn hợp là:

A. $(0.4, 0.4)$

B. $(0.6, 0.7)$

C. $(0.2, 0.1)$

D. $(0.8, 0.8)$

**Đáp án: A.** $x_{mix} = (0.2 + 0.6)/2 = 0.4$; $y_{mix} = (0.7 + 0.1)/2 = 0.4$. Phép trộn màu 50-50 cho điểm nằm đúng giữa hai điểm trên sơ đồ.

---

**Câu 3:** Màu phổ thuần (pure spectral colors) trên sơ đồ chromaticity tạo thành:

A. Một đường thẳng đi qua gốc tọa độ

B. Một tam giác đều

C. Một đường cong dạng móng ngựa (horseshoe curve)

D. Một hình tròn đơn vị

**Đáp án: C.** Mỗi bước sóng đơn từ ~380 nm đến ~700 nm tạo ra một điểm trên đường cong spectral locus. Đường cong này có hình dạng đặc trưng giống móng ngựa. Đường thẳng nối hai đầu là locus của màu purple.

---

**Câu hỏi tự luận:**

Trong hệ thống machine vision của bạn dùng để kiểm tra chất lượng linh kiện cơ điện tử, cảm biến màu RGB đo được các giá trị $(R, G, B) = (180, 120, 60)$ cho một linh kiện đạt chuẩn, và $(R, G, B) = (360, 240, 120)$ cho linh kiện thứ hai. Khi so sánh bằng giá trị RGB tuyệt đối, hai linh kiện có vẻ khác nhau. Hãy giải thích tại sao việc chuyển sang tọa độ chromaticity $(x, y)$ lại phù hợp hơn cho bài toán phân loại màu trong điều kiện chiếu sáng thay đổi, và tính tọa độ chromaticity cho cả hai mẫu trên.

**Gợi ý trả lời:** Tọa độ chromaticity của mẫu 1: $x = 180/360 = 0.5$, $y = 120/360 = 0.333$. Mẫu 2: $x = 360/720 = 0.5$, $y = 240/720 = 0.333$. Hai mẫu cho cùng tọa độ chromaticity — chứng tỏ chúng cùng màu sắc, chỉ khác cường độ chiếu sáng (mẫu 2 dưới ánh sáng gấp đôi). Đây là nguyên tắc **illumination invariance** — quan trọng trong hệ thống đo lường tại nhà máy nơi ánh sáng không kiểm soát được hoàn toàn.


---
*Exported from Feynman Bot*
