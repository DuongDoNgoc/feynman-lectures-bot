---
lesson_id: 5475
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-02T15:10:30.413605+00:00"
content_hash: d24134a3fb22
chapter_number: 21
chapter_title: Chapter 21
section_number: 4
section_title: 21–3Harmonic motion and circular motion
---
# ## Quiz: Dao Động Điều Hòa và Chuyển Động Tròn

*Source: Chapter 21 - Chapter 21 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_21.html)*

## Quiz: Dao Động Điều Hòa và Chuyển Động Tròn

### Câu 1 (Trắc nghiệm)

Một hạt chuyển động tròn đều bán kính $R = 0.05$ m với tốc độ góc $\omega_0 = 100$ rad/s. Gia tốc thành phần $x$ khi hạt ở vị trí $x = 0.03$ m là bao nhiêu?

A. $a_x = +300$ m/s²  
B. $a_x = -300$ m/s²  
C. $a_x = -500$ m/s²  
D. $a_x = +500$ m/s²  

**Đáp án: B**  
**Giải thích:** $a_x = -\omega_0^2 x = -(100)^2 \times 0.03 = -10000 \times 0.03 = -300$ m/s². Dấu âm phản ánh gia tốc hướng vào tâm (ngược chiều $x$ dương).

---

### Câu 2 (Trắc nghiệm)

Trong lock-in amplifier, sau khi nhân tín hiệu $V_s = A\cos(\omega_0 t + \phi)$ với $\cos(\omega_0 t)$ và lọc thông thấp, output $X$ bằng:

A. $X = A\cos(\phi)$  
B. $X = \frac{A}{2}\cos(\phi)$  
C. $X = A\cos(2\omega_0 t + \phi)$  
D. $X = \frac{A}{2}\cos(2\omega_0 t)$  

**Đáp án: B**  
**Giải thích:** $\cos(\omega_0 t + \phi)\cos(\omega_0 t) = \frac{1}{2}[\cos(\phi) + \cos(2\omega_0 t + \phi)]$. Sau lọc thông thấp, thành phần $2\omega_0$ bị loại, còn lại $X = \frac{A}{2}\cos\phi$.

---

### Câu 3 (Trắc nghiệm)

Một hệ harmonic oscillator bắt đầu từ $x(0) = 0$ và $\dot{x}(0) = v_0 = \omega_0 C$ (vận tốc ban đầu). Hằng số tích phân $A$ và $a$ trong nghiệm $x(t) = A\cos(\omega_0 t) + a\sin(\omega_0 t)$ là:

A. $A = C$, $a = 0$  
B. $A = 0$, $a = C$  
C. $A = C/2$, $a = C/2$  
D. $A = C$, $a = C$  

**Đáp án: B**  
**Giải thích:** $x(0) = A = 0$. $\dot{x}(0) = a\omega_0 = v_0 = \omega_0 C \Rightarrow a = C$. Vậy $x(t) = C\sin(\omega_0 t)$ — thuần sine khi bắt đầu tại tâm với vận tốc ban đầu.

---

### Câu 4 (Tự luận mở)

Trong hệ thống đo lường hoặc điều khiển chính xác của bạn, hãy giải thích cách mối liên hệ giữa dao động điều hòa và chuyển động tròn được khai thác thực tế. Ví dụ: resolver trong servo motor, lock-in amplifier, FFT phân tích rung động, hoặc encoder quadrature. Giải thích tại sao biểu diễn phức (phasor) đơn giản hóa phân tích so với xử lý sin/cos riêng lẽ.

**Gợi ý đáp án:** Trong hệ điều khiển servo của cơ cấu định vị chính xác (ví dụ stage chuyển động micro-mét), resolver phát ra tín hiệu $V_{\sin} \propto \sin\theta$ và $V_{\cos} \propto \cos\theta$ — hai thành phần của một phasor $\tilde{V} = V_0 e^{i\theta}$. Mạch R/D converter tính $\theta = \arctan(V_{\sin}/V_{\cos})$ trong miền phức, cho kết quả góc 16-bit. Biểu diễn phức thống nhất hai kênh tín hiệu thành một đối tượng toán học duy nhất, giúp phân tích phase noise, tracking error, và loop gain trong miền tần số đơn giản hơn nhiều so với xử lý sin và cos riêng lẽ.

```json
{"questions":[{"id":"q1","type":"mcq","question":"Hạt chuyển động tròn đều R = 0.05 m, ω₀ = 100 rad/s. Gia tốc thành phần x khi x = 0.03 m là bao nhiêu?","options":["A. ax = +300 m/s²","B. ax = -300 m/s²","C. ax = -500 m/s²","D. ax = +500 m/s²"],"answer":"B","explanation":"ax = -ω₀²x = -(100)²×0.03 = -300 m/s². Dấu âm: gia tốc hướng vào tâm (hướng tâm luôn ngược chiều vị trí từ tâm)."},{"id":"q2","type":"mcq","question":"Trong lock-in amplifier, sau khi nhân Vs = Acos(ω₀t + φ) với cos(ω₀t) và lọc thông thấp, output X bằng:","options":["A. X = Acos(φ)","B. X = (A/2)cos(φ)","C. X = Acos(2ω₀t + φ)","D. X = (A/2)cos(2ω₀t)"],"answer":"B","explanation":"cos(ω₀t+φ)·cos(ω₀t) = (1/2)[cos(φ) + cos(2ω₀t+φ)]. Sau LPF loại thành phần 2ω₀, còn lại X = (A/2)cos(φ)."},{"id":"q3","type":"mcq","question":"Harmonic oscillator x(0)=0, ẋ(0)=v₀=ω₀C. Các hằng số A, a trong x(t)=Acos(ω₀t)+asin(ω₀t) là:","options":["A. A=C, a=0","B. A=0, a=C","C. A=C/2, a=C/2","D. A=C, a=C"],"answer":"B","explanation":"x(0)=A=0. ẋ(0)=aω₀=ω₀C → a=C. Nghiệm: x(t)=Csin(ω₀t) — thuần sine khi khởi đầu tại tâm với vận tốc ban đầu."},{"id":"q4","type":"open","question":"Trong hệ đo lường hoặc điều khiển chính xác của bạn, hãy giải thích cách mối liên hệ dao động-chuyển động tròn được khai thác thực tế (resolver, lock-in, FFT, encoder quadrature). Tại sao biểu diễn phức đơn giản hóa phân tích?","sample_answer":"Resolver trong servo motor định vị: phát tín hiệu V_sin = V₀sin(ωt)sinθ và V_cos = V₀sin(ωt)cosθ — hai thành phần phasor e^{iθ}. R/D converter tính θ = arctan(V_sin/V_cos) trong miền phức. Biểu diễn phức thống nhất hai kênh thành một phasor, phân tích loop gain và phase margin trong miền tần số đơn giản hơn nhiều so với xử lý sin/cos riêng lẽ."}]}
```


## Quiz Questions

**Q1:** Hạt chuyển động tròn đều R = 0.05 m, ω₀ = 100 rad/s. Gia tốc thành phần x khi x = 0.03 m là bao nhiêu?
- A) A. ax = +300 m/s²
- B) B. ax = -300 m/s²
- C) C. ax = -500 m/s²
- D) D. ax = +500 m/s²

**Correct:** B

**Explanation:** ax = -ω₀²x = -(100)²×0.03 = -300 m/s². Dấu âm: gia tốc hướng vào tâm (hướng tâm luôn ngược chiều vị trí từ tâm).

**Q2:** Trong lock-in amplifier, sau khi nhân Vs = Acos(ω₀t + φ) với cos(ω₀t) và lọc thông thấp, output X bằng:
- A) A. X = Acos(φ)
- B) B. X = (A/2)cos(φ)
- C) C. X = Acos(2ω₀t + φ)
- D) D. X = (A/2)cos(2ω₀t)

**Correct:** B

**Explanation:** cos(ω₀t+φ)·cos(ω₀t) = (1/2)[cos(φ) + cos(2ω₀t+φ)]. Sau LPF loại thành phần 2ω₀, còn lại X = (A/2)cos(φ).

**Q3:** Harmonic oscillator x(0)=0, ẋ(0)=v₀=ω₀C. Các hằng số A, a trong x(t)=Acos(ω₀t)+asin(ω₀t) là:
- A) A. A=C, a=0
- B) B. A=0, a=C
- C) C. A=C/2, a=C/2
- D) D. A=C, a=C

**Correct:** B

**Explanation:** x(0)=A=0. ẋ(0)=aω₀=ω₀C → a=C. Nghiệm: x(t)=Csin(ω₀t) — thuần sine khi khởi đầu tại tâm với vận tốc ban đầu.

**Q4:** Trong hệ đo lường hoặc điều khiển chính xác của bạn, hãy giải thích cách mối liên hệ dao động-chuyển động tròn được khai thác thực tế (resolver, lock-in, FFT, encoder quadrature). Tại sao biểu diễn phức đơn giản hóa phân tích?

**Correct:** N/A


---
*Exported from Feynman Bot*
