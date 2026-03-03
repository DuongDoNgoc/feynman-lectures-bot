---
lesson_id: 5541
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:07.501822+00:00"
content_hash: e3495e16388b
chapter_number: 30
chapter_title: Chapter 30
section_number: 2
section_title: 30–1The resultant amplitude due tonnequal oscillators
---
# ## Kiểm Tra: Nhiễu Xạ từ N Nguồn Đều Nhau

*Source: Chapter 30 - Chapter 30 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_30.html)*

## Kiểm Tra: Nhiễu Xạ từ N Nguồn Đều Nhau

**Câu 1 (Trắc nghiệm):** Một mảng gồm $n = 10$ anten cách đều nhau phát sóng kết hợp. So với 1 anten đơn có cùng công suất phát mỗi phần tử, cường độ tại cực đại chính của mảng lớn hơn bao nhiêu lần?

A) 10 lần
B) 20 lần
C) 100 lần
D) 1000 lần

**Đáp án: C**

*Giải thích:* Tại cực đại chính, $n$ phasor cùng hướng nên biên độ hợp $A_R = nA$. Cường độ $I \propto A_R^2 = n^2 A^2$. So với 1 anten ($I_0 \propto A^2$), mảng 10 anten cho $I = 100 I_0$. Đây là nguyên tắc **array gain** — lý do tại sao radar quân sự dùng mảng phần tử lớn để tăng phạm vi phát hiện.

---

**Câu 2 (Trắc nghiệm):** Điều kiện để xảy ra cực tiểu (null) đầu tiên trong vân nhiễu xạ của $n$ nguồn đều nhau là:

A) $\phi = \pi/n$ (hiệu pha giữa hai nguồn liên tiếp bằng $\pi/n$)
B) $\phi = 2\pi/n$ (hiệu pha giữa hai nguồn liên tiếp bằng $2\pi/n$)
C) $\phi = \pi$ (nguồn đầu và cuối ngược pha nhau)
D) $\phi = 2\pi$ (mỗi nguồn lệch pha đúng một vòng so với nguồn trước)

**Đáp án: B**

*Giải thích:* Cực tiểu xảy ra khi $n$ phasor khép thành vòng tròn đóng, tức tổng pha tích lũy $n\phi = 2\pi$, suy ra $\phi = 2\pi/n$. Trong hình học phasor, đây là lúc $n$ vectơ tạo thành đa giác đều kín và tổng về 0. Hiểu điều này giúp thiết kế null steering trong anten array.

---

**Câu 3 (Trắc nghiệm):** Độ phân giải góc $\Delta\theta$ của một mảng anten phased array phụ thuộc chủ yếu vào yếu tố nào?

A) Số lượng phần tử $n$ và khoảng cách $d$ riêng lẻ
B) Tổng chiều dài array $L = nd$ và bước sóng $\lambda$
C) Chỉ bước sóng $\lambda$, không phụ thuộc kích thước vật lý
D) Công suất phát của từng phần tử

**Đáp án: B**

*Giải thích:* $\Delta\theta \approx \lambda/(L\cos\theta)$ với $L = nd$. Độ phân giải phụ thuộc vào **tổng chiều dài** array, không phải số lượng phần tử riêng lẻ. Nếu giữ $L$ cố định nhưng tăng $n$ (giảm $d$), độ phân giải góc không đổi nhưng mức búp sóng phụ giảm xuống. Đây là trade-off quan trọng trong thiết kế radar.

---

**Câu 4 (Tự luận):** Trong hệ thống đo vị trí chính xác cấp micrometer (ví dụ: hệ thống căn chỉnh bàn trượt CNC hoặc đầu đọc encoder quang học), người ta thường dùng cách tử nhiễu xạ thay vì thước thẳng thông thường. Hãy giải thích:
(a) Tại sao cách tử nhiễu xạ lại cho độ chính xác cao hơn encoder thước từ?
(b) Nếu cách tử có $d = 1$ μm, bước sóng laser $\lambda = 780$ nm, tính góc của cực đại bậc 1. Tín hiệu bậc 1 này có thể dùng để đo vị trí với độ phân giải $\lambda/2$ = 390 nm không?

**Gợi ý đáp án:**

(a) Cách tử nhiễu xạ dùng ánh sáng laser kết hợp (coherent): vị trí đầu đọc được mã hóa bằng **pha của vân nhiễu xạ** chứ không phải cường độ. Mỗi khi bàn trượt dịch chuyển $\delta x$, pha của tín hiệu thay đổi $\Delta\phi = 4\pi\delta x\sin\theta_1/\lambda$ (đường đi cả chiều đi lẫn về). Bằng cách đếm vân và nội suy pha, hệ thống đạt $\delta x_{min} \approx \lambda/(4\sin\theta_1)$. Với laser và điện tử hiện đại, có thể đạt $< 1$ nm.

Encoder thước từ đọc tín hiệu analog dựa trên từ trường — dễ bị nhiễu điện từ, nhiệt độ, và hao mòn cơ học. Cách tử quang không tiếp xúc, không bị ảnh hưởng bởi từ trường.

(b) Cực đại bậc 1: $\sin\theta_1 = \lambda/d = 0.780/1 = 0.780 \implies \theta_1 = 51.3°$.

Với góc phản xạ $\theta_1 = 51.3°$, tín hiệu bậc 1 phản xạ trở lại. Mỗi khi bàn trượt dịch $d = 1$ μm, tín hiệu bậc 1 hoàn thành một chu kỳ (do path difference thay đổi $2d\sin\theta_1 = 2 \times 1 \times 0.780 = 1.56$ μm $= 2\lambda$). Mỗi chu kỳ tín hiệu tương đương $d_{step} = d/2 = 0.5$ μm dịch chuyển. Với nội suy điện tử chia 1000, có thể đạt $0.5$ nm — tốt hơn yêu cầu $390$ nm. Trên thực tế, encoder quang Linear Scale của Heidenhain dùng nguyên lý này, đạt $< 1$ nm.


---
*Exported from Feynman Bot*
