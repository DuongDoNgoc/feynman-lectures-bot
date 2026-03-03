---
lesson_id: 5585
lesson_type: deep_dive
approval_status: pending
exported_at: "2026-03-03T15:33:08.599560+00:00"
content_hash: f3c9136f26aa
chapter_number: 34
chapter_title: Chapter 34
section_number: 7
section_title: 34–6The Doppler effect
---
# ## Hiệu Ứng Doppler: Phân Tích Toán Học Đầy Đủ và Ứng Dụng Kỹ Thuật

*Source: Chapter 34 - Chapter 34 (Section 7) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_34.html)*

## Hiệu Ứng Doppler: Phân Tích Toán Học Đầy Đủ và Ứng Dụng Kỹ Thuật

### 1. Thiết Lập Bài Toán: Oscillator Chuyển Động

Xét một oscillator điện tử dao động với tần số $\omega_1$ và chuyển động với vận tốc $v$ dọc theo trục $x$ về phía người quan sát ở vô cực (hướng $-x$).

**Tọa độ thực của oscillator:**
$$x(t) = -vt + A\sin(\omega_1 t)$$

(phần $-vt$ là chuyển động tịnh tiến, $A\sin(\omega_1 t)$ là dao động)

**Theo trick của Feynman** — "trượt" đồ thị: biến đổi sang trục thời gian trễ $	au = t + x(t)/c$ (thời gian retarded):

Trong khoảng thời gian $\Delta	au$, nguồn đã chuyển động $v\Delta	au$ về phía người quan sát. Điều này nén toàn bộ các chu kỳ dao động từ khoảng $\Delta	au$ xuống còn $\Delta t = (1 - v/c)\Delta	au$.

Số chu kỳ dao động trong $\Delta	au$ ở nguồn = số chu kỳ trong $\Delta t$ ở người quan sát:
$$\omega_1 \Delta	au = \omega_{obs} \Delta t = \omega_{obs}(1-v/c)\Delta	au$$

Suy ra:
$$oxed{\omega_{obs} = rac{\omega_1}{1 - v/c}}$$

### 2. Doppler Relativistic: Kết Hợp Time Dilation

Ở vận tốc cao ($v \sim c$), phải tính thêm time dilation. Đồng hồ của nguồn chuyển động chạy chậm hơn một factor $\gamma = 1/\sqrt{1-v^2/c^2}$ so với đồng hồ của người quan sát. Do đó tần số phát trong hệ lab thực sự là $\omega_1/\gamma$.

Công thức Doppler relativistic đầy đủ (nguồn tiến lại theo phương trực tiếp):

$$\omega_{obs} = rac{\omega_1/\gamma}{1 - v/c} = \omega_1 rac{\sqrt{1-v^2/c^2}}{1-v/c} = \omega_1\sqrt{rac{1+v/c}{1-v/c}}$$

**Giới hạn kiểm tra:**
- $v = 0$: $\omega_{obs} = \omega_1$ ✓
- $v 	o c$: $\omega_{obs} 	o \infty$ (blueshift cực lớn) ✓
- $v 	o -c$: $\omega_{obs} 	o 0$ (redshift hoàn toàn) ✓

### 3. Transverse Doppler Effect

Điều thú vị: ngay cả khi nguồn chuyển động **vuông góc** với đường nhìn ($	heta = 90°$), vẫn có Doppler shift thuần túy tương đối tính:

$$\omega_{obs} = rac{\omega_1}{\gamma} = \omega_1\sqrt{1-v^2/c^2}$$

Đây là **transverse Doppler effect** — không tồn tại trong âm thanh (Doppler âm thanh bằng 0 khi $	heta = 90°$). Nó là bằng chứng trực tiếp của time dilation tương đối tính.

**Công thức tổng quát** cho góc $	heta$ giữa vận tốc nguồn và đường nhìn:

$$\omega_{obs} = rac{\omega_1}{\gamma(1 - eta\cos	heta)}$$

với $eta = v/c$.

### 4. Ứng Dụng 1: Laser Doppler Vibrometer (LDV) — Phân Tích Chi Tiết

**Nguyên lý:** Chùm laser chiếu vào bề mặt rung. Ánh sáng phản xạ bị Doppler shift $\pm 2v(t)/\lambda$ (hệ số 2 do đường đi kép: đến và về).

**Sơ đồ giao thoa kế Mach-Zehnder:**

1. Laser phát tần số $f_0$
2. Beamsplitter tách thành: Reference beam ($f_0$) và Signal beam ($f_0$)
3. Signal beam chiếu vào mục tiêu rung với $v(t)$: phản xạ có tần số $f_0 + \Delta f(t)$ với $\Delta f = 2v(t)/\lambda$
4. Reference và Signal beam giao thoa tại photodetector
5. Photocurrent có thành phần: $I \propto \cos(2\pi\Delta f(t) \cdot t + \phi_0)$ — tín hiệu FM
6. Giải điều chế FM: thu được $\Delta f(t) = 2v(t)/\lambda$ → tính được $v(t)$
7. Tích phân: $x(t) = \int v(t)dt$ — dịch chuyển với độ phân giải nanometer

**Vấn đề thực tế — direction ambiguity:** Khi $v(t)$ thay đổi dấu (bề mặt rung qua điểm không), tần số Doppler shift cũng thay đổi dấu. Nếu dùng giao thoa kế đơn giản, không phân biệt được chiều dương và chiều âm (do $|cos|$ symmetric).

**Giải pháp — Heterodyne detection:** Thêm AOM (Acousto-Optic Modulator) vào nhánh reference, dịch tần số reference thêm $f_{AOM} = 40$ MHz. Signal beam vẫn là $f_0 + \Delta f(t)$. Tín hiệu beat:

$$f_{beat} = f_{AOM} + \Delta f(t) = 40	ext{ MHz} \pm rac{2v(t)}{\lambda}$$

Bây giờ $f_{beat}$ luôn dương, và chiều của $v(t)$ được xác định bởi $f_{beat} > 40$ MHz hay $< 40$ MHz.

### 5. Ứng Dụng 2: Radar Doppler trong Hệ Thống Vũ Khí

**Fuze Doppler (proximity fuse):** Đầu đạn phát sóng radio tần số $f_0$, sóng phản xạ từ mục tiêu có Doppler shift $\Delta f = 2v_{closure}/\lambda$ (với $v_{closure}$ là tốc độ đến gần). Khi $\Delta f$ tương ứng với khoảng cách mong muốn kích nổ, fuze phát tín hiệu nổ. Độ chính xác kích nổ phụ thuộc trực tiếp vào độ chính xác đo $\Delta f$.

**Fire Control Radar:** Radar Doppler đo vận tốc mục tiêu di động (xe tăng, máy bay). Với $\lambda = 3$ cm (Ka-band) và mục tiêu tốc độ $v = 300$ m/s:
$$\Delta f = rac{2 	imes 300}{0.03} = 20 	ext{ kHz}$$

Doppler shift dễ đo bằng FFT. Độ phân giải vận tốc:
$$\delta v = rac{\lambda}{2T_{coherent}}$$

Với $T_{coherent} = 1$ s: $\delta v = 0.015$ m/s — đủ phân biệt xe tăng đứng yên và đang chạy chậm.

### 6. Ứng Dụng 3: Thiên Văn Học — Đo Tốc Độ Thiên Hà

**Hubble's Law** — nền tảng của vũ trụ học hiện đại — dựa trực tiếp vào Doppler shift:

Đo redshift $z$ của vạch phổ hydrogen ($\lambda_0 = 656.3$ nm) từ thiên hà xa:
$$z = rac{\lambda_{obs} - \lambda_0}{\lambda_0} = rac{\Delta\lambda}{\lambda_0}$$

Với $z \ll 1$ (thiên hà gần): $v_{recession} pprox cz$.

Với $z$ lớn (thiên hà xa, vũ trụ giãn nở): dùng công thức relativistic đầy đủ.

**Kết quả:** Thiên hà xa hơn thì redshift lớn hơn tuyến tính → vũ trụ đang giãn nở. Đây là bằng chứng quan sát đầu tiên cho Big Bang.

### Kết Luận

Từ công thức đơn giản $\omega_{obs} = \omega_1/(1-v/c)$ đến hệ quả tương đối tính đầy đủ, hiệu ứng Doppler thống nhất vật lý thiên văn vũ trụ học với kỹ thuật đo lường chính xác. Trong thiết kế hệ thống vũ khí và điều khiển micrometer, hiểu sâu Doppler shift — kể cả chiều dương âm, heterodyne detection, và nhiễu loạn linewidth laser — là không thể thiếu để thiết kế LDV, radar, và FOG chính xác.

---
*Exported from Feynman Bot*
