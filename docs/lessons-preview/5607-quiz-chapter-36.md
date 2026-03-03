---
lesson_id: 5607
lesson_type: quiz
approval_status: pending
exported_at: "2026-03-03T15:33:08.992412+00:00"
content_hash: babbb0f5c491
chapter_number: 36
chapter_title: Chapter 36
section_number: 3
section_title: 36–2The physiology of the eye
---
# ## Quiz: Cấu trúc và Cơ chế Thần kinh của Mắt Người

*Source: Chapter 36 - Chapter 36 (Section 3) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_36.html)*

## Quiz: Cấu trúc và Cơ chế Thần kinh của Mắt Người

Hãy kiểm tra mức độ hiểu biết của bạn về cơ chế quang học và thần kinh của mắt người qua các câu hỏi dưới đây.

---

### Câu 1 (Trắc nghiệm)
Tại sao chúng ta không thể nhìn rõ dưới nước mà không có kính lặn?

A. Vì áp suất nước làm biến dạng nhãn cầu
B. Vì chiết suất giác mạc ($n \approx 1.37$) và nước ($n \approx 1.33$) quá gần nhau, làm mất khả năng hội tụ của giác mạc
C. Vì ánh sáng bị hấp thụ mạnh hơn trong nước
D. Vì thủy tinh thể không điều tiết được trong môi trường nước

**Đáp án: B**
*Giải thích*: Khả năng hội tụ của giác mạc phụ thuộc vào sự chênh lệch chiết suất giữa không khí ($n = 1.0$) và giác mạc ($n \approx 1.37$). Dưới nước, chiết suất nước ($n \approx 1.33$) gần bằng chiết suất giác mạc, nên ánh sáng gần như không bị khúc xạ tại bề mặt giác mạc, mất đi ~2/3 khả năng hội tụ.

---

### Câu 2 (Trắc nghiệm)
Thủy tinh thể (lens) của mắt người có đặc điểm chiết suất như thế nào so với một thấu kính thủy tinh đồng nhất thông thường?

A. Chiết suất đồng nhất $n = 1.40$ trên toàn bộ thể tích
B. Chiết suất biến thiên: $n \approx 1.40$ ở trung tâm và $n \approx 1.38$ ở ngoại vi
C. Chiết suất biến thiên: $n \approx 1.38$ ở trung tâm và $n \approx 1.40$ ở ngoại vi
D. Thủy tinh thể không có vai trò khúc xạ ánh sáng đáng kể

**Đáp án: B**
*Giải thích*: Thủy tinh thể có cấu trúc phân lớp như củ hành, với chiết suất $n \approx 1.40$ ở trung tâm giảm dần xuống $n \approx 1.38$ ở ngoại vi. Cấu trúc gradient chiết suất (GRIN - Gradient-Index) này giúp giảm quang sai cầu (spherical aberration), tương tự nguyên lý của thấu kính GRIN trong hệ thống quang học chính xác cao.

---

### Câu 3 (Trắc nghiệm)
Trong cơ chế điều tiết iris (đồng tử), điều nào sau đây là đúng về vòng cơ tròn (circular muscle) L?

A. Khi kích hoạt, cơ L giãn ra làm đồng tử mở rộng
B. Khi kích hoạt, cơ L co lại làm đồng tử thu hẹp, với phản ứng rất nhanh qua kết nối thần kinh trực tiếp
C. Cơ L được điều khiển gián tiếp qua vỏ não thị giác
D. Cơ L chỉ hoạt động trong điều kiện ánh sáng yếu

**Đáp án: B**
*Giải thích*: Cơ tròn L khi bị kích thích sẽ co lại (như bất kỳ cơ nào), kéo iris thu hẹp đồng tử nhanh chóng. Đây là phản xạ pupillary — các sợi thần kinh đo lường ánh sáng trung bình chạy qua mid-brain rồi phản hồi trực tiếp đến iris, không qua vỏ não thị giác, nên phản ứng rất nhanh.

---

### Câu 4 (Tự luận mở)
**Câu hỏi**: Là một kỹ sư cơ điện tử thiết kế hệ thống đo lường chính xác ở mức micrometer, bạn nhận thấy cơ chế auto-focus và điều chỉnh aperture của mắt người có nhiều điểm tương đồng với hệ thống camera công nghiệp. Hãy phân tích: (1) Cơ chế lens accommodation (điều tiết thủy tinh thể) tương đương với bộ phận nào trong hệ thống quang học chính xác của bạn? (2) Cơ chế gradient chiết suất (GRIN lens) của thủy tinh thể có thể ứng dụng thế nào trong thiết kế đầu đo quang học micro-precision?

**Gợi ý trả lời mẫu**:
1. *Lens accommodation* tương đương với **motorized focus actuator** trong hệ thống quang học chính xác: cơ thể mi (ciliary muscles) hoạt động như một piezo actuator thay đổi tiêu cự liên tục. Trong hệ thống đo lường micrometer, chúng ta dùng piezoelectric lens actuator hoặc voice coil motor để dịch chuyển thấu kính với độ phân giải nanometer. Mắt người "encode" khoảng cách vật thể thông qua mức độ co cơ thể mi, tương tự encoder phản hồi vị trí trong closed-loop servo.

2. *Thủy tinh thể GRIN*: Trong quang học chính xác, thấu kính GRIN được sử dụng trong đầu đo laser confocal và hệ thống collimation sợi quang. Chiết suất biến thiên liên tục giúp hội tụ ánh sáng mà không cần bề mặt cong lớn, giảm đáng kể spherical và chromatic aberration — đây là yêu cầu quan trọng khi đo lường ở độ phân giải sub-micrometer. Nghiên cứu biomimetic GRIN lens đang mở ra hướng chế tạo đầu đo quang học siêu nhỏ cho robot phẫu thuật và hệ thống kiểm tra chip bán dẫn.

---

```json
{
  "questions": [
    {"id": "q1", "type": "mcq", "question": "Tại sao chúng ta không thể nhìn rõ dưới nước mà không có kính lặn?", "options": ["A. Vì áp suất nước làm biến dạng nhãn cầu", "B. Vì chiết suất giác mạc và nước quá gần nhau, làm mất khả năng hội tụ của giác mạc", "C. Vì ánh sáng bị hấp thụ mạnh hơn trong nước", "D. Vì thủy tinh thể không điều tiết được trong môi trường nước"], "answer": "B", "explanation": "Khả năng hội tụ của giác mạc phụ thuộc vào sự chênh lệch chiết suất. Dưới nước, n_nước ≈ 1.33 gần bằng n_giác_mạc ≈ 1.37, nên mất phần lớn khả năng khúc xạ."},
    {"id": "q2", "type": "mcq", "question": "Thủy tinh thể (lens) của mắt người có đặc điểm chiết suất như thế nào?", "options": ["A. Chiết suất đồng nhất n=1.40 trên toàn bộ", "B. n≈1.40 ở trung tâm, giảm xuống n≈1.38 ở ngoại vi (cấu trúc GRIN)", "C. n≈1.38 ở trung tâm, tăng lên n≈1.40 ở ngoại vi", "D. Thủy tinh thể không có vai trò khúc xạ đáng kể"], "answer": "B", "explanation": "Thủy tinh thể có cấu trúc gradient chiết suất (GRIN), với n≈1.40 ở trung tâm giảm dần xuống n≈1.38 ở ngoại vi, giúp giảm quang sai cầu."},
    {"id": "q3", "type": "mcq", "question": "Về cơ chế điều tiết iris, điều nào đúng về vòng cơ tròn L?", "options": ["A. Khi kích hoạt, cơ L giãn ra làm đồng tử mở rộng", "B. Khi kích hoạt, cơ L co lại làm đồng tử thu hẹp, phản ứng rất nhanh qua kết nối thần kinh trực tiếp", "C. Cơ L được điều khiển gián tiếp qua vỏ não thị giác", "D. Cơ L chỉ hoạt động trong điều kiện ánh sáng yếu"], "answer": "B", "explanation": "Cơ tròn L co lại khi kích thích, thu hẹp đồng tử. Phản xạ này đi qua mid-brain chứ không qua vỏ não thị giác, nên rất nhanh."},
    {"id": "q4", "type": "open", "question": "Là kỹ sư cơ điện tử thiết kế hệ thống đo lường micrometer, hãy phân tích: (1) Cơ chế lens accommodation tương đương với bộ phận nào trong hệ thống quang học chính xác? (2) Cấu trúc GRIN lens của thủy tinh thể có thể ứng dụng thế nào trong thiết kế đầu đo quang học micro-precision?", "sample_answer": "1. Lens accommodation tương đương motorized focus actuator (piezoelectric hoặc voice coil), điều chỉnh tiêu cự với phản hồi closed-loop. 2. GRIN lens được ứng dụng trong đầu đo laser confocal và collimation sợi quang, giảm aberration cho đo lường sub-micrometer."}
  ]
}
```


## Quiz Questions

**Q1:** Tại sao chúng ta không thể nhìn rõ dưới nước mà không có kính lặn?
- A) A. Vì áp suất nước làm biến dạng nhãn cầu
- B) B. Vì chiết suất giác mạc và nước quá gần nhau, làm mất khả năng hội tụ của giác mạc
- C) C. Vì ánh sáng bị hấp thụ mạnh hơn trong nước
- D) D. Vì thủy tinh thể không điều tiết được trong môi trường nước

**Correct:** B

**Explanation:** Khả năng hội tụ của giác mạc phụ thuộc vào sự chênh lệch chiết suất. Dưới nước, n_nước ≈ 1.33 gần bằng n_giác_mạc ≈ 1.37, nên mất phần lớn khả năng khúc xạ.

**Q2:** Thủy tinh thể (lens) của mắt người có đặc điểm chiết suất như thế nào?
- A) A. Chiết suất đồng nhất n=1.40 trên toàn bộ
- B) B. n≈1.40 ở trung tâm, giảm xuống n≈1.38 ở ngoại vi (cấu trúc GRIN)
- C) C. n≈1.38 ở trung tâm, tăng lên n≈1.40 ở ngoại vi
- D) D. Thủy tinh thể không có vai trò khúc xạ đáng kể

**Correct:** B

**Explanation:** Thủy tinh thể có cấu trúc gradient chiết suất (GRIN), với n≈1.40 ở trung tâm giảm dần xuống n≈1.38 ở ngoại vi, giúp giảm quang sai cầu.

**Q3:** Về cơ chế điều tiết iris, điều nào đúng về vòng cơ tròn L?
- A) A. Khi kích hoạt, cơ L giãn ra làm đồng tử mở rộng
- B) B. Khi kích hoạt, cơ L co lại làm đồng tử thu hẹp, phản ứng rất nhanh qua kết nối thần kinh trực tiếp
- C) C. Cơ L được điều khiển gián tiếp qua vỏ não thị giác
- D) D. Cơ L chỉ hoạt động trong điều kiện ánh sáng yếu

**Correct:** B

**Explanation:** Cơ tròn L co lại khi kích thích, thu hẹp đồng tử. Phản xạ này đi qua mid-brain chứ không qua vỏ não thị giác, nên rất nhanh.

**Q4:** Là kỹ sư cơ điện tử thiết kế hệ thống đo lường micrometer, hãy phân tích: (1) Cơ chế lens accommodation tương đương với bộ phận nào trong hệ thống quang học chính xác? (2) Cấu trúc GRIN lens của thủy tinh thể có thể ứng dụng thế nào trong thiết kế đầu đo quang học micro-precision?

**Correct:** N/A


---
*Exported from Feynman Bot*
