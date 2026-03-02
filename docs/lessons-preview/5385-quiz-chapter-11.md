---
lesson_id: 5385
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-02T15:10:28.074989+00:00"
content_hash: 7e83d5482526
chapter_number: 11
chapter_title: Chapter 11
section_number: 1
section_title: 11Vectors
---
# ## Quiz: Đối xứng Định luật Vật lý và Vectơ

*Source: Chapter 11 - Chapter 11 (Section 1) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_11.html)*

## Quiz: Đối xứng Định luật Vật lý và Vectơ

**Câu 1.** Tích vô hướng $\mathbf{a}\cdot\mathbf{b}$ có tính chất đặc biệt nào so với các thành phần riêng lẻ $a_x, a_y$?

A. Nó luôn dương
B. Nó bất biến dưới phép xoay hệ tọa độ
C. Nó luôn bằng 0 nếu hai vectơ vuông góc với trục $z$
D. Nó thay đổi khi ta đổi đơn vị đo

**Đáp án: B** — Tích vô hướng là một vô hướng (scalar), giá trị không thay đổi khi xoay hệ tọa độ. Đây là lý do nó được dùng để tính các đại lượng vật lý không phụ thuộc hướng nhìn (như công, năng lượng).

---

**Câu 2.** Phương trình $m\mathbf{a} = \mathbf{F}$ là phương trình vectơ. Điều này có nghĩa là:

A. Chỉ đúng khi lực hướng theo trục $x$
B. Tương đương với ba phương trình vô hướng cho các thành phần $x$, $y$, $z$
C. Chỉ đúng trong hệ tọa độ Cartesian
D. Không thể áp dụng khi xoay hệ tọa độ

**Đáp án: B** — Một phương trình vectơ tương đương ba phương trình vô hướng cho từng thành phần. Nó đúng trong mọi hệ tọa độ vì cả $\mathbf{a}$ và $\mathbf{F}$ đều là vectơ (biến đổi cùng quy tắc).

---

**Câu 3.** Định nghĩa đúng nhất của đối xứng theo Weyl trong vật lý là:

A. Hình dạng bên trái giống bên phải
B. Có thể thực hiện một phép biến đổi mà hệ thống không thay đổi
C. Định luật vật lý giống nhau ở mọi vị trí trong vũ trụ
D. Phương trình toán học có cùng số hạng ở hai vế

**Đáp án: B** — Weyl định nghĩa đối xứng là bất biến dưới phép biến đổi. Đối xứng tịnh tiến (câu C) là một trường hợp đặc biệt của định nghĩa tổng quát hơn này.

---

**Câu 4 (Tự luận).** Trong hệ robot Delta 3 cánh tay, khi lập trình quỹ đạo đầu công tác (end-effector), phần mềm phải chuyển đổi tọa độ giữa nhiều frame (base frame, tool frame, world frame). Giải thích tại sao việc biểu diễn vị trí và lực bằng vectơ (kết hợp với ma trận xoay $R$) là cần thiết, và điều gì xảy ra nếu lập trình nhầm frame?

**Gợi ý đáp án:** Vectơ vị trí $\mathbf{r}$ và lực $\mathbf{F}$ của end-effector phải được biến đổi giữa các frame bằng ma trận xoay $R$: $\mathbf{r}' = R\mathbf{r}$. Điều này đảm bảo thực thể vật lý (vị trí thực trong không gian) không thay đổi dù biểu diễn bằng tọa độ nào. Nếu lập trình nhầm frame (ví dụ dùng tọa độ tool frame như thể là world frame), robot sẽ di chuyển sai hướng — sai số tăng theo góc lệch giữa hai frame, có thể gây va chạm hoặc hỏng sản phẩm.

```json
{
  "questions": [
    {"id": "q1", "type": "mcq", "question": "Tích vô hướng a·b có tính chất đặc biệt nào?", "options": ["A. Luôn dương", "B. Bất biến dưới phép xoay hệ tọa độ", "C. Luôn bằng 0 nếu vuông góc với trục z", "D. Thay đổi khi đổi đơn vị"], "answer": "B", "explanation": "Tích vô hướng là scalar — không đổi khi xoay hệ tọa độ. Dùng để tính đại lượng vật lý không phụ thuộc góc nhìn."},
    {"id": "q2", "type": "mcq", "question": "Phương trình vectơ ma=F tương đương với:", "options": ["A. Chỉ đúng theo trục x", "B. Ba phương trình vô hướng cho x, y, z", "C. Chỉ đúng trong Cartesian", "D. Không áp dụng khi xoay trục"], "answer": "B", "explanation": "Một phương trình vectơ = ba phương trình vô hướng, đúng trong mọi hệ tọa độ."},
    {"id": "q3", "type": "mcq", "question": "Định nghĩa đối xứng theo Weyl:", "options": ["A. Trái = phải", "B. Bất biến dưới phép biến đổi", "C. Định luật giống nhau mọi nơi", "D. Phương trình có số hạng bằng nhau"], "answer": "B", "explanation": "Weyl: đối xứng = bất biến dưới phép biến đổi. Đối xứng tịnh tiến là trường hợp riêng."},
    {"id": "q4", "type": "open", "question": "Tại sao biểu diễn vị trí/lực bằng vectơ + ma trận xoay là cần thiết trong lập trình robot đa frame? Điều gì xảy ra nếu nhầm frame?", "sample_answer": "Vectơ biến đổi đúng quy tắc r'=Rr khi chuyển frame — thực thể vật lý không đổi. Nhầm frame → robot di chuyển sai hướng, sai số theo góc lệch, có thể gây va chạm."}
  ]
}
```


## Quiz Questions

**Q1:** Tích vô hướng a·b có tính chất đặc biệt nào?
- A) A. Luôn dương
- B) B. Bất biến dưới phép xoay hệ tọa độ
- C) C. Luôn bằng 0 nếu vuông góc với trục z
- D) D. Thay đổi khi đổi đơn vị

**Correct:** B

**Explanation:** Tích vô hướng là scalar — không đổi khi xoay hệ tọa độ. Dùng để tính đại lượng vật lý không phụ thuộc góc nhìn.

**Q2:** Phương trình vectơ ma=F tương đương với:
- A) A. Chỉ đúng theo trục x
- B) B. Ba phương trình vô hướng cho x, y, z
- C) C. Chỉ đúng trong Cartesian
- D) D. Không áp dụng khi xoay trục

**Correct:** B

**Explanation:** Một phương trình vectơ = ba phương trình vô hướng, đúng trong mọi hệ tọa độ.

**Q3:** Định nghĩa đối xứng theo Weyl:
- A) A. Trái = phải
- B) B. Bất biến dưới phép biến đổi
- C) C. Định luật giống nhau mọi nơi
- D) D. Phương trình có số hạng bằng nhau

**Correct:** B

**Explanation:** Weyl: đối xứng = bất biến dưới phép biến đổi. Đối xứng tịnh tiến là trường hợp riêng.

**Q4:** Tại sao biểu diễn vị trí/lực bằng vectơ + ma trận xoay là cần thiết trong lập trình robot đa frame? Điều gì xảy ra nếu nhầm frame?

**Correct:** N/A


---
*Exported from Feynman Bot*
