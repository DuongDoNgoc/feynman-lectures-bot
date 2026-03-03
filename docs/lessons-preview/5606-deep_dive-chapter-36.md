---
lesson_id: 5606
lesson_type: deep_dive
approval_status: pending
exported_at: "2026-03-03T15:33:08.976691+00:00"
content_hash: 6017024f0fba
chapter_number: 36
chapter_title: Chapter 36
section_number: 3
section_title: 36–2The physiology of the eye
---
# ## Cấu Trúc Võng Mạc và Quang Học Mắt Người — Phân tích Chuyên sâu

*Source: Chapter 36 - Chapter 36 (Section 3) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_36.html)*

## Cấu Trúc Võng Mạc và Quang Học Mắt Người — Phân tích Chuyên sâu

### 1. Kiến trúc mạng thần kinh võng mạc

Võng mạc là mô thần kinh duy nhất có thể quan sát trực tiếp (không xâm lấn) trong cơ thể — điều này làm nó trở thành cửa sổ để nghiên cứu não bộ. Cấu trúc của nó gồm:

#### 1.1 Photoreceptors — Transducer quang-điện sinh học

**Tế bào que (Rods):**
- Phân bố: Ngoại vi võng mạc, mật độ ~150,000/mm²
- Sắc tố: Rhodopsin (peak ~498 nm)
- Ngưỡng: Nhạy đến photon đơn lẻ
- Không phân biệt màu (achromatic)
- **Receptive field:** Hàng trăm tế bào que hội tụ vào 1 ganglion cell → tích hợp không gian → nhạy, nhưng phân giải kém

**Tế bào nón (Cones):**
- Phân bố: Tập trung ở fovea centralis (1.5 mm đường kính)
- Fovea: Mật độ nón ~150,000/mm², gần như 1:1 với ganglion cells → phân giải cao nhất
- Ba loại: S-cone (~420 nm), M-cone (~530 nm), L-cone (~560 nm)
- Tỉ lệ: L:M:S ≈ 40:20:1 trong fovea

#### 1.2 Bipolar cells — Bộ phân loại ON/OFF

Có hai loại bipolar cells quan trọng:

**ON-center bipolar cells:** Hoạt hóa khi có ánh sáng ở tâm receptive field và bóng tối ở rìa. Phát hiện "điểm sáng trên nền tối".

**OFF-center bipolar cells:** Hoạt hóa khi có bóng tối ở tâm và ánh sáng ở rìa. Phát hiện "điểm tối trên nền sáng".

Cơ chế này tương đương hai bộ lọc đối lập song song — tương tự cặp cảm biến vi sai trong cảm biến áp suất, cho phép phát hiện cả biến thiên dương lẫn âm của kích thích.

#### 1.3 Ganglion cells — Bộ tạo xung thần kinh và nén tín hiệu

Ganglion cells tích hợp đầu ra của nhiều bipolar cells và tạo **action potentials** (xung điện, ~70 mV, ~1 ms). Đây là dạng tín hiệu số (digital pulse train) trong hệ thần kinh — tần suất xung mã hóa cường độ kích thích.

**Tỉ lệ nén tín hiệu:**

$$\text{Compression ratio} = \frac{\text{Photoreceptors}}{\text{Ganglion cells}} = \frac{126 \times 10^6}{1.2 \times 10^6} \approx 105:1$$

Nén này đạt được mà **không mất thông tin quan trọng** nhờ: tế bào nón fovea có tỉ lệ 1:1 (không nén); tế bào que ngoại vi nén mạnh (tập trung vào phát hiện chuyển động).

### 2. Quang học của mắt — Phân tích định lượng

#### 2.1 Phương trình thấu kính mỏng và sức hội tụ

Sức hội tụ (power) của mắt tính bằng diopter (D = 1/f, f tính bằng mét):

$$P_{total} = P_{cornea} + P_{lens} - \frac{d}{n_{aqueous}} P_{cornea} P_{lens}$$

trong đó $d$ là khoảng cách giữa giác mạc và thủy tinh thể, $n_{aqueous} \approx 1.336$ là chỉ số thủy dịch (aqueous humor). Thông thường:
- $P_{cornea} \approx 43$ D (cố định)
- $P_{lens} \approx 17$–$25$ D (thay đổi khi điều tiết)
- $P_{total} \approx 60$ D (nhìn xa) đến $70$ D (nhìn gần)

#### 2.2 Khúc xạ tại giác mạc

Định luật Snell tại bề mặt cong giác mạc:

$$n_1 \sin\theta_1 = n_2 \sin\theta_2$$

với $n_1 = 1.0$ (không khí), $n_2 = 1.376$ (giác mạc). Với tia nhỏ (paraxial approximation):

$$P_{cornea} = \frac{n_2 - n_1}{R} = \frac{1.376 - 1.0}{R}$$

với $R \approx 7.8$ mm (bán kính cong giác mạc trung bình). Suy ra: $P_{cornea} \approx 0.376/0.0078 \approx 48$ D.

Dưới nước ($n_1 = 1.33$): $P_{cornea} = (1.376 - 1.33)/0.0078 \approx 5.9$ D — giảm 8 lần! Giải thích tại sao mắt người không lấy nét được dưới nước.

#### 2.3 Gradient Index (GRIN) của thủy tinh thể

Thủy tinh thể có chỉ số khúc xạ biến đổi:

$$n(r) = n_0 - \frac{n_0 - n_s}{2}\left(\frac{r}{a}\right)^2 + \text{higher order terms}$$

với $n_0 = 1.40$ (tâm), $n_s = 1.38$ (rìa), $a$ bán kính. Sức hội tụ hiệu dụng của thấu kính GRIN lớn hơn thấu kính đồng nhất cùng hình dạng:

$$P_{GRIN} = P_{surface} + P_{gradient}$$

trong đó $P_{gradient}$ là đóng góp từ gradient chỉ số — thường tương đương $P_{surface}$, nghĩa là GRIN cho sức hội tụ gấp đôi so với thấu kính đồng nhất cùng kích thước.

#### 2.4 Quang sai cầu của mắt và giác mạc phi cầu

Với thấu kính cầu, tia rìa hội tụ gần hơn tia tâm — quang sai cầu (spherical aberration) dương. Giác mạc hình prolate ellipsoid khắc phục điều này:

$$Q_{cornea} \approx -0.26 \quad \Rightarrow \quad \text{Quang sai cầu giảm}$$

Tuy nhiên thủy tinh thể có quang sai cầu âm (vì GRIN), bổ sung và triệt tiêu một phần quang sai của giác mạc. Kết quả: mắt trẻ khỏe mạnh có tổng quang sai cầu gần bằng không!

**Hệ quả cho kỹ sư quang học:** Khi thiết kế thấu kính cho camera machine vision, phải dùng thấu kính aspherical (phi cầu) hoặc kết hợp nhiều thấu kính để triệt quang sai — chính xác là điều mắt người làm tự nhiên.

### 3. Hệ điều khiển thần kinh — Phân tích vòng điều khiển

#### 3.1 Pupillary Light Reflex (PLR) — Điều chỉnh iris

**Cung phản xạ:**
Ánh sáng → Retinal ganglion cells (ipRGCs, chứa melanopsin) → Pretectal nucleus (midbrain) → Edinger-Westphal nucleus → Ciliary ganglion → Cơ vòng đồng tử

**Đặc trưng điều khiển:**
- Latency: ~200 ms (một trong các phản xạ chậm nhất của hệ thần kinh)
- Dải điều chỉnh: Đường kính đồng tử từ 2 mm (sáng) đến 8 mm (tối) → diện tích thay đổi 16 lần → lượng ánh sáng thay đổi 16 lần (~1.2 log units)
- So sánh: mắt nhạy sáng trong dải 11 log units → đồng tử chỉ bù được ~10% → phần lớn là do adaptation của photoreceptors

**Mô hình điều khiển (transfer function):**

$$H(s) = \frac{K e^{-\tau s}}{T s + 1}$$

với $K$ là hệ số khuếch đại, $\tau \approx 200$ ms là thời gian trễ (dead time), $T \approx 500$ ms là hằng số thời gian. Đây là hệ bậc nhất với pure delay — phổ biến trong nhiều hệ sinh học.

#### 3.2 Accommodation Reflex — Điều tiết thủy tinh thể

**Cơ thể mi (ciliary muscle):** Khi co → vòng dây chằng Zinn nới lỏng → thủy tinh thể phồng → độ cong tăng → sức hội tụ tăng (nhìn gần).

**Tín hiệu điều khiển:** Khi ảnh mờ (blur), não giữa (midbrain) so sánh ảnh từ hai mắt và từ các vùng võng mạc khác nhau để phán đoán hướng điều chỉnh (tăng hay giảm sức hội tụ).

**Đặc trưng điều khiển:**
- Dải điều tiết: Từ 17D (nhìn xa) đến 25D (nhìn gần 10 cm) — khoảng 8D
- Latency: ~300–500 ms
- Mất dần sau 40 tuổi (presbyopia): thủy tinh thể cứng hơn, giảm khả năng thay đổi hình dạng

### 4. Ứng dụng cho cơ điện tử và đo lường chính xác

**Ứng dụng 1: Thiết kế thấu kính cho camera đo lường độ chính xác cao**

Trong hệ thống đo lường quang học micrometer, thấu kính phải có:
- Quang sai cầu tối thiểu: Dùng thấu kính aspherical hoặc achromat doublet
- Quang sai màu tối thiểu: Vì mắt dùng GRIN để bù quang sai màu, camera cần apochromat triplet
- MTF (Modulation Transfer Function) cao: Độ phân giải tốt ở toàn bộ trường nhìn

**Đặc trưng quan trọng:** Tại bước sóng laser (ví dụ HeNe, 632.8 nm), không có vấn đề quang sai màu. Nhưng nếu dùng đèn LED trắng, quang sai màu ảnh hưởng đến độ chính xác đo chiều sâu — tương tự ảnh hưởng của quang sai màu mắt khi nhìn vật thể nhiều màu.

**Ứng dụng 2: Autofocus cho hệ thống đo tọa độ quang học**

Mô phỏng accommodation reflex trong autofocus máy ảnh:

**Phase Detection AF (PDAF):**
- Hai cặp pixel đặc biệt đặt ở các vị trí khác nhau trong sensor
- Nếu ảnh nét: hai điểm ảnh từ hai hướng trùng nhau → phase difference = 0
- Nếu ảnh mờ: phase difference $\neq 0$, và **dấu** của nó chỉ hướng cần di chuyển thấu kính

$$\Delta_{focus} = k \cdot \phi_{phase}$$

Đây chính xác là cơ chế mắt người dùng: so sánh ảnh từ hai vùng võng mạc để xác định hướng điều tiết.

**Ứng dụng 3: Iris control trong hệ thống chiếu sáng tự động**

Trong máy đo tọa độ quang học (optical CMM) hoặc kính hiển vi đo lường, nguồn sáng phải ổn định chính xác. Vòng điều khiển iris của mắt người là inspiration cho:

- **Auto-iris lens:** Điều chỉnh khẩu độ (aperture) tự động theo cường độ ánh sáng
- **Transfer function:** Tương tự PLR của mắt — bậc nhất với dead time
- **PID tuning:** $K_P$ không được quá lớn để tránh dao động (mắt cũng có hiện tượng hippus — dao động nhỏ của đồng tử do loop gain hơi cao)

### 5. Bài tập mẫu

**Đề bài:** Một camera đo lường dùng thấu kính có tiêu cự $f = 50$ mm, chỉ số khúc xạ đồng nhất $n = 1.5$, bán kính cong $R_1 = R_2 = 51.5$ mm (thấu kính lồi hai mặt). Tính:
(a) Sức hội tụ của thấu kính
(b) Quang sai cầu bậc 3 (Seidel) có dạng $\delta f = \alpha (D/2)^2$ với $\alpha = 0.01$ mm⁻¹, $D = 10$ mm. Tính $\delta f$ và so sánh với DOF (Depth of Field) $= 2\lambda(f/D)^2$ với $\lambda = 0.5\,\mu\text{m}$.

**Giải:**

**(a) Sức hội tụ:**

Dùng công thức lensmaker's equation:

$$P = (n-1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right) = (1.5-1)\left(\frac{1}{51.5} - \frac{1}{-51.5}\right) = 0.5 \times \frac{2}{51.5}$$

$$P = \frac{1}{51.5} \approx 19.4 \text{ D}, \quad f = \frac{1}{P} \approx 51.5 \text{ mm}$$

(Gần đúng $f \approx 50$ mm theo thiết kế, sai lệch do công thức đơn giản hóa.)

**(b) Quang sai cầu:**

$$\delta f = \alpha \left(\frac{D}{2}\right)^2 = 0.01 \times \left(\frac{10}{2}\right)^2 = 0.01 \times 25 = 0.25 \text{ mm} = 250\,\mu\text{m}$$

DOF:

$$DOF = 2\lambda\left(\frac{f}{D}\right)^2 = 2 \times 0.0005 \times \left(\frac{50}{10}\right)^2 = 0.001 \times 25 = 0.025 \text{ mm} = 25\,\mu\text{m}$$

**Nhận xét:** $\delta f = 250\,\mu\text{m} \gg DOF = 25\,\mu\text{m}$ — quang sai cầu lớn gấp 10 lần DOF! Điều này nghĩa là thấu kính đồng nhất này **không đủ chất lượng** cho đo lường chính xác — cần dùng thấu kính aspherical (phi cầu) để giảm $\delta f$ xuống dưới $DOF/2 = 12.5\,\mu\text{m}$. Mắt người đã giải quyết vấn đề tương tự bằng giác mạc phi cầu và thủy tinh thể GRIN.

### Tóm tắt

Mắt người là hệ thống quang-thần kinh tinh vi: giác mạc phi cầu và thủy tinh thể GRIN cùng nhau triệt tiêu quang sai; ba lớp tế bào thần kinh võng mạc nén thông tin hiệu quả 100:1; vòng điều khiển phản xạ (accommodation, PLR) là hệ thống điều khiển closed-loop với đặc trưng bậc nhất có trễ. Hiểu sâu kiến trúc này không chỉ là vật lý cơ bản mà còn là kim chỉ nam thiết kế cho kỹ sư quang học và cơ điện tử.

---
*Exported from Feynman Bot*
