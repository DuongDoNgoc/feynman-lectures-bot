---
lesson_id: 5463
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:05.636359+00:00"
content_hash: c2129e32c207
chapter_number: 19
chapter_title: Chapter 19
section_number: 5
section_title: 19–4Rotational kinetic energy
---
# ## Quiz: Động Năng Quay và Bảo Toàn Moment Động Lượng

*Source: Chapter 19 - Chapter 19 (Section 5) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_19.html)*

## Quiz: Động Năng Quay và Bảo Toàn Moment Động Lượng

Bài kiểm tra về động năng quay, moment động lượng và ứng dụng trong hệ cơ điện tử.

---

**Câu 1.** Động năng của vật thể cứng quay với vận tốc góc $\omega$ và moment quán tính $I$ là:

A. $E = I\omega$

B. $E = \dfrac{1}{2}I\omega$

C. $E = \dfrac{1}{2}I\omega^2$

D. $E = I\omega^2$

**Đáp án: C**
*Giải thích:* Tương tự động năng tịnh tiến $\frac{1}{2}mv^2$, động năng quay là $\frac{1}{2}I\omega^2$. Chứng minh: tổng $\sum \frac{1}{2}m_i v_i^2 = \sum \frac{1}{2}m_i(\omega r_i)^2 = \frac{1}{2}\omega^2\sum m_i r_i^2 = \frac{1}{2}I\omega^2$.

---

**Câu 2.** Một vận động viên trượt băng đang quay với $\omega_1 = 2\,\text{rad/s}$, moment quán tính $I_1 = 4\,\text{kg·m}^2$. Cô thu tay vào làm $I_2 = 1\,\text{kg·m}^2$. Vận tốc góc mới $\omega_2$ là:

A. $\omega_2 = 0.5\,\text{rad/s}$

B. $\omega_2 = 2\,\text{rad/s}$

C. $\omega_2 = 6\,\text{rad/s}$

D. $\omega_2 = 8\,\text{rad/s}$

**Đáp án: D**
*Giải thích:* Bảo toàn $L = I\omega$: $I_1\omega_1 = I_2\omega_2 \Rightarrow 4 \times 2 = 1 \times \omega_2 \Rightarrow \omega_2 = 8\,\text{rad/s}$. Khi $I$ giảm 4 lần, $\omega$ tăng 4 lần. Động năng tăng từ $4\,\text{J}$ lên $32\,\text{J}$ — năng lượng từ công cơ bắp.

---

**Câu 3.** Hai đĩa có $I_1 = 0.1\,\text{kg·m}^2$, $\omega_1 = 100\,\text{rad/s}$ và $I_2 = 0.4\,\text{kg·m}^2$, $\omega_2 = 0$ được nối cứng với nhau đột ngột. Vận tốc góc chung sau khi nối là:

A. $\omega_f = 100\,\text{rad/s}$

B. $\omega_f = 50\,\text{rad/s}$

C. $\omega_f = 25\,\text{rad/s}$

D. $\omega_f = 20\,\text{rad/s}$

**Đáp án: D**
*Giải thích:* Bảo toàn $L$: $\omega_f = \dfrac{I_1\omega_1 + I_2\omega_2}{I_1+I_2} = \dfrac{0.1 \times 100 + 0}{0.5} = \dfrac{10}{0.5} = 20\,\text{rad/s}$. Năng lượng mất: $T_i = \frac{1}{2}(0.1)(100^2) = 500\,\text{J}$, $T_f = \frac{1}{2}(0.5)(20^2) = 100\,\text{J}$. Mất $400\,\text{J}$ dưới dạng nhiệt trong khớp nối.

---

**Câu 4 (Tự luận).** Trong hệ servo của robot hoặc thiết bị đo lường chính xác, hiện tượng "inertia mismatch" xảy ra khi moment quán tính tải thay đổi đột ngột (ví dụ: kẹp/thả vật, thu/duỗi cánh tay). Hãy phân tích ảnh hưởng của sự thay đổi $I$ đến hệ điều khiển và đề xuất giải pháp để duy trì độ chính xác vị trí ở cấp micromet.

*Gợi ý trả lời:*
Khi $I$ giảm đột ngột mà không có torque ngoài, $\omega$ tăng để bảo toàn $L$, gây overshoot trong vòng lặp điều khiển vị trí. Với bộ điều khiển PID thuần, thời gian settling tăng do hằng số thời gian thay đổi. Giải pháp: (1) **Feedforward với model động lực học**: lưu $I(q)$ theo cấu hình khớp $q$, bù trước torque motor; (2) **Adaptive control**: nhận dạng $I$ online từ tín hiệu encoder và cập nhật gain điều khiển; (3) **Mechanical pre-compensation**: thiết kế counterweight để $I$ thay đổi ít nhất khi cánh tay thu/duỗi. Trong CMM (Coordinate Measuring Machine), đầu đo Renishaw thiết kế mass distribution để $I$ gần như không đổi trong toàn dải góc, đạt lặp lại vị trí $< 1\,\mu\text{m}$.

```json
{"questions":[{"id":"q1","type":"mcq","question":"Động năng của vật thể cứng quay với vận tốc góc ω và moment quán tính I là:","options":["A. E = I·ω","B. E = (1/2)I·ω","C. E = (1/2)I·ω²","D. E = I·ω²"],"answer":"C","explanation":"E = (1/2)I·ω². Suy ra từ tổng Σ(1/2)m_i·v_i² = Σ(1/2)m_i(ω·r_i)² = (1/2)ω²·Σm_i·r_i² = (1/2)I·ω². Đây là dạng quay của động năng tịnh tiến (1/2)mv²."},{"id":"q2","type":"mcq","question":"Vận động viên quay với ω₁=2 rad/s, I₁=4 kg·m². Thu tay vào I₂=1 kg·m². Tốc độ mới ω₂?","options":["A. ω₂ = 0.5 rad/s","B. ω₂ = 2 rad/s","C. ω₂ = 6 rad/s","D. ω₂ = 8 rad/s"],"answer":"D","explanation":"Bảo toàn L: I₁ω₁=I₂ω₂ → 4×2=1×ω₂ → ω₂=8 rad/s. I giảm 4 lần, ω tăng 4 lần. Động năng tăng từ 4J lên 32J nhờ công cơ bắp thu tay."},{"id":"q3","type":"mcq","question":"Hai đĩa I₁=0.1 kg·m²,ω₁=100 rad/s và I₂=0.4 kg·m²,ω₂=0 nối cứng đột ngột. Tốc độ chung?","options":["A. ωf = 100 rad/s","B. ωf = 50 rad/s","C. ωf = 25 rad/s","D. ωf = 20 rad/s"],"answer":"D","explanation":"ωf = (I₁ω₁+I₂ω₂)/(I₁+I₂) = (0.1×100)/(0.5) = 20 rad/s. Năng lượng mất: 500-100=400J thành nhiệt trong khớp nối."},{"id":"q4","type":"open","question":"Trong servo robot/thiết bị đo lường chính xác, inertia mismatch khi I thay đổi đột ngột ảnh hưởng thế nào đến hệ điều khiển? Đề xuất giải pháp duy trì độ chính xác ở cấp micromet.","sample_answer":"Khi I giảm đột ngột, ω tăng để bảo toàn L, gây overshoot trong vòng vị trí. Giải pháp: (1) feedforward với model I(q) theo cấu hình khớp; (2) adaptive control nhận dạng I online từ encoder; (3) thiết kế counterweight để I ít thay đổi. CMM Renishaw thiết kế mass distribution cho I gần không đổi, đạt lặp lại <1μm."}]}
```


## Quiz Questions

**Q1:** Động năng của vật thể cứng quay với vận tốc góc ω và moment quán tính I là:
- A) A. E = I·ω
- B) B. E = (1/2)I·ω
- C) C. E = (1/2)I·ω²
- D) D. E = I·ω²

**Correct:** C

**Explanation:** E = (1/2)I·ω². Suy ra từ tổng Σ(1/2)m_i·v_i² = Σ(1/2)m_i(ω·r_i)² = (1/2)ω²·Σm_i·r_i² = (1/2)I·ω². Đây là dạng quay của động năng tịnh tiến (1/2)mv².

**Q2:** Vận động viên quay với ω₁=2 rad/s, I₁=4 kg·m². Thu tay vào I₂=1 kg·m². Tốc độ mới ω₂?
- A) A. ω₂ = 0.5 rad/s
- B) B. ω₂ = 2 rad/s
- C) C. ω₂ = 6 rad/s
- D) D. ω₂ = 8 rad/s

**Correct:** D

**Explanation:** Bảo toàn L: I₁ω₁=I₂ω₂ → 4×2=1×ω₂ → ω₂=8 rad/s. I giảm 4 lần, ω tăng 4 lần. Động năng tăng từ 4J lên 32J nhờ công cơ bắp thu tay.

**Q3:** Hai đĩa I₁=0.1 kg·m²,ω₁=100 rad/s và I₂=0.4 kg·m²,ω₂=0 nối cứng đột ngột. Tốc độ chung?
- A) A. ωf = 100 rad/s
- B) B. ωf = 50 rad/s
- C) C. ωf = 25 rad/s
- D) D. ωf = 20 rad/s

**Correct:** D

**Explanation:** ωf = (I₁ω₁+I₂ω₂)/(I₁+I₂) = (0.1×100)/(0.5) = 20 rad/s. Năng lượng mất: 500-100=400J thành nhiệt trong khớp nối.

**Q4:** Trong servo robot/thiết bị đo lường chính xác, inertia mismatch khi I thay đổi đột ngột ảnh hưởng thế nào đến hệ điều khiển? Đề xuất giải pháp duy trì độ chính xác ở cấp micromet.

**Correct:** N/A


---
*Exported from Feynman Bot*
