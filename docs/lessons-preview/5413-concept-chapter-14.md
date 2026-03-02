---
lesson_id: 5413
lesson_type: concept
approval_status: approved
exported_at: "2026-03-02T15:10:28.822982+00:00"
content_hash: c3459eb05021
chapter_number: 14
chapter_title: Chapter 14
section_number: 2
section_title: 14–1Work
---
# Ôn Tập: Công — Tích Phân Vectơ Trong Không Gian 3D

*Source: Chapter 14 - Chapter 14 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_14.html)*

# Ôn Tập: Công — Tích Phân Vectơ Trong Không Gian 3D

## Câu Hỏi Mở Đầu

Khi cánh tay robot di chuyển đầu hàn theo quỹ đạo 3D phức tạp, motor thực hiện bao nhiêu công? Làm sao tính được khi lực và hướng chuyển động thay đổi liên tục?

## Phân Tích Công Theo Thành Phần

Dịch chuyển thực sự $\Delta\vec{s}$ trong không gian 3D có thể phân tích:
$$\Delta\vec{s} = \Delta x\,\hat{i} + \Delta y\,\hat{j} + \Delta z\,\hat{k}$$

Lực: $\vec{F} = F_x\hat{i} + F_y\hat{j} + F_z\hat{k}$

Công trên đoạn nhỏ:
$$dW = \vec{F}\cdot d\vec{s} = F_x\,dx + F_y\,dy + F_z\,dz$$

Công trên toàn đường đi:
$$W = \int_1^2 \vec{F}\cdot d\vec{s} = \int_1^2 (F_x\,dx + F_y\,dy + F_z\,dz)$$

Đây là **tích phân đường** (line integral) — một trong những công cụ toán học quan trọng nhất trong vật lý và kỹ thuật.

## Ý Nghĩa Hình Học

Hình dung: lực $\vec{F}$ như một "mũi tên" tại mỗi điểm trong không gian. Dịch chuyển $d\vec{s}$ là đoạn nhỏ của quỹ đạo. Tích $\vec{F}\cdot d\vec{s}$ là hình chiếu của lực lên hướng chuyển động, nhân với chiều dài đoạn.

Công = "diện tích" dưới đường cong $F_\parallel$ vs. $s$ (thành phần lực song song vs. quãng đường).

## Phép So Sánh Với Điện Tử

Tích phân đường tương tự với điện áp:
$$V_{AB} = -\int_A^B \vec{E}\cdot d\vec{l}$$

Điện áp giữa hai điểm = tích phân âm của điện trường dọc theo đường nối. Đây là lý do điện áp có thể định nghĩa được (lực điện bảo toàn) và tại sao điện áp không phụ thuộc đường đi từ A đến B (chỉ phụ thuộc A và B).

Trong kỹ thuật đo: khi bạn đo điện áp bằng voltmeter giữa hai điểm trên mạch, bạn đang đo tích phân đường của điện trường — không quan trọng dây đo đi theo đường nào.

## Ứng Dụng: Tính Công Motor Robot

Robot SCARA (2 link phẳng) di chuyển đầu công cụ từ A$(0.3, 0.2)$ đến B$(0.5, -0.1)$ m theo đường thẳng. Lực tác dụng: $\vec{F} = (20, -15)\,N$ (từ motor, không đổi).

Dịch chuyển: $\Delta\vec{s} = (0.2, -0.3)\,m$

Công: $W = \vec{F}\cdot\Delta\vec{s} = 20\times0.2 + (-15)\times(-0.3) = 4 + 4.5 = 8.5\,J$

Nếu lực không đổi, tích phân đường đơn giản thành tích vô hướng. Nhưng khi motor phải điều chỉnh lực theo vị trí (để duy trì tốc độ không đổi dù tải thay đổi), phải dùng tích phân đường đầy đủ.

## Điểm Mấu Chốt

Công là tích phân đường của lực theo quỹ đạo 3D. Phân tích theo thành phần $x, y, z$ biến tích phân đường thành ba tích phân thông thường. Với lực bảo toàn, tích phân này không phụ thuộc đường đi — chỉ phụ thuộc điểm đầu và cuối, và bằng hiệu thế năng.

---
*Exported from Feynman Bot*
