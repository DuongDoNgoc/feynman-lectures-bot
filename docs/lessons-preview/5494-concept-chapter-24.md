---
lesson_id: 5494
lesson_type: concept
approval_status: approved
exported_at: "2026-03-03T15:33:06.490820+00:00"
content_hash: 1f75aebb12e4
chapter_number: 24
chapter_title: Chapter 24
section_number: 4
section_title: 24–3Electrical transients
---
# ## Bài Giảng: Quá Độ Điện — Thực Nghiệm Với Mạch RLC và Oscilloscope

*Source: Chapter 24 - Chapter 24 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_24.html)*

## Bài Giảng: Quá Độ Điện — Thực Nghiệm Với Mạch RLC và Oscilloscope

### 1. Từ Lý Thuyết Đến Thực Nghiệm

Trong các bài trước, chúng ta đã phân tích phương trình dao động tắt dần về mặt toán học. Bây giờ Feynman đưa chúng ta vào phòng thí nghiệm: liệu những gì lý thuyết dự đoán có thực sự xảy ra trong mạch điện không?

Để kiểm nghiệm, ta xây dựng mạch RLC đơn giản và dùng **oscilloscope** để quan sát điện áp trên cuộn cảm $L$ ngay sau khi đóng công tắc $S$. Oscilloscope vẽ điện áp theo thời gian trực tiếp trên màn hình — đây là "con mắt điện tử" hiện thực hóa những đường cong toán học chúng ta đã tính.

---

### 2. Cách Hoạt Động Của Thí Nghiệm

**Cấu hình mạch:** Cuộn cảm $L$, tụ điện $C$, và điện trở biến đổi $R$ mắc nối tiếp với công tắc $S$ và nguồn DC. Oscilloscope đo điện áp $V_L$ trên $L$.

**Thủ thuật lặp lại:** Thay vì đóng mở công tắc tay (mắt không theo kịp), mạch được kích thích tự động $f$ lần/giây. Mỗi lần đóng công tắc đồng thời kích hoạt quét ngang của oscilloscope — kết quả là đường cong được vẽ *đè lên nhau* nhiều lần, cho ảnh rõ nét nhờ hiện tượng lưu ảnh (persistence of vision).

---

### 3. Các Trường Hợp Quan Sát

**Trường hợp 1: Q cao, R nhỏ — Underdamping**

$$x(t) \propto e^{-\gamma t/2}\cos(\omega_1 t)$$

Oscilloscope (Hình 24–3): Đường sin tắt dần, dao động nhiều lần trước khi biến mất. Tần số dao động $\omega_1 \approx \omega_0 = 1/\sqrt{LC}$. Đây là chế độ điển hình của mạch cộng hưởng cao phẩm chất.

**Trường hợp 2: Q trung bình — Tăng R**

Tăng điện trở $R$ làm $\gamma = R/L$ tăng. Oscilloscope (Hình 24–4): Dao động tắt nhanh hơn — biên độ giảm mạnh hơn sau mỗi chu kỳ. Tần số hơi thấp hơn vì $\omega_1 = \sqrt{\omega_0^2 - \gamma^2/4} < \omega_0$.

**Trường hợp 3: R lớn hơn nữa**

Oscilloscope (Hình 24–5): Chỉ còn 1–2 dao động rồi tắt. Gần ngưỡng critical damping.

**Trường hợp 4: Overdamping ($R > 2\sqrt{L/C}$)**

Oscilloscope (Hình 24–6): **Không có dao động!** Điện áp tăng lên, đạt đỉnh, rồi giảm dần theo hàm mũ. Đây là chế độ overdamped — hệ "nặng nề" quá không thể dao động.

---

### 4. Phân Tích Định Lượng

Điều kiện critical damping trong mạch điện:
$$\gamma_c = \frac{R_c}{L} = 2\omega_0 = \frac{2}{\sqrt{LC}}$$
$$\implies R_c = 2\sqrt{\frac{L}{C}}$$

Đây là giá trị điện trở tới hạn (critical resistance). Với $L = 10\,\text{mH}$, $C = 1\,\mu\text{F}$:
$$R_c = 2\sqrt{\frac{10^{-2}}{10^{-6}}} = 2\sqrt{10^4} = 200\,\Omega$$

Khi $R < 200\,\Omega$: underdamped; khi $R > 200\,\Omega$: overdamped.

---

### 5. Hệ Số Q Từ Quan Sát Oscilloscope

Đo Q trực tiếp từ dạng sóng oscilloscope:
$$Q = \pi\frac{t_1}{T_1}\frac{1}{\ln(A_1/A_2)}$$

Trong đó $A_1, A_2$ là biên độ của hai đỉnh liên tiếp, $T_1$ là chu kỳ. Hoặc đơn giản hơn:
$$Q \approx \frac{\omega_1}{2} \cdot \frac{1}{\gamma/2} = \frac{\omega_1}{\gamma}$$

Đây là phương pháp đo Q *trực tiếp từ thực nghiệm* — quan trọng vì giá trị R, L, C thực tế thường khác giá trị danh định.

---

### 6. Tương Đồng Với Hệ Cơ Học

Mạch RLC điện tương đương với hệ cơ học:
- Đóng công tắc = kéo lò xo rồi thả
- Oscilloscope = đầu đo dịch chuyển laser interferometer
- Điện trở R = lực cản nhớt (viscous damping)

Thí nghiệm điện dễ thực hiện, tốn ít chi phí, và dễ thay đổi tham số hơn thí nghiệm cơ học. Đây là lý do kỹ sư thường dùng mô phỏng mạch điện tương đương (electrical analog) để nghiên cứu hệ cơ học phức tạp trước khi chế tạo.

---

### 7. Ứng Dụng Kỹ Thuật

- **Kiểm tra đặc tính hệ cơ học:** Đo tần số và hệ số tắt dần từ step response để xác định $\omega_0$ và $Q$ của cơ cấu.
- **Thiết kế bộ giảm chấn:** Chọn vật liệu và kết cấu để đạt critical damping cho máy in chính xác, cân phân tích.
- **Kiểm tra mạch điện:** Kỹ sư dùng step response để nhanh chóng đo $L$ và $C$ chưa biết trong mạch.

---

### 8. Tóm Tắt

Thí nghiệm oscilloscope với mạch RLC minh họa trực quan ba chế độ tắt dần: underdamped (dao động tắt), critically damped (về 0 nhanh nhất, không dao động), overdamped (về 0 chậm, không dao động). Tăng điện trở $R$ chuyển mạch từ underdamped sang overdamped qua ngưỡng critical $R_c = 2\sqrt{L/C}$. Đây là kiểm nghiệm trực tiếp lý thuyết dao động tắt dần và là nền tảng cho phân tích step response trong kỹ thuật điều khiển.

---
*Exported from Feynman Bot*
