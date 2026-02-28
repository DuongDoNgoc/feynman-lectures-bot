---
lesson_id: 5
lesson_type: deep_dive
approval_status: pending
exported_at: "2026-02-28T02:21:44.319270+00:00"
content_hash: 1e8fc146d83f
chapter_number: 2
chapter_title: Chapter 2
section_number: 1
section_title: Introduction
---
# ## Vật lý Cơ bản — Phân tích Chuyên sâu

*Source: Chapter 2 - Chapter 2 (Section 1)*

## Vật lý Cơ bản — Phân tích Chuyên sâu

### 1. Sự thống nhất của Vật lý Cổ điển

Trước năm 1900, ba lĩnh vực lớn của vật lý cổ điển đã được xây dựng hoàn chỉnh:

**1.1 Cơ học Newton và Lagrangian**

Từ $\vec{F} = m\vec{a}$, Lagrange và Hamilton xây dựng cách tiếp cận tổng quát hơn. Nguyên lý Hamilton (nguyên lý tác dụng cực tiểu):

$$\delta S = \delta \int_{t_1}^{t_2} L(q, \dot{q}, t) \, dt = 0$$

trong đó $L = T - V$ là Lagrangian (động năng trừ thế năng). Từ đây suy ra phương trình Euler-Lagrange:

$$\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{q}_i}\right) - \frac{\partial L}{\partial q_i} = 0$$

Đây là nền tảng của robotics hiện đại: mô phỏng động lực học robot nhiều khớp dùng chính formulation này. Thay vì viết $F = ma$ cho từng lực, ta viết $L$ một lần và suy ra toàn bộ phương trình chuyển động.

**Ví dụ mechatronics:** Một robot 6-DOF có 6 biến khớp $q_1, ..., q_6$. Lagrangian $L(q, \dot{q}) = T(q, \dot{q}) - V(q)$ cho phép suy ra moment cần thiết tại mỗi khớp:

$$\tau_i = \frac{d}{dt}\frac{\partial T}{\partial \dot{q}_i} - \frac{\partial T}{\partial q_i} + \frac{\partial V}{\partial q_i}$$

**1.2 Điện từ học Maxwell**

Bốn phương trình Maxwell thống nhất điện, từ và ánh sáng:

$$\nabla \cdot \vec{E} = \frac{\rho}{\varepsilon_0} \qquad (\text{Gauss điện})$$
$$\nabla \cdot \vec{B} = 0 \qquad (\text{Gauss từ})$$
$$\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t} \qquad (\text{Faraday})$$
$$\nabla \times \vec{B} = \mu_0 \vec{J} + \mu_0\varepsilon_0 \frac{\partial \vec{E}}{\partial t} \qquad (\text{Ampere-Maxwell})$$

Từ các phương trình này suy ra phương trình sóng:
$$\nabla^2 \vec{E} = \mu_0\varepsilon_0 \frac{\partial^2 \vec{E}}{\partial t^2}$$

Vận tốc sóng: $c = 1/\sqrt{\mu_0\varepsilon_0} = 3 \times 10^8$ m/s — đúng bằng vận tốc ánh sáng. Đây là một trong những khám phá vĩ đại nhất của vật lý.

**Ứng dụng mechatronics:** Cảm biến từ (Hall sensor, encoder từ) hoạt động dựa trên định luật Faraday. EMC (Electromagnetic Compatibility) của board điều khiển liên quan trực tiếp đến Maxwell.

**1.3 Thuyết Tương đối Hẹp**

Einstein nhận ra mâu thuẫn: vận tốc ánh sáng phải bất biến, nhưng điều đó mâu thuẫn với phép biến đổi Galileo. Giải pháp: không gian và thời gian biến đổi cùng nhau theo phép biến đổi Lorentz:

$$t' = \gamma\left(t - \frac{vx}{c^2}\right), \quad x' = \gamma(x - vt)$$

trong đó $\gamma = 1/\sqrt{1-v^2/c^2}$ là hệ số Lorentz.

Hệ quả: đồng hồ chuyển động chạy chậm hơn (giãn thời gian), vật chuyển động co lại theo chiều chuyển động (co chiều dài). Với GPS, hiệu ứng tương đối tính (đồng hồ trên vệ tinh chạy nhanh hơn 38 μs/ngày do kết hợp special và general relativity) phải được hiệu chỉnh — nếu không GPS sẽ sai lệch ~10 km/ngày.

### 2. Bức tranh Lượng tử và QED

**2.1 Hàm sóng và nguyên lý bất định**

Cơ học lượng tử thay thế quỹ đạo xác định bằng hàm sóng $\Psi(x,t)$. Xác suất tìm thấy hạt tại $x$: $P(x) = |\Psi(x,t)|^2$.

Nguyên lý bất định Heisenberg:
$$\Delta x \cdot \Delta p \geq \frac{\hbar}{2}$$

Ý nghĩa công nghệ: transistor MOSFET hiện đại có kênh dài ~3-5 nm. Ở kích thước đó, electron "xuyên hầm" qua cổng transistor kể cả khi không đủ năng lượng cổ điển — gây ra dòng rò tăng mạnh. Đây là giới hạn vật lý cơ bản của miniaturization.

**2.2 Quantum Electrodynamics (QED)**

QED mô tả tương tác giữa electron và photon với độ chính xác chưa từng có. Moment từ bất thường của electron được tính:

$$a_e = \frac{g-2}{2} = \frac{\alpha}{2\pi} - 0.328\frac{\alpha^2}{\pi^2} + ... = 0.001159652...$$

Thực nghiệm đo: $0.001159652181...$ — khớp đến 12 chữ số có nghĩa.

### 3. Vật lý Hạt nhân và Hạt cơ bản

Khi bắn các hạt tăng tốc vào nhau với năng lượng ngày càng cao, các hạt mới xuất hiện liên tục. Meson, baryon, lepton... hàng trăm "hạt cơ bản". Mô hình chuẩn (Standard Model) tổ chức chúng thành quarks và leptons, kết hợp bằng 3 lực cơ bản (điện từ, yếu, mạnh).

Nhưng hấp dẫn vẫn chưa được lượng tử hóa thành công — đây là bài toán mở lớn nhất của vật lý lý thuyết.

### 4. Bài tập mẫu: GPS và Thuyết tương đối

**Bài toán:** Vệ tinh GPS bay ở độ cao 20,200 km với vận tốc $v = 3.87$ km/s. Tính hiệu ứng giãn thời gian special relativity (đồng hồ vệ tinh chạy chậm hơn bao nhiêu so với mặt đất mỗi ngày)?

**Lời giải:**

Hệ số Lorentz:
$$\gamma = \frac{1}{\sqrt{1 - v^2/c^2}} = \frac{1}{\sqrt{1 - (3870)^2/(3 \times 10^8)^2}}$$

$$\gamma \approx 1 + \frac{v^2}{2c^2} = 1 + \frac{(3.87 \times 10^3)^2}{2 \times (3 \times 10^8)^2} = 1 + 8.35 \times 10^{-11}$$

Thời gian mất đi do giãn thời gian special relativity trong 1 ngày:
$$\Delta t_{SR} = (\gamma - 1) \times 86400 \text{ s} = 8.35 \times 10^{-11} \times 86400 \approx 7.2 \text{ μs/ngày}$$

*Đồng hồ vệ tinh chạy chậm hơn 7.2 μs/ngày do special relativity.*

*(Thực tế cần cộng thêm hiệu chỉnh general relativity +45.9 μs/ngày, net effect là +38.7 μs/ngày — đồng hồ vệ tinh chạy nhanh hơn và phải được điều chỉnh.)*

### Điểm Mấu Chốt

- Vật lý cổ điển gồm 3 trụ cột: Newton (cơ học), Maxwell (điện từ), Einstein (tương đối)
- Lagrangian mechanics là ngôn ngữ của robotics và điều khiển hiện đại
- Maxwell tổng hợp điện và từ: $c = 1/\sqrt{\mu_0\varepsilon_0}$
- GPS đòi hỏi hiệu chỉnh cả special lẫn general relativity — công nghệ hiện đại phụ thuộc vào vật lý hiện đại
- QED là lý thuyết chính xác nhất trong lịch sử khoa học
- Giới hạn lượng tử đặt ra rào cản vật lý cho thu nhỏ bán dẫn — thách thức kỹ thuật quan trọng nhất hiện nay


---
*Exported from Feynman Bot*
