---
lesson_id: 5600
lesson_type: deep_dive
approval_status: pending
exported_at: "2026-03-03T15:33:08.883079+00:00"
content_hash: 9a5f527e3b09
chapter_number: 35
chapter_title: Chapter 35
section_number: 7
section_title: 35–6Physiochemistry of color vision
---
# ## Sắc Tố Thị Giác và Kỹ Thuật Đo Quang Phổ In Vivo — Phân tích Chuyên sâu

*Source: Chapter 35 - Chapter 35 (Section 7) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_35.html)*

## Sắc Tố Thị Giác và Kỹ Thuật Đo Quang Phổ In Vivo — Phân tích Chuyên sâu

### 1. Bối cảnh: Bài toán đo lường sắc tố cực nhỏ

Mắt người có khoảng 120 triệu tế bào que (rods) và 6 triệu tế bào nón (cones). Mỗi tế bào nón chứa một lượng cực nhỏ sắc tố màu — ước tính nồng độ chỉ đủ để quan sát được nếu được cô đặc từ hàng triệu mắt. Đây là thách thức đo lường tương tự như việc phát hiện tạp chất ở mức ppm trong vật liệu nano hay đo dịch chuyển ở mức picometer trong giao thoa kế laser.

Rushton (1958) giải quyết bằng cách **không chiết xuất** sắc tố mà đo **in vivo** — ngay bên trong mắt sống — dùng nguyên lý quang phổ phản xạ vi sai.

### 2. Sắc tố tế bào que: Visual Purple (Rhodopsin)

#### 2.1 Cấu trúc phân tử

Rhodopsin gồm protein opsin kết hợp với chromophore **11-cis-retinal** (dẫn xuất vitamin A). Khi hấp thụ photon:

$$\text{11-cis-retinal} \xrightarrow{h\nu} \text{all-trans-retinal}$$

Sự thay đổi cấu hình hình học này kích hoạt chuỗi phản ứng hóa học dẫn đến tín hiệu thần kinh — **quang dẫn điện sinh học**. Đây là ví dụ đẹp nhất của **transducer** (bộ chuyển đổi) tự nhiên: chuyển photon đơn lẻ thành xung điện thần kinh, với hiệu suất năng lượng cực cao.

#### 2.2 Khớp giữa phổ hấp thụ và độ nhạy mắt

Năm 1877, Boll phát hiện visual purple. Năm 1894, König đo đường cong nhạy sáng của mắt dark-adapted và so sánh với phổ hấp thụ của visual purple — chúng khớp chính xác (Fig. 35-9 trong Feynman). Về mặt toán học:

$$V(\lambda) \propto \epsilon_{\text{rho}}(\lambda)$$

trong đó $V(\lambda)$ là luminous efficiency function (photopic/scotopic) và $\epsilon_{\text{rho}}(\lambda)$ là hệ số hấp thụ molar của rhodopsin. Điều này có nghĩa: **mắt tối thích nghi nhạy nhất ở các bước sóng mà rhodopsin hấp thụ mạnh nhất** (~498 nm, xanh lam-lục).

#### 2.3 Phương trình Beer-Lambert cho hấp thụ ánh sáng

Ánh sáng truyền qua lớp sắc tố dày $d$ với nồng độ $c$ tuân theo định luật Beer-Lambert:

$$I(\lambda) = I_0(\lambda) \cdot e^{-\epsilon(\lambda) c d}$$

Trong kỹ thuật Rushton, ánh sáng đi **hai lần** qua lớp sắc tố (chiều vào và chiều ra sau phản xạ), nên:

$$R(\lambda) = \frac{I_{reflected}(\lambda)}{I_0(\lambda)} = e^{-2\epsilon(\lambda) c d}$$

Lấy logarithm: $-\ln R(\lambda) = 2\epsilon(\lambda) cd$. Đây chính là **optical density** đo được, tỉ lệ thuận với nồng độ sắc tố.

### 3. Kỹ thuật đo Rushton: Phân tích từng bước

#### Bước 1: Thiết lập đo phản xạ (reflectometry)

Dùng ophthalmoscope để:
- Chiếu chùm ánh sáng đã biết phổ $I_0(\lambda)$ vào fovea (nơi không có tế bào que, chỉ có tế bào nón)
- Thu ánh sáng phản xạ $I_r(\lambda)$ đi ra
- Tính $R(\lambda) = I_r(\lambda)/I_0(\lambda)$

#### Bước 2: Chọn đối tượng đặc biệt — người mù màu protanope

Protanope thiếu sắc tố đỏ (erythrolabe). Điều này đơn giản hóa phân tích vì mắt chỉ có **một** sắc tố màu chưa biết thay vì hai.

#### Bước 3: Tẩy trắng chọn lọc (selective bleaching)

Chiếu ánh sáng cường độ cao vào mắt để **bleach** (tẩy trắng) sắc tố — phá vỡ liên kết 11-cis-retinal, làm sắc tố mất màu. Đo lại $R'(\lambda)$ sau khi bleach.

#### Bước 4: Tính phổ vi sai

$$\Delta A(\lambda) = -\ln R'(\lambda) - (-\ln R(\lambda)) = -\ln\frac{R'(\lambda)}{R(\lambda)}$$

$\Delta A(\lambda)$ chỉ phản ánh **sự thay đổi của sắc tố** — không bị ảnh hưởng bởi màu máu, mô nền, hay các hấp thụ không đổi khác. Đây là **common-mode rejection** trong quang học, tương tự như trong khuếch đại vi sai điện tử.

#### Bước 5: Đối với mắt bình thường

Với mắt bình thường, bleach bằng ánh sáng đỏ (>620 nm) — chỉ ảnh hưởng sắc tố đỏ (erythrolabe), không ảnh hưởng sắc tố xanh lá (chlorolabe). Sau khi trừ contribution của erythrolabe (đã biết từ bước trên), thu được phổ của chlorolabe.

### 4. Kết quả thực nghiệm

| Sắc tố | Đỉnh hấp thụ $\lambda_{max}$ | Tế bào nón |
|--------|------|------|
| Cyanolabe (S-cone) | ~420 nm | Xanh lam |
| Chlorolabe (M-cone) | ~530 nm | Xanh lá |
| Erythrolabe (L-cone) | ~560 nm | Đỏ |

Phổ của chlorolabe khớp tốt với đường cong màu xanh lá của Yustova (1955), nhưng erythrolabe lệch một chút về phía xanh lá so với dự đoán từ dữ liệu psychophysical — cho thấy mô hình 3 thụ thể (trichromatic theory) vẫn cần tinh chỉnh.

### 5. Ứng dụng trong cơ điện tử và đo lường chính xác

**Ứng dụng 1: Quang phổ kế phản xạ (reflectance spectrophotometer) cho kiểm tra bề mặt**

Nguyên lý Rushton là nền tảng của quang phổ kế phản xạ dùng trong:
- Kiểm tra độ dày lớp phủ (coating thickness) bằng phổ phản xạ: $d = -\frac{\ln R}{2\epsilon c}$
- Đo độ dày màng SiO₂ trên wafer silicon trong sản xuất bán dẫn (bề dày nm đến μm)
- Kiểm tra chất lượng bề mặt linh kiện quân sự (anti-reflection coating trên optic)

**Ứng dụng 2: Differential measurement trong cảm biến MEMS**

Kỹ thuật vi sai (differential) của Rushton — đo sự thay đổi trước/sau kích thích — là nguyên lý cơ bản của cảm biến vi sai:

$$\Delta V_{out} = V_{out,after} - V_{out,before} \propto \Delta\text{(physical quantity)}$$

Trong gia tốc kế MEMS vi sai, hai tụ điện đo biến thiên điện dung $\Delta C = C_1 - C_2$, loại bỏ offset chung và nhiễu nhiệt độ. Độ phân giải đạt sub-μg (micro-g).

**Ứng dụng 3: Hệ thống night vision và IR imaging**

Rhodopsin với peak ~498 nm giải thích tại sao tầm nhìn ban đêm của người tốt nhất trong vùng xanh lam-lục, không phải đỏ. Trong thiết kế đèn đỏ cho phòng tối hải quân (dark-adapted navigation): ánh sáng đỏ (~650 nm) không bleach rhodopsin, duy trì dark adaptation cho quan sát.

### 6. Bài tập mẫu

**Đề bài:** Một lớp sắc tố mắt có hệ số hấp thụ molar $\epsilon = 40,000$ L/(mol·cm) tại $\lambda = 500$ nm, nồng độ $c = 10^{-5}$ mol/L, bề dày $d = 2\,\mu\text{m} = 2 \times 10^{-4}$ cm. Tính hệ số phản xạ $R$ mà kỹ thuật Rushton đo được.

**Giải:**

Bước 1: Tính optical density $A$ cho một lần đi qua:

$$A = \epsilon c d = 40000 \times 10^{-5} \times 2 \times 10^{-4} = 8 \times 10^{-5}$$

Ý nghĩa: Sắc tố rất loãng, hấp thụ rất yếu mỗi lần đi qua.

Bước 2: Ánh sáng đi **hai lần** qua (phản xạ kép):

$$R = e^{-2A} = e^{-2 \times 8 \times 10^{-5}} = e^{-1.6 \times 10^{-4}} \approx 1 - 1.6 \times 10^{-4}$$

Bước 3: Sự thay đổi $\Delta R$ khi sắc tố bị bleach hoàn toàn ($c \to 0$):

$$\Delta R = R_{bleached} - R_{pigmented} \approx 1.6 \times 10^{-4}$$

Đây là tín hiệu chỉ khoảng 0.016% — đòi hỏi detector quang cực nhạy và kỹ thuật lock-in amplification để đo được. Đây là lý do tại sao kỹ thuật này khó thực hiện và Rushton phải dùng người mù màu (ít sắc tố phức tạp hơn) làm điểm khởi đầu.

### 7. Giới hạn và câu hỏi mở

Với người mù màu deuteranope (thiếu M-cone), thực nghiệm mới nhất không tìm thấy bằng chứng rõ ràng về sắc tố bị thiếu — có thể họ có đủ 3 sắc tố nhưng với nồng độ khác, hoặc sự khác biệt nằm ở mức xử lý thần kinh chứ không phải sắc tố. Điều này gợi ý: **thị giác màu sắc không chỉ là vấn đề hóa học sắc tố** mà còn là vấn đề xử lý thông tin thần kinh.

---
*Exported from Feynman Bot*
