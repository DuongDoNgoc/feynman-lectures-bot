---
lesson_id: 5562
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:08.047404+00:00"
content_hash: 33be03721600
chapter_number: 32
chapter_title: Chapter 32
section_number: 1
section_title: 32Radiation Damping. Light Scattering
---
# ## Bài Kiểm Tra: Trở Kháng Bức Xạ và Công Suất Bức Xạ

*Source: Chapter 32 - Chapter 32 (Section 1) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_32.html)*

## Bài Kiểm Tra: Trở Kháng Bức Xạ và Công Suất Bức Xạ

**Câu 1.** Theo công thức Larmor, công suất bức xạ từ một điện tích dao động tỉ lệ với tần số dao động theo lũy thừa nào?

A) $\omega^1$
B) $\omega^2$
C) $\omega^3$
D) $\omega^4$

**Đáp án: D**
*Giải thích:* Công thức Larmor cho gia tốc dao động điều hòa: $P = q^2\langle a^2\rangle/(6\pi\varepsilon_0 c^3)$. Vì $a = -\omega^2 x_0\cos(\omega t)$, nên $\langle a^2\rangle = \omega^4 x_0^2/2$, dẫn đến $P \propto \omega^4$. Đây cũng là lý do bầu trời có màu xanh (Rayleigh scattering): ánh sáng tần số cao bị tán xạ mạnh hơn gấp $\sim 10$ lần ánh sáng đỏ.

---

**Câu 2.** Trở kháng bức xạ $R_{\text{rad}}$ của một anten được định nghĩa như thế nào và ý nghĩa vật lý của nó là gì?

A) Điện trở do dây dẫn anten tỏa nhiệt, biến năng lượng thành nhiệt
B) Tổng trở kháng của mạch nguồn cộng với trở kháng anten
C) Giá trị điện trở tương đương mà nguồn điện "nhìn thấy" khi anten bức xạ công suất ra không gian
D) Điện trở giữa hai đầu anten khi không bức xạ

**Đáp án: C**
*Giải thích:* $R_{\text{rad}}$ được định nghĩa qua $P_{\text{rad}} = I_0^2 R_{\text{rad}}/2$. Nó không liên quan đến sự tỏa nhiệt mà là đại lượng mô tả "tải" mà anten đặt lên nguồn điện do công suất bị bức xạ ra không gian. Từ góc độ bảo toàn năng lượng, nguồn điện phải cấp năng lượng, và $R_{\text{rad}}$ mô tả điều đó trong ngôn ngữ mạch điện.

---

**Câu 3.** Hệ số Q của một nguyên tử hydrogen phát sáng (electron dao động ở tần số ánh sáng khả kiến $\omega_0 \sim 3\times10^{15}\,\text{rad/s}$) theo cơ chế bức xạ điện từ cổ điển vào khoảng:

A) $Q \sim 10^2$
B) $Q \sim 10^5$
C) $Q \sim 10^8$
D) $Q \sim 10^{12}$

**Đáp án: C**
*Giải thích:* $Q_{\text{rad}} = 6\pi\varepsilon_0 m_e c^3/(e^2\omega_0^2)$. Thay số với $m_e = 9.11\times10^{-31}\,\text{kg}$, $e = 1.6\times10^{-19}\,\text{C}$, $\omega_0 \sim 3\times10^{15}\,\text{rad/s}$, ta được $Q \sim 10^8$. Điều này có nghĩa electron cần khoảng $10^8$ chu kỳ dao động (tương đương $\sim 10\,\text{ns}$) để bức xạ phần lớn năng lượng - phù hợp với thực nghiệm về thời gian sống trạng thái kích thích nguyên tử.

---

**Câu 4 (Tự luận).** Trong thiết kế anten cho hệ thống radar điều hướng (tracking radar) sử dụng trong vũ khí dẫn đường, hai thông số $R_{\text{rad}}$ và $Q$ có tầm quan trọng như thế nào? Hãy phân tích từ góc độ kỹ sư thiết kế hệ thống đo lường chính xác.

*Gợi ý trả lời:* Radar điều hướng cần:
(1) **$R_{\text{rad}}$ lớn** để hiệu suất bức xạ cao ($\eta = R_{\text{rad}}/(R_{\text{rad}}+R_{\text{loss}})$ gần 1), giảm tổn thất nhiệt, tăng tầm xa và giảm thời gian lộ diện.
(2) **Q thấp** để băng thông rộng: radar pulse thường dùng xung ngắn (tăng độ phân giải cự ly), xung ngắn trong miền thời gian tương đương băng thông rộng trong miền tần số ($\Delta f = 1/\tau_{pulse}$). Anten Q cao sẽ lọc mất năng lượng ở biên tần, làm méo dạng xung và giảm độ phân giải. Ngoài ra, anten mảng pha (phased array) giúp tổng hợp $R_{\text{rad}}$ từ nhiều phần tử, vừa tăng hiệu suất vừa cho phép quét búp sóng điện tử không cần cơ cấu xoay cơ học.


---
*Exported from Feynman Bot*
