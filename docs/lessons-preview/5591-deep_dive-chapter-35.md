---
lesson_id: 5591
lesson_type: deep_dive
approval_status: pending
exported_at: "2026-03-03T15:33:08.746383+00:00"
content_hash: ad412d3ed6a2
chapter_number: 35
chapter_title: Chapter 35
section_number: 1
section_title: 35Color Vision
---
# ## Bài Giảng Chuyên Sâu: Cấu Trúc Thị Giác Màu Sắc — Từ Giải Phẫu đến Không Gian

*Source: Chapter 35 - Chapter 35 (Section 1) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_35.html)*

## Bài Giảng Chuyên Sâu: Cấu Trúc Thị Giác Màu Sắc — Từ Giải Phẫu đến Không Gian Màu

### 1. Giải phẫu hệ thống thị giác

**Võng mạc và phân bố tế bào quang thụ**

Võng mạc người (diện tích ~1100 mm²) chứa khoảng:
- **120 triệu tế bào que (rods)**: phân bố ở vùng ngoại vi, nhạy với ánh sáng yếu (ngưỡng khoảng 1 photon), không phân biệt màu, đáp ứng đỉnh tại $\lambda \approx 498\,\text{nm}$
- **6-7 triệu tế bào nón (cones)**: tập trung tại fovea (đường kính ~1.5 mm), ba loại S/M/L

**Fovea** là vùng nhìn trung tâm với mật độ cone cực cao (~150,000 cone/mm²), không có rod. Đây là lý do mắt người cần di chuyển ("saccade") liên tục để quét thông tin — không phải toàn bộ võng mạc đều sắc nét.

**Điểm mù (optic disc)**: nơi dây thần kinh thị giác và mạch máu đi qua, không có tế bào quang thụ, kích thước ~1.5 mm × 2 mm, nằm ở ~15° phía mũi từ fovea.

### 2. Phổ hấp thụ của ba loại tế bào nón

Ba loại tế bào nón có đỉnh hấp thụ:
- **S-cone (Short)**: $\lambda_S \approx 420\,\text{nm}$ (tím-xanh)
- **M-cone (Medium)**: $\lambda_M \approx 534\,\text{nm}$ (xanh lá)
- **L-cone (Long)**: $\lambda_L \approx 564\,\text{nm}$ (đỏ-vàng)

Đáp ứng của mỗi loại cone với phổ ánh sáng $I(\lambda)$:
$$S = \int I(\lambda)\, s(\lambda)\, d\lambda, \quad M = \int I(\lambda)\, m(\lambda)\, d\lambda, \quad L = \int I(\lambda)\, l(\lambda)\, d\lambda$$

trong đó $s(\lambda)$, $m(\lambda)$, $l(\lambda)$ là hàm nhạy quang phổ của từng loại cone.

### 3. Metamerism — Hiện tượng đồng màu

Hai nguồn sáng có phổ $I_1(\lambda)$ và $I_2(\lambda)$ khác nhau nhưng tạo cảm giác màu như nhau nếu:
$$\int I_1(\lambda) s(\lambda) d\lambda = \int I_2(\lambda) s(\lambda) d\lambda$$
$$\int I_1(\lambda) m(\lambda) d\lambda = \int I_2(\lambda) m(\lambda) d\lambda$$
$$\int I_1(\lambda) l(\lambda) d\lambda = \int I_2(\lambda) l(\lambda) d\lambda$$

Vì không gian $I(\lambda)$ là vô chiều còn không gian $(S, M, L)$ là ba chiều, phép ánh xạ $I(\lambda) \to (S,M,L)$ có kernel vô chiều — nghĩa là vô số phổ khác nhau cho cùng một bộ ba $(S,M,L)$.

### 4. Ứng dụng kỹ thuật: Calibration màu trong camera công nghiệp

**Bài toán thực tế:** Camera inspection trong dây chuyền sản xuất cần phát hiện lỗi màu sơn. Camera RGB có sensor với hàm đáp ứng phổ $r(\lambda)$, $g(\lambda)$, $b(\lambda)$ khác với hàm $l(\lambda)$, $m(\lambda)$, $s(\lambda)$ của mắt người. Do đó, camera "thấy" màu khác với người — cần hiệu chỉnh.

**Quy trình calibration:**

Bước 1: Đo phổ ánh sáng của bảng màu chuẩn (color checker chart) bằng spectrophotometer: $I_i(\lambda)$ cho $i = 1..24$ màu.

Bước 2: Tính tọa độ CIE XYZ từ phổ (dùng hàm color matching functions $\bar{x}$, $\bar{y}$, $\bar{z}$ — tương đương hàm nhạy mắt chuẩn):
$$X_i = \int I_i(\lambda)\bar{x}(\lambda)d\lambda$$

Bước 3: Đo giá trị RGB của camera cho cùng 24 màu.

Bước 4: Tìm ma trận $3\times 3$ chuyển đổi $[R_i, G_i, B_i]^T \to [X_i, Y_i, Z_i]^T$ bằng least squares.

**Tầm quan trọng với máy đo precision:** Trong kiểm tra bề mặt chip bán dẫn, màu sắc của oxide layer là chỉ thị cho độ dày (giao thoa màng mỏng). Sai số màu dẫn đến sai số ước tính độ dày lớp oxide — có thể ảnh hưởng đến quy trình etch.

### 5. Bài tập mẫu: Phân tích metamerism trong hệ LED

**Đề bài:** Hai đèn LED:
- LED A: ánh sáng trắng broadband, phổ xấp xỉ flat từ 400–700 nm.
- LED B: ba LED đơn sắc (R: 630 nm, G: 530 nm, B: 455 nm) được trộn lại.

Cả hai đèn đều trông "trắng" với mắt người. Chứng minh chúng là metamers và giải thích tại sao camera multispectral (có thêm kênh NIR và UV) có thể phân biệt chúng.

**Lời giải:**

Với mắt người (3 kênh S, M, L), cả hai đèn cho cùng bộ ba $(S_A, M_A, L_A) = (S_B, M_B, L_B)$ — đây là điều kiện metamerism. Tuy nhiên phổ $I_A(\lambda) \ne I_B(\lambda)$ tại mọi bước sóng.

Camera multispectral đo tại nhiều bước sóng hơn (ví dụ 16 kênh từ 400–1000 nm). Bởi vì phổ $I_A$ và $I_B$ khác nhau, các kênh đo tại bước sóng mà hàm $s(\lambda)$, $m(\lambda)$, $l(\lambda)$ không đủ nhạy sẽ cho giá trị khác nhau. Camera multispectral "phá vỡ" metamerism vì nó có nhiều chiều đo lường hơn ba.

**Ứng dụng:** Hệ thống phân loại thực phẩm dùng camera hyperspectral (>100 kênh) để phân biệt các sản phẩm có màu giống nhau với mắt người nhưng khác nhau về thành phần hóa học.

### 6. Giới hạn của thị giác và cảm biến

| Thuộc tính | Mắt người | Camera RGB | Spectrophotometer |
|---|---|---|---|
| Số kênh màu | 3 (S, M, L) | 3 (R, G, B) | ~1000 |
| Dải bước sóng | 380–780 nm | 380–700 nm | 300–1100 nm |
| Metamerism | Có | Có | Không |
| Dynamic range | ~10⁶ (thích nghi) | ~10⁴ | ~10⁸ |

Kết luận: Mắt người là bộ cảm biến 3-kênh thích nghi cao nhưng có giới hạn cơ bản về phân giải màu. Trong kỹ thuật đo lường precision, cần hiểu rõ giới hạn này để chọn công cụ phù hợp.

---
*Exported from Feynman Bot*
