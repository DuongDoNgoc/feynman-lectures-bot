---
lesson_id: 5490
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:06.394757+00:00"
content_hash: b2c192e56278
chapter_number: 23
chapter_title: Chapter 23
section_number: 4
section_title: 23–3Electrical resonance
---
# ## Quiz: Cộng Hưởng Trong Mạch Điện RLC

*Source: Chapter 23 - Chapter 23 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_23.html)*

## Quiz: Cộng Hưởng Trong Mạch Điện RLC

### Câu 1 (Trắc nghiệm)
Trong mạch RLC nối tiếp, tần số cộng hưởng $\omega_0$ là tần số tại đó:

A. Điện áp trên điện trở $R$ đạt cực đại bằng đúng điện áp nguồn EMF
B. Cảm kháng bằng dung kháng ($\omega L = 1/(\omega C)$), dòng điện đạt cực đại
C. Tổng điện áp trên cuộn cảm $L$ và tụ điện $C$ đạt cực đại
D. Điện áp trên tụ điện $C$ bằng không

**Đáp án: B**
*Giải thích:* Tại cộng hưởng, phần ảo của trở kháng phức triệt tiêu: $X = \omega_0 L - 1/(\omega_0 C) = 0$, nên $\omega_0 = 1/\sqrt{LC}$. Tổng trở kháng $|Z| = R$ (cực tiểu), dòng điện $I = \mathcal{E}_0/R$ (cực đại). Lưu ý: $V_L$ và $V_C$ riêng lẻ đều đạt $Q\mathcal{E}_0$ tại cộng hưởng, không phải bằng không.

---

### Câu 2 (Trắc nghiệm)
Tụ điện $C$ trong mạch điện tương đương với phần tử nào trong hệ dao động cơ học?

A. Khối lượng $m$ (quán tính)
B. Hệ số cản $\gamma m$
C. Lò xo với độ cứng $k = 1/C$
D. Lực ngoài cưỡng bức $F(t)$

**Đáp án: C**
*Giải thích:* Điện áp tụ $V_C = q/C$ tỉ lệ với điện tích $q$ (tương đương dịch chuyển $x$), giống lực lò xo $F = kx$ tỉ lệ với $x$. Hằng số lò xo $k$ tương đương $1/C$ trong bảng tương đồng cơ–điện.

---

### Câu 3 (Trắc nghiệm)
Mạch RLC nối tiếp có $L = 10\,\text{mH}$, $C = 1\,\mu\text{F}$, $R = 10\,\Omega$. Hệ số phẩm chất $Q$ bằng:

A. $Q = 1$
B. $Q = 10$
C. $Q = 100$
D. $Q = 0{,}1$

**Đáp án: B**
*Giải thích:* $\omega_0 = 1/\sqrt{LC} = 1/\sqrt{10^{-2} \times 10^{-6}} = 1/10^{-4} = 10^4\,\text{rad/s}$. Hệ số $Q = \omega_0 L/R = 10^4 \times 10^{-2} / 10 = 10$.

---

### Câu 4 (Tự luận mở)
**Câu hỏi:** Trong thiết kế hệ thống đo chính xác micrometer, tụ điện ký sinh (parasitic capacitance) và điện cảm ký sinh (parasitic inductance) của dây dẫn và PCB trace ảnh hưởng đến tần số cộng hưởng thực tế của mạch đo. Hãy giải thích cơ chế ảnh hưởng này và đề xuất ít nhất hai biện pháp kỹ thuật để kiểm soát tác động của ký sinh trong mạch đo tần số cao.

**Gợi ý trả lời mẫu:** Điện cảm và điện dung ký sinh làm thay đổi giá trị $L_{eff}$ và $C_{eff}$ thực tế so với giá trị danh định, kéo theo $\omega_0 = 1/\sqrt{L_{eff}C_{eff}}$ dịch chuyển và Q giảm. Ký sinh cũng tạo thêm các cộng hưởng phụ gây nhiễu trong dải tần đo. Biện pháp: (1) thiết kế PCB với ground plane liên tục để giảm điện cảm ký sinh của via và trace; (2) dùng tụ decoupling đặt sát linh kiện để ngắn mạch ký sinh; (3) mô phỏng bằng SPICE với mô hình linh kiện thực có parasitics; (4) đo kiểm bằng VNA (vector network analyzer) để đặc trưng hóa trở kháng thực tế và so sánh với thiết kế.

```json
{
  "questions": [
    {"id": "q1", "type": "mcq", "question": "Trong mạch RLC nối tiếp, tần số cộng hưởng ω0 xảy ra khi nào?", "options": ["A. Điện áp trên R đạt cực đại bằng EMF nguồn", "B. ωL = 1/(ωC), dòng điện đạt cực đại", "C. Tổng điện áp trên L và C đạt cực đại", "D. Điện áp trên tụ C bằng không"], "answer": "B", "explanation": "Tại cộng hưởng X = ωL - 1/(ωC) = 0, |Z| = R là cực tiểu, dòng điện I = E0/R là cực đại."},
    {"id": "q2", "type": "mcq", "question": "Tụ điện C trong mạch điện tương đương phần tử nào trong hệ dao động cơ học?", "options": ["A. Khối lượng m", "B. Hệ số cản γm", "C. Lò xo với độ cứng k = 1/C", "D. Lực ngoài cưỡng bức"], "answer": "C", "explanation": "V_C = q/C tỉ lệ với q (như F = k*x tỉ lệ x). k tương đương 1/C."},
    {"id": "q3", "type": "mcq", "question": "Mạch RLC với L = 10mH, C = 1μF, R = 10Ω. Hệ số Q bằng:", "options": ["A. Q = 1", "B. Q = 10", "C. Q = 100", "D. Q = 0,1"], "answer": "B", "explanation": "ω0 = 1/sqrt(10e-3 * 1e-6) = 10^4 rad/s. Q = ω0*L/R = 10^4 * 10^(-2)/10 = 10."},
    {"id": "q4", "type": "open", "question": "Tụ và điện cảm ký sinh trong PCB ảnh hưởng đến tần số cộng hưởng thực tế của mạch đo như thế nào? Đề xuất biện pháp kiểm soát.", "sample_answer": "Ký sinh làm thay đổi L_eff và C_eff, dịch chuyển ω0 và giảm Q. Biện pháp: ground plane liên tục, tụ decoupling sát linh kiện, mô phỏng SPICE với parasitic model, đo kiểm bằng VNA."}
  ]
}
```


## Quiz Questions

**Q1:** Trong mạch RLC nối tiếp, tần số cộng hưởng ω0 xảy ra khi nào?
- A) A. Điện áp trên R đạt cực đại bằng EMF nguồn
- B) B. ωL = 1/(ωC), dòng điện đạt cực đại
- C) C. Tổng điện áp trên L và C đạt cực đại
- D) D. Điện áp trên tụ C bằng không

**Correct:** B

**Explanation:** Tại cộng hưởng X = ωL - 1/(ωC) = 0, |Z| = R là cực tiểu, dòng điện I = E0/R là cực đại.

**Q2:** Tụ điện C trong mạch điện tương đương phần tử nào trong hệ dao động cơ học?
- A) A. Khối lượng m
- B) B. Hệ số cản γm
- C) C. Lò xo với độ cứng k = 1/C
- D) D. Lực ngoài cưỡng bức

**Correct:** C

**Explanation:** V_C = q/C tỉ lệ với q (như F = k*x tỉ lệ x). k tương đương 1/C.

**Q3:** Mạch RLC với L = 10mH, C = 1μF, R = 10Ω. Hệ số Q bằng:
- A) A. Q = 1
- B) B. Q = 10
- C) C. Q = 100
- D) D. Q = 0,1

**Correct:** B

**Explanation:** ω0 = 1/sqrt(10e-3 * 1e-6) = 10^4 rad/s. Q = ω0*L/R = 10^4 * 10^(-2)/10 = 10.

**Q4:** Tụ và điện cảm ký sinh trong PCB ảnh hưởng đến tần số cộng hưởng thực tế của mạch đo như thế nào? Đề xuất biện pháp kiểm soát.

**Correct:** N/A


---
*Exported from Feynman Bot*
