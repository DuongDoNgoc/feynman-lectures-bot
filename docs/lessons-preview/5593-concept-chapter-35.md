---
lesson_id: 5593
lesson_type: concept
approval_status: pending
exported_at: "2026-03-03T15:33:08.775163+00:00"
content_hash: cd6400cba2f5
chapter_number: 35
chapter_title: Chapter 35
section_number: 4
section_title: 35–3Measuring the color sensation
---
# ## Nhận Thức Màu Sắc: Tại Sao Ba Màu Chủ Đạo Là Đủ?

*Source: Chapter 35 - Chapter 35 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_35.html)*

## Nhận Thức Màu Sắc: Tại Sao Ba Màu Chủ Đạo Là Đủ?

Bạn có bao giờ đặt câu hỏi tại sao màn hình hiển thị của thiết bị đo lường — dù đó là oscilloscope, màn hình điều khiển PLC, hay HMI trong hệ thống automation — chỉ dùng ba màu đèn LED (đỏ, xanh lá, xanh lam) mà hiển thị được cả triệu màu sắc? Câu trả lời không nằm ở kỹ thuật điện tử, mà nằm ở cách mắt người xử lý màu sắc — và đây là một trong những bài học đẹp nhất về phối màu (color mixing).

**Ánh sáng trắng và phân tách phổ**

Khi ánh sáng trắng đi qua lăng kính, nó tách ra thành một dải liên tục của màu sắc từ tím (khoảng 400 nm) đến đỏ (khoảng 700 nm). Đây là phân bố phổ vật lý đầy đủ. Một nguồn sáng bất kỳ có thể có nhiều hay ít ánh sáng ở mỗi bước sóng — đó là đặc tính vật lý khách quan của nguồn. Nhưng câu hỏi thú vị hơn là: từ phân bố phổ đó, mắt người cảm nhận màu gì?

**Nguyên lý cơ bản: Phối màu cộng (additive color mixing)**

Thực nghiệm với máy chiếu ánh sáng màu cho thấy: khi trộn ánh sáng đỏ (Red) với ánh sáng xanh lá (Green) theo tỉ lệ thích hợp, ta thu được cảm giác màu vàng. Không phải màu "đỏ-xanh-lá" mà là một màu mới: vàng. Đây là phối màu cộng — khác hoàn toàn với phối màu trừ (pigment/sơn) mà bạn học hồi tiểu học.

Gọi $R$, $G$, $B$ là các nguồn màu chủ đạo. Khi trộn với hệ số $r$ và $g$:
$$Y = rR + gG$$

Công thức này không phải đại số thông thường — dấu cộng ở đây là "kết hợp ánh sáng cho cảm giác tương tự". Feynman gọi đây là "phép cộng màu" (color addition).

**Câu hỏi cốt lõi: Có thể tái tạo mọi màu từ ba màu chủ đạo không?**

Thực nghiệm cho thấy: với ba màu chủ đạo R, G, B, ta có thể khớp (match) hầu hết các màu mà mắt người nhìn thấy. Tuy nhiên có những màu cần "hệ số âm" — điều này có nghĩa là phải thêm màu đó vào phía màu cần khớp, không phải phía hỗn hợp.

Mối quan hệ này có thể viết tổng quát:

$$C = aR + bG + cB$$

trong đó $a$, $b$, $c$ là các hệ số có thể dương hoặc âm. Nếu tất cả ba hệ số dương, màu $C$ nằm trong gamut của hệ R, G, B. Nếu một hệ số âm, màu đó nằm ngoài gamut — không thể tái tạo bằng cách cộng ánh sáng từ ba nguồn đó.

**So sánh với đo lường precision: Phương trình màu như ma trận chuyển đổi**

Trong kỹ thuật đo lường, bạn quen với khái niệm chuyển đổi tọa độ giữa các hệ tham chiếu. Phối màu hoạt động theo nguyên lý tương tự: một màu là "vector" trong không gian ba chiều (vì mắt người có ba loại tế bào nón). Bộ ba màu chủ đạo R, G, B định nghĩa một "hệ trục tọa độ" trong không gian màu. Màu khác được biểu diễn là vector với tọa độ $(a, b, c)$ trong hệ này.

Cũng như hệ tọa độ Cartesian không thể biểu diễn tất cả điểm nếu ba trục không độc lập tuyến tính, bộ ba màu R, G, B không tái tạo được tất cả màu nếu "gamut tam giác" của chúng không bao phủ toàn bộ không gian màu có thể nhìn thấy.

**Thực nghiệm với bốn máy chiếu**

Khi dùng bốn máy chiếu (đỏ, xanh lá, xanh lam, và một màu thứ tư), bạn có thể quan sát trực tiếp:
- Vùng chồng chéo đỏ + xanh lá cho màu vàng
- Đỏ + xanh lam cho màu đỏ tía (magenta)
- Xanh lá + xanh lam cho màu cyan
- Đỏ + xanh lá + xanh lam cho màu trắng

Có thể tạo màu vàng theo nhiều cách khác nhau (đỏ+xanh lá vs. ánh sáng đơn sắc 580 nm) và mắt người không phân biệt được — đây là metamerism trong thực tế.

**Điểm mấu chốt**

Mắt người có ba loại tế bào cảm nhận màu (S, M, L cones), nên không gian màu là ba chiều. Bất kỳ màu nào có thể biểu diễn qua ba hệ số: $C = aR + bG + cB$. Phần lớn màu tự nhiên có thể tái tạo từ ba màu chủ đạo với hệ số dương — đây là cơ sở của màn hình RGB, máy in CMY, và mọi hệ thống hiển thị màu. Màu nằm ngoài gamut của ba màu chủ đạo đòi hỏi hệ số âm — không thể tái tạo bằng cộng ánh sáng đơn giản.

---
*Exported from Feynman Bot*
