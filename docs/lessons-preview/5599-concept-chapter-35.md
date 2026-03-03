---
lesson_id: 5599
lesson_type: concept
approval_status: pending
exported_at: "2026-03-03T15:33:08.867440+00:00"
content_hash: c72dedc3ed16
chapter_number: 35
chapter_title: Chapter 35
section_number: 7
section_title: 35–6Physiochemistry of color vision
---
# ## Visual Purple và Bí Ẩn Sắc Tố Màu Của Mắt

*Source: Chapter 35 - Chapter 35 (Section 7) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_35.html)*

## Visual Purple và Bí Ẩn Sắc Tố Màu Của Mắt

Bạn đã bao giờ tự hỏi: tại sao mắt người cần vài phút để "quen bóng tối" khi đi từ nơi sáng vào phòng tối? Hay tại sao con mèo nhìn ban đêm tốt hơn người? Câu trả lời nằm trong một sắc tố kỳ diệu có màu tím — **visual purple (rhodopsin)** — và cơ chế phân tử của nó.

### Sắc tố thị giác: Nền tảng hóa học của thị giác

Võng mạc (retina) của mắt chứa hai loại tế bào cảm quang: **tế bào que (rods)** — hoạt động trong điều kiện ánh sáng yếu, không phân biệt màu; và **tế bào nón (cones)** — chuyên về màu sắc, cần ánh sáng đủ mạnh.

Năm 1877, nhà khoa học người Đức Boll phát hiện rằng sắc tố chính trong tế bào que là **visual purple (rhodopsin)** — một protein kết hợp với retinal (dẫn xuất vitamin A). Điều đặc biệt: đường cong hấp thụ ánh sáng của visual purple khớp chính xác với đường cong nhạy sáng của mắt trong bóng tối (dark-adapted eye):

$$S(\lambda) \approx A(\lambda)_{\text{visual purple}}$$

trong đó $S(\lambda)$ là độ nhạy của mắt tối thích nghi tại bước sóng $\lambda$, và $A(\lambda)$ là hệ số hấp thụ của visual purple. Sự trùng khớp đẹp đẽ này chứng tỏ visual purple chính là sắc tố ta dùng để nhìn trong bóng tối.

### Cơ chế tẩy trắng (bleaching) — chìa khóa đo lường sắc tố

Khi ánh sáng chiếu vào visual purple, phân tử retinal thay đổi cấu hình từ 11-cis sang all-trans, "tẩy trắng" (bleach) sắc tố — đó là lý do mắt mất độ nhạy khi vào ánh sáng mạnh. Quá trình tái tổng hợp (regeneration) trong bóng tối mất vài phút — giải thích hiện tượng "mắt quen bóng tối".

### Kỹ thuật Rushton: Đo sắc tố ngay trong mắt sống

Sắc tố màu của tế bào nón (cones) chưa bao giờ được chiết xuất thành công vào ống nghiệm — hàm lượng quá ít. Đây là vấn đề kỹ thuật đo lường đặt ra thách thức tương tự như đo lường các thông số cực nhỏ trong cảm biến cơ điện tử.

Năm 1958, W.A.H. Rushton giải quyết bằng cách **đo trực tiếp trong mắt sống** dùng **ophthalmoscope** (kính soi đáy mắt):

1. Chiếu ánh sáng qua thủy tinh thể vào võng mạc
2. Ánh sáng đi qua lớp sắc tố tế bào nón, phản xạ ở lớp nền, đi ngược lại qua sắc tố lần nữa
3. Đo phổ ánh sáng phản xạ: hệ số phản xạ $R(\lambda)$ liên quan đến độ hấp thụ $A(\lambda)$ theo: $R(\lambda) \approx e^{-2A(\lambda)d}$

Chiều dày $d$ của lớp sắc tố rất nhỏ, nhưng ánh sáng đi **hai lần** qua (khử và phản xạ), tăng gấp đôi tín hiệu — một trick quang học tinh tế.

**Loại bỏ nhiễu nền (background subtraction):** Võng mạc có màu cam hồng vì máu và mô nền. Rushton giải quyết bằng cách **tẩy trắng chọn lọc**: chiếu ánh sáng đỏ (chỉ tẩy trắng sắc tố bình thường, không ảnh hưởng mắt protanope — người mù màu đỏ). Đo sự **thay đổi** phổ trước và sau tẩy trắng — phần thay đổi chính xác là chữ ký của sắc tố đó.

Đây chính là nguyên tắc **differential measurement** — giống như kỹ thuật đo lường vi sai (differential sensing) trong cảm biến áp suất, gia tốc kế MEMS: đo hiệu số giữa hai trạng thái để loại bỏ offset và nhiễu chung.

### So sánh với cảm biến quang học trong cơ điện tử

Kỹ thuật đo của Rushton giống hệt nguyên lý **reflectance spectroscopy** dùng trong cảm biến màu công nghiệp:
- Nguồn sáng → mẫu → detector đo phổ phản xạ
- Chuẩn hóa bằng mẫu trắng (white reference) — tương đương "mắt không có sắc tố" của Rushton
- Đo **sự thay đổi** để loại bỏ ảnh hưởng môi trường

### Kết quả và giới hạn của khoa học

Rushton tìm được hai sắc tố trong mắt bình thường:
- **Erythrolabe** (đỏ): đỉnh hấp thụ ~560 nm
- **Chlorolabe** (xanh lá): đỉnh ~530 nm

Sắc tố xanh lam (cyanolabe, ~420 nm) khó đo hơn do số lượng tế bào nón xanh lam ít nhất.

Tuy nhiên, nghiên cứu mới nhất với người mù màu deuteranope (thiếu sắc tố xanh lá) không luôn luôn cho kết quả rõ ràng — khoa học về màu sắc vẫn còn bí ẩn.

### Điểm mấu chốt

Visual purple (rhodopsin) là sắc tố của tế bào que, chịu trách nhiệm thị giác ban đêm, và đã được xác nhận bằng sự trùng khớp hoàn hảo giữa phổ hấp thụ và đường cong nhạy sáng. Sắc tố màu của tế bào nón (tạo ra màu sắc) quá ít để chiết xuất, nhưng Rushton đã dùng kỹ thuật đo phản xạ vi sai in-vivo — một phương pháp đo lường phi xâm lấn kiểu mẫu — để lần đầu tiên "nhìn thấy" chúng.

---
*Exported from Feynman Bot*
