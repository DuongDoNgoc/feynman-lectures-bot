---
lesson_id: 5517
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:06.995021+00:00"
content_hash: fb4b1286170a
chapter_number: 27
chapter_title: Chapter 27
section_number: 2
section_title: 27–1Introduction
---
# ## Quiz: Quang Học Hình Học (Geometrical Optics) - Ứng Dụng Thực Tiễn

*Source: Chapter 27 - Chapter 27 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_27.html)*

## Quiz: Quang Học Hình Học (Geometrical Optics) - Ứng Dụng Thực Tiễn

### Câu 1 (Trắc nghiệm)
Trong quang học hình học, khi một tia sáng đi từ môi trường có chiết suất $n_1$ sang môi trường có chiết suất $n_2$ qua một bề mặt cong bán kính $R$, công thức liên hệ khoảng cách vật $s$ và khoảng cách ảnh $s'$ là:

A. $\frac{n_1}{s} + \frac{n_2}{s'} = \frac{n_2 - n_1}{R}$

B. $\frac{n_2}{s} + \frac{n_1}{s'} = \frac{n_1 - n_2}{R}$

C. $\frac{n_1}{s} - \frac{n_2}{s'} = \frac{n_2 + n_1}{R}$

D. $\frac{1}{s} + \frac{1}{s'} = \frac{1}{R}$

**Đáp án: A**
*Giải thích:* Đây là công thức tổng quát cho bề mặt khúc xạ đơn. Khi $n_1 = 1$ (không khí) thì ta thu được dạng quen thuộc hơn. Công thức này xuất phát từ nguyên lý thời gian cực tiểu (principle of least time) của Fermat.

---

### Câu 2 (Trắc nghiệm)
Phương trình $\Delta \approx \frac{h^2}{2s}$ trong quang học hình học dùng để tính:

A. Độ lệch pha của tia sáng khi đi qua thấu kính

B. Hiệu đường đi (path length difference) giữa tia xiên và tia trục trong tam giác có cạnh đáy $s$ và chiều cao $h$

C. Bước sóng hiệu dụng của ánh sáng trong môi trường chiết suất $n$

D. Năng lượng mất mát do tán xạ tại bề mặt phân cách

**Đáp án: B**
*Giải thích:* Đây là công thức hình học cơ bản: nếu có một tam giác với đáy $d$ và chiều cao $h$ nhỏ, thì cạnh huyền $s$ dài hơn đáy một lượng $\Delta \approx h^2/2s$. Đây là nền tảng để chứng minh điều kiện hội tụ của bề mặt cong.

---

### Câu 3 (Trắc nghiệm)
Lý thuyết quang học hình học của Hamilton (Hamiltonian optics) quan trọng nhất vì:

A. Nó cho phép tính toán màu sắc của ảnh qua thấu kính

B. Nó giải quyết hoàn toàn vấn đề aberration trong thiết kế thấu kính

C. Nó có ứng dụng sâu rộng trong cơ học giải tích (analytical mechanics), quan trọng hơn cả trong quang học

D. Nó là phương pháp duy nhất để thiết kế hệ quang học đa bề mặt

**Đáp án: C**
*Giải thích:* Feynman nhấn mạnh rằng lý thuyết Hamilton trong quang học thực ra quan trọng hơn trong cơ học. Đây là cầu nối giữa quang học và cơ học lượng tử thông qua nguyên lý tác dụng cực tiểu (principle of least action).

---

### Câu 4 (Tự luận)
**Câu hỏi mở:** Với vai trò là kỹ sư cơ điện tử thiết kế hệ thống điều khiển chính xác ở cấp độ micromet, bạn cần tích hợp một hệ quang học để đo vị trí bằng laser interferometry. Hãy phân tích tại sao việc hiểu nguyên lý quang học hình học (geometrical optics) — đặc biệt là cách tia sáng truyền qua nhiều bề mặt khúc xạ — lại quan trọng trong việc thiết kế đường quang của hệ đo lường này. Nêu ít nhất 2 yếu tố cụ thể mà bạn cần kiểm soát.

**Gợi ý trả lời mẫu:** Trong hệ laser interferometry đo vị trí micromet, quang học hình học quyết định chất lượng chùm tia: (1) *Căn chỉnh quang trục (optical axis alignment)*: mỗi thấu kính, gương, và beam splitter đều là bề mặt khúc xạ/phản xạ; sai lệch nhỏ trong căn chỉnh sẽ dịch chuyển điểm hội tụ hàng chục micromet, gây sai số đo; (2) *Kiểm soát aberration*: với chùm laser có đường kính lớn, spherical aberration làm méo wavefront, ảnh hưởng đến fringe pattern của interferometer; cần dùng thấu kính chất lượng cao (diffraction-limited) hoặc bù aberration bằng hệ nhiều thấu kính.

```json
{
  "questions": [
    {"id": "q1", "type": "mcq", "question": "Công thức liên hệ khoảng cách vật s và khoảng cách ảnh s' qua bề mặt khúc xạ đơn với hai môi trường chiết suất n1 và n2 là:", "options": ["A. n1/s + n2/s' = (n2-n1)/R", "B. n2/s + n1/s' = (n1-n2)/R", "C. n1/s - n2/s' = (n2+n1)/R", "D. 1/s + 1/s' = 1/R"], "answer": "A", "explanation": "Đây là công thức tổng quát cho bề mặt khúc xạ đơn, xuất phát từ nguyên lý thời gian cực tiểu của Fermat."},
    {"id": "q2", "type": "mcq", "question": "Phương trình Delta ≈ h²/2s trong quang học hình học dùng để tính:", "options": ["A. Độ lệch pha của tia sáng", "B. Hiệu đường đi giữa tia xiên và tia trục trong tam giác có đáy s và chiều cao h", "C. Bước sóng hiệu dụng trong môi trường", "D. Năng lượng mất mát do tán xạ"], "answer": "B", "explanation": "Công thức hình học cơ bản: cạnh huyền s dài hơn đáy d một lượng h²/2s, nền tảng chứng minh điều kiện hội tụ."},
    {"id": "q3", "type": "mcq", "question": "Lý thuyết quang học hình học của Hamilton quan trọng nhất vì:", "options": ["A. Cho phép tính màu sắc ảnh", "B. Giải quyết hoàn toàn vấn đề aberration", "C. Có ứng dụng sâu rộng trong cơ học giải tích, quan trọng hơn cả trong quang học", "D. Là phương pháp duy nhất thiết kế hệ đa bề mặt"], "answer": "C", "explanation": "Feynman nhấn mạnh lý thuyết Hamilton trong quang học quan trọng hơn trong cơ học, là cầu nối với cơ học lượng tử."},
    {"id": "q4", "type": "open", "question": "Với vai trò kỹ sư cơ điện tử thiết kế hệ laser interferometry đo vị trí micromet, hãy phân tích tại sao hiểu quang học hình học quan trọng và nêu 2 yếu tố cụ thể cần kiểm soát.", "sample_answer": "(1) Căn chỉnh quang trục: mỗi bề mặt khúc xạ/phản xạ gây dịch chuyển điểm hội tụ nếu không căn chỉnh đúng; (2) Kiểm soát spherical aberration làm méo wavefront của laser, ảnh hưởng fringe pattern interferometer."}
  ]
}
```


## Quiz Questions

**Q1:** Công thức liên hệ khoảng cách vật s và khoảng cách ảnh s' qua bề mặt khúc xạ đơn với hai môi trường chiết suất n1 và n2 là:
- A) A. n1/s + n2/s' = (n2-n1)/R
- B) B. n2/s + n1/s' = (n1-n2)/R
- C) C. n1/s - n2/s' = (n2+n1)/R
- D) D. 1/s + 1/s' = 1/R

**Correct:** A

**Explanation:** Đây là công thức tổng quát cho bề mặt khúc xạ đơn, xuất phát từ nguyên lý thời gian cực tiểu của Fermat.

**Q2:** Phương trình Delta ≈ h²/2s trong quang học hình học dùng để tính:
- A) A. Độ lệch pha của tia sáng
- B) B. Hiệu đường đi giữa tia xiên và tia trục trong tam giác có đáy s và chiều cao h
- C) C. Bước sóng hiệu dụng trong môi trường
- D) D. Năng lượng mất mát do tán xạ

**Correct:** B

**Explanation:** Công thức hình học cơ bản: cạnh huyền s dài hơn đáy d một lượng h²/2s, nền tảng chứng minh điều kiện hội tụ.

**Q3:** Lý thuyết quang học hình học của Hamilton quan trọng nhất vì:
- A) A. Cho phép tính màu sắc ảnh
- B) B. Giải quyết hoàn toàn vấn đề aberration
- C) C. Có ứng dụng sâu rộng trong cơ học giải tích, quan trọng hơn cả trong quang học
- D) D. Là phương pháp duy nhất thiết kế hệ đa bề mặt

**Correct:** C

**Explanation:** Feynman nhấn mạnh lý thuyết Hamilton trong quang học quan trọng hơn trong cơ học, là cầu nối với cơ học lượng tử.

**Q4:** Với vai trò kỹ sư cơ điện tử thiết kế hệ laser interferometry đo vị trí micromet, hãy phân tích tại sao hiểu quang học hình học quan trọng và nêu 2 yếu tố cụ thể cần kiểm soát.

**Correct:** N/A


---
*Exported from Feynman Bot*
