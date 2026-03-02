---
lesson_id: 5489
lesson_type: deep_dive
approval_status: pending
exported_at: "2026-03-02T15:10:30.896409+00:00"
content_hash: d22f1559f34d
chapter_number: 23
chapter_title: Chapter 23
section_number: 4
section_title: 23–3Electrical resonance
---
# ## Bài Giảng Chuyên Sâu: Cộng Hưởng Điện — Phân Tích Trở Kháng Phức và Ứng Dụng 

*Source: Chapter 23 - Chapter 23 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_23.html)*

## Bài Giảng Chuyên Sâu: Cộng Hưởng Điện — Phân Tích Trở Kháng Phức và Ứng Dụng Kỹ Thuật

### 1. Từ Phương Trình Vi Phân Đến Đại Số Phức

Phân tích mạch RLC bằng phương trình vi phân tuy chính xác nhưng tốn công. Kỹ thuật điện tử hiện đại dùng **phương pháp phasor** để đơn giản hóa: giả sử nguồn EMF là $\mathcal{E}(t) = \text{Re}[\hat{\mathcal{E}} e^{i\omega t}]$, mọi điện áp và dòng điện đều có dạng phasor nhân với $e^{i\omega t}$. Khi đó phép vi phân $d/dt \to i\omega$, phương trình vi phân trở thành phương trình đại số phức:
$$\hat{I}(\omega) = \frac{\hat{\mathcal{E}}}{Z(\omega)}$$

Trong đó $Z(\omega)$ là **trở kháng phức** (complex impedance). Sau khi giải đại số, lấy phần thực cho kết quả vật lý thực tế.

---

### 2. Trở Kháng Phức Của Từng Phần Tử

Định nghĩa $Z$ sao cho $\hat{V} = Z\hat{I}$:

**Điện trở:** $Z_R = R$ (thuần thực, không lệch pha)

**Tụ điện:**
$$Z_C = \frac{1}{i\omega C} = \frac{-i}{\omega C}$$
Thuần ảo âm. Dòng điện *vượt trước* điện áp 90°. Tại $\omega \to \infty$: $|Z_C| \to 0$ (tụ như dây dẫn); tại $\omega \to 0$: $|Z_C| \to \infty$ (tụ như hở mạch).

**Cuộn cảm:**
$$Z_L = i\omega L$$
Thuần ảo dương. Điện áp *vượt trước* dòng điện 90°. Đặc tính ngược lại tụ điện.

**Tổng trở kháng mạch RLC nối tiếp:**
$$Z(\omega) = R + i\left(\omega L - \frac{1}{\omega C}\right) = R + iX(\omega)$$

Trong đó $X(\omega) = \omega L - 1/(\omega C)$ là **reactance** (kháng trở).

---

### 3. Phân Tích Đầy Đủ Cộng Hưởng

**Biên độ dòng điện:**
$$|\hat{I}| = \frac{\mathcal{E}_0}{|Z|} = \frac{\mathcal{E}_0}{\sqrt{R^2 + X(\omega)^2}}$$

Dòng điện cực đại khi $X = 0$:
$$\omega_0 L = \frac{1}{\omega_0 C} \implies \omega_0 = \frac{1}{\sqrt{LC}}$$

Tại $\omega_0$: $Z = R$, $|\hat{I}|_{max} = \mathcal{E}_0 / R$.

**Góc pha của dòng điện so với EMF:**
$$\phi = \arctan\left(\frac{X(\omega)}{R}\right) = \arctan\left(\frac{\omega L - 1/(\omega C)}{R}\right)$$

| Vùng tần số | Đặc tính | Góc pha $\phi$ |
|-------------|----------|----------------|
| $\omega < \omega_0$ | Capacitive (dung kháng) | $\phi < 0$ (dòng vượt EMF) |
| $\omega = \omega_0$ | Resistive (thuần trở) | $\phi = 0$ |
| $\omega > \omega_0$ | Inductive (cảm kháng) | $\phi > 0$ (EMF vượt dòng) |

---

### 4. Điện Áp Trên Từng Phần Tử — Khuếch Đại Điện Áp

Tại tần số cộng hưởng $\omega = \omega_0$, dòng điện $|\hat{I}| = \mathcal{E}_0/R$:

$$|V_L| = \omega_0 L |\hat{I}| = \frac{\omega_0 L}{R}\mathcal{E}_0 = Q\mathcal{E}_0$$

$$|V_C| = \frac{|\hat{I}|}{\omega_0 C} = \frac{1}{\omega_0 RC}\mathcal{E}_0 = Q\mathcal{E}_0$$

**Cả $V_L$ lẫn $V_C$ đều bằng $Q$ lần điện áp nguồn!** Với $Q = 100$, nguồn $10\,\text{V}$ tạo ra $1000\,\text{V}$ trên tụ và cuộn. Đây là *voltage magnification* — nguy hiểm cho linh kiện nếu không tính toán kỹ, nhưng hữu ích trong thiết kế mạch đánh lửa (ignition circuit) hay stun gun.

$V_L$ và $V_C$ *ngược chiều nhau* (lệch pha 180°), nên chúng triệt tiêu nhau trong tổng $V_L + V_C = 0$, và toàn bộ điện áp nguồn rơi trên $R$.

---

### 5. Hàm Đáp Ứng Tần Số — Biểu Đồ Bode

Dạng chuẩn hóa của hàm truyền dòng điện:
$$H(\omega) = \frac{\hat{I}}{\hat{\mathcal{E}}/R} = \frac{1}{1 + iQ(\omega/\omega_0 - \omega_0/\omega)}$$

**Biên độ:**
$$|H| = \frac{1}{\sqrt{1 + Q^2(\omega/\omega_0 - \omega_0/\omega)^2}}$$

Tại $\omega = \omega_0$: $|H| = 1$ (cực đại). Tại $\omega_{1,2}$ thoả $|H| = 1/\sqrt{2}$ (mức $-3\,\text{dB}$):
$$\omega_{1,2} \approx \omega_0 \pm \frac{\omega_0}{2Q} = \omega_0 \pm \frac{\Delta\omega}{2} \quad (Q \gg 1)$$

Băng thông: $\Delta\omega = \omega_0/Q = R/L$.

Trên đồ thị Bode: đỉnh cộng hưởng càng cao và hẹp khi Q càng lớn.

---

### 6. Năng Lượng và Ý Nghĩa Q

Năng lượng tích trữ tổng:
$$U = \frac{1}{2}L|\hat{I}|^2 + \frac{|\hat{q}|^2}{2C}$$

Tại cộng hưởng, $U_L = U_C = Q\mathcal{E}_0^2/(2R\omega_0)$ dao động qua lại giữa từ trường ($L$) và điện trường ($C$), giống con lắc lý tưởng.

Định nghĩa năng lượng của Q:
$$Q = 2\pi\frac{\text{Năng lượng tích trữ}}{\text{Năng lượng tiêu tán mỗi chu kỳ}} = \frac{\omega_0 L}{R}$$

Đây là lý do Q gọi là "hệ số phẩm chất" — nó đo hiệu quả tích trữ năng lượng của mạch cộng hưởng.

---

### 7. Mạch Cộng Hưởng Song Song (Tank Circuit)

Admittance (hỗ dẫn) của mạch song song:
$$Y(\omega) = \frac{1}{R} + i\left(\omega C - \frac{1}{\omega L}\right)$$

Cộng hưởng khi phần ảo của $Y = 0$: cùng $\omega_0 = 1/\sqrt{LC}$.

Khác biệt: tại $\omega_0$ mạch song song có **trở kháng cực đại** $Z_{max} = R_{parallel} = Q^2 R_L$ (trong đó $R_L$ là điện trở dây cuộn). Dòng từ nguồn cực tiểu, điện áp trên mạch cực đại. Đây là cấu hình dùng trong oscillator (bộ tạo dao động) và RF amplifier.

---

### 8. Ký Sinh và Giới Hạn Mô Hình Lý Tưởng

Trong thực tế linh kiện có **thành phần ký sinh** (parasitics):

- Cuộn cảm: điện trở dây quấn $R_{DC}$, điện dung ký sinh $C_p$ → tần số tự cộng hưởng (SRF)
- Tụ điện: ESR (equivalent series resistance), điện cảm ký sinh $L_s$ → ESL
- Điện trở: điện cảm dây dẫn, điện dung giữa các đầu

Ở tần số MHz–GHz, các yếu tố ký sinh ảnh hưởng đáng kể: $\omega_0$ thực tế lệch so với tính toán, Q giảm, xuất hiện cộng hưởng phụ. Kỹ sư RF dùng:
- Mô hình SPICE đầy đủ với parasitics
- Network analyzer (VNA) đo trở kháng thực tế
- Bố trí PCB cẩn thận (ground plane, via stitching)

---

### 9. Ứng Dụng Trong Hệ Thống Đo Chính Xác

**Cảm biến điện cảm (inductive displacement sensor):** Mạch cộng hưởng LC với cuộn cảm là đầu đo. Khoảng cách đến vật dẫn thay đổi $\to$ hỗ cảm M thay đổi $\to$ $L_{eff}$ thay đổi $\to$ $\omega_0$ dịch chuyển. Độ nhạy:
$$\frac{\Delta\omega_0}{\omega_0} = -\frac{1}{2}\frac{\Delta L}{L}$$

Với $Q = 100$, độ phân giải tần số $\Delta\omega_0/\omega_0 \sim 10^{-5}$ tương ứng $\Delta L/L \sim 2\times10^{-5}$, cho phép đo dịch chuyển cỡ nano-mét.

---

### 10. Tóm Tắt

Phân tích trở kháng phức biến mạch RLC từ bài toán vi phân thành đại số tuyến tính. Tần số cộng hưởng $\omega_0 = 1/\sqrt{LC}$, hệ số Q định lượng độ sắc nét và khuếch đại điện áp ($Q$ lần EMF nguồn trên $L$ và $C$). Mạch nối tiếp và song song có trở kháng cực tiểu/cực đại tại $\omega_0$ cho phép thiết kế bộ lọc chọn lọc cao. Parasitics là thách thức thực tế ở tần số cao, cần mô phỏng và đo kiểm nghiệm để đảm bảo thiết kế chính xác.

---
*Exported from Feynman Bot*
