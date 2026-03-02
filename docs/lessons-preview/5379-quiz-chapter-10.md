---
lesson_id: 5379
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-02T15:10:27.926618+00:00"
content_hash: 79684e8771b0
chapter_number: 10
chapter_title: Chapter 10
section_number: 4
section_title: 10–3Momentumisconserved!
---
# ## Quiz: Thực Nghiệm Bảo Toàn Động Lượng

*Source: Chapter 10 - Chapter 10 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_10.html)*

## Quiz: Thực Nghiệm Bảo Toàn Động Lượng

**Câu 1.** Trên máng khí, hai xe bằng nhau ($m = 250\,\text{g}$) đứng yên được nổ tách ra bởi lò xo. Xe A đo được $v_A = 0.40\,\text{m/s}$ sang phải. Vận tốc xe B là:

A. $0\,\text{m/s}$
B. $0.20\,\text{m/s}$ sang phải
C. $0.40\,\text{m/s}$ sang trái
D. $0.80\,\text{m/s}$ sang phải

---

**Câu 2.** Xe A ($m = 400\,\text{g}$, $v = 0.6\,\text{m/s}$) va chạm không đàn hồi với xe B ($m = 200\,\text{g}$, đứng yên). Vận tốc sau va chạm là:

A. $0.3\,\text{m/s}$
B. $0.4\,\text{m/s}$
C. $0.6\,\text{m/s}$
D. $0.2\,\text{m/s}$

---

**Câu 3.** Trong thực nghiệm trên máng khí, nguồn sai số nào có ảnh hưởng lớn nhất đến kết quả?

A. Nhiệt độ không khí thay đổi
B. Ma sát nhỏ còn lại do đệm khí không hoàn hảo
C. Biến động điện áp nguồn cấp
D. Rung động từ môi trường xung quanh

---

**Câu 4 (Tự luận).** Bạn cần xây dựng hệ thống kiểm tra vận tốc đạn (ballistic chronograph) cho phòng thử nghiệm đạn dược. Yêu cầu độ chính xác $\pm 0.5\,\text{m/s}$ tại $v_0 = 800\,\text{m/s}$. Thiết kế hệ đo (chọn khoảng cách giữa cổng quang, độ phân giải đồng hồ cần thiết) và phân tích ngân sách sai số.

---

```json
{"questions": [
  {"id": "q1", "type": "mcq", "question": "Hai xe bằng nhau trên máng khí, nổ từ đứng yên. Xe A: vA=0.40 m/s sang phải. Vận tốc xe B là bao nhiêu?", "options": ["A. 0 m/s", "B. 0.20 m/s sang phải", "C. 0.40 m/s sang trái", "D. 0.80 m/s sang phải"], "answer": "C", "explanation": "Bảo toàn động lượng từ đứng yên: 0 = m×vA + m×vB → vB = -vA = -0.40 m/s = 0.40 m/s sang trái. Hai xe bằng nhau bay ra với tốc độ bằng nhau ngược chiều."},
  {"id": "q2", "type": "mcq", "question": "Xe A (m=400g, v=0.6m/s) va chạm không đàn hồi với xe B (m=200g, đứng yên). Vận tốc sau va chạm là bao nhiêu?", "options": ["A. 0.3 m/s", "B. 0.4 m/s", "C. 0.6 m/s", "D. 0.2 m/s"], "answer": "B", "explanation": "V = m₁v₁/(m₁+m₂) = (0.4×0.6)/(0.4+0.2) = 0.24/0.6 = 0.4 m/s."},
  {"id": "q3", "type": "mcq", "question": "Trên máng khí, nguồn sai số nào ảnh hưởng lớn nhất?", "options": ["A. Nhiệt độ không khí thay đổi", "B. Ma sát nhỏ còn lại do đệm khí không hoàn hảo", "C. Biến động điện áp nguồn", "D. Rung động từ môi trường"], "answer": "B", "explanation": "Ma sát còn lại trực tiếp làm thay đổi động lượng của xe theo thời gian, ảnh hưởng trực tiếp đến kết quả đo. Các yếu tố khác có ảnh hưởng thứ yếu hoặc gián tiếp. Máng khí tốt có ma sát ≈0.1 mN, đủ nhỏ nhưng vẫn cần hiệu chỉnh trong thực nghiệm chính xác."},
  {"id": "q4", "type": "open", "question": "Thiết kế ballistic chronograph: độ chính xác ±0.5 m/s tại v₀=800 m/s. Chọn L và độ phân giải đồng hồ, phân tích ngân sách sai số.", "sample_answer": "Yêu cầu: δv/v = 0.5/800 = 0.0625% → phân bổ đều cho L và Δt: mỗi nguồn ≤ 0.044%. Chọn L=1.000 m: δL cần ≤ 0.044%×1000mm = 0.44mm → dùng thước chuẩn ±0.1mm (thừa yêu cầu). Tại v=800m/s, Δt=L/v=1.25ms; cần δt/Δt ≤ 0.044% → δt ≤ 0.044%×1.25ms = 0.55μs → đồng hồ phân giải 0.1μs (100ns), dễ đạt với oscillator quartz TCXO. Kiểm tra: δv = v×√((δL/L)²+(δt/Δt)²) = 800×√((0.1/1000)²+(0.1/1250)²) = 800×√(10⁻⁸+6.4×10⁻⁹) = 800×1.27×10⁻⁴ = 0.10 m/s << 0.5 m/s. Thực tế cần thêm: trigger jitter của cổng quang (<0.5μs), căn chỉnh trục cổng với đường đạn (<1mrad)."}
]}
```



## Quiz Questions

**Q1:** Hai xe bằng nhau trên máng khí, nổ từ đứng yên. Xe A: vA=0.40 m/s sang phải. Vận tốc xe B là bao nhiêu?
- A) A. 0 m/s
- B) B. 0.20 m/s sang phải
- C) C. 0.40 m/s sang trái
- D) D. 0.80 m/s sang phải

**Correct:** C

**Explanation:** Bảo toàn động lượng từ đứng yên: 0 = m×vA + m×vB → vB = -vA = -0.40 m/s = 0.40 m/s sang trái. Hai xe bằng nhau bay ra với tốc độ bằng nhau ngược chiều.

**Q2:** Xe A (m=400g, v=0.6m/s) va chạm không đàn hồi với xe B (m=200g, đứng yên). Vận tốc sau va chạm là bao nhiêu?
- A) A. 0.3 m/s
- B) B. 0.4 m/s
- C) C. 0.6 m/s
- D) D. 0.2 m/s

**Correct:** B

**Explanation:** V = m₁v₁/(m₁+m₂) = (0.4×0.6)/(0.4+0.2) = 0.24/0.6 = 0.4 m/s.

**Q3:** Trên máng khí, nguồn sai số nào ảnh hưởng lớn nhất?
- A) A. Nhiệt độ không khí thay đổi
- B) B. Ma sát nhỏ còn lại do đệm khí không hoàn hảo
- C) C. Biến động điện áp nguồn
- D) D. Rung động từ môi trường

**Correct:** B

**Explanation:** Ma sát còn lại trực tiếp làm thay đổi động lượng của xe theo thời gian, ảnh hưởng trực tiếp đến kết quả đo. Các yếu tố khác có ảnh hưởng thứ yếu hoặc gián tiếp. Máng khí tốt có ma sát ≈0.1 mN, đủ nhỏ nhưng vẫn cần hiệu chỉnh trong thực nghiệm chính xác.

**Q4:** Thiết kế ballistic chronograph: độ chính xác ±0.5 m/s tại v₀=800 m/s. Chọn L và độ phân giải đồng hồ, phân tích ngân sách sai số.

**Correct:** N/A


---
*Exported from Feynman Bot*
