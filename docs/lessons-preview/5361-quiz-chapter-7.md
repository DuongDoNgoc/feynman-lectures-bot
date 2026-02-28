---
lesson_id: 5361
lesson_type: quiz
approval_status: pending
exported_at: "2026-02-28T11:31:20.686972+00:00"
content_hash: 957a043c76c4
chapter_number: 7
chapter_title: Chapter 7
section_number: 8
section_title: 7–7What is gravity?
---
# ## Quiz: Luc Hap Dan va Luc Dien Tu — So Sanh Cuong Do

*Source: Chapter 7 - Chapter 7 (Section 8) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_07.html)*

## Quiz: Luc Hap Dan va Luc Dien Tu — So Sanh Cuong Do

**Cau 1:** Ti so luc Coulomb tren luc hap dan giua hai electron xap xi bang:

A. $10^{10}$
B. $10^{20}$
C. $10^{42}$
D. $10^{60}$

**Dap an: C** — $F_e/F_g \approx 4.17 \times 10^{42}$. Ti so nay la hang so khong thich nghi (dimensionless), khong phu thuoc khoang cach giua cac hat.

---

**Cau 2:** Tai sao luc hap dan chi phoi cau truc vu tru lon (thien ha, sao, hanh tinh) mac du rat yeu?

A. Hap dan truyen nhanh hon luc dien
B. Dien tich trung hoa (triet tieu), con khoi luong luon duong (cong lai)
C. Hap dan co tam xa xa hon
D. Hanh tinh khong co dien tich

**Dap an: B** — Vat chat trung hoa ve dien (dien tich net = 0) nen luc dien triet tieu o thang lon. Khoi luong khong co dau am, nen luc hap dan luon cong lai khi them vat chat.

---

**Cau 3:** Cam bien dung luong (capacitive sensor) va cam bien cam ung (inductive sensor) deu dua tren nguyen ly dien tu. Neu duoc dung 'cam bien hap dan' co do nhay tuong duong, kich thuoc can tang bao nhieu lan so voi cam bien dung luong 1 cm?

A. Khoang $10^{10}$ lan
B. Khoang $10^{21}$ lan
C. Khoang $10^{42}$ lan
D. Chi can tang $10^3$ lan

**Dap an: B** — Luc $\propto$ (kich thuoc)^2 (doi voi ca hai luc). De bu ti so $4.17 \times 10^{42}$, can tang kich thuoc len $\sqrt{4.17 \times 10^{42}} \approx 2 \times 10^{21}$ lan. Bat kha thi trong thuc te.

---

**Cau 4 (Tu luan):** Feynman nhan xet rang cac dinh luat vat ly co 'tinh tru tuong' — mo ta hanh vi ma khong co co che. Ban co the lien he dieu nay voi cach ban dung mo hinh toan hoc trong thiet ke he thong dieu khien (PID, transfer function, state space) khong? Su tru tuong la diem manh hay yeu?

**Goi y tra loi:** Transfer function $G(s)$ mo ta hanh vi dau vao-dau ra ma khong can biet chi tiet vat ly ben trong (do la 'black box'). Tuong tu $F = ma$ mo ta hanh vi khoi luong ma khong giai thich 'co che' cua quan tinh. Su tru tuong la MANH: (1) Mo hinh $G(s)$ ap dung cho nhieu he thong khac nhau (dien, co, nhiet); (2) Cho phep thiet ke robust controller khong can biet tham so vat ly chinh xac; (3) Ngan xep nhieu lop (layered abstraction) cho phep quan ly do phuc tap. Diem yeu: mat di insight vat ly o muc co ban — khi he thong hanh xu bat thuong, 'black box' kho debug hon.

```json
{"questions": [
  {"id": "q1", "type": "mcq", "question": "Ti so luc Coulomb tren luc hap dan giua hai electron xap xi bang:", "options": ["A. 10^10", "B. 10^20", "C. 10^42", "D. 10^60"], "answer": "C", "explanation": "F_e/F_g = e^2/(4*pi*eps0) / (G*me^2) = 4.17e42. Hang so khong thich nghi, khong phu thuoc khoang cach."},
  {"id": "q2", "type": "mcq", "question": "Tai sao hap dan chi phoi vu tru lon mac du rat yeu?", "options": ["A. Hap dan truyen nhanh hon", "B. Dien tich trung hoa (triet tieu), khoi luong luon duong (cong lai)", "C. Hap dan co tam xa xa hon", "D. Hanh tinh khong co dien tich"], "answer": "B", "explanation": "Vat chat trung hoa dien nen F_e net = 0 o thang lon. Khoi luong luon duong nen F_g cong lai."},
  {"id": "q3", "type": "mcq", "question": "Cam bien hap dan co do nhay tuong duong cam bien dung luong 1 cm can kich thuoc lon hon bao nhieu?", "options": ["A. 10^10 lan", "B. 10^21 lan", "C. 10^42 lan", "D. 10^3 lan"], "answer": "B", "explanation": "De bu ti so F_e/F_g = 4.17e42, can tang kich thuoc sqrt(4.17e42) ~ 2e21 lan. Bat kha thi."},
  {"id": "q4", "type": "open", "question": "Lien he tinh tru tuong cua dinh luat vat ly voi mo hinh toan hoc trong thiet ke dieu khien. Manh hay yeu?", "sample_answer": "Transfer function G(s) mo ta hanh vi ma khong can biet vat ly ben trong — giong F=ma mo ta quan tinh khong giai thich co che. Manh: ap dung rong, thiet ke robust, quan ly phuc tap. Yeu: kho debug khi he thong hanh xu bat thuong."}
]}
```


## Quiz Questions

**Q1:** Ti so luc Coulomb tren luc hap dan giua hai electron xap xi bang:
- A) A. 10^10
- B) B. 10^20
- C) C. 10^42
- D) D. 10^60

**Correct:** C

**Explanation:** F_e/F_g = e^2/(4*pi*eps0) / (G*me^2) = 4.17e42. Hang so khong thich nghi, khong phu thuoc khoang cach.

**Q2:** Tai sao hap dan chi phoi vu tru lon mac du rat yeu?
- A) A. Hap dan truyen nhanh hon
- B) B. Dien tich trung hoa (triet tieu), khoi luong luon duong (cong lai)
- C) C. Hap dan co tam xa xa hon
- D) D. Hanh tinh khong co dien tich

**Correct:** B

**Explanation:** Vat chat trung hoa dien nen F_e net = 0 o thang lon. Khoi luong luon duong nen F_g cong lai.

**Q3:** Cam bien hap dan co do nhay tuong duong cam bien dung luong 1 cm can kich thuoc lon hon bao nhieu?
- A) A. 10^10 lan
- B) B. 10^21 lan
- C) C. 10^42 lan
- D) D. 10^3 lan

**Correct:** B

**Explanation:** De bu ti so F_e/F_g = 4.17e42, can tang kich thuoc sqrt(4.17e42) ~ 2e21 lan. Bat kha thi.

**Q4:** Lien he tinh tru tuong cua dinh luat vat ly voi mo hinh toan hoc trong thiet ke dieu khien. Manh hay yeu?

**Correct:** N/A


---
*Exported from Feynman Bot*
