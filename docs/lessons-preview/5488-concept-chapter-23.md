---
lesson_id: 5488
lesson_type: concept
approval_status: pending
exported_at: "2026-03-02T15:10:30.867329+00:00"
content_hash: 7da12f5d047d
chapter_number: 23
chapter_title: Chapter 23
section_number: 4
section_title: 23–3Electrical resonance
---
# ## Bài Giảng: Cộng Hưởng Trong Mạch Điện — Khái Niệm Cơ Bản

*Source: Chapter 23 - Chapter 23 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_23.html)*

## Bài Giảng: Cộng Hưởng Trong Mạch Điện — Khái Niệm Cơ Bản

### 1. Điện Và Dao Động: Hai Thế Giới, Một Phương Trình

Nếu bạn đã từng thấy một bộ lọc điện tử tách âm bass khỏi treble, hay chiếc radio bắt đúng đài phát sóng, bạn đang chứng kiến *cộng hưởng điện* (electrical resonance) — một ứng dụng thanh lịch và quan trọng bậc nhất của vật lý trong kỹ thuật. Điều thú vị là thế giới điện và thế giới cơ học tuân theo *cùng một phương trình toán học* cho dao động cưỡng bức. Sự tương đồng này không phải trùng hợp ngẫu nhiên — nó phản ánh bản chất phổ quát của dao động.

---

### 2. Ba Loại Phần Tử Thụ Động (Passive Circuit Elements)

Trong mạch điện, có ba loại phần tử cơ bản — gọi là **passive circuit elements** vì chúng không tạo ra năng lượng mà chỉ tích trữ hoặc tiêu tán:

**a) Điện trở (Resistor) — R**

Điện trở tuân theo định luật Ohm: $V_R = IR$

Điện trở *tiêu tán* năng lượng dưới dạng nhiệt. Trong hệ dao động, nó đóng vai trò tương tự **lực cản** (damping) trong cơ học. Đơn vị: Ohm ($\Omega$).

**b) Tụ điện (Capacitor) — C**

Tụ điện *tích trữ* năng lượng trong điện trường:
$$V_C = \frac{q}{C}, \quad I = C\frac{dV_C}{dt}$$

Tụ điện tương đương với **lò xo**: điện áp tỉ lệ với điện tích tích lũy, giống như lực lò xo tỉ lệ với độ dịch chuyển.

**c) Cuộn cảm (Inductor) — L**

Cuộn cảm *tích trữ* năng lượng trong từ trường:
$$V_L = L\frac{dI}{dt}$$

Cuộn cảm tương đương với **khối lượng (quán tính)**: điện áp tỉ lệ với tốc độ biến thiên dòng điện, giống như lực tỉ lệ với gia tốc.

---

### 3. Bảng Tương Đồng Cơ–Điện

| Cơ học | Điện học |
|--------|----------|
| Lực $F$ (nguồn kích thích) | Điện áp $V$ (EMF) |
| Khối lượng $m$ | Điện cảm $L$ |
| Lực cản $\gamma m$ | Điện trở $R$ |
| Độ cứng lò xo $k$ | Nghịch đảo điện dung $1/C$ |
| Dịch chuyển $x$ | Điện tích $q$ |
| Vận tốc $\dot{x}$ | Dòng điện $I = \dot{q}$ |

Bảng này không chỉ là mẹo nhớ — nó cho phép kỹ sư dùng mạch điện để *mô phỏng và phân tích* hệ cơ học phức tạp trước khi chế tạo, tiết kiệm chi phí đáng kể.

---

### 4. Mạch RLC Nối Tiếp — Trái Tim Của Cộng Hưởng Điện

Xét mạch RLC nối tiếp với nguồn EMF $\mathcal{E}(t) = \mathcal{E}_0\cos(\omega t)$. Áp dụng định luật Kirchhoff:
$$L\frac{dI}{dt} + RI + \frac{q}{C} = \mathcal{E}_0\cos(\omega t)$$

Đây chính xác là phương trình dao động cưỡng bức có cản! Dòng điện $I(t)$ đóng vai trò vận tốc, điện tích $q(t)$ đóng vai trò dịch chuyển.

**Tần số tự nhiên của mạch:**
$$\omega_0 = \frac{1}{\sqrt{LC}}$$

Ở tần số $\omega = \omega_0$, mạch đạt **cộng hưởng**: dòng điện đạt cực đại, trở kháng tổng bằng $R$ (phần kháng của $L$ và $C$ triệt tiêu nhau).

---

### 5. Hệ Số Phẩm Chất Q (Quality Factor)

Hệ số Q là thước đo "sắc nét" của cộng hưởng:
$$Q = \frac{\omega_0 L}{R} = \frac{1}{\omega_0 RC} = \frac{\omega_0}{\Delta\omega}$$

Trong đó $\Delta\omega$ là băng thông tại mức công suất giảm một nửa ($-3\,\text{dB}$).

- **Q cao** ($Q \gg 1$): Cộng hưởng sắc nét, chọn lọc dải tần hẹp — dùng trong bộ lọc chọn lọc, anten thu sóng.
- **Q thấp** ($Q \sim 1$): Cộng hưởng rộng — dùng trong bộ lọc băng rộng.

Một ý nghĩa khác của Q: điện áp trên $L$ hoặc $C$ tại cộng hưởng bằng $Q$ lần điện áp nguồn. Đây là *khuếch đại điện áp* (voltage magnification) — cần lưu ý khi thiết kế để tránh hỏng linh kiện.

---

### 6. Ứng Dụng Thực Tế

- **Radio/TV tuner**: Thay đổi $C$ (tụ biến dung) để điều chỉnh $\omega_0$, chọn đài phát.
- **Bộ lọc tần số** trong âm thanh: Tách bass, mid, treble với mạch RLC có Q và $\omega_0$ khác nhau.
- **Cảm biến điện cảm (eddy current sensor)**: Khoảng cách thay đổi làm $L$ thay đổi, kéo theo $\omega_0$ dịch chuyển. Đo $\Delta\omega_0$ cho phép xác định vị trí với độ phân giải nano-mét.
- **Nguồn switching**: Mạch cộng hưởng trong converter LLC giúp đạt hiệu suất cao ở tần số MHz.

---

### 7. Tóm Tắt

Cộng hưởng trong mạch điện là biểu hiện điện của cùng hiện tượng vật lý như dao động cưỡng bức cơ học. Ba phần tử R, L, C tương ứng với cản, quán tính và lò xo. Tần số cộng hưởng $\omega_0 = 1/\sqrt{LC}$ và hệ số Q xác định đặc tính lọc tần số. Bảng tương đồng cơ–điện là công cụ tư duy mạnh mẽ cho mọi kỹ sư thiết kế hệ thống dao động.

---
*Exported from Feynman Bot*
