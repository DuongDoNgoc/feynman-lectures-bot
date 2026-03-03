---
lesson_id: 5569
lesson_type: concept
approval_status: approved
exported_at: "2026-03-03T15:33:08.201229+00:00"
content_hash: 61c55b80458a
chapter_number: 33
chapter_title: Chapter 33
section_number: 2
section_title: 33–1The electric vector of light
---
# ## Phân cực Ánh sáng: Khi Điện trường "Biết Hướng"

*Source: Chapter 33 - Chapter 33 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_33.html)*

## Phân cực Ánh sáng: Khi Điện trường "Biết Hướng"

### Câu hỏi mở đầu

Bạn đã bao giờ nhìn qua kính mắt phân cực (polarized sunglasses) và thấy ánh phản chiếu trên mặt hồ biến mất hoàn toàn? Hay nhìn vào màn hình LCD của máy tính và thấy hình ảnh biến mất khi nghiêng đầu 90 độ? Hiện tượng này không phải ma thuật — nó tiết lộ một tính chất cơ bản của ánh sáng mà chúng ta thường bỏ qua: điện trường của ánh sáng **có hướng**.

---

### Ý tưởng cốt lõi: Ánh sáng là vector

Từ trước đến nay, khi nói về ánh sáng, ta hay nghĩ đến tần số, bước sóng, cường độ — những đại lượng vô hướng. Nhưng thực ra, ánh sáng là **sóng điện từ**, và điện trường $\mathbf{E}$ là một vector. Vector này phải nằm trong mặt phẳng vuông góc với hướng truyền sóng — nhưng trong mặt phẳng đó, nó có thể chỉ về hướng nào tùy ý.

Xét ánh sáng truyền theo trục $z$. Điện trường có thể có thành phần $x$ và thành phần $y$:

$$\mathbf{E} = E_x \hat{x} + E_y \hat{y}$$

Hai thành phần này dao động cùng tần số nhưng có thể **lệch pha** với nhau, tạo ra các kiểu phân cực khác nhau.

---

### Phép so sánh: Con lắc đa chiều

Hãy tưởng tượng một quả cầu treo bằng dây dài, có thể dao động tự do trong mặt phẳng ngang. Đây chính là mô hình trực quan của điện trường ánh sáng:

- **Phân cực tuyến tính (linear polarization)**: Con lắc dao động qua lại theo một đường thẳng. $E_x$ và $E_y$ cùng pha — điện trường luôn chỉ theo một hướng cố định.

- **Phân cực tròn (circular polarization)**: Con lắc quay thành vòng tròn đều. $E_x$ và $E_y$ có biên độ bằng nhau nhưng lệch pha $90°$ — điện trường quay tròn với tốc độ góc $\omega$.

- **Phân cực elip (elliptical polarization)**: Con lắc vẽ hình elip. Trường hợp tổng quát nhất — biên độ $E_x 
eq E_y$ và/hoặc pha lệch tùy ý.

$$\mathbf{E}(t) = E_{0x}\cos(\omega t)\,\hat{x} + E_{0y}\cos(\omega t + \delta)\,\hat{y}$$

Khi $\delta = 0$: phân cực tuyến tính. Khi $\delta = \pm 90°$ và $E_{0x} = E_{0y}$: phân cực tròn.

---

### Ánh sáng thông thường là "hỗn loạn"

Ánh sáng mặt trời hay bóng đèn sợi đốt là **ánh sáng không phân cực** (unpolarized light): điện trường dao động theo mọi hướng ngẫu nhiên trong mặt phẳng vuông góc với tia sáng. Có thể hiểu như hàng triệu con lắc dao động độc lập theo mọi hướng cùng lúc.

Phân cực xảy ra khi ta "lọc" ánh sáng để chỉ giữ lại thành phần theo một hướng nhất định — như chọn chỉ giữ những con lắc dao động theo hướng Bắc-Nam.

---

### Ứng dụng: Cảm biến giao thoa và đo lường chính xác

Trong lĩnh vực cơ điện tử và đo lường chính xác ở cấp độ micromet, phân cực ánh sáng là **nền tảng** của nhiều hệ thống:

**Giao thoa kế laser (laser interferometer)**: Các hệ thống đo dịch chuyển cấp nm (như Renishaw XL-80) dùng ánh sáng phân cực tuyến tính để tạo hai chùm tham chiếu và đo. Bộ chia chùm phân cực (PBS — polarizing beam splitter) tách ánh sáng thành hai nhánh phân cực vuông góc nhau, đo dịch chuyển tương đối qua hiệu pha.

**Cảm biến áp suất quang đàn hồi (photoelastic sensor)**: Vật liệu chịu ứng suất cơ học thay đổi tính chất phân cực của ánh sáng đi qua — đây là cơ sở của kỹ thuật quang đàn hồi (photoelasticity) để đo phân bố ứng suất trong linh kiện cơ khí chính xác.

**Encoder quang học**: Đĩa mã hóa (optical encoder) trong servo motor dùng ánh sáng phân cực và tấm phân tích để đọc vị trí góc với độ phân giải cao.

---

### Điểm mấu chốt

- Ánh sáng là sóng điện từ với điện trường **vector** — phương dao động của vector này là **trạng thái phân cực**
- Ba trạng thái chính: phân cực tuyến tính ($\delta = 0$), phân cực tròn ($\delta = 90°$, $E_x = E_y$), và phân cực elip (tổng quát)
- Ánh sáng tự nhiên là tổ hợp ngẫu nhiên của mọi trạng thái phân cực
- Trong kỹ thuật đo lường chính xác, kiểm soát trạng thái phân cực là chìa khóa để tách tín hiệu, triệt nhiễu, và đạt độ phân giải cấp nm

---
*Exported from Feynman Bot*
