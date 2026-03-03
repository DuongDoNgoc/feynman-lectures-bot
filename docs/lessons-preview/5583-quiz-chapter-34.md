---
lesson_id: 5583
lesson_type: quiz
approval_status: pending
exported_at: "2026-03-03T15:33:08.540874+00:00"
content_hash: 1d65afb55d8c
chapter_number: 34
chapter_title: Chapter 34
section_number: 4
section_title: 34–3Synchrotron radiation
---
# ## Quiz: Bức Xạ Synchrotron và Động Học Electron Trong Từ Trường

*Source: Chapter 34 - Chapter 34 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_34.html)*

## Quiz: Bức Xạ Synchrotron và Động Học Electron Trong Từ Trường

---

**Câu 1.** Tại sao electron chuyển động trong từ trường đều đi theo đường tròn mà tốc độ không thay đổi?

A. Từ trường truyền năng lượng cho electron để duy trì tốc độ  
B. Lực Lorentz luôn vuông góc với vận tốc nên không thực hiện công, chỉ thay đổi hướng  
C. Từ trường triệt tiêu lực cản không khí trong buồng chân không  
D. Electron di chuyển theo đường xoắn ốc, không phải đường tròn  

**Đáp án: B**  
Giải thích: $\mathbf{F} = q\mathbf{v} 	imes \mathbf{B}$ luôn vuông góc với $\mathbf{v}$ → công $dW = \mathbf{F}\cdot d\mathbf{s} = 0$ → $|\mathbf{v}| = 	ext{const}$. Tốc độ không đổi nhưng hướng liên tục thay đổi → chuyển động tròn đều.

---

**Câu 2.** Trong synchrotron, electron năng lượng $E$ (GeV) chuyển động trên đường tròn bán kính $R$. Bức xạ phát ra tập trung trong góc:

A. $\Delta	heta = \gamma = E/(m_e c^2)$ (radian)  
B. $\Delta	heta = 1/\gamma = m_e c^2/E$ (radian)  
C. $\Delta	heta = \pi/2$ (90° mọi hướng ngang)  
D. $\Delta	heta = \lambda/R$ (phụ thuộc bước sóng)  

**Đáp án: B**  
Giải thích: Do aberration relativistic, bức xạ tập trung trong góc $\Delta	heta pprox 1/\gamma \ll 1$. Càng năng lượng cao ($\gamma$ lớn), chùm tia càng hẹp.

---

**Câu 3.** Quan hệ giữa động lượng electron $p$, điện tích $q$, từ trường $B$ và bán kính quỹ đạo $R$ là:

A. $p = qB/R$  
B. $p = qBR$  
C. $p = q^2BR$  
D. $p = qB^2R$  

**Đáp án: B**  
Giải thích: Từ cân bằng $qvB = mv^2/R$ (non-relativistic) tổng quát hóa thành $p = qBR$ cho cả trường hợp tương đối tính. Đây là quan hệ thiết kế cơ bản (rigidity) trong máy gia tốc.

---

**Câu 4 (Tự luận).** Trong thiết kế hệ thống dẫn đường quán tính (INS) cho vũ khí, con quay hồi chuyển MEMS được chế tạo bằng phương pháp lithography từ bức xạ synchrotron. Tại sao bức xạ synchrotron cho phép chế tạo cấu trúc MEMS (flexure, beam) với dung sai tốt hơn UV lithography thông thường? Liệt kê ít nhất 2 đặc tính của bức xạ synchrotron giải thích điều này.

**Gợi ý trả lời:**  
(1) **Bước sóng ngắn (tia X)**: Bước sóng tới hạn synchrotron $\sim 1$–$10$ Å, nhỏ hơn nhiều so với UV ($\sim 200$–$400$ nm). Phân giải lithography tỉ lệ với $\lambda$ → tia X cho cấu trúc nhỏ hơn nhiều, dưới 100 nm. (2) **Chùm tia song song cao**: Góc phân kỳ $\Delta	heta \sim 1/\gamma \ll 1$ mrad → ít penumbral blur ở rìa hình chiếu mặt nạ (mask) → cạnh sắc nét, dung sai tốt hơn. (3) **Độ sáng (brightness) cao**: Flux lớn → thời gian phơi ngắn → ít drift nhiệt trong quá trình exposure → ổn định hơn. (4) **Đâm xuyên sâu trong vật liệu dày**: Tia X xuyên sâu vào resist dày → chế tạo cấu trúc 3D aspect ratio cao (LIGA process) — quan trọng cho flexure gyroscope.

---

```json
{
  "questions": [
    {"id": "q1", "type": "mcq", "question": "Tại sao electron trong từ trường đều đi theo đường tròn mà tốc độ không thay đổi?", "options": ["A. Từ trường cấp năng lượng duy trì tốc độ", "B. Lực Lorentz vuông góc vận tốc nên không thực hiện công, chỉ đổi hướng", "C. Từ trường triệt tiêu lực cản không khí", "D. Electron đi theo đường xoắn ốc"], "answer": "B", "explanation": "F = qv×B luôn ⊥ v → dW = 0 → |v| = const, chỉ hướng thay đổi → chuyển động tròn đều."},
    {"id": "q2", "type": "mcq", "question": "Bức xạ synchrotron từ electron năng lượng E tập trung trong góc bao nhiêu?", "options": ["A. Δθ = γ = E/(m_e c²)", "B. Δθ = 1/γ = m_e c²/E (radian)", "C. Δθ = π/2", "D. Δθ = λ/R"], "answer": "B", "explanation": "Aberration relativistic nén bức xạ vào góc Δθ ≈ 1/γ. Năng lượng càng cao → γ lớn → chùm càng hẹp."},
    {"id": "q3", "type": "mcq", "question": "Quan hệ giữa động lượng electron p, điện tích q, từ trường B và bán kính R là gì?", "options": ["A. p = qB/R", "B. p = qBR", "C. p = q²BR", "D. p = qB²R"], "answer": "B", "explanation": "p = qBR — quan hệ magnetic rigidity, áp dụng cho cả trường hợp tương đối tính, là công thức thiết kế cơ bản trong máy gia tốc."},
    {"id": "q4", "type": "open", "question": "Tại sao bức xạ synchrotron cho phép chế tạo cấu trúc MEMS (flexure gyroscope) với dung sai tốt hơn UV lithography? Liệt kê ít nhất 2 đặc tính.", "sample_answer": "(1) Bước sóng tia X ngắn → phân giải cao hơn UV; (2) Chùm song song (Δθ~1/γ) → cạnh sắc nét; (3) Brightness cao → thời gian phơi ngắn, ít drift; (4) Xuyên sâu → LIGA 3D aspect ratio cao."}
  ]
}
```


## Quiz Questions

**Q1:** Tại sao electron trong từ trường đều đi theo đường tròn mà tốc độ không thay đổi?
- A) A. Từ trường cấp năng lượng duy trì tốc độ
- B) B. Lực Lorentz vuông góc vận tốc nên không thực hiện công, chỉ đổi hướng
- C) C. Từ trường triệt tiêu lực cản không khí
- D) D. Electron đi theo đường xoắn ốc

**Correct:** B

**Explanation:** F = qv×B luôn ⊥ v → dW = 0 → |v| = const, chỉ hướng thay đổi → chuyển động tròn đều.

**Q2:** Bức xạ synchrotron từ electron năng lượng E tập trung trong góc bao nhiêu?
- A) A. Δθ = γ = E/(m_e c²)
- B) B. Δθ = 1/γ = m_e c²/E (radian)
- C) C. Δθ = π/2
- D) D. Δθ = λ/R

**Correct:** B

**Explanation:** Aberration relativistic nén bức xạ vào góc Δθ ≈ 1/γ. Năng lượng càng cao → γ lớn → chùm càng hẹp.

**Q3:** Quan hệ giữa động lượng electron p, điện tích q, từ trường B và bán kính R là gì?
- A) A. p = qB/R
- B) B. p = qBR
- C) C. p = q²BR
- D) D. p = qB²R

**Correct:** B

**Explanation:** p = qBR — quan hệ magnetic rigidity, áp dụng cho cả trường hợp tương đối tính, là công thức thiết kế cơ bản trong máy gia tốc.

**Q4:** Tại sao bức xạ synchrotron cho phép chế tạo cấu trúc MEMS (flexure gyroscope) với dung sai tốt hơn UV lithography? Liệt kê ít nhất 2 đặc tính.

**Correct:** N/A


---
*Exported from Feynman Bot*
