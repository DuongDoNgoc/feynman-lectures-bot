---
lesson_id: 5559
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:07.982091+00:00"
content_hash: dd5658bd6be4
chapter_number: 31
chapter_title: Chapter 31
section_number: 5
section_title: 31–4Absorption
---
# ## Bài Kiểm Tra: Chỉ Số Khúc Xạ Phức và Hấp Thụ Ánh Sáng

*Source: Chapter 31 - Chapter 31 (Section 5) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_31.html)*

## Bài Kiểm Tra: Chỉ Số Khúc Xạ Phức và Hấp Thụ Ánh Sáng

**Câu 1.** Khi chỉ số khúc xạ của vật liệu là số phức $n = n' - in''$, phần ảo $n''$ đặc trưng cho hiện tượng nào sau đây?

A) Sự thay đổi tốc độ pha của ánh sáng trong vật liệu
B) Sự hấp thụ năng lượng của ánh sáng khi truyền qua vật liệu
C) Sự phân tán (tán sắc) của ánh sáng trắng thành các màu
D) Sự phản xạ toàn phần tại bề mặt vật liệu

**Đáp án: B**
*Giải thích:* Phần ảo $n''$ xuất hiện do lực cản (damping) trong vật liệu. Nó làm biên độ sóng giảm theo hàm mũ $e^{-\omega n'' z/c}$ khi truyền qua vật liệu - đây chính là hấp thụ. Phần thực $n'$ mới mô tả tốc độ pha và tán sắc.

---

**Câu 2.** Một tia laser bước sóng $\lambda = 500\,\text{nm}$ truyền qua tấm kính có $n'' = 0.01$ và độ dày $\Delta z = 1\,\text{cm}$. Tỉ số cường độ ra/vào $I_{out}/I_{in}$ xấp xỉ bằng bao nhiêu? (Cho $\alpha = 2\omega n''/c$, $c = 3\times10^8\,\text{m/s}$)

A) $e^{-2513}$ (gần bằng 0)
B) $e^{-2.51}\approx 0.081$
C) $e^{-0.00251}\approx 0.997$
D) $e^{-251}$ (gần bằng 0)

**Đáp án: B**
*Giải thích:* $\omega = 2\pi c/\lambda = 2\pi \times 3\times10^8 / 500\times10^{-9} \approx 3.77\times10^{15}\,\text{rad/s}$. Hệ số suy giảm $\alpha = 2\omega n''/c = 2 \times 3.77\times10^{15} \times 0.01 / (3\times10^8) \approx 2.51\times10^5\,\text{m}^{-1}$. Với $\Delta z = 0.01\,\text{m}$: $\alpha \Delta z \approx 2.51$. Do đó $I_{out}/I_{in} = e^{-2.51} \approx 0.081$.

---

**Câu 3.** Theo phương trình tán sắc, phần ảo $n''$ của chỉ số khúc xạ đạt cực đại khi nào?

A) Khi tần số ánh sáng bằng một nửa tần số cộng hưởng ($\omega = \omega_0/2$)
B) Khi tần số ánh sáng bằng tần số cộng hưởng ($\omega = \omega_0$)
C) Khi tần số ánh sáng lớn hơn tần số cộng hưởng ($\omega \gg \omega_0$)
D) Khi tần số ánh sáng rất nhỏ ($\omega \to 0$)

**Đáp án: B**
*Giải thích:* Biểu thức $n'' \propto \gamma\omega / [(\omega_0^2-\omega^2)^2 + \gamma^2\omega^2]$ đạt cực đại khi $(\omega_0^2-\omega^2)^2$ nhỏ nhất, tức khi $\omega \approx \omega_0$. Đây là tần số cộng hưởng, nơi electron hấp thụ năng lượng mạnh nhất từ sóng điện từ.

---

**Câu 4 (Tự luận).** Trong hệ thống đo lường quang học chính xác cao mà bạn thiết kế (ví dụ: laser interferometer đo dịch chuyển ở mức micrometer), tại sao phải kiểm soát thành phần khí trong đường quang học? Hãy giải thích dựa trên khái niệm chỉ số khúc xạ phức.

*Gợi ý trả lời:* Không khí có $n' > 1$ (khoảng 1.0003) và $n'' > 0$ (dù rất nhỏ). Sự thay đổi nhiệt độ, áp suất, độ ẩm làm thay đổi $n'$, gây ra sai số pha tương đương với sai số dịch chuyển. Quan trọng hơn, các phân tử nước và CO$_2$ có tần số cộng hưởng trong vùng IR làm $n''$ lớn ở một số bước sóng laser. Điều này làm suy giảm cường độ tín hiệu, giảm contrast vân giao thoa và tăng noise. Các interferometer chính xác cao (như trong máy photolithography chip bán dẫn) dùng đường quang học chân không hoặc kiểm soát nghiêm ngặt môi trường khí để $n' = 1$ và $n'' = 0$.


---
*Exported from Feynman Bot*
