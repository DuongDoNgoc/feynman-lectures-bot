---
lesson_id: 5333
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-02T15:10:26.890775+00:00"
content_hash: 3db740130a99
chapter_number: 4
chapter_title: Chapter 4
section_number: 4
section_title: 4–3Kinetic energy
---
# ## Động Năng và Bảo Toàn Năng Lượng — Phân tích Chuyên sâu

*Source: Chapter 4 - Chapter 4 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_04.html)*

## Động Năng và Bảo Toàn Năng Lượng — Phân tích Chuyên sâu

### 1. Dẫn Xuất Công Thức Động Năng Từ Nguyên Lý Máy Thuận Nghịch

Feynman dẫn xuất $KE = \frac{1}{2}mv^2$ không phải qua tích phân thông thường mà qua lập luận về **máy thuận nghịch** (reversible machines) — một cách tiếp cận vật lý thuần túy.

**Bước 1**: Xét một vật khối lượng $m$ được nâng lên độ cao $h$, rồi rơi xuống. Công cần thiết để nâng lên là $W = mgh$.

**Bước 2**: Khi vật rơi tự do từ $h$ xuống 0 (bỏ qua ma sát), mọi thế năng chuyển thành động năng:
$$mgh = KE$$

**Bước 3**: Từ cơ học kinh điển, vật rơi tự do với gia tốc $g$ từ đứng yên sẽ đạt vận tốc $v$ sau khoảng cách $h$:
$$v^2 = 2gh \implies h = \frac{v^2}{2g}$$

**Bước 4**: Thay vào:
$$KE = mgh = mg \cdot \frac{v^2}{2g} = \frac{1}{2}mv^2 \quad \checkmark$$

Đây là cách Feynman ưa thích: dùng những gì đã biết (thế năng hấp dẫn, động học) để **suy ra** những gì chưa biết (công thức động năng), thay vì chỉ định nghĩa nó.

### 2. Định Lý Công — Động Năng (Work-Energy Theorem)

Cách tiếp cận tổng quát hơn: khi lực $F$ tác dụng lên vật trong khoảng cách $s$, công thực hiện là:
$$W = \int_0^s F \, ds = \int_0^s ma \, ds$$

Sử dụng $a = \frac{dv}{dt}$ và $ds = v \, dt$:
$$W = \int m\frac{dv}{dt} \cdot v \, dt = m\int v \, dv = \frac{1}{2}mv^2 - \frac{1}{2}mv_0^2$$

**Định lý công — động năng**: Công thực hiện bởi hợp lực bằng độ biến thiên động năng:
$$W_{net} = \Delta KE = \frac{1}{2}mv_f^2 - \frac{1}{2}mv_i^2$$

### 3. Phân Tích Năng Lượng Con Lắc Theo Vị Trí

Xét con lắc dài $L$, khối lượng $m$, góc lệch tối đa $\theta_0$.

- **Độ cao cực đại**: $h_{max} = L(1 - \cos\theta_0)$
- **Thế năng cực đại**: $PE_{max} = mgh_{max} = mgL(1-\cos\theta_0)$
- **Tại vị trí góc $\theta$**: $PE(\theta) = mgL(1-\cos\theta)$
- **Động năng tại $\theta$**: $KE(\theta) = PE_{max} - PE(\theta) = mgL(\cos\theta - \cos\theta_0)$
- **Vận tốc tại $\theta$**: $v(\theta) = \sqrt{2gL(\cos\theta - \cos\theta_0)}$
- **Vận tốc cực đại tại đáy** ($\theta=0$): $v_{max} = \sqrt{2gL(1-\cos\theta_0)}$

### 4. Ví Dụ Thực Tế: Tính Động Năng Rotor Servo Motor

**Bài toán**: Một servo motor dùng trong hệ thống vũ khí tự động có rotor với mô men quán tính $I = 0.002 \, \text{kg}\cdot\text{m}^2$, quay ở $\omega = 3000 \, \text{rpm}$. Tính:

a) Động năng của rotor
b) Lực phanh cần thiết để dừng trong $0.5$ giây
c) Công suất tản nhiệt nếu dùng resistor xả

**Giải:**

a) Đổi đơn vị: $\omega = 3000 \times \frac{2\pi}{60} = 314.16 \, \text{rad/s}$

$$KE_{rotor} = \frac{1}{2}I\omega^2 = \frac{1}{2}(0.002)(314.16)^2 = 98.7 \, \text{J}$$

b) Mô men phanh cần thiết:
$$\tau = I\frac{\Delta\omega}{\Delta t} = 0.002 \times \frac{314.16}{0.5} = 1.26 \, \text{N}\cdot\text{m}$$

c) Công suất tản nhiệt trung bình:
$$P_{avg} = \frac{KE}{\Delta t} = \frac{98.7}{0.5} = 197 \, \text{W}$$

→ Resistor xả phải chịu được ít nhất 200W trong 0.5 giây — đây là thông số kỹ thuật quan trọng khi chọn linh kiện.

### 5. Bài Tập Mẫu: Con Lắc Với Cảm Biến MEMS

**Bài toán**: Cảm biến gia tốc MEMS dạng con lắc có khối lượng chứng $m = 0.5 \, \mu\text{g}$, dài $L = 200 \, \mu\text{m}$. Khi bị kích thích góc $\theta_0 = 5°$, tính vận tốc cực đại của khối lượng chứng.

**Giải từng bước:**

1. $\cos\theta_0 = \cos(5°) = 0.9962$
2. $1 - \cos\theta_0 = 0.0038$
3. $v_{max} = \sqrt{2gL(1-\cos\theta_0)}$
4. $= \sqrt{2 \times 9.81 \times 200\times10^{-6} \times 0.0038}$
5. $= \sqrt{1.49 \times 10^{-5}} = 3.86 \times 10^{-3} \, \text{m/s} = 3.86 \, \text{mm/s}$

**Ý nghĩa vật lý**: Tốc độ chỉ 3.86 mm/s ở micro-scale nhưng MEMS phải đo được độ dịch chuyển nanometer tương ứng — đây là thách thức kỹ thuật của cảm biến độ nhạy cao.

### 6. Năng Lượng Trong Hệ Thống Đo Lường Độ Chính Xác Cao

Trong đo lường ở cấp độ micrometer, ngay cả dao động nhiệt (thermal vibration) cũng ảnh hưởng:
- Năng lượng nhiệt của phần tử cơ học: $KE_{thermal} \approx \frac{1}{2}k_BT$ (định lý phân bố đều)
- Ở $T = 300K$: $KE_{thermal} \approx 2 \times 10^{-21} \, \text{J}$
- Vận tốc nhiệt của phần tử $m = 1 \, \mu\text{g}$: $v_{thermal} = \sqrt{\frac{k_BT}{m}} \approx 2 \, \text{mm/s}$

Đây là lý do tại sao các thiết bị đo lường cực kỳ chính xác phải hoạt động ở nhiệt độ thấp hoặc có cơ chế khử dao động nhiệt.

---

**Điểm mấu chốt:**
- Công thức $KE = \frac{1}{2}mv^2$ được suy ra từ nguyên lý bảo toàn năng lượng và động học cơ bản
- Định lý công-động năng: $W_{net} = \Delta KE$ — công thức tính toán thực tế trong kỹ thuật
- Trong servo và hệ tự động hóa: tính đúng KE của rotor giúp thiết kế hệ phanh an toàn
- Ở micro/nano scale: dao động nhiệt trở thành yếu tố không thể bỏ qua trong thiết kế cảm biến

---
*Exported from Feynman Bot*
