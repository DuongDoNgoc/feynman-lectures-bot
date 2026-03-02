---
lesson_id: 5410
lesson_type: concept
approval_status: approved
exported_at: "2026-03-02T15:10:28.738922+00:00"
content_hash: 44aab9e2866f
chapter_number: 13
chapter_title: Chapter 13
section_number: 4
section_title: 13–3Summation of energy
---
# Năng Lượng Hệ Nhiều Vật

*Source: Chapter 13 - Chapter 13 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_13.html)*

# Năng Lượng Hệ Nhiều Vật

## Câu Hỏi Mở Đầu

Khi bạn tính năng lượng của cả hệ robot 6-bậc-tự-do với 6 khớp, 6 đoạn cánh tay, và tải — có cần tính tất cả tương tác chéo không? Hay có công thức đơn giản hơn?

## Mở Rộng Bảo Toàn Năng Lượng Cho N Vật

Với hệ $N$ vật, tổng động năng là tổng đơn giản:
$$K = \sum_{i=1}^{N} \frac{1}{2}m_i v_i^2$$

Còn thế năng? Feynman chứng minh: thế năng tương tác cặp vật $i$ và $j$:
$$U_{ij} = -\frac{Gm_im_j}{r_{ij}}$$

Tổng thế năng là tổng trên tất cả các **cặp** (mỗi cặp tính một lần):
$$U = \sum_{\text{cặp}} U_{ij} = \sum_{i<j} \left(-\frac{Gm_im_j}{r_{ij}}\right)$$

Và tổng cơ năng $E = K + U$ là hằng số!

## Tại Sao Chỉ Tính Theo Cặp?

Lực giữa vật $i$ và $j$ thoả mãn Newton III: $\vec{F}_{ij} = -\vec{F}_{ji}$. Do đó, khi tính tốc độ thay đổi năng lượng, đóng góp của cặp $(i,j)$ là:

$$\frac{dU_{ij}}{dt} = \frac{d}{dt}\left(-\frac{Gm_im_j}{r_{ij}}\right)$$

Và công suất của lực: $\vec{F}_{ij}\cdot\vec{v}_i + \vec{F}_{ji}\cdot\vec{v}_j$

Hai số hạng này triệt tiêu nhau đúng bằng $-dU_{ij}/dt$. Phép tính này có thể mở rộng cho mọi cặp, và chứng minh $dE/dt = 0$.

## Phép So Sánh: Hệ Nhiều Vật Như Mạng Điện Trở

Hãy nghĩ hệ $N$ vật như mạng điện với $N$ nút. Năng lượng tương tác giữa mỗi cặp như "tụ điện" nối hai nút. Tổng năng lượng hệ = tổng năng lượng tất cả tụ điện + tổng động năng các "nút" (phần tử chuyển động).

Trong thiết kế mạng truyền cơ năng (hộp số, dây đai, bánh răng): năng lượng được truyền từ động cơ qua nhiều "cặp" tương tác. Bảo toàn năng lượng đảm bảo: tổng đầu ra = đầu vào - tổn thất.

## Ứng Dụng: Phân Tích Hệ Robot

Robot có $N$ khớp. Mỗi link $i$ có khối lượng $m_i$ và trọng tâm tại độ cao $h_i(\vec{q})$ (phụ thuộc góc khớp $\vec{q}$). Tổng thế năng trọng lực:
$$U = \sum_{i=1}^{N} m_i g h_i(\vec{q})$$

Đây không phải tương tác cặp (không có hấp dẫn giữa các link) mà là thế năng từng link trong trường ngoài (trọng lực Trái Đất). Vẫn là tổng đơn giản!

Thuật toán điều khiển robot hiện đại (model-based control) tính $U(\vec{q})$ và $K(\vec{q}, \dot{\vec{q}})$ real-time để tính mô-men bù trọng lực tại mỗi khớp — đây là ứng dụng trực tiếp của bảo toàn năng lượng nhiều vật.

## Điểm Mấu Chốt

Hệ $N$ vật có năng lượng bảo toàn bằng tổng động năng từng vật cộng tổng thế năng từng cặp. Cấu trúc đơn giản này (không có "tương tác ba vật" thực sự trong cơ học Newton) là lý do tại sao bảo toàn năng lượng cực kỳ mạnh mẽ trong thực tế kỹ thuật.

---
*Exported from Feynman Bot*
