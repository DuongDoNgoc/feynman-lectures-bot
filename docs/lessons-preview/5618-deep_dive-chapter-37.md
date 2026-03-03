---
lesson_id: 5618
lesson_type: deep_dive
approval_status: pending
exported_at: "2026-03-03T15:33:09.191427+00:00"
content_hash: ea3cb770ea03
chapter_number: 37
chapter_title: Chapter 37
section_number: 5
section_title: 37–4An experiment with electrons
---
# ## Phân Tích Toán Học: Thí Nghiệm Giao Thoa Hai Khe Với Electron

*Source: Chapter 37 - Chapter 37 (Section 5) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_37.html)*

## Phân Tích Toán Học: Thí Nghiệm Giao Thoa Hai Khe Với Electron

### 1. Thiết lập thí nghiệm và ký hiệu

Xét một súng electron bắn các electron có động năng $E_k$ xác định về phía tấm chắn có hai khe hở 1 và 2. Gọi:
- $d$ = khoảng cách giữa hai khe
- $L$ = khoảng cách từ tấm chắn đến màn dò
- $x$ = tọa độ trên màn dò (đo từ tâm)
- $P_1(x)$ = xác suất phát hiện electron tại $x$ khi chỉ mở khe 1
- $P_2(x)$ = xác suất phát hiện electron tại $x$ khi chỉ mở khe 2
- $P_{12}(x)$ = xác suất phát hiện electron tại $x$ khi cả hai khe mở

**Quan sát thực nghiệm căn bản:** $P_{12}(x) 
eq P_1(x) + P_2(x)$

### 2. Phân bố từng khe riêng lẻ

Khi chỉ mở khe 1, phân bố electron trải rộng do nhiễu xạ (diffraction). Đây là hành vi đặc trưng của sóng đi qua khe đơn. Nếu đường kính khe là $a$ và bước sóng de Broglie là $\lambda$, góc nhiễu xạ thỏa:

$$\sin	heta_{	ext{min}} = rac{\lambda}{a}$$

Bước sóng de Broglie của electron có động lượng $p$:

$$\lambda = rac{h}{p} = rac{h}{\sqrt{2m_e E_k}}$$

với $h = 6.626 	imes 10^{-34}$ J·s là hằng số Planck, $m_e = 9.109 	imes 10^{-31}$ kg là khối lượng electron.

**Ví dụ số:** Electron được tăng tốc qua điện thế $V = 100$ V:
$$E_k = eV = 1.6 	imes 10^{-17} 	ext{ J}$$
$$p = \sqrt{2m_e E_k} = \sqrt{2 	imes 9.109 	imes 10^{-31} 	imes 1.6 	imes 10^{-17}} pprox 5.4 	imes 10^{-24} 	ext{ kg·m/s}$$
$$\lambda = rac{6.626 	imes 10^{-34}}{5.4 	imes 10^{-24}} pprox 0.123 	ext{ nm} = 1.23 	ext{ Å}$$

Đây là cỡ khoảng cách nguyên tử — giải thích tại sao chúng ta quan sát nhiễu xạ electron trong tinh thể.

### 3. Biên độ xác suất phức (Complex Probability Amplitude)

Mấu chốt của cơ học lượng tử là mỗi electron được mô tả bởi một hàm sóng phức $\psi(x,t)$. Biên độ xác suất đến vị trí $x$ qua khe $j$ là số phức $\phi_j(x)$.

Khi hai khe đều mở, nguyên lý superposition lượng tử cho:

$$\phi_{12}(x) = \phi_1(x) + \phi_2(x)$$

Xác suất (có thể đo được) là:

$$P_{12}(x) = |\phi_{12}(x)|^2 = |\phi_1(x) + \phi_2(x)|^2$$

Khai triển:

$$P_{12}(x) = |\phi_1|^2 + |\phi_2|^2 + 2	ext{Re}(\phi_1^* \phi_2)$$

$$= P_1(x) + P_2(x) + 2	ext{Re}(\phi_1^* \phi_2)$$

Số hạng $2	ext{Re}(\phi_1^* \phi_2)$ chính là **số hạng giao thoa (interference term)** — nó có thể dương (tăng cường) hoặc âm (triệt tiêu), và đây là nguồn gốc của vân giao thoa.

### 4. Tính toán vân giao thoa

Viết các biên độ ở dạng cực: $\phi_j(x) = |\phi_j(x)| e^{iarphi_j(x)}$

Hiệu pha giữa hai đường đi (từ khe 1 và khe 2 đến điểm $x$):

$$\delta(x) = arphi_1(x) - arphi_2(x) = rac{2\pi}{\lambda} \cdot \Delta r(x)$$

Hiệu đường đi (path difference) cho trường hợp $L \gg d$:

$$\Delta r(x) pprox rac{d \cdot x}{L}$$

Khi hai biên độ có cùng độ lớn $|\phi_1| = |\phi_2| = A$:

$$P_{12}(x) = 2A^2[1 + \cos\delta(x)] = 4A^2\cos^2\!\left(rac{\delta(x)}{2}ight)$$

$$= 4A^2\cos^2\!\left(rac{\pi d x}{\lambda L}ight)$$

**Điều kiện vân sáng (cực đại):** $\Delta r = n\lambda$, tức là:

$$x_n = rac{n\lambda L}{d}, \quad n = 0, \pm1, \pm2, \ldots$$

**Điều kiện vân tối (cực tiểu):** $\Delta r = (n + rac{1}{2})\lambda$, tức là:

$$x_n = rac{(n+rac{1}{2})\lambda L}{d}$$

### 5. Khoảng vân (fringe spacing)

Khoảng cách giữa hai vân sáng liên tiếp:

$$\Delta x = rac{\lambda L}{d}$$

**Ví dụ kỹ thuật:** Trong kính hiển vi điện tử truyền qua (TEM), electron 100 keV có $\lambda pprox 3.7$ pm. Nếu hai lỗ cách nhau $d = 1$ μm và $L = 10$ cm:

$$\Delta x = rac{3.7 	imes 10^{-12} 	imes 0.1}{10^{-6}} = 0.37 	ext{ mm}$$

Hoàn toàn có thể đo được bằng sensor CCD!

### 6. Mất giao thoa khi quan sát (which-path information)

Đây là điểm then chốt nhất. Khi ta thêm nguồn sáng để xác định electron qua khe nào, photon tán xạ truyền thông tin "electron ở đây" — nhưng quá trình tán xạ này làm rối loạn động lượng của electron một lượng:

$$\Delta p_x \sim rac{h}{\lambda_{	ext{light}}}$$

Để phân biệt được khe 1 và khe 2, cần độ phân giải không gian $\leq d$, nghĩa là:

$$\lambda_{	ext{light}} \leq d$$

Điều này dẫn đến nhiễu loạn pha ngẫu nhiên của electron, xóa bỏ sự tương quan pha giữa $\phi_1$ và $\phi_2$. Trung bình theo các nhiễu loạn ngẫu nhiên:

$$\langle 	ext{Re}(\phi_1^* \phi_2) angle_{	ext{random}} = 0$$

Vân giao thoa biến mất! Và khi đó:

$$P_{12}(x) = P_1(x) + P_2(x)$$

Cổ điển hóa hoàn toàn — electron "hành xử như hạt" khi bị quan sát.

### 7. Nguyên lý bất định Heisenberg — căn bản của hiện tượng này

Lý do sâu xa là nguyên lý bất định:

$$\Delta x \cdot \Delta p_x \geq rac{\hbar}{2}$$

Khi ta đo vị trí electron (qua khe nào) với độ chính xác $\Delta x pprox d$, ta tạo ra bất định động lượng:

$$\Delta p_x \geq rac{\hbar}{2d}$$

Bất định này đủ lớn để "xóa" thông tin pha — vân giao thoa biến mất.

### 8. Ứng dụng trong kỹ thuật chính xác cao

**Giao thoa kế electron (Electron interferometry):** Tương tự giao thoa kế laser Michelson nhưng dùng sóng de Broglie của electron. Dùng trong đo trường điện từ, phân tích cấu trúc tinh thể, và nghiên cứu vật liệu nano.

**Nhiễu xạ electron năng lượng thấp (LEED):** Electron $10$–$500$ eV ($\lambda pprox 0.05$–$0.4$ nm) tán xạ từ bề mặt tinh thể tạo ra mẫu nhiễu xạ cho phép xác định cấu trúc nguyên tử bề mặt với độ chính xác picometer.

**Kính hiển vi điện tử (TEM/SEM):** Dùng bước sóng de Broglie ngắn của electron để đạt độ phân giải dưới nanometer — vượt xa giới hạn nhiễu xạ của kính hiển vi quang học.

**Sensor SQUID:** Giao thoa lượng tử của cặp Cooper (superconductive pair) tạo ra sensor từ trường nhạy nhất thế giới ($\sim 10^{-15}$ T), ứng dụng trong chẩn đoán y tế và hoa tiêu quán tính.

### Tổng kết toán học

| Đại lượng | Công thức | Ý nghĩa |
|-----------|-----------|---------|
| $\lambda_{dB}$ | $h/p$ | Bước sóng de Broglie |
| $P_{12}$ | $\|\phi_1+\phi_2\|^2$ | Xác suất khi 2 khe mở |
| Vân sáng | $x_n = n\lambda L/d$ | Cực đại giao thoa |
| Khoảng vân | $\Delta x = \lambda L/d$ | Chu kỳ vân |
| Mất giao thoa | $\Delta p \sim h/\lambda_{	ext{light}}$ | Khi quan sát which-path |

---
*Exported from Feynman Bot*
