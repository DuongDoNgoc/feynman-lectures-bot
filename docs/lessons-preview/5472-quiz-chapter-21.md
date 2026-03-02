---
lesson_id: 5472
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-02T15:10:30.346201+00:00"
content_hash: 3bc4add48845
chapter_number: 21
chapter_title: Chapter 21
section_number: 2
section_title: 21–1Linear differential equations
---
# ## Quiz: Bộ Dao Động Điều Hòa

*Source: Chapter 21 - Chapter 21 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_21.html)*

## Quiz: Bộ Dao Động Điều Hòa

### Câu 1 (Trắc nghiệm)

Một accelerometer MEMS có proof mass $m = 2$ µg và spring constant $k = 0.2$ N/m. Tần số cộng hưởng tự nhiên $f_0$ bằng bao nhiêu?

A. $f_0 \approx 1592$ Hz  
B. $f_0 \approx 500$ Hz  
C. $f_0 \approx 2251$ Hz  
D. $f_0 \approx 318$ Hz  

**Đáp án: A**  
**Giải thích:** $\omega_0 = \sqrt{k/m} = \sqrt{0.2/(2\times10^{-9})} = \sqrt{10^8} = 10^4$ rad/s. Tần số: $f_0 = \omega_0/(2\pi) = 10000/(2\pi) \approx 1592$ Hz.

---

### Câu 2 (Trắc nghiệm)

Phương trình vi phân của harmonic oscillator $d^2x/dt^2 = -\omega_0^2 x$ có nghiệm tổng quát là:

A. $x(t) = Ae^{\omega_0 t} + Be^{-\omega_0 t}$  
B. $x(t) = A\cos(\omega_0 t) + B\sin(\omega_0 t)$  
C. $x(t) = At\cos(\omega_0 t)$  
D. $x(t) = A\omega_0^2 t^2 + Bt$  

**Đáp án: B**  
**Giải thích:** Thử nghiệm $x = \cos(\omega_0 t)$ cho $\ddot{x} = -\omega_0^2\cos(\omega_0 t) = -\omega_0^2 x$ — thỏa mãn. Tương tự với $\sin$. Nghiệm tổng quát là tổ hợp tuyến tính của hai nghiệm độc lập này.

---

### Câu 3 (Trắc nghiệm)

Một hệ lò xo-khối lượng dao động với $x(0) = 0.01$ m và $\dot{x}(0) = 0$ (bắt đầu từ trạng thái tĩnh ở vị trí kéo lệch). Nghiệm $x(t)$ là:

A. $x(t) = 0.01\sin(\omega_0 t)$  
B. $x(t) = 0.01\cos(\omega_0 t)$  
C. $x(t) = 0.01e^{-\omega_0 t}$  
D. $x(t) = 0.01(1 - \cos(\omega_0 t))$  

**Đáp án: B**  
**Giải thích:** Từ nghiệm tổng quát $x(t) = A\cos(\omega_0 t) + B\sin(\omega_0 t)$: điều kiện $x(0) = A = 0.01$ và $\dot{x}(0) = B\omega_0 = 0 \Rightarrow B = 0$. Vậy $x(t) = 0.01\cos(\omega_0 t)$.

---

### Câu 4 (Tự luận mở)

Trong công việc thiết kế hệ thống cơ điện tử, bạn thường gặp cộng hưởng cơ khí (mechanical resonance) là một vấn đề nghiêm trọng. Hãy mô tả một tình huống cụ thể trong thiết kế hệ thống đo lường chính xác hoặc vũ khí của bạn, trong đó tần số cộng hưởng $f_0 = \frac{1}{2\pi}\sqrt{k/m}$ của một thành phần gây ra vấn đề, và giải thích cách bạn sử dụng kiến thức về harmonic oscillator để giải quyết.

**Gợi ý đáp án:** Trong thiết kế bệ gá đầu đo laser interferometer cho hệ đo micro-mét: cột đỡ kim loại có tần số cộng hưởng $f_0$ khoảng 80 Hz do $k$ (độ cứng uốn) và $m$ (khối lượng phân bố). Khi máy bơm chân không gần đó tạo rung động 60 Hz (gần $f_0$), biên độ dao động cột đỡ tăng mạnh do cộng hưởng, gây sai số đo vượt quá 10 µm. Giải pháp: (1) Tăng $k$ bằng cách thêm gân tăng cứng → tăng $f_0$ lên 200 Hz; (2) Thêm bộ giảm chấn (vibration isolator) cao su silicon ở chân bệ để giảm hệ số khuếch đại cộng hưởng Q; (3) Đặt lịch đo ngoài giờ có nguồn rung động.

```json
{"questions":[{"id":"q1","type":"mcq","question":"Accelerometer MEMS có proof mass m = 2 µg và spring constant k = 0.2 N/m. Tần số cộng hưởng f0 bằng bao nhiêu?","options":["A. f0 ≈ 1592 Hz","B. f0 ≈ 500 Hz","C. f0 ≈ 2251 Hz","D. f0 ≈ 318 Hz"],"answer":"A","explanation":"ω0 = sqrt(k/m) = sqrt(0.2/2e-9) = sqrt(1e8) = 1e4 rad/s. f0 = ω0/(2π) = 10000/6.283 ≈ 1592 Hz."},{"id":"q2","type":"mcq","question":"Phương trình d²x/dt² = -ω₀²x có nghiệm tổng quát là:","options":["A. x(t) = Ae^(ω₀t) + Be^(-ω₀t)","B. x(t) = Acos(ω₀t) + Bsin(ω₀t)","C. x(t) = At·cos(ω₀t)","D. x(t) = Aω₀²t² + Bt"],"answer":"B","explanation":"Thử x = cos(ω₀t): x'' = -ω₀²cos(ω₀t) = -ω₀²x. Thỏa mãn. Tương tự sin(ω₀t). Nghiệm tổng quát là tổ hợp tuyến tính hai nghiệm độc lập."},{"id":"q3","type":"mcq","question":"Hệ lò xo-khối lượng với x(0) = 0.01 m và ẋ(0) = 0. Nghiệm x(t) là:","options":["A. x(t) = 0.01sin(ω₀t)","B. x(t) = 0.01cos(ω₀t)","C. x(t) = 0.01e^(-ω₀t)","D. x(t) = 0.01(1-cos(ω₀t))"],"answer":"B","explanation":"x(t) = Acos(ω₀t) + Bsin(ω₀t). Từ x(0)=A=0.01 và ẋ(0)=Bω₀=0 → B=0. Vậy x(t) = 0.01cos(ω₀t)."},{"id":"q4","type":"open","question":"Trong thiết kế hệ đo lường chính xác hoặc hệ vũ khí của bạn, hãy mô tả một tình huống cụ thể mà tần số cộng hưởng f0 = (1/2π)√(k/m) của một thành phần gây ra vấn đề, và giải thích cách dùng kiến thức harmonic oscillator để giải quyết.","sample_answer":"Ví dụ: cột đỡ đầu đo laser interferometer có f0 ≈ 80 Hz, gần tần số rung động 60 Hz của thiết bị phụ trợ. Cộng hưởng gây biên độ dao động lớn, sai số đo vượt 10 µm. Giải pháp: tăng k (thêm gân tăng cứng) để đẩy f0 lên 200 Hz, và thêm vibration isolator để giảm Q-factor tại cộng hưởng."}]}
```


## Quiz Questions

**Q1:** Accelerometer MEMS có proof mass m = 2 µg và spring constant k = 0.2 N/m. Tần số cộng hưởng f0 bằng bao nhiêu?
- A) A. f0 ≈ 1592 Hz
- B) B. f0 ≈ 500 Hz
- C) C. f0 ≈ 2251 Hz
- D) D. f0 ≈ 318 Hz

**Correct:** A

**Explanation:** ω0 = sqrt(k/m) = sqrt(0.2/2e-9) = sqrt(1e8) = 1e4 rad/s. f0 = ω0/(2π) = 10000/6.283 ≈ 1592 Hz.

**Q2:** Phương trình d²x/dt² = -ω₀²x có nghiệm tổng quát là:
- A) A. x(t) = Ae^(ω₀t) + Be^(-ω₀t)
- B) B. x(t) = Acos(ω₀t) + Bsin(ω₀t)
- C) C. x(t) = At·cos(ω₀t)
- D) D. x(t) = Aω₀²t² + Bt

**Correct:** B

**Explanation:** Thử x = cos(ω₀t): x'' = -ω₀²cos(ω₀t) = -ω₀²x. Thỏa mãn. Tương tự sin(ω₀t). Nghiệm tổng quát là tổ hợp tuyến tính hai nghiệm độc lập.

**Q3:** Hệ lò xo-khối lượng với x(0) = 0.01 m và ẋ(0) = 0. Nghiệm x(t) là:
- A) A. x(t) = 0.01sin(ω₀t)
- B) B. x(t) = 0.01cos(ω₀t)
- C) C. x(t) = 0.01e^(-ω₀t)
- D) D. x(t) = 0.01(1-cos(ω₀t))

**Correct:** B

**Explanation:** x(t) = Acos(ω₀t) + Bsin(ω₀t). Từ x(0)=A=0.01 và ẋ(0)=Bω₀=0 → B=0. Vậy x(t) = 0.01cos(ω₀t).

**Q4:** Trong thiết kế hệ đo lường chính xác hoặc hệ vũ khí của bạn, hãy mô tả một tình huống cụ thể mà tần số cộng hưởng f0 = (1/2π)√(k/m) của một thành phần gây ra vấn đề, và giải thích cách dùng kiến thức harmonic oscillator để giải quyết.

**Correct:** N/A


---
*Exported from Feynman Bot*
