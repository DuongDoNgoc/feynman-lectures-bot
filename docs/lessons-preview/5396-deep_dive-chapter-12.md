---
lesson_id: 5396
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:04.018681+00:00"
content_hash: 798c539516eb
chapter_number: 12
chapter_title: Chapter 12
section_number: 3
section_title: 12–2Friction
---
# ## Các Loại Lực và Ý Nghĩa Định Luật — Phân tích Chuyên sâu

*Source: Chapter 12 - Chapter 12 (Section 3) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_12.html)*

## Các Loại Lực và Ý Nghĩa Định Luật — Phân tích Chuyên sâu

### 1. Lực Cản — Phân Tích Nhiều Lớp

Lực cản phụ thuộc Reynolds number $Re = \rho v L / \eta$:

**Re nhỏ** (Stokes flow, $Re < 1$): hạt bụi trong không khí
$$F_{drag} = 6\pi\eta r v \quad \text{(Stokes)}$$

**Re trung bình** (10 < Re < 1000): hạt mưa, viên bi nhỏ
$$F_{drag} \approx cv^{1.5}$$

**Re lớn** ($Re > 1000$): đạn, máy bay, xe hơi
$$F_{drag} = \frac{1}{2}\rho C_D A v^2$$

Không có công thức duy nhất cho mọi chế độ. Đây là minh chứng rõ ràng: lực cản là **lực thực nghiệm**, không phải định luật cơ bản.

### 2. Ý Nghĩa của "Định Luật Vật Lý"

Feynman phân biệt ba cấp độ:

**Cấp 1 — Định luật cơ bản:** $\mathbf{F} = q\mathbf{E}$, $G = 6.674 \times 10^{-11}$ N·m²/kg²
- Chính xác trong mọi điều kiện đã kiểm chứng
- Không có ngoại lệ đã biết
- Giá trị hằng số không phụ thuộc nhiệt độ, áp suất, v.v.

**Cấp 2 — Mô hình tốt:** $F = -kx$ (Hooke), $F = \mu N$ (Coulomb)
- Đúng trong điều kiện nhất định (biến dạng nhỏ, bề mặt nhất định)
- Sai khi vượt giới hạn
- Cần hiệu chỉnh thực nghiệm cho từng hệ thống cụ thể

**Cấp 3 — Mô hình thực nghiệm:** $F = cv^2$, $C_D = f(Re, M)$
- Chỉ xấp xỉ trong dải nhất định
- Cần dữ liệu thực nghiệm (wind tunnel test)
- Không thể tính từ lý thuyết đơn thuần

### 3. Phân Tích: Quỹ Đạo Đạn trong Khí Quyển

**Bài toán:** Đạn khối lượng $m = 0.1$ kg, $C_D = 0.3$, $A = 10^{-4}$ m², mật độ không khí $\rho = 1.2$ kg/m³. Tốc độ đầu nòng $v_0 = 800$ m/s. Tính lực cản và so sánh với trọng lực.

**Lực cản:**
$$F_{drag} = \frac{1}{2} \times 1.2 \times 0.3 \times 10^{-4} \times 800^2 = \frac{1}{2} \times 1.2 \times 0.3 \times 10^{-4} \times 640000$$
$$= \frac{1}{2} \times 23.04 = 11.52 \text{ N}$$

**Trọng lực:** $F_g = mg = 0.1 \times 9.8 = 0.98$ N

**Tỷ lệ:** $F_{drag}/F_g = 11.52/0.98 \approx 11.8$

**Ý nghĩa:** Ở tốc độ đầu nòng, lực cản gấp ~12 lần trọng lực! Quỹ đạo thực hoàn toàn khác quỹ đạo parabol lý tưởng. Khi tốc độ giảm còn $v = 100$ m/s: $F_{drag} = 0.18$ N $< F_g$ — lực cản nhỏ hơn trọng lực.

**Bài học kỹ thuật:** Hệ dẫn đường ballistic phải dùng look-up table $C_D(v, h)$ (phụ thuộc vận tốc và độ cao) để tính quỹ đạo chính xác, không thể dùng công thức đơn giản.

### 4. Mô Hình Lực Trong Hệ Thống Servo Chính Xác

Xét bàn định vị (XY stage) với:

**Lực dẫn động:** Motor tuyến tính, $F_{motor} = K_f \cdot i$
- $K_f$ = force constant (N/A), tính được từ thiết kế nam châm
- Tuyến tính hoàn toàn trong dải hoạt động
- **Loại:** Lực cơ bản (điện từ)

**Lực ma sát:** $F_f = \mu_k \cdot m \cdot g + F_{viscous}(v)$
- $\mu_k$ thay đổi theo mài mòn, nhiệt độ, bôi trơn
- $F_{viscous}$ tuyến tính với vận tốc ở tốc độ thấp
- **Loại:** Lực thực nghiệm

**Phương trình chuyển động tổng:**
$$m\ddot{x} = K_f \cdot i - \mu_k mg - b\dot{x}$$

Bộ điều khiển feedforward tính:
$$i_{ff} = \frac{m\ddot{x}_{ref} + b\dot{x}_{ref}}{K_f}$$

Bộ điều khiển bù ma sát (friction compensator) ước lượng $\mu_k mg$ và cộng thêm vào $i_{ff}$. Phần cơ bản ($K_f$) tính chính xác; phần thực nghiệm ($\mu_k$) cần nhận dạng hệ thống.

### 5. Tại Sao Lực Điện Từ Dễ Điều Khiển

Phương trình lực Lorentz $F = BIL$:
- $B$ = từ trường (đo được hoặc thiết kế được)
- $I$ = dòng điện (điều khiển trực tiếp)
- $L$ = chiều dài dây dẫn trong từ trường (hình học cố định)

**Tuyến tính hoàn toàn** — tăng $I$ gấp đôi → lực tăng gấp đôi. Không có ngưỡng, không có trễ, không phụ thuộc nhiệt độ (trong dải hoạt động bình thường). Đây là lý do motor servo điện tử điều khiển được ở tốc độ cao, chính xác cao — lực là đại lượng cơ bản, tuyến tính.

### Bảng So Sánh

| Lực | Cơ sở | Tuyến tính? | Mô hình hóa | Điều khiển |
|-----|-------|-------------|-------------|------------|
| Lực motor EM | Cơ bản (Lorentz) | Có | Chính xác | Trực tiếp |
| Lực hấp dẫn | Cơ bản (Newton) | Gần đúng | Chính xác | Bù feedforward |
| Lực cản $cv^2$ | Thực nghiệm | Không | Xấp xỉ | Look-up table |
| Lực ma sát | Thực nghiệm | Không | Mô hình LuGre | Adaptive |
| Lực lò xo $kx$ | Xấp xỉ | Có (nhỏ) | Tốt | Bù độ cứng |

---
*Exported from Feynman Bot*
