---
lesson_id: 5373
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-02T15:10:27.819169+00:00"
content_hash: 3d9a4f9517d7
chapter_number: 9
chapter_title: Chapter 9
section_number: 6
section_title: 9–5Meaning of the dynamical equations
---
# ## Quiz: Giải Phương Trình Chuyển Động Số

*Source: Chapter 9 - Chapter 9 (Section 6) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_09.html)*

## Quiz: Giải Phương Trình Chuyển Động Số

**Câu 1.** Áp dụng phương pháp Euler cho $\ddot{x} = -x$ với $x(0) = 1$, $v(0) = 0$, bước $h = 0.1\,\text{s}$. Giá trị $x$ sau bước đầu tiên ($t = 0.1\,\text{s}$) là:

A. $x = 1.0$
B. $x = 0.99$
C. $x = 0.9$
D. $x = 1.1$

---

**Câu 2.** Điều kiện ổn định của phương pháp Euler cho hệ dao động $\ddot{x} = -\omega_n^2 x$ là:

A. $h < 1/\omega_n$
B. $h < 2/\omega_n$
C. $h < \pi/\omega_n$
D. $h < \omega_n/2$

---

**Câu 3.** Trong phương pháp leap-frog (Verlet), vận tốc và vị trí được tính:

A. Cùng tại một thời điểm
B. Xen kẽ nhau, lệch nửa bước thời gian
C. Vận tốc trễ một bước so với vị trí
D. Vị trí trễ một bước so với vận tốc

---

**Câu 4 (Tự luận).** Bạn đang mô phỏng chuyển động của đầu đo trong máy đo tọa độ CMM. Hệ có độ cứng $k = 10^6\,\text{N/m}$, khối lượng $m = 1\,\text{kg}$. Hãy tính bước thời gian tối đa cho phép (theo tiêu chí 20 bước/chu kỳ) và giải thích tại sao chọn bước thời gian quá lớn gây ra vấn đề trong mô phỏng.

---

```json
{"questions": [
  {"id": "q1", "type": "mcq", "question": "Euler cho ẍ = -x, x(0)=1, v(0)=0, h=0.1s. Giá trị x sau bước đầu tiên là bao nhiêu?", "options": ["A. x = 1.0", "B. x = 0.99", "C. x = 0.9", "D. x = 1.1"], "answer": "A", "explanation": "Bước 1: v₁ = v₀ + a₀·h = 0 + (-x₀)·h = 0 + (-1)(0.1) = -0.1. x₁ = x₀ + v₀·h = 1 + 0×0.1 = 1.0. Vị trí chưa thay đổi sau bước đầu vì v₀=0 — nhưng vận tốc đã bắt đầu âm."},
  {"id": "q2", "type": "mcq", "question": "Điều kiện ổn định Euler cho hệ dao động ẍ = -ωn²x là gì?", "options": ["A. h < 1/ωn", "B. h < 2/ωn", "C. h < π/ωn", "D. h < ωn/2"], "answer": "B", "explanation": "Phân tích ổn định Euler cho phương trình tuyến tính: eigenvalue λ = ±iωn. Điều kiện |1 + hλ| ≤ 1 cho complex eigenvalue → h ≤ 2/|Re(λ)| = 2/ωn."},
  {"id": "q3", "type": "mcq", "question": "Trong phương pháp leap-frog (Verlet), vận tốc và vị trí được tính như thế nào?", "options": ["A. Cùng tại một thời điểm", "B. Xen kẽ nhau, lệch nửa bước thời gian", "C. Vận tốc trễ một bước so với vị trí", "D. Vị trí trễ một bước so với vận tốc"], "answer": "B", "explanation": "Leap-frog: vị trí tính tại t_n, vận tốc tính tại t_{n+1/2} = t_n + h/2. Cách bố trí lệch pha này cho phép sơ đồ bậc 2 trong đó năng lượng được bảo toàn tốt hơn Euler."},
  {"id": "q4", "type": "open", "question": "CMM: k=10⁶ N/m, m=1 kg. Tính bước thời gian tối đa (20 bước/chu kỳ) và giải thích hậu quả khi bước quá lớn.", "sample_answer": "ωn = √(k/m) = √(10⁶) = 1000 rad/s → fn = 159 Hz → T = 6.28 ms. Bước tối đa: h_max = T/20 = 6.28/20 = 0.314 ms. Khi h > 2/ωn = 2/1000 = 2 ms: phương pháp Euler mất ổn định — biên độ dao động tăng theo thời gian thay vì tắt dần. Ngay cả khi h < 2ms nhưng > 0.314ms: sai số lớn — đường cong dao động bị méo, biên độ và pha không đúng. Hậu quả thực tế: mô phỏng cho thấy đầu đo 'rung tắt' khi thực tế nó tiếp tục dao động, dẫn đến quyết định sai về thời gian chờ ổn định trước khi đo."}
]}
```



## Quiz Questions

**Q1:** Euler cho ẍ = -x, x(0)=1, v(0)=0, h=0.1s. Giá trị x sau bước đầu tiên là bao nhiêu?
- A) A. x = 1.0
- B) B. x = 0.99
- C) C. x = 0.9
- D) D. x = 1.1

**Correct:** A

**Explanation:** Bước 1: v₁ = v₀ + a₀·h = 0 + (-x₀)·h = 0 + (-1)(0.1) = -0.1. x₁ = x₀ + v₀·h = 1 + 0×0.1 = 1.0. Vị trí chưa thay đổi sau bước đầu vì v₀=0 — nhưng vận tốc đã bắt đầu âm.

**Q2:** Điều kiện ổn định Euler cho hệ dao động ẍ = -ωn²x là gì?
- A) A. h < 1/ωn
- B) B. h < 2/ωn
- C) C. h < π/ωn
- D) D. h < ωn/2

**Correct:** B

**Explanation:** Phân tích ổn định Euler cho phương trình tuyến tính: eigenvalue λ = ±iωn. Điều kiện |1 + hλ| ≤ 1 cho complex eigenvalue → h ≤ 2/|Re(λ)| = 2/ωn.

**Q3:** Trong phương pháp leap-frog (Verlet), vận tốc và vị trí được tính như thế nào?
- A) A. Cùng tại một thời điểm
- B) B. Xen kẽ nhau, lệch nửa bước thời gian
- C) C. Vận tốc trễ một bước so với vị trí
- D) D. Vị trí trễ một bước so với vận tốc

**Correct:** B

**Explanation:** Leap-frog: vị trí tính tại t_n, vận tốc tính tại t_{n+1/2} = t_n + h/2. Cách bố trí lệch pha này cho phép sơ đồ bậc 2 trong đó năng lượng được bảo toàn tốt hơn Euler.

**Q4:** CMM: k=10⁶ N/m, m=1 kg. Tính bước thời gian tối đa (20 bước/chu kỳ) và giải thích hậu quả khi bước quá lớn.

**Correct:** N/A


---
*Exported from Feynman Bot*
