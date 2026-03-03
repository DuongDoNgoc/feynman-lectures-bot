---
lesson_id: 5586
lesson_type: quiz
approval_status: pending
exported_at: "2026-03-03T15:33:08.629203+00:00"
content_hash: 41181641d82f
chapter_number: 34
chapter_title: Chapter 34
section_number: 7
section_title: 34–6The Doppler effect
---
# ## Quiz: Hiệu Ứng Doppler và Nguồn Sáng Chuyển Động

*Source: Chapter 34 - Chapter 34 (Section 7) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_34.html)*

## Quiz: Hiệu Ứng Doppler và Nguồn Sáng Chuyển Động

---

**Câu 1.** Một nguyên tử phát tần số $\omega_1$ đang chuyển động về phía người quan sát với vận tốc $v \ll c$. Tần số người quan sát nhận được là:

A. $\omega_{obs} = \omega_1(1 + v/c)$  
B. $\omega_{obs} = \omega_1(1 - v/c)$  
C. $\omega_{obs} = \omega_1/(1 - v/c)$  
D. $\omega_{obs} = \omega_1\cdot c/(c - v/2)$  

**Đáp án: C**  
Giải thích: Khi nguồn tiến lại gần, chu kỳ quan sát được rút ngắn: $T_{obs} = T_1(1 - v/c)$, suy ra $\omega_{obs} = \omega_1/(1 - v/c) > \omega_1$ — blueshift. Đáp án A là xấp xỉ bậc nhất của C khi $v \ll c$ nhưng không chính xác.

---

**Câu 2.** Điều gì đúng về **transverse Doppler effect** (nguồn chuyển động vuông góc với đường nhìn, $	heta = 90°$)?

A. Không có Doppler shift vì thành phần vận tốc hướng vào người quan sát bằng 0  
B. Có Doppler shift $\omega_{obs} = \omega_1/\gamma < \omega_1$ do time dilation tương đối tính  
C. Có Doppler shift $\omega_{obs} = \omega_1\gamma > \omega_1$ do length contraction  
D. Chỉ xảy ra với âm thanh, không xảy ra với ánh sáng  

**Đáp án: B**  
Giải thích: Ngay cả khi nguồn chuyển động vuông góc, đồng hồ của nguồn chạy chậm hơn do time dilation → tần số phát (trong hệ lab) thấp hơn: $\omega_{obs} = \omega_1/\gamma$. Đây là hiệu ứng thuần tương đối tính, không có trong âm học.

---

**Câu 3.** Trong hệ thống Laser Doppler Vibrometer (LDV) dùng giao thoa kế đơn giản (không có AOM), vấn đề **direction ambiguity** xuất hiện khi nào?

A. Khi bề mặt rung với biên độ lớn hơn $\lambda/4$  
B. Khi vận tốc bề mặt đổi dấu (qua điểm không), vì tín hiệu beat đối xứng không phân biệt được chiều  
C. Khi tần số rung lớn hơn băng thông photodetector  
D. Khi chùm laser không vuông góc với bề mặt  

**Đáp án: B**  
Giải thích: Tín hiệu giao thoa đơn giản $\propto \cos(2\pi\Delta f \cdot t)$ có tính đối xứng — $+\Delta f$ và $-\Delta f$ cho cùng tín hiệu. Khi $v$ đổi dấu, không phân biệt được. Giải pháp: thêm AOM offset tần số reference (heterodyne), tạo bias carrier $f_{AOM} = 40$ MHz.

---

**Câu 4 (Tự luận).** Bạn đang thiết kế hệ thống đo rung động của đầu đạn trong ống nòng bằng LDV (λ = 633 nm). Mục tiêu rung với tần số $f = 5$ kHz và biên độ $A = 2$ μm. (a) Tính vận tốc đỉnh và Doppler shift đỉnh. (b) Nếu dùng heterodyne LDV với AOM offset $f_{AOM} = 40$ MHz, dải tần số beat signal cần đo là bao nhiêu? (c) Tại sao cần heterodyne thay vì đo trực tiếp tần số Doppler?

**Gợi ý trả lời:**  
(a) $v_{peak} = A\omega = 2	imes10^{-6} 	imes 2\pi 	imes 5000 pprox 62.8$ mm/s.  
$\Delta f_{peak} = 2v_{peak}/\lambda = 2	imes0.0628/633	imes10^{-9} pprox 198.4$ kHz.  
(b) Beat signal: $f_{beat} = f_{AOM} \pm \Delta f(t) = 40$ MHz $\pm$ 198 kHz → dải $[39.8, 40.2]$ MHz. Cần photodetector và ADC với bandwidth $\geq 40.2$ MHz, sampling rate $\geq 80$ MSa/s.  
(c) Heterodyne giải quyết direction ambiguity: khi $v$ đổi dấu, $f_{beat}$ thay đổi từ $(40 + \Delta f)$ MHz xuống $(40 - \Delta f)$ MHz — hai giá trị khác nhau → phân biệt được chiều dương/âm. Đo trực tiếp không phân biệt được chiều rung.

---

```json
{
  "questions": [
    {"id": "q1", "type": "mcq", "question": "Nguyên tử phát tần số ω₁ tiến lại gần người quan sát với v≪c. Tần số quan sát được là?", "options": ["A. ω_obs = ω₁(1+v/c)", "B. ω_obs = ω₁(1-v/c)", "C. ω_obs = ω₁/(1-v/c)", "D. ω_obs = ω₁·c/(c-v/2)"], "answer": "C", "explanation": "T_obs = T₁(1-v/c) → ω_obs = ω₁/(1-v/c) > ω₁, blueshift."},
    {"id": "q2", "type": "mcq", "question": "Điều gì đúng về transverse Doppler effect (θ=90°)?", "options": ["A. Không có Doppler shift vì thành phần vận tốc hướng về người quan sát = 0", "B. Có Doppler shift ω_obs = ω₁/γ < ω₁ do time dilation tương đối tính", "C. Có Doppler shift ω_obs = ω₁γ > ω₁ do length contraction", "D. Chỉ xảy ra với âm thanh"], "answer": "B", "explanation": "Time dilation làm đồng hồ nguồn chậm hơn → tần số phát trong hệ lab thấp hơn: ω_obs = ω₁/γ — hiệu ứng thuần tương đối tính."},
    {"id": "q3", "type": "mcq", "question": "Direction ambiguity trong LDV giao thoa kế đơn giản xuất hiện khi nào?", "options": ["A. Khi biên độ rung > λ/4", "B. Khi vận tốc bề mặt đổi dấu vì cos(Δf·t) đối xứng", "C. Khi tần số rung > bandwidth photodetector", "D. Khi chùm laser không vuông góc bề mặt"], "answer": "B", "explanation": "cos(+Δf·t) = cos(-Δf·t) — không phân biệt được chiều. Heterodyne (AOM) tạo bias carrier giải quyết vấn đề này."},
    {"id": "q4", "type": "open", "question": "LDV (λ=633nm) đo rung động f=5kHz, biên độ A=2μm: (a) vận tốc đỉnh và Doppler shift đỉnh; (b) dải beat signal với AOM 40MHz; (c) tại sao cần heterodyne?", "sample_answer": "(a) v_peak≈62.8 mm/s, Δf_peak≈198 kHz. (b) Beat: 40MHz±198kHz → cần BW≥40.2MHz. (c) Heterodyne phân biệt chiều rung: f_beat > hay < 40MHz → v>0 hay v<0."}
  ]
}
```


## Quiz Questions

**Q1:** Nguyên tử phát tần số ω₁ tiến lại gần người quan sát với v≪c. Tần số quan sát được là?
- A) A. ω_obs = ω₁(1+v/c)
- B) B. ω_obs = ω₁(1-v/c)
- C) C. ω_obs = ω₁/(1-v/c)
- D) D. ω_obs = ω₁·c/(c-v/2)

**Correct:** C

**Explanation:** T_obs = T₁(1-v/c) → ω_obs = ω₁/(1-v/c) > ω₁, blueshift.

**Q2:** Điều gì đúng về transverse Doppler effect (θ=90°)?
- A) A. Không có Doppler shift vì thành phần vận tốc hướng về người quan sát = 0
- B) B. Có Doppler shift ω_obs = ω₁/γ < ω₁ do time dilation tương đối tính
- C) C. Có Doppler shift ω_obs = ω₁γ > ω₁ do length contraction
- D) D. Chỉ xảy ra với âm thanh

**Correct:** B

**Explanation:** Time dilation làm đồng hồ nguồn chậm hơn → tần số phát trong hệ lab thấp hơn: ω_obs = ω₁/γ — hiệu ứng thuần tương đối tính.

**Q3:** Direction ambiguity trong LDV giao thoa kế đơn giản xuất hiện khi nào?
- A) A. Khi biên độ rung > λ/4
- B) B. Khi vận tốc bề mặt đổi dấu vì cos(Δf·t) đối xứng
- C) C. Khi tần số rung > bandwidth photodetector
- D) D. Khi chùm laser không vuông góc bề mặt

**Correct:** B

**Explanation:** cos(+Δf·t) = cos(-Δf·t) — không phân biệt được chiều. Heterodyne (AOM) tạo bias carrier giải quyết vấn đề này.

**Q4:** LDV (λ=633nm) đo rung động f=5kHz, biên độ A=2μm: (a) vận tốc đỉnh và Doppler shift đỉnh; (b) dải beat signal với AOM 40MHz; (c) tại sao cần heterodyne?

**Correct:** N/A


---
*Exported from Feynman Bot*
