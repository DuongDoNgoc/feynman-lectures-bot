---
lesson_id: 5395
lesson_type: concept
approval_status: approved
exported_at: "2026-03-03T15:33:03.997219+00:00"
content_hash: d6e9c6572372
chapter_number: 12
chapter_title: Chapter 12
section_number: 3
section_title: 12–2Friction
---
# ## Các Loại Lực: Từ Lực Cản đến Trường Điện Từ

*Source: Chapter 12 - Chapter 12 (Section 3) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_12.html)*

## Các Loại Lực: Từ Lực Cản đến Trường Điện Từ

Tại sao quả đạn pháo bay khác với hạt mưa? Một phần vì lực cản không khí — nhưng định luật cho lực cản này ở dạng nào? Và tại sao nó khác hoàn toàn với định luật cho lực điện từ trong động cơ?

### Lực Cản Không Khí — Quy Luật Thực Nghiệm

Thực tế, không có công thức tổng quát duy nhất cho lực cản. Tuy nhiên, thực nghiệm cho thấy hai giới hạn:

- **Tốc độ thấp** (viscous drag): $F_{drag} \approx \eta v$ (tỷ lệ tuyến tính với vận tốc)
- **Tốc độ cao** (inertial drag): $F_{drag} \approx cv^2$

Đối với vật bay (đạn, tên lửa, máy bay), regime $cv^2$ thường áp dụng. Hằng số $c$ phụ thuộc vào diện tích mặt cắt, hệ số drag $C_D$ (phụ thuộc hình dạng và Reynolds number):

$$F_{drag} = \frac{1}{2}\rho C_D A v^2$$

**Chú ý:** Đây không phải định luật cơ bản — nó chỉ là mô hình thực nghiệm tốt trong một dải nhất định.

### Lực Đàn Hồi — Giới Hạn Tuyến Tính

Lực đàn hồi của lò xo (Hooke): $F = -kx$

Đây cũng không phải định luật cơ bản. Ở cấp phân tử, lực giữa các nguyên tử là phi tuyến (Lennard-Jones). Hooke là xấp xỉ tuyến tính quanh điểm cân bằng — chỉ đúng với biến dạng nhỏ.

### Lực Điện Từ — Định Luật Cơ Bản

Khác hoàn toàn với lực cản và ma sát, lực điện từ có định luật chính xác:

$$\mathbf{F} = q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$$

Đây là **lực Lorentz** — định luật cơ bản, không có ngoại lệ, chính xác đến mức kiểm chứng bằng thực nghiệm tốt nhất hiện có.

### Ý Nghĩa của "Định Luật"

Feynman đặt câu hỏi sâu sắc: khi nói $F = cv^2$, đó có phải "sự thật" không? Hay chỉ là mô hình tiện dụng?

Sự thật là: $F = cv^2$ là **hiện tượng luận** (phenomenological) — đúng khi Reynolds number trong dải nhất định, nhưng phá vỡ ở siêu âm, ở mật độ không khí khác, ở hình dạng khác. Khác với $\mathbf{F} = q\mathbf{E}$ — đây là định luật thực sự, không phá vỡ trong mọi điều kiện đã biết.

### So Sánh: Thiết Kế Hệ Thống Vũ khí

Trong tên lửa dẫn đường, bộ điều hướng (guidance system) cần mô hình lực tác dụng lên tên lửa:

- **Lực đẩy động cơ** ($F_{thrust}$): dựa trên đốt cháy nhiên liệu — phức tạp, cần thực nghiệm
- **Lực cản khí động** ($F_{drag} = C_D \cdot \frac{1}{2}\rho v^2 A$): thực nghiệm, thay đổi theo Mach number
- **Lực hấp dẫn** ($\mathbf{F}_g = m\mathbf{g}$): định luật cơ bản, tính chính xác

Bộ điều hướng phải kết hợp cả ba loại — phần "cơ bản" tính chính xác, phần "thực nghiệm" tra bảng (look-up table) từ dữ liệu thử nghiệm.

### Điểm Mấu Chốt

- **Lực cản** $F \approx cv^2$: thực nghiệm, phụ thuộc điều kiện
- **Lực đàn hồi** $F = -kx$: xấp xỉ tuyến tính, giới hạn biến dạng nhỏ
- **Lực điện từ** $\mathbf{F} = q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$: định luật cơ bản, chính xác mọi điều kiện
- Hệ thống kỹ thuật dùng hỗn hợp: mô hình lý thuyết cho lực cơ bản, look-up table cho lực phức tạp

---
*Exported from Feynman Bot*
