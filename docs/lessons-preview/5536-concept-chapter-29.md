---
lesson_id: 5536
lesson_type: concept
approval_status: approved
exported_at: "2026-03-03T15:33:07.380247+00:00"
content_hash: 95045ce5a93c
chapter_number: 29
chapter_title: Chapter 29
section_number: 6
section_title: 29–5The mathematics of interference
---
# ## Phasor và Nghệ Thuật Cộng Sóng: Từ Lượng Giác đến Số Phức

*Source: Chapter 29 - Chapter 29 (Section 6) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_29.html)*

## Phasor và Nghệ Thuật Cộng Sóng: Từ Lượng Giác đến Số Phức

Khi thiết kế mạch lọc cho bộ điều khiển PID của servo motor, bạn thường xuyên làm việc với Bode plot — biểu đồ cho thấy biên độ và pha của tín hiệu theo tần số. Bạn có biết rằng phép phân tích này, bao gồm cả notation số phức $H(j\omega)$, bắt nguồn từ cùng bài toán mà Feynman trình bày trong chương này không? Bài toán: làm thế nào để cộng nhiều dao động điều hòa cùng tần số nhưng khác pha? Câu trả lời dẫn đến một trong những phát minh toán học đẹp nhất trong vật lý: phương pháp phasor.

**Bài toán cụ thể**

Xét hai nguồn sóng dao động cùng tần số $\omega$, biên độ bằng nhau $A$, nhưng pha ban đầu lần lượt là $\phi_1$ và $\phi_2$. Ta cần tìm tổng:
$$R(t) = A\cos(\omega t + \phi_1) + A\cos(\omega t + \phi_2)$$

Cách cổ điển: dùng công thức tổng cosine:
$$R(t) = 2A\cos\left(\frac{\phi_1 - \phi_2}{2}\right)\cos\left(\omega t + \frac{\phi_1 + \phi_2}{2}\right)$$

Kết quả là một sóng mới: cùng tần số $\omega$, biên độ $R_A = 2A\cos\left(\frac{\phi_1 - \phi_2}{2}\right)$, pha trung bình $\bar{\phi} = (\phi_1 + \phi_2)/2$. Điều này đúng nhưng khó mở rộng cho nhiều nguồn hơn.

**Phương pháp Phasor: Từ sóng đến vector**

Ý tưởng thiên tài: mỗi dao động điều hòa $A\cos(\omega t + \phi)$ có thể được biểu diễn bởi một **phasor** — vector quay với tốc độ $\omega$ trong mặt phẳng phức. Phần thực của vector này theo thời gian chính là dao động vật lý.

Phasor của sóng thứ nhất: $\tilde{A}_1 = Ae^{i\phi_1}$ (vector độ dài $A$, góc $\phi_1$)
Phasor của sóng thứ hai: $\tilde{A}_2 = Ae^{i\phi_2}$ (vector độ dài $A$, góc $\phi_2$)

Vì cả hai đều quay cùng tốc độ $\omega$, góc giữa chúng luôn không đổi. Phasor tổng:
$$\tilde{R} = \tilde{A}_1 + \tilde{A}_2$$

Đây là phép cộng vector đơn giản! Biên độ kết quả là độ dài của vector tổng $|\tilde{R}|$, pha kết quả là góc của vector tổng với trục thực.

**Trực giác hình học**

Hình dung: hai vector từ gốc tọa độ, mỗi vector độ dài $A$, góc giữa chúng là $\Delta\phi = \phi_1 - \phi_2$. Vector tổng là đường chéo hình bình hành. Khi $\Delta\phi = 0$ (cùng pha): hai vector cùng hướng, tổng có độ dài $2A$. Khi $\Delta\phi = \pi$ (ngược pha): hai vector ngược chiều, tổng triệt tiêu. Khi $\Delta\phi = \pi/2$: tổng có độ dài $A\sqrt{2}$ (Pythagoras). Bằng mắt thường, bạn có thể ước tính biên độ kết quả của bất kỳ tổ hợp pha nào.

**Phép ẩn dụ cho kỹ sư cơ điện tử**

Phasor trong vật lý sóng chính là tiền thân của **phasor trong mạch điện xoay chiều** (AC circuit analysis). Impedance $Z = R + jX$ là một phasor: phần thực là điện trở (dissipative, cùng pha với dòng), phần ảo là reactance (storage, lệch pha 90°). Hàm truyền $H(j\omega)$ của bộ lọc là tỉ số phasor đầu ra/đầu vào. Khi bạn vẽ Nyquist plot hay Bode plot, bạn đang vẽ quỹ tích của phasor $H(j\omega)$ khi $\omega$ thay đổi.

Như vậy, từ bài toán cộng sóng điện từ của hai anten, Feynman đưa ta đến nền tảng toán học của toàn bộ lý thuyết mạch tuyến tính — cùng một ngôn ngữ toán học, hai ứng dụng hoàn toàn khác nhau.

**Tổng quát hóa: N nguồn**

Sức mạnh thực sự của phasor thể hiện khi có nhiều nguồn. Với N nguồn:
$$\tilde{R} = \sum_{n=1}^{N} A_n e^{i\phi_n}$$

Về mặt hình học: ta nối N vector đầu đuôi, vector kết quả là dây cung từ đầu đến cuối. Khi $N \to \infty$ và mỗi vector nhỏ dần, chuỗi vector trở thành một đường cong — và biên độ kết quả là chiều dài dây cung. Đây là cách Feynman tính tích phân Huygens-Fresnel trong bài toán nhiễu xạ ánh sáng qua khe.

**Tại sao điều này quan trọng trong thực tế?**

Trong thiết kế hệ thống điều khiển cho thiết bị đo lường chính xác micro-mét:
- Noise rejection: phasor cho thấy nhiễu từ nhiều nguồn cộng ngẫu nhiên ($\Delta\phi$ random) dẫn đến $R_A \propto \sqrt{N}$ (coherent: $R_A \propto N$) — cơ sở của average và lock-in amplifier
- Phase margin: trong phân tích ổn định Bode, phasor $H(j\omega)$ xác định độ dự trữ pha của vòng lặp điều khiển
- Signal reconstruction: trong ADC, các harmonic được biểu diễn bằng phasor, FFT là phép tính tổng phasor song song

**Điểm mấu chốt**

- Tổng của hai dao động cùng tần số luôn là dao động cùng tần số đó, với biên độ và pha mới
- Biên độ kết quả phụ thuộc vào hiệu pha: max khi cùng pha, min khi ngược pha
- Phasor (vector phức) biến bài toán cộng sóng thành cộng vector — mạnh mẽ và trực quan
- Cùng toán học phasor làm nền tảng cho phân tích mạch AC, Bode plot, phased array anten, và FFT — tất cả đều là biến thể của cùng một ý tưởng

---
*Exported from Feynman Bot*
