---
lesson_id: 5386
lesson_type: concept
approval_status: approved
exported_at: "2026-03-03T15:33:03.757617+00:00"
content_hash: 132d1bec39cc
chapter_number: 11
chapter_title: Chapter 11
section_number: 5
section_title: 11–4Vectors
---
# ## Phân tích Vectơ: Ngôn ngữ Toán học của Đối xứng

*Source: Chapter 11 - Chapter 11 (Section 5) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_11.html)*

## Phân tích Vectơ: Ngôn ngữ Toán học của Đối xứng

Khi bạn đặt một encoder tuyến tính trên băng chuyền và đo dịch chuyển, con số hiển thị phụ thuộc vào hướng đặt encoder. Nếu xoay encoder 45°, cùng một chuyển động thực tế cho số đọc khác. Vậy "dịch chuyển thực" là gì, và làm sao biểu diễn nó độc lập với cách đặt thiết bị đo? Câu trả lời: **vectơ**.

### Hai Loại Đại lượng Vật lý

Vật lý phân chia đại lượng thành hai nhóm chính:

**Vô hướng (scalar):** Một con số, không có hướng. Nhiệt độ, khối lượng, năng lượng. Số đọc của nó không thay đổi khi bạn xoay hệ tọa độ.

**Vectơ:** Ba con số $(x, y, z)$, có hướng. Vận tốc, lực, gia tốc, dịch chuyển. Khi xoay hệ tọa độ, ba số này thay đổi — nhưng thay đổi theo một quy tắc xác định, bảo toàn "thực thể vật lý" phía sau chúng.

### Vectơ Là Gì?

Ký hiệu $\mathbf{r}$ đại diện cho một điểm trong không gian. Trong hệ tọa độ A, nó có tọa độ $(x, y, z)$. Trong hệ tọa độ B (xoay so với A), tọa độ trở thành $(x', y', z')$. Nhưng **điểm vật lý đó vẫn là một** — chỉ cách đo của chúng ta thay đổi.

Bất kỳ đại lượng vật lý nào có ba thành phần biến đổi **đúng theo quy tắc này** đều gọi là vectơ. Lực $\mathbf{F}$, vận tốc $\mathbf{v}$, gia tốc $\mathbf{a}$ đều là vectơ vì chúng biến đổi cùng quy tắc với tọa độ không gian khi xoay trục.

### Quy Tắc Cộng và Nhân

Nếu $\mathbf{a} + \mathbf{b} = \mathbf{c}$, thì:
$$c_x = a_x + b_x, \quad c_y = a_y + b_y, \quad c_z = a_z + b_z$$

Điều quan trọng: quy tắc này đúng trong mọi hệ tọa độ. Không cần viết lại khi đổi frame.

Tích vô hướng tạo ra một **scalar bất biến**:
$$\mathbf{a} \cdot \mathbf{b} = a_x b_x + a_y b_y + a_z b_z = |\mathbf{a}||\mathbf{b}|\cos\theta$$

### Tại Sao Không Phải Mọi "Ba Số" Đều Là Vectơ?

Trong robot học, **góc Euler** $(\alpha, \beta, \gamma)$ cũng là ba số mô tả định hướng — nhưng chúng không phải vectơ vì phép cộng góc Euler **không giao hoán**: xoay quanh $z$ rồi $x$ cho kết quả khác xoay quanh $x$ rồi $z$. Đây là lý do quaternion và ma trận xoay được ưu tiên trong điều khiển định hướng robot.

### Phép So Sánh: Encoder và Hình Chiếu

Trong hệ đo độ thẳng (straightness measurement) của máy CNC, một laser interferometer đo dịch chuyển $\mathbf{d}$ dọc trục danh nghĩa. Nếu bàn máy thực tế lệch hướng góc nhỏ $\epsilon$, số đọc thực là:

$$L = |\mathbf{d}|\cos\epsilon \approx |\mathbf{d}|$$

Sai số $\delta = |\mathbf{d}|(1-\cos\epsilon)$ chính là lỗi Abbe — cũng là bài toán hình chiếu vectơ. Hiểu tích vô hướng giúp bạn ước lượng và bù trừ sai số này.

### Điểm Mấu Chốt

- **Vectơ** = đại lượng có hướng, biến đổi đúng quy tắc khi xoay hệ tọa độ
- **Không phải mọi "ba số"** đều là vectơ (góc Euler không giao hoán)
- **Tích vô hướng** $\mathbf{a}\cdot\mathbf{b}$ là scalar bất biến — thực chất là "chiều dài hình chiếu"
- **Phương trình vectơ** $m\mathbf{a}=\mathbf{F}$ đúng trong mọi frame, không cần viết lại khi đổi hệ tọa độ

---
*Exported from Feynman Bot*
