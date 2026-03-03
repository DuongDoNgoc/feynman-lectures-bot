---
lesson_id: 5610
lesson_type: quiz
approval_status: pending
exported_at: "2026-03-03T15:33:09.037929+00:00"
content_hash: f0f6624c4fed
chapter_number: 36
chapter_title: Chapter 36
section_number: 4
section_title: 36–3The rod cells
---
# ## Quiz: Tế Bào Que, Rhodopsin và Mắt Kép

*Source: Chapter 36 - Chapter 36 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_36.html)*

## Quiz: Tế Bào Que, Rhodopsin và Mắt Kép

Kiểm tra hiểu biết về cơ chế thị giác cấp phân tử và so sánh các loại mắt trong tự nhiên.

---

### Câu 1 (Trắc nghiệm)
Tại sao chuỗi "conjugated double bonds" (liên kết đôi liên hợp) trong retinene lại hấp thụ ánh sáng rất mạnh?

A. Vì số lượng nguyên tử carbon trong phân tử rất lớn
B. Vì các electron $\pi$ có thể dịch chuyển đồng thời dọc toàn bộ chuỗi liên kết, tạo hiệu ứng tương đương một electron di chuyển qua toàn bộ chiều dài phân tử
C. Vì liên kết đôi có năng lượng cao hơn liên kết đơn
D. Vì retinene có màu tím, phản xạ ánh sáng đỏ

**Đáp án: B**
*Giải thích*: Trong chuỗi liên kết đôi liên hợp, khi photon kích thích một electron dịch chuyển, hiệu ứng lan truyền như domino qua toàn bộ chuỗi. Kết quả thực tế tương đương một electron đơn di chuyển qua toàn bộ chiều dài phân tử — phạm vi di chuyển lớn hơn nhiều so với một liên kết đơn lẻ — dẫn đến tiết diện hấp thụ (absorption cross-section) rất lớn.

---

### Câu 2 (Trắc nghiệm)
Thiếu vitamin $A$ gây ra hậu quả gì đối với thị giác và tại sao?

A. Gây mù màu vì cone cells bị ảnh hưởng trước
B. Gây quáng gà (night blindness) vì vitamin $A$ là tiền chất của retinene — thành phần cốt lõi của rhodopsin trong tế bào que
C. Gây mờ mắt ban ngày vì thủy tinh thể bị đục
D. Gây mất độ phân giải vì tế bào que không có đủ năng lượng

**Đáp án: B**
*Giải thích*: Vitamin $A$ (retinol) là dạng ăn uống được của retinene (thêm một H ở đầu chuỗi). Không có vitamin $A$ → không tổng hợp đủ retinene → rhodopsin thiếu sắc tố nhận photon → tế bào que không hoạt động → mất thị giác trong điều kiện ánh sáng yếu (quáng gà). Tế bào nón (cone cells) cần nhiều ánh sáng hơn nên ít bị ảnh hưởng.

---

### Câu 3 (Trắc nghiệm)
So sánh cấu trúc mắt bạch tuộc với mắt người, điểm nào là **cải tiến về thiết kế** trong mắt bạch tuộc?

A. Mắt bạch tuộc có nhiều tế bào nón hơn, cho phép nhìn màu tốt hơn
B. Mắt bạch tuộc có kích thước lớn hơn, cho phép thu nhận nhiều ánh sáng hơn
C. Tế bào cảm quang ở phía trước (không "inside-out"), tránh được điểm mù do dây thần kinh thị giác xuyên võng mạc
D. Mắt bạch tuộc dùng cơ chế lateral inhibition hiệu quả hơn

**Đáp án: C**
*Giải thích*: Mắt người có cấu trúc "lộn ngược" — tế bào cảm quang ở sau, tế bào thần kinh ở trước, và dây thần kinh thị giác phải xuyên qua võng mạc tạo ra điểm mù (blind spot). Mắt bạch tuộc không bị điều này: tế bào cảm quang ở trước, tế bào thần kinh ở sau — một thiết kế logic hơn đã được tiến hóa tìm ra độc lập.

---

### Câu 4 (Tự luận mở)
**Câu hỏi**: Cơ chế "lateral inhibition" (ức chế bên) trong mắt kép của cua móng ngựa thực hiện edge detection sinh học. Là kỹ sư cơ điện tử thiết kế hệ thống AOI (Automated Optical Inspection) kiểm tra bề mặt wafer bán dẫn ở độ phân giải micrometer, hãy giải thích: (1) Tại sao lateral inhibition lại hiệu quả hơn việc đơn giản chỉ đo cường độ ánh sáng thô tại mỗi điểm? (2) Thuật toán xử lý ảnh nào tương đương lateral inhibition và bạn sẽ áp dụng nó như thế nào trong hệ thống kiểm tra chip của mình?

**Gợi ý trả lời mẫu**:
1. *Lateral inhibition* hiệu quả hơn đo cường độ thô vì nó **loại bỏ thành phần DC** (ánh sáng nền đồng đều) và **khuếch đại gradient** (biên cạnh, khuyết tật). Trong kiểm tra wafer, bề mặt chip có thể có chiếu sáng không đều; lateral inhibition tự động chuẩn hóa nền và làm nổi bật các điểm dị thường. Tương tự trong kỹ thuật điện, đây là bộ lọc high-pass không gian.

2. *Thuật toán tương đương*: **Difference of Gaussians (DoG)** hoặc **Laplacian of Gaussian (LoG)** — hai bộ lọc này mô phỏng chính xác lateral inhibition. Trong hệ thống AOI wafer: (a) chụp ảnh bề mặt với độ phân giải 0.5μm/pixel; (b) áp DoG với $\sigma_1 = 2$ pixel và $\sigma_2 = 5$ pixel để phát hiện khuyết tật kích thước 1-10μm; (c) so sánh với die reference (die-to-die comparison) để phân loại true defect vs. nuisance. Kết hợp với threshold thích nghi (adaptive thresholding), hệ thống đạt sensitivity >99% với false positive rate <0.1%.

---

```json
{
  "questions": [
    {"id": "q1", "type": "mcq", "question": "Tại sao chuỗi conjugated double bonds trong retinene hấp thụ ánh sáng rất mạnh?", "options": ["A. Vì số lượng nguyên tử carbon trong phân tử rất lớn", "B. Vì các electron π dịch chuyển đồng thời dọc toàn bộ chuỗi, tương đương một electron di chuyển qua toàn bộ phân tử", "C. Vì liên kết đôi có năng lượng cao hơn liên kết đơn", "D. Vì retinene có màu tím, phản xạ ánh sáng đỏ"], "answer": "B", "explanation": "Hiệu ứng domino electron qua chuỗi conjugated double bonds tạo ra phạm vi di chuyển hiệu quả rất lớn, dẫn đến tiết diện hấp thụ cao."},
    {"id": "q2", "type": "mcq", "question": "Thiếu vitamin A gây ra hậu quả gì đối với thị giác?", "options": ["A. Gây mù màu vì cone cells bị ảnh hưởng", "B. Gây quáng gà vì vitamin A là tiền chất của retinene trong rhodopsin tế bào que", "C. Gây mờ mắt ban ngày vì thủy tinh thể bị đục", "D. Gây mất độ phân giải vì tế bào que thiếu năng lượng"], "answer": "B", "explanation": "Vitamin A (retinol) → retinene → rhodopsin. Thiếu vitamin A → thiếu rhodopsin → tế bào que không hoạt động → quáng gà."},
    {"id": "q3", "type": "mcq", "question": "Điểm cải tiến thiết kế trong mắt bạch tuộc so với mắt người là gì?", "options": ["A. Nhiều tế bào nón hơn cho màu sắc tốt hơn", "B. Kích thước lớn hơn thu nhiều ánh sáng hơn", "C. Tế bào cảm quang ở phía trước, tránh được điểm mù do dây thần kinh xuyên võng mạc", "D. Dùng lateral inhibition hiệu quả hơn"], "answer": "C", "explanation": "Mắt bạch tuộc không 'inside-out' như mắt người, không có điểm mù — đây là thiết kế tốt hơn được tiến hóa hội tụ tìm ra độc lập."},
    {"id": "q4", "type": "open", "question": "Là kỹ sư thiết kế hệ thống AOI kiểm tra wafer bán dẫn ở độ phân giải micrometer, hãy giải thích: (1) Tại sao lateral inhibition hiệu quả hơn đo cường độ thô? (2) Thuật toán nào tương đương và bạn áp dụng thế nào trong kiểm tra chip?", "sample_answer": "1. Lateral inhibition loại bỏ thành phần DC (nền đồng đều) và khuếch đại gradient (biên, khuyết tật), tự động chuẩn hóa bất đồng đều chiếu sáng. 2. Thuật toán DoG/LoG mô phỏng lateral inhibition; trong AOI dùng DoG với σ phù hợp kích thước khuyết tật, kết hợp die-to-die comparison và adaptive thresholding."}
  ]
}
```


## Quiz Questions

**Q1:** Tại sao chuỗi conjugated double bonds trong retinene hấp thụ ánh sáng rất mạnh?
- A) A. Vì số lượng nguyên tử carbon trong phân tử rất lớn
- B) B. Vì các electron π dịch chuyển đồng thời dọc toàn bộ chuỗi, tương đương một electron di chuyển qua toàn bộ phân tử
- C) C. Vì liên kết đôi có năng lượng cao hơn liên kết đơn
- D) D. Vì retinene có màu tím, phản xạ ánh sáng đỏ

**Correct:** B

**Explanation:** Hiệu ứng domino electron qua chuỗi conjugated double bonds tạo ra phạm vi di chuyển hiệu quả rất lớn, dẫn đến tiết diện hấp thụ cao.

**Q2:** Thiếu vitamin A gây ra hậu quả gì đối với thị giác?
- A) A. Gây mù màu vì cone cells bị ảnh hưởng
- B) B. Gây quáng gà vì vitamin A là tiền chất của retinene trong rhodopsin tế bào que
- C) C. Gây mờ mắt ban ngày vì thủy tinh thể bị đục
- D) D. Gây mất độ phân giải vì tế bào que thiếu năng lượng

**Correct:** B

**Explanation:** Vitamin A (retinol) → retinene → rhodopsin. Thiếu vitamin A → thiếu rhodopsin → tế bào que không hoạt động → quáng gà.

**Q3:** Điểm cải tiến thiết kế trong mắt bạch tuộc so với mắt người là gì?
- A) A. Nhiều tế bào nón hơn cho màu sắc tốt hơn
- B) B. Kích thước lớn hơn thu nhiều ánh sáng hơn
- C) C. Tế bào cảm quang ở phía trước, tránh được điểm mù do dây thần kinh xuyên võng mạc
- D) D. Dùng lateral inhibition hiệu quả hơn

**Correct:** C

**Explanation:** Mắt bạch tuộc không 'inside-out' như mắt người, không có điểm mù — đây là thiết kế tốt hơn được tiến hóa hội tụ tìm ra độc lập.

**Q4:** Là kỹ sư thiết kế hệ thống AOI kiểm tra wafer bán dẫn ở độ phân giải micrometer, hãy giải thích: (1) Tại sao lateral inhibition hiệu quả hơn đo cường độ thô? (2) Thuật toán nào tương đương và bạn áp dụng thế nào trong kiểm tra chip?

**Correct:** N/A


---
*Exported from Feynman Bot*
