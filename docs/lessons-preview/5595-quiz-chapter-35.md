---
lesson_id: 5595
lesson_type: quiz
approval_status: pending
exported_at: "2026-03-03T15:33:08.805675+00:00"
content_hash: 328640eb6aae
chapter_number: 35
chapter_title: Chapter 35
section_number: 4
section_title: 35–3Measuring the color sensation
---
# ## Quiz: Phối Màu và Không Gian Màu CIE

*Source: Chapter 35 - Chapter 35 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_35.html)*

## Quiz: Phối Màu và Không Gian Màu CIE

**Câu 1 (Trắc nghiệm):** Khi trộn ánh sáng đỏ (R) và xanh lá (G) với nhau theo tỉ lệ thích hợp, ta thu được cảm giác màu gì?

A. Màu nâu sẫm
B. Màu vàng
C. Màu tím
D. Màu trắng

**Đáp án: B**
Giải thích: Đây là phối màu cộng (additive mixing). Ánh sáng đỏ kích thích chủ yếu L-cone, ánh sáng xanh lá kích thích M-cone. Khi trộn theo tỉ lệ đúng, não cảm nhận kết hợp L+M tương tự ánh sáng đơn sắc ~580 nm, cho cảm giác màu vàng. Trái ngược với phối màu trừ (sơn/mực in) trong đó đỏ + xanh lá = màu tối.

---

**Câu 2 (Trắc nghiệm):** Trên biểu đồ chromaticity CIE, nếu màu A ở điểm $(x_A, y_A)$ và màu B ở $(x_B, y_B)$, hỗn hợp $1/3 A + 2/3 B$ nằm ở đâu?

A. Ở điểm trung điểm AB
B. Ở điểm cách A một phần ba đoạn AB
C. Ở điểm cách B một phần ba đoạn AB
D. Ngoài đoạn AB

**Đáp án: C**
Giải thích: Theo quy tắc cánh tay đòn (lever rule), điểm hỗn hợp $\alpha A + (1-\alpha) B$ nằm ở vị trí cách B một phần $(1-\alpha) = 1/3$ và cách A một phần $\alpha = 2/3$ — tức là nằm ở $1/3$ đoạn từ B về phía A, hay gần B hơn. Phần tỉ lệ lớn hơn (2/3 màu B) kéo điểm hỗn hợp gần màu B hơn.

---

**Câu 3 (Trắc nghiệm):** Tại sao không có bộ ba màu chủ đạo R, G, B nào có thể tái tạo 100% màu mà mắt người có thể nhìn thấy?

A. Vì mắt người có bốn loại tế bào nón, nên cần bốn màu chủ đạo
B. Vì một số màu phổ thuần túy nằm ngoài tam giác trong biểu đồ chromaticity và cần hệ số âm
C. Vì ánh sáng R, G, B can nhiễu lẫn nhau khi chiếu đồng thời
D. Vì mắt người không phân biệt được màu phổ thuần túy

**Đáp án: B**
Giải thích: Trên biểu đồ chromaticity, gamut của bộ ba màu chủ đạo là tam giác nội tiếp trong spectral locus (đường cong của màu phổ thuần túy). Vì spectral locus là đường cong lồi không phải tam giác, luôn có phần của nó nằm ngoài tam giác. Màu nằm ngoài tam giác cần hệ số âm — nghĩa là phải thêm vào phía màu cần tái tạo, không thể làm bằng cộng ánh sáng đơn giản.

---

**Câu 4 (Tự luận):** Trong hệ thống hiển thị HMI (Human-Machine Interface) cho robot hàn (welding robot) của bạn, bạn cần hiển thị cảnh báo màu "đỏ tươi" và "cam" để phân biệt hai mức cảnh báo khác nhau. Dựa trên nguyên lý không gian màu, hãy phân tích: (a) làm thế nào để đảm bảo hai màu đủ khác biệt về mặt tri giác (perceptually distinct), và (b) cách kiểm tra điều này bằng số liệu định lượng.

**Gợi ý đáp án:**

(a) Hai màu cần có khoảng cách đủ lớn trong không gian màu tri giác đều (perceptually uniform color space) như CIELab. Trong CIELab, trục $a^*$ đặc trưng cho sắc đỏ-xanh lá, trục $b^*$ cho sắc vàng-xanh lam, $L^*$ cho độ sáng. Màu đỏ tươi cần $a^*$ cao và $b^*$ gần 0, còn màu cam cần cả $a^*$ và $b^*$ đều dương. Để đảm bảo phân biệt được trong điều kiện ánh sáng nhà máy (có thể bị nhòe do bụi hay góc nhìn), nên chọn $\Delta E_{00} > 5$ giữa hai màu.

(b) Kiểm tra định lượng: (1) Đo tọa độ CIELab của hai màu hiển thị trên màn hình HMI thực tế bằng colorimeter hoặc spectrophotometer cầm tay; (2) Tính $\Delta E_{00}$ theo công thức CIEDE2000; (3) Nếu $\Delta E_{00} < 3$: khó phân biệt trong điều kiện khắc nghiệt; (4) Kiểm tra thêm với người mù màu đỏ-xanh lá (8% nam giới) — nên tránh phân biệt chỉ bằng đỏ vs xanh lá; (5) Thêm ký hiệu hình học (tam giác vs tròn) kết hợp màu sắc để tăng tính phân biệt.


---
*Exported from Feynman Bot*
