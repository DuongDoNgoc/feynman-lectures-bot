---
lesson_id: 5415
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:04.500459+00:00"
content_hash: 7c08985e27b3
chapter_number: 14
chapter_title: Chapter 14
section_number: 2
section_title: 14–1Work
---
# Quiz: Ôn Tập Công và Thế Năng

*Source: Chapter 14 - Chapter 14 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_14.html)*

# Quiz: Ôn Tập Công và Thế Năng

## Câu 1

Lực $\vec{F} = (3y)\hat{i} + (3x)\hat{j}\,N$ tác dụng lên vật. Điều kiện lực bảo toàn được kiểm tra bằng $\nabla\times\vec{F} = 0$. Lực này có bảo toàn không?

A) Không, vì $F_x$ phụ thuộc $y$ và $F_y$ phụ thuộc $x$
B) Có, vì $\partial F_x/\partial y = \partial F_y/\partial x = 3$
C) Không, vì lực không hướng về một điểm cố định
D) Có, vì lực tuyến tính theo tọa độ

**Đáp án: B**

*Giải thích: Điều kiện lực bảo toàn (2D): $\frac{\partial F_x}{\partial y} = \frac{\partial F_y}{\partial x}$. Ở đây: $\frac{\partial(3y)}{\partial y} = 3$ và $\frac{\partial(3x)}{\partial x} = 3$. Bằng nhau → lực bảo toàn. Thế năng: $U = -3xy$ (kiểm tra: $-\partial U/\partial x = 3y = F_x$, $-\partial U/\partial y = 3x = F_y$).*

## Câu 2

Robot di chuyển tải từ A$(0,0,0)$ đến B$(1,1,1)$ m theo hai đường: đường thẳng và đường $L$-shaped (đi theo $x$, rồi $y$, rồi $z$). Lực tác dụng chỉ là trọng lực $\vec{F} = -mg\hat{k}$. So sánh công của trọng lực theo hai đường:

A) Đường thẳng cho công lớn hơn
B) Đường L-shaped cho công lớn hơn
C) Hai đường cho công bằng nhau: $W = -mg \times 1\,m$
D) Phụ thuộc vào khối lượng tải

**Đáp án: C**

*Giải thích: Trọng lực bảo toàn — công chỉ phụ thuộc hiệu độ cao $\Delta z = 1\,m$. $W = -mg\Delta z$ (âm vì lực trọng lực ngược chiều dịch chuyển lên). Đường đi không ảnh hưởng.*

## Câu 3

Thế năng của một hệ là $U = \frac{1}{2}kx^2 + mgy$. Lực tác dụng lên vật tại điểm $(x_0, y_0)$ là:

A) $\vec{F} = kx_0\hat{i} + mg\hat{j}$
B) $\vec{F} = -kx_0\hat{i} - mg\hat{j}$
C) $\vec{F} = -kx_0\hat{i} + mg\hat{j}$
D) $\vec{F} = kx_0\hat{i} - mg\hat{j}$

**Đáp án: B**

*Giải thích: $\vec{F} = -\nabla U = -\frac{\partial U}{\partial x}\hat{i} - \frac{\partial U}{\partial y}\hat{j} = -kx_0\hat{i} - mg\hat{j}$. Đây là sự kết hợp lực lò xo (theo $x$) và trọng lực (theo $y$, hướng xuống = $-\hat{j}$).*

## Câu 4 — Tự Luận

Trong hệ thống khắc laser CNC 3-trục của bạn, đầu laser di chuyển theo quỹ đạo: lên thẳng đứng $\Delta z = 0.5\,m$ rồi ngang $\Delta x = 1\,m$ rồi xuống $\Delta z = -0.5\,m$. Tổng tải chuyển động (khối lượng đầu laser) $m = 3\,kg$. 

(a) Tính công tổng của trọng lực trên toàn quỹ đạo khép kín.
(b) Nếu hiệu suất motor lên/xuống là 90%/70% (thu hồi), tính năng lượng ròng từ nguồn điện cho một chu kỳ.

*Gợi ý: (a) đường kín → công trọng lực = 0; (b) năng lượng tiêu thụ = lên×(1-η_lên) + |năng lượng xuống|×(1-η_xuống)*

```json
{
  "quiz_id": 5415,
  "questions": [
    {"id": 1, "answer": "B", "concept": "điều kiện lực bảo toàn: curl bằng 0"},
    {"id": 2, "answer": "C", "concept": "công lực bảo toàn độc lập đường đi"},
    {"id": 3, "answer": "B", "concept": "lực = âm gradient thế năng"}
  ]
}
```


## Quiz Questions

**Q1:** No question text

**Correct:** B

**Q2:** No question text

**Correct:** C

**Q3:** No question text

**Correct:** B


---
*Exported from Feynman Bot*
