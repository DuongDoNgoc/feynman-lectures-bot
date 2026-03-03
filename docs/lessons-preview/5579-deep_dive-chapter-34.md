---
lesson_id: 5579
lesson_type: deep_dive
approval_status: pending
exported_at: "2026-03-03T15:33:08.424726+00:00"
content_hash: ca2c6743d2ec
chapter_number: 34
chapter_title: Chapter 34
section_number: 2
section_title: 34–1Moving sources
---
# ## Bức Xạ Từ Nguồn Chuyển Động: Phân Tích Toán Học Đầy Đủ

*Source: Chapter 34 - Chapter 34 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_34.html)*

## Bức Xạ Từ Nguồn Chuyển Động: Phân Tích Toán Học Đầy Đủ

### 1. Phương Trình Cơ Bản: Trường Bức Xạ của Điện Tích Chuyển Động

Xuất phát từ các phương trình Maxwell, có thể chứng minh rằng điện trường tại khoảng cách lớn từ một điện tích $q$ đang chuyển động được cho bởi:

$$\mathbf{E} = -rac{q}{4\piarepsilon_0 r'^2} rac{d^2\hat{e}_{R'}}{dt^2}$$

Trong đó:
- $r'$ = khoảng cách **biểu kiến** (retarded distance) — khoảng cách từ vị trí **trễ** của điện tích đến điểm quan sát
- $\hat{e}_{R'}$ = vector đơn vị theo hướng biểu kiến từ điện tích đến điểm quan sát
- $t$ là thời gian quan sát (không phải thời gian phát)

Từ trường luôn đi kèm và vuông góc:
$$\mathbf{B} = -\hat{e}_{R'} 	imes \mathbf{E}/c$$

**Tại sao lại là đạo hàm bậc hai của $\hat{e}_{R'}$?**

$\hat{e}_{R'}$ là vector đơn vị — độ lớn luôn bằng 1 — nên thay đổi của nó chỉ là thay đổi **hướng**. Đạo hàm bậc nhất $d\hat{e}_{R'}/dt$ là tốc độ quay của hướng nhìn. Đạo hàm bậc hai là **gia tốc góc** của hướng nhìn. Nếu điện tích chuyển động đều thẳng, hướng nhìn quay đều — không có gia tốc góc — không có bức xạ. Chỉ khi chuyển động có gia tốc mới có bức xạ.

### 2. Trường Hợp Điện Tích Dao Động Đơn Giản

Xét điện tích dao động: $x(t) = x_0 \sin(\omega t)$, người quan sát ở xa theo phương $z$.

Với khoảng cách lớn ($r \gg x_0$), hướng biểu kiến xấp xỉ:
$$\hat{e}_{R'} pprox \hat{z} + rac{x(t_{ret})}{r}\hat{x}$$

Đạo hàm bậc hai:
$$rac{d^2\hat{e}_{R'}}{dt^2} pprox rac{\ddot{x}(t_{ret})}{r}\hat{x} = rac{-\omega^2 x_0 \sin(\omega t_{ret})}{r}\hat{x}$$

Suy ra cường độ bức xạ:
$$\mathbf{E} = rac{q\omega^2 x_0}{4\piarepsilon_0 r c^2}\sin(\omega t_{ret})\hat{x}$$

Và công suất bức xạ trung bình (công thức Larmor):
$$P = rac{q^2 a^2}{6\piarepsilon_0 c^3}$$

với $a = \omega^2 x_0$ là gia tốc cực đại.

### 3. Hiệu Ứng Doppler: Suy Luận Từng Bước

**Thiết lập bài toán:** Nguồn sáng phát tần số $\omega_1$, đang chuyển động đến gần người quan sát với vận tốc $v$.

**Bước 1: Thời gian giữa các đỉnh sóng**

Tại thời điểm $t = 0$, nguồn phát đỉnh sóng đầu tiên. Tại thời điểm $t = T_1 = 2\pi/\omega_1$, nguồn phát đỉnh sóng thứ hai. Nhưng trong thời gian $T_1$ đó, nguồn đã tiến thêm một đoạn $v \cdot T_1$ đến gần người quan sát.

**Bước 2: Thời gian đến của hai đỉnh sóng**

Đỉnh 1 phải đi quãng đường $r_0$ với vận tốc $c$: đến lúc $t_{arr,1} = t_0 + r_0/c$.

Đỉnh 2 phát từ vị trí gần hơn $(r_0 - v T_1)$: đến lúc $t_{arr,2} = T_1 + (r_0 - v T_1)/c$.

**Bước 3: Chu kỳ quan sát được**

$$T_{obs} = t_{arr,2} - t_{arr,1} = T_1 - rac{v T_1}{c} = T_1\left(1 - rac{v}{c}ight)$$

**Bước 4: Tần số quan sát được**

$$\omega_{obs} = rac{2\pi}{T_{obs}} = rac{\omega_1}{1 - v/c}$$

Đây là **công thức Doppler cổ điển** cho nguồn tiến lại gần ($v > 0$ → $\omega_{obs} > \omega_1$: blueshifted).

Khi tính đến hiệu ứng tương đối tính (time dilation), công thức đầy đủ:

$$\omega_{obs} = \omega_1 \sqrt{rac{1 + v/c}{1 - v/c}}$$

### 4. Bức Xạ Synchrotron: Đặc Điểm Tập Trung Chùm Tia

Electron trong synchrotron chuyển động gần vận tốc ánh sáng ($v pprox c$, $\gamma = 1/\sqrt{1-v^2/c^2} \gg 1$). Bức xạ phát ra tập trung trong một góc khối rất hẹp:

$$\Delta	heta pprox rac{1}{\gamma} = rac{m_e c^2}{E_{electron}}$$

Với electron năng lượng $E = 1$ GeV, $\gamma pprox 1957$, góc mở $\Delta	heta pprox 0.03°$ — cực kỳ hẹp.

**Phổ bức xạ synchrotron** trải từ hồng ngoại đến tia X, với tần số tới hạn:

$$\omega_c = rac{3}{2}\gamma^3 rac{v}{R}$$

trong đó $R$ là bán kính quỹ đạo tròn.

### 5. Ứng Dụng Thực Tế: LDV trong Hệ Thống Đo Lường Chính Xác

**Laser Doppler Velocimetry (LDV)** — phương pháp đo tốc độ rung động bề mặt hoặc tốc độ dòng chảy mà không cần tiếp xúc — hoạt động trực tiếp trên hiệu ứng Doppler:

Một chùm laser tần số $f_0$ chiếu vào bề mặt đang rung động với vận tốc $v(t)$. Ánh sáng phản xạ bị dịch tần số:

$$\Delta f = rac{2 v(t)}{λ}$$

với $\lambda$ là bước sóng laser. Với laser He-Ne ($\lambda = 632.8$ nm) và bề mặt rung tốc độ $v = 1$ mm/s:

$$\Delta f = rac{2 	imes 10^{-3}}{632.8 	imes 10^{-9}} pprox 3160 	ext{ Hz}$$

Trong thiết kế vũ khí và hệ thống điều khiển chính xác cấp micrometer, LDV được dùng để:
- Đo rung động cơ cấu chấp hành piezo (PZT) mà không làm thay đổi đặc tính cơ học
- Kiểm định hành trình actuator với độ phân giải nanometer
- Đo vận tốc đầu đạn không tiếp xúc trong thử nghiệm đạn đạo học

**Nguyên lý hoạt động của giao thoa kế Mach-Zehnder trong LDV:**

Chùm laser chia làm hai: một chùm chiếu thẳng (reference), một chùm chiếu vào mục tiêu. Khi tín hiệu phản xạ Doppler-shifted ($f_0 + \Delta f$) giao thoa với reference ($f_0$), tín hiệu beat tần số $\Delta f$ xuất hiện tại photodetector. Giải điều chế tín hiệu này cho ra vận tốc tức thời $v(t)$. Tích phân cho ra dịch chuyển $x(t)$ với độ chính xác nanometer.

### 6. Phổ Bức Xạ và Độ Rộng Vạch Phổ

Một nguồn phát không phải sóng sine hoàn hảo mãi mãi — nó bắt đầu và kết thúc, hoặc bị nhiễu loạn. Xét nguồn phát xung ngắn thời gian $	au$: phổ tần số có độ rộng $\Delta\omega pprox 1/	au$ (theo nguyên lý bất định thời gian-tần số).

Trong thực tế, vạch phổ laser có độ rộng hữu hạn (linewidth) do:
- Thăng giáng nhiệt (thermal noise)
- Va chạm nguyên tử (pressure broadening)
- Hiệu ứng Doppler nhiệt (Doppler broadening) từ chuyển động nhiệt ngẫu nhiên của nguyên tử phát sáng

Với laser bán dẫn thông dụng, linewidth ~MHz; laser ổn định cộng hưởng ngoài (external cavity laser) có thể đạt < 1 kHz — quan trọng cho LDV chính xác cao.

### Kết Luận

Từ một công thức duy nhất $\mathbf{E} \propto d^2\hat{e}_{R'}/dt^2$, chúng ta đã suy ra được Doppler shift, bức xạ synchrotron tập trung chùm hẹp, và nguyên lý hoạt động của LDV. Đây là sức mạnh của lý thuyết điện động lực học cổ điển: một nguyên lý thống nhất, vô số ứng dụng.

---
*Exported from Feynman Bot*
