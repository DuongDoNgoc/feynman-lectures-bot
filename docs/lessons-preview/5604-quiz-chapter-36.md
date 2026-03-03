---
lesson_id: 5604
lesson_type: quiz
approval_status: pending
exported_at: "2026-03-03T15:33:08.945989+00:00"
content_hash: 1f5bb17f78a9
chapter_number: 36
chapter_title: Chapter 36
section_number: 1
section_title: 36Mechanisms of Seeing
---
# ### Bài kiểm tra: Xử Lý Thông Tin Thị Giác và Color Constancy

*Source: Chapter 36 - Chapter 36 (Section 1) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_36.html)*

### Bài kiểm tra: Xử Lý Thông Tin Thị Giác và Color Constancy

**Câu 1:** Lateral inhibition trong võng mạc có tác dụng chính là:

A. Tăng độ nhạy với ánh sáng yếu bằng cách khuếch đại tín hiệu từ nhiều tế bào

B. Tăng cường tương phản tại ranh giới sáng-tối, tạo hiệu ứng phát hiện cạnh ngay trong võng mạc

C. Cho phép phân biệt màu sắc bằng cách ức chế tế bào nón không phù hợp

D. Điều chỉnh kích thước đồng tử (iris) dựa trên cường độ ánh sáng

**Đáp án: B.** Tế bào ngang (horizontal cells) kết nối các tế bào quang kề nhau và ức chế chúng. Tại ranh giới sáng-tối, vùng sáng cạnh ranh giới bị ức chế ít hơn (tế bào tối bên cạnh yếu, ức chế ít), nên trông sáng hơn. Vùng tối cạnh ranh giới bị ức chế nhiều hơn (tế bào sáng bên cạnh mạnh, ức chế nhiều), nên trông tối hơn — tạo sọc Mach.

---

**Câu 2:** Trong thí nghiệm "bóng xanh" của Land, vùng được chiếu chỉ bởi ánh sáng trắng trông có màu xanh lam vì:

A. Ánh sáng trắng thực chất chứa nhiều thành phần xanh lam hơn các màu khác

B. Não so sánh vùng đó với bối cảnh hồng xung quanh và suy luận rằng vùng đó "thiếu đỏ" → có màu xanh lam

C. Mắt mệt mỏi với màu hồng nên thấy màu bổ sung là xanh lam (afterimage)

D. Ánh sáng đỏ phản xạ từ vùng bên cạnh giao thoa với ánh sáng trắng tạo màu xanh lam

**Đáp án: B.** Đây là color constancy: não dùng bối cảnh (nền hồng) làm tham chiếu và tính tỉ số màu. Vùng trắng có thành phần đỏ thấp hơn bối cảnh hồng → não giải thích đây là bề mặt phản xạ màu xanh lam, không phải bề mặt trắng dưới ánh sáng hồng. Khác với afterimage (C) vì hiệu ứng xảy ra tức thì, không cần nhìn lâu.

---

**Câu 3:** Thuật toán Retinex của Land loại bỏ ảnh hưởng của chiếu sáng (illuminant) bằng cách:

A. Chia ảnh cho giá trị trung bình của toàn cảnh (Grey World)

B. Chọn pixel sáng nhất làm điểm trắng tham chiếu (Max RGB)

C. Tính tỉ số màu giữa các điểm kề nhau, vì tỉ số này không phụ thuộc vào phổ chiếu sáng

D. Lọc thông cao (high-pass filter) ảnh để loại bỏ thành phần chiếu sáng biến đổi chậm

**Đáp án: C.** Tỉ số $I_A(\lambda)/I_B(\lambda) = E(\lambda)S_A/[E(\lambda)S_B] = S_A/S_B$ — illuminant $E(\lambda)$ triệt tiêu hoàn toàn. Bằng cách tích lũy các tỉ số dọc theo đường nối nhiều điểm, thuật toán Retinex ước tính được màu thực $S$ của từng vùng.

---

**Câu hỏi tự luận:**

Trong hệ thống đo lường bề mặt của bạn dùng structured light (ánh sáng có hoa văn) để đo địa hình 3D của linh kiện cơ khí chính xác: khi chiếu hoa văn vạch trắng-đen lên bề mặt kim loại đánh bóng, bạn quan sát thấy các "vùng tối giả" (false dark bands) tại các cạnh sắc của linh kiện — dù camera đo được cường độ ánh sáng đều. Hiện tượng này liên hệ như thế nào với sọc Mach (Mach bands) trong thị giác sinh học? Và làm thế nào bạn có thể thiết kế bộ lọc xử lý ảnh để loại bỏ artifact này trong phép đo chiều cao bề mặt?

**Gợi ý trả lời:** "Vùng tối giả" tại cạnh linh kiện là Mach bands kỹ thuật số — xảy ra khi bộ lọc edge-enhancement trong firmware camera (thường bật mặc định) áp dụng lateral inhibition số học. Giải pháp: (1) Tắt edge enhancement trong camera settings; (2) Dùng bộ lọc Gaussian làm mịn (low-pass) trước khi phát hiện vị trí vân (fringe peak detection); (3) Hoặc dùng phase-shifting structured light thay vì binary pattern — ít nhạy cảm với Mach bands hơn vì thông tin pha được mã hóa trong tín hiệu sin liên tục.


---
*Exported from Feynman Bot*
