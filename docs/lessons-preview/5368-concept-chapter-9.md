---
lesson_id: 5368
lesson_type: concept
approval_status: approved
exported_at: "2026-03-02T15:10:27.647236+00:00"
content_hash: 3931a77b924c
chapter_number: 9
chapter_title: Chapter 9
section_number: 1
section_title: 9Newton’s Laws of Dynamics
---
# ## Các Định Luật Động Lực Học Newton

*Source: Chapter 9 - Chapter 9 (Section 1) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_09.html)*

## Các Định Luật Động Lực Học Newton

Tại sao một tên lửa đẩy được vào quỹ đạo? Tại sao bánh răng trong hộp số truyền lực theo đúng tỉ lệ? Tại sao đầu đo áp suất rung khi dòng chảy biến động? Tất cả những câu hỏi này có chung một câu trả lời: **Định luật Newton**.

Feynman gọi phát hiện các định luật động lực học là "khoảnh khắc kịch tính trong lịch sử khoa học" — và quả thực, đây là lần đầu tiên con người có thể **tiên đoán** chuyển động của mọi vật thể chỉ bằng ba quy tắc.

---

### Ba Định Luật Newton

**Định luật I (Quán tính):** Vật giữ nguyên trạng thái (đứng yên hoặc chuyển động thẳng đều) trừ khi có lực tác dụng.

**Định luật II (Lực — Gia tốc):** Lực bằng tốc độ thay đổi động lượng:

$$F = \frac{d(mv)}{dt} = ma$$

Khi khối lượng không đổi: $F = ma$, hay theo các thành phần:

$$F_x = m\frac{d^2x}{dt^2}, \quad F_y = m\frac{d^2y}{dt^2}, \quad F_z = m\frac{d^2z}{dt^2}$$

**Định luật III (Phản lực):** Mỗi lực tác dụng đều có phản lực bằng về độ lớn, ngược chiều.

---

### Ý nghĩa sâu của Định luật II

$F = ma$ trông đơn giản nhưng chứa đựng điều phi thường: nó là **phương trình vi phân**. Biết lực tại mọi thời điểm (như hàm của vị trí và vận tốc), ta có thể giải phương trình này để tìm chuyển động của vật mọi lúc — quá khứ và tương lai.

Đây là nền tảng của cơ học dự đoán: từ trạng thái ban đầu + quy luật lực → biết toàn bộ quỹ đạo.

---

### Phép so sánh: Hệ điều khiển servo

Trong servo motor, phương trình động lực học của rotor là:

$$J\frac{d\omega}{dt} = \tau_{điện} - \tau_{tải} - B\omega$$

Đây chính xác là $F = ma$ dưới dạng quay ($J$ = mô men quán tính, $\omega$ = vận tốc góc, $\tau$ = mô men lực, $B$ = ma sát nhớt). Khi lập trình bộ điều khiển servo, bạn đang giải phương trình Newton cho chuyển động quay — chỉ là dưới dạng số hóa.

Trong thiết kế vũ khí, định luật Newton cho phép tính quỹ đạo đạn, lực giật (recoil), và phân phối lực trong cơ cấu truyền động — mọi thứ đều quy về $F = ma$ theo từng trục.

---

### Tại sao "biết luật lực" là đủ?

Feynman nhấn mạnh: nếu biết quy luật lực (như hàm của vị trí và vận tốc), ta **có thể giải từng bước theo thời gian** — không cần giải tích giải tích phân. Phương pháp số (Euler, Runge-Kutta) cho phép máy tính mô phỏng chuyển động bất kỳ.

---

**Điểm mấu chốt:**

- $F = ma$ là phương trình vi phân bậc 2 — biết trạng thái đầu và quy luật lực, toàn bộ quỹ đạo được xác định.
- Trong 3D: bài toán tách thành 3 phương trình độc lập theo $x$, $y$, $z$.
- Động lực học quay của servo motor là ứng dụng trực tiếp của định luật II Newton.
- Phương pháp số (bước nhỏ theo thời gian) cho phép giải $F = ma$ khi không có nghiệm giải tích.


---
*Exported from Feynman Bot*
