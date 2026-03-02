---
lesson_id: 5394
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-02T15:10:28.337021+00:00"
content_hash: ad17d7db502e
chapter_number: 12
chapter_title: Chapter 12
section_number: 1
section_title: 12Characteristics of Force
---
# ## Quiz: Đặc Tính của Lực và Trường

*Source: Chapter 12 - Chapter 12 (Section 1) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_12.html)*

## Quiz: Đặc Tính của Lực và Trường

**Câu 1.** Lực nào sau đây là lực **cơ bản** (fundamental), không phải lực thực nghiệm xấp xỉ?

A. Lực cản không khí $F \approx cv^2$
B. Lực ma sát trượt $F = \mu_k N$
C. Lực điện trường $\mathbf{F} = q\mathbf{E}$
D. Lực đàn hồi lò xo $F = -kx$

**Đáp án: C** — Lực điện trường là lực cơ bản, xuất phát từ phương trình Maxwell, chính xác tuyệt đối. Lực cản và ma sát là xấp xỉ thực nghiệm; Hooke chỉ đúng trong giới hạn đàn hồi.

---

**Câu 2.** Ưu điểm của khái niệm **trường** (field) so với khái niệm "tác dụng từ xa":

A. Tính toán nhanh hơn
B. Tách rời nguồn và vật chịu lực — trường tồn tại độc lập trong không gian
C. Chỉ áp dụng cho lực điện từ
D. Loại bỏ nhu cầu tính lực

**Đáp án: B** — Khái niệm trường: vật A tạo trường $\mathbf{E}$ trong không gian, trường tác dụng lên vật B. Trường tồn tại độc lập, ngay cả khi không có vật B. Điều này quan trọng trong sóng điện từ (trường truyền đi không cần vật chất).

---

**Câu 3.** Trong điều khiển servo chính xác (micro-mét), lực ma sát gây hiện tượng "stick-slip". Nguyên nhân cơ bản là:

A. Lực ma sát tĩnh lớn hơn lực ma sát động
B. Lực ma sát luôn bằng không khi vật đứng yên
C. Bộ điều khiển PID không đủ mạnh
D. Lực ma sát tỷ lệ tuyến tính với vận tốc

**Đáp án: A** — Khi bộ điều khiển tăng lực dần, vật không chuyển động cho đến khi vượt qua lực ma sát tĩnh $F_s > F_k$. Khi vượt qua, lực đột ngột giảm xuống $F_k$ → vật "nhảy" — gây stick-slip. Hiện tượng này là lý do model Coulomb đơn giản không đủ cho điều khiển chính xác.

---

**Câu 4 (Tự luận).** Trong hệ thống vũ khí dẫn đường sử dụng con quay hồi chuyển (gyroscope) với ổ trục từ trường (magnetic bearing), giải thích tại sao ổ trục từ trường được ưu tiên hơn ổ trục cơ khí (ball bearing) về phương diện mô hình hóa lực.

**Gợi ý đáp án:** Ổ từ trường: lực tỷ lệ với $i^2/x^2$ — tuân theo định luật điện từ cơ bản, tính toán được từ hằng số vật liệu và hình học. Mô hình hóa chính xác → bộ điều khiển model-based hoạt động tốt. Ổ bi cơ khí: ma sát phụ thuộc nhiệt độ, mài mòn, bôi trơn — khó mô hình hóa, thay đổi theo thời gian → bộ điều khiển phải thích nghi (adaptive) hoặc bù thực nghiệm. Ngoài ra, ổ từ không tiếp xúc → không mài mòn, không cần bôi trơn, phù hợp với yêu cầu độ tin cậy cao của vũ khí.

```json
{
  "questions": [
    {"id": "q1", "type": "mcq", "question": "Lực nào là lực cơ bản (fundamental)?", "options": ["A. Lực cản F≈cv²", "B. Ma sát F=μN", "C. Lực điện trường F=qE", "D. Lực lò xo F=-kx"], "answer": "C", "explanation": "Lực điện trường từ phương trình Maxwell — cơ bản, chính xác. Cản/ma sát là xấp xỉ thực nghiệm; Hooke chỉ đúng trong giới hạn đàn hồi."},
    {"id": "q2", "type": "mcq", "question": "Ưu điểm chính của khái niệm trường:", "options": ["A. Tính nhanh hơn", "B. Tách rời nguồn và vật chịu lực — trường tồn tại độc lập", "C. Chỉ cho điện từ", "D. Loại bỏ tính lực"], "answer": "B", "explanation": "Trường tồn tại trong không gian độc lập với vật nhận lực — nền tảng của sóng điện từ."},
    {"id": "q3", "type": "mcq", "question": "Stick-slip trong servo chính xác gây ra bởi:", "options": ["A. Lực ma sát tĩnh > ma sát động", "B. Ma sát = 0 khi đứng yên", "C. PID không đủ mạnh", "D. Ma sát tuyến tính với vận tốc"], "answer": "A", "explanation": "F_s > F_k → khi vượt qua ngưỡng tĩnh, lực đột ngột giảm → vật nhảy. Cần bù ma sát (friction compensation)."},
    {"id": "q4", "type": "open", "question": "Tại sao ổ từ trường được ưu tiên hơn ổ bi trong gyroscope vũ khí từ góc nhìn mô hình hóa lực?", "sample_answer": "Ổ từ: lực = f(i,x) theo luật EM cơ bản, tính được từ lý thuyết → model-based control. Ổ bi: ma sát phức tạp, thay đổi theo thời gian → cần bù thực nghiệm. Ổ từ không tiếp xúc, không mài mòn, độ tin cậy cao hơn."}
  ]
}
```


## Quiz Questions

**Q1:** Lực nào là lực cơ bản (fundamental)?
- A) A. Lực cản F≈cv²
- B) B. Ma sát F=μN
- C) C. Lực điện trường F=qE
- D) D. Lực lò xo F=-kx

**Correct:** C

**Explanation:** Lực điện trường từ phương trình Maxwell — cơ bản, chính xác. Cản/ma sát là xấp xỉ thực nghiệm; Hooke chỉ đúng trong giới hạn đàn hồi.

**Q2:** Ưu điểm chính của khái niệm trường:
- A) A. Tính nhanh hơn
- B) B. Tách rời nguồn và vật chịu lực — trường tồn tại độc lập
- C) C. Chỉ cho điện từ
- D) D. Loại bỏ tính lực

**Correct:** B

**Explanation:** Trường tồn tại trong không gian độc lập với vật nhận lực — nền tảng của sóng điện từ.

**Q3:** Stick-slip trong servo chính xác gây ra bởi:
- A) A. Lực ma sát tĩnh > ma sát động
- B) B. Ma sát = 0 khi đứng yên
- C) C. PID không đủ mạnh
- D) D. Ma sát tuyến tính với vận tốc

**Correct:** A

**Explanation:** F_s > F_k → khi vượt qua ngưỡng tĩnh, lực đột ngột giảm → vật nhảy. Cần bù ma sát (friction compensation).

**Q4:** Tại sao ổ từ trường được ưu tiên hơn ổ bi trong gyroscope vũ khí từ góc nhìn mô hình hóa lực?

**Correct:** N/A


---
*Exported from Feynman Bot*
