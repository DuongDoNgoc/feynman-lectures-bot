---
lesson_id: 5596
lesson_type: concept
approval_status: pending
exported_at: "2026-03-03T15:33:08.821353+00:00"
content_hash: 7ad15bc33a1c
chapter_number: 35
chapter_title: Chapter 35
section_number: 5
section_title: 35–4The chromaticity diagram
---
# ## Biểu Đồ Chromaticity: Bản Đồ Hình Học của Màu Sắc

*Source: Chapter 35 - Chapter 35 (Section 5) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_35.html)*

## Biểu Đồ Chromaticity: Bản Đồ Hình Học của Màu Sắc

Trong kỹ thuật đo lường và automation, bạn quen với việc biểu diễn dữ liệu trong không gian nhiều chiều — vector trạng thái, không gian tham số calibration, hay diagrams pha (phase portrait). Màu sắc cũng có "bản đồ" riêng của nó: biểu đồ chromaticity (sơ đồ màu sắc chuẩn). Một khi hiểu được hình học của biểu đồ này, bạn có thể đọc ngay các tính chất của màu sắc — gamut, bão hòa, điểm trắng — giống như đọc bản vẽ kỹ thuật.

**Màu là vector trong không gian ba chiều**

Mọi màu sắc mà mắt người cảm nhận có thể biểu diễn bởi ba số thực $(a, b, c)$ — lượng của ba màu chủ đạo cần để khớp màu đó. Hai màu khác nhau ứng với hai vector khác nhau trong không gian 3D này. Phép trộn màu là phép cộng vector: nếu màu $C_1 = (a_1, b_1, c_1)$ và $C_2 = (a_2, b_2, c_2)$, thì hỗn hợp của chúng là $C_1 + C_2 = (a_1+a_2, b_1+b_2, c_1+c_2)$.

Điều thú vị: nếu nhân đôi tất cả $(a, b, c)$, màu sắc không đổi — chỉ sáng hơn. Điều này có nghĩa là "màu sắc" (chromaticity) thực ra là một hướng trong không gian 3D, không phải một điểm cụ thể. Thông tin màu sắc (bỏ qua độ sáng) sống trong không gian hai chiều — một mặt phẳng projective.

**Chiếu xuống mặt phẳng: Biểu đồ chromaticity**

Để bỏ đi thông tin độ sáng và chỉ giữ màu sắc, ta chuẩn hóa: đặt $x = a/(a+b+c)$, $y = b/(a+b+c)$. Với $x + y \leq 1$ (và $z = 1 - x - y$), mọi màu có thể vẽ lên mặt phẳng $(x, y)$. Đây là biểu đồ chromaticity CIE.

Trên biểu đồ này:
- Màu phổ đơn sắc (pure spectral colors — ánh sáng laser thuần túy) tạo thành một đường cong "horseshoe" (hình móng ngựa) từ tím (~400 nm) vòng qua xanh, xanh lá, vàng đến đỏ (~700 nm).
- Đường thẳng nối hai đầu đường cong (từ tím đến đỏ) là "line of purples" — dải màu tím-đỏ không có trong phổ đơn sắc tự nhiên.
- Tất cả màu sắc tự nhiên mà mắt người nhìn thấy nằm trong vùng bao bởi đường cong và đường thẳng này.

**Quy tắc vàng: Trộn màu = điểm trên đoạn thẳng**

Đây là tính chất hình học cực kỳ hữu dụng: bất kỳ hỗn hợp nào của hai màu $A$ và $B$ đều cho màu nằm trên đoạn thẳng $AB$ trong biểu đồ chromaticity. Hỗn hợp 50-50 nằm ở trung điểm, hỗn hợp $1/4 A + 3/4 B$ nằm cách $A$ một phần tư đoạn.

Đây chính xác là tính chất của kết hợp tuyến tính trong không gian vector — và biểu đồ chromaticity trực quan hóa điều này hoàn hảo. Giống như bạn dùng biểu đồ Bode để đọc đáp ứng tần số của hệ thống điều khiển, biểu đồ chromaticity cho phép bạn đọc kết quả phối màu trực quan mà không cần tính toán.

**Gamut của màn hình RGB**

Ba màu chủ đạo R, G, B định nghĩa một tam giác trong biểu đồ chromaticity (ví dụ đỉnh tại các vị trí của đèn LED đỏ, xanh lá, xanh lam). Tất cả màu trong tam giác này có thể tái tạo bằng cách trộn R, G, B với hệ số $a, b, c \geq 0$. Màu nằm ngoài tam giác — như một số màu xanh lá hay cyan bão hòa — không thể tái tạo với ba màu đó.

So sánh với không gian làm việc của robot (workspace): cũng như robot 3-DOF có workspace hữu hạn và không đến được một số vị trí, hệ màu RGB có gamut hữu hạn và không tái tạo được tất cả màu tự nhiên. Màn hình Wide Color Gamut (WCG) dùng đèn LED có màu sắc bão hòa hơn để mở rộng tam giác, bao phủ nhiều màu hơn.

**Young-Helmholtz và nguồn gốc không gian ba chiều**

Tại sao không gian màu lại là ba chiều? Lý thuyết Young-Helmholtz đề xuất rằng trong mắt người có ba loại tế bào nón, mỗi loại nhạy cảm với một dải bước sóng khác nhau (S, M, L). Não chỉ nhận được ba tín hiệu này — và đó là tất cả thông tin màu sắc mà nó xử lý. Không gian ba chiều là hệ quả trực tiếp của sinh học tiến hóa.

**Điểm mấu chốt**

Màu sắc là vector trong không gian ba chiều, và biểu đồ chromaticity là hình chiếu 2D của không gian đó (bỏ đi độ sáng). Quy tắc cốt lõi: trộn hai màu bất kỳ cho điểm nằm trên đoạn thẳng nối hai màu đó trong biểu đồ. Gamut của bộ ba màu chủ đạo là tam giác trong biểu đồ — không bao giờ bao phủ hết tất cả màu tự nhiên. Hiểu biểu đồ chromaticity giúp kỹ sư automation thiết kế, đánh giá và hiệu chỉnh hệ thống đo màu trong QC tự động một cách có cơ sở khoa học.

---
*Exported from Feynman Bot*
