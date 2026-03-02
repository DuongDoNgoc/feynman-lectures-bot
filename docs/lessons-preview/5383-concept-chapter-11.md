---
lesson_id: 5383
lesson_type: concept
approval_status: approved
exported_at: "2026-03-02T15:10:28.015275+00:00"
content_hash: a4d2e06b503a
chapter_number: 11
chapter_title: Chapter 11
section_number: 1
section_title: 11Vectors
---
# ## Đối xứng trong Định luật Vật lý và Vectơ

*Source: Chapter 11 - Chapter 11 (Section 1) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_11.html)*

## Đối xứng trong Định luật Vật lý và Vectơ

Nếu bạn lắp đặt một hệ thống điều khiển chính xác ở Hà Nội, sau đó mang nguyên xi sang Tokyo lắp lại với cùng điều kiện ban đầu — liệu nó có hoạt động y chang không? Câu hỏi tưởng chừng hiển nhiên này lại chứa đựng một trong những nguyên lý sâu sắc nhất của vật lý: **đối xứng tịnh tiến** (translation symmetry).

### Đối xứng là gì?

Hermann Weyl định nghĩa: *một vật thể là đối xứng nếu có thể thực hiện một phép biến đổi nào đó lên nó mà trạng thái sau giống hệt trạng thái trước*. Trong vật lý, chúng ta hỏi: **các định luật vật lý có đối xứng không?**

Câu trả lời là **có**, và điều này không hiển nhiên chút nào. Định luật Newton $\mathbf{F} = m\mathbf{a}$ viết tại Hà Nội có hình thức y chang như viết tại Tokyo hay trên Mặt Trăng. Vị trí trong vũ trụ không ảnh hưởng đến dạng của định luật — miễn là bạn mang theo mọi thứ liên quan (nguồn lực, môi trường).

### Từ đối xứng đến Vectơ

Đối xứng này không chỉ là triết học — nó dẫn trực tiếp đến công cụ toán học gọi là **vectơ**. Tại sao?

Khi ta xoay hệ tọa độ (đổi cách đo), các định luật vật lý phải giữ nguyên dạng. Điều này đòi hỏi các đại lượng vật lý phải biến đổi theo một quy tắc nhất định khi đổi hệ tọa độ. Những đại lượng tuân theo quy tắc biến đổi này được gọi là **vectơ**.

Vận tốc $\mathbf{v}$, lực $\mathbf{F}$, gia tốc $\mathbf{a}$, độ dịch chuyển $\mathbf{r}$ — đều là vectơ. Nhiệt độ, khối lượng, năng lượng — là **vô hướng** (scalar), không có hướng.

### Vectơ — Một ký hiệu, Ba con số

Một bước di chuyển trong không gian cần **ba con số** $(x, y, z)$ để mô tả đầy đủ. Thay vì viết ba phương trình riêng lẻ:

$$mrac{d^2x}{dt^2} = F_x, \quad mrac{d^2y}{dt^2} = F_y, \quad mrac{d^2z}{dt^2} = F_z$$

Ta viết gọn thành **một** phương trình vectơ:

$$m\mathbf{a} = \mathbf{F}$$

Cái hay là phương trình này đúng trong **mọi hệ tọa độ**. Không cần viết lại khi xoay trục. Đây chính là sức mạnh của ký hiệu vectơ — nó nắm bắt tính đối xứng của định luật vật lý.

### Phép so sánh cho kỹ sư cơ điện tử

Trong hệ thống điều khiển robot 6 bậc tự do, khi bạn lập trình quỹ đạo end-effector, phần mềm sử dụng **ma trận chuyển đổi tọa độ** (rotation matrix $R$) để chuyển đổi vectơ từ frame này sang frame khác. Bản chất toán học của phép chuyển đổi này chính là điều Feynman đang mô tả: cùng một vectơ vật lý $\mathbf{r}$ được biểu diễn bằng bộ số $(x,y,z)$ trong frame A và $(x',y',z')$ trong frame B, nhưng **thực thể vật lý là như nhau**.

Laser interferometer đo dịch chuyển tuyến tính theo một trục. Nếu đầu đo bị lệch góc $\theta$ so với trục chuyển động, số đọc thực ra là $d\cos\theta$ — hình chiếu của vectơ dịch chuyển lên trục đo. Hiểu vectơ giúp bạn hiệu chỉnh sai số này.

### Tích vô hướng — Đại lượng bất biến

Từ hai vectơ, ta tạo ra được một **vô hướng** (không phụ thuộc hệ tọa độ):

$$\mathbf{a} \cdot \mathbf{b} = a_x b_x + a_y b_y + a_z b_z = |\mathbf{a}||\mathbf{b}|\cos\theta$$

Công $W = \mathbf{F} \cdot \mathbf{d}$ là ví dụ điển hình: đây là một số thực, không phụ thuộc cách ta chọn trục tọa độ.

### Điểm mấu chốt

- **Đối xứng tịnh tiến**: định luật vật lý có cùng dạng ở mọi vị trí không gian
- **Vectơ** là ngôn ngữ toán học nắm bắt tính đối xứng đó — một ký hiệu thay thế ba phương trình
- **Phương trình vectơ** $m\mathbf{a} = \mathbf{F}$ đúng trong mọi hệ tọa độ, không cần viết lại khi xoay trục
- **Tích vô hướng** $\mathbf{a}\cdot\mathbf{b}$ là đại lượng bất biến — giống như số đọc encoder không phụ thuộc cách đặt tên trục

---
*Exported from Feynman Bot*
