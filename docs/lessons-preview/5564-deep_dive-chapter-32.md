---
lesson_id: 5564
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:08.091811+00:00"
content_hash: 88116672744f
chapter_number: 32
chapter_title: Chapter 32
section_number: 4
section_title: 32–3Radiation damping
---
# ## Radiation Damping và Hệ Số Q Bức Xạ: Phân Tích Chuyên Sâu

*Source: Chapter 32 - Chapter 32 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_32.html)*

## Radiation Damping và Hệ Số Q Bức Xạ: Phân Tích Chuyên Sâu

### 1. Phương Trình Chuyển Động Của Dao Động Tử Có Bức Xạ

Một điện tích $q$ có khối lượng $m$ gắn vào lò xo hằng số $k = m\omega_0^2$ trong chân không tuân theo phương trình Newton. Nhưng do bức xạ điện từ, có thêm lực phản ứng bức xạ (radiation reaction force) - lực Abraham-Lorentz:

$$F_{\text{rad}} = \frac{q^2}{6\pi\varepsilon_0 c^3} \dddot{x}$$

Phương trình chuyển động đầy đủ:

$$m\ddot{x} = -m\omega_0^2 x + \frac{q^2}{6\pi\varepsilon_0 c^3}\dddot{x}$$

Đây là phương trình vi phân bậc 3, nổi tiếng vì có nghiệm "runaway" phi vật lý. Trong giới hạn lực bức xạ nhỏ (xấp xỉ tốt cho hầu hết hệ vật lý), ta thay $\dddot{x} \approx -\omega_0^2 \dot{x}$:

$$m\ddot{x} = -m\omega_0^2 x - \frac{q^2\omega_0^2}{6\pi\varepsilon_0 c^3}\dot{x}$$

Đây là phương trình dao động tắt dần quen thuộc với hệ số tắt dần:

$$\gamma_{\text{rad}} = \frac{q^2\omega_0^2}{6\pi\varepsilon_0 m c^3}$$

### 2. Tính Q Từ Các Nguyên Lý Đầu Tiên

Hệ số Q được định nghĩa qua:
$$Q = \frac{\omega_0 W}{P_{\text{rad}}}$$

Từ công thức Larmor, công suất bức xạ trung bình:
$$P_{\text{rad}} = \frac{q^2\omega_0^4 x_0^2}{12\pi\varepsilon_0 c^3}$$

Năng lượng toàn phần của dao động tử:
$$W = \frac{1}{2}m\omega_0^2 x_0^2$$

Do đó:
$$Q = \frac{\omega_0 \cdot \frac{1}{2}m\omega_0^2 x_0^2}{\frac{q^2\omega_0^4 x_0^2}{12\pi\varepsilon_0 c^3}} = \frac{6\pi\varepsilon_0 m c^3}{q^2\omega_0^2}$$

Quan hệ với hệ số tắt dần: $Q = \omega_0/\gamma_{\text{rad}}$, hoàn toàn nhất quán với lý thuyết dao động tắt dần.

### 3. Bán Kính Cổ Điển Của Electron

Định nghĩa **bán kính cổ điển của electron** $r_e$ qua điều kiện năng lượng tĩnh điện bằng năng lượng nghỉ:

$$\frac{e^2}{4\pi\varepsilon_0 r_e} = m_e c^2 \implies r_e = \frac{e^2}{4\pi\varepsilon_0 m_e c^2} \approx 2.82\times10^{-15}\,\text{m}$$

Viết lại hệ số tắt dần bằng $r_e$:
$$\gamma_{\text{rad}} = \frac{2}{3}\frac{r_e}{c}\omega_0^2$$

Và Q:
$$Q = \frac{3}{2}\frac{c}{r_e \omega_0} = \frac{3\lambda}{4\pi r_e}$$

Với ánh sáng khả kiến $\lambda \sim 500\,\text{nm}$ và $r_e \sim 2.82\times10^{-15}\,\text{m}$:
$$Q \approx \frac{3 \times 500\times10^{-9}}{4\pi \times 2.82\times10^{-15}} \approx 4.2\times10^7$$

Kết quả: $Q \sim 10^7 - 10^8$ tùy bước sóng, phù hợp thực nghiệm.

### 4. Thời Gian Sống và Độ Rộng Vạch Phổ

Từ $W(t) = W_0 e^{-\omega_0 t/Q} = W_0 e^{-\gamma_{\text{rad}} t}$, thời gian sống:

$$\tau = \frac{1}{\gamma_{\text{rad}}} = \frac{Q}{\omega_0} = \frac{6\pi\varepsilon_0 m_e c^3}{e^2\omega_0^2}$$

Với $\omega_0 = 3.77\times10^{15}\,\text{rad/s}$ (ánh sáng xanh lá, $\lambda = 500\,\text{nm}$):
$$\tau \approx \frac{6\pi \times 8.85\times10^{-12} \times 9.11\times10^{-31} \times (3\times10^8)^3}{(1.6\times10^{-19})^2 \times (3.77\times10^{15})^2} \approx 11\,\text{ns}$$

Do dao động tử tắt dần theo hàm mũ, biên độ dao động có dạng $E(t) = E_0 e^{-t/2\tau} \cos(\omega_0 t)$. Phổ Fourier của hàm này cho **profil Lorentzian**:

$$I(\omega) \propto \frac{1}{(\omega-\omega_0)^2 + (1/2\tau)^2}$$

Độ rộng bán biên (FWHM - Full Width at Half Maximum):
$$\Delta\omega_{\text{natural}} = \frac{1}{\tau} = \gamma_{\text{rad}} \approx 10^8\,\text{rad/s}$$

Hoặc: $\Delta f_{\text{natural}} = \Delta\omega/(2\pi) \approx 15\,\text{MHz}$.

### 5. So Sánh Các Cơ Chế Làm Rộng Vạch Phổ

Trong thực tế, độ rộng vạch phổ quan sát được thường lớn hơn nhiều so với độ rộng tự nhiên:

| Cơ chế | Độ rộng điển hình | Nguyên nhân |
|--------|-------------------|-------------|
| Tự nhiên (radiation damping) | $\sim 10\,\text{MHz}$ | Tắt dần do bức xạ |
| Doppler (nhiệt độ phòng) | $\sim 1\,\text{GHz}$ | Chuyển động nhiệt của nguyên tử |
| Va chạm (áp suất) | $\sim 100\,\text{MHz/atm}$ | Va chạm nguyên tử-nguyên tử |
| Stark (điện trường) | Thay đổi nhiều | Perturbation năng lượng |

Dộ rộng tự nhiên là giới hạn dưới **vật lý cơ bản** không thể vượt qua bằng bất kỳ kỹ thuật nào.

### 6. Ứng Dụng: Đồng Hồ Nguyên Tử và Tiêu Chuẩn Tần Số

Trong đồng hồ nguyên tử caesium (Cs-133), vạch hyperfine ở $9.192631770\,\text{GHz}$ có $\tau \sim$ mili-giây (chuyển tiếp từ trạng thái cơ bản), dẫn đến:
$$\Delta f_{\text{natural}} = 1/(2\pi\tau) \sim 160\,\text{Hz}$$

Với $f_0 \approx 9.2\,\text{GHz}$, độ phân giải tần số:
$$\delta f/f_0 \sim 160/(9.2\times10^9) \approx 10^{-11}$$

Đây là lý do đồng hồ nguyên tử có độ chính xác $\sim 10^{-14}$ đến $10^{-16}$ (cải thiện thêm bằng kỹ thuật fountain và laser cooling để giảm Doppler broadening).

Trong đo lường vũ khí chính xác cao: GPS dựa trên đồng hồ Cs với sai số thời gian $< 100\,\text{ns}$, tương đương sai số vị trí $< 30\,\text{m}$. Các hệ thống dẫn đường quán tính (INS) kết hợp GPS cần biết chính xác $\tau$ của các chuẩn tần số để hiệu chuẩn drift.

### Kết Luận

Tắt dần do bức xạ là cơ chế vật lý sâu sắc: nó nối liền điện động học cổ điển với cấu trúc nguyên tử, giải thích thời gian sống trạng thái kích thích, và đặt ra giới hạn cơ bản cho mọi phép đo tần số-thời gian chính xác. Hệ số Q bức xạ $\sim 10^8$ của electron ánh sáng khả kiến là con số đẹp nối liền thế giới vĩ mô (mạch dao động, anten) với thế giới vi mô (nguyên tử, photon).

---
*Exported from Feynman Bot*
