---
lesson_id: 5603
lesson_type: deep_dive
approval_status: pending
exported_at: "2026-03-03T15:33:08.930476+00:00"
content_hash: 72417866eadb
chapter_number: 36
chapter_title: Chapter 36
section_number: 1
section_title: 36Mechanisms of Seeing
---
# ## Xử Lý Thông Tin Thị Giác — Từ Võng Mạc Đến Nhận Thức — Phân tích Chuyên sâu

*Source: Chapter 36 - Chapter 36 (Section 1) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_36.html)*

## Xử Lý Thông Tin Thị Giác — Từ Võng Mạc Đến Nhận Thức — Phân tích Chuyên sâu

### 1. Võng mạc: Bộ xử lý tiền tuyến của não

Võng mạc không phải là lớp cảm quang thụ động như film ảnh — nó là **phần mở rộng của não bộ**, gồm ba lớp tế bào thần kinh xử lý thông tin trước khi truyền đến não:

- **Lớp 1 (Photoreceptors):** Tế bào que (rods) và nón (cones) — chuyển đổi photon thành tín hiệu điện hóa
- **Lớp 2 (Bipolar cells):** Tập hợp tín hiệu từ nhiều tế bào quang, tính trung bình hoặc lấy vi phân không gian
- **Lớp 3 (Ganglion cells):** Kết hợp tín hiệu từ nhiều bipolar cells, tạo ra **các xung thần kinh** truyền dọc dây thần kinh thị giác (optic nerve)

**Kết nối ngang (lateral connections):** Tế bào ngang (horizontal cells) và amacrine cells kết nối các tế bào trong cùng lớp với nhau — tạo ra sự ức chế bên (lateral inhibition), cơ chế phát hiện cạnh (edge detection) ngay trong võng mạc.

### 2. Lateral Inhibition — Edge Detection sinh học

Lateral inhibition là hiện tượng: tế bào thần kinh bị kích thích sẽ ức chế các tế bào lân cận. Cơ chế này tạo ra hiệu ứng tăng cường tương phản tại ranh giới sáng-tối.

Mô hình toán học đơn giản (Mach bands): Nếu tế bào $i$ nhận ánh sáng $I_i$, đầu ra của nó sau lateral inhibition là:

$$O_i = I_i - k \sum_{j \neq i} O_j \cdot w(|i-j|)$$

trong đó $k$ là hệ số ức chế và $w(d)$ là hàm trọng số giảm theo khoảng cách $d$. Giải phương trình này cho thấy: ở ranh giới sáng-tối, vùng sáng gần ranh giới trông **sáng hơn** bình thường, vùng tối gần ranh giới trông **tối hơn** — tạo ra sọc Mach (Mach bands) quan sát được.

**Ứng dụng trong kỹ thuật:** Toán tử Laplacian-of-Gaussian (LoG) trong xử lý ảnh chính xác là mô hình toán học của lateral inhibition:

$$\nabla^2 G(\sigma) = \frac{\partial^2 G}{\partial x^2} + \frac{\partial^2 G}{\partial y^2}$$

Đây là bộ lọc phát hiện cạnh dùng trong machine vision — mô phỏng chính xác những gì võng mạc làm sinh học.

### 3. Color Constancy — Bài toán tương đương hệ phương trình thiếu ràng buộc

Bài toán color constancy được phát biểu toán học: ánh sáng nhận tại điểm $(x,y)$ là:

$$I(x,y,\lambda) = E(\lambda) \cdot S(x,y,\lambda)$$

trong đó $E(\lambda)$ là phổ chiếu sáng (illuminant) và $S(x,y,\lambda)$ là phổ phản xạ bề mặt (surface reflectance). Hệ thống thị giác chỉ đo được $I$ nhưng cần xác định $S$ (màu "thực" của vật) — bài toán này **underdetermined** (thiếu ràng buộc) về mặt toán học.

Não giải quyết bằng cách thêm các **prior assumptions (tiên đề):**
- Grey World Assumption: Trung bình màu của cả cảnh là xám → $E(\lambda) = \text{const}$
- Max RGB: Pixel sáng nhất là trắng → $E(\lambda) = \max I(x,y,\lambda)$
- Retinex (Land): Tỉ số màu tại các vùng kề nhau loại bỏ $E(\lambda)$

Land's Retinex Algorithm (1977): Xét hai điểm kề nhau $A$ và $B$:

$$\frac{I_A(\lambda)}{I_B(\lambda)} = \frac{E(\lambda)S_A(\lambda)}{E(\lambda)S_B(\lambda)} = \frac{S_A(\lambda)}{S_B(\lambda)}$$

Tỉ số loại bỏ hoàn toàn $E(\lambda)$! Não tích lũy các tỉ số dọc theo đường nối nhiều điểm, cuối cùng ước tính được $S(x,y,\lambda)$ cho toàn cảnh — đó là "màu thực" của vật.

### 4. Thí nghiệm "bóng xanh" của Land — Phân tích định lượng

**Thiết lập:** Chiếu ánh sáng trắng ($W$) và ánh sáng đỏ ($R$, ~620 nm) lên màn trắng:
- Vùng A: Chỉ có $W$ → ánh sáng đến mắt là trắng thuần túy
- Vùng B: Có cả $W$ và $R$ → ánh sáng đến mắt là hồng $(W + R)$

Mắt nhìn thấy: Vùng A trông **xanh lam** dù nó phát ra ánh sáng trắng!

**Giải thích Retinex:** Tỉ số thành phần đỏ: $R_A/R_B = W_{red}/(W_{red}+R) < 1$. Não suy luận: "Vùng A có ít đỏ hơn bối cảnh → đây là bề mặt có phản xạ xanh lam."

**Định lượng:** Nếu $W = (W_R, W_G, W_B)$ và đèn đỏ thêm $\Delta R$ vào kênh đỏ:
$$\text{Vùng B: } (W_R + \Delta R, W_G, W_B)$$
$$\text{Tỉ số đỏ: } \frac{W_R}{W_R + \Delta R} < 1 \Rightarrow \text{Vùng A "thiếu đỏ" } \Rightarrow \text{trông xanh lam}$$

### 5. Đĩa Benham — Tín hiệu thời gian và màu sắc

Đĩa Benham xoay với tần số $f$ rad/s. Tại bán kính $r$, chuỗi thời gian ánh sáng đến mắt là:

$$I(t) = I_0[1 + m(r) \cdot \text{pattern}(\omega t)]$$

trong đó $m(r)$ là modulation depth phụ thuộc bán kính và pattern là hàm tuần hoàn của vị trí góc. Tần số kích thích $f$ khác nhau tại các bán kính khác nhau → kích thích ưu tiên các kênh màu khác nhau (kênh L, M, S-cone có temporal response khác nhau). Đây là nguyên lý **temporal chromatic aberration** của hệ thần kinh.

### 6. Ứng dụng cho hệ thống cơ điện tử và vũ khí

**Ứng dụng 1: Image stabilization trong hệ thống ngắm quân sự**

Dây thần kinh thị giác truyền không chỉ thông tin về "ảnh" mà còn thông tin điều khiển phản xạ: một phần xung thần kinh từ mắt đi thẳng vào **midbrain** (não giữa) để điều khiển cơ mắt (eye muscles) và iris — không qua vỏ não thị giác. Đây là vòng điều khiển phản xạ tốc độ cao (~50 ms latency).

Hệ thống ngắm bắn (sight stabilization) của súng bắn tỉa hoặc xe tăng hoạt động theo nguyên lý tương tự: Gyroscope đo chuyển động thân xe → Actuator quay ngược gương ngắm → Ảnh giữ nguyên. Vòng điều khiển này phải có latency < 5 ms để hiệu quả — tốt hơn phản xạ mắt người.

**Ứng dụng 2: Adaptive optics dựa trên cơ chế accommodation**

Khi mắt điều tiết (accommodation), cơ thể mi (ciliary muscle) thay đổi độ cong của thủy tinh thể. Tín hiệu điều khiển đến từ midbrain — khi ảnh mờ, não gửi lệnh "tăng/giảm độ cong". Hệ thống adaptive optics trong kính thiên văn và camera y tế mô phỏng cơ chế này:
- Wavefront sensor (Shack-Hartmann) đo độ mờ của wavefront — tương tự phát hiện "ảnh mờ"
- Deformable mirror điều chỉnh hình dạng — tương tự cơ thể mi
- Vòng điều khiển PID khép kín — tương tự vòng phản xạ midbrain

**Ứng dụng 3: Edge detection trong hệ thống nhận dạng mục tiêu**

Lateral inhibition của võng mạc là cơ sở của bộ lọc Sobel, Canny trong OpenCV dùng cho nhận dạng mục tiêu:

```
Sobel_x = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
Sobel_y = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
Edge = sqrt(Sobel_x^2 + Sobel_y^2)
```

Trong hệ thống nhận dạng mục tiêu tự động (ATRS — Automatic Target Recognition System), edge detection là bước đầu tiên trước khi nhận dạng hình dạng và phân loại mục tiêu.

### 7. Bài tập mẫu

**Đề bài:** Camera trong hệ thống QC của bạn đặt dưới ánh đèn LED trắng lạnh (5500K) và ánh sáng mặt trời lọt qua cửa sổ (6500K). Cảm biến đo RGB của linh kiện màu xanh lá chuẩn: $(R, G, B) = (40, 120, 30)$ dưới đèn LED; $(R, G, B) = (35, 110, 28)$ dưới ánh mặt trời. Dùng Grey World Assumption để hiệu chỉnh màu và kiểm tra xem hai mẫu có cùng màu không.

**Giải:**

Bước 1: Tính trung bình màu của ảnh tham chiếu (trắng) dưới mỗi điều kiện:
- LED: Giả sử đo tấm trắng chuẩn: $(R_w, G_w, B_w) = (200, 210, 190)$
- Mặt trời: $(R_w, G_w, B_w) = (180, 195, 210)$

Bước 2: Tính gain hiệu chỉnh (để trắng → (200, 200, 200)):
- LED: $k_R = 200/200 = 1.0$, $k_G = 200/210 = 0.952$, $k_B = 200/190 = 1.053$
- Mặt trời: $k_R = 200/180 = 1.111$, $k_G = 200/195 = 1.026$, $k_B = 200/210 = 0.952$

Bước 3: Áp dụng hiệu chỉnh cho mẫu linh kiện:
- LED: $(40 \times 1.0, 120 \times 0.952, 30 \times 1.053) = (40, 114, 31.6)$
- Mặt trời: $(35 \times 1.111, 110 \times 1.026, 28 \times 0.952) = (38.9, 112.9, 26.7)$

Bước 4: Tính chromaticity sau hiệu chỉnh:
- LED: $x = 40/185.6 = 0.216$, $y = 114/185.6 = 0.614$
- Mặt trời: $x = 38.9/178.5 = 0.218$, $y = 112.9/178.5 = 0.633$

Hai giá trị gần nhau (sai lệch < 3%) → xác nhận cùng màu, sự khác biệt ban đầu do điều kiện chiếu sáng khác nhau.

**Ý nghĩa vật lý:** Não bộ thực hiện thao tác tương đương này tự động và tức thì — đó là lý do bạn thấy cùng màu xanh lá dù ánh sáng thay đổi.

---
*Exported from Feynman Bot*
