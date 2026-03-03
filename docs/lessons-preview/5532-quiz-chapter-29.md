---
lesson_id: 5532
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:07.291973+00:00"
content_hash: ee2840bf1b25
chapter_number: 29
chapter_title: Chapter 29
section_number: 2
section_title: 29–1Electromagnetic waves
---
# ## Kiểm Tra: Toán Học Trường Bức Xạ và Giao Thoa Sóng Điện Từ

*Source: Chapter 29 - Chapter 29 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_29.html)*

## Kiểm Tra: Toán Học Trường Bức Xạ và Giao Thoa Sóng Điện Từ

**Câu 1:** Trường bức xạ của một điện tích dao động điều hòa $a(t) = a_0\cos(\omega t)$ tại điểm quan sát cách xa $r$, góc $\theta$ so với trục dao động có dạng:

A) $E \propto a_0 \cos(\omega t) / r^2$
B) $E \propto a_0 \sin\theta \cos(\omega t - r/c) / r$
C) $E \propto a_0 \cos\theta \cos(\omega t - kr) / r$
D) $E \propto a_0 \sin\theta / r^2$

**Đáp án: B**
Giải thích: Trường bức xạ tỉ lệ với $\sin\theta$ (không phải $\cos\theta$), giảm theo $1/r$ (không phải $1/r^2$), và mang yếu tố thời gian trễ $t - r/c$ trong argument của cosine. Đây phản ánh ba đặc trưng quan trọng: sự phụ thuộc góc dạng dipole ($\sin\theta$), bản chất sóng truyền đi xa ($1/r$), và nguyên lý nhân quả (thời gian trễ). Chú ý: $r/c = kr/\omega$, nên $\cos(\omega t - r/c) = \cos(\omega t - kr)$ — hai cách viết tương đương.

---

**Câu 2:** Hai nguồn bức xạ cùng pha, cách nhau $d = \lambda/2$ (nửa bước sóng). Cường độ bức xạ theo phương vuông góc với đường nối hai nguồn ($\theta = 90°$) bằng bao nhiêu lần so với một nguồn đơn?

A) 0 (triệt tiêu hoàn toàn)
B) 1 (bằng một nguồn đơn)
C) 2 (gấp đôi)
D) 4 (gấp bốn)

**Đáp án: D**
Giải thích: Với $d = \lambda/2$, hai nguồn cùng pha nhìn từ phương vuông góc ($\theta = 90°$ so với trục nối hai nguồn) đều cùng khoảng cách đến điểm quan sát. Độ lệch đường đi bằng 0, nên hai sóng cộng pha nhau hoàn toàn: $E_{total} = 2E_0$. Cường độ tỉ lệ với $E^2$, nên $I = (2E_0)^2 = 4E_0^2$ — gấp bốn lần cường độ của một nguồn đơn ($I_0 = E_0^2$). Đây là constructive interference hoàn toàn.

---

**Câu 3:** Trong hệ thống phased array với $N$ phần tử, khi tăng số phần tử $N$ lên gấp đôi (giữ nguyên tổng khẩu độ $L = Nd = const$) thì:

A) Beamwidth giảm một nửa, peak gain tăng gấp đôi
B) Beamwidth không đổi, peak gain tăng gấp bốn
C) Beamwidth và peak gain đều không đổi
D) Beamwidth không đổi, peak gain tăng gấp đôi

**Đáp án: D**
Giải thích: Beamwidth xấp xỉ $\Delta\theta \approx \lambda/L$ — chỉ phụ thuộc tổng khẩu độ $L$, không phụ thuộc số phần tử $N$. Tuy nhiên khi $N$ tăng gấp đôi mà $L$ không đổi, khoảng cách giữa phần tử $d = L/N$ giảm một nửa. Điều này không ảnh hưởng beamwidth nhưng loại bỏ grating lobes (giả thuyết $d < \lambda/2$ được thỏa mãn tốt hơn). Peak gain xấp xỉ tỉ lệ với $N$ (tổng số phần tử bức xạ), nên tăng gấp đôi.

---

**Câu 4 (Tự luận):** Trong thiết kế hệ thống radar dẫn đường cho vũ khí chính xác cao, bạn cần phân biệt hai mục tiêu cách nhau 10 cm ở khoảng cách 1000 m. Tính góc phân giải cần thiết, và từ đó xác định khẩu độ anten tối thiểu cần dùng nếu radar hoạt động ở tần số 77 GHz (millimeter wave). Nêu các yếu tố thực tế có thể ảnh hưởng đến khả năng đạt được giá trị lý thuyết này.

**Hướng dẫn trả lời:**

Góc phân giải cần thiết: $\Delta\theta = 0.1 \text{ m} / 1000 \text{ m} = 10^{-4}$ rad = 0.1 mrad.

Bước sóng tại 77 GHz: $\lambda = c/f = 3\times10^8 / 77\times10^9 \approx 3.9 \text{ mm}$.

Khẩu độ tối thiểu từ tiêu chuẩn Rayleigh: $L = \lambda/\Delta\theta = 3.9 \times 10^{-3} / 10^{-4} = 39 \text{ m}$.

Đây là anten rất lớn. Trong thực tế, hệ thống SAR (Synthetic Aperture Radar) trên UAV hay vệ tinh tổng hợp khẩu độ ảo bằng cách di chuyển anten theo thời gian, tạo ra khẩu độ hiệu dụng lớn hơn nhiều anten thật. Các yếu tố ảnh hưởng thực tế: nhiễu nhiệt (noise floor), clutter từ nền đất, multipath reflection, hiệu ứng khí quyển làm lệch pha, và giới hạn SNR (signal-to-noise ratio).


---
*Exported from Feynman Bot*
