---
lesson_id: 5534
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:07.336652+00:00"
content_hash: 417e0974be60
chapter_number: 29
chapter_title: Chapter 29
section_number: 5
section_title: 29–4Two dipole radiators
---
# ## Phân Tích Sâu: Toán Học Giao Thoa Hai Nguồn — Phasor, Vector Diagram và Array

*Source: Chapter 29 - Chapter 29 (Section 5) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_29.html)*

## Phân Tích Sâu: Toán Học Giao Thoa Hai Nguồn — Phasor, Vector Diagram và Array Factor

### Bài toán tổng quát

Xét hai nguồn bức xạ có biên độ $A_1$, $A_2$ và pha ban đầu $\phi_1$, $\phi_2$. Ta cần tìm trường tổng hợp tại một điểm $P$ xa, theo góc $\theta$ so với đường vuông góc với đường nối hai nguồn.

Mục tiêu: $R(t) = A_1\cos(\omega t + \phi_1) + A_2\cos(\omega t + \phi_2)$

Trong đó pha hiệu dụng tại $P$ đã bao gồm cả lệch pha do sai khác đường đi.

### Phương pháp 1: Giải tích lượng giác (trường hợp $A_1 = A_2 = A$)

Dùng công thức tổng cosine:
$$\cos A + \cos B = 2\cos\frac{A+B}{2}\cos\frac{A-B}{2}$$

Áp dụng:
$$R = A[\cos(\omega t + \phi_1) + \cos(\omega t + \phi_2)]$$
$$= 2A\cos\left(\frac{\phi_1 - \phi_2}{2}\right)\cos\left(\omega t + \frac{\phi_1 + \phi_2}{2}\right)$$

Kết quả: sóng dao động tần số $\omega$, biên độ $R_A = 2A\cos\left(\frac{\phi_1 - \phi_2}{2}\right)$, pha trung bình $\bar{\phi} = (\phi_1 + \phi_2)/2$.

**Quan sát quan trọng:** Biên độ kết quả phụ thuộc vào *hiệu pha* $\Delta\phi = \phi_1 - \phi_2$:
- $\Delta\phi = 0$: $R_A = 2A$ (constructive)
- $\Delta\phi = \pi$: $R_A = 0$ (destructive)
- $\Delta\phi = \pi/2$: $R_A = \sqrt{2}A$ (trung gian)

### Phương pháp 2: Phasor (Phương pháp số phức — Phương pháp ưu việt hơn)

Biểu diễn dao động dưới dạng phần thực của số phức:
$$A_1\cos(\omega t + \phi_1) = \text{Re}[A_1 e^{i(\omega t + \phi_1)}] = \text{Re}[\tilde{A}_1 e^{i\omega t}]$$

trong đó $\tilde{A}_1 = A_1 e^{i\phi_1}$ là **phasor** — vector phức đại diện cho biên độ và pha.

Tổng hai phasor:
$$\tilde{R} = \tilde{A}_1 + \tilde{A}_2 = A_1 e^{i\phi_1} + A_2 e^{i\phi_2}$$

Biên độ kết quả: $R_A = |\tilde{R}| = \sqrt{A_1^2 + A_2^2 + 2A_1 A_2 \cos(\phi_1 - \phi_2)}$

Pha kết quả: $\phi_R = \arg(\tilde{R}) = \arctan\left(\frac{A_1\sin\phi_1 + A_2\sin\phi_2}{A_1\cos\phi_1 + A_2\cos\phi_2}\right)$

**Lý do phasor ưu việt hơn:** Cho trường hợp $N$ nguồn bất kỳ, phasor đơn giản hóa bài toán thành cộng $N$ vector phức — không cần nhớ vô số công thức lượng giác.

### Phương pháp 3: Sơ đồ vector (Vector Diagram / Phasor Diagram)

Vẽ hai vector trong mặt phẳng phức:
- Vector $\tilde{A}_1$: độ dài $A_1$, góc $\phi_1$ so với trục thực
- Vector $\tilde{A}_2$: độ dài $A_2$, góc $\phi_2$ so với trục thực
- Hợp lực $\tilde{R}$: đường chéo của hình bình hành

Đây là công cụ hình học mạnh mẽ. Khi $\Delta\phi$ thay đổi từ 0 đến $2\pi$, đầu mút của vector $\tilde{R}$ vẽ một vòng tròn — điều này cho thấy biên độ kết quả dao động giữa $|A_1 - A_2|$ (minimum) và $A_1 + A_2$ (maximum).

### Bài toán thực tế: Hiệu pha tổng hợp cho hai nguồn

Giả sử hai nguồn có biên độ bằng nhau $A_1 = A_2 = A$, lệch pha intrinsic $\delta$ (do thiết kế anten), và sóng từ nguồn 2 đến điểm $P$ trễ hơn một đoạn $\Delta = kd\sin\theta$ (do sai khác đường đi hình học).

Pha hiệu dụng của nguồn 1: $\phi_1 = 0$
Pha hiệu dụng của nguồn 2 tại $P$: $\phi_2 = \delta + kd\sin\theta$

Tổng pha hiệu: $\Psi = \phi_2 - \phi_1 = \delta + kd\sin\theta$

Biên độ tổng: $R_A = 2A\cos(\Psi/2) = 2A\cos\left(\frac{\delta + kd\sin\theta}{2}\right)$

Cường độ: $I(\theta) \propto R_A^2 = 4A^2\cos^2\left(\frac{\delta + kd\sin\theta}{2}\right)$

**Đây là array factor (AF) cho hai phần tử** — hàm mô tả đặc trưng định hướng của mảng anten.

### Ví dụ số: Hai nguồn $d = \lambda/2$, cùng pha ($\delta = 0$)

$$I(\theta) \propto 4A^2\cos^2\left(\frac{\pi\sin\theta}{2}\right)$$

Tính tại các góc đặc biệt:
- $\theta = 0°$: $I = 4A^2\cos^2(0) = 4A^2$ ✓ (cực đại)
- $\theta = 30°$: $I = 4A^2\cos^2(\pi/4) = 4A^2 \times 0.5 = 2A^2$ (half-power)
- $\theta = 90°$: $I = 4A^2\cos^2(\pi/2) = 0$ ✓ (null)

3dB beamwidth: góc tại đó $I = 2A^2$, tức $\cos^2(\pi\sin\theta/2) = 0.5$, nghĩa là $\pi\sin\theta/2 = \pi/4$, nên $\sin\theta = 0.5$, $\theta = 30°$. Beamwidth (từ -30° đến +30°) = 60°.

### Ví dụ số: Hai nguồn $d = \lambda/2$, lệch pha $\delta = \pi/2$

$$I(\theta) \propto 4A^2\cos^2\left(\frac{\pi/2 + \pi\sin\theta}{2}\right) = 4A^2\cos^2\left(\frac{\pi(1 + 2\sin\theta)}{4}\right)$$

- $\theta = 0°$: $I = 4A^2\cos^2(\pi/4) = 2A^2$ (không còn là cực đại)
- $\theta = -30°$ ($\sin\theta = -0.5$): $I = 4A^2\cos^2(0) = 4A^2$ (cực đại mới!)

Chùm tia đã bị lái sang góc $-30°$ nhờ lệch pha $\delta = \pi/2$. Tổng quát: điều kiện cực đại khi $\Psi = 0$:
$$\delta + kd\sin\theta_0 = 0 \Rightarrow \sin\theta_0 = -\frac{\delta}{kd} = -\frac{\delta\lambda}{2\pi d}$$

### Mở rộng: N nguồn — Array Factor tổng quát

Cho $N$ nguồn cách đều $d$, mỗi nguồn lệch pha $\delta$ so với nguồn trước:
$$AF(\Psi) = \sum_{n=0}^{N-1} e^{in\Psi} = \frac{1 - e^{iN\Psi}}{1 - e^{i\Psi}} = e^{i(N-1)\Psi/2} \frac{\sin(N\Psi/2)}{\sin(\Psi/2)}$$

$$|AF(\Psi)|^2 = \frac{\sin^2(N\Psi/2)}{\sin^2(\Psi/2)}$$

Đây là **hàm Dirichlet** — tương tự hàm $\text{sinc}$ nhưng cho không gian tuần hoàn. Khi $N$ lớn, main lobe hẹp lại, side lobes xuất hiện ở vị trí $\Psi = 2m\pi/N$ với $m \neq 0, \pm N, \pm 2N,...$

### Ứng dụng: Thiết kế bộ lọc không gian

Phased array về bản chất là bộ lọc không gian (spatial filter): nó cho qua tín hiệu từ hướng $\theta_0$ và chặn các hướng khác. Tương tự như bộ lọc thông thấp trong miền thời gian lọc tần số, phased array lọc không gian. Đây là khái niệm quan trọng trong beamforming cho hệ thống lidar (light detection and ranging) dùng trong xe tự hành — N laser emitter/receiver phối hợp tạo ra "ống kính không gian" tập trung vào vùng quan tâm.

### Tóm tắt

- **Phasor method**: cộng vector phức — tổng quát và hiệu quả hơn trig
- **Array factor**: $|AF|^2 = \sin^2(N\Psi/2)/\sin^2(\Psi/2)$, với $\Psi = \delta + kd\sin\theta$
- **Beam steering**: $\sin\theta_0 = -\delta\lambda/(2\pi d)$
- **Beam narrowing**: beamwidth $\propto 1/N$ khi $N \to \infty$ với $d$ cố định
- **Ứng dụng**: phased array radar, lidar, sonar, sensor giao thoa — tất cả dùng cùng toán học

---
*Exported from Feynman Bot*
