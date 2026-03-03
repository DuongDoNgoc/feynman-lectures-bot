---
lesson_id: 5605
lesson_type: concept
approval_status: pending
exported_at: "2026-03-03T15:33:08.961320+00:00"
content_hash: f83fa2566d33
chapter_number: 36
chapter_title: Chapter 36
section_number: 3
section_title: 36–2The physiology of the eye
---
# ## Mắt Người — Hệ Thống Quang Học Tinh Xảo Nhất Mà Tự Nhiên Tạo Ra

*Source: Chapter 36 - Chapter 36 (Section 3) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_36.html)*

## Mắt Người — Hệ Thống Quang Học Tinh Xảo Nhất Mà Tự Nhiên Tạo Ra

Bạn có biết rằng thấu kính trong mắt người không đồng nhất — chỉ số khúc xạ thay đổi từ 1.40 ở tâm đến 1.38 ở rìa? Và giác mạc (cornea) không phải hình cầu hoàn hảo — nó được "làm phẳng" ở rìa để giảm quang sai cầu? Tự nhiên đã thiết kế một hệ thống quang học tối ưu hàng triệu năm trước khi con người phát minh ra thấu kính.

### Cấu trúc ba lớp tế bào thần kinh võng mạc

Võng mạc không đơn giản là một lớp tế bào cảm quang. Nó gồm ba lớp xử lý nối tiếp nhau:

1. **Photoreceptors (tế bào quang):** Tế bào que (120 triệu) và nón (6 triệu) hấp thụ photon, chuyển thành tín hiệu điện hóa
2. **Bipolar cells (tế bào lưỡng cực):** Nhận tín hiệu từ một hoặc vài tế bào quang, truyền đến lớp tiếp theo
3. **Ganglion cells (tế bào hạch):** Kết hợp từ nhiều bipolar cells, tạo xung thần kinh (action potentials) truyền qua dây thần kinh thị giác

**Tổng số ganglion cells:** ~1 triệu — dây thần kinh thị giác có 1 triệu sợi. So với 126 triệu photoreceptors, đây là mức nén thông tin 126:1 ngay tại võng mạc!

Các kết nối ngang (horizontal cells, amacrine cells) cho phép các tế bào trong cùng lớp giao tiếp — đây là cơ sở của phát hiện cạnh (edge detection) và các tính toán không gian cục bộ.

### Hệ thống quang học mắt — So sánh với thiết kế quang học kỹ thuật

**Giác mạc (cornea) — thấu kính chính:**

Giác mạc thực hiện ~70% sức hội tụ của mắt. Nó hoạt động vì sự chênh lệch chỉ số khúc xạ: không khí ($n=1.0$) → giác mạc ($n \approx 1.37$). Dưới nước, chỉ số nước ($n=1.33$) gần với giác mạc → không còn khúc xạ đủ mạnh → mắt không lấy nét được.

**Thủy tinh thể — thấu kính tinh chỉnh với gradient index:**

$$n(r) = n_{center} - \Delta n \cdot \left(\frac{r}{R}\right)^2 \approx 1.40 - 0.02\left(\frac{r}{R}\right)^2$$

với $R$ là bán kính thủy tinh thể. Gradient index (GRIN) này có hai lợi ích:
1. Giảm quang sai cầu (tia rìa hội tụ gần hơn tia tâm với thấu kính đồng nhất)
2. Tăng sức hội tụ mà không cần độ cong lớn (ít quang sai hơn)

Đây là nguyên lý mà kỹ sư quang học hiện đại đang cố gắng tái tạo trong thấu kính GRIN cho kính hiển vi, thiết bị y tế và hệ thống laser.

**Giác mạc phi cầu (aspheric cornea):**

Giác mạc hình cầu hoàn hảo có quang sai cầu (spherical aberration): tia rìa hội tụ gần hơn tia tâm. Giác mạc thực tế "phẳng hơn" ở rìa (hình **prolate ellipsoid**):

$$z(r) = \frac{r^2}{R_0[1 + \sqrt{1-(1+Q)r^2/R_0^2}]}$$

với hệ số cônic $Q \approx -0.26$ (so với $Q=0$ cho hình cầu). Điều này giảm quang sai cầu đáng kể so với hình cầu — chứng tỏ tiến hóa đã "tối ưu hóa" hình dạng giác mạc.

### Hệ điều khiển thần kinh của mắt

Thông tin từ dây thần kinh thị giác đi theo hai luồng:

**Luồng chính:** → Vỏ não thị giác (visual cortex) → "Nhìn thấy" ảnh

**Luồng phản xạ qua não giữa (midbrain):**
- Điều chỉnh iris (pupillary light reflex): ánh sáng mạnh → đồng tử co lại (~200 ms latency)
- Điều tiết thủy tinh thể (accommodation): khi ảnh mờ → cơ thể mi (ciliary muscle) co lại → thủy tinh thể phồng lên → tăng sức hội tụ
- Điều chỉnh hướng nhìn hai mắt (vergence): để hội tụ vào vật ở các khoảng cách khác nhau

Đây là **hệ thống điều khiển tự động (closed-loop control system)** với:
- **Plant:** Thủy tinh thể + cơ thể mi
- **Sensor:** Tế bào ganglion trong võng mạc (phát hiện độ mờ)
- **Controller:** Midbrain
- **Actuator:** Cơ thể mi

Phép so sánh trực tiếp với hệ thống autofocus camera: phase detection AF trong máy ảnh hiện đại dùng cặp pixel đặc biệt để phát hiện mờ và hướng điều chỉnh tiêu cự — hoàn toàn mô phỏng cơ chế accommodation của mắt.

### Điểm mấu chốt

Mắt người là hệ thống quang học-thần kinh đa lớp: giác mạc phi cầu giảm quang sai, thủy tinh thể gradient index tăng sức hội tụ, ba lớp tế bào thần kinh võng mạc nén và xử lý 126 triệu tín hiệu thành 1 triệu sợi thần kinh, và vòng điều khiển phản xạ qua midbrain tự động điều chỉnh tiêu cự và độ sáng trong vài trăm mili giây. Hiểu kiến trúc này giúp kỹ sư thiết kế hệ thống quang học và camera thông minh hơn — từ autofocus đến adaptive optics.

---
*Exported from Feynman Bot*
