---
lesson_id: 5527
lesson_type: concept
approval_status: approved
exported_at: "2026-03-03T15:33:07.192912+00:00"
content_hash: 40de9647ba18
chapter_number: 28
chapter_title: Chapter 28
section_number: 3
section_title: 28–2Radiation
---
# ## Bức Xạ Điện Từ: Khi Điện Tích Chuyển Động, Ánh Sáng Được Sinh Ra

*Source: Chapter 28 - Chapter 28 (Section 3) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_28.html)*

## Bức Xạ Điện Từ: Khi Điện Tích Chuyển Động, Ánh Sáng Được Sinh Ra

Bạn đã bao giờ tự hỏi tại sao anten của radio, radar hay thiết bị liên lạc lại phải có hình dạng và kích thước cụ thể không? Tại sao một đầu dò radar quân sự có thể phát hiện máy bay cách hàng trăm km, nhưng khi bạn che nó bằng một tấm kim loại thì tín hiệu biến mất hoàn toàn? Câu trả lời nằm ở một trong những định luật sâu sắc nhất của vật lý: điện tích tăng tốc thì tạo ra bức xạ điện từ — chính là ánh sáng, sóng radio, tia X, và mọi loại sóng điện từ khác.

**Bức xạ sinh ra từ đâu?**

Khi một điện tích đứng yên, nó tạo ra điện trường tĩnh giảm theo $1/r^2$ — càng xa càng yếu rất nhanh. Khi điện tích chuyển động đều (không tăng tốc), nó chỉ tạo ra điện trường và từ trường đi theo nó, không lan ra xa được. Nhưng khi điện tích *tăng tốc* — thay đổi vận tốc — thì xuất hiện một thành phần trường đặc biệt chỉ giảm theo $1/r$, không phải $1/r^2$. Đây chính là sóng bức xạ.

Tại sao điều này quan trọng? Vì $1/r$ giảm chậm hơn $1/r^2$ rất nhiều. Ở khoảng cách 1000 lần, một trường $1/r^2$ yếu đi 1.000.000 lần, còn trường $1/r$ chỉ yếu đi 1000 lần. Đây chính là lý do tại sao sóng radio có thể truyền đi hàng nghìn km — năng lượng bức xạ lan ra đến vô cùng.

Feynman đã đưa ra một công thức kỳ diệu để mô tả trường bức xạ này:

$$\mathbf{E} = \frac{-q}{4\pi\varepsilon_0 c^2 r} \frac{d^2\hat{e}_{r'}}{dt^2}$$

Nhìn vào công thức này, điều đáng chú ý là: trường điện không phụ thuộc vào vị trí hay vận tốc của điện tích, mà phụ thuộc vào **gia tốc của vector đơn vị hướng từ điện tích đến điểm quan sát**. Nói đơn giản hơn: khi điện tích dao động, cái "bóng" của nó chiếu lên mặt cầu đơn vị sẽ lắc lư, và chính gia tốc của sự lắc lư đó tạo ra trường bức xạ.

**Phép ẩn dụ dành cho kỹ sư cơ điện tử**

Hãy tưởng tượng hệ thống điều khiển servo motor của bạn. Khi motor quay đều (vận tốc không đổi), nó tạo ra EMF và từ trường, nhưng không phát ra sóng điện từ đáng kể. Nhưng khi bạn bật/tắt motor đột ngột — thay đổi dòng điện nhanh (tức là *gia tốc* của điện tích trong dây dẫn) — máy hiện sóng của bạn sẽ nhảy loạn. Đó chính là pulse EMI (electromagnetic interference) phát ra từ gia tốc của điện tích! Đây là lý do tại sao trong thiết kế board điều khiển độ chính xác micro-mét, bạn phải đặt tụ bypass, dùng twisted pair, hay thêm ferrite bead — tất cả để giảm thiểu hiệu ứng bức xạ từ dòng điện biến đổi nhanh.

Radar quân sự hoạt động theo nguyên lý ngược lại: bạn *cố ý* tạo ra dòng điện dao động mạnh trong anten để phát ra sóng điện từ. Sóng này truyền đi theo hướng $1/r$, đập vào máy bay, phản xạ lại theo cùng $1/r$, và máy thu nhận được tín hiệu. Đây là lý do tại sao công suất radar phải rất lớn: mỗi lần phản xạ lại mất thêm một lần suy giảm $1/r$.

**Ý nghĩa vật lý của thành phần bức xạ**

Có một điều tuyệt đẹp trong công thức Feynman: thành phần trường bức xạ phụ thuộc vào **gia tốc tại thời điểm trễ** $t - r/c$. Điều này có nghĩa là thông tin về chuyển động của điện tích phải mất một khoảng thời gian $r/c$ — đúng bằng thời gian ánh sáng đi từ điện tích đến điểm quan sát — để truyền tới bạn. Không có gì truyền nhanh hơn ánh sáng, kể cả thông tin về sự thay đổi của điện trường.

Đây chính là lý do tại sao khi một ngôi sao cách chúng ta 100 năm ánh sáng phát nổ (supernova), chúng ta phải đợi đúng 100 năm mới thấy ánh sáng từ vụ nổ đó. Và theo cùng nguyên lý, nếu bạn di chuyển electron trong anten, thông tin về sự dao động đó sẽ lan ra với tốc độ ánh sáng, mang theo năng lượng đến mọi nơi trong không gian.

Một điểm nữa: cường độ bức xạ còn phụ thuộc vào góc quan sát. Điện tích dao động theo một trục không bức xạ năng lượng dọc theo trục đó — nếu bạn nhìn thẳng vào hướng dao động, bạn không thấy bức xạ. Nhưng nhìn từ góc vuông góc, bức xạ là mạnh nhất. Đây là lý do anten dipole phải đặt vuông góc với hướng thu phát.

**Điểm mấu chốt**

- Chỉ có điện tích *tăng tốc* mới tạo ra bức xạ điện từ; chuyển động đều không phát sóng
- Trường bức xạ giảm theo $1/r$ (không phải $1/r^2$), nên sóng điện từ có thể truyền đến vô cùng
- Công thức $\mathbf{E} \propto \frac{1}{r}\frac{d^2\hat{e}_{r'}}{dt^2}$ cho thấy: bức xạ tỉ lệ với gia tốc của hướng nhìn từ điểm quan sát đến điện tích
- Thông tin truyền với tốc độ ánh sáng — trường bức xạ phụ thuộc vào gia tốc tại *thời điểm trễ* $t - r/c$
- Trong kỹ thuật: mọi dòng điện biến đổi nhanh đều phát bức xạ EMI — đây là thách thức cốt lõi trong thiết kế hệ thống điện tử độ chính xác cao

---
*Exported from Feynman Bot*
