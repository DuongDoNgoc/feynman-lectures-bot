---
lesson_id: 5545
lesson_type: concept
approval_status: approved
exported_at: "2026-03-03T15:33:07.601275+00:00"
content_hash: a355a5d45ea1
chapter_number: 30
chapter_title: Chapter 30
section_number: 4
section_title: 30–3Resolving power of a grating
---
# ## Độ Phân Giải của Cách Tử: Tại Sao Không Thể Nhìn Thấy Vô Hạn Sắc Nét?

*Source: Chapter 30 - Chapter 30 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_30.html)*

## Độ Phân Giải của Cách Tử: Tại Sao Không Thể Nhìn Thấy Vô Hạn Sắc Nét?

### Câu hỏi mở đầu

Bạn đang kiểm tra hai laser diode có bước sóng rất gần nhau — 852.1 nm và 852.3 nm — bằng một spectrometer cách tử. Spectrometer nhìn thấy một đỉnh sáng duy nhất hay hai đỉnh riêng biệt? Câu trả lời không phụ thuộc vào chất lượng thấu kính hay độ tinh tế của cơ học — nó phụ thuộc vào **số lượng vạch của cách tử** và một nguyên lý gọi là **độ phân giải** (resolving power). Đây là ví dụ đẹp về cách giới hạn vật lý giao thoa ảnh hưởng trực tiếp đến kỹ thuật đo lường.

### Hai đỉnh hay một đỉnh?

Khi hai bước sóng $\lambda$ và $\lambda' = \lambda + \Delta\lambda$ gần nhau, vân nhiễu xạ của chúng trùng lên nhau một phần. Vấn đề: khi nào ta có thể "thấy" chúng là hai đỉnh tách biệt?

**Tiêu chuẩn Rayleigh** đưa ra câu trả lời thực dụng:

> Hai vạch phổ vừa đủ phân biệt khi **cực đại của vạch này** rơi đúng vào **cực tiểu đầu tiên** của vạch kia.

**Phép so sánh với kỹ thuật điều khiển:** Tiêu chuẩn Rayleigh giống như ngưỡng phân giải của bộ ADC (Analog-to-Digital Converter) — nếu hai tín hiệu gần nhau hơn 1 LSB (Least Significant Bit), ADC không phân biệt được. Ở đây, "LSB" của cách tử là khoảng cách bước sóng tối thiểu $\delta\lambda$ mà nó phân giải được.

### Tính $\delta\lambda$: Bước sóng tối thiểu phân giải được

Cực đại bậc $m$ của bước sóng $\lambda'$ xuất hiện tại góc $\theta$ thỏa mãn $Nd \cdot \sin\theta = mN\lambda'$ (tổng đường đi của $N$ vạch).

Cực tiểu đầu tiên của $\lambda$ xuất hiện khi tổng đường đi lệch đúng $\lambda$ so với cực đại: $Nd\sin\theta = mN\lambda + \lambda$.

Đặt hai điều kiện bằng nhau theo tiêu chuẩn Rayleigh:
$$mN\lambda' = mN\lambda + \lambda$$
$$mN(\lambda' - \lambda) = \lambda$$
$$\Delta\lambda = \frac{\lambda}{mN}$$

Suy ra **khả năng phân giải** (resolving power):

$$R = \frac{\lambda}{\Delta\lambda} = mN$$

**Đây là kết quả đẹp nhất trong quang học nhiễu xạ:** Khả năng phân giải bằng **bậc nhiễu xạ nhân với tổng số vạch được chiếu sáng**. Không phụ thuộc vào mật độ vạch $d$, không phụ thuộc vào tiêu cự!

### Liên hệ với nguyên lý tổng quát

Feynman chỉ ra một điều còn sâu sắc hơn: công thức $R = mN$ là trường hợp đặc biệt của nguyên lý phổ quát:

$$\Delta\nu = \frac{1}{T}$$

Trong đó $T$ là **hiệu thời gian** giữa các tia sáng đi qua những phần khác nhau của cách tử. Tia qua vạch đầu và tia qua vạch cuối (cách nhau $L = Nd$) có hiệu đường đi $mL$ (ở bậc $m$), hiệu thời gian $T = mL/c = mNd/c$.

$$\Delta\nu = c/T = c/(mNd)$$

$$\Delta\lambda = \frac{\lambda^2}{c}\Delta\nu = \frac{\lambda^2}{mNd} \cdot \frac{d}{\lambda} = \frac{\lambda}{mN}$$

Sự thống nhất! Và quan trọng hơn: nguyên lý $\Delta\nu = 1/T$ áp dụng cho **mọi loại thiết bị quang học** — Fabry-Perot etalon, Michelson interferometer, Fourier transform spectrometer — không chỉ cách tử.

**Phép so sánh với xử lý tín hiệu:** $\Delta\nu = 1/T$ chính là **nguyên lý bất định thời gian-tần số** trong DSP: để phân giải hai tần số cách nhau $\Delta f$, cần cửa sổ quan sát ít nhất $T = 1/\Delta f$. Spectrometer cách tử là một "bộ phân tích tần số quang học" hoạt động theo đúng nguyên lý này.

### Ứng dụng: Kính thiên văn radio và phân giải góc

Feynman mở rộng thêm một ví dụ thú vị: kính thiên văn radio (radio telescope) cũng dùng nguyên lý mảng để đạt phân giải góc cao. Hàng trăm anten đặt rải rác trên diện tích lớn (như VLA — Very Large Array ở New Mexico), tín hiệu tổng hợp cho độ phân giải góc tương đương kính thiên văn khổng lồ kích thước bằng khoảng cách giữa các anten xa nhất. Nguyên lý giống hệt cách tử nhiễu xạ — chỉ thay ánh sáng bằng sóng radio.

**Điểm mấu chốt:**

- Tiêu chuẩn Rayleigh: hai vạch phổ phân giải được khi cực đại của vạch này trùng với cực tiểu đầu tiên của vạch kia
- Khả năng phân giải: $R = \lambda/\Delta\lambda = mN$ — tỷ lệ với bậc nhiễu xạ và tổng số vạch
- Nguyên lý phổ quát: $\Delta\nu = 1/T$ — bất định thời gian-tần số áp dụng cho mọi thiết bị quang học
- Tăng phân giải: hoặc tăng $N$ (cách tử to hơn), hoặc tăng $m$ (bậc cao hơn, ví dụ cách tử Echelle)
- Cùng nguyên lý áp dụng cho kính thiên văn, spectrometer, encoder quang học, và phân tích tín hiệu số

---
*Exported from Feynman Bot*
