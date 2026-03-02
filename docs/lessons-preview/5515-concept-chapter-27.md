---
lesson_id: 5515
lesson_type: concept
approval_status: pending
exported_at: "2026-03-02T15:10:31.494839+00:00"
content_hash: 74f080ad041e
chapter_number: 27
chapter_title: Chapter 27
section_number: 2
section_title: 27–1Introduction
---
# ## Quang Học Hình Học và Thiết Kế Hệ Thống Quang Học Thực Tế

*Source: Chapter 27 - Chapter 27 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_27.html)*

## Quang Học Hình Học và Thiết Kế Hệ Thống Quang Học Thực Tế

### Mở Đầu: Tại Sao Camera Smartphone Lại Nhỏ Được?

Camera trên smartphone của bạn chứa hàng chục thấu kính tinh vi, kính lọc, và cảm biến trong không gian chưa đầy 1cm. Cách đây 50 năm, tính toán thiết kế như thế mất nhiều tháng. Ngày nay, máy tính làm việc đó trong vài giây. Nhưng nguyên lý quang học cơ bản — quang học hình học (geometrical optics) — vẫn là nền tảng. Hãy cùng khám phá tại sao.

### Quang Học Hình Học: Đơn Giản hay Phức Tạp?

Quang học hình học (geometrical optics) có một nghịch lý thú vị: nó vừa cực kỳ đơn giản, vừa cực kỳ phức tạp. Đơn giản ở cấp độ nhập môn — bạn chỉ cần vẽ tia sáng và áp dụng định luật Snell. Nhưng khi cần thiết kế thật sự — tính toán sai số của thấu kính (aberrations), tối ưu hóa profile bề mặt — bài toán trở nên cực kỳ phức tạp.

Giải pháp thực tế ngày nay: **ray tracing** bằng máy tính. Thay vì dùng công thức gần đúng, ta tính đường đi của từng tia sáng qua từng bề mặt quang học, bề mặt này sang bề mặt khác, cho đến khi ra khỏi hệ thống. Với hàng triệu tia, ta đánh giá chất lượng hệ thống. Đây là cách thiết kế thực tế trong công nghiệp.

### Gần Đúng Paraxial: Công Thức Hình Học Cơ Bản

Để xử lý gần đúng (paraxial approximation — tia gần trục), ta cần một công thức hình học đơn giản:

Xét tam giác có chiều cao nhỏ $h$ và đáy dài $d$. Cạnh huyền $s = \sqrt{d^2 + h^2}$. Sự chênh lệch:
$$\Delta = s - d = \sqrt{d^2 + h^2} - d \approx \frac{h^2}{2d}$$

(Dùng khai triển Taylor: $\sqrt{1+x} \approx 1 + x/2$ với $x = h^2/d^2 \ll 1$)

Đây là công thức đơn giản nhất mà quang học cần! Chỉ với $\Delta \approx h^2/2d$, ta có thể tính toán hội tụ của mọi hệ quang học paraxial.

### Bề Mặt Khúc Xạ Đơn: Phương Trình Gaussian

Bài toán cơ bản nhất: ánh sáng từ điểm $O$ (trong không khí) qua bề mặt cong vào môi trường chiết suất $n$, hội tụ tại $O'$. Điều kiện Fermat (thời gian bằng nhau) cho ra **phương trình ảnh Gaussian** cho bề mặt cầu:

$$\frac{n}{s'} - \frac{1}{s} = \frac{n-1}{R}$$

trong đó:
- $s$ = khoảng cách vật (object distance, âm nếu vật ở trước)
- $s'$ = khoảng cách ảnh (image distance)
- $R$ = bán kính cong bề mặt (dương nếu tâm cong ở phía ánh sáng truyền đi)
- $n$ = chiết suất môi trường sau bề mặt

Phép so sánh dễ nhớ: đây giống như bài toán mạch điện với điện trở song song $\frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2}$ — các nghịch đảo cộng lại.

### Ứng Dụng: Thiết Kế Hệ Quang Học trong Cảm Biến và Vũ Khí

Như một kỹ sư thiết kế hệ thống đo lường cấp micromet, bạn sẽ gặp quang học hình học ở khắp nơi:

**1. Collimator trong laser displacement sensor:**
Thấu kính collimator biến nguồn điểm thành chùm song song. Với phương trình Gaussian, đặt $s' \to \infty$ (ảnh ở vô cực → chùm song song):
$$\frac{1}{\infty} - \frac{1}{s} = \frac{n-1}{R} \Rightarrow s = \frac{R}{n-1} = f$$

Nguồn phải đặt tại tiêu điểm $f$ của collimator.

**2. Objective lens trong confocal microscope hoặc interferometer:**
Thấu kính objective hội tụ chùm laser xuống spot kích thước micromet. Độ phân giải và depth of focus quyết định phạm vi đo và độ chính xác.

**3. Hệ ngắm quang học (optical sight) trong vũ khí:**
Thấu kính objective thu ánh sáng từ mục tiêu xa, thấu kính eyepiece phóng đại ảnh. Nguyên lý hoàn toàn dựa trên phương trình Gaussian cho từng bề mặt.

### Di Sản Hamilton: Từ Quang Học đến Cơ Học Giải Tích

Lý thuyết quang học hình học tổng quát nhất được Hamilton phát triển, và điều kỳ diệu là nó lại **quan trọng hơn trong cơ học** hơn là trong quang học. Hàm đặc trưng Hamilton (Hamilton's characteristic function) trong quang học trực tiếp dẫn đến phương trình Hamilton-Jacobi trong cơ học, và từ đó đến cơ học lượng tử.

Là kỹ sư cơ điện tử, bạn có thể gặp cấu trúc toán học Hamilton trong:
- Lý thuyết điều khiển tối ưu (LQR, MPC)
- Bài toán quy hoạch động (dynamic programming)
- Phương trình trạng thái (state-space equations)

Tất cả đều bắt nguồn từ cùng một tư tưởng: nguyên lý cực trị toàn cục.

### Kết Luận

Quang học hình học là công cụ thực tế mạnh mẽ: đủ đơn giản để thiết kế nhanh, đủ chính xác cho hầu hết ứng dụng kỹ thuật. Chìa khóa là phương trình Gaussian và gần đúng paraxial. Khi cần độ chính xác cao hơn, ray tracing số học là giải pháp thực tế. Và tư tưởng Hamilton ẩn sau tất cả, kết nối quang học với cơ học và lý thuyết điều khiển.

---
*Exported from Feynman Bot*
