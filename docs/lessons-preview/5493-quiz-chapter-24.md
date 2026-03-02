---
lesson_id: 5493
lesson_type: quiz
approval_status: pending
exported_at: "2026-03-02T15:10:31.003746+00:00"
content_hash: ee869cbf7efc
chapter_number: 24
chapter_title: Chapter 24
section_number: 2
section_title: 24–1The energy of an oscillator
---
# ## Quiz: Quá Độ (Transients) và Năng Lượng Trong Dao Động

*Source: Chapter 24 - Chapter 24 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_24.html)*

## Quiz: Quá Độ (Transients) và Năng Lượng Trong Dao Động

### Câu 1 (Trắc nghiệm)
Khi tính giá trị trung bình bình phương của đại lượng dao động $A_{real}(t) = A_0\cos(\omega t + \Delta)$ bằng phương pháp số phức, kết quả đúng là:

A. $\langle A^2 \rangle = |\hat{A}|^2 = A_0^2$ (bình phương môđun phasor)
B. $\langle A^2 \rangle = \dfrac{1}{2}|\hat{A}|^2 = \dfrac{A_0^2}{2}$ (nửa bình phương môđun phasor)
C. $\langle A^2 \rangle = \text{Re}[\hat{A}^2] = A_0^2\cos(2\Delta)$
D. $\langle A^2 \rangle = |\hat{A}|^2/4 = A_0^2/4$

**Đáp án: B**
*Giải thích:* Giá trị trung bình $\langle\cos^2(\omega t + \Delta)\rangle = 1/2$, nên $\langle A^2\rangle = A_0^2/2 = |\hat{A}|^2/2$. Công thức chung: $\langle A^2\rangle = \frac{1}{2}\hat{A}\hat{A}^* = \frac{1}{2}|\hat{A}|^2$. Không được bình phương trực tiếp số phức vì cho kết quả dao động ở tần số $2\omega$.

---

### Câu 2 (Trắc nghiệm)
Hệ dao động tắt dần (damped oscillation) ở chế độ **critical damping** (cản tới hạn) khi:

A. Hệ số cản $\gamma > 2\omega_0$ — hệ không dao động, về 0 rất chậm
B. Hệ số cản $\gamma < 2\omega_0$ — hệ dao động tắt dần với tần số $\omega_1 < \omega_0$
C. Hệ số cản $\gamma = 2\omega_0$ — hệ không dao động và trở về 0 *nhanh nhất*
D. $Q = 10$ — hệ dao động nhiều chu kỳ trước khi tắt

**Đáp án: C**
*Giải thích:* Critical damping xảy ra khi $\gamma = 2\omega_0$ (tương đương $Q = 1/2$). Đây là điều kiện giúp hệ trở về 0 nhanh nhất mà không dao động — lý tưởng cho thiết kế cơ cấu đo và cửa tự đóng.

---

### Câu 3 (Trắc nghiệm)
Điện áp RMS (hiệu dụng) của lưới điện gia dụng $220\,\text{V}$ ở Việt Nam có biên độ đỉnh $V_0$ bằng:

A. $V_0 = 220\,\text{V}$
B. $V_0 = 220/\sqrt{2} \approx 155.6\,\text{V}$
C. $V_0 = 220\sqrt{2} \approx 311\,\text{V}$
D. $V_0 = 2 \times 220 = 440\,\text{V}$

**Đáp án: C**
*Giải thích:* $V_{RMS} = V_0/\sqrt{2}$, nên $V_0 = V_{RMS}\sqrt{2} = 220\sqrt{2} \approx 311\,\text{V}$. Đây là lý do thiết bị điện phải chịu được điện áp đỉnh ~311 V dù ổ cắm ghi 220 V.

---

### Câu 4 (Tự luận mở)
**Câu hỏi:** Trong hệ thống điều khiển định vị chính xác micrometer (ví dụ: piezo stage hoặc linear motor), khi nhận lệnh dịch chuyển bước nhảy (step command), hệ xuất hiện dao động quá độ (transient oscillation) trước khi đạt vị trí đích. Hãy giải thích mối quan hệ giữa hệ số Q (hoặc hệ số cản $\gamma$) của hệ cơ học và: (a) thời gian ổn định (settling time), (b) độ vượt quá (overshoot). Đề xuất chiến lược điều chỉnh cản để đạt cân bằng giữa tốc độ và độ chính xác trong ứng dụng đo lường.

**Gợi ý trả lời mẫu:** Q cao (cản thấp): settling time dài $T_s \approx 4Q/\omega_0$, overshoot lớn — không tốt cho đo lường cần ổn định nhanh. Q = 0.5 (critical): không overshoot, settling time ngắn nhất — lý tưởng về lý thuyết nhưng nhạy cảm với biến động tham số. Q ≈ 0.7 (slightly underdamped, $\zeta = 1/\sqrt{2}$): cân bằng tốt, overshoot ~5%, settling time ngắn — thực tế thường chọn. Điều chỉnh qua bộ điều khiển PID: tăng $K_D$ (derivative gain) tương đương tăng cản, giảm overshoot; giảm $K_P$ giảm tần số cộng hưởng vòng kín.

```json
{
  "questions": [
    {"id": "q1", "type": "mcq", "question": "Giá trị trung bình bình phương ⟨A²⟩ của A_real = A0*cos(ωt + Δ) khi tính qua số phức bằng:", "options": ["A. |Â|² = A0²", "B. |Â|²/2 = A0²/2", "C. Re[Â²] = A0²*cos(2Δ)", "D. |Â|²/4 = A0²/4"], "answer": "B", "explanation": "⟨cos²(ωt+Δ)⟩ = 1/2, nên ⟨A²⟩ = A0²/2 = |Â|²/2. Không bình phương trực tiếp số phức."},
    {"id": "q2", "type": "mcq", "question": "Hệ dao động tắt dần ở chế độ critical damping khi:", "options": ["A. γ > 2ω0 — không dao động, về 0 rất chậm", "B. γ < 2ω0 — dao động tắt dần", "C. γ = 2ω0 — không dao động, về 0 nhanh nhất", "D. Q = 10 — dao động nhiều chu kỳ"], "answer": "C", "explanation": "Critical damping tại γ = 2ω0 (Q = 0.5): hệ về 0 nhanh nhất không dao động, lý tưởng cho cơ cấu đo."},
    {"id": "q3", "type": "mcq", "question": "Điện áp lưới 220V (RMS) có biên độ đỉnh V0 bằng:", "options": ["A. 220V", "B. 220/√2 ≈ 155.6V", "C. 220√2 ≈ 311V", "D. 440V"], "answer": "C", "explanation": "V_RMS = V0/√2, nên V0 = 220√2 ≈ 311V. Thiết bị phải chịu điện áp đỉnh ~311V."},
    {"id": "q4", "type": "open", "question": "Trong hệ định vị chính xác micrometer, hãy giải thích mối quan hệ giữa hệ số Q và (a) settling time, (b) overshoot, rồi đề xuất chiến lược điều chỉnh cản.", "sample_answer": "Q cao: settling time dài (4Q/ω0), overshoot lớn. Q=0.5 (critical): không overshoot, settling nhanh nhất. Q≈0.7: cân bằng tốt, overshoot ~5%. Điều chỉnh qua PID: tăng K_D tăng cản, giảm overshoot."}
  ]
}
```


## Quiz Questions

**Q1:** Giá trị trung bình bình phương ⟨A²⟩ của A_real = A0*cos(ωt + Δ) khi tính qua số phức bằng:
- A) A. |Â|² = A0²
- B) B. |Â|²/2 = A0²/2
- C) C. Re[Â²] = A0²*cos(2Δ)
- D) D. |Â|²/4 = A0²/4

**Correct:** B

**Explanation:** ⟨cos²(ωt+Δ)⟩ = 1/2, nên ⟨A²⟩ = A0²/2 = |Â|²/2. Không bình phương trực tiếp số phức.

**Q2:** Hệ dao động tắt dần ở chế độ critical damping khi:
- A) A. γ > 2ω0 — không dao động, về 0 rất chậm
- B) B. γ < 2ω0 — dao động tắt dần
- C) C. γ = 2ω0 — không dao động, về 0 nhanh nhất
- D) D. Q = 10 — dao động nhiều chu kỳ

**Correct:** C

**Explanation:** Critical damping tại γ = 2ω0 (Q = 0.5): hệ về 0 nhanh nhất không dao động, lý tưởng cho cơ cấu đo.

**Q3:** Điện áp lưới 220V (RMS) có biên độ đỉnh V0 bằng:
- A) A. 220V
- B) B. 220/√2 ≈ 155.6V
- C) C. 220√2 ≈ 311V
- D) D. 440V

**Correct:** C

**Explanation:** V_RMS = V0/√2, nên V0 = 220√2 ≈ 311V. Thiết bị phải chịu điện áp đỉnh ~311V.

**Q4:** Trong hệ định vị chính xác micrometer, hãy giải thích mối quan hệ giữa hệ số Q và (a) settling time, (b) overshoot, rồi đề xuất chiến lược điều chỉnh cản.

**Correct:** N/A


---
*Exported from Feynman Bot*
