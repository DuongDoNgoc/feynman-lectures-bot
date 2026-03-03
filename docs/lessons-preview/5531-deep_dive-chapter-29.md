---
lesson_id: 5531
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:07.270165+00:00"
content_hash: 83cf5abd9791
chapter_number: 29
chapter_title: Chapter 29
section_number: 2
section_title: 29–1Electromagnetic waves
---
# ## Phân Tích Sâu: Toán Học của Trường Bức Xạ — Sóng, Snapshot và Giao Thoa

*Source: Chapter 29 - Chapter 29 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_29.html)*

## Phân Tích Sâu: Toán Học của Trường Bức Xạ — Sóng, Snapshot và Giao Thoa

### Xuất phát điểm: Công thức trường bức xạ

Ta bắt đầu từ công thức cơ bản cho trường điện của điện tích dao động biên độ nhỏ:

$$E(r, t) = \frac{-q \, a(t - r/c) \sin\theta}{4\pi\varepsilon_0 c^2 r}$$

Đây là biểu thức cho trường tại điểm quan sát cách điện tích khoảng $r$, theo góc $\theta$ so với trục dao động. Điểm quan trọng: $a(t - r/c)$ là gia tốc tại thời điểm *trễ* $t_{ret} = t - r/c$.

### Trường hợp đặc biệt: Dao động điều hòa $a(t) = a_0 \cos(\omega t)$

Khi điện tích dao động điều hòa với gia tốc:
$$a(t) = a_0 \cos(\omega t) = -\omega^2 x_0 \cos(\omega t)$$

(trong đó $x_0$ là biên độ dao động)

Thì trường bức xạ:
$$E(r, t) = \frac{q \omega^2 x_0 \sin\theta}{4\pi\varepsilon_0 c^2 r} \cos\left(\omega t - \frac{\omega r}{c}\right)$$

Hãy viết lại $k = \omega/c$ (số sóng) và $\lambda = 2\pi/k = 2\pi c/\omega$ (bước sóng):
$$E(r, t) = \frac{q \omega^2 x_0 \sin\theta}{4\pi\varepsilon_0 c^2 r} \cos(\omega t - kr)$$

Đây là sóng cầu phân cực: biên độ giảm theo $1/r$, pha thay đổi theo $kr$ (pha quét $2\pi$ mỗi bước sóng $\lambda$).

### Bức ảnh snapshot của trường

Sau đây ta phân tích dạng không gian. Giả sử $\theta = 90°$ (quan sát từ phương vuông góc với trục dao động — phương có bức xạ mạnh nhất).

Snapshot tại thời điểm $t = 0$:
$$E(r) = \frac{A}{r} \cos(kr) = \frac{A}{r} \cos\left(\frac{2\pi r}{\lambda}\right)$$

Bức ảnh này là một sóng dao động theo $r$, với biên độ tắt dần theo $1/r$. Các đỉnh sóng cách nhau đúng một bước sóng $\lambda$. Toàn bộ hình ảnh chạy ra ngoài với tốc độ $c$ — tức là sau thời gian $\Delta t$, bức ảnh dịch chuyển ra ngoài thêm $c \Delta t$.

### Vật lý của thời gian trễ: Khúc lịch sử bị đóng băng

Giả sử điện tích thực hiện N chu kỳ dao động rồi dừng lại. Snapshot không gian khi đó cho thấy N vùng sóng liên tiếp, mỗi vùng dài $\lambda$, tổng chiều dài $N\lambda$, đang lan ra ngoài. Trước và sau vùng sóng là trường Coulomb tĩnh của điện tích đứng yên.

Vùng sóng này chứa đựng toàn bộ năng lượng đã bức xạ. Nó chạy ra ngoài với tốc độ $c$, không bao giờ quay lại. Tổng năng lượng trong vùng sóng:
$$U_{rad} = P \cdot N T = \frac{q^2 a_0^2}{6\pi\varepsilon_0 c^3} \cdot N \cdot \frac{2\pi}{\omega}$$

trong đó $P$ là công suất bức xạ (công thức Larmor) và $T = 2\pi/\omega$ là chu kỳ.

### Giao thoa từ hai nguồn: Bài toán toán học chi tiết

Xét hai điện tích dao động tại hai vị trí cách nhau khoảng $d$, cùng biên độ, cùng tần số $\omega$, cùng pha (phase difference = 0). Ta muốn tìm trường tổng hợp tại một điểm $P$ ở xa (far field).

**Bước 1: Tính đường đi của từng sóng đến điểm P**

Gọi $\theta$ là góc giữa hướng đến điểm $P$ và trục nối hai nguồn. Khoảng cách từ nguồn 1 đến $P$ là $r_1$, từ nguồn 2 là $r_2$.

Ở far field ($r \gg d$): $r_1 \approx r - \frac{d}{2}\sin\theta$, $r_2 \approx r + \frac{d}{2}\sin\theta$

**Bước 2: Viết biểu thức trường từ mỗi nguồn**
$$E_1 \propto \frac{\cos(\omega t - kr_1)}{r_1} \approx \frac{\cos(\omega t - kr + \frac{kd}{2}\sin\theta)}{r}$$
$$E_2 \propto \frac{\cos(\omega t - kr_2)}{r_2} \approx \frac{\cos(\omega t - kr - \frac{kd}{2}\sin\theta)}{r}$$

**Bước 3: Tổng hợp (dùng công thức cosine)**
$$E_{total} = E_1 + E_2 \propto \frac{2\cos\left(\frac{kd\sin\theta}{2}\right) \cos(\omega t - kr)}{r}$$

Biên độ tổng hợp theo góc $\theta$:
$$A(\theta) \propto \cos\left(\frac{\pi d \sin\theta}{\lambda}\right)$$

**Bước 4: Phân tích interference pattern**

- Cực đại (constructive interference) khi $\frac{d \sin\theta}{\lambda} = 0, \pm 1, \pm 2, ...$
  Tức là $\sin\theta = n\lambda/d$ với $n = 0, \pm 1, \pm 2, ...$
- Cực tiểu (destructive interference) khi $\frac{d \sin\theta}{\lambda} = \pm 1/2, \pm 3/2, ...$
  Tức là $\sin\theta = (n+\frac{1}{2})\lambda/d$

Với $d = \lambda/2$: cực đại chính tại $\theta = 0$, cực tiểu tại $\sin\theta = \pm 1$ (tức $\theta = \pm 90°$).

### Ứng dụng kỹ thuật: Phased Array trong Radar Quân sự

Hệ thống radar AESA (Active Electronically Scanned Array) sử dụng hàng nghìn phần tử anten, mỗi phần tử có thể điều khiển pha độc lập. Giả sử ta có $N$ phần tử cách đều nhau $d$, phần tử thứ $n$ có pha $n\delta$ so với phần tử đầu.

Trường tổng hợp theo góc $\theta$:
$$E_{total}(\theta) \propto \sum_{n=0}^{N-1} e^{in(kd\sin\theta + \delta)}$$

Đây là chuỗi hình học, tổng là:
$$E_{total}(\theta) \propto \frac{\sin(N\psi/2)}{\sin(\psi/2)}$$

trong đó $\psi = kd\sin\theta + \delta$.

Cực đại tại $\psi = 0$, tức là $\sin\theta_0 = -\delta/(kd)$. Bằng cách điều chỉnh $\delta$ (độ lệch pha giữa các phần tử), ta quét chùm sóng đến góc $\theta_0$ bất kỳ mà không cần quay anten cơ học. Đây là ưu điểm quyết định của phased array: tốc độ quét điện tử nhanh hơn quét cơ học hàng nghìn lần.

### Beamwidth và độ phân giải góc

Độ rộng của main lobe (3dB beamwidth) xấp xỉ:
$$\Delta\theta \approx \frac{\lambda}{Nd} = \frac{\lambda}{L}$$

trong đó $L = Nd$ là tổng khẩu độ (aperture) của array. Radar tầm xa muốn phân giải góc tốt cần khẩu độ lớn $L$ hoặc bước sóng nhỏ $\lambda$. Đây là lý do radar thế hệ mới dùng tần số millimeter wave (bước sóng mm) để có resolution cao trong kích thước anten nhỏ.

### Tổng kết toán học

| Đại lượng | Công thức | Ý nghĩa vật lý |
|-----------|-----------|----------------|
| Trường đơn nguồn | $E \propto \frac{\sin\theta}{r}\cos(\omega t - kr)$ | Sóng cầu phân cực |
| Biên độ giao thoa 2 nguồn | $A \propto \cos(kd\sin\theta/2)$ | Interference pattern |
| Cực đại giao thoa | $d\sin\theta = n\lambda$ | Điều kiện constructive |
| Beamwidth N phần tử | $\Delta\theta \approx \lambda/L$ | Phân giải góc |
| Lái beam phased array | $\sin\theta_0 = -\delta/(kd)$ | Điều khiển pha số |

---
*Exported from Feynman Bot*
