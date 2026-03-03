---
lesson_id: 5613
lesson_type: quiz
approval_status: pending
exported_at: "2026-03-03T15:33:09.083648+00:00"
content_hash: c9fcdfa9da33
chapter_number: 36
chapter_title: Chapter 36
section_number: 6
section_title: 36–5Other eyes
---
# ## Quiz: Thị Giác Màu, Mắt Kép và Mã Hóa Thần Kinh

*Source: Chapter 36 - Chapter 36 (Section 6) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_36.html)*

## Quiz: Thị Giác Màu, Mắt Kép và Mã Hóa Thần Kinh

Kiểm tra hiểu biết về nguyên lý vật lý và thần kinh học của thị giác trong thế giới động vật.

---

### Câu 1 (Trắc nghiệm)
Tại sao khi cường độ ánh sáng tăng gấp đôi, dây thần kinh thị giác không tăng gấp đôi tần số spike mà tăng ít hơn?

A. Vì tế bào thần kinh bị mệt mỏi khi ánh sáng mạnh
B. Vì hệ thần kinh mã hóa theo thang logarithm (Weber-Fechner law) — tần số spike tỉ lệ với $\log(I/I_0)$, không tỉ lệ tuyến tính với $I$
C. Vì iris thu hẹp lại làm giảm lượng ánh sáng vào mắt
D. Vì tế bào nón bị bão hòa ở cường độ cao

**Đáp án: B**
*Giải thích*: Định luật Weber-Fechner mô tả quan hệ $f \propto \log(I/I_0)$. Khi $I$ tăng gấp đôi, $\log(2I/I_0) = \log(I/I_0) + \log 2$ — tăng thêm một lượng **cố định** (tương đương 1 đơn vị log), không phải gấp đôi. Đây là lý do ta dùng thang dB cho âm thanh và thang EV cho ánh sáng — các thang đo "tuyến tính hóa" cảm nhận của hệ thần kinh.

---

### Câu 2 (Trắc nghiệm)
Trong mắt kép của côn trùng, kích thước tối ưu của mỗi facet lens được quyết định bởi điều kiện nào?

A. Phải lớn nhất có thể để thu tối đa ánh sáng
B. Phải nhỏ nhất có thể để có nhiều ommatidia nhất
C. Sự cân bằng giữa giới hạn nhiễu xạ (muốn facet lớn) và mật độ lấy mẫu không gian (muốn facet nhỏ), cho $D_{opt} = \sqrt{2.44\lambda R}$
D. Được quyết định bởi áp lực cơ học của vỏ ngoài côn trùng

**Đáp án: C**
*Giải thích*: Facet lớn hơn → giảm nhiễu xạ → phân giải tốt hơn trong mỗi ommatidium. Nhưng facet lớn hơn cũng đồng nghĩa ít ommatidium hơn → khoảng cách góc giữa các ommatidium lớn hơn → aliasing không gian. Kích thước tối ưu $D_{opt} = \sqrt{2.44\lambda R}$ là điểm cân bằng Nyquist-Rayleigh.

---

### Câu 3 (Trắc nghiệm)
Câu nào mô tả ĐÚNG về thị giác màu trong thế giới động vật?

A. Tất cả động vật có xương sống đều nhìn được màu sắc
B. Hầu hết động vật có vú không nhìn được màu; thị giác màu phát triển ở linh trưởng, chim, cá, bò sát, và nhiều côn trùng
C. Chỉ con người và các loài linh trưởng lớn mới có thị giác màu
D. Thị giác màu và thị giác đen-trắng phụ thuộc vào kích thước của mắt

**Đáp án: B**
*Giải thích*: Thị giác màu phân bố bất thường: hầu hết động vật có vú (dichromat hoặc monochromat), nhưng chim, cá, bò sát, ong, bướm đều có thị giác màu tốt. Chim thậm chí nhìn được UV. Điều này phản ánh áp lực tiến hóa: loài cần phân biệt thức ăn chín/sống, hoa màu sắc, hay bạn tình thì phát triển thị giác màu.

---

### Câu 4 (Tự luận mở)
**Câu hỏi**: Event camera (Dynamic Vision Sensor) hoạt động theo nguyên lý gần giống hệ thần kinh thị giác sinh học — chỉ phát tín hiệu khi có thay đổi. Là kỹ sư cơ điện tử thiết kế hệ thống tracking đạn hoặc đo rung tần số cao cho vũ khí, hãy phân tích: (1) Tại sao event camera có ưu thế vượt trội so với frame camera truyền thống trong ứng dụng này? (2) Thách thức kỹ thuật nào bạn phải giải quyết khi tích hợp event camera vào hệ thống đo lường chính xác?

**Gợi ý trả lời mẫu**:
1. *Ưu thế của event camera*:
   - **Latency cực thấp** (< 1 μs so với 33 ms của 30fps camera) — thiết yếu để track projectile ở vận tốc vài km/s
   - **Dynamic range rất cao** (~120 dB so với ~60 dB của frame camera) — quan trọng khi có cả vùng sáng (muzzle flash) và tối trong cùng cảnh
   - **Không có motion blur** — mỗi sự kiện được timestamp chính xác đến microsecond
   - **Băng thông thấp** — chỉ truyền dữ liệu thay đổi, không phải toàn bộ frame

2. *Thách thức kỹ thuật*:
   - **Event processing pipeline**: Dữ liệu event không có cấu trúc frame thông thường — cần thuật toán xử lý event bất đồng bộ (event-based optical flow, event-based feature detection)
   - **Noise trong điều kiện ánh sáng ổn định**: Pixel noise tạo ra false events — cần filter adaptive threshold
   - **Synchronization**: Để kết hợp event camera với IMU hoặc cảm biến khác, cần clock đồng bộ precision < 1 μs
   - **Thuật toán reconstruction**: Từ event stream, tái tạo trajectory của đạn đòi hỏi thuật toán Kalman filter hoặc particle filter được tối ưu cho event data

---

```json
{
  "questions": [
    {"id": "q1", "type": "mcq", "question": "Tại sao khi cường độ ánh sáng tăng gấp đôi, tần số spike thần kinh không tăng gấp đôi?", "options": ["A. Vì tế bào thần kinh bị mệt mỏi", "B. Vì hệ thần kinh mã hóa theo thang logarithm (Weber-Fechner law): f ∝ log(I/I₀)", "C. Vì iris thu hẹp làm giảm ánh sáng vào", "D. Vì tế bào nón bị bão hòa"], "answer": "B", "explanation": "Weber-Fechner law: f ∝ log(I/I₀). Tăng I gấp đôi chỉ thêm một lượng cố định log2 vào tần số, không nhân đôi."},
    {"id": "q2", "type": "mcq", "question": "Kích thước tối ưu của facet lens trong mắt kép được quyết định bởi điều kiện nào?", "options": ["A. Phải lớn nhất để thu tối đa ánh sáng", "B. Phải nhỏ nhất để có nhiều ommatidia", "C. Cân bằng giữa giới hạn nhiễu xạ và mật độ lấy mẫu không gian: D_opt = √(2.44λR)", "D. Được quyết định bởi áp lực cơ học vỏ ngoài"], "answer": "C", "explanation": "Điểm tối ưu Nyquist-Rayleigh: facet đủ lớn để giảm nhiễu xạ nhưng đủ nhỏ để mật độ ommatidia đủ cao tránh aliasing. D_opt = √(2.44λR) ≈ 35μm cho ong mật."},
    {"id": "q3", "type": "mcq", "question": "Câu nào mô tả ĐÚNG về thị giác màu trong thế giới động vật?", "options": ["A. Tất cả động vật có xương sống đều nhìn được màu", "B. Hầu hết động vật có vú không nhìn được màu; chim, cá, bò sát và nhiều côn trùng có thị giác màu tốt", "C. Chỉ người và linh trưởng lớn mới có thị giác màu", "D. Thị giác màu phụ thuộc kích thước mắt"], "answer": "B", "explanation": "Thị giác màu phân bố theo áp lực tiến hóa: chim, cá, côn trùng cần phân biệt màu để sinh tồn đều phát triển thị giác màu. Hầu hết động vật có vú thì không."},
    {"id": "q4", "type": "open", "question": "Là kỹ sư cơ điện tử thiết kế hệ thống tracking đạn hoặc đo rung tần số cao, hãy phân tích ưu thế của event camera so với frame camera và các thách thức kỹ thuật khi tích hợp vào hệ thống đo lường chính xác.", "sample_answer": "Ưu thế: latency <1μs, dynamic range 120dB, không motion blur, băng thông thấp. Thách thức: cần event-based processing algorithms (không dùng được CV truyền thống), noise filtering, time synchronization <1μs với sensor khác, và thuật toán trajectory reconstruction từ event stream bất đồng bộ."}
  ]
}
```


## Quiz Questions

**Q1:** Tại sao khi cường độ ánh sáng tăng gấp đôi, tần số spike thần kinh không tăng gấp đôi?
- A) A. Vì tế bào thần kinh bị mệt mỏi
- B) B. Vì hệ thần kinh mã hóa theo thang logarithm (Weber-Fechner law): f ∝ log(I/I₀)
- C) C. Vì iris thu hẹp làm giảm ánh sáng vào
- D) D. Vì tế bào nón bị bão hòa

**Correct:** B

**Explanation:** Weber-Fechner law: f ∝ log(I/I₀). Tăng I gấp đôi chỉ thêm một lượng cố định log2 vào tần số, không nhân đôi.

**Q2:** Kích thước tối ưu của facet lens trong mắt kép được quyết định bởi điều kiện nào?
- A) A. Phải lớn nhất để thu tối đa ánh sáng
- B) B. Phải nhỏ nhất để có nhiều ommatidia
- C) C. Cân bằng giữa giới hạn nhiễu xạ và mật độ lấy mẫu không gian: D_opt = √(2.44λR)
- D) D. Được quyết định bởi áp lực cơ học vỏ ngoài

**Correct:** C

**Explanation:** Điểm tối ưu Nyquist-Rayleigh: facet đủ lớn để giảm nhiễu xạ nhưng đủ nhỏ để mật độ ommatidia đủ cao tránh aliasing. D_opt = √(2.44λR) ≈ 35μm cho ong mật.

**Q3:** Câu nào mô tả ĐÚNG về thị giác màu trong thế giới động vật?
- A) A. Tất cả động vật có xương sống đều nhìn được màu
- B) B. Hầu hết động vật có vú không nhìn được màu; chim, cá, bò sát và nhiều côn trùng có thị giác màu tốt
- C) C. Chỉ người và linh trưởng lớn mới có thị giác màu
- D) D. Thị giác màu phụ thuộc kích thước mắt

**Correct:** B

**Explanation:** Thị giác màu phân bố theo áp lực tiến hóa: chim, cá, côn trùng cần phân biệt màu để sinh tồn đều phát triển thị giác màu. Hầu hết động vật có vú thì không.

**Q4:** Là kỹ sư cơ điện tử thiết kế hệ thống tracking đạn hoặc đo rung tần số cao, hãy phân tích ưu thế của event camera so với frame camera và các thách thức kỹ thuật khi tích hợp vào hệ thống đo lường chính xác.

**Correct:** N/A


---
*Exported from Feynman Bot*
