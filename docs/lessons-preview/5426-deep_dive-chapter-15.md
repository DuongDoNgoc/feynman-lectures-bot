---
lesson_id: 5426
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-02T15:10:29.137111+00:00"
content_hash: 0ab04e795b2b
chapter_number: 15
chapter_title: Chapter 15
section_number: 4
section_title: 15–3The Michelson-Morley experiment
---
# Michelson-Morley — Phân Tích Chuyên Sâu

*Source: Chapter 15 - Chapter 15 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_15.html)*

# Michelson-Morley — Phân Tích Chuyên Sâu

## Bước 1: Tính Toán Dự Đoán Của Lý Thuyết Ether

Xét giao thoa kế với hai nhánh dài $L$, một nhánh song song ($\parallel$) và một nhánh vuông góc ($\perp$) với "gió ether" vận tốc $v$.

**Nhánh song song với gió ether** (đi và về):
- Đi (ngược gió): $t_1 = L/(c-v)$
- Về (xuôi gió): $t_2 = L/(c+v)$
- Tổng: $t_\parallel = \frac{L}{c-v} + \frac{L}{c+v} = \frac{2Lc}{c^2-v^2} = \frac{2L/c}{1-v^2/c^2}$

**Nhánh vuông góc với gió ether** (phải đi chéo để bù gió):
- Vận tốc thực sự theo nhánh: $\sqrt{c^2 - v^2}$
- Thời gian: $t_\perp = \frac{2L}{\sqrt{c^2-v^2}} = \frac{2L/c}{\sqrt{1-v^2/c^2}}$

**Hiệu thời gian:**
$$\Delta t = t_\parallel - t_\perp = \frac{2L}{c}\left[\frac{1}{1-\beta^2} - \frac{1}{\sqrt{1-\beta^2}}\right]$$

Trong đó $\beta = v/c \ll 1$. Dùng khai triển Taylor:
$$\frac{1}{1-\beta^2} \approx 1 + \beta^2, \quad \frac{1}{\sqrt{1-\beta^2}} \approx 1 + \frac{\beta^2}{2}$$

$$\Delta t \approx \frac{2L}{c}\left[(1+\beta^2) - \left(1+\frac{\beta^2}{2}\right)\right] = \frac{L\beta^2}{c} = \frac{Lv^2}{c^3}$$

**Dịch chuyển vân giao thoa** khi quay 90° (đổi vai trò hai nhánh):
$$\Delta N = \frac{2c\Delta t}{\lambda} = \frac{2Lv^2}{c^2\lambda}$$

Với $L = 11\,m$, $v = 30\,km/s = 3\times10^4\,m/s$, $\lambda = 590\,nm$:
$$\Delta N = \frac{2 \times 11 \times (3\times10^4)^2}{(3\times10^8)^2 \times 590\times10^{-9}} = \frac{2 \times 11 \times 9\times10^8}{9\times10^{16} \times 5.9\times10^{-7}} \approx 0.37 \text{ vân}$$

Kết quả đo: $< 0.01$ vân → **nhỏ hơn 37 lần dự đoán**.

## Bước 2: Giải Thích FitzGerald-Lorentz

George FitzGerald và Hendrik Lorentz (độc lập, 1889-1892) đề xuất: vật thể co lại theo hướng chuyển động với hệ số $\sqrt{1-v^2/c^2}$.

Nếu nhánh song song co thành $L\sqrt{1-\beta^2}$:
$$t_\parallel^{corrected} = \frac{2L\sqrt{1-\beta^2}/c}{1-\beta^2} = \frac{2L/c}{\sqrt{1-\beta^2}} = t_\perp$$

$\Delta t = 0$ → giải thích được thí nghiệm! Nhưng giải thích này là **ad hoc** — không có lý do vật lý sâu xa nào.

## Bước 3: Einstein — Giải Thích Nguyên Lý

Einstein không giải thích tại sao kết quả bằng 0 — ông **tiên đề hóa** $c$ = hằng số và suy ra mọi thứ:

1. $c$ bằng nhau trong mọi hệ quy chiếu quán tính
2. Suy ra biến đổi Lorentz (thay thế Galilean)
3. Suy ra co độ dài, giãn thời gian, $E = mc^2$, v.v.

Co độ dài Lorentz không phải "lực ether tác dụng" mà là hệ quả hình học của không-thời gian Minkowski. Thí nghiệm MM là **bằng chứng thực nghiệm cho tiên đề của Einstein**.

## Bước 4: Giao Thoa Kế Michelson Hiện Đại — LIGO

**Thiết kế LIGO** (phiên bản cực đoan của giao thoa kế Michelson):
- Hai nhánh dài $L = 4\,km$, vuông góc nhau
- Gương Fabry-Perot: ánh sáng đi lại ~300 lần → độ dài hiệu quả ~1200 km
- Laser công suất 100 W, sóng đứng trong cavity
- Độ nhạy: $\delta L \sim 10^{-18}\,m$

**Tại sao cần độ nhạy này?** Sóng hấp dẫn từ sáp nhập hai lỗ đen cách $1.3$ tỷ năm ánh sáng gây biến dạng không gian $h = \Delta L/L \sim 10^{-21}$ → $\Delta L = 4\times10^3 \times 10^{-21} = 4\times10^{-18}\,m$.

**Nguồn nhiễu phải khắc phục:**
- Nhiễu địa chấn: cách ly bằng con lắc 4 tầng
- Nhiễu nhiệt (Brownian motion của gương): làm lạnh đến $\sim20\,K$
- Nhiễu lượng tử photon (shot noise): tăng công suất laser + squeezed light

## Bước 5: Cảm Biến Giao Thoa Kế Trong Máy CNC

Giao thoa kế laser Renishaw XL-80 (dùng trong máy CNC chính xác):
- Bước sóng laser He-Ne: $\lambda = 632.8\,nm$
- Mỗi vân giao thoa = $\lambda/2 = 316.4\,nm$ dịch chuyển
- Đếm vân với phân giải $1/1024$ vân → **độ phân giải $\sim 0.3\,nm$**

**Hiệu chỉnh môi trường** (quan trọng ở mức nm!):
- Bước sóng thực tế: $\lambda_{thực} = \lambda_0/n_{không\,khí}$
- $n_{không\,khí}$ phụ thuộc nhiệt độ, áp suất, độ ẩm
- Sai số 1°C nhiệt độ → sai số 1 ppm → $1\,\mu m/m$ chiều dài

Đây là kỹ thuật đo chính xác nhất trong cơ khí chính xác — ứng dụng trực tiếp nguyên lý Michelson vào đo lường công nghiệp.

## Điểm Mấu Chốt

Michelson-Morley 1887 là thí nghiệm âm tính có ảnh hưởng lớn nhất lịch sử vật lý. Phân tích toán học dự đoán $\Delta N \approx 0.37$ vân nhưng thực đo $< 0.01$. FitzGerald-Lorentz giải thích bằng co độ dài ad hoc; Einstein giải thích bằng tiên đề $c$ = hằng số — đơn giản, sâu sắc, và dẫn đến toàn bộ tương đối hẹp. Ngày nay, nguyên lý giao thoa kế Michelson là nền tảng của thiết bị đo chính xác nhất: LIGO (đo sóng hấp dẫn) và giao thoa kế laser CNC (đo nm trong cơ khí chính xác).

---
*Exported from Feynman Bot*
