---
lesson_id: 5542
lesson_type: concept
approval_status: approved
exported_at: "2026-03-03T15:33:07.526946+00:00"
content_hash: 64edb2c020f5
chapter_number: 30
chapter_title: Chapter 30
section_number: 3
section_title: 30–2The diffraction grating
---
# ## Cách Tử Nhiễu Xạ: Chiếc Lăng Kính Tinh Tế của Ánh Sáng

*Source: Chapter 30 - Chapter 30 (Section 3) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_30.html)*

## Cách Tử Nhiễu Xạ: Chiếc Lăng Kính Tinh Tế của Ánh Sáng

### Câu hỏi mở đầu

Tại sao đĩa CD phát ra cầu vồng màu sắc khi bạn nghiêng nó dưới ánh đèn? Và liệu có cách nào để nhìn thấy màu sắc của một nguồn sáng với độ chính xác đến phần tỷ mét (nanomét) mà không cần đến máy móc phức tạp? Câu trả lời ẩn trong những đường khắc song song cực mịn trên bề mặt kính — đó chính là **cách tử nhiễu xạ** (diffraction grating).

### Nguyên lý hoạt động: Từ anten radio đến ánh sáng

Feynman mở đầu bằng một ý tưởng táo bạo: trong kỹ thuật radio, ta có thể điều khiển pha của từng anten riêng lẻ bằng dây dẫn. Với ánh sáng, ta không thể làm vậy. Nhưng có một cách thông minh hơn!

Tưởng tượng hàng trăm dây kim loại song song, cách đều nhau khoảng cách $d$, được chiếu bởi một nguồn sóng điện từ rất xa (sóng phẳng). Sóng này rung các electron trong mỗi dây — mỗi dây trở thành một anten phát lại. Vì tất cả đều nhận sóng phẳng cùng lúc, chúng phát lại **đồng pha**. Thế là ta có ngay $n$ nguồn đồng pha, cách đều — mà không cần một mét dây điện nào!

Với ánh sáng, thay vì dây kim loại, ta dùng **cách tử** — bản kính (hoặc kim loại) có $n$ vạch khắc song song, đều nhau. Mỗi vạch tán xạ ánh sáng theo hướng khác nhau, đóng vai trò một nguồn phát mới.

### Cực đại chính: Khi tất cả sóng gặp nhau

Ánh sáng từ cách tử cho cực đại chính tại các góc $\theta$ thỏa mãn:

$$d\sin\theta = m\lambda \quad (m = 0, \pm 1, \pm 2, ...)$$

**Phép so sánh trực quan:** Hãy nghĩ đến hàng quân tuần hành — nếu mỗi người bước theo nhịp cùng một lúc (đồng pha), tiếng bước chân cộng hưởng mạnh hơn nhiều so với đám đông bước loạn. Cực đại chính là lúc mọi "tiếng bước" sóng ánh sáng từ $n$ vạch cùng pha nhau — biên độ cộng thẳng hàng, cường độ tăng $n^2$ lần.

**Điều quan trọng:** Vì $\lambda$ xuất hiện trong công thức, **mỗi màu sắc cho cực đại tại góc khác nhau**. Đỏ ($\lambda \approx 700$ nm) bị uốn nhiều hơn tím ($\lambda \approx 400$ nm). Cầu vồng màu sắc của đĩa CD là do ánh sáng trắng bị phân tán theo nguyên lý này.

### Ứng dụng: Phân tích phổ và đo lường chính xác

**Máy quang phổ kế (Spectrometer):** Trong phòng thí nghiệm đo lường chính xác, spectrometer dùng cách tử để phân tích thành phần bước sóng của nguồn sáng laser — ví dụ để kiểm tra chất lượng laser diode trong cảm biến. Cách tử $N = 1200$ vạch/mm ($d \ approx 833$ nm) phân tán ánh sáng khả kiến với góc $20°$–$60°$, đủ rõ để đọc bằng camera CCD.

**Encoder quang học (Optical Encoder):** Trong servo motor của máy CNC, robot arm, hay bàn trượt chính xác của bạn, encoder quang dùng cách tử thước — một thước thủy tinh với $n$ vạch/mm được laser chiếu qua. Ánh sáng nhiễu xạ bậc $\pm 1$ tạo ra vân giao thoa dịch chuyển theo vị trí thước. Mỗi vân = một chu kỳ $d$ dịch chuyển — với $d = 20$ μm và nội suy điện tử, ta đạt độ phân giải $< 20$ nm, hoàn toàn đủ cho gia công micrometer-level.

### Điểm mấu chốt

- Cách tử nhiễu xạ = nhiều nguồn sóng đồng pha cách đều nhau, hoạt động nhờ sóng tới kích thích mỗi phần tử tán xạ độc lập
- Cực đại chính tại: $d\sin\theta = m\lambda$ — mỗi bước sóng có góc riêng, đây là cơ sở phân tích phổ
- Càng nhiều vạch $n$: cực đại càng hẹp, phân giải càng cao (như anten array, như radar)
- Ứng dụng trực tiếp trong encoder quang, spectrometer, và bộ lọc bước sóng của hệ thống viễn thông quang (WDM)

---
*Exported from Feynman Bot*
