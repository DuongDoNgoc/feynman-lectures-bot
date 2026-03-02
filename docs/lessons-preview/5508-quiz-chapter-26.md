---
lesson_id: 5508
lesson_type: quiz
approval_status: pending
exported_at: "2026-03-02T15:10:31.340749+00:00"
content_hash: 6a936be03433
chapter_number: 26
chapter_title: Chapter 26
section_number: 4
section_title: 26–3Fermat’s principle of least time
---
# ## Kiểm Tra: Nguyên Lý Thời Gian Cực Tiểu của Fermat

*Source: Chapter 26 - Chapter 26 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_26.html)*

## Kiểm Tra: Nguyên Lý Thời Gian Cực Tiểu của Fermat

### Câu 1 (Trắc nghiệm)

Nguyên lý Fermat (Principle of Least Time) phát biểu rằng:

A. Ánh sáng luôn đi theo đường thẳng giữa hai điểm
B. Trong tất cả các đường đi có thể, ánh sáng chọn đường tốn ít thời gian nhất
C. Ánh sáng đi theo đường có tổng góc tới nhỏ nhất
D. Tốc độ ánh sáng luôn không đổi trong mọi môi trường

**Đáp án: B**

*Giải thích:* Fermat (1650) phát biểu rằng ánh sáng, trong tất cả các đường đi có thể từ điểm này đến điểm khác, sẽ chọn đường đi tốn ít thời gian nhất. Điều này dẫn đến cả định luật phản xạ lẫn định luật khúc xạ Snell.

---

### Câu 2 (Trắc nghiệm)

Để chứng minh định luật phản xạ từ nguyên lý Fermat, người ta dùng mẹo hình học nào?

A. Vẽ tiếp tuyến với mặt gương tại điểm tới
B. Dựng điểm ảnh $B'$ đối xứng với $B$ qua mặt gương, tìm đường thẳng $AB'$ cắt gương
C. Tính đạo hàm tổng khoảng cách theo vị trí điểm tới
D. Dùng định lý Pythagorean cho tam giác tạo bởi tia tới và tia phản xạ

**Đáp án: B**

*Giải thích:* Bằng cách dựng điểm ảo $B'$ đối xứng với $B$ qua gương, ta có $CB = CB'$ với mọi điểm $C$ trên gương. Tổng $AC + CB = AC + CB'$ đạt nhỏ nhất khi $A$, $C$, $B'$ thẳng hàng, điều này tự động đảm bảo góc tới bằng góc phản xạ.

---

### Câu 3 (Trắc nghiệm)

Trong một hệ thống laser interferometer đo vị trí cấp micromet, gương phản xạ bị nghiêng một góc $\Delta\theta = 2\,\mu\text{rad}$ so với vị trí lý tưởng. Nếu khoảng cách từ gương đến detector là $L = 0.5\,\text{m}$, sai số vị trí detector gây ra xấp xỉ là:

A. $0.5\,\mu\text{m}$
B. $1\,\mu\text{m}$
C. $2\,\mu\text{m}$
D. $4\,\mu\text{m}$

**Đáp án: B**

*Giải thích:* Sai số vị trí $\delta = L \cdot \Delta\theta = 0.5\,\text{m} \times 2\times10^{-6}\,\text{rad} = 1\times10^{-6}\,\text{m} = 1\,\mu\text{m}$. Đây minh họa tầm quan trọng của kiểm soát góc gương trong hệ đo chính xác.

---

### Câu 4 (Tự luận mở)

**Câu hỏi:** Trong công việc thiết kế hệ thống tự động hóa hoặc vũ khí có độ chính xác cao, bạn thường phải tối ưu hóa quỹ đạo của cảm biến hoặc cơ cấu chấp hành. Hãy liên hệ nguyên lý Fermat (ánh sáng chọn đường tốn ít thời gian nhất) với bài toán tối ưu hóa quỹ đạo trong kỹ thuật cơ điện tử. Điểm tương đồng triết học giữa hai bài toán này là gì? Liệu "nguyên lý tác dụng cực tiểu" (principle of least action) trong cơ học Hamilton có thể áp dụng vào bài toán điều khiển tối ưu (optimal control) của bạn không?

*Gợi ý trả lời:* Học sinh cần thảo luận về: (1) Fermat's principle là tiền thân của Hamilton's principle of least action; (2) Trong optimal control, hệ thống servo tối thiểu hóa một hàm chi phí (cost function) tương tự như ánh sáng tối thiểu hóa thời gian; (3) Phương trình Euler-Lagrange xuất hiện ở cả hai bài toán; (4) Ứng dụng cụ thể trong trajectory planning cho robot hoặc điều khiển đầu đọc của thiết bị đo lường chính xác.

```json
{
  "quiz_id": "q5508",
  "topic": "Fermat's Principle of Least Time",
  "questions": [
    {"id": 1, "type": "mcq", "answer": "B"},
    {"id": 2, "type": "mcq", "answer": "B"},
    {"id": 3, "type": "mcq", "answer": "B"},
    {"id": 4, "type": "open", "topic": "Fermat principle vs optimal control"}
  ]
}
```


## Quiz Questions

**Q1:** No question text

**Correct:** B

**Q2:** No question text

**Correct:** B

**Q3:** No question text

**Correct:** B

**Q4:** No question text

**Correct:** N/A


---
*Exported from Feynman Bot*
