---
lesson_id: 5616
lesson_type: quiz
approval_status: pending
exported_at: "2026-03-03T15:33:09.150932+00:00"
content_hash: d778ac72e691
chapter_number: 37
chapter_title: Chapter 37
section_number: 2
section_title: 37–1Atomic mechanics
---
# ## Quiz: Nhập Môn Cơ Học Lượng Tử — Từ Wave-Particle Duality đến Uncertainty

*Source: Chapter 37 - Chapter 37 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_37.html)*

## Quiz: Nhập Môn Cơ Học Lượng Tử — Từ Wave-Particle Duality đến Uncertainty

Kiểm tra hiểu biết về các nguyên lý cơ bản của cơ học lượng tử và ứng dụng trong kỹ thuật đo lường chính xác.

---

### Câu 1 (Trắc nghiệm)
Trong thí nghiệm khe đôi với electron, điều gì xảy ra khi ta đặt detector ở một khe để xác định electron đi qua khe nào?

A. Pattern giao thoa mờ đi một chút nhưng vẫn còn nhìn thấy
B. Pattern giao thoa biến mất hoàn toàn, chỉ còn hai vạch tương ứng hai khe
C. Tốc độ electron giảm xuống
D. Electron bị hấp thụ bởi detector và không đến màn cuối

**Đáp án: B**
*Giải thích*: Theo nguyên lý bổ sung (complementarity) của Bohr: không thể quan sát đồng thời hành vi sóng (giao thoa) và hành vi hạt (biết đi qua khe nào). Việc đo "which-path information" phá hủy sự chồng chất (superposition) của hàm sóng qua hai khe, xóa hoàn toàn pattern giao thoa. Đây không phải do tác động vật lý của detector mà do bản chất lượng tử cơ bản.

---

### Câu 2 (Trắc nghiệm)
Bước sóng de Broglie của electron tăng khi nào?

A. Khi năng lượng electron tăng
B. Khi khối lượng electron tăng
C. Khi động lượng electron giảm (electron chậm hơn): $\lambda = h/p$
D. Khi điện tích electron tăng

**Đáp án: C**
*Giải thích*: Công thức de Broglie $\lambda = h/p = h/(mv)$. Bước sóng **tỉ lệ nghịch** với động lượng. Electron chậm hơn có $p$ nhỏ hơn, dẫn đến $\lambda$ lớn hơn — tức là hành vi sóng rõ ràng hơn. Ngược lại, electron nhanh (năng lượng cao) có $\lambda$ nhỏ hơn, hành vi giống hạt hơn ở cấp độ quan sát.

---

### Câu 3 (Trắc nghiệm)
Hiệu ứng tunnel (quantum tunneling) được ứng dụng trong thiết bị đo lường nào với độ phân giải sub-Angstrom?

A. Kính hiển vi quang học (optical microscope) — giới hạn nhiễu xạ $\sim \lambda/2$
B. Kính hiển vi điện tử quét (SEM) — phân giải $\sim 1$ nm bằng nhiễu xạ electron
C. Scanning Tunneling Microscope (STM) — dòng tunnel $I \propto e^{-2\kappa z}$ cho phép phân giải nguyên tử
D. Atomic Force Microscope (AFM) ở chế độ tiếp xúc — phân giải do lực van der Waals

**Đáp án: C**
*Giải thích*: STM dùng hiệu ứng tunnel: khi đầu kim loại cách bề mặt $\sim 1$ Å, dòng tunnel thay đổi **10 lần** mỗi khi khoảng cách thay đổi 1 Å. Độ nhạy theo hàm mũ này cho phép đo topography bề mặt với độ phân giải sub-Angstrom — quan sát và thao tác từng nguyên tử đơn lẻ. SEM và AFM tiếp xúc không dùng tunnel effect.

---

### Câu 4 (Tự luận mở)
**Câu hỏi**: Nguyên lý bất định Heisenberg $\Delta x \cdot \Delta p \geq \hbar/2$ đặt ra giới hạn cơ bản cho mọi phép đo. Là kỹ sư cơ điện tử thiết kế cảm biến MEMS (Micro-Electro-Mechanical Systems) để đo gia tốc hoặc rung với độ chính xác tiệm cận giới hạn vật lý, hãy giải thích: (1) Khi nào giới hạn lượng tử trở nên quan trọng trong hệ MEMS thực tế? (2) Kỹ thuật **squeezed state measurement** giúp vượt qua Standard Quantum Limit như thế nào?

**Gợi ý trả lời mẫu**:
1. *Khi nào giới hạn lượng tử quan trọng*:
   Standard Quantum Limit (SQL) cho MEMS oscillator: $\Delta x_{SQL} = \sqrt{\hbar/(m\omega)}$. Với accelerometer MEMS tiêu biểu: mass $m = 1$ μg, tần số cộng hưởng $f_0 = 1$ kHz:
   $$\Delta x_{SQL} = \sqrt{\frac{1.055 \times 10^{-34}}{10^{-9} \times 6283}} \approx 4 \text{ fm}$$
   Cảm biến gia tốc MEMS tốt nhất hiện nay (Allan deviation $\sim 1$ ng/$\sqrt{\text{Hz}}$) tương ứng độ nhạy vị trí $\sim 10^{-14}$ m/$\sqrt{\text{Hz}}$ — đã trong vùng $10 \times$ của SQL! Với hệ MEMS quang-cơ (optomechanical) làm lạnh về ground state, giới hạn lượng tử trực tiếp chi phối.

2. *Squeezed state measurement*:
   Nguyên lý bất định cho phép "dồn" bất định từ một biến ($\Delta x$) sang biến liên hợp ($\Delta p$), miễn là tích $\Delta x \cdot \Delta p \geq \hbar/2$. Trong đo lường vị trí (position measurement), dùng **back-action evading** hoặc **variational measurement**: chỉ đo một quadrature của oscillator (ví dụ chỉ đo $x$ tại phase nhất định, bỏ qua $p$), có thể đạt $\Delta x < \Delta x_{SQL}$ về một chiều. Ứng dụng: interferometer LIGO dùng squeezed light để giảm shot noise, nâng cao sensitivity phát hiện sóng hấp dẫn xuống $10^{-23}$ m/$\sqrt{\text{Hz}}$ — nhỏ hơn $10^{-9}$ đường kính proton!

---

```json
{
  "questions": [
    {"id": "q1", "type": "mcq", "question": "Trong thí nghiệm khe đôi với electron, điều gì xảy ra khi đặt detector ở một khe để biết electron đi qua khe nào?", "options": ["A. Pattern giao thoa mờ đi nhưng vẫn còn", "B. Pattern giao thoa biến mất hoàn toàn, chỉ còn hai vạch", "C. Tốc độ electron giảm xuống", "D. Electron bị hấp thụ bởi detector"], "answer": "B", "explanation": "Đo which-path information phá hủy superposition hàm sóng, xóa hoàn toàn pattern giao thoa (nguyên lý complementarity của Bohr)."},
    {"id": "q2", "type": "mcq", "question": "Bước sóng de Broglie của electron tăng khi nào?", "options": ["A. Khi năng lượng electron tăng", "B. Khi khối lượng electron tăng", "C. Khi động lượng electron giảm (electron chậm hơn): λ = h/p", "D. Khi điện tích electron tăng"], "answer": "C", "explanation": "λ = h/p = h/(mv). Bước sóng tỉ lệ nghịch với động lượng — electron chậm có λ lớn hơn, hành vi sóng rõ ràng hơn."},
    {"id": "q3", "type": "mcq", "question": "Hiệu ứng tunnel được ứng dụng trong thiết bị đo lường nào với độ phân giải sub-Angstrom?", "options": ["A. Kính hiển vi quang học — giới hạn λ/2", "B. SEM — nhiễu xạ electron, phân giải ~1nm", "C. Scanning Tunneling Microscope (STM) — dòng tunnel I ∝ e^(-2κz), phân giải nguyên tử", "D. AFM tiếp xúc — lực van der Waals"], "answer": "C", "explanation": "STM dùng hiệu ứng tunnel: dòng thay đổi 10 lần mỗi 1Å khoảng cách. Độ nhạy hàm mũ này cho phép phân giải sub-Angstrom, quan sát từng nguyên tử."},
    {"id": "q4", "type": "open", "question": "Là kỹ sư thiết kế cảm biến MEMS tiệm cận giới hạn vật lý, hãy giải thích: (1) Khi nào giới hạn lượng tử quan trọng trong MEMS? (2) Squeezed state measurement giúp vượt qua Standard Quantum Limit như thế nào?", "sample_answer": "1. SQL cho MEMS: Δx_SQL = √(ℏ/mω) ≈ 4 fm với m=1μg, f=1kHz. Cảm biến MEMS tốt nhất đã trong vùng 10× SQL. 2. Squeezed measurement 'dồn' bất định từ Δx sang Δp (back-action evading), đo một quadrature, đạt Δx < Δx_SQL về một chiều — nguyên lý LIGO dùng để đạt 10^-23 m/√Hz."}
  ]
}
```


## Quiz Questions

**Q1:** Trong thí nghiệm khe đôi với electron, điều gì xảy ra khi đặt detector ở một khe để biết electron đi qua khe nào?
- A) A. Pattern giao thoa mờ đi nhưng vẫn còn
- B) B. Pattern giao thoa biến mất hoàn toàn, chỉ còn hai vạch
- C) C. Tốc độ electron giảm xuống
- D) D. Electron bị hấp thụ bởi detector

**Correct:** B

**Explanation:** Đo which-path information phá hủy superposition hàm sóng, xóa hoàn toàn pattern giao thoa (nguyên lý complementarity của Bohr).

**Q2:** Bước sóng de Broglie của electron tăng khi nào?
- A) A. Khi năng lượng electron tăng
- B) B. Khi khối lượng electron tăng
- C) C. Khi động lượng electron giảm (electron chậm hơn): λ = h/p
- D) D. Khi điện tích electron tăng

**Correct:** C

**Explanation:** λ = h/p = h/(mv). Bước sóng tỉ lệ nghịch với động lượng — electron chậm có λ lớn hơn, hành vi sóng rõ ràng hơn.

**Q3:** Hiệu ứng tunnel được ứng dụng trong thiết bị đo lường nào với độ phân giải sub-Angstrom?
- A) A. Kính hiển vi quang học — giới hạn λ/2
- B) B. SEM — nhiễu xạ electron, phân giải ~1nm
- C) C. Scanning Tunneling Microscope (STM) — dòng tunnel I ∝ e^(-2κz), phân giải nguyên tử
- D) D. AFM tiếp xúc — lực van der Waals

**Correct:** C

**Explanation:** STM dùng hiệu ứng tunnel: dòng thay đổi 10 lần mỗi 1Å khoảng cách. Độ nhạy hàm mũ này cho phép phân giải sub-Angstrom, quan sát từng nguyên tử.

**Q4:** Là kỹ sư thiết kế cảm biến MEMS tiệm cận giới hạn vật lý, hãy giải thích: (1) Khi nào giới hạn lượng tử quan trọng trong MEMS? (2) Squeezed state measurement giúp vượt qua Standard Quantum Limit như thế nào?

**Correct:** N/A


---
*Exported from Feynman Bot*
