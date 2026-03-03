---
lesson_id: 5580
lesson_type: quiz
approval_status: pending
exported_at: "2026-03-03T15:33:08.453221+00:00"
content_hash: d20d5df4e1bc
chapter_number: 34
chapter_title: Chapter 34
section_number: 2
section_title: 34–1Moving sources
---
# ## Quiz: Bức Xạ Từ Nguồn Chuyển Động và Điện Động Lực Học Cổ Điển

*Source: Chapter 34 - Chapter 34 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_34.html)*

## Quiz: Bức Xạ Từ Nguồn Chuyển Động và Điện Động Lực Học Cổ Điển

Bài kiểm tra này kiểm tra hiểu biết về điện trường bức xạ, nguyên lý retarded potential, và các hệ quả thực tế từ nguồn sáng chuyển động.

---

**Câu 1.** Theo lý thuyết bức xạ cổ điển của Feynman, điện trường tại điểm quan sát xa nguồn tỉ lệ với đại lượng nào sau đây?

A. Vận tốc tức thời của điện tích tại thời điểm quan sát  
B. Gia tốc của điện tích tại thời điểm quan sát  
C. Đạo hàm bậc hai theo thời gian của vector đơn vị hướng biểu kiến $\hat{e}_{R'}$  
D. Vị trí hiện tại của điện tích tại thời điểm quan sát  

**Đáp án: C**  
Giải thích: Điện trường bức xạ $\mathbf{E} = -rac{q}{4\piarepsilon_0 r'^2}rac{d^2\hat{e}_{R'}}{dt^2}$. Vector $\hat{e}_{R'}$ chỉ theo hướng **biểu kiến** (retarded) từ điện tích đến người quan sát. Điện tích không tăng tốc góc thì không bức xạ.

---

**Câu 2.** Điện trường bức xạ liên quan đến từ trường qua biểu thức nào?

A. $\mathbf{B} = \mathbf{E}/c$, song song với $\mathbf{E}$  
B. $\mathbf{B} = -\hat{e}_{R'} 	imes \mathbf{E}/c$, vuông góc với cả $\mathbf{E}$ và $\hat{e}_{R'}$  
C. $\mathbf{B} = 
abla 	imes \mathbf{E}$, chỉ phụ thuộc vào gradient không gian  
D. $\mathbf{B} = \hat{e}_{R'} \cdot \mathbf{E}/c$, theo hướng nhìn tới nguồn  

**Đáp án: B**  
Giải thích: Từ trường $\mathbf{B} = -\hat{e}_{R'} 	imes \mathbf{E}/c$ luôn vuông góc với $\mathbf{E}$ và vuông góc với hướng biểu kiến $\hat{e}_{R'}$ đến nguồn — điều này đảm bảo sóng điện từ ngang (transverse).

---

**Câu 3.** Một nguồn sáng phát tần số $\omega_1$ đang tiến lại gần người quan sát với vận tốc $v \ll c$. Tần số quan sát được (classical Doppler) là bao nhiêu?

A. $\omega_{obs} = \omega_1(1 - v/c)$  
B. $\omega_{obs} = \omega_1/(1 + v/c)$  
C. $\omega_{obs} = \omega_1/(1 - v/c)$  
D. $\omega_{obs} = \omega_1\sqrt{1 - v^2/c^2}$  

**Đáp án: C**  
Giải thích: Khi nguồn tiến lại gần, chu kỳ quan sát được rút ngắn: $T_{obs} = T_1(1-v/c)$, nên tần số tăng lên $\omega_{obs} = \omega_1/(1-v/c)$ — hiệu ứng blueshift.

---

**Câu 4 (Tự luận).** Trong hệ thống Laser Doppler Velocimetry (LDV) mà bạn tích hợp vào máy đo rung động của cơ cấu chấp hành (actuator) ở cấp micromet: (a) Giải thích cơ chế vật lý cho phép LDV đo vận tốc mà không tiếp xúc. (b) Với laser $\lambda = 633$ nm và actuator rung với biên độ $\pm 5\ \mu	ext{m}$ ở tần số $1\ 	ext{kHz}$, ước tính dải tần Doppler shift cần đo và yêu cầu về bandwidth của photodetector.

**Gợi ý trả lời:**  
(a) LDV chiếu chùm laser vào bề mặt chuyển động. Ánh sáng phản xạ bị dịch tần số Doppler $\Delta f = 2v(t)/\lambda$ do chuyển động của bề mặt. Giao thoa với chùm tham chiếu tạo tín hiệu beat tần số $\Delta f$ tại photodetector. Giải điều chế cho ra $v(t)$; tích phân cho $x(t)$.  
(b) Vận tốc đỉnh: $v_{peak} = A\omega = 5	imes10^{-6} 	imes 2\pi 	imes 10^3 pprox 31.4\ 	ext{mm/s}$. Doppler shift đỉnh: $\Delta f_{peak} = 2 	imes 31.4	imes10^{-3}/633	imes10^{-9} pprox 99\ 	ext{kHz}$. Photodetector cần bandwidth tối thiểu $\sim 100\ 	ext{kHz}$ với noise floor đủ thấp để phân giải vận tốc nhỏ nhất tương ứng dịch chuyển ~nanometer.

---

```json
{
  "questions": [
    {"id": "q1", "type": "mcq", "question": "Điện trường bức xạ tại điểm quan sát xa nguồn tỉ lệ với đại lượng nào?", "options": ["A. Vận tốc tức thời của điện tích", "B. Gia tốc của điện tích tại thời điểm quan sát", "C. Đạo hàm bậc hai theo thời gian của vector đơn vị hướng biểu kiến", "D. Vị trí hiện tại của điện tích"], "answer": "C", "explanation": "E ∝ d²ê_R'/dt² — đạo hàm bậc hai của hướng biểu kiến, phản ánh gia tốc góc của hướng nhìn tới nguồn."},
    {"id": "q2", "type": "mcq", "question": "Từ trường trong sóng điện từ bức xạ liên hệ với điện trường qua biểu thức nào?", "options": ["A. B = E/c, song song với E", "B. B = -ê_R' × E/c, vuông góc với E và ê_R'", "C. B = ∇×E", "D. B = ê_R'·E/c"], "answer": "B", "explanation": "B = -ê_R' × E/c đảm bảo sóng ngang (transverse), B vuông góc E và vuông góc hướng truyền."},
    {"id": "q3", "type": "mcq", "question": "Nguồn phát tần số ω₁ tiến lại gần người quan sát với vận tốc v≪c. Tần số quan sát được là?", "options": ["A. ω₁(1-v/c)", "B. ω₁/(1+v/c)", "C. ω₁/(1-v/c)", "D. ω₁√(1-v²/c²)"], "answer": "C", "explanation": "Chu kỳ rút ngắn T_obs = T₁(1-v/c), suy ra ω_obs = ω₁/(1-v/c) — blueshift."},
    {"id": "q4", "type": "open", "question": "Trong LDV đo rung động actuator: (a) giải thích cơ chế vật lý; (b) với λ=633nm, biên độ ±5μm, f=1kHz, ước tính dải Doppler shift và yêu cầu bandwidth photodetector.", "sample_answer": "(a) Ánh sáng phản xạ bị Doppler shift Δf=2v/λ; giao thoa với reference cho beat frequency = Δf → giải điều chế → v(t). (b) v_peak ≈ 31.4 mm/s → Δf_peak ≈ 99 kHz → cần bandwidth ≥ 100 kHz."}
  ]
}
```


## Quiz Questions

**Q1:** Điện trường bức xạ tại điểm quan sát xa nguồn tỉ lệ với đại lượng nào?
- A) A. Vận tốc tức thời của điện tích
- B) B. Gia tốc của điện tích tại thời điểm quan sát
- C) C. Đạo hàm bậc hai theo thời gian của vector đơn vị hướng biểu kiến
- D) D. Vị trí hiện tại của điện tích

**Correct:** C

**Explanation:** E ∝ d²ê_R'/dt² — đạo hàm bậc hai của hướng biểu kiến, phản ánh gia tốc góc của hướng nhìn tới nguồn.

**Q2:** Từ trường trong sóng điện từ bức xạ liên hệ với điện trường qua biểu thức nào?
- A) A. B = E/c, song song với E
- B) B. B = -ê_R' × E/c, vuông góc với E và ê_R'
- C) C. B = ∇×E
- D) D. B = ê_R'·E/c

**Correct:** B

**Explanation:** B = -ê_R' × E/c đảm bảo sóng ngang (transverse), B vuông góc E và vuông góc hướng truyền.

**Q3:** Nguồn phát tần số ω₁ tiến lại gần người quan sát với vận tốc v≪c. Tần số quan sát được là?
- A) A. ω₁(1-v/c)
- B) B. ω₁/(1+v/c)
- C) C. ω₁/(1-v/c)
- D) D. ω₁√(1-v²/c²)

**Correct:** C

**Explanation:** Chu kỳ rút ngắn T_obs = T₁(1-v/c), suy ra ω_obs = ω₁/(1-v/c) — blueshift.

**Q4:** Trong LDV đo rung động actuator: (a) giải thích cơ chế vật lý; (b) với λ=633nm, biên độ ±5μm, f=1kHz, ước tính dải Doppler shift và yêu cầu bandwidth photodetector.

**Correct:** N/A


---
*Exported from Feynman Bot*
