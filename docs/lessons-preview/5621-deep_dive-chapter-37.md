---
lesson_id: 5621
lesson_type: deep_dive
approval_status: pending
exported_at: "2026-03-03T15:33:09.254082+00:00"
content_hash: b182a245bb1e
chapter_number: 37
chapter_title: Chapter 37
section_number: 7
section_title: 37–6Watching the electrons
---
# ## Phân Tích Toán Học: Mất Giao Thoa Khi Quan Sát và Nguyên Lý Bổ Sung

*Source: Chapter 37 - Chapter 37 (Section 7) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_37.html)*

## Phân Tích Toán Học: Mất Giao Thoa Khi Quan Sát và Nguyên Lý Bổ Sung

### 1. Mô hình toán học của "which-path" measurement

Xét thí nghiệm hai khe với nguồn sáng dùng để xác định electron đi qua khe nào. Trạng thái tổng cộng của hệ (electron + photon sau tán xạ) là:

$$|\Psiangle = rac{1}{\sqrt{2}}|\phi_1angle_e |1angle_\gamma + rac{1}{\sqrt{2}}|\phi_2angle_e |2angle_\gamma$$

trong đó $|jangle_\gamma$ là trạng thái photon cho biết electron qua khe $j$.

**Xác suất giao thoa:**

$$P_{12}(x) = \langle x|ho_e|xangle$$

với $ho_e = 	ext{Tr}_\gamma(|\Psiangle\langle\Psi|)$ là ma trận mật độ rút gọn của electron.

Tính trực tiếp:

$$ho_e = rac{1}{2}\left(|\phi_1angle\langle\phi_1| + |\phi_2angle\langle\phi_2| + \langle 2|1angle_\gamma |\phi_1angle\langle\phi_2| + \langle 1|2angle_\gamma |\phi_2angle\langle\phi_1|ight)$$

Số hạng giao thoa tỉ lệ với $\langle 2|1angle_\gamma$ — tích vô hướng giữa hai trạng thái photon.

- Nếu $|1angle_\gamma \perp |2angle_\gamma$ (phân biệt hoàn toàn): $\langle 2|1angle_\gamma = 0$ → **không có giao thoa**
- Nếu $|1angle_\gamma = |2angle_\gamma$ (không phân biệt được): $\langle 2|1angle_\gamma = 1$ → **giao thoa đầy đủ**

### 2. Phân tích độ tương phản (visibility) phụ thuộc bước sóng ánh sáng

Photon với bước sóng $\lambda_{	ext{light}}$ có hàm sóng dạng Gaussian với độ rộng không gian $\sigma \sim \lambda_{	ext{light}}$.

Khi electron tán xạ photon tại vị trí khe $j$, photon bị định xứ tại $y_j$ ($j = 1, 2$, cách nhau $d$). Tích chồng chập (overlap) giữa hai hàm sóng photon:

$$\langle 2|1angle_\gamma pprox \exp\!\left(-rac{d^2}{2\sigma^2}ight) pprox \exp\!\left(-rac{d^2}{2\lambda_{	ext{light}}^2}ight)$$

**Visibility của vân giao thoa:**

$$\mathcal{V} = |\langle 2|1angle_\gamma| pprox \exp\!\left(-rac{d^2}{2\lambda_{	ext{light}}^2}ight)$$

Phân tích:
- $\lambda_{	ext{light}} \gg d$: $\mathcal{V} pprox 1$ → giao thoa tốt, không phân biệt được khe
- $\lambda_{	ext{light}} \ll d$: $\mathcal{V} pprox 0$ → mất giao thoa, phân biệt được khe rõ ràng

### 3. Quan hệ định lượng: Which-path distinguishability

Khả năng phân biệt khe (distinguishability):

$$\mathcal{D} = \sqrt{1 - |\langle 2|1angle_\gamma|^2} = \sqrt{1 - \mathcal{V}^2}$$

Dẫn đến bất đẳng thức bổ sung tổng quát:

$$\mathcal{D}^2 + \mathcal{V}^2 = 1$$

(Đây là đẳng thức khi nguồn ánh sáng thuần nhất; trường hợp tổng quát hơn cho bất đẳng thức $\leq 1$.)

### 4. Phân tích xung động lượng do tán xạ photon

Khi electron tán xạ photon, xung động lượng truyền đến electron theo phương $x$ (phương song song màn) là:

$$\Delta p_x = \hbar q_x$$

trong đó $q_x$ là thành phần $x$ của vectơ sóng photon tán xạ. Do tán xạ xảy ra ở góc ngẫu nhiên, phân phối của $\Delta p_x$ là:

$$\langle (\Delta p_x)^2 angle \sim \left(rac{\hbar}{\lambda_{	ext{light}}}ight)^2$$

Bất định pha tương ứng tại màn dò:

$$\Deltaarphi \sim rac{d \cdot \Delta p_x}{\hbar} \sim rac{d}{\lambda_{	ext{light}}}$$

Khi $\Deltaarphi \gg 1$, các pha của $\phi_1$ và $\phi_2$ bị ngẫu nhiên hóa hoàn toàn — vân giao thoa biến mất.

**Điều này tương đương với nguyên lý bất định Heisenberg:** để phân giải không gian $\delta y \leq d$ (phân biệt khe), cần $\lambda_{	ext{light}} \leq d$, suy ra $\Delta p_x \geq h/d$, đủ để xóa vân giao thoa.

### 5. Thí nghiệm "quantum eraser" — khôi phục giao thoa

Đây là thí nghiệm quan trọng nhất minh họa vai trò của thông tin:

**Ý tưởng:** Sau khi photon đã tán xạ và mang thông tin which-path, nếu ta **xóa** thông tin đó (bằng cách không phân biệt hai trạng thái photon) → vân giao thoa **khôi phục**!

Thực hiện: Đặt phân cực tuyến tính $0°$ trước khe 1 và $90°$ trước khe 2. Photon tán xạ mang thông tin which-path (phân cực $0°$ hoặc $90°$). Vân giao thoa biến mất.

Bây giờ đặt thêm phân cực $45°$ trước detector → đây là "quantum eraser":
- Photon $45°$: cả phân cực $0°$ và $90°$ đều có xác suất $50\%$ đi qua → không phân biệt được khe
- Chọn lọc các sự kiện mà photon tán xạ cũng đi qua $45°$ → vân giao thoa xuất hiện trong **tập con** này!

Điều này chứng minh: giao thoa không phải do nhiễu loạn vật lý của electron, mà do **thông tin** lưu trong trạng thái lượng tử.

### 6. Standard Quantum Limit trong hệ điều khiển

Đối với kỹ sư cơ điện tử, khái niệm này có ứng dụng trực tiếp trong hệ servo chính xác cao:

**SQL cho phép đo vị trí liên tục:**

$$\Delta x_{	ext{SQL}} = \sqrt{rac{\hbar 	au}{m}}$$

trong đó $	au$ là thời gian đo, $m$ là khối lượng đối tượng.

Ví dụ: Gương laser interferometry, $m = 1$ g, $	au = 1$ ms:

$$\Delta x_{	ext{SQL}} = \sqrt{rac{1.055 	imes 10^{-34} 	imes 10^{-3}}{10^{-3}}} pprox 3.2 	imes 10^{-17} 	ext{ m}$$

Đây là giới hạn $\sim 30$ am (attometer) — vẫn còn xa hơn nhiều so với độ chính xác hiện tại của các hệ thống nano-positioning ($\sim$ pm). Nhưng với các hệ thống MEMS và quantum sensors, giới hạn này bắt đầu có ý nghĩa thực tiễn.

**Back-action evasion techniques:** Để vượt SQL, người ta dùng kỹ thuật "squeezed states" — nén bất định ở một chiều, mở rộng ở chiều kia (vẫn thỏa $\Delta x \cdot \Delta p \geq \hbar/2$).

### 7. Ứng dụng: Electron beam lithography và quantum effects

Trong hệ thống EBL (Electron Beam Lithography) cho sản xuất vi mạch:

- Electron $100$ keV: $\lambda pprox 3.7$ pm → độ phân giải lý thuyết $\sim$ pm
- Giới hạn thực tế: electron-electron repulsion, detector noise, mechanical vibration
- Ảnh hưởng lượng tử: forward scattering spread giới hạn resolution đến $\sim 10$ nm

**Tính toán:** Electron $100$ keV trong vật liệu PMMA (resist), tán xạ nhiều lần với góc trung bình $	heta_{	ext{rms}}$:

$$	heta_{	ext{rms}} pprox rac{13.6 	ext{ MeV}}{eta cp}\sqrt{rac{x}{X_0}}\left[1 + 0.038\lnrac{x}{X_0}ight]$$

với $X_0 pprox 40$ g/cm² là radiation length của PMMA, $x$ là chiều dày.

Cho $x = 100$ nm PMMA: $x/X_0 pprox 10^{-7}$ → $	heta_{	ext{rms}} pprox 0.003$ rad → spread $\delta y pprox 	heta \cdot x/2 pprox 0.15$ nm.

Hoàn toàn tính được và quan trọng trong thiết kế EBL process!

### Tổng kết

| Hiện tượng | Điều kiện | Kết quả |
|-----------|-----------|---------|
| Giao thoa đầy đủ | $\lambda_{	ext{light}} \gg d$, không biết which-path | $P_{12} = \|{\phi_1+\phi_2}\|^2$, $\mathcal{V}=1$ |
| Mất giao thoa hoàn toàn | $\lambda_{	ext{light}} \ll d$, biết which-path | $P_{12} = P_1 + P_2$, $\mathcal{V}=0$ |
| Giao thoa một phần | $\lambda_{	ext{light}} \sim d$ | $\mathcal{D}^2 + \mathcal{V}^2 = 1$ |
| Quantum eraser | Xóa thông tin which-path | Khôi phục giao thoa trong tập con |

---
*Exported from Feynman Bot*
