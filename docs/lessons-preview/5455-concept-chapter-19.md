---
lesson_id: 5455
lesson_type: concept
approval_status: approved
exported_at: "2026-03-02T15:10:29.865219+00:00"
content_hash: 5cf029f2472f
chapter_number: 19
chapter_title: Chapter 19
section_number: 2
section_title: 19–1Properties of the center of mass
---
# ## Trung Tâm Khối: Điểm Ma Thuật của Mọi Vật Thể

*Source: Chapter 19 - Chapter 19 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_19.html)*

## Trung Tâm Khối: Điểm Ma Thuật của Mọi Vật Thể

Tưởng tượng bạn cầm một cây búa và thử quăng nó lên không trung. Nhìn kỹ chuyển động: đầu búa và cán búa xoay loạn xạ, nhưng có **một điểm duy nhất** chuyển động theo đường parabol hoàn hảo — như thể toàn bộ khối lượng cây búa tập trung tại đó. Điểm đó chính là **trung tâm khối** (center of mass, CM). Đây không phải thủ thuật toán học — đây là thực tế vật lý sâu sắc.

### Tại Sao Trung Tâm Khối Tồn Tại?

Từ chương trước, chúng ta biết: ngoại lực tổng hợp bằng tốc độ thay đổi tổng động lượng. Feynman chứng minh rằng tổng $\sum_i m_i \vec{r}_i$ có một điểm đặc biệt, gọi là $\vec{R}_{\text{CM}}$, sao cho:
$$M\vec{a}_{\text{CM}} = \vec{F}_{\text{ext}}$$

trong đó $M = \sum_i m_i$ là tổng khối lượng. Nội lực (lực giữa các hạt trong hệ) triệt tiêu hoàn toàn. Vật thể phức tạp đến mức nào — ô tô, vũ khí, robot — đều tuân theo quy tắc đơn giản này cho trung tâm khối.

### Định Nghĩa và Cách Tính

Vị trí trung tâm khối:
$$X_{\text{CM}} = \frac{\sum_i m_i x_i}{\sum_i m_i} = \frac{\sum_i m_i x_i}{M}$$

Đây là **trung bình có trọng số** của các vị trí — mỗi phần tử khối lượng "kéo" CM về phía nó theo tỉ lệ khối lượng. Nếu tất cả phần tử có cùng khối lượng $m$:
$$X_{\text{CM}} = \frac{m\sum x_i}{mN} = \frac{\sum x_i}{N}$$

— chỉ là trung bình số học của vị trí. Đơn giản và đẹp.

### Phép So Sánh Kỹ Thuật: CM như Weighted Average trong Xử Lý Tín Hiệu

Kỹ sư cơ điện tử quen thuộc với **weighted average** trong digital signal processing. Bộ lọc FIR tính đầu ra:
$$y[n] = \sum_k h[k] \cdot x[n-k]$$

Đây chính xác là công thức CM: $h[k]$ (hệ số lọc) tương ứng $m_i$ (khối lượng), $x[n-k]$ (mẫu tín hiệu) tương ứng $x_i$ (vị trí). Trung tâm khối là "trọng tâm thống kê" của phân phối khối lượng — giống như mean của một phân phối xác suất nơi $m_i/M$ là xác suất.

Trong đo lường độ chính xác cao, kỹ thuật **centroid detection** trong xử lý ảnh cảm biến (CCD/CMOS) tính vị trí chính xác của vật thể bằng công thức CM:
$$x_{\text{centroid}} = \frac{\sum_{i,j} I_{ij} \cdot x_j}{\sum_{i,j} I_{ij}}$$

trong đó $I_{ij}$ là cường độ pixel — hoàn toàn tương tự CM với khối lượng thay bằng cường độ sáng. Phương pháp này cho phép đo vị trí với độ chính xác sub-pixel, tức là dưới micrometer với optical setup phù hợp.

### Ứng Dụng Quan Trọng: Balancing và Vibration

Trong thiết kế vũ khí và hệ thống cơ khí chính xác, trung tâm khối là thông số thiết kế sống còn:

**1. Cân bằng động (dynamic balancing):** Rotor của motor servo, turbine, hay spindle phải có CM nằm chính xác trên trục quay. Nếu CM lệch khỏi trục một khoảng $e$ (eccentricity), lực ly tâm $F = m\omega^2 e$ gây rung động ở tần số quay. Với spindle CNC tốc độ cao ($\omega = 5000$ RPM $= 524$ rad/s), eccentricity $e = 1$ mm trên mass $m = 0.5$ kg tạo lực $F = 0.5 \times 524^2 \times 10^{-3} = 137$ N — đủ để gây sai số gia công micrometer và hỏng vòng bi.

**2. Hệ thống vũ khí:** CM của đạn pháo hay tên lửa phải nằm trước trung tâm áp lực (center of pressure) để đảm bảo bay ổn định. Đây là nguyên lý tương tự như CM của máy bay phải nằm trước neutral point.

**3. Tính chất cộng của CM:** Nếu biết CM của từng bộ phận:
$$M \vec{R}_{\text{CM}} = M_A \vec{R}_{\text{CM,A}} + M_B \vec{R}_{\text{CM,B}}$$

Kỹ sư không cần tính lại từ đầu khi thêm bộ phận — chỉ cần kết hợp CM của các phần như những điểm vật chất. Trong CAD software, đây là thuật toán tính CM của cụm lắp ghép phức tạp.

### Thí Nghiệm Tư Duy: Tên Lửa Nổ Giữa Chừng

Một tên lửa bay theo quỹ đạo parabol thì nổ tung. Mảnh vỡ bay tứ tán. Nhưng tổng ngoại lực vẫn chỉ là trọng lực $M\vec{g}$. Vậy CM của hệ mảnh vỡ vẫn tiếp tục chuyển động theo đúng quỹ đạo parabol ban đầu — như thể vụ nổ không xảy ra! Nội lực của vụ nổ không thay đổi quỹ đạo CM. Đây là nguyên lý pháo hoa và cũng là cơ sở tính toán mảnh văng trong phân tích đạn đạo.

**Điểm mấu chốt:**

- Trung tâm khối là điểm duy nhất của vật thể tuân theo $\vec{F} = M\vec{a}$ như một hạt điểm — bất kể bên trong phức tạp đến đâu
- CM là trung bình có trọng số của vị trí các phần tử: $X_{\text{CM}} = \sum m_i x_i / \sum m_i$ — đây chính xác là phép tính centroid trong xử lý ảnh cảm biến độ chính xác cao
- Tính cộng của CM cho phép phân chia và kết hợp: CM của hệ phức tạp tính được từ CM của các bộ phận — nền tảng của thuật toán CAD và cân bằng động học trong thiết kế cơ khí
- Với kỹ sư cơ điện tử, hiểu CM nghĩa là hiểu tại sao rotor mất cân bằng gây rung động, tại sao đạn pháo cần CM trước center of pressure, và tại sao centroid detection cho độ chính xác sub-pixel trong hệ thống đo lường quang học

---
*Exported from Feynman Bot*
