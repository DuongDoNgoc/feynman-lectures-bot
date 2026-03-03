---
lesson_id: 5588
lesson_type: deep_dive
approval_status: pending
exported_at: "2026-03-03T15:33:08.687595+00:00"
content_hash: cb33bf7c42af
chapter_number: 34
chapter_title: Chapter 34
section_number: 10
section_title: 34–9The momentum of light
---
# ## Bài Giảng Chuyên Sâu: Áp Suất Bức Xạ — Từ Lorentz Đến Động Lượng Photon

*Source: Chapter 34 - Chapter 34 (Section 10) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_34.html)*

## Bài Giảng Chuyên Sâu: Áp Suất Bức Xạ — Từ Lorentz Đến Động Lượng Photon

### 1. Bối cảnh vật lý

Trong bức xạ điện từ, sóng ánh sáng mang cả trường điện $\mathbf{E}$ và trường từ $\mathbf{B}$ vuông góc nhau và vuông góc với phương truyền sóng. Thông thường ta chỉ quan tâm đến trường điện vì nó mạnh hơn về tác dụng đối với điện tích đứng yên. Nhưng khi điện tích bắt đầu chuyển động (do bị trường điện kích thích), trường từ bắt đầu có vai trò. Đây chính là nguồn gốc của áp suất bức xạ.

### 2. Cơ chế vật lý: Phân tích từng bước

**Bước 1: Trường điện kích thích điện tích**

Giả sử sóng ánh sáng truyền theo phương $z$, trường điện dao động theo phương $x$:
$$E_x = E_0 \cos(\omega t - kz)$$

Điện tích $q$ (khối lượng $m$) bị lực điện $F_x = qE_x$ kéo, dao động theo $x$:
$$\ddot{x} + \gamma\dot{x} + \omega_0^2 x = \frac{q}{m}E_0\cos(\omega t)$$

Nghiệm ở trạng thái ổn định:
$$x(t) = x_0\cos(\omega t + \phi), \quad v_x = \dot{x} = -\omega x_0 \sin(\omega t + \phi)$$

**Bước 2: Trường từ tác dụng lên điện tích đang chuyển động**

Trường từ của sóng nằm theo phương $y$: $B_y = E_x/c$ (từ phương trình Maxwell cho sóng phẳng).

Lực Lorentz theo phương $z$ (phương truyền sóng):
$$F_z = q v_x B_y = q v_x \frac{E_x}{c}$$

**Bước 3: Tính lực trung bình**

$$\langle F_z \rangle = \frac{q}{c}\langle v_x E_x \rangle$$

Nhưng $q\langle v_x E_x \rangle$ chính là công suất trung bình mà trường điện thực hiện lên điện tích (công suất hấp thụ $dW/dt$). Vì vậy:

$$\boxed{\langle F \rangle = \frac{1}{c}\frac{dW}{dt}}$$

Đây là kết quả then chốt: **lực bức xạ = công suất hấp thụ / c**. Lực này hoàn toàn độc lập với bản chất của hệ hấp thụ.

**Bước 4: Từ cổ điển đến lượng tử**

Năng lượng photon: $W = \hbar\omega$

Động lượng photon suy ra từ công thức trên:
$$p = \frac{W}{c} = \frac{\hbar\omega}{c} = \hbar k$$

Dạng vector 4 chiều (four-vector): $(W, \mathbf{p}) = \hbar(\omega, \mathbf{k})$, thống nhất năng lượng và động lượng trong hệ thức tương đối tính.

### 3. Hệ quả quan trọng

- **Gương phản xạ**: nếu ánh sáng phản chiếu hoàn toàn, động lượng đổi chiều $2p$, nên lực gấp đôi so với hấp thụ hoàn toàn:
$$F_{\text{phản xạ}} = \frac{2P}{c}$$

- **Phát xạ photon**: nguồn phát ánh sáng nhận lực giật lùi (recoil) với động lượng $p = \hbar k$ ngược chiều photon.

### 4. Ứng dụng kỹ thuật: Bù trừ áp suất bức xạ trong đo lường nm

**Bài toán thực tế:** Trong máy CMM (Coordinate Measuring Machine) sử dụng interferometer laser He-Ne ($\lambda = 632.8\,\text{nm}$, $P = 5\,\text{mW}$) với gương phản xạ $m = 50\,\text{g}$:

Lực bức xạ tác dụng lên gương phản xạ:
$$F = \frac{2P}{c} = \frac{2 \times 5 \times 10^{-3}}{3\times10^8} = 3.33\times10^{-11}\,\text{N} = 33.3\,\text{pN}$$

Gia tốc gây ra:
$$a = \frac{F}{m} = \frac{3.33\times10^{-11}}{0.05} = 6.67\times10^{-10}\,\text{m/s}^2$$

Sau $t = 1\,\text{s}$ đo lường:
$$\Delta x = \frac{1}{2}at^2 = 0.33\,\text{pm}$$

Sai số 0.33 pm này nhỏ hơn yêu cầu độ chính xác nm, nên bỏ qua được. Nhưng với laser công suất cao hơn ($P = 1\,\text{W}$), sai số sẽ là $\sim 66\,\text{pm}$, đủ để gây lỗi đo ở thang nm.

**Ứng dụng trong vũ khí định hướng năng lượng (DEW):** Laser công suất cao $P = 100\,\text{kW}$ chiếu lên bề mặt mục tiêu trong thời gian $t = 0.1\,\text{s}$:
- Năng lượng: $W = 10\,\text{kJ}$
- Động lượng chuyển giao (hấp thụ hoàn toàn): $p = W/c = 33.3\,\mu\text{N·s}$
- Đây là lực cơ học bổ sung ngoài hiệu ứng nhiệt, có thể gây biến dạng kết cấu mục tiêu.

### 5. Bài tập mẫu

**Đề bài:** Một cảm biến quang học dùng trong automation nhận chùm laser $P = 10\,\text{mW}$, hệ số phản xạ của bề mặt cảm biến $R = 0.8$. Tính lực bức xạ tác dụng lên cảm biến.

**Lời giải:**

Phần ánh sáng phản chiếu: $P_R = 0.8 \times 10\,\text{mW} = 8\,\text{mW}$, đóng góp lực $2P_R/c$.

Phần ánh sáng hấp thụ: $P_A = 0.2 \times 10\,\text{mW} = 2\,\text{mW}$, đóng góp lực $P_A/c$.

Tổng lực:
$$F = \frac{2P_R + P_A}{c} = \frac{2\times8\times10^{-3} + 2\times10^{-3}}{3\times10^8} = \frac{18\times10^{-3}}{3\times10^8} = 60\,\text{pN}$$

Lực 60 pN này cực nhỏ với cảm biến thông thường nhưng cần bù trừ trong MEMS sensor với khối lượng $\mu$g.

### 6. Kết nối với lý thuyết trường lượng tử

Áp suất bức xạ là biểu hiện cổ điển của việc photon mang động lượng. Trong QED (Quantum Electrodynamics), đây là hệ quả của hàm sóng photon có xung lượng $\hbar k$ xác định. Thực nghiệm đã xác nhận bằng "bẫy quang học" (optical tweezers) — một ứng dụng trực tiếp của áp suất bức xạ để kẹp và di chuyển các hạt sinh học ở thang nm với lực pN.

---
*Exported from Feynman Bot*
