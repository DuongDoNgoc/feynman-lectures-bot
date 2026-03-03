---
lesson_id: 5554
lesson_type: concept
approval_status: approved
exported_at: "2026-03-03T15:33:07.841884+00:00"
content_hash: 7f1ffb0df73d
chapter_number: 31
chapter_title: Chapter 31
section_number: 3
section_title: 31–2The field due to the material
---
# ## Tính Toán Chiết Suất Từ Đầu: Khi Vật Lý Vi Mô Gặp Quang Học Vĩ Mô

*Source: Chapter 31 - Chapter 31 (Section 3) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_31.html)*

## Tính Toán Chiết Suất Từ Đầu: Khi Vật Lý Vi Mô Gặp Quang Học Vĩ Mô

Nhiều năm bạn dùng chiết suất $n$ trong các công thức quang học mà không bao giờ thắc mắc: con số $n = 1.5$ cho thủy tinh ấy — nó đến từ đâu? Nó có thể được **tính toán từ đầu** (from first principles) từ các tính chất vi mô của nguyên tử không? Câu trả lời là: có thể, và đây là một trong những kết quả đẹp nhất của vật lý cổ điển.

---

### Điểm Xuất Phát: Trường Tổng Hợp

Feynman đã thiết lập ở bài trước rằng trường điện tổng tại điểm $P$ (phía sau tấm kính) có dạng:

$$E_{\text{total}} = E_s + E_a$$

Trong đó $E_s$ là trường từ nguồn ngoài (lan truyền tốc độ $c$) và $E_a$ là trường từ các electron trong tấm kính. Ta đã có:

$$E_{\text{total}} \approx E_0 e^{i\omega(t-z/c)} \cdot e^{i\phi}$$

với $\phi = (n-1)\omega\Delta z/c$ là lệch pha do tấm kính gây ra. Câu hỏi bây giờ là: liệu $E_a$ có thực sự tạo ra đúng hiệu pha này không? Và từ đó, $n$ phải bằng bao nhiêu?

---

### Bảng Tổng Hợp Các Ký Hiệu (Quan Trọng!)

Before đi vào toán học, Feynman liệt kê tất cả ký hiệu để không bị nhầm lẫn:

| Ký hiệu | Ý nghĩa |
|---|---|
| $E_s$ | Trường từ nguồn ngoài |
| $E_a$ | Trường từ các điện tích trong tấm kính |
| $\Delta z$ | Chiều dày tấm kính |
| $z$ | Khoảng cách vuông góc từ tấm kính |
| $n$ | Chiết suất |
| $\omega$ | Tần số góc của bức xạ |
| $N_V$ | Số điện tích trên đơn vị thể tích |
| $N_a$ | Số điện tích trên đơn vị diện tích ($= N_V \Delta z$) |
| $e$ | Điện tích electron |
| $m$ | Khối lượng electron |
| $\omega_0$ | Tần số cộng hưởng của electron trong nguyên tử |

Việc ghi rõ bảng ký hiệu này không phải hình thức — khi tính toán phức tạp, nhầm ký hiệu một lần là sai hết!

---

### Thiết Lập Bài Toán: Trường Tại Tấm Kính

Nguồn $S$ ở rất xa bên trái, nên trường tại tấm kính là sóng phẳng:
$$E_s = E_0 e^{i\omega t} \quad \text{(tại } z=0 \text{)}$$

Mỗi electron trong nguyên tử bị kích thích bởi trường này và dao động theo phương $x$ (hướng phân cực). Theo mô hình dao động tử điều hòa:

$$m\ddot{x} + m\omega_0^2 x = eE_s$$

Nghiệm cưỡng bức dừng:
$$x = \frac{e E_0 e^{i\omega t}}{m(\omega_0^2 - \omega^2)}$$

Đây là phương trình đơn giản nhưng chứa đựng bản chất vật lý sâu sắc: tần số ánh sáng $\omega$ so với tần số cộng hưởng $\omega_0$ quyết định pha và biên độ dao động.

---

### Tính Trường $E_a$ Từ Các Electron Dao Động

Bây giờ là phần kỹ thuật nhất: tổng hợp đóng góp của vô số electron trong tấm kính mỏng.

Mỗi electron gia tốc với $\ddot{x} = -\omega^2 x$, phát ra trường bức xạ. Khi tích phân trên toàn bộ diện tích tấm kính (xem tấm kính vô hạn theo phương ngang), đóng góp từ các vành đai tròn tại khoảng cách $r$ khác nhau tổng hợp lại theo cách đặc biệt: **chỉ những đóng góp gần trục thẳng đứng mới không bị triệt tiêu**, và kết quả là trường lan truyền dọc theo trục $z$.

Kết quả tích phân cho trường tại điểm $P$ (khoảng cách $z$ từ tấm kính):

$$E_a = \frac{-iNe^2\omega}{2m\varepsilon_0 c(\omega_0^2 - \omega^2)} \cdot E_0 e^{i\omega(t-z/c)} \cdot \Delta z$$

Trường này có **pha lệch $-90°$ ($= -i$)** so với $E_s$.

---

### So Sánh Với Hiệu Pha Mong Đợi: Rút Ra Giá Trị $n$

Trường tổng:
$$E_{\text{total}} = E_s + E_a = E_0 e^{i\omega(t-z/c)} \left[1 - \frac{iNe^2\omega\Delta z}{2m\varepsilon_0 c(\omega_0^2-\omega^2)}\right]$$

Dùng xấp xỉ $1 + i\phi \approx e^{i\phi}$ (với $\phi$ nhỏ):
$$E_{\text{total}} \approx E_0 \exp\left[i\omega\left(t - \frac{z}{c}\right) - i\frac{Ne^2\omega\Delta z}{2m\varepsilon_0 c(\omega_0^2-\omega^2)}\right]$$

Mặt khác, nếu tấm kính có chiết suất $n$ thực sự, hiệu pha tích lũy qua chiều dày $\Delta z$ phải là:
$$\Delta\phi_{\text{mong đợi}} = \omega(n-1)\Delta z/c$$

So sánh hai biểu thức:
$$\frac{\omega(n-1)\Delta z}{c} = \frac{Ne^2\omega\Delta z}{2m\varepsilon_0 c(\omega_0^2-\omega^2)}$$

Rút ra:
$$\boxed{n = 1 + \frac{Ne^2}{2m\varepsilon_0(\omega_0^2-\omega^2)}}$$

Đây là **chiết suất được tính toán từ đầu** — không có tham số điều chỉnh tùy tiện!

---

### Ý Nghĩa Vật Lý Và Ứng Dụng Kỹ Thuật

Công thức này không chỉ là kết quả lý thuyết đẹp — nó có hàm ý kỹ thuật thực tế:

**1. Hệ số thermo-optic (dn/dT):** Khi nhiệt độ thay đổi, mật độ $N$ thay đổi (giãn nở nhiệt), và tần số cộng hưởng $\omega_0$ cũng dịch chuyển nhẹ. Từ công thức trên:
$$\frac{dn}{dT} = \frac{-Ne^2}{2m\varepsilon_0(\omega_0^2-\omega^2)} \cdot \frac{1}{N}\frac{dN}{dT} + \frac{Ne^2 \cdot 2\omega_0}{2m\varepsilon_0(\omega_0^2-\omega^2)^2}\frac{d\omega_0}{dT}$$

Với kính quang học: $dn/dT \sim 10^{-6}/°C$ đến $10^{-5}/°C$ — quan trọng với hệ đo micro-mét.

**2. Áp suất quang học của vật liệu:** Môi trường chỉ số khúc xạ $n$ khác nhau gây ra **lực bức xạ** (radiation pressure) — cơ sở của optical tweezers dùng trong nghiên cứu sinh học và MEMS.

**3. Thiết kế thấu kính:** Nhà sản xuất kính quang học kiểm soát thành phần hóa học (thay đổi $N$ và $\omega_0$) để đạt chiết suất và tán sắc theo ý muốn — đây là cơ sở của kính achromatic và apochromatic.

---

### Điểm Mấu Chốt

- **Trường tổng** $E_{\text{total}} = E_s + E_a$ là nền tảng để tính chiết suất vi mô
- **Trường thứ cấp** $E_a$ từ electron dao động lệch pha $90°$ so với $E_s$
- **Chiết suất Lorentz**: $n = 1 + Ne^2/[2m\varepsilon_0(\omega_0^2-\omega^2)]$ — kết nối vi mô và vĩ mô
- **Tán sắc**: $n$ phụ thuộc $\omega$ → ánh sáng các màu đi với tốc độ khác nhau
- **Ứng dụng**: thermo-optic effect, thiết kế thấu kính, cảm biến áp suất/nhiệt độ bằng quang học

---
*Exported from Feynman Bot*
