---
lesson_id: 5408
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-02T15:10:28.680619+00:00"
content_hash: 126c608a00cd
chapter_number: 13
chapter_title: Chapter 13
section_number: 3
section_title: 13–2Work done by gravity
---
# Bảo Toàn Năng Lượng — Phân Tích Chuyên Sâu

*Source: Chapter 13 - Chapter 13 (Section 3) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_13.html)*

# Bảo Toàn Năng Lượng — Phân Tích Chuyên Sâu

## Chứng Minh Chặt Chẽ: Tích Phân Đường Kín Bằng Không

Feynman đặt câu hỏi cụ thể: hãy chứng minh rằng công của trọng lực trên đường kín bất kỳ bằng 0.

**Chiến lược**: Chia đường cong thành các đoạn nhỏ. Với mỗi đoạn nhỏ, phân tích chuyển vị thành thành phần ngang (vuông góc $\hat{r}$) và thành phần hướng kính (dọc $\hat{r}$).

- Thành phần ngang: $\vec{F} \cdot d\vec{s}_\perp = 0$ (lực vuông góc với chuyển vị)
- Thành phần hướng kính: $\vec{F} \cdot d\vec{s}_r = F_r\,dr = -\frac{GMm}{r^2}dr$

Công tổng:
$$W = \int_\text{đường kín} \vec{F} \cdot d\vec{s} = \oint \left(-\frac{GMm}{r^2}\right)dr = \left[\frac{GMm}{r}\right]_\text{đường kín} = 0$$

(vì điểm đầu và điểm cuối trùng nhau: $r_{cuối} = r_{đầu}$)

Điều này hoàn toàn nghiêm ngặt — không phụ thuộc vào hình dạng đường cong!

## Năng Lượng Cơ Học — Hằng Số Chuyển Động

Từ định lý công-động năng:
$$\frac{1}{2}mv_2^2 - \frac{1}{2}mv_1^2 = W_{1\to2} = -\frac{GMm}{r_2} + \frac{GMm}{r_1} = U(1) - U(2)$$

Suy ra: $\frac{1}{2}mv_2^2 + U(r_2) = \frac{1}{2}mv_1^2 + U(r_1)$

Hay: $E = \frac{1}{2}mv^2 - \frac{GMm}{r} = \text{const}$

**Ý nghĩa**: $E$ là một đại lượng bảo toàn — nó không thay đổi trong suốt quá trình chuyển động của vật trong trường hấp dẫn (không ma sát).

## Phân Loại Quỹ Đạo Theo Năng Lượng

| Năng lượng $E$ | Loại quỹ đạo | Vận tốc ở $\infty$ |
|---|---|---|
| $E < 0$ | Ellipse (bị giam) | 0 (không đạt vô cực) |
| $E = 0$ | Parabol | 0 (vừa thoát) |
| $E > 0$ | Hyperbol | $\sqrt{2E/m}$ (thoát với vận tốc dư) |

**Ứng dụng**: Tên lửa từ Trái Đất cần đạt $v_{thoat} = \sqrt{2GM/R} \approx 11.2\,km/s$ để $E = 0$ (quỹ đạo parabol) và rời khỏi hệ Mặt Trời - Trái Đất.

## Bài Toán Vệ Tinh — Quỹ Đạo Hohmann

Vệ tinh ở quỹ đạo tròn $r_1 = 6600\,km$ (ISS, $h \approx 230\,km$). Muốn đưa lên quỹ đạo địa tĩnh $r_2 = 42164\,km$. Cần bao nhiêu năng lượng?

**Năng lượng quỹ đạo tròn** (có thể chứng minh từ bảo toàn E và điều kiện lực hướng tâm):
$$E_{tròn} = -\frac{GMm}{2r}$$

Thay số ($M = 5.97\times10^{24}\,kg$, $m = 1000\,kg$):
- $E_1 = -\frac{6.67\times10^{-11} \times 5.97\times10^{24} \times 1000}{2 \times 6.6\times10^6} \approx -3.02\times10^{10}\,J$
- $E_2 = -\frac{6.67\times10^{-11} \times 5.97\times10^{24} \times 1000}{2 \times 4.22\times10^7} \approx -4.72\times10^9\,J$

$\Delta E = E_2 - E_1 \approx 2.55\times10^{10}\,J$ → Cần ít nhất 25.5 GJ năng lượng cho 1 tấn vệ tinh!

## Ứng Dụng Công Nghiệp: Phân Tích Năng Lượng Cơ Hệ

Trong hệ cơ khí có nhiều thành phần chuyển động (robot, băng tải, dây chuyền), bảo toàn năng lượng là công cụ phân tích mạnh:

**Ví dụ**: Hệ vít me - trượt ngang:
- Motor quay vít me, trục vít chuyển thành chuyển động tịnh tiến
- Năng lượng đầu vào = Thế năng tích trữ + Động năng + Tổn thất ma sát
- $P_{motor} = \frac{d}{dt}\left(\frac{1}{2}mv^2 + mgh\right) + P_{ma\,sat}$

Trong thiết kế: biết $P_{ma\,sat}$ (từ thực nghiệm), biết yêu cầu $v$ và $a$ → tính $P_{motor}$ tối thiểu.

## Bài Tập Có Hướng Dẫn

Một quả cầu thép $m = 0.5\,kg$ bắn ra từ lò xo nén $\Delta x = 5\,cm$ (hằng số $k = 8000\,N/m$) theo hướng ngang trên mặt bàn cao $h = 1.2\,m$. Tìm tầm bay ngang.

**Giải:**
1. Thế năng lò xo: $U_{lx} = \frac{1}{2}k(\Delta x)^2 = \frac{1}{2}\times8000\times0.05^2 = 10\,J$
2. Vận tốc ngang khi rời bàn: $\frac{1}{2}mv^2 = 10\,J \Rightarrow v = \sqrt{20/0.5} = \sqrt{40} \approx 6.32\,m/s$
3. Thời gian rơi: $h = \frac{1}{2}gt^2 \Rightarrow t = \sqrt{2h/g} = \sqrt{2.4/9.8} \approx 0.495\,s$
4. Tầm ngang: $x = vt = 6.32 \times 0.495 \approx 3.13\,m$

## Điểm Mấu Chốt

Bảo toàn năng lượng cơ học ($E = K + U = \text{const}$) là hệ quả trực tiếp của tính bảo toàn của lực hấp dẫn. Trong thực tế kỹ thuật, nó là công cụ thiết kế mạnh mẽ: biết năng lượng đầu vào và tổn thất, có thể tính toán mọi thông số chuyển động mà không cần giải phương trình vi phân phức tạp.

---
*Exported from Feynman Bot*
