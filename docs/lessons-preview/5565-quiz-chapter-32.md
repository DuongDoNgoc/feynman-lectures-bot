---
lesson_id: 5565
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:08.113786+00:00"
content_hash: 941fb9fbff89
chapter_number: 32
chapter_title: Chapter 32
section_number: 4
section_title: 32–3Radiation damping
---
# ## Bài Kiểm Tra: Tắt Dần Do Bức Xạ và Hệ Số Q

*Source: Chapter 32 - Chapter 32 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_32.html)*

## Bài Kiểm Tra: Tắt Dần Do Bức Xạ và Hệ Số Q

**Câu 1.** Tại sao một điện tích dao động trong chân không tuyệt đối (không có ma sát hay môi trường) vẫn tắt dần theo thời gian?

A) Do lực hút hấp dẫn từ các vật thể xung quanh làm mất năng lượng
B) Do điện tích bức xạ sóng điện từ mang theo năng lượng ra khỏi hệ thống
C) Do dao động nhiệt của chính điện tích làm phân tán năng lượng
D) Do hiệu ứng lượng tử, điện tích không thể dao động mãi mãi

**Đáp án: B**
*Giải thích:* Theo điện động học cổ điển, bất kỳ điện tích nào có gia tốc đều bức xạ sóng điện từ (công thức Larmor). Một điện tích dao động liên tục có gia tốc, do đó liên tục bức xạ năng lượng. Năng lượng này lấy từ năng lượng dao động của hệ, khiến biên độ giảm dần - đây là tắt dần do bức xạ (radiation damping).

---

**Câu 2.** Hệ số Q của một dao động tử được định nghĩa là $Q = \omega_0 W / P_{\text{rad}}$. Nếu electron trong nguyên tử có $Q \approx 10^8$ và tần số dao động $\omega_0 = 3\times10^{15}\,\text{rad/s}$, thời gian sống (thời gian để năng lượng giảm $e$ lần) là:

A) $\tau \approx 3\times10^7\,\text{s}$ (gần 1 năm)
B) $\tau \approx 33\,\mu\text{s}$
C) $\tau \approx 33\,\text{ns}$
D) $\tau \approx 33\,\text{ps}$

**Đáp án: C**
*Giải thích:* $\tau = Q/\omega_0 = 10^8 / (3\times10^{15}\,\text{rad/s}) = 3.33\times10^{-8}\,\text{s} \approx 33\,\text{ns}$. Đây là thang thời gian phát xạ tự nhiên điển hình của các nguyên tử trong thực nghiệm, xác nhận tính đúng đắn của lý thuyết cổ điển.

---

**Câu 3.** Hệ số Q bức xạ của electron phụ thuộc vào tần số dao động $\omega_0$ theo quy luật nào?

A) $Q \propto \omega_0^4$
B) $Q \propto \omega_0^2$
C) $Q \propto \omega_0^{-2}$
D) $Q \propto \omega_0^{-1}$

**Đáp án: C**
*Giải thích:* Từ công thức $Q = 6\pi\varepsilon_0 m c^3/(q^2\omega_0^2)$, rõ ràng $Q \propto \omega_0^{-2}$. Nghĩa là tần số càng cao (như tia X, UV), Q càng nhỏ, điện tử phát năng lượng càng nhanh. Ngược lại, sóng radio tần số thấp có Q rất cao (electron mất năng lượng rất chậm qua bức xạ điện từ).

---

**Câu 4 (Tự luận).** Trong một hệ thống cộng hưởng MEMS (Micro-Electro-Mechanical System) mà bạn thiết kế để đo gia tốc với độ chính xác nano-g, hệ số Q của bộ cộng hưởng ảnh hưởng đến hiệu suất đo lường như thế nào? Hãy so sánh với hệ số Q bức xạ của electron nguyên tử.

*Gợi ý trả lời:* Q cao trong MEMS gia tốc kế mang lại:
(1) **Độ nhạy tốt hơn**: Q cao nghĩa là đáp ứng cộng hưởng có biên độ lớn hơn với cùng lực kích thích, dễ đo hơn.
(2) **Nhiễu thấp hơn**: Theo Fluctuation-Dissipation theorem, nhiễu nhiệt (thermal noise) của bộ cộng hưởng tỉ lệ nghịch với Q: $S_x(f) \propto k_BT/(Q m\omega_0^3)$. Q cao $\to$ nhiễu thấp $\to$ độ phân giải gia tốc tốt hơn.
(3) **Thời gian ổn định dài hơn**: Tắt dần chậm ($\tau = Q/\omega_0$ lớn) nghĩa là phải chờ lâu hơn sau mỗi nhiễu loạn. Trong đo lường động (dynamic measurement), Q quá cao làm đáp ứng chậm, hạn chế băng thông. Tương tự như Q bức xạ electron ($\sim 10^8$), MEMS chân không có thể đạt $Q \sim 10^6$ - cùng chế độ, nhưng do cơ chế vật lý khác (clamping loss, thermoelastic damping thay vì radiation damping).


---
*Exported from Feynman Bot*
