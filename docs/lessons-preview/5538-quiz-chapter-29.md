---
lesson_id: 5538
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:07.423370+00:00"
content_hash: f57e5d82fa00
chapter_number: 29
chapter_title: Chapter 29
section_number: 6
section_title: 29–5The mathematics of interference
---
# ## Kiểm Tra: Cộng Sóng và Phương Pháp Phasor

*Source: Chapter 29 - Chapter 29 (Section 6) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_29.html)*

## Kiểm Tra: Cộng Sóng và Phương Pháp Phasor

**Câu 1 (Trắc nghiệm):** Hai sóng $R_1 = A\cos(\omega t + 30°)$ và $R_2 = A\cos(\omega t + 90°)$ có biên độ bằng nhau. Biên độ hợp $A_R$ bằng bao nhiêu?

A) $A$
B) $A\sqrt{2}$
C) $A\sqrt{3}$
D) $2A$

**Đáp án: C**

*Giải thích:* Hiệu pha $\Delta\phi = 90° - 30° = 60°$. Áp dụng công thức: $A_R = 2A\cos(\Delta\phi/2) = 2A\cos(30°) = 2A \times \frac{\sqrt{3}}{2} = A\sqrt{3}$.

---

**Câu 2 (Trắc nghiệm):** Trong phương pháp phasor (vectơ quay), hai sóng cùng tần số được biểu diễn là hai vectơ quay. Điều gì đúng về chuyển động của chúng?

A) Hai vectơ quay với vận tốc góc khác nhau, góc tương đối thay đổi theo thời gian
B) Hai vectơ tạo thành hệ cứng quay với cùng vận tốc góc $\omega$, góc tương đối cố định
C) Chỉ vectơ nào có biên độ lớn hơn mới quay, vectơ kia đứng yên
D) Cả hai vectơ đều đứng yên, chỉ tính hình chiếu tại $t = 0$

**Đáp án: B**

*Giải thích:* Vì hai sóng cùng tần số $\omega$, cả hai phasor quay với cùng vận tốc góc. Góc tương đối giữa chúng $= \phi_1 - \phi_2 = $ hằng số. Hệ hoạt động như một vật rắn quay, nên chỉ cần phân tích tại một thời điểm bất kỳ (thường chọn $t = 0$).

---

**Câu 3 (Trắc nghiệm):** Một hệ phased array radar gồm 2 anten cách nhau $d$, phát sóng bước sóng $\lambda$. Điều kiện để có cực đại chính theo phương $\theta$ là:

A) $d\cos\theta = m\lambda$ với $m$ nguyên
B) $d\sin\theta + \alpha/(2\pi) \cdot \lambda = m\lambda$ với $m$ nguyên
C) $d\sin\theta = \lambda/2$
D) $d\tan\theta = m\lambda$ với $m$ nguyên

**Đáp án: B**

*Giải thích:* Điều kiện giao thoa tăng cường là hiệu pha tổng bằng $2\pi m$. Hiệu pha tổng = pha hình học + pha nội tại $\alpha$: $\frac{2\pi d\sin\theta}{\lambda} + \alpha = 2\pi m$, suy ra $d\sin\theta + \alpha\lambda/(2\pi) = m\lambda$. Đây là cơ sở để điều khiển hướng chùm tia bằng cách thay đổi $\alpha$.

---

**Câu 4 (Tự luận):** Trong công việc thiết kế hệ thống đo lường chính xác (micrometer-level), bạn sử dụng cảm biến siêu âm hoặc laser interferometer để đo vị trí. Hãy giải thích nguyên lý hoạt động của **laser interferometer** (giao thoa kế laser) theo ngôn ngữ của bài học hôm nay — cụ thể là: hai sóng nào đang cộng với nhau, hiệu pha được tạo ra bởi yếu tố nào, và tại sao hệ thống có thể đo được chuyển dịch ở cấp độ nanomet?

**Gợi ý đáp án:**

Trong laser interferometer (ví dụ Michelson), chùm laser được chia thành hai nhánh bởi beam splitter:
- **Nhánh tham chiếu (reference arm):** phản xạ từ gương cố định, tạo sóng $E_1 = A\cos(\omega t + \phi_1)$
- **Nhánh đo lường (measurement arm):** phản xạ từ gương di động (gắn trên bề mặt cần đo), tạo sóng $E_2 = A\cos(\omega t + \phi_2)$

Khi hai nhánh gặp nhau tại detector, hiệu pha:
$$\Delta\phi = \phi_2 - \phi_1 = \frac{4\pi \Delta L}{\lambda}$$

Trong đó $\Delta L$ là độ dịch chuyển của gương đo. Hệ số 4 (không phải 2) vì ánh sáng đi và về (round trip). Với laser He-Ne ($\lambda = 633$ nm), mỗi khi $\Delta L = \lambda/4 = 158$ nm, $\Delta\phi$ thay đổi $\pi$ và cường độ đầu ra đảo từ cực đại sang cực tiểu. Bằng cách đếm số vân (fringe counting) và nội suy pha, hệ thống có thể phân giải chuyển dịch đến cấp $\lambda/1000 \approx 0.6$ nm — đây chính là lý do tại sao giao thoa kế laser là chuẩn đo lường tuyệt đối trong kỹ thuật chế tạo chính xác và kiểm định máy CNC.


---
*Exported from Feynman Bot*
