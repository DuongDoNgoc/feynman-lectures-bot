---
lesson_id: 5391
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:03.911627+00:00"
content_hash: 16859bf8e25e
chapter_number: 11
chapter_title: Chapter 11
section_number: 7
section_title: 11–6Newton’s laws in vector notation
---
# ## Quiz: Định luật Newton Dạng Vectơ và Gia tốc

*Source: Chapter 11 - Chapter 11 (Section 7) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_11.html)*

## Quiz: Định luật Newton Dạng Vectơ và Gia tốc

**Câu 1.** Một vật chuyển động trên đường tròn bán kính $R = 2$ m với tốc độ không đổi $v = 4$ m/s. Độ lớn gia tốc của vật là:

A. 0 m/s²
B. 2 m/s²
C. 8 m/s²
D. 16 m/s²

**Đáp án: C** — $a_\perp = v^2/R = 16/2 = 8$ m/s². Tốc độ không đổi nên $a_\parallel = 0$, nhưng hướng thay đổi nên $a_\perp \neq 0$.

---

**Câu 2.** Phương trình $m\mathbf{a} = \mathbf{F}$ là phương trình vectơ. So sánh với ba phương trình vô hướng, ưu điểm chính là:

A. Dễ giải hơn về mặt toán học
B. Đúng trong mọi hệ tọa độ, không cần viết lại khi đổi frame
C. Chỉ cần một con số mô tả lực
D. Không cần biết hướng của lực

**Đáp án: B** — Phương trình vectơ không phụ thuộc hệ tọa độ. Dù dùng Cartesian, cực, hay hình trụ, phương trình có cùng dạng.

---

**Câu 3.** Gia tốc pháp tuyến (centripetal) $a_\perp = v^2/R$ có hướng:

A. Cùng chiều vận tốc
B. Ngược chiều vận tốc
C. Hướng vào tâm cong quỹ đạo
D. Vuông góc với mặt phẳng quỹ đạo

**Đáp án: C** — Gia tốc pháp tuyến luôn hướng vào tâm cong (centripetal = hướng tâm). Nó là nguyên nhân thay đổi hướng chuyển động.

---

**Câu 4 (Tự luận).** Trong hệ thống điều khiển CNC 5 trục, đầu công tác chạy đường tròn bán kính $R = 50$ mm với tốc độ $F = 3000$ mm/min. Tính gia tốc hướng tâm và giải thích tại sao bộ điều khiển CNC hiện đại cần tính trước (feed-forward) gia tốc này để giảm sai số bám.

**Gợi ý đáp án:**
$v = 3000/60 = 50$ mm/s $= 0.05$ m/s

$a_\perp = v^2/R = (0.05)^2/0.05 = 0.05$ m/s² = 50 mm/s²

Lực cần thiết cho khối lượng đầu 2 kg: $F = 2 \times 0.05 = 0.1$ N

Nếu không có feed-forward, bộ điều khiển phản hồi (PID thuần) cần sai số vị trí mới tạo ra lực điều chỉnh → sai số bám tỷ lệ với $v^2/R$. Feed-forward tính trước $m\mathbf{a}$ từ quỹ đạo rồi cộng vào tín hiệu điều khiển, loại bỏ sai số hệ thống khi chạy đường cong.

```json
{
  "questions": [
    {"id": "q1", "type": "mcq", "question": "Vật chuyển động tròn R=2m, v=4m/s không đổi. Gia tốc?", "options": ["A. 0 m/s²", "B. 2 m/s²", "C. 8 m/s²", "D. 16 m/s²"], "answer": "C", "explanation": "a_perp = v²/R = 16/2 = 8 m/s². Tốc độ không đổi nhưng hướng đổi → gia tốc hướng tâm."},
    {"id": "q2", "type": "mcq", "question": "Ưu điểm chính của phương trình vectơ ma=F so với ba phương trình vô hướng?", "options": ["A. Dễ giải hơn", "B. Đúng mọi hệ tọa độ không cần viết lại", "C. Chỉ cần một số", "D. Không cần biết hướng lực"], "answer": "B", "explanation": "Phương trình vectơ bất biến dưới phép xoay trục — đúng trong mọi hệ tọa độ."},
    {"id": "q3", "type": "mcq", "question": "Gia tốc pháp tuyến a_perp = v²/R có hướng:", "options": ["A. Cùng chiều vận tốc", "B. Ngược chiều vận tốc", "C. Hướng vào tâm cong", "D. Vuông góc mặt phẳng quỹ đạo"], "answer": "C", "explanation": "Centripetal = hướng tâm. Đây là nguyên nhân thay đổi hướng chuyển động."},
    {"id": "q4", "type": "open", "question": "CNC 5 trục: R=50mm, F=3000mm/min. Tính a_perp và giải thích tại sao cần feed-forward gia tốc.", "sample_answer": "v=50mm/s, a=v²/R=50mm/s². Feed-forward tính trước ma từ quỹ đạo, cộng vào lệnh điều khiển, loại bỏ sai số bám hệ thống khi đường cong."}
  ]
}
```


## Quiz Questions

**Q1:** Vật chuyển động tròn R=2m, v=4m/s không đổi. Gia tốc?
- A) A. 0 m/s²
- B) B. 2 m/s²
- C) C. 8 m/s²
- D) D. 16 m/s²

**Correct:** C

**Explanation:** a_perp = v²/R = 16/2 = 8 m/s². Tốc độ không đổi nhưng hướng đổi → gia tốc hướng tâm.

**Q2:** Ưu điểm chính của phương trình vectơ ma=F so với ba phương trình vô hướng?
- A) A. Dễ giải hơn
- B) B. Đúng mọi hệ tọa độ không cần viết lại
- C) C. Chỉ cần một số
- D) D. Không cần biết hướng lực

**Correct:** B

**Explanation:** Phương trình vectơ bất biến dưới phép xoay trục — đúng trong mọi hệ tọa độ.

**Q3:** Gia tốc pháp tuyến a_perp = v²/R có hướng:
- A) A. Cùng chiều vận tốc
- B) B. Ngược chiều vận tốc
- C) C. Hướng vào tâm cong
- D) D. Vuông góc mặt phẳng quỹ đạo

**Correct:** C

**Explanation:** Centripetal = hướng tâm. Đây là nguyên nhân thay đổi hướng chuyển động.

**Q4:** CNC 5 trục: R=50mm, F=3000mm/min. Tính a_perp và giải thích tại sao cần feed-forward gia tốc.

**Correct:** N/A


---
*Exported from Feynman Bot*
