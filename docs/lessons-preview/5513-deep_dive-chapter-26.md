---
lesson_id: 5513
lesson_type: deep_dive
approval_status: pending
exported_at: "2026-03-02T15:10:31.444789+00:00"
content_hash: e41552df14e3
chapter_number: 26
chapter_title: Chapter 26
section_number: 6
section_title: 26–5A more precise statement of Fermat’s principle
---
# ## Nguyên Lý Stationary Time và Bản Chất Sóng của Ánh Sáng — Phân tích Chuyên sâ

*Source: Chapter 26 - Chapter 26 (Section 6) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_26.html)*

## Nguyên Lý Stationary Time và Bản Chất Sóng của Ánh Sáng — Phân tích Chuyên sâu

### Từ "Minimum" đến "Stationary": Sự Hiệu Chỉnh Quan Trọng

Phiên bản thông thường của nguyên lý Fermat — "ánh sáng đi theo đường tốn ít thời gian nhất" — là không chính xác trong trường hợp tổng quát. Phát biểu đúng là: ánh sáng đi theo đường mà thời gian là **stationary** (cực trị hoặc điểm yên ngựa), tức là đạo hàm bậc nhất bằng không:

$$\delta t = 0 \quad \text{(với mọi biến phân nhỏ } \delta\gamma \text{)}$$

Đây tương tự với tính chất điểm cực trị trong giải tích: $f'(x_0) = 0$ tại điểm cực trị, không cần phân biệt cực tiểu hay cực đại.

**Tại sao điều này quan trọng?** Với gương lõm, tia phản xạ qua điểm hội tụ $F$ thực ra đi theo đường **dài hơn** đường thẳng. Đây là trường hợp cực đại địa phương (local maximum) về thời gian so với các đường phản xạ lân cận không qua $F$. Nhưng điều kiện $\delta t = 0$ vẫn thỏa mãn.

### Cơ Chế Sóng: Tại Sao Stationary Time Lại Quan Trọng?

Ánh sáng là sóng điện từ. Sóng từ nguồn $S$ truyền theo **tất cả đường có thể** đến điểm quan sát $P$, mỗi đường mang một pha:

$$\phi(\gamma) = \frac{2\pi}{\lambda} \cdot c \cdot t(\gamma) = \frac{2\pi}{\lambda} \cdot L(\gamma)$$

trong đó $L(\gamma) = \int_\gamma n\,ds$ là optical path length.

Amplitude tổng tại $P$:
$$A_P = \int_{\text{tất cả } \gamma} a(\gamma) e^{i\phi(\gamma)} d\gamma$$

Khi $\phi(\gamma)$ thay đổi nhanh theo $\gamma$ (không stationary), các đóng góp triệt tiêu nhau (giao thoa phá). Chỉ tại vùng stationary ($d\phi/d\gamma = 0$), pha thay đổi chậm và các đóng góp **giao thoa xây dựng** (constructive interference). Đây là phương pháp **stationary phase approximation** trong toán học.

### Bán Kính Fresnel: Kích Thước "Vùng Ngửi" của Ánh Sáng

Vùng xung quanh đường stationary đóng góp đáng kể vào amplitude có kích thước xác định bởi **bán kính Fresnel** $r_F$:

$$r_F = \sqrt{\frac{\lambda \cdot d_1 \cdot d_2}{d_1 + d_2}}$$

trong đó $d_1$, $d_2$ là khoảng cách từ nguồn và điểm quan sát đến mặt phẳng quan tâm.

**Ví dụ với laser đo lường:**
- $\lambda = 632.8\,\text{nm}$ (He-Ne laser)
- $d_1 = d_2 = 0.5\,\text{m}$
- $r_F = \sqrt{\frac{632.8 \times 10^{-9} \times 0.25}{1}} \approx 0.4\,\text{mm}$

Ý nghĩa: nếu có chướng ngại vật hay khe hở nhỏ hơn $0.4\,\text{mm}$ trên đường quang của hệ đo laser, hiệu ứng nhiễu xạ sẽ xuất hiện và ảnh hưởng đến phép đo!

### Thí Nghiệm Radio Wave: Nhiễu Xạ Qua Khe

Feynman mô tả thí nghiệm kinh điển với sóng radio $\lambda = 3\,\text{cm}$:

**Khe rộng (> vài bước sóng):**
- Sóng đến $D$ (thẳng hàng): các đường lân cận đều có gần cùng thời gian → giao thoa xây dựng → tín hiệu mạnh.
- Sóng đến $D'$ (lệch sang bên): các đường qua các phần khác nhau của khe có thời gian khác nhau → giao thoa phá → tín hiệu yếu.

**Khe hẹp (~ bước sóng):**
- Chỉ còn một vùng Fresnel khả dụng → không có giao thoa phá → sóng phân tán ra mọi hướng → $D'$ nhận được nhiều tín hiệu hơn!

Hệ quả nghịch lý: **khe hẹp hơn → sóng trải rộng hơn**. Đây là nhiễu xạ Fraunhofer, với góc nhiễu xạ $\theta \approx \lambda/a$ ($a$ là chiều rộng khe).

### Ứng Dụng: Nhiễu Xạ trong Hệ Cảm Biến Quang Học

**Aperture diffraction trong encoder quang học:**
Encoder quang học tuyến tính (linear optical encoder) trong hệ servo của bạn sử dụng chùm tia laser qua mạch quang. Nếu aperture (khe đọc) quá nhỏ, nhiễu xạ làm mờ vạch mã, giảm độ phân giải. Ngược lại, aperture quá rộng giảm depth of focus.

Điều kiện tối ưu: aperture $a \approx 2r_F$ để cân bằng giữa độ phân giải không gian và nhiễu xạ.

**Diffraction-limited resolution:**
Giới hạn nhiễu xạ của thấu kính (tiêu chí Rayleigh):
$$\Delta x_{\min} = 1.22 \frac{\lambda f}{D}$$

trong đó $D$ là đường kính thấu kính, $f$ là tiêu cự. Với $\lambda = 633\,\text{nm}$, $f = 50\,\text{mm}$, $D = 25\,\text{mm}$:
$$\Delta x_{\min} = 1.22 \times \frac{633 \times 10^{-6} \times 50}{25} \approx 1.55\,\mu\text{m}$$

Đây là giới hạn tuyệt đối của độ phân giải không gian — không thể vượt qua bằng quang học hình học thông thường!

### Bài Tập Mẫu: Tính Diffraction Limit cho Đầu Đọc Laser

**Đề bài:** Hệ đo dịch chuyển dùng laser $\lambda = 780\,\text{nm}$ với thấu kính hội tụ $f = 20\,\text{mm}$, $D = 10\,\text{mm}$. Tính kích thước spot tại tiêu điểm và xác định xem có đạt độ phân giải $1\,\mu\text{m}$ không.

**Lời giải:**

*Bước 1:* Tính kích thước Airy disk:
$$r_{Airy} = 1.22 \frac{\lambda f}{D} = 1.22 \times \frac{780 \times 10^{-6} \times 20}{10} = 1.22 \times 1.56 \times 10^{-3} \approx 1.9\,\mu\text{m}$$

*Bước 2:* So sánh với yêu cầu $1\,\mu\text{m}$: spot size $\approx 1.9\,\mu\text{m}$ lớn hơn yêu cầu.

*Bước 3:* Để đạt $1\,\mu\text{m}$, cần tăng $D$ hoặc giảm $f$: $D = 1.22 \times \frac{780 \times 10^{-6} \times 20}{1 \times 10^{-3}} \approx 19\,\text{mm}$.

*Ý nghĩa vật lý:* Giới hạn nhiễu xạ xuất phát từ nguyên lý stationary time và bản chất sóng — đây là giới hạn cơ bản của vật lý, không phải giới hạn công nghệ.

### Liên Kết với Nguyên Lý Tác Dụng trong Cơ Học

Nguyên lý stationary time của Fermat là nguyên mẫu của **nguyên lý Hamilton** (principle of least action) trong cơ học:
$$\delta S = \delta \int_{t_1}^{t_2} L(q,\dot{q},t)\,dt = 0$$

trong đó $L$ là Lagrangian. Phương trình Euler-Lagrange — nền tảng của điều khiển tối ưu và quy hoạch quỹ đạo robot — chính là hệ quả trực tiếp. Tư duy "stationary" thống nhất quang học, cơ học, và lý thuyết trường.

---
*Exported from Feynman Bot*
