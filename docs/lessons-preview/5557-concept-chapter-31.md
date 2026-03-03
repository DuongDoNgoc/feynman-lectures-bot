---
lesson_id: 5557
lesson_type: concept
approval_status: approved
exported_at: "2026-03-03T15:33:07.926262+00:00"
content_hash: b00fdb739a76
chapter_number: 31
chapter_title: Chapter 31
section_number: 5
section_title: 31–4Absorption
---
# ## Chỉ Số Khúc Xạ Phức: Khi Ánh Sáng Bị "Hấp Thụ" Bởi Vật Liệu

*Source: Chapter 31 - Chapter 31 (Section 5) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_31.html)*

## Chỉ Số Khúc Xạ Phức: Khi Ánh Sáng Bị "Hấp Thụ" Bởi Vật Liệu

Bạn đã bao giờ tự hỏi tại sao kính lọc màu lại làm ánh sáng yếu đi? Hay tại sao kim loại phản chiếu ánh sáng mạnh đến vậy, trong khi thủy tinh trong suốt lại không? Câu trả lời nằm ở một khái niệm tưởng chừng kỳ lạ: **chỉ số khúc xạ phức** (complex index of refraction).

### Vấn đề: Tại sao chỉ số khúc xạ lại "phức"?

Khi Feynman xây dựng phương trình tán sắc (dispersion equation) cho ánh sáng truyền qua vật liệu, ông đưa vào một số hạng mô tả **lực cản** (damping) - tức là sự mất năng lượng của electron khi dao động. Kết quả thật bất ngờ: chỉ số khúc xạ $n$ không còn là số thực nữa, mà trở thành số phức:

$$n = n' - in''$$

Trong đó:
- $n'$ là phần thực - phần quen thuộc, mô tả **sự thay đổi tốc độ pha** của ánh sáng trong vật liệu
- $n''$ là phần ảo (luôn dương) - phần mới, mô tả **sự hấp thụ** (absorption) năng lượng

### Ý nghĩa vật lý: Hai hiệu ứng tách biệt

Để hiểu $n$ phức có nghĩa gì, hãy xét một sóng điện từ sau khi truyền qua một tấm vật liệu dày $\Delta z$. Khi thay $n = n' - in''$ vào phương trình sóng, ta nhận được:

$$E_{\text{sau}} = e^{-\omega n'' \Delta z / c} \cdot E_0 e^{i\omega(n' - 1)\Delta z/c} e^{i\omega(t - z/c)}$$

Hãy nhìn kỹ hai thừa số này:

**Thừa số A** - $e^{-\omega n'' \Delta z / c}$: Đây là số thực, luôn nhỏ hơn 1 (vì $n'' > 0$). Nó làm **biên độ** sóng giảm đi theo hàm mũ khi truyền qua vật liệu. Đây chính là hiện tượng **hấp thụ** (absorption)!

**Thừa số B** - phần còn lại: Đây là sóng dao động với pha bị trễ đi một lượng $\omega n' \Delta z / c$ so với sóng trong chân không. Đây là hiệu ứng khúc xạ thông thường.

Nói cách khác: **phần thực $n'$ quyết định tốc độ, phần ảo $n''$ quyết định độ suy giảm**.

### Phép so sánh với kỹ sư cơ điện tử

Là một kỹ sư điều khiển tự động, bạn đã quen với **hàm truyền phức** (complex transfer function) trong miền tần số. Khi bạn thiết kế bộ lọc hoặc phân tích đáp ứng hệ thống, số phức xuất hiện tự nhiên:

- **Phần thực** $\leftrightarrow$ đáp ứng pha (phase response) - ảnh hưởng đến trễ tín hiệu
- **Phần ảo** $\leftrightarrow$ đáp ứng biên độ (magnitude response) - ảnh hưởng đến suy giảm hay khuếch đại

Tương tự, chỉ số khúc xạ phức $n = n' - in''$ chính là "hàm truyền" của vật liệu đối với sóng điện từ:
- $n'$ kiểm soát **tốc độ pha** (phase velocity)
- $n''$ kiểm soát **sự suy giảm biên độ** (amplitude attenuation)

Hằng số $\alpha = 2\omega n''/c$ chính là **hệ số suy giảm** (attenuation coefficient) của vật liệu, đơn vị là $\text{m}^{-1}$, hoàn toàn tương đương với hệ số suy giảm trong lý thuyết tín hiệu.

### Khi nào $n''$ lớn? Cộng hưởng hấp thụ

Phần ảo $n''$ không phải hằng số - nó phụ thuộc mạnh vào tần số. Khi tần số ánh sáng gần với tần số cộng hưởng $\omega_0$ của electron trong vật liệu, $n''$ tăng vọt. Đây là lý do:

- Kính màu hấp thụ mạnh ở một số tần số nhất định (tần số cộng hưởng của các phân tử màu nhuộm)
- Kim loại hấp thụ hầu hết ánh sáng khả kiến (electron tự do có cộng hưởng ở tần số thấp)
- Thủy tinh trong suốt vì $n''$ rất nhỏ trong vùng khả kiến

Đây cũng là nguyên lý của **quang phổ hấp thụ** (absorption spectroscopy) - một công cụ đo lường cực kỳ chính xác được dùng trong nhiều hệ thống đo đạc hiện đại.

### Điểm mấu chốt

- Khi vật liệu có lực cản (damping), chỉ số khúc xạ trở thành **số phức** $n = n' - in''$
- **$n'$** (phần thực): kiểm soát tốc độ pha và sự khúc xạ của ánh sáng
- **$n''$** (phần ảo, luôn dương): kiểm soát sự hấp thụ - biên độ sóng giảm theo hàm mũ $e^{-\omega n'' \Delta z/c}$
- Hai hiệu ứng này hoàn toàn tách biệt và độc lập, giống như phần thực và phần ảo của hàm truyền trong lý thuyết điều khiển
- $n''$ đạt cực đại gần tần số cộng hưởng của vật liệu, giải thích hiện tượng hấp thụ chọn lọc theo màu sắc

---
*Exported from Feynman Bot*
