---
lesson_id: 5388
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:03.820812+00:00"
content_hash: 459bc5c59708
chapter_number: 11
chapter_title: Chapter 11
section_number: 5
section_title: 11–4Vectors
---
# ## Quiz: Phân tích Vectơ

*Source: Chapter 11 - Chapter 11 (Section 5) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_11.html)*

## Quiz: Phân tích Vectơ

**Câu 1.** Một vectơ lực $\mathbf{F} = (3, 4, 0)$ N. Độ lớn của lực là:

A. 7 N
B. 5 N
C. 3.5 N
D. 25 N

**Đáp án: B** — $|\mathbf{F}| = \sqrt{3^2 + 4^2 + 0^2} = \sqrt{9+16} = \sqrt{25} = 5$ N. Độ dài vectơ bất biến dưới phép xoay trục.

---

**Câu 2.** Sensor đo lực đặt theo hướng $\hat{n} = (0.8, 0.6, 0)$. Lực thực tác dụng $\mathbf{F} = (10, 0, 0)$ N. Số đọc của sensor là:

A. 10 N
B. 6 N
C. 8 N
D. 0 N

**Đáp án: C** — Số đọc = $\mathbf{F}\cdot\hat{n} = 10\times0.8 + 0\times0.6 = 8$ N. Sensor chỉ đo hình chiếu của lực lên hướng nhạy của nó.

---

**Câu 3.** Cross product $\mathbf{a}\times\mathbf{b}$:

A. Là một scalar bất biến
B. Là một vectơ vuông góc với cả $\mathbf{a}$ và $\mathbf{b}$
C. Bằng $\mathbf{b}\times\mathbf{a}$ (giao hoán)
D. Luôn bằng zero nếu cả hai trong mặt phẳng $xy$

**Đáp án: B** — Cross product tạo vectơ mới vuông góc với mặt phẳng chứa hai vectơ gốc. Không giao hoán: $\mathbf{a}\times\mathbf{b} = -(\mathbf{b}\times\mathbf{a})$.

---

**Câu 4 (Tự luận).** Trong hệ thống đo lực 6 bậc tự do (6-axis force/torque sensor), sensor đo 6 thành phần $(F_x, F_y, F_z, \tau_x, \tau_y, \tau_z)$ trong frame sensor. Khi gắn sensor vào đầu robot theo một góc xoay, bộ điều khiển cần chuyển đổi các giá trị đo sang frame robot. Mô tả phép toán vectơ nào cần thực hiện và tại sao cần thiết.

**Gợi ý đáp án:** Cần nhân vectơ lực $\mathbf{F}_s$ và mô-men $\mathbf{\tau}_s$ trong frame sensor với ma trận xoay $R$ (rotation matrix $3\times3$): $\mathbf{F}_r = R\mathbf{F}_s$, $\mathbf{\tau}_r = R\mathbf{\tau}_s$. Phép nhân ma trận này thực hiện đúng quy tắc biến đổi vectơ — bảo đảm lực vật lý được biểu diễn đúng trong frame robot để bộ điều khiển tính toán đúng. Không thực hiện sẽ dẫn đến bộ điều khiển "thấy" lực sai hướng, gây mất ổn định.

```json
{
  "questions": [
    {"id": "q1", "type": "mcq", "question": "Vectơ lực F=(3,4,0) N. Độ lớn?", "options": ["A. 7 N", "B. 5 N", "C. 3.5 N", "D. 25 N"], "answer": "B", "explanation": "|F| = sqrt(9+16) = 5 N. Độ dài vectơ bất biến khi xoay trục."},
    {"id": "q2", "type": "mcq", "question": "Sensor hướng n=(0.8,0.6,0), lực F=(10,0,0) N. Số đọc?", "options": ["A. 10 N", "B. 6 N", "C. 8 N", "D. 0 N"], "answer": "C", "explanation": "F·n = 10×0.8 = 8 N. Sensor đo hình chiếu lực lên hướng nhạy."},
    {"id": "q3", "type": "mcq", "question": "Cross product a×b là:", "options": ["A. Scalar bất biến", "B. Vectơ vuông góc với a và b", "C. Bằng b×a", "D. Luôn zero nếu trong mặt phẳng xy"], "answer": "B", "explanation": "Cross product tạo vectơ ⊥ với mặt phẳng chứa hai vectơ. Phản giao hoán: a×b = -(b×a)."},
    {"id": "q4", "type": "open", "question": "Sensor lực 6-DOF gắn vào đầu robot theo góc xoay. Phép toán vectơ nào cần để chuyển đổi sang frame robot?", "sample_answer": "Nhân với ma trận xoay R: F_r = R·F_s, τ_r = R·τ_s. Bảo đảm vectơ biến đổi đúng quy tắc — thiếu sẽ gây bộ điều khiển thấy lực sai hướng."}
  ]
}
```


## Quiz Questions

**Q1:** Vectơ lực F=(3,4,0) N. Độ lớn?
- A) A. 7 N
- B) B. 5 N
- C) C. 3.5 N
- D) D. 25 N

**Correct:** B

**Explanation:** |F| = sqrt(9+16) = 5 N. Độ dài vectơ bất biến khi xoay trục.

**Q2:** Sensor hướng n=(0.8,0.6,0), lực F=(10,0,0) N. Số đọc?
- A) A. 10 N
- B) B. 6 N
- C) C. 8 N
- D) D. 0 N

**Correct:** C

**Explanation:** F·n = 10×0.8 = 8 N. Sensor đo hình chiếu lực lên hướng nhạy.

**Q3:** Cross product a×b là:
- A) A. Scalar bất biến
- B) B. Vectơ vuông góc với a và b
- C) C. Bằng b×a
- D) D. Luôn zero nếu trong mặt phẳng xy

**Correct:** B

**Explanation:** Cross product tạo vectơ ⊥ với mặt phẳng chứa hai vectơ. Phản giao hoán: a×b = -(b×a).

**Q4:** Sensor lực 6-DOF gắn vào đầu robot theo góc xoay. Phép toán vectơ nào cần để chuyển đổi sang frame robot?

**Correct:** N/A


---
*Exported from Feynman Bot*
