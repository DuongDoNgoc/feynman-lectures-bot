---
lesson_id: 5575
lesson_type: concept
approval_status: approved
exported_at: "2026-03-03T15:33:08.320418+00:00"
content_hash: 0c138a37211c
chapter_number: 33
chapter_title: Chapter 33
section_number: 8
section_title: 33–7Anomalous refraction
---
# ## Khúc xạ Bất thường: Khi Tinh thể Làm Nhân Đôi Ảnh

*Source: Chapter 33 - Chapter 33 (Section 8) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_33.html)*

## Khúc xạ Bất thường: Khi Tinh thể Làm Nhân Đôi Ảnh

### Câu hỏi mở đầu

Năm 1669, những thủy thủ đến từ Iceland mang về châu Âu một loại tinh thể kỳ lạ: nhìn qua nó, mọi vật đều hiện ra **hai ảnh**. Ngay cả Huygens — nhà vật lý thiên tài — cũng mất nhiều năm để giải thích hiện tượng này. Tại sao một miếng thủy tinh bình thường chỉ tạo một ảnh, nhưng tinh thể Iceland spar (canxit, $	ext{CaCO}_3$) lại tạo hai? Câu trả lời tiết lộ một trong những tính chất sâu sắc nhất của sóng ánh sáng.

---

### Ý tưởng cốt lõi: Hai tốc độ ánh sáng trong một tinh thể

Trong tinh thể dị hướng như Iceland spar, phân tử $	ext{CaCO}_3$ có cấu trúc không đối xứng — trục dài của phân tử tạo thành **trục quang học** (optic axis) của tinh thể. Điều này dẫn đến một hệ quả kỳ lạ: **tốc độ ánh sáng trong tinh thể phụ thuộc vào hướng phân cực**:

- **Tia thường** (ordinary ray, tia $o$): ánh sáng phân cực **vuông góc** với trục quang học, truyền với tốc độ $v_o = c/n_o$ — như mọi vật liệu đẳng hướng
- **Tia bất thường** (extraordinary ray, tia $e$): ánh sáng phân cực **song song** với trục quang học, truyền với tốc độ $v_e = c/n_e$ — khác với tia thường!

Do $n_o 
eq n_e$, hai thành phần phân cực vuông góc nhau của chùm tới **bị khúc xạ khác nhau** — và đi theo hai đường khác nhau qua tinh thể. Kết quả: **hai ảnh**.

---

### Phép so sánh: Robot đi trên địa hình khác nhau

Hãy tưởng tượng một robot có hai bánh xe: bánh trái và bánh phải. Khi chạy trên địa hình **đồng nhất** (đường bằng phẳng), cả hai bánh có cùng lực cản, robot đi thẳng. Nhưng khi địa hình **bất đối xứng** — bánh trái chạy trên cát, bánh phải chạy trên nhựa — hai bánh quay với tốc độ khác nhau, robot **tự động rẽ cong**.

Trong tinh thể Iceland spar, "địa hình" cho ánh sáng phân cực theo hai hướng là khác nhau — nên hai thành phần phân cực bị "đẩy" theo hai hướng khác nhau.

---

### Nguyên lý Huygens và mặt sóng elipsoid

Tia thường tuân thủ định luật Snell bình thường — mặt sóng là mặt cầu. Nhưng tia bất thường có tốc độ phụ thuộc vào góc so với trục quang học, nên **mặt sóng là elipsoid** (hình cầu dẹt hoặc kéo dài). Trong tinh thể calcite:

$$n_o = 1.658, \quad n_e = 1.486$$

Hai chỉ số khúc xạ khác nhau $\Delta n = n_o - n_e = 0.172$ — một trong những độ lưỡng chiết lớn nhất tự nhiên. Đây là lý do Iceland spar dễ thấy hiện tượng nhân đôi ảnh bằng mắt thường.

---

### Ứng dụng thực tế: Bộ chia chùm phân cực (PBS)

Đối với kỹ sư cơ điện tử làm việc với hệ thống đo lường chính xác, hiện tượng "kỳ lạ" của khúc xạ bất thường lại là nền tảng của những linh kiện quan trọng nhất:

**Lăng kính Wollaston**: Tạo từ hai lăng kính calcite ghép lại với trục quang học vuông góc nhau. Chùm sáng vào bị tách thành **hai chùm phân cực vuông góc**, phân kỳ theo các hướng khác nhau. Ứng dụng trong:
- Phân tích phân cực ánh sáng tán xạ (đo độ đục, kiểm tra bề mặt)
- Giao thoa kế vi phân (differential interference contrast microscopy — DIC) cho hiển vi chính xác

**Lăng kính Glan-Thompson**: Chỉ cho qua một trạng thái phân cực, phân cực kia bị phản xạ toàn phần trong. Dùng trong:
- Hệ thống laser phân cực cao công suất
- Thiết bị đo ellipsometry để kiểm tra màng mỏng trong sản xuất vi điện tử quân sự

**Tấm bước sóng (wave plate)**: Lát mỏng calcite cắt sao cho trục quang học song song bề mặt. Tia $o$ và $e$ đi cùng hướng nhưng với tốc độ khác nhau — tạo ra **hiệu pha tích lũy**:

$$\delta = rac{2\pi}{\lambda}(n_o - n_e)d$$

Chọn độ dày $d$ phù hợp để tạo $\delta = 90°$ (bản $\lambda/4$) hay $\delta = 180°$ (bản $\lambda/2$).

---

### Điểm mấu chốt

- Khúc xạ bất thường xảy ra vì tốc độ ánh sáng trong tinh thể dị hướng **phụ thuộc hướng phân cực**
- Hai chỉ số khúc xạ: $n_o$ (tia thường) và $n_e$ (tia bất thường) — $\Delta n = n_o - n_e$ gọi là độ lưỡng chiết
- Tia thường tuân thủ định luật Snell; tia bất thường truyền theo hướng không tuân thủ định luật Snell thông thường
- Ứng dụng kỹ thuật quan trọng: PBS (polarizing beam splitter), wave plate, lăng kính phân tích phân cực — thiết yếu trong đo lường chính xác cấp nm

---
*Exported from Feynman Bot*
