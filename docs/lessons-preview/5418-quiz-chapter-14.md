---
lesson_id: 5418
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-02T15:10:28.936069+00:00"
content_hash: 9f5372d5291f
chapter_number: 14
chapter_title: Chapter 14
section_number: 4
section_title: 14–3Conservative forces
---
# Quiz: Lực Bảo Toàn

*Source: Chapter 14 - Chapter 14 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_14.html)*

# Quiz: Lực Bảo Toàn

## Câu 1

Lực $\vec{F} = (2xy + z^3)\hat{i} + x^2\hat{j} + 3xz^2\hat{k}$ cần kiểm tra tính bảo toàn. Điều kiện nào cần kiểm tra?

A) $|\vec{F}|$ = const
B) $\frac{\partial F_x}{\partial y} = \frac{\partial F_y}{\partial x}$, $\frac{\partial F_y}{\partial z} = \frac{\partial F_z}{\partial y}$, $\frac{\partial F_z}{\partial x} = \frac{\partial F_x}{\partial z}$
C) $\vec{F}\cdot\vec{r} = 0$
D) $\nabla\cdot\vec{F} = 0$

**Đáp án: B**

*Giải thích: Điều kiện lực bảo toàn là $\nabla\times\vec{F} = 0$, tương đương với 3 phương trình trong B. Kiểm tra: $\partial F_x/\partial y = 2x = \partial F_y/\partial x = 2x$ ✓; $\partial F_y/\partial z = 0 = \partial F_z/\partial y = 0$ ✓; $\partial F_z/\partial x = 3z^2 = \partial F_x/\partial z = 3z^2$ ✓ → Lực bảo toàn!*

## Câu 2

Khớp đàn hồi robot có thế năng $U(\theta) = \frac{1}{2}k\theta^2$ với $k = 200\,N\cdot m/rad$. Mô-men lực đàn hồi tại $\theta = 15° = \pi/12\,rad$ là:

A) $+200 \times \pi/12 \approx +52.4\,N\cdot m$ (hướng tăng $\theta$)
B) $-200 \times \pi/12 \approx -52.4\,N\cdot m$ (hướng giảm $\theta$)
C) $+100 \times (\pi/12)^2 \approx +6.9\,N\cdot m$
D) Không xác định vì $\theta$ tính theo radian

**Đáp án: B**

*Giải thích: Mô-men = $\tau = -\partial U/\partial\theta = -k\theta = -200\times\pi/12 \approx -52.4\,N\cdot m$. Dấu âm: lực đàn hồi chống lại sự lệch khỏi vị trí cân bằng (hướng về $\theta = 0$).*

## Câu 3

Điểm tham chiếu của thế năng (nơi $U = 0$) được chọn:

A) Bắt buộc phải là vô cực
B) Bắt buộc phải là mặt đất ($h = 0$)
C) Tùy ý — thay đổi mốc chỉ thêm hằng số vào $U$ và không ảnh hưởng đến $\Delta U$
D) Phải là điểm có $\vec{F} = 0$

**Đáp án: C**

*Giải thích: Thế năng xác định đến hằng số cộng. Vì bảo toàn năng lượng và lực ($\vec{F} = -\nabla U$) chỉ phụ thuộc $\Delta U$ và $\nabla U$ (không phụ thuộc hằng số cộng), mốc thế năng hoàn toàn tùy ý. Thực tế: thường chọn $U = 0$ tại mặt đất (trọng lực) hay vô cực (hấp dẫn) cho tiện tính toán.*

## Câu 4 — Tự Luận

Trong thiết bị đo lực nano-Newton (dùng trong kiểm tra chip bán dẫn), đầu đo cantilever có hằng số lò xo $k = 0.1\,N/m$. Khi đầu đo tiếp xúc bề mặt và bị lệch $\delta = 50\,nm = 50\times10^{-9}\,m$.

(a) Tính thế năng đàn hồi tích trữ.
(b) Tính lực tiếp xúc tác dụng lên bề mặt.
(c) Lực từ của cantilever có phải lực bảo toàn không? Giải thích theo quan điểm thế năng.

*Gợi ý: (a) $U = \frac{1}{2}k\delta^2$; (b) $F = k\delta$; (c) lực đàn hồi có curl = 0, có thế năng $U(\delta)$ — là lực bảo toàn*

```json
{
  "quiz_id": 5418,
  "questions": [
    {"id": 1, "answer": "B", "concept": "điều kiện lực bảo toàn: curl = 0, kiểm tra 3 phương trình"},
    {"id": 2, "answer": "B", "concept": "mô-men đàn hồi = -dU/dθ = -kθ"},
    {"id": 3, "answer": "C", "concept": "mốc thế năng tùy ý - chỉ ΔU mới có ý nghĩa"}
  ]
}
```


## Quiz Questions

**Q1:** No question text

**Correct:** B

**Q2:** No question text

**Correct:** B

**Q3:** No question text

**Correct:** C


---
*Exported from Feynman Bot*
