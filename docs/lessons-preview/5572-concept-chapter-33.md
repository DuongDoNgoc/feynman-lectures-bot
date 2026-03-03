---
lesson_id: 5572
lesson_type: concept
approval_status: approved
exported_at: "2026-03-03T15:33:08.261399+00:00"
content_hash: d0e01e8d6a3d
chapter_number: 33
chapter_title: Chapter 33
section_number: 5
section_title: 33–4Polarizers
---
# ## Định luật Malus và Tính Lưỡng Sắc: Khi Vật liệu "Ăn" Ánh sáng theo Hướng

*Source: Chapter 33 - Chapter 33 (Section 5) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_33.html)*

## Định luật Malus và Tính Lưỡng Sắc: Khi Vật liệu "Ăn" Ánh sáng theo Hướng

### Câu hỏi mở đầu

Tại sao kính mắt phân cực (polarized sunglasses) loại bỏ được ánh sáng chói phản chiếu từ mặt đường hay mặt nước, nhưng kính thường thì không? Câu trả lời nằm ở một tính chất kỳ diệu của một số vật liệu: chúng **hấp thụ ánh sáng theo hướng nhưng không hấp thụ theo hướng kia** — hiện tượng gọi là **lưỡng sắc** (dichroism).

---

### Ý tưởng cốt lõi: Vật liệu lưỡng sắc

Tourmaline và vật liệu polaroid đều có cấu trúc tinh thể hay phân tử sắp xếp theo một trục ưu tiên. Khi ánh sáng đến, điện tử bị buộc dao động:
- Theo hướng **vuông góc trục truyền qua** (pass axis): điện tử dao động nhưng **không** bị hấp thụ nhiều
- Theo hướng **song song trục hấp thụ**: điện tử dao động và **bị hấp thụ mạnh**

Kết quả: chỉ có thành phần ánh sáng theo hướng "cho qua" mới thoát ra phía kia.

---

### Định luật Malus

Khi ánh sáng phân cực tuyến tính với biên độ $E_0$ chiếu vào tấm polaroid, góc giữa hướng phân cực và trục cho qua là $	heta$. Biên độ đi qua chỉ là thành phần chiếu:

$$E_{ra} = E_0 \cos	heta$$

Cường độ ánh sáng tỉ lệ với bình phương biên độ, nên:

$$oxed{I_{ra} = I_0 \cos^2	heta}$$

Đây là **Định luật Malus** (Malus's Law). Kết quả trực quan: ở $	heta = 0°$, $I_{ra} = I_0$ (qua hoàn toàn); ở $	heta = 90°$, $I_{ra} = 0$ (bị chặn hoàn toàn).

---

### Phép so sánh: Cửa lọc tín hiệu

Hãy nghĩ đến một hàng rào gồm những thanh gỗ dọc đứng, cách đều nhau. Một sóng trên dây có thể qua hàng rào hay không phụ thuộc vào **hướng dao động** của sóng:
- Sóng dao động dọc (song song hàng rào): qua dễ
- Sóng dao động ngang (vuông góc hàng rào): bị chặn

Polaroid hoạt động tương tự — nhưng ở cấp độ phân tử với ánh sáng điện từ.

**Nghịch lý thú vị**: Nếu đặt hai tấm polaroid vuông góc nhau, không có ánh sáng đi qua. Nhưng nếu **thêm một tấm thứ ba** vào giữa, nghiêng $45°$, ánh sáng lại **xuất hiện**! Tấm giữa đóng vai "cầu nối" — biến đổi hướng phân cực từng bước. Đây là minh chứng cho thấy phân cực là **tính chất vector, không phải vô hướng**.

---

### Ứng dụng: Màn hình LCD và cảm biến góc

Trong công việc thiết kế hệ thống cơ điện tử và đo lường, bạn gặp polaroid mọi nơi:

**Màn hình LCD**: Cấu tạo gồm hai tấm polaroid vuông góc nhau, kẹp lớp tinh thể lỏng (liquid crystal) ở giữa. Điện áp điều khiển góc quay tinh thể lỏng, thay đổi trạng thái phân cực ánh sáng đi qua, từ đó kiểm soát cường độ ánh sáng thoát ra (sáng/tối). Mỗi pixel là một "van ánh sáng" dùng hiệu ứng phân cực.

**Cảm biến đo góc dùng phân cực**: Trong hệ thống đo góc nghiêng (tilt sensor) cho vũ khí hay máy đo tọa độ, có thể dùng hai tấm polaroid — một cố định, một gắn với vật thể đo. Đo cường độ ánh sáng qua hệ thống, suy ra góc $	heta$ từ $I = I_0\cos^2	heta$.

**Kính chắn glare trong hệ thống ngắm bắn**: Ánh sáng phản chiếu từ bề mặt nằm ngang (mặt đất, nước) thường phân cực song song với bề mặt. Kính phân cực với trục đứng chặn lại thành phần này, giảm chói lóa — ứng dụng trực tiếp trong thiết kế kính ngắm quân sự.

---

### Điểm mấu chốt

- Vật liệu lưỡng sắc (polaroid, tourmaline) hấp thụ ánh sáng chọn lọc theo hướng phân cực — chỉ cho thành phần theo trục cho qua đi qua
- **Định luật Malus**: $I = I_0\cos^2	heta$ — cường độ phụ thuộc cosin bình phương của góc giữa hướng phân cực và trục cho qua
- Nghịch lý "ba polaroid": thêm tấm trung gian vào hệ hai polaroid vuông góc làm xuất hiện ánh sáng — phân cực là tính chất vector
- Ứng dụng thực tế: LCD, cảm biến góc phân cực, kính ngắm chống chói — đều dựa trên định luật Malus

---
*Exported from Feynman Bot*
