---
lesson_id: 5458
lesson_type: concept
approval_status: approved
exported_at: "2026-03-02T15:10:29.938637+00:00"
content_hash: 9fdbf4a87e26
chapter_number: 19
chapter_title: Chapter 19
section_number: 3
section_title: 19–2Locating the center of mass
---
# ## Định Lý Pappus và Moment Quán Tính

*Source: Chapter 19 - Chapter 19 (Section 3) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_19.html)*

## Định Lý Pappus và Moment Quán Tính

Bạn có bao giờ tự hỏi: tại sao khi thiết kế một bánh đà (flywheel) cho hệ thống truyền động, kỹ sư lại chú trọng đến hình dạng tiết diện hơn là chỉ tổng khối lượng? Hay tại sao một trục quay rỗng lại có thể tích trữ năng lượng quay hiệu quả hơn một trục đặc cùng khối lượng? Câu trả lời nằm ở một khái niệm hình học thanh lịch: **định lý Pappus** và **moment quán tính** (moment of inertia).

### Định Lý Pappus — Hình Học Phục Vụ Cơ Học

Hãy tưởng tượng bạn lấy một hình phẳng bất kỳ — ví dụ tam giác vuông có diện tích $A$ — và quay nó quanh một trục nằm ngoài hình đó. Khối rắn tạo thành có thể tích bằng bao nhiêu? Bạn không cần tích phân phức tạp: **định lý Pappus** phát biểu rằng thể tích bằng diện tích nhân với quãng đường mà *khối tâm* của hình đi được:

$$V = A \cdot D$$

trong đó $D = 2\pi x$ là chu vi đường tròn mà khối tâm (ở khoảng cách $x$ tính từ trục) quét qua.

Đây là một ví dụ tuyệt vời về cách hình học và cơ học đan xen nhau. Để tìm thể tích hình nón có đường kính đáy $D$ và chiều cao $H$: tam giác vuông có diện tích $\tfrac{1}{2}HD$ được quay quanh trục đối xứng. Khối tâm của tam giác vuông nằm tại $x = D/3$ tính từ trục. Áp dụng định lý Pappus:

$$V_{\text{nón}} = \tfrac{1}{2}HD \times 2\pi \cdot \frac{D}{3} = \frac{\pi D^2 H}{3}$$

Kết quả này khớp hoàn toàn với công thức quen thuộc $V = \frac{1}{3}\pi r^2 h$. Thay vì tích phân, ta chỉ cần biết vị trí khối tâm!

### Ngược Lại: Tìm Khối Tâm Từ Thể Tích Đã Biết

Định lý Pappus còn có thể đảo ngược. Nếu ta đã biết thể tích của vật (từ công thức hoặc thực nghiệm) và diện tích tiết diện, ta có thể tìm ngược vị trí khối tâm. Đây là "mẹo" kỹ thuật rất thực dụng: trong thiết kế CAD/CAM, phần mềm thường tính thể tích trực tiếp, và từ đó kỹ sư có thể suy ra khối tâm của tiết diện phức tạp mà không cần giải tích phân thủ công.

Ví dụ: nửa hình tròn (bán cầu) có diện tích $\dfrac{\pi r^2}{2}$. Khi quay quanh đường kính để tạo hình cầu có thể tích $\dfrac{4}{3}\pi r^3$, ta tìm được vị trí khối tâm của nửa hình tròn:

$$x_{\text{CM}} = \frac{V}{A \cdot 2\pi} = \frac{\frac{4}{3}\pi r^3}{\frac{\pi r^2}{2} \cdot 2\pi} = \frac{4r}{3\pi} \approx 0.424r$$

### Moment Quán Tính — Đại Lượng Quyết Định Hành Vi Quay

Sau khi nắm vị trí khối tâm, bước tiếp theo trong thiết kế hệ truyền động quay là xác định **moment quán tính** $I$ — đại lượng đo mức độ "lười" của vật thể khi bị thay đổi trạng thái quay. Công thức tổng quát:

$$I = \sum_i m_i r_i^2$$

trong đó $r_i$ là khoảng cách từ phần tử khối lượng $m_i$ đến trục quay. Phần tử càng xa trục, đóng góp của nó vào $I$ càng lớn theo bình phương khoảng cách.

**Phép loại suy kỹ thuật:** Trong hệ cơ điện tử, moment quán tính $I$ tương tự như điện dung $C$ trong mạch điện. Điện dung lưu trữ năng lượng dưới dạng điện trường ($E = \tfrac{1}{2}CV^2$), còn vật quay lưu trữ năng lượng động năng quay ($E_{\text{quay}} = \tfrac{1}{2}I\omega^2$). Muốn tăng tốc nhanh (tương tự nạp điện nhanh), cần giảm $I$ (hoặc $C$). Muốn duy trì tốc độ ổn định (lọc nhiễu), cần tăng $I$ (hoặc $C$). Đây chính là lý do bánh đà (flywheel) trong động cơ đốt trong hay hệ năng lượng tái tạo có $I$ lớn — để "san phẳng" biến động tốc độ.

### Định Lý Trục Song Song (Parallel Axis Theorem)

Một kết quả quan trọng giúp kỹ sư tính $I$ khi trục quay không đi qua khối tâm: nếu biết $I_{\text{CM}}$ (moment quán tính qua khối tâm) và trục mới cách khối tâm một khoảng $d$, thì:

$$I = I_{\text{CM}} + Md^2$$

Trong thiết kế cánh tay robot hoặc gimbal (hệ giữ thăng bằng camera/vũ khí), khi trục motor không trùng với khối tâm của tải, số hạng $Md^2$ thường chiếm phần lớn tổng $I$. Kỹ sư phải bố trí cơ học sao cho trục quay càng gần khối tâm càng tốt để giảm moment quán tính hiệu dụng — từ đó giảm yêu cầu torque của motor và cải thiện độ đáp ứng điều khiển.

**Điểm mấu chốt:**
- Định lý Pappus biến bài toán tích phân thể tích thành bài toán tìm khối tâm đơn giản: $V = A \cdot 2\pi x_{\text{CM}}$.
- Moment quán tính $I = \sum m_i r_i^2$ quyết định "sức ì" quay — phần tử khối lượng xa trục đóng góp theo bình phương khoảng cách.
- Định lý trục song song $I = I_{\text{CM}} + Md^2$ là công cụ thực tiễn để tính $I$ khi trục quay lệch khỏi khối tâm.
- Trong cơ điện tử, tối ưu hóa $I$ trực tiếp ảnh hưởng đến torque motor, độ đáp ứng servo và năng lượng lưu trữ trong bánh đà.

---
*Exported from Feynman Bot*
