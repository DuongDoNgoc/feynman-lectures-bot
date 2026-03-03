---
lesson_id: 5384
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:03.698620+00:00"
content_hash: 87d1fb77f081
chapter_number: 11
chapter_title: Chapter 11
section_number: 1
section_title: 11Vectors
---
# ## Đối xứng trong Định luật Vật lý và Vectơ — Phân tích Chuyên sâu

*Source: Chapter 11 - Chapter 11 (Section 1) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_11.html)*

## Đối xứng trong Định luật Vật lý và Vectơ — Phân tích Chuyên sâu

### 1. Bất biến (Invariance) — Nền tảng của Vật lý Hiện đại

Feynman đặt câu hỏi cốt lõi: nếu ta xây dựng một cỗ máy ở vị trí A, rồi sao chép y hệt sang vị trí B với cùng điều kiện ban đầu — cỗ máy ở B có hoạt động y chang không? Nếu có, ta nói **định luật vật lý bất biến dưới phép tịnh tiến**.

Điều này không tầm thường. Nó đòi hỏi:
1. Mọi **nguồn lực liên quan** phải được sao chép cùng (không chỉ cỗ máy)
2. Nếu kết quả khác nhau, **phải tìm nguyên nhân** — không kết luận ngay rằng vật lý không đối xứng

Trong thực nghiệm, phát biểu này đã được kiểm chứng với độ chính xác cao. Hằng số vật lý ($G$, $e$, $m_e$) đồng nhất trên toàn vũ trụ quan sát được.

### 2. Suy dẫn Toán học: Từ Đối xứng đến Vectơ

Xét phương trình Newton trong hệ tọa độ $(x, y, z)$:

$$mrac{d^2x}{dt^2} = F_x, \quad mrac{d^2y}{dt^2} = F_y, \quad mrac{d^2z}{dt^2} = F_z$$

Bây giờ xoay hệ tọa độ quanh trục $z$ một góc $\phi$. Hệ mới $(x', y', z')$ liên hệ với hệ cũ bởi:

$$x' = x\cos\phi + y\sin\phi, \quad y' = -x\sin\phi + y\cos\phi, \quad z' = z$$

**Câu hỏi**: Phương trình Newton có giữ cùng dạng trong hệ $(x', y', z')$ không?

Điều này đúng **nếu và chỉ nếu** lực $\mathbf{F}$ biến đổi theo đúng cùng quy tắc như $(x, y, z)$ biến đổi — tức là $\mathbf{F}$ là một **vectơ**. Đây là lý do các đại lượng có hướng trong vật lý phải là vectơ: không phải quy ước, mà là **yêu cầu của đối xứng**.

### 3. Định nghĩa Chính xác của Vectơ

Một **vectơ** là tập hợp ba số $(A_x, A_y, A_z)$ biến đổi theo cùng quy tắc như tọa độ $(x, y, z)$ khi ta thực hiện phép xoay hệ tọa độ:

$$A_{x'} = A_x\cos\phi + A_y\sin\phi$$
$$A_{y'} = -A_x\sin\phi + A_y\cos\phi$$

Một số đại lượng **trông có vẻ** có hướng nhưng **không phải vectơ** vì không tuân theo quy tắc này (ví dụ: góc hữu hạn trong không gian 3D không cộng giao hoán). Trong kỹ thuật điều khiển, điều này giải thích tại sao phép cộng góc Euler không giao hoán — chúng không phải vectơ thực sự.

### 4. Phép Tính Vectơ

**Cộng vectơ:**
$$\mathbf{a} + \mathbf{b} = (a_x+b_x, \; a_y+b_y, \; a_z+b_z)$$

**Nhân với hằng số:**
$$\alpha\mathbf{a} = (\alpha a_x, \alpha a_y, \alpha a_z)$$

**Tích vô hướng (dot product):**
$$\mathbf{a}\cdot\mathbf{b} = a_x b_x + a_y b_y + a_z b_z = |\mathbf{a}||\mathbf{b}|\cos\theta$$

Tích vô hướng là **bất biến**: có cùng giá trị bất kể hệ tọa độ. Đây là công cụ mạnh để kiểm tra xem một biểu thức có ý nghĩa vật lý không — nếu kết quả phải là vô hướng, dùng dot product.

### 5. Ví dụ Thực tế: Hệ Đo Lường Nhiều Trục

Trong hệ đo lường interferometric 3D (ví dụ: Renishaw XL-80 với beam splitter đa trục), mỗi đầu đo chỉ đo dịch chuyển theo một hướng. Khi bàn máy dịch chuyển theo hướng tùy ý $\mathbf{d} = (d_x, d_y, d_z)$, số đọc của đầu đo thứ $i$ có đơn vị pháp tuyến $\hat{n}_i$ là:

$$L_i = \mathbf{d} \cdot \hat{n}_i = d_x n_{ix} + d_y n_{iy} + d_z n_{iz}$$

Từ ít nhất 3 đầu đo không đồng phẳng, ta giải hệ phương trình để tìm $\mathbf{d}$. Bản chất là đang chiếu vectơ dịch chuyển lên các hướng đo — ứng dụng trực tiếp của tích vô hướng.

### 6. Bài Tập Mẫu

**Bài toán:** Một bàn máy CNC di chuyển theo hướng vectơ đơn vị $\hat{u} = (0.6, 0.8, 0)$. Sensor đặt dọc trục $x$ đọc được $\Delta x = 30\,\mu m$. Tính dịch chuyển thực $d$ của bàn máy.

**Giải:**

Số đọc sensor trục $x$: $L_x = d \cdot \hat{u} \cdot \hat{e}_x = d \times 0.6$

Vậy: $d = \frac{L_x}{0.6} = \frac{30}{0.6} = 50\,\mu m$

**Ý nghĩa vật lý:** Sensor chỉ đo hình chiếu của dịch chuyển. Kỹ sư cần biết hướng chuyển động để suy ra dịch chuyển thực — bài toán vectơ thuần túy.

**Kiểm tra:** Số đọc sensor trục $y$ phải là: $L_y = 50 \times 0.8 = 40\,\mu m$.

### 7. Tích Vô Hướng và Công

Công thực hiện bởi lực $\mathbf{F}$ khi vật dịch chuyển $\mathbf{d}$:

$$W = \mathbf{F} \cdot \mathbf{d} = |F||d|\cos\theta$$

Nếu $\theta = 90°$: lực vuông góc với dịch chuyển không sinh công. Trong động cơ servo, lực từ trường vuông góc với dây dẫn ($\mathbf{F} = I\mathbf{L} \times \mathbf{B}$) sinh ra mô-men — một ứng dụng khác của hình học vectơ.

### Tóm tắt

| Khái niệm | Ý nghĩa | Ứng dụng kỹ thuật |
|-----------|---------|-------------------|
| Đối xứng tịnh tiến | Định luật vật lý giống nhau mọi nơi | Calibration không phụ thuộc vị trí |
| Vectơ | 3 số biến đổi đúng quy tắc khi xoay trục | Coordinate frame transforms |
| Dot product | Bất biến — không phụ thuộc hệ tọa độ | Đo hình chiếu, tính công |
| $m\mathbf{a}=\mathbf{F}$ | 1 phương trình thay 3 — đúng mọi frame | Kiểm soát lực đa trục |

---
*Exported from Feynman Bot*
