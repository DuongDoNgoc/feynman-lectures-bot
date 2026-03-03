---
lesson_id: 5496
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:06.538855+00:00"
content_hash: b27cfda1ea22
chapter_number: 24
chapter_title: Chapter 24
section_number: 4
section_title: 24–3Electrical transients
---
# ## Quiz: Quá Độ Điện — Mạch RLC Và Oscilloscope

*Source: Chapter 24 - Chapter 24 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_24.html)*

## Quiz: Quá Độ Điện — Mạch RLC Và Oscilloscope

### Câu 1 (Trắc nghiệm)
Trong mạch RLC nối tiếp với Q cao, sau khi đóng công tắc đột ngột, dạng sóng điện áp trên oscilloscope có dạng:

A. Xung vuông (square wave) tắt dần
B. Hàm mũ đơn giản (đường cong giảm dần không dao động)
C. Dao động sinusoidal tắt dần (sinusoidal envelope with exponential decay)
D. Hàm bước nhảy (step function) không thay đổi

**Đáp án: C**
*Giải thích:* Với Q cao ($\gamma < 2\omega_0$), hệ underdamped: $V_L(t) \propto e^{-\alpha t}\cos(\omega_d t + \phi)$. Đây là dao động tần số $\omega_d \approx \omega_0$ với biên độ tắt dần theo hàm mũ $e^{-\alpha t}$. Oscilloscope hiển thị đường sin bao quanh bởi đường bao (envelope) hàm mũ.

---

### Câu 2 (Trắc nghiệm)
Khi tăng điện trở $R$ trong mạch RLC đến giá trị $R_c = 2\sqrt{L/C}$, hệ đạt trạng thái:

A. Cộng hưởng — dòng điện cực đại
B. Underdamping — dao động ngày càng mạnh hơn
C. Critical damping — điện áp về 0 nhanh nhất mà không dao động
D. Không thay đổi — điện trở không ảnh hưởng đến quá độ

**Đáp án: C**
*Giải thích:* $R_c = 2\sqrt{L/C}$ là điện trở tới hạn ứng với $\gamma_c = R_c/L = 2\omega_0$ (critical damping, $Q = 1/2$). Tại điểm này hệ về 0 nhanh nhất mà không dao động. Tăng $R$ thêm nữa sẽ vào vùng overdamping.

---

### Câu 3 (Trắc nghiệm)
Từ dạng sóng oscilloscope của mạch RLC underdamped, có thể đo hệ số Q bằng cách nào sau đây?

A. Đo chu kỳ dao động $T_d$ và nhân với $\omega_0$
B. Đo tỉ số biên độ hai đỉnh liên tiếp $A_n/A_{n+1}$ rồi tính $Q \approx \pi/\ln(A_n/A_{n+1})$
C. Đo điện trở $R$ của mạch trực tiếp bằng đồng hồ vạn năng
D. Đo thời gian từ 0 đến đỉnh đầu tiên

**Đáp án: B**
*Giải thích:* Logarithmic decrement: $\delta = \ln(A_n/A_{n+1}) = \alpha T_d \approx \pi/Q$ (với $Q \gg 1$). Từ đó $Q \approx \pi/\delta$. Phương pháp này đo Q *thực tế* từ thực nghiệm, kể cả các yếu tố tổn hao không lý tưởng.

---

### Câu 4 (Tự luận mở)
**Câu hỏi:** Trong phòng thí nghiệm kiểm tra thiết bị đo chính xác, bạn cần xác định tần số cộng hưởng $\omega_0$ và hệ số Q của một cơ cấu cơ học (ví dụ: bệ đỡ piezoelectric stage). Thay vì thực nghiệm cơ học phức tạp, bạn quyết định dùng **mô hình điện tương đương** (electrical analog) với mạch RLC, kết hợp oscilloscope để đo step response. Hãy mô tả: (a) cách xây dựng mô hình điện tương đương, (b) cách đo $\omega_0$ và Q từ oscilloscope, và (c) cách chuyển đổi kết quả điện trở về thông số cơ học.

**Gợi ý trả lời mẫu:** (a) Xây dựng bảng tương đồng: $m \to L$, $k \to 1/C$, $b \to R$. Chọn $L$ (mH) đại diện $m$ (kg), $C$ (F) đại diện $1/k$, $R$ ($\Omega$) đại diện $b$ với tỉ lệ phù hợp. (b) Đóng công tắc, đọc tần số dao động $f_d = \omega_d/(2\pi)$ từ oscilloscope → $\omega_0 \approx \omega_d$ (nếu Q > 3). Đo $\delta = \ln(A_n/A_{n+1})$ → $Q = \pi/\delta$. (c) $\omega_0^{cơ} = \omega_0^{điện}$, $Q^{cơ} = Q^{điện}$, $k = m\omega_0^2$, $b = m\omega_0/Q$. Ưu điểm: thay đổi $R$, $L$, $C$ dễ hơn thay đổi vật liệu cơ học, thời gian prototype rút ngắn.

```json
{
  "questions": [
    {"id": "q1", "type": "mcq", "question": "Mạch RLC nối tiếp với Q cao, sau khi đóng công tắc, dạng sóng trên oscilloscope có dạng:", "options": ["A. Xung vuông tắt dần", "B. Hàm mũ đơn giản không dao động", "C. Dao động sinusoidal tắt dần", "D. Hàm bước nhảy không thay đổi"], "answer": "C", "explanation": "Underdamped (Q > 1/2): V_L(t) ∝ e^(-αt)*cos(ωd*t + φ) — dao động tắt dần với envelope hàm mũ."},
    {"id": "q2", "type": "mcq", "question": "Khi tăng R đến Rc = 2√(L/C) trong mạch RLC, hệ đạt:", "options": ["A. Cộng hưởng - dòng cực đại", "B. Underdamping - dao động mạnh hơn", "C. Critical damping - về 0 nhanh nhất không dao động", "D. Không thay đổi"], "answer": "C", "explanation": "Rc = 2√(L/C) tương ứng γc = 2ω0 (Q = 0.5, critical damping): hệ về 0 nhanh nhất không dao động."},
    {"id": "q3", "type": "mcq", "question": "Từ dạng sóng oscilloscope underdamped, đo Q bằng cách:", "options": ["A. Đo chu kỳ Td rồi nhân ω0", "B. Đo tỉ số biên độ An/An+1, Q ≈ π/ln(An/An+1)", "C. Đo R bằng đồng hồ vạn năng", "D. Đo thời gian đến đỉnh đầu tiên"], "answer": "B", "explanation": "Logarithmic decrement δ = ln(An/An+1) = αTd ≈ π/Q (Q >> 1). Q ≈ π/δ đo Q thực tế từ thực nghiệm."},
    {"id": "q4", "type": "open", "question": "Mô tả cách dùng mô hình điện tương đương (RLC + oscilloscope) để xác định ω0 và Q của cơ cấu cơ học (piezo stage), bao gồm cách xây dựng mô hình, đo đạc và chuyển đổi kết quả.", "sample_answer": "(a) m→L, k→1/C, b→R với tỉ lệ phù hợp. (b) Đo fd=ωd/(2π) → ω0≈ωd. Đo δ=ln(An/An+1) → Q=π/δ. (c) ω0(cơ)=ω0(điện), Q(cơ)=Q(điện), k=m*ω0², b=m*ω0/Q. Ưu điểm: thay đổi tham số nhanh, prototype rút ngắn."}
  ]
}
```


## Quiz Questions

**Q1:** Mạch RLC nối tiếp với Q cao, sau khi đóng công tắc, dạng sóng trên oscilloscope có dạng:
- A) A. Xung vuông tắt dần
- B) B. Hàm mũ đơn giản không dao động
- C) C. Dao động sinusoidal tắt dần
- D) D. Hàm bước nhảy không thay đổi

**Correct:** C

**Explanation:** Underdamped (Q > 1/2): V_L(t) ∝ e^(-αt)*cos(ωd*t + φ) — dao động tắt dần với envelope hàm mũ.

**Q2:** Khi tăng R đến Rc = 2√(L/C) trong mạch RLC, hệ đạt:
- A) A. Cộng hưởng - dòng cực đại
- B) B. Underdamping - dao động mạnh hơn
- C) C. Critical damping - về 0 nhanh nhất không dao động
- D) D. Không thay đổi

**Correct:** C

**Explanation:** Rc = 2√(L/C) tương ứng γc = 2ω0 (Q = 0.5, critical damping): hệ về 0 nhanh nhất không dao động.

**Q3:** Từ dạng sóng oscilloscope underdamped, đo Q bằng cách:
- A) A. Đo chu kỳ Td rồi nhân ω0
- B) B. Đo tỉ số biên độ An/An+1, Q ≈ π/ln(An/An+1)
- C) C. Đo R bằng đồng hồ vạn năng
- D) D. Đo thời gian đến đỉnh đầu tiên

**Correct:** B

**Explanation:** Logarithmic decrement δ = ln(An/An+1) = αTd ≈ π/Q (Q >> 1). Q ≈ π/δ đo Q thực tế từ thực nghiệm.

**Q4:** Mô tả cách dùng mô hình điện tương đương (RLC + oscilloscope) để xác định ω0 và Q của cơ cấu cơ học (piezo stage), bao gồm cách xây dựng mô hình, đo đạc và chuyển đổi kết quả.

**Correct:** N/A


---
*Exported from Feynman Bot*
