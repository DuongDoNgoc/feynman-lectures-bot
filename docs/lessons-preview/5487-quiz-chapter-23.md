---
lesson_id: 5487
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:06.309116+00:00"
content_hash: ebbb12b7ae69
chapter_number: 23
chapter_title: Chapter 23
section_number: 2
section_title: 23–1Complex numbers and harmonic motion
---
# ## Quiz: Dao Động Cưỡng Bức và Số Phức

*Source: Chapter 23 - Chapter 23 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_23.html)*

## Quiz: Dao Động Cưỡng Bức và Số Phức

### Câu 1 (Trắc nghiệm)
Trong phân tích dao động cưỡng bức bằng phương pháp số phức, nếu lực ngoài được biểu diễn là $F = F_0 e^{i\omega t}$, thì dao động thực của hệ được xác định bằng:

A. Phần thực của nghiệm phức $x_{phức}$
B. Phần ảo của nghiệm phức $x_{phức}$
C. Môđun của nghiệm phức $|x_{phức}|$
D. Bình phương môđun $|x_{phức}|^2$

**Đáp án: A**
*Giải thích:* Khi lực tác dụng là phần thực của $F_0 e^{i\omega t}$, theo nguyên lý tuyến tính, dao động thực chính là phần thực của nghiệm phức $x = \hat{X} e^{i\omega t}$. Đây là nền tảng của phương pháp phasor trong phân tích dao động và mạch điện.

---

### Câu 2 (Trắc nghiệm)
Trên giản đồ Argand (mặt phẳng số phức), biên độ $A$ và góc pha $\phi$ của dao động $x = A\cos(\omega t + \phi)$ được biểu diễn như thế nào qua phasor $\hat{X}$?

A. $A$ là phần thực, $\phi$ là phần ảo của phasor
B. $A$ là môđun $|\hat{X}|$ và $\phi$ là argument (góc) của phasor $\hat{X} = A e^{i\phi}$
C. $A$ là phần ảo, $\phi$ là môđun của phasor
D. $A$ và $\phi$ không thể biểu diễn trên giản đồ Argand

**Đáp án: B**
*Giải thích:* Phasor $\hat{X} = A e^{i\phi} = A\cos\phi + iA\sin\phi$. Môđun $|\hat{X}| = A$ là biên độ dao động; argument $\arg(\hat{X}) = \phi$ là góc pha. Cách biểu diễn hình học này rất hữu ích trong kỹ thuật điện tử và tự động hóa.

---

### Câu 3 (Trắc nghiệm)
Ở tần số cộng hưởng $\omega = \omega_0$, biên độ dao động cưỡng bức của hệ *có lực cản* $\gamma \neq 0$ bằng:

A. Vô cùng lớn, tiến đến vô cực
B. $A = F_0 / (m\gamma\omega_0)$, hữu hạn và tỉ lệ nghịch với hệ số cản $\gamma$
C. Bằng đúng biên độ dao động tự do ban đầu
D. Bằng không vì hai thành phần dao động triệt tiêu nhau

**Đáp án: B**
*Giải thích:* Tại $\omega = \omega_0$, phần tử kháng của lò xo và quán tính triệt tiêu nhau, chỉ còn lại lực cản $m\gamma\omega_0$, nên $A = F_0/(m\gamma\omega_0)$. Chỉ khi $\gamma \to 0$ (không ma sát hoàn toàn) thì $A \to \infty$.

---

### Câu 4 (Tự luận mở)
**Câu hỏi:** Với vai trò là kỹ sư cơ điện tử thiết kế hệ thống điều khiển chính xác ở mức micrometer, bạn cần cách ly thiết bị đo khỏi rung động môi trường từ bơm và động cơ lân cận. Hãy giải thích tại sao việc hiểu biên độ phức và góc pha của dao động cưỡng bức lại quan trọng khi thiết kế bộ cách ly rung động (vibration isolation mount). Đặc biệt, hiện tượng cộng hưởng có thể gây ra nguy cơ gì cho độ chính xác đo lường?

**Gợi ý trả lời mẫu:** Biên độ phức và pha xác định không chỉ mức độ rung động truyền qua mà còn độ trễ (phase lag) giữa lực kích thích và phản ứng của cơ cấu định vị. Khi tần số nguồn rung ngoài gần tần số tự nhiên $\omega_0$ của bàn đo hoặc cơ cấu, hiện tượng cộng hưởng khuếch đại biên độ dao động lên hàng chục lần (hệ số $Q$), khiến sai số định vị vượt xa ngưỡng cho phép (vài micrometer). Hiểu hàm truyền độ rung (transmissibility) $T(\omega)$ giúp chọn đế cách ly với tần số riêng đủ thấp sao cho $T < 1$ ở toàn bộ dải tần hoạt động thực tế của hệ thống.

```json
{
  "questions": [
    {"id": "q1", "type": "mcq", "question": "Trong phân tích dao động cưỡng bức bằng số phức, dao động thực được xác định từ đâu?", "options": ["A. Phần thực của nghiệm phức", "B. Phần ảo của nghiệm phức", "C. Môđun của nghiệm phức", "D. Bình phương môđun"], "answer": "A", "explanation": "Dao động thực là phần thực của nghiệm phức theo nguyên lý tuyến tính."},
    {"id": "q2", "type": "mcq", "question": "Trên giản đồ Argand, biên độ A và pha φ của phasor X̂ = A*e^(iφ) là:", "options": ["A. A là phần thực, φ là phần ảo", "B. A là môđun |X̂| và φ là argument của phasor", "C. A là phần ảo, φ là môđun", "D. Không thể biểu diễn trên giản đồ Argand"], "answer": "B", "explanation": "Phasor X̂ = A*e^(iφ): môđun |X̂| = A là biên độ, argument arg(X̂) = φ là góc pha."},
    {"id": "q3", "type": "mcq", "question": "Tại tần số cộng hưởng ω = ω0 với lực cản γ ≠ 0, biên độ dao động cưỡng bức bằng:", "options": ["A. Vô cùng lớn", "B. F0/(m*γ*ω0), hữu hạn tỉ lệ nghịch γ", "C. Biên độ dao động tự do ban đầu", "D. Bằng không"], "answer": "B", "explanation": "Tại cộng hưởng, chỉ còn lực cản m*γ*ω0, nên A = F0/(m*γ*ω0). Chỉ khi γ→0 thì A→∞."},
    {"id": "q4", "type": "open", "question": "Với vai trò kỹ sư cơ điện tử thiết kế hệ đo chính xác micrometer, hãy giải thích tầm quan trọng của biên độ phức, góc pha và cộng hưởng trong thiết kế bộ cách ly rung động.", "sample_answer": "Biên độ phức và pha xác định mức rung động truyền qua và độ trễ của hệ. Cộng hưởng tại ω0 khuếch đại biên độ Q lần, khiến sai số vượt ngưỡng micrometer. Hàm transmissibility T(ω) giúp chọn isolation mount với ω_mount thấp để T < 1 ở dải tần hoạt động."}
  ]
}
```


## Quiz Questions

**Q1:** Trong phân tích dao động cưỡng bức bằng số phức, dao động thực được xác định từ đâu?
- A) A. Phần thực của nghiệm phức
- B) B. Phần ảo của nghiệm phức
- C) C. Môđun của nghiệm phức
- D) D. Bình phương môđun

**Correct:** A

**Explanation:** Dao động thực là phần thực của nghiệm phức theo nguyên lý tuyến tính.

**Q2:** Trên giản đồ Argand, biên độ A và pha φ của phasor X̂ = A*e^(iφ) là:
- A) A. A là phần thực, φ là phần ảo
- B) B. A là môđun |X̂| và φ là argument của phasor
- C) C. A là phần ảo, φ là môđun
- D) D. Không thể biểu diễn trên giản đồ Argand

**Correct:** B

**Explanation:** Phasor X̂ = A*e^(iφ): môđun |X̂| = A là biên độ, argument arg(X̂) = φ là góc pha.

**Q3:** Tại tần số cộng hưởng ω = ω0 với lực cản γ ≠ 0, biên độ dao động cưỡng bức bằng:
- A) A. Vô cùng lớn
- B) B. F0/(m*γ*ω0), hữu hạn tỉ lệ nghịch γ
- C) C. Biên độ dao động tự do ban đầu
- D) D. Bằng không

**Correct:** B

**Explanation:** Tại cộng hưởng, chỉ còn lực cản m*γ*ω0, nên A = F0/(m*γ*ω0). Chỉ khi γ→0 thì A→∞.

**Q4:** Với vai trò kỹ sư cơ điện tử thiết kế hệ đo chính xác micrometer, hãy giải thích tầm quan trọng của biên độ phức, góc pha và cộng hưởng trong thiết kế bộ cách ly rung động.

**Correct:** N/A


---
*Exported from Feynman Bot*
