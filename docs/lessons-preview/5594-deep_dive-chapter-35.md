---
lesson_id: 5594
lesson_type: deep_dive
approval_status: pending
exported_at: "2026-03-03T15:33:08.789773+00:00"
content_hash: 80fe914fe59b
chapter_number: 35
chapter_title: Chapter 35
section_number: 4
section_title: 35–3Measuring the color sensation
---
# ## Bài Giảng Chuyên Sâu: Đại Số Màu Sắc — Từ Phối Màu đến Không Gian CIE

*Source: Chapter 35 - Chapter 35 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_35.html)*

## Bài Giảng Chuyên Sâu: Đại Số Màu Sắc — Từ Phối Màu đến Không Gian CIE

### 1. Nền tảng toán học của phối màu

**Định nghĩa toán học:**

Gọi $C$ là một "màu" (tập hợp các phổ ánh sáng tạo ra cùng cảm giác thị giác). Phép cộng màu được định nghĩa:
- $C_1 + C_2$: chiếu đồng thời hai nguồn sáng
- $\alpha C$: điều chỉnh cường độ nguồn sáng hệ số $\alpha > 0$
- Bằng nhau ($=$): hai màu trông như nhau với mắt người

Với ba màu chủ đạo $R$, $G$, $B$ (được chọn sao cho không màu nào là hỗn hợp của hai màu kia), bất kỳ màu $C$ đều thỏa:

$$C \equiv a \cdot R + b \cdot G + c \cdot B$$

trong đó $a$, $b$, $c$ là "color coefficients" (có thể âm).

**Hệ quả đại số:**

Nếu $X \equiv a_1 R + b_1 G + c_1 B$ và $Y \equiv a_2 R + b_2 G + c_2 B$ thì:
$$X + Y \equiv (a_1+a_2)R + (b_1+b_2)G + (c_1+c_2)B$$

Không gian màu là không gian vector tuyến tính 3 chiều trên $\mathbb{R}$.

### 2. Xây dựng biểu đồ màu CIE (Chromaticity Diagram)

**Bước 1: Chuẩn hóa theo cường độ**

Màu sắc không phụ thuộc cường độ — nếu nhân tất cả $a, b, c$ với cùng một hệ số $k > 0$, màu không đổi. Do đó ta chiếu không gian 3D lên mặt phẳng 2D bằng cách chuẩn hóa:
$$x = \frac{a}{a+b+c}, \quad y = \frac{b}{a+b+c}, \quad z = \frac{c}{a+b+c}$$

với ràng buộc $x + y + z = 1$, nên chỉ cần hai tọa độ $(x, y)$ để xác định màu sắc (không tính độ sáng).

**Bước 2: Color matching functions**

CIE 1931 định nghĩa ba hàm color matching $\bar{x}(\lambda)$, $\bar{y}(\lambda)$, $\bar{z}(\lambda)$ dựa trên thực nghiệm trung bình với nhiều người quan sát. Tọa độ CIE XYZ của một nguồn sáng có phổ $I(\lambda)$:

$$X = \int I(\lambda)\bar{x}(\lambda)d\lambda, \quad Y = \int I(\lambda)\bar{y}(\lambda)d\lambda, \quad Z = \int I(\lambda)\bar{z}(\lambda)d\lambda$$

**Bước 3: Chromaticity coordinates**

$$x = \frac{X}{X+Y+Z}, \quad y = \frac{Y}{X+Y+Z}$$

Biểu đồ chromaticity (Fig. 35-4 của Feynman) là đồ thị $(x, y)$ trong đó:
- Màu phổ thuần túy (pure spectral colors) tạo thành đường cong khép kín (spectral locus)
- Màu trắng tại tâm (~$x = y = 1/3$)
- Màu bão hòa nằm trên đường biên
- Đường thẳng nối đỏ và tím tạo "line of purples" (màu tím-đỏ không có trong phổ tự nhiên)

### 3. Phép tính hình học trên biểu đồ chromaticity

**Trộn màu = điểm nằm trên đoạn thẳng**

Nếu màu $A$ ở vị trí $(x_A, y_A)$ và màu $B$ ở $(x_B, y_B)$, thì hỗn hợp $\alpha A + (1-\alpha)B$ nằm tại:
$$(x_{mix}, y_{mix}) = \alpha(x_A, y_A) + (1-\alpha)(x_B, y_B)$$

Hỗn hợp 50-50 nằm giữa đoạn $AB$; tỉ lệ $1/4 : 3/4$ nằm ở điểm chia $1/4$ từ $A$ đến $B$.

**Gamut của hệ màu:**

Ba màu chủ đạo R, G, B định nghĩa tam giác trong biểu đồ. Tất cả màu nằm trong tam giác có thể được tái tạo với hệ số dương. Màu nằm ngoài tam giác đòi hỏi hệ số âm — không thể tái tạo bằng phép cộng ánh sáng từ ba nguồn.

Gamut của màn hình sRGB (tiêu chuẩn phổ biến) bao phủ khoảng **35%** diện tích của spectral locus. Màn hình Display P3 bao phủ khoảng **45%**. Không có hệ ba màu chủ đạo nào bao phủ 100% vì spectral locus là đường cong lồi không phải tam giác.

### 4. Ứng dụng kỹ thuật: Calibration màu camera và QC tự động

**Bài toán:** Dây chuyền sản xuất vũ khí cần kiểm tra màu sơn chống gỉ (mặt ngoài thân tên lửa) với dung sai màu $\Delta E_{00} < 2$ (đơn vị CIEDE2000). Camera RGB thông thường có nhiễu đo màu $\Delta E_{00} \approx 5$–10 — không đủ.

**Giải pháp precision color measurement:**

Bước 1: Chuyển đổi từ RGB camera sang CIE XYZ:
$$\begin{pmatrix} X \\ Y \\ Z \end{pmatrix} = M_{3\times3} \begin{pmatrix} R \\ G \\ B \end{pmatrix}$$

Ma trận $M$ được xác định bằng calibration với bảng màu chuẩn (đo bằng spectrophotometer).

Bước 2: Chuyển từ XYZ sang CIELab (perceptually uniform color space):
$$L^* = 116\left(\frac{Y}{Y_n}\right)^{1/3} - 16$$
$$a^* = 500\left[\left(\frac{X}{X_n}\right)^{1/3} - \left(\frac{Y}{Y_n}\right)^{1/3}\right]$$
$$b^* = 200\left[\left(\frac{Y}{Y_n}\right)^{1/3} - \left(\frac{Z}{Z_n}\right)^{1/3}\right]$$

Bước 3: Tính $\Delta E_{00}$ giữa màu mẫu và tiêu chuẩn.

**Kết quả:** Với calibration đúng, sai số $\Delta E_{00}$ của camera có thể giảm xuống $<1$ — vượt yêu cầu.

### 5. Bài tập mẫu

**Đề bài:** Màu A có tọa độ $(x_A, y_A) = (0.6, 0.3)$ (đỏ) và màu B có $(x_B, y_B) = (0.2, 0.7)$ (xanh lá). Tìm tọa độ chromaticity của hỗn hợp $3A + 1B$ (tỉ lệ 3:1 về cường độ).

**Lời giải:**

Hỗn hợp $\frac{3}{4}A + \frac{1}{4}B$:
$$x_{mix} = \frac{3}{4}(0.6) + \frac{1}{4}(0.2) = 0.45 + 0.05 = 0.50$$
$$y_{mix} = \frac{3}{4}(0.3) + \frac{1}{4}(0.7) = 0.225 + 0.175 = 0.40$$

Điểm hỗn hợp tại $(0.50, 0.40)$ — nằm ở $1/4$ đường từ A đến B (cách A một phần tư khoảng cách AB), tương ứng với màu cam-vàng.

### 6. Ý nghĩa sâu xa

Không gian màu 3D là hệ quả trực tiếp của việc mắt người có ba loại cone. Nếu tiến hóa cho chúng ta bốn loại cone (như một số loài chim), không gian màu sẽ là 4D và biểu đồ chromaticity sẽ là khối 3D. Người mù màu (dichromacy) chỉ có hai loại cone hoạt động — không gian màu của họ là 2D, và họ thấy ít màu hơn nhưng không "mù hoàn toàn". Đây là minh chứng rõ nhất cho việc toán học của thị giác xuất phát từ sinh học.

---
*Exported from Feynman Bot*
