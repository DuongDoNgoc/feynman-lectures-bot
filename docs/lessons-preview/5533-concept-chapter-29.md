---
lesson_id: 5533
lesson_type: concept
approval_status: approved
exported_at: "2026-03-03T15:33:07.314374+00:00"
content_hash: e1fe682ee88d
chapter_number: 29
chapter_title: Chapter 29
section_number: 5
section_title: 29–4Two dipole radiators
---
# ## Giao Thoa Hai Nguồn: Khi Sóng Cộng và Triệt Nhau

*Source: Chapter 29 - Chapter 29 (Section 5) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_29.html)*

## Giao Thoa Hai Nguồn: Khi Sóng Cộng và Triệt Nhau

Bạn đã bao giờ đứng gần hai loa âm thanh phát cùng một nốt nhạc và bước dần sang ngang chưa? Có những vị trí âm thanh rất to, có những vị trí gần như im lặng hoàn toàn — dù bạn chỉ di chuyển vài bước chân. Đây là hiện tượng giao thoa sóng âm, và ánh sáng cũng hoạt động hoàn toàn như vậy. Hiểu được giao thoa của hai nguồn là bước đệm để hiểu cách anten mảng phát hiện và theo dõi mục tiêu, cách sensor interferometry đo dịch chuyển nanometer, và cách bộ lọc RF được thiết kế.

**Bài toán cơ bản: Hai nguồn, một điểm quan sát**

Xét hai dipole oscillator (anten) cách nhau $d = \lambda/2$ (nửa bước sóng), dao động cùng pha. Ta muốn biết cường độ bức xạ theo các hướng khác nhau.

Nguyên lý cơ bản: điện trường là đại lượng vector, và sóng tuân theo nguyên lý chồng chất — trường tổng bằng tổng đại số của các trường thành phần. Cường độ (intensity) tỉ lệ với bình phương trường: $I \propto E^2$.

Nếu hai sóng hoàn toàn cùng pha tại điểm quan sát: $E_{total} = 2E_0$, nên $I = 4E_0^2 = 4I_0$ — gấp bốn lần.

Nếu hai sóng hoàn toàn ngược pha: $E_{total} = 0$, nên $I = 0$ — triệt tiêu hoàn toàn.

Giữa hai thái cực này là mọi giá trị trung gian, tùy thuộc vào góc quan sát và khoảng cách giữa hai nguồn.

**Tại sao $I \propto E^2$ mà không phải $I \propto E$?**

Trường điện $E$ cho biết lực tác dụng lên điện tích thử đứng yên. Nhưng năng lượng mà sóng mang theo (đơn vị: watt/m²) tỉ lệ với tích của điện trường và từ trường: $S = \varepsilon_0 c E^2$ (đây là vector Poynting). Vì $|B| = |E|/c$, nên $S \propto E^2$. Đây là lý do tại sao khi hai anten cộng pha, cường độ tăng lên 4 lần (không phải 2 lần) so với một anten đơn — và đây cũng là lý do tại sao trong thiết kế anten mảng, ta thu được gain vượt trội.

**Phép so sánh: Sensor giao thoa cho kỹ sư cơ điện tử**

Trong hệ thống đo vị trí laser interferometry (ví dụ: hệ thống phản hồi vị trí trong máy in mạch in PCB hay máy CNC chính xác), nguyên lý giao thoa được sử dụng trực tiếp. Chùm laser được chia làm hai: một chùm đi theo đường chuẩn (reference arm), một chùm phản xạ từ bề mặt cần đo (measurement arm). Khi hai chùm gặp nhau tại detector, chúng giao thoa. Mỗi lần bề mặt di chuyển $\lambda/2$ (nửa bước sóng, khoảng 316 nm với laser HeNe), vân giao thoa dịch chuyển một kỳ hoàn chỉnh — bộ đếm vân xác định vị trí với độ chính xác dưới nanometer.

Đây chính xác là cùng hiện tượng: hai sóng từ hai "nguồn" (thực ra là hai đường đi khác nhau của cùng một nguồn) gặp nhau và giao thoa tùy thuộc vào hiệu đường đi.

**Kết quả định lượng cho hai nguồn cùng pha, cách nhau $d = \lambda/2$**

Nhìn từ phương Tây (vuông góc, $\theta = 0$): cả hai nguồn đều cách đều điểm quan sát, cùng pha, $E_{total} = 2E_0$, $I = 4I_0$.

Nhìn từ phương Bắc hay Nam (dọc theo trục nối hai nguồn, $\theta = 90°$): sóng từ nguồn gần hơn và xa hơn lệch pha nhau $\pi$ (vì hiệu đường đi bằng $d = \lambda/2$), $E_{total} = 0$, $I = 0$ — triệt tiêu hoàn toàn.

**Điều gì xảy ra khi hai nguồn lệch pha nhau $180°$?**

Nếu ta đảo pha một anten (lệch pha $\delta = \pi$), kết quả ngược lại: nhìn từ phương Tây thì triệt tiêu (vì cùng khoảng cách nhưng ngược pha), nhìn từ phương Bắc/Nam thì cộng pha (vì hiệu đường đi $\lambda/2$ bù lại với lệch pha $\pi$). Bức xạ tập trung sang hai phía thay vì về phía trước!

Đây chính là nguyên lý của anten cardioid (tim), hay anten Yagi-Uda trong vô tuyến nghiệp dư: bằng cách chọn khoảng cách và pha phù hợp, ta định hướng bức xạ.

**Điểm mấu chốt**

- Cường độ sóng $I \propto E^2$ — tổng hợp trường xong mới bình phương, không được bình phương từng thành phần rồi cộng
- Hai nguồn cùng pha, cách nhau $\lambda/2$: cực đại 4 lần theo phương vuông góc, triệt tiêu theo phương dọc trục
- Hai nguồn lệch pha $\pi$, cách nhau $\lambda/2$: kết quả ngược lại — bức xạ tập trung dọc theo trục nối hai nguồn
- Giao thoa là nền tảng của phased array radar, sensor interferometry và mọi hệ thống đo lường bằng sóng

---
*Exported from Feynman Bot*
