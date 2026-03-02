---
lesson_id: 5400
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-02T15:10:28.465019+00:00"
content_hash: 43b1ca6d967c
chapter_number: 12
chapter_title: Chapter 12
section_number: 4
section_title: 12–3Molecular forces
---
# ## Quiz: Lực Phân Tử và Kết Dính

*Source: Chapter 12 - Chapter 12 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_12.html)*

## Quiz: Lực Phân Tử và Kết Dính

**Câu 1.** Định luật Hooke $F = -kx$ có nguồn gốc sâu xa từ:

A. Định luật Newton thứ ba
B. Tuyến tính hóa của lực phân tử phi tuyến quanh điểm cân bằng $r_0$
C. Định luật bảo toàn năng lượng
D. Lực van der Waals tỷ lệ $1/r^6$

**Đáp án: B** — Tại vị trí cân bằng $r_0$, lực phân tử = 0 và tuyến tính hóa quanh đó cho $F \approx -kx$. Đây là xấp xỉ tốt khi biến dạng $x \ll r_0$. Vượt giới hạn đàn hồi nghĩa là ra khỏi vùng tuyến tính.

---

**Câu 2.** Lực van der Waals giữa hai phân tử không phân cực (như O₂) xuất phát từ:

A. Lực Coulomb giữa ion dương và âm
B. Lưỡng cực vĩnh viễn của phân tử
C. Lưỡng cực tức thời ngẫu nhiên và lưỡng cực cảm ứng
D. Lực hạt nhân tầm ngắn

**Đáp án: C** — London dispersion: phân bố điện tử ngẫu nhiên tạo lưỡng cực tức thời → phân cực phân tử lân cận → lực hút. Phụ thuộc polarizability của phân tử.

---

**Câu 3.** Trong MEMS, "stiction" (static friction ở micro-scale) là vấn đề nghiêm trọng vì:

A. Ma sát Coulomb lớn hơn ở kích thước nhỏ
B. Lực van der Waals và lực mao dẫn tỷ lệ không thuận với khối lượng — càng nhỏ càng nguy hiểm hơn
C. MEMS không có đủ điện áp để vượt qua ma sát
D. Bề mặt MEMS không đủ phẳng

**Đáp án: B** — Khối lượng tỷ lệ $L^3$, lực van der Waals và mao dẫn tỷ lệ $L^2$ và $L$ → khi $L$ nhỏ, lực dính/trọng lực tăng → cấu trúc micro dễ bị "dán" vào đế hơn cấu trúc macro.

---

**Câu 4 (Tự luận).** Đầu đo tactile của CMM (ruby ball, $R = 1.5$ mm) hoạt động trong môi trường độ ẩm cao (80% RH). Giải thích tại sao cần kiểm soát độ ẩm hoặc tăng lực đo tối thiểu, và lực phân tử nào gây ra vấn đề này.

**Gợi ý đáp án:** Ở độ ẩm cao, nước ngưng tụ tại điểm tiếp xúc ruby-bề mặt (vì bán kính cong nhỏ → áp suất Laplace âm → hạ điểm sương cục bộ). Lực mao dẫn $F_{cap} = 2\gamma A\cos\theta/d$ xuất hiện, thêm vào lực tiếp xúc danh nghĩa. Khi tách đầu đo, lực mao dẫn "giữ" lại → lực tách thực tế > lực đặt vào → sai số vị trí tiếp xúc. Giải pháp: kiểm soát RH < 50%, hoặc tăng lực đo tối thiểu để lực mao dẫn chiếm phần trăm nhỏ, hoặc dùng đầu đo non-contact (laser, chromatic aberration).

```json
{
  "questions": [
    {"id": "q1", "type": "mcq", "question": "Định luật Hooke F=-kx có nguồn gốc từ:", "options": ["A. Định luật Newton III", "B. Tuyến tính hóa lực phân tử phi tuyến tại r₀", "C. Bảo toàn năng lượng", "D. Lực van der Waals 1/r⁶"], "answer": "B", "explanation": "Hooke là xấp xỉ tuyến tính của lực phân tử tại điểm cân bằng r₀. Đúng khi x << r₀."},
    {"id": "q2", "type": "mcq", "question": "Lực van der Waals giữa O₂ (không phân cực) từ:", "options": ["A. Lực Coulomb ion", "B. Lưỡng cực vĩnh viễn", "C. Lưỡng cực tức thời và cảm ứng", "D. Lực hạt nhân"], "answer": "C", "explanation": "London dispersion: lưỡng cực tức thời ngẫu nhiên → phân cực phân tử lân cận → hút. Phụ thuộc polarizability."},
    {"id": "q3", "type": "mcq", "question": "Stiction trong MEMS nguy hiểm vì:", "options": ["A. Ma sát Coulomb lớn hơn", "B. Lực dính/trọng lực tăng khi kích thước nhỏ", "C. Điện áp không đủ", "D. Bề mặt không phẳng"], "answer": "B", "explanation": "Lực vdW và mao dẫn ~ L², L; khối lượng ~ L³ → khi L nhỏ, lực dính/trọng lực tỷ số tăng."},
    {"id": "q4", "type": "open", "question": "CMM ruby ball R=1.5mm ở 80% RH. Tại sao cần kiểm soát độ ẩm? Lực phân tử nào gây vấn đề?", "sample_answer": "Nước ngưng tụ tại tiếp xúc → lực mao dẫn F_cap = 2γAcosθ/d thêm vào → sai số khi tách đầu đo. Giải pháp: RH < 50%, tăng lực đo tối thiểu, hoặc đầu đo non-contact."}
  ]
}
```


## Quiz Questions

**Q1:** Định luật Hooke F=-kx có nguồn gốc từ:
- A) A. Định luật Newton III
- B) B. Tuyến tính hóa lực phân tử phi tuyến tại r₀
- C) C. Bảo toàn năng lượng
- D) D. Lực van der Waals 1/r⁶

**Correct:** B

**Explanation:** Hooke là xấp xỉ tuyến tính của lực phân tử tại điểm cân bằng r₀. Đúng khi x << r₀.

**Q2:** Lực van der Waals giữa O₂ (không phân cực) từ:
- A) A. Lực Coulomb ion
- B) B. Lưỡng cực vĩnh viễn
- C) C. Lưỡng cực tức thời và cảm ứng
- D) D. Lực hạt nhân

**Correct:** C

**Explanation:** London dispersion: lưỡng cực tức thời ngẫu nhiên → phân cực phân tử lân cận → hút. Phụ thuộc polarizability.

**Q3:** Stiction trong MEMS nguy hiểm vì:
- A) A. Ma sát Coulomb lớn hơn
- B) B. Lực dính/trọng lực tăng khi kích thước nhỏ
- C) C. Điện áp không đủ
- D) D. Bề mặt không phẳng

**Correct:** B

**Explanation:** Lực vdW và mao dẫn ~ L², L; khối lượng ~ L³ → khi L nhỏ, lực dính/trọng lực tỷ số tăng.

**Q4:** CMM ruby ball R=1.5mm ở 80% RH. Tại sao cần kiểm soát độ ẩm? Lực phân tử nào gây vấn đề?

**Correct:** N/A


---
*Exported from Feynman Bot*
