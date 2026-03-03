---
lesson_id: 5597
lesson_type: deep_dive
approval_status: pending
exported_at: "2026-03-03T15:33:08.837462+00:00"
content_hash: 72a40abf27ae
chapter_number: 35
chapter_title: Chapter 35
section_number: 5
section_title: 35–4The chromaticity diagram
---
# ## Sơ Đồ Màu Sắc (Chromaticity Diagram) — Phân tích Chuyên sâu

*Source: Chapter 35 - Chapter 35 (Section 5) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_35.html)*

## Sơ Đồ Màu Sắc (Chromaticity Diagram) — Phân tích Chuyên sâu

### 1. Biểu diễn màu sắc như vector trong không gian 3 chiều

Mỗi màu sắc có thể biểu diễn theo phương trình:

$$C = a\mathbf{R} + b\mathbf{G} + c\mathbf{B}$$

trong đó $a$, $b$, $c$ là các hệ số (color coefficients) tương ứng với ba màu cơ bản (primaries): đỏ (Red), xanh lá (Green), xanh lam (Blue). Một màu bất kỳ là một **điểm trong không gian 3 chiều** với tọa độ $(a, b, c)$.

Nếu màu thứ hai có hệ số $(a', b', c')$, thì màu hỗn hợp của hai màu này là:

$$C_{mix} = (a + a')\mathbf{R} + (b + b')\mathbf{G} + (c + c')\mathbf{B}$$

Đây chính là phép **cộng vector** — hoàn toàn tuyến tính (linear). Ý nghĩa vật lý: ánh sáng là sóng điện từ, cường độ các bước sóng cộng chồng lên nhau một cách tuyến tính, không có hiệu ứng phi tuyến ở mức nhận thức màu sắc khi cường độ ở ngưỡng bình thường.

### 2. Chiếu xuống mặt phẳng chromaticity — loại bỏ độ sáng

Nhân đôi $a$, $b$, $c$ đồng thời (nhân cùng một hệ số $k > 0$) cho cùng màu sắc, chỉ khác độ sáng. Do đó, **màu sắc** (chroma) không phụ thuộc vào độ sáng tuyệt đối, chỉ phụ thuộc vào **tỉ lệ** giữa $a$, $b$, $c$.

Ta chuẩn hóa bằng cách chiếu mọi điểm $(a, b, c)$ lên mặt phẳng $a + b + c = 1$:

$$x = \frac{a}{a+b+c}, \quad y = \frac{b}{a+b+c}, \quad z = \frac{c}{a+b+c} = 1 - x - y$$

Chỉ cần hai tọa độ $x$ và $y$ là đủ xác định màu sắc — đó chính là **sơ đồ chromaticity (CIE 1931)**. Đây là một phép **chiếu xuyên tâm (central projection)** từ gốc tọa độ lên mặt phẳng $a+b+c=1$.

### 3. Tính chất quan trọng: màu hỗn hợp nằm trên đoạn thẳng

Xét hai màu $P_1 = (x_1, y_1)$ và $P_2 = (x_2, y_2)$ trên sơ đồ chromaticity. Màu hỗn hợp với tỉ lệ $\lambda : (1-\lambda)$ là:

$$P_{mix} = \lambda P_1 + (1-\lambda) P_2, \quad \lambda \in [0,1]$$

Ví dụ:
- Hỗn hợp 50-50: điểm nằm đúng giữa $P_1$ và $P_2$
- Tỉ lệ $1/4$ của $P_1$ và $3/4$ của $P_2$: điểm cách $P_2$ một khoảng $1/4$ đoạn $P_1P_2$

Bộ ba màu cơ bản Đỏ-Xanh lá-Xanh lam tạo nên **tam giác màu** (color gamut). Mọi màu có thể tạo ra bằng tổ hợp dương của ba màu này đều nằm **bên trong tam giác**. Đây là giới hạn của màn hình RGB.

### 4. Đường cong spectral locus và vùng màu nhìn thấy được

Màu phổ thuần (pure spectral colors) là các bước sóng đơn từ ~380 nm (tím) đến ~700 nm (đỏ). Chúng tạo nên **đường cong móng ngựa** (horseshoe curve) trên sơ đồ chromaticity.

Để xác định đường cong này, người ta đo hệ số color matching $\bar{r}(\lambda)$, $\bar{g}(\lambda)$, $\bar{b}(\lambda)$ — lượng ba màu cơ bản cần để tái tạo mỗi bước sóng đơn $\lambda$. Chú ý: một số giá trị âm (người ta phải cộng màu vào phía màu cần đo, không phải vào hỗn hợp). Rồi chuẩn hóa để ra $(x(\lambda), y(\lambda))$.

Mọi ánh sáng thực tế $A$ đều là tổng dương của các màu phổ:

$$A = \int_0^\infty I(\lambda) d\lambda$$

Do đó điểm biểu diễn màu $A$ trên sơ đồ luôn nằm **trong hoặc trên đường cong**. Đường thẳng nối hai đầu đường cong (tím–đỏ) là locus của các màu **purple**, không tồn tại trong phổ nhìn thấy nhưng có thể tạo ra bằng cách trộn ánh sáng.

### 5. Ứng dụng trong kỹ thuật cơ điện tử và đo lường chính xác

**Ứng dụng 1: Cảm biến màu sắc (color sensor) trong hệ thống vision machine**

Trong dây chuyền kiểm tra chất lượng (quality control) bằng machine vision, cảm biến màu như TCS3200 hay AS7341 đo năng lượng ánh sáng tại nhiều kênh phổ. Để phân loại màu sắc chính xác, hệ thống cần:

1. Đo các giá trị $R_{raw}$, $G_{raw}$, $B_{raw}$ từ cảm biến
2. Tính tọa độ chromaticity: $x = R/(R+G+B)$, $y = G/(R+G+B)$
3. So sánh với database màu chuẩn (reference gamut)

Việc dùng tọa độ chromaticity thay vì RGB tuyệt đối loại bỏ ảnh hưởng của điều kiện chiếu sáng (illumination normalization) — rất quan trọng khi ánh sáng môi trường thay đổi trong nhà máy.

**Ứng dụng 2: Hệ thống nhắm mục tiêu quân sự (military targeting) với đầu tìm nhiệt-quang**

Đầu tìm kép (dual-mode seeker) kết hợp IR thermal và visible camera cần fusion màu sắc. Sơ đồ chromaticity giúp đặc trưng hóa "signature" màu của mục tiêu độc lập với cường độ ánh sáng mặt trời, giảm false alarm.

### 6. Bài tập mẫu

**Đề bài:** Hai màu có tọa độ chromaticity $P_1 = (0.64, 0.33)$ (đỏ sRGB) và $P_2 = (0.30, 0.60)$ (xanh lá sRGB). Tính tọa độ màu hỗn hợp với tỉ lệ đỏ:xanh lá = 1:3.

**Giải:**

Bước 1: Xác định $\lambda$. Tỉ lệ 1:3 nghĩa là $1/4$ đỏ và $3/4$ xanh lá, nên $\lambda = 1/4$ (trọng số cho $P_1$):

$$P_{mix} = \frac{1}{4} P_1 + \frac{3}{4} P_2$$

Bước 2: Tính $x_{mix}$:

$$x_{mix} = \frac{1}{4} \times 0.64 + \frac{3}{4} \times 0.30 = 0.16 + 0.225 = 0.385$$

Bước 3: Tính $y_{mix}$:

$$y_{mix} = \frac{1}{4} \times 0.33 + \frac{3}{4} \times 0.60 = 0.0825 + 0.45 = 0.5325$$

**Kết quả:** $P_{mix} = (0.385, 0.533)$ — một màu xanh lá ngả xanh dương, nằm gần $P_2$ hơn (đúng vì tỉ lệ xanh lá chiếm 3/4).

Ý nghĩa vật lý: Điểm này nằm trên đoạn thẳng $P_1P_2$, cách $P_1$ một khoảng $3/4$ đoạn — xác nhận tính chất tuyến tính của phép trộn màu ánh sáng.

### 7. Giới hạn của mô hình tuyến tính

Mô hình chromaticity chỉ đúng với **ánh sáng phát xạ** (emissive light). Với **màu hấp thụ** (như mực in, sơn), việc trộn màu không tuyến tính — cần mô hình Kubelka-Munk. Đây là lý do màu in CMYK hoạt động theo nguyên tắc khác RGB màn hình.

Trong đo lường chính xác, độ phân giải của cảm biến màu bị giới hạn bởi noise photon — ảnh hưởng đến vị trí điểm trên sơ đồ chromaticity. Để đạt độ chính xác micrometer trong camera-based metrology, cần hiệu chỉnh sắc sai (chromatic aberration) của quang học, vì các bước sóng khác nhau có tiêu điểm khác nhau.

### Tóm tắt

Sơ đồ chromaticity là công cụ toán học mạnh mẽ để phân tích màu sắc: mỗi màu là một điểm, trộn màu là nội suy tuyến tính, và tất cả màu nhìn thấy được nằm trong đường cong spectral locus. Đây là nền tảng của tiêu chuẩn màu sắc quốc tế CIE và mọi thiết bị hiển thị, đo lường màu hiện đại.

---
*Exported from Feynman Bot*
