---
lesson_id: 5411
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:04.403715+00:00"
content_hash: e1e5b41df6e6
chapter_number: 13
chapter_title: Chapter 13
section_number: 4
section_title: 13–3Summation of energy
---
# Năng Lượng Hệ Nhiều Vật — Phân Tích Chuyên Sâu

*Source: Chapter 13 - Chapter 13 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_13.html)*

# Năng Lượng Hệ Nhiều Vật — Phân Tích Chuyên Sâu

## Chứng Minh Bảo Toàn Năng Lượng Cho N Vật

Xét $N$ vật với vị trí $\vec{r}_i$, khối lượng $m_i$. Lực tác dụng lên vật $i$ do tất cả vật khác:
$$m_i\frac{d^2\vec{r}_i}{dt^2} = \sum_{j \neq i} \vec{F}_{ij}$$

Tốc độ thay đổi tổng động năng:
$$\frac{dK}{dt} = \sum_i \vec{F}_i^{tổng} \cdot \vec{v}_i = \sum_i \sum_{j\neq i} \vec{F}_{ij} \cdot \vec{v}_i$$

Tổng thế năng cặp: $U = \sum_{i<j} U_{ij}(r_{ij})$

Tốc độ thay đổi thế năng cặp $(i,j)$:
$$\frac{dU_{ij}}{dt} = \frac{\partial U_{ij}}{\partial r_{ij}}\frac{dr_{ij}}{dt}$$

Với $\vec{r}_{ij} = \vec{r}_i - \vec{r}_j$ và $\vec{F}_{ij} = -\frac{\partial U_{ij}}{\partial r_{ij}}\hat{r}_{ij}$:

$$\frac{dU_{ij}}{dt} = -\vec{F}_{ij}\cdot\frac{d\vec{r}_{ij}}{dt} = -\vec{F}_{ij}\cdot(\vec{v}_i - \vec{v}_j) = -\vec{F}_{ij}\cdot\vec{v}_i + \vec{F}_{ij}\cdot\vec{v}_j$$

Dùng Newton III: $\vec{F}_{ji} = -\vec{F}_{ij}$:
$$\frac{dU_{ij}}{dt} = -\vec{F}_{ij}\cdot\vec{v}_i - \vec{F}_{ji}\cdot\vec{v}_j$$

Tổng tất cả các cặp:
$$\frac{dU}{dt} = -\sum_{i<j}(\vec{F}_{ij}\cdot\vec{v}_i + \vec{F}_{ji}\cdot\vec{v}_j) = -\frac{dK}{dt}$$

Do đó: $\frac{d(K+U)}{dt} = 0$ — chứng minh hoàn chỉnh!

## Đối Xứng $r_{ij} = r_{ji}$: Tại Sao Quan Trọng?

Điều kiện $r_{ij} = r_{ji}$ (khoảng cách không có hướng) đảm bảo:
$$U_{ij} = U(r_{ij}) = U(r_{ji}) = U_{ji}$$

Nếu thế năng tương tác phụ thuộc vào hướng (không đối xứng), bảo toàn năng lượng có thể bị phá vỡ. Trong thực tế, tất cả các lực cơ bản (hấp dẫn, điện từ, hạt nhân) đều thỏa mãn tính đối xứng này — đây là hệ quả của định luật Newton III.

## Ứng Dụng: Mô Phỏng Động Lực Học Robot

Phương trình chuyển động robot (Euler-Lagrange):
$$\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{q}_i}\right) - \frac{\partial L}{\partial q_i} = \tau_i$$

Trong đó $L = K - U$ (Lagrangian). Viết tường minh:
$$M(\vec{q})\ddot{\vec{q}} + C(\vec{q},\dot{\vec{q}})\dot{\vec{q}} + G(\vec{q}) = \vec{\tau}$$

- $M(\vec{q})$: ma trận quán tính (từ $K$)
- $C(\vec{q},\dot{\vec{q}})$: ma trận Coriolis-ly tâm
- $G(\vec{q})$: vectơ trọng lực (gradient của $U$ theo $\vec{q}$)
- $\vec{\tau}$: vectơ mô-men khớp

**Bảo toàn năng lượng** đảm bảo: $\dot{E} = \vec{\tau}\cdot\dot{\vec{q}} - P_{ma\,sat}$ — công suất đầu vào bằng tốc độ thay đổi năng lượng cộng tổn thất.

## Hệ Thống Nhiều Vật Trong Đo Lường Chính Xác

**Bài toán**: Cân Wheatstone cơ học (dùng trong cân phân tích) có hệ thống đòn bẩy 3 vật. Phân tích cân bằng năng lượng khi thêm tải nhỏ $\delta m$:

Thế năng hệ: $U = \sum_i m_i g h_i(\theta)$

Tại vị trí cân bằng: $\frac{dU}{d\theta} = 0$

Độ nhạy: $\frac{d^2U}{d\theta^2}$ — hệ số này quyết định độ nhạy của cân.

Thiết kế cân chính xác: tối ưu hóa $\frac{d^2U}{d\theta^2}$ để đạt độ nhạy cao nhất trong khi vẫn giữ ổn định.

## Bài Tập Có Hướng Dẫn

Hệ gồm 3 vật nối bằng lò xo: $m_1 = 1\,kg$ và $m_3 = 1\,kg$ nối với $m_2 = 2\,kg$ ở giữa. Hai lò xo có $k = 100\,N/m$. Ban đầu $m_2$ bị đẩy sang phải $x = 0.1\,m$ rồi thả.

**Năng lượng ban đầu:**
$E_0 = \frac{1}{2}k x^2 + \frac{1}{2}k x^2 = kx^2 = 100\times0.01 = 1\,J$ (cả hai lò xo nén/giãn)

**Khi $m_2$ đến vị trí cân bằng:**
Tất cả $E$ chuyển thành động năng: $\frac{1}{2}(m_1+m_2+m_3)v_{cm}^2 + E_{dao\,động\,nội} = 1\,J$

**Tần số dao động**: $\omega = \sqrt{k(1/m_1 + 1/m_2 + 1/m_3)/...}$ (cần giải eigenvalue).

Đây là bài toán mô phỏng rung động trong máy công cụ CNC — hiểu dao động nhiều vật để tránh cộng hưởng.

## Điểm Mấu Chốt

Bảo toàn năng lượng hệ nhiều vật là hệ quả của Newton III và tính đối xứng của tương tác cặp. Nó là nền tảng của phương trình Lagrange — công cụ mạnh nhất để mô tả hệ cơ học phức tạp (robot, máy móc, cấu trúc) trong kỹ thuật hiện đại.

---
*Exported from Feynman Bot*
