---
lesson_id: 5526
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:07.175461+00:00"
content_hash: 0e063a1ef36a
chapter_number: 28
chapter_title: Chapter 28
section_number: 2
section_title: 28–1Electromagnetism
---
# ## Quiz: Bức Xạ Điện Từ và Phương Trình Maxwell

*Source: Chapter 28 - Chapter 28 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_28.html)*

## Quiz: Bức Xạ Điện Từ và Phương Trình Maxwell

### Câu 1 (Trắc nghiệm)
Maxwell thêm số hạng "dòng điện dịch" (displacement current) vào phương trình Ampère vì lý do nào?

A. Để giải thích tại sao ánh sáng có màu sắc khác nhau

B. Phương trình Ampère gốc không nhất quán về mặt toán học — divergence của nó mâu thuẫn với phương trình liên tục

C. Để bổ sung tác dụng của từ trường lên điện tích chuyển động

D. Để giải thích hiện tượng cảm ứng điện từ của Faraday

**Đáp án: B**
*Giải thích:* $\nabla \cdot (\nabla \times \vec{B}) = 0$ luôn đúng, nhưng $\nabla \cdot \vec{J} = -\partial\rho/\partial t \neq 0$ trong trường hợp tổng quát. Để giải quyết mâu thuẫn này, Maxwell thêm số hạng $\varepsilon_0 \partial\vec{E}/\partial t$ vào vế phải của phương trình Ampère, và điều này dẫn đến dự đoán sóng điện từ.

---

### Câu 2 (Trắc nghiệm)
Vận tốc ánh sáng trong chân không $c = 3 \times 10^8$ m/s được suy ra từ phương trình Maxwell thông qua công thức:

A. $c = \mu_0 / \varepsilon_0$

B. $c = \sqrt{\mu_0 \varepsilon_0}$

C. $c = 1 / \sqrt{\mu_0 \varepsilon_0}$

D. $c = \mu_0 \varepsilon_0 / 2\pi$

**Đáp án: C**
*Giải thích:* Từ phương trình sóng điện từ $\nabla^2\vec{E} = \mu_0\varepsilon_0 \partial^2\vec{E}/\partial t^2$, so sánh với phương trình sóng chuẩn $\nabla^2 u = (1/v^2)\partial^2 u/\partial t^2$, ta suy ra $v = c = 1/\sqrt{\mu_0\varepsilon_0}$. Tính toán cho giá trị đúng bằng vận tốc ánh sáng đo được.

---

### Câu 3 (Trắc nghiệm)
Trường bức xạ điện từ (radiation field) của điện tích dao động giảm theo khoảng cách như thế nào?

A. Tỉ lệ nghịch với bình phương khoảng cách: $E \propto 1/r^2$

B. Tỉ lệ nghịch với khoảng cách: $E \propto 1/r$

C. Không thay đổi theo khoảng cách

D. Tỉ lệ nghịch với căn bậc hai khoảng cách: $E \propto 1/\sqrt{r}$

**Đáp án: B**
*Giải thích:* Đây là phát hiện then chốt của Maxwell. Trường Coulomb tĩnh giảm theo $1/r^2$, nhưng trường bức xạ (radiation field) chỉ giảm theo $1/r$. Điều này có nghĩa cường độ sóng ($\propto E^2$) giảm theo $1/r^2$ — định luật bình phương nghịch đảo đúng cho cường độ, không phải biên độ trường. Đây là lý do sóng radio có thể truyền đi hàng nghìn km.

---

### Câu 4 (Tự luận)
**Câu hỏi mở:** Trong thiết kế hệ thống radar cho phương tiện tự hành hoặc ứng dụng quân sự, bạn cần hiểu phương trình radar: $P_r = P_t G_t G_r \sigma \lambda^2 / [(4\pi)^3 R^4]$.

(a) Giải thích tại sao công suất thu $P_r$ tỉ lệ với $R^{-4}$ (không phải $R^{-2}$) dựa trên tính chất $1/r$ của trường bức xạ.

(b) Nếu bạn muốn tăng gấp đôi tầm phát hiện (từ $R$ lên $2R$) trong khi giữ nguyên công suất phát và gain anten, cần tăng $\sigma$ (diện tích phản xạ radar của mục tiêu) lên bao nhiêu lần? Hay cần thay đổi tham số nào?

(c) Tại sao wavelength $\lambda$ nhỏ hơn (tần số cao hơn) không nhất thiết là tốt hơn cho radar tầm xa, dù độ phân giải không gian tốt hơn?

**Gợi ý trả lời mẫu:** (a) Trường bức xạ $E \propto 1/r$, nên cường độ $I \propto E^2 \propto 1/r^2$ khi sóng đi từ anten đến mục tiêu. Sau đó mục tiêu tái phát xạ, cường độ sóng phản xạ lại giảm $1/r^2$ khi quay về anten. Tổng cộng: $1/r^2 \times 1/r^2 = 1/r^4$; (b) $P_r \propto 1/R^4$, nếu $R \to 2R$ thì $P_r$ giảm $16$ lần. Để bù lại cần tăng $\sigma$ lên 16 lần, hoặc tăng $P_t$ lên 16 lần, hoặc tăng $G_t G_r$ lên 16 lần (ví dụ tăng gain mỗi anten 4 lần); (c) Từ phương trình radar, $P_r \propto \lambda^2$, nên tần số cao (λ nhỏ) thực ra làm giảm $P_r$. Hơn nữa, sóng tần số cao bị suy hao khí quyển mạnh hơn, không phù hợp tầm xa.

```json
{
  "questions": [
    {"id": "q1", "type": "mcq", "question": "Maxwell thêm dòng điện dịch vào phương trình Ampère vì:", "options": ["A. Để giải thích màu sắc ánh sáng", "B. Phương trình Ampère gốc không nhất quán: div(curl B)=0 mâu thuẫn với div J ≠ 0", "C. Để bổ sung tác dụng từ trường lên điện tích", "D. Để giải thích cảm ứng điện từ Faraday"], "answer": "B", "explanation": "Mâu thuẫn toán học trong phương trình Ampère gốc buộc Maxwell thêm εε∂E/∂t, dẫn đến dự đoán sóng điện từ."},
    {"id": "q2", "type": "mcq", "question": "Vận tốc ánh sáng c suy ra từ phương trình Maxwell là:", "options": ["A. c = μ₀/ε₀", "B. c = √(μ₀ε₀)", "C. c = 1/√(μ₀ε₀)", "D. c = μ₀ε₀/2π"], "answer": "C", "explanation": "Từ phương trình sóng, so sánh với ∇²u = (1/v²)∂²u/∂t², suy ra c = 1/√(μ₀ε₀) ≈ 3×10⁸ m/s."},
    {"id": "q3", "type": "mcq", "question": "Trường bức xạ điện từ của điện tích dao động giảm theo khoảng cách r như thế nào?", "options": ["A. E ∝ 1/r²", "B. E ∝ 1/r", "C. E không thay đổi", "D. E ∝ 1/√r"], "answer": "B", "explanation": "Trường bức xạ ∝ 1/r (không phải 1/r²), nên cường độ ∝ 1/r². Đây là lý do sóng radio truyền được xa."},
    {"id": "q4", "type": "open", "question": "Về phương trình radar Pr = PtGtGrσλ²/[(4π)³R⁴]: (a) tại sao Pr ∝ R⁻⁴? (b) tăng tầm gấp đôi cần tăng tham số nào bao nhiêu lần? (c) tại sao λ nhỏ không nhất thiết tốt cho radar tầm xa?", "sample_answer": "(a) Cường độ giảm 1/r² từ anten đến mục tiêu, rồi lại 1/r² khi phản xạ về, tổng 1/r⁴; (b) Cần tăng PtGtGrσ lên 16 lần (ví dụ tăng Pt×16 hoặc σ×16); (c) Pr ∝ λ², nên λ nhỏ làm giảm Pr; thêm vào đó tần số cao bị suy hao khí quyển mạnh hơn."}
  ]
}
```


## Quiz Questions

**Q1:** Maxwell thêm dòng điện dịch vào phương trình Ampère vì:
- A) A. Để giải thích màu sắc ánh sáng
- B) B. Phương trình Ampère gốc không nhất quán: div(curl B)=0 mâu thuẫn với div J ≠ 0
- C) C. Để bổ sung tác dụng từ trường lên điện tích
- D) D. Để giải thích cảm ứng điện từ Faraday

**Correct:** B

**Explanation:** Mâu thuẫn toán học trong phương trình Ampère gốc buộc Maxwell thêm εε∂E/∂t, dẫn đến dự đoán sóng điện từ.

**Q2:** Vận tốc ánh sáng c suy ra từ phương trình Maxwell là:
- A) A. c = μ₀/ε₀
- B) B. c = √(μ₀ε₀)
- C) C. c = 1/√(μ₀ε₀)
- D) D. c = μ₀ε₀/2π

**Correct:** C

**Explanation:** Từ phương trình sóng, so sánh với ∇²u = (1/v²)∂²u/∂t², suy ra c = 1/√(μ₀ε₀) ≈ 3×10⁸ m/s.

**Q3:** Trường bức xạ điện từ của điện tích dao động giảm theo khoảng cách r như thế nào?
- A) A. E ∝ 1/r²
- B) B. E ∝ 1/r
- C) C. E không thay đổi
- D) D. E ∝ 1/√r

**Correct:** B

**Explanation:** Trường bức xạ ∝ 1/r (không phải 1/r²), nên cường độ ∝ 1/r². Đây là lý do sóng radio truyền được xa.

**Q4:** Về phương trình radar Pr = PtGtGrσλ²/[(4π)³R⁴]: (a) tại sao Pr ∝ R⁻⁴? (b) tăng tầm gấp đôi cần tăng tham số nào bao nhiêu lần? (c) tại sao λ nhỏ không nhất thiết tốt cho radar tầm xa?

**Correct:** N/A


---
*Exported from Feynman Bot*
