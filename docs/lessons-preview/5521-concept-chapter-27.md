---
lesson_id: 5521
lesson_type: concept
approval_status: pending
exported_at: "2026-03-02T15:10:31.626541+00:00"
content_hash: afd00dc96e90
chapter_number: 27
chapter_title: Chapter 27
section_number: 7
section_title: 27–6Aberrations
---
# ## Giới Hạn Của Thấu Kính: Aberration — Khi Quang Học Không Hoàn Hảo

*Source: Chapter 27 - Chapter 27 (Section 7) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_27.html)*

## Giới Hạn Của Thấu Kính: Aberration — Khi Quang Học Không Hoàn Hảo

### Mở đầu: Tại sao ảnh chụp bằng kính rẻ tiền lại mờ ở góc?

Bạn đã từng chụp ảnh bằng điện thoại rẻ tiền và nhận thấy các vật thể ở góc ảnh bị mờ hoặc có viền màu? Hay quan sát qua kính lúp và thấy ảnh ở rìa bị méo? Đây không phải là lỗi sản xuất ngẫu nhiên — đây là **aberration**, một giới hạn cơ bản của thấu kính hình cầu mà ngay cả Einstein hay Feynman cũng không thể "xoá bỏ" bằng toán học thuần tuý.

### Vấn đề cốt lõi: Xấp xỉ paraxial có giới hạn

Toàn bộ lý thuyết thấu kính đẹp đẽ mà chúng ta đã xây dựng — từ phương trình bề mặt khúc xạ đến lensmaker's equation — đều dựa trên một giả thiết quan trọng: **tia sáng phải ở gần trục quang** (paraxial approximation). Chúng ta đã dùng $\sin\theta \approx \theta$ và $\cos\theta \approx 1$.

Nhưng thực tế, thấu kính có kích thước hữu hạn. Một tia sáng đập vào mép thấu kính thì góc $\theta$ không còn nhỏ nữa. Khi đó, công thức paraxial bắt đầu sai, và tất cả các tia không còn hội tụ về một điểm duy nhất.

### Hai loại aberration chính

**1. Spherical Aberration (Quang sai cầu)**

Tia sáng đi qua tâm thấu kính hội tụ đúng vào tiêu điểm. Tia gần trục vẫn hội tụ tốt. Nhưng tia đi qua mép thấu kính lại hội tụ ở điểm khác — gần hơn hoặc xa hơn tùy hình dạng thấu kính. Kết quả: thay vì một điểm ảnh sắc nét, ta nhận được một vùng mờ (*circle of least confusion*).

Phép so sánh: Tưởng tượng bạn đang cố gắng chiếu sáng một điểm nhỏ bằng một ngọn đèn pin hình cầu. Ánh sáng từ trung tâm đèn tập trung tốt, nhưng ánh sáng từ mép đèn lại tản ra theo nhiều hướng khác nhau.

**2. Chromatic Aberration (Quang sai màu sắc)**

Ánh sáng trắng gồm nhiều bước sóng. Chiết suất thuỷ tinh phụ thuộc vào bước sóng — hiện tượng **dispersion** (tán sắc). Do đó, tiêu cự của thấu kính khác nhau cho ánh sáng đỏ, vàng, tím.

Từ lensmaker's equation: $\frac{1}{f} = (n-1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right)$

Khi $n$ thay đổi theo bước sóng, $f$ cũng thay đổi theo. Ánh sáng tím (bước sóng ngắn, $n$ lớn hơn) hội tụ gần thấu kính hơn ánh sáng đỏ. Kết quả: ảnh có viền màu (*chromatic fringing*).

### Giới hạn của sự hoàn hảo: Nguyên lý nhiễu xạ

Feynman đặt một câu hỏi thú vị: *Chúng ta có thể làm cho hệ quang học hoàn hảo tuyệt đối không?* Câu trả lời là **không** — và lý do đến từ bản chất sóng của ánh sáng.

Ngay cả khi ta khử hoàn toàn mọi aberration, vẫn tồn tại một giới hạn nhiễu xạ (*diffraction limit*). Nguyên lý thời gian cực tiểu chỉ là xấp xỉ — ánh sáng thực chất là sóng, và nếu sai lệch thời gian giữa tia biên và tia trục nhỏ hơn **một chu kỳ dao động** của ánh sáng, thì không cần cải thiện thêm nữa.

Nói cách khác, kích thước điểm hội tụ nhỏ nhất có thể là:
$$d_{min} \approx \frac{\lambda}{NA}$$

Trong đó $\lambda$ là bước sóng ánh sáng và $NA$ là *numerical aperture* (khẩu độ số) của hệ quang học. Đây là giới hạn Rayleigh — một giới hạn không thể vượt qua bằng quang học thông thường.

### Ý nghĩa cho kỹ sư

Với kỹ sư thiết kế hệ đo lường chính xác micromet, hai loại aberration trên đặt ra những bài toán thực tế:

- **Spherical aberration** giới hạn kích thước điểm hội tụ của laser → ảnh hưởng độ phân giải không gian
- **Chromatic aberration** gây vấn đề khi dùng ánh sáng trắng (như trong white-light interferometry hoặc chromatic confocal sensor)
- **Diffraction limit** là rào cản vật lý không thể vượt qua bằng thiết kế quang học thông thường → muốn vượt qua phải dùng near-field optics hoặc kỹ thuật super-resolution

### Cách khắc phục

1. **Dùng thấu kính aspheric** (bề mặt không cầu): tối ưu hình dạng bề mặt để khử spherical aberration cho một khoảng cách vật cụ thể
2. **Dùng doublet achromat**: ghép hai thấu kính vật liệu khác nhau để tiêu cự bằng nhau cho hai màu (thường là đỏ và xanh)
3. **Giới hạn khẩu độ** (aperture stop): dùng ít tia biên hơn, hi sinh cường độ để tăng chất lượng ảnh
4. **Ray tracing bằng máy tính**: không dùng xấp xỉ paraxial mà tính chính xác đường đi từng tia qua từng bề mặt

### Tóm tắt

- Aberration xuất hiện khi tia sáng xa trục — xấp xỉ paraxial không còn đúng
- Spherical aberration: tia biên và tia trục hội tụ ở điểm khác nhau
- Chromatic aberration: chiết suất phụ thuộc bước sóng → tiêu cự khác nhau cho mỗi màu
- Ngay cả hệ quang học hoàn hảo cũng bị giới hạn nhiễu xạ: $d_{min} \approx \lambda/NA$
- Khắc phục: thấu kính aspheric, doublet achromat, hạn chế khẩu độ

---
*Exported from Feynman Bot*
