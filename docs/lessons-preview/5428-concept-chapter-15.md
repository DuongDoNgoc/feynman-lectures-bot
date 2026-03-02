---
lesson_id: 5428
lesson_type: concept
approval_status: approved
exported_at: "2026-03-02T15:10:29.187756+00:00"
content_hash: d2bd4d9a5385
chapter_number: 15
chapter_title: Chapter 15
section_number: 6
section_title: 15–5The Lorentz contraction
---
# ## Co Lorentz và Sự Thất Bại của Đồng Thời Tuyệt Đối

*Source: Chapter 15 - Chapter 15 (Section 6) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_15.html)*

## Co Lorentz và Sự Thất Bại của Đồng Thời Tuyệt Đối

### Đặt vấn đề

Bạn đang hiệu chỉnh một hệ thống đo lường gồm hai cảm biến vị trí đặt cách nhau 10 mét, cả hai kết nối với cùng một bộ đồng hồ trung tâm qua cáp dài. Bạn gửi xung điện từ trung tâm để đồng bộ hoá hai cảm biến. Câu hỏi: liệu tín hiệu có đến hai cảm biến cùng lúc hay không? Câu trả lời phụ thuộc vào... hệ quy chiếu của người quan sát. Đây chính là trái tim của thuyết tương đối Einstein.

### Phép biến đổi Lorentz — Từ Joe nhìn Moe

Hãy tưởng tượng hai hệ quy chiếu: hệ $S$ (tọa độ $(x, y, z, t)$, gọi là "Joe đứng yên") và hệ $S'$ (tọa độ $(x', y', z', t')$, gọi là "Moe đang chuyển động" với vận tốc $u$ theo trục $x$).

Câu hỏi đặt ra: nếu Moe dùng thước đo chiều dài $x'$, Joe nhìn thước đó như thế nào?

Trong thí nghiệm Michelson-Morley, ta thấy nhánh ngang $BC$ không thay đổi chiều dài theo nguyên lý tương đối. Nhưng để kết quả bằng không (null result), nhánh dọc $BE$ phải co lại theo hệ số $\sqrt{1-u^2/c^2}$. Đây là co Lorentz (Lorentz contraction).

Moe đặt thước đo $x'$ lần, nghĩ rằng khoảng cách là $x'$ mét. Nhưng theo Joe, thước của Moe đã bị co lại — "thước thật" chỉ dài $x'\sqrt{1-u^2/c^2}$ mét. Cộng thêm khoảng cách $ut$ mà hệ $S'$ đã dịch chuyển xa hệ $S$:

$$x' = rac{x - ut}{\sqrt{1-u^2/c^2}}$$

Đây là phương trình đầu tiên của **phép biến đổi Lorentz** — phương trình kết nối cách Joe và Moe đo cùng một sự kiện vật lý.

### Hiệu ứng gây sốc: Sự Đồng Thời Tương Đối

Phần thú vị hơn nằm ở phương trình thứ tư của biến đổi Lorentz — biến đổi thời gian. Nếu Moe trong hệ $S'$ quan sát hai sự kiện xảy ra ở hai vị trí khác nhau nhưng cùng thời điểm, Joe trong hệ $S$ sẽ đo được hai khoảnh khắc thời gian KHÁC nhau:

$$t_2' - t_1' = rac{u(x_1 - x_2)/c^2}{\sqrt{1-u^2/c^2}}$$

Đây là **"failure of simultaneity at a distance"** — sự thất bại của đồng thời ở khoảng cách.

### Phép so sánh với kỹ sư cơ điện tử

Hãy tưởng tượng bạn thiết kế hệ thống hai encoder đặt ở hai đầu của băng tải đang chạy nhanh. Bạn gửi tín hiệu đồng bộ từ điểm giữa để cả hai encoder ghi lại vị trí "cùng lúc". Với người đứng yên nhìn vào, tín hiệu đến hai encoder đồng thời — hoàn hảo. Nhưng nếu có một người quan sát đang chuyển động nhanh dọc theo băng tải, họ sẽ thấy tín hiệu đến encoder đầu này trước encoder kia. "Cùng lúc" trở thành khái niệm phụ thuộc vào người quan sát.

Tất nhiên ở vận tốc của băng tải công nghiệp (dù nhanh đến đâu), hiệu ứng này hoàn toàn không đáng kể — $u^2/c^2$ cực nhỏ. Nhưng nguyên lý này giải thích tại sao trong GPS (vệ tinh chuyển động ~14,000 km/h), phải hiệu chỉnh cả thuyết tương đối hẹp lẫn thuyết tương đối rộng để đạt độ chính xác mét.

### Đồng hồ trên tàu vũ trụ — minh họa tư duy

Moe trên tàu vũ trụ đặt hai đồng hồ ở hai đầu tàu, đồng bộ hoá bằng cách gửi xung ánh sáng từ điểm giữa. Theo Moe, tín hiệu đến cùng lúc — hai đồng hồ đồng bộ. Nhưng Joe đứng ngoài thấy: tàu đang tiến về phía trước nên đồng hồ phía trước "chạy trốn" khỏi tín hiệu ánh sáng, còn đồng hồ phía sau "lao vào" tín hiệu. Tín hiệu đến đồng hồ sau trước. Joe kết luận hai đồng hồ của Moe không đồng bộ!

Ai đúng? Cả hai đều đúng — trong hệ quy chiếu của riêng mình. Không có "thời gian tuyệt đối" tồn tại độc lập với người quan sát.

### Điểm mấu chốt

- **Co Lorentz**: Thước trong hệ chuyển động bị co lại theo hệ số $\sqrt{1-u^2/c^2}$ theo hướng chuyển động — đây không phải ảo giác quang học mà là thực tế vật lý được đo được.
- **Đồng thời tương đối**: Hai sự kiện xảy ra đồng thời trong một hệ quy chiếu có thể không đồng thời trong hệ quy chiếu khác — hiệu thời gian tỉ lệ với khoảng cách không gian và vận tốc tương đối.
- Phép biến đổi Lorentz $x' = (x-ut)/\sqrt{1-u^2/c^2}$ là phương trình "dịch ngôn ngữ" giữa hai hệ quy chiếu — tương tự như ma trận biến đổi tọa độ trong robotics, nhưng có thêm chiều thời gian được trộn vào không gian.

---
*Exported from Feynman Bot*
