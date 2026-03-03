---
lesson_id: 5430
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:04.879718+00:00"
content_hash: 2962ef42f21a
chapter_number: 15
chapter_title: Chapter 15
section_number: 6
section_title: 15–5The Lorentz contraction
---
# ## Quiz: Phép Biến Đổi Lorentz và Sự Đồng Thời Tương Đối

*Source: Chapter 15 - Chapter 15 (Section 6) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_15.html)*

## Quiz: Phép Biến Đổi Lorentz và Sự Đồng Thời Tương Đối

### Câu 1 (Trắc nghiệm)
Moe chuyển động trong hệ $S'$ dọc theo trục $x$ với vận tốc $u$ và dùng thước đo khoảng cách $x'$. Theo Joe trong hệ $S$ đứng yên, "thước thực" mà Moe đang dùng có độ dài là bao nhiêu?

**A.** $x'$ (không thay đổi vì thước vuông góc với chuyển động)
**B.** $x'\sqrt{1-u^2/c^2}$ (bị co lại theo hướng chuyển động)
**C.** $x'/\sqrt{1-u^2/c^2}$ (bị dài ra theo hướng chuyển động)
**D.** $x' + ut$ (tịnh tiến theo thời gian)

**Đáp án: B**
*Giải thích:* Co Lorentz (Lorentz contraction) làm thước của Moe bị co lại theo hệ số $\sqrt{1-u^2/c^2}$ theo hướng chuyển động. Đây chính là cơ sở để suy ra phương trình $x' = (x-ut)/\sqrt{1-u^2/c^2}$ của phép biến đổi Lorentz.

---

### Câu 2 (Trắc nghiệm)
Trong phép biến đổi Lorentz, phương trình biến đổi thời gian $t' = (t - ux/c^2)/\sqrt{1-u^2/c^2}$ chứa số hạng $ux/c^2$ trong tử số. Số hạng này có ý nghĩa vật lý gì?

**A.** Đây là hiệu chỉnh vi nhiễu Doppler do chuyển động của nguồn sáng.
**B.** Đây là nguyên nhân gây ra sự thất bại đồng thời (failure of simultaneity) — hai sự kiện cùng lúc trong $S'$ có thể không cùng lúc trong $S$.
**C.** Đây là hệ số giãn thời gian (time dilation) thuần túy do vận tốc chuyển động.
**D.** Đây là hiệu chỉnh do trường hấp dẫn (thuyết tương đối rộng).

**Đáp án: B**
*Giải thích:* Số hạng $ux/c^2$ phụ thuộc vào vị trí không gian $x$. Điều này có nghĩa là hai sự kiện xảy ra cùng lúc ($\Delta t = 0$) nhưng ở hai vị trí khác nhau ($\Delta x 
eq 0$) sẽ có $\Delta t' = -u\Delta x/c^2\gamma 
eq 0$. Đây chính là "failure of simultaneity at a distance".

---

### Câu 3 (Trắc nghiệm)
Moe trên tàu vũ trụ đồng bộ hai đồng hồ ở hai đầu tàu bằng cách gửi xung ánh sáng từ điểm giữa. Theo Joe đứng trên mặt đất, kết quả là:

**A.** Hai đồng hồ vẫn đồng bộ vì ánh sáng đi cùng vận tốc $c$ theo cả hai hướng.
**B.** Đồng hồ phía trước nhận tín hiệu trước vì tàu tiến về phía trước.
**C.** Đồng hồ phía sau nhận tín hiệu trước vì tàu đang lao vào phía có tín hiệu đến; đồng hồ phía trước đang "chạy trốn" — hai đồng hồ KHÔNG đồng bộ theo Joe.
**D.** Không thể kết luận vì chưa biết vận tốc tàu.

**Đáp án: C**
*Giải thích:* Joe thấy: đồng hồ phía trước chạy trốn khỏi tín hiệu nên ánh sáng phải đi xa hơn nửa tàu để bắt kịp; đồng hồ phía sau tiến về phía tín hiệu nên ánh sáng đến sớm hơn. Tín hiệu đến đồng hồ sau trước. Moe nghĩ đồng bộ, Joe nghĩ không đồng bộ — cả hai đều đúng trong hệ quy chiếu riêng.

---

### Câu 4 (Tự luận mở)
**Câu hỏi:** Trong thiết kế hệ thống đo lường phân tán cho máy CNC hoặc hệ thống vũ khí dẫn đường, bạn có nhiều cảm biến encoder đặt cách nhau hàng mét. Hiện tượng "failure of simultaneity" (sự thất bại đồng thời) trong thuyết tương đối có liên quan gì đến vấn đề đồng bộ hoá thời gian giữa các sensor trong hệ thống thực tế của bạn không? Hãy phân tích và đề xuất giải pháp kỹ thuật.

**Gợi ý trả lời mẫu:**
Mặc dù tốc độ vận hành máy móc công nghiệp quá nhỏ để thuyết tương đối hẹp gây ra hiệu ứng đáng kể, nguyên lý cơ bản là tương đồng: tín hiệu điện truyền qua cáp với tốc độ hữu hạn (~2/3 vận tốc ánh sáng) tạo ra độ trễ lan truyền giữa các sensor. Với cảm biến cách nhau 1 m, độ trễ tín hiệu ~5 ns. Nếu trục di chuyển 1 m/s, trong 5 ns trục đi được 5 nm — đáng kể ở mức micrometer. Giải pháp: (1) Dùng IEEE 1588 PTP đồng bộ đồng hồ tất cả node đến độ chính xác sub-microsecond. (2) Dùng hardware timestamp — ghi timestamp tại điểm nhận tín hiệu chứ không phải điểm xử lý. (3) Với EtherCAT: distributed clock cho phép đồng bộ đến <1 µs. Đây là ứng dụng thực tế của "sự thất bại đồng thời" — thứ gì đó xảy ra "đồng thời" theo đồng hồ trung tâm thực ra có thể không đồng thời theo thực tế vật lý tại điểm đo.

```json
{
  "questions": [
    {
      "id": "q1",
      "type": "mcq",
      "question": "Moe chuyển động trong hệ S' với vận tốc u và dùng thước đo khoảng cách x'. Theo Joe trong hệ S đứng yên, thước của Moe có độ dài thực là bao nhiêu (theo hướng chuyển động)?",
      "options": [
        "A. x' (không thay đổi vì thước vuông góc với chuyển động)",
        "B. x'√(1-u²/c²) (bị co lại theo hướng chuyển động — co Lorentz)",
        "C. x'/√(1-u²/c²) (bị dài ra theo hướng chuyển động)",
        "D. x' + ut (tịnh tiến theo thời gian thuần túy)"
      ],
      "answer": "B",
      "explanation": "Co Lorentz: thước trong hệ chuyển động bị co theo hệ số √(1-u²/c²) theo hướng chuyển động. Đây là cơ sở suy ra phương trình x' = (x-ut)/√(1-u²/c²)."
    },
    {
      "id": "q2",
      "type": "mcq",
      "question": "Trong phép biến đổi Lorentz, số hạng ux/c² trong phương trình biến đổi thời gian t' = (t - ux/c²)/√(1-u²/c²) có ý nghĩa vật lý là:",
      "options": [
        "A. Hiệu chỉnh vi nhiễu Doppler do chuyển động nguồn sáng.",
        "B. Nguyên nhân gây ra failure of simultaneity — hai sự kiện đồng thời trong S' có thể không đồng thời trong S.",
        "C. Hệ số giãn thời gian thuần túy do vận tốc chuyển động.",
        "D. Hiệu chỉnh trường hấp dẫn từ thuyết tương đối rộng."
      ],
      "answer": "B",
      "explanation": "Số hạng ux/c² phụ thuộc vị trí x: hai sự kiện cùng lúc (Δt=0) nhưng khác vị trí (Δx≠0) sẽ có Δt' = -uΔx/(c²γ) ≠ 0. Đây là failure of simultaneity at a distance."
    },
    {
      "id": "q3",
      "type": "mcq",
      "question": "Moe trên tàu vũ trụ đồng bộ hai đồng hồ ở hai đầu bằng xung ánh sáng từ điểm giữa. Theo Joe trên mặt đất, kết quả của quá trình đồng bộ này là:",
      "options": [
        "A. Hai đồng hồ vẫn đồng bộ vì ánh sáng luôn đi với vận tốc c theo cả hai hướng.",
        "B. Đồng hồ phía trước nhận tín hiệu trước vì tàu tiến về phía trước.",
        "C. Đồng hồ phía sau nhận tín hiệu trước (tàu lao vào tín hiệu); đồng hồ phía trước chạy trốn — hai đồng hồ KHÔNG đồng bộ theo Joe.",
        "D. Không thể kết luận nếu không biết vận tốc tàu."
      ],
      "answer": "C",
      "explanation": "Joe thấy: đồng hồ phía trước chạy trốn khỏi tín hiệu (ánh sáng đi xa hơn nửa tàu), đồng hồ phía sau tiến vào tín hiệu (ánh sáng đi ngắn hơn). Tín hiệu đến đồng hồ đuôi trước. Moe thấy đồng bộ, Joe thấy không — cả hai đều đúng."
    },
    {
      "id": "q4",
      "type": "open",
      "question": "Trong thiết kế hệ đo lường phân tán (nhiều encoder cách nhau hàng mét trên máy CNC hoặc hệ thống dẫn đường vũ khí), nguyên lý 'failure of simultaneity' liên quan thế nào đến vấn đề đồng bộ sensor thực tế? Đề xuất giải pháp kỹ thuật.",
      "sample_answer": "Dù hiệu ứng tương đối hẹp không đáng kể ở tốc độ công nghiệp, nguyên lý tương đồng: tín hiệu điện truyền với tốc độ hữu hạn (~2/3c) tạo độ trễ lan truyền. Sensor cách nhau 1m có độ trễ ~5ns; với trục chuyển động 1m/s, sai số vị trí là 5nm. Giải pháp: IEEE 1588 PTP đồng bộ đồng hồ đến sub-µs; hardware timestamp tại điểm nhận; EtherCAT distributed clock (<1µs). Bài học: 'đồng thời' theo đồng hồ trung tâm không đảm bảo đồng thời thực tế tại điểm đo."
    }
  ]
}
```


## Quiz Questions

**Q1:** Moe chuyển động trong hệ S' với vận tốc u và dùng thước đo khoảng cách x'. Theo Joe trong hệ S đứng yên, thước của Moe có độ dài thực là bao nhiêu (theo hướng chuyển động)?
- A) A. x' (không thay đổi vì thước vuông góc với chuyển động)
- B) B. x'√(1-u²/c²) (bị co lại theo hướng chuyển động — co Lorentz)
- C) C. x'/√(1-u²/c²) (bị dài ra theo hướng chuyển động)
- D) D. x' + ut (tịnh tiến theo thời gian thuần túy)

**Correct:** B

**Explanation:** Co Lorentz: thước trong hệ chuyển động bị co theo hệ số √(1-u²/c²) theo hướng chuyển động. Đây là cơ sở suy ra phương trình x' = (x-ut)/√(1-u²/c²).

**Q2:** Trong phép biến đổi Lorentz, số hạng ux/c² trong phương trình biến đổi thời gian t' = (t - ux/c²)/√(1-u²/c²) có ý nghĩa vật lý là:
- A) A. Hiệu chỉnh vi nhiễu Doppler do chuyển động nguồn sáng.
- B) B. Nguyên nhân gây ra failure of simultaneity — hai sự kiện đồng thời trong S' có thể không đồng thời trong S.
- C) C. Hệ số giãn thời gian thuần túy do vận tốc chuyển động.
- D) D. Hiệu chỉnh trường hấp dẫn từ thuyết tương đối rộng.

**Correct:** B

**Explanation:** Số hạng ux/c² phụ thuộc vị trí x: hai sự kiện cùng lúc (Δt=0) nhưng khác vị trí (Δx≠0) sẽ có Δt' = -uΔx/(c²γ) ≠ 0. Đây là failure of simultaneity at a distance.

**Q3:** Moe trên tàu vũ trụ đồng bộ hai đồng hồ ở hai đầu bằng xung ánh sáng từ điểm giữa. Theo Joe trên mặt đất, kết quả của quá trình đồng bộ này là:
- A) A. Hai đồng hồ vẫn đồng bộ vì ánh sáng luôn đi với vận tốc c theo cả hai hướng.
- B) B. Đồng hồ phía trước nhận tín hiệu trước vì tàu tiến về phía trước.
- C) C. Đồng hồ phía sau nhận tín hiệu trước (tàu lao vào tín hiệu); đồng hồ phía trước chạy trốn — hai đồng hồ KHÔNG đồng bộ theo Joe.
- D) D. Không thể kết luận nếu không biết vận tốc tàu.

**Correct:** C

**Explanation:** Joe thấy: đồng hồ phía trước chạy trốn khỏi tín hiệu (ánh sáng đi xa hơn nửa tàu), đồng hồ phía sau tiến vào tín hiệu (ánh sáng đi ngắn hơn). Tín hiệu đến đồng hồ đuôi trước. Moe thấy đồng bộ, Joe thấy không — cả hai đều đúng.

**Q4:** Trong thiết kế hệ đo lường phân tán (nhiều encoder cách nhau hàng mét trên máy CNC hoặc hệ thống dẫn đường vũ khí), nguyên lý 'failure of simultaneity' liên quan thế nào đến vấn đề đồng bộ sensor thực tế? Đề xuất giải pháp kỹ thuật.

**Correct:** N/A


---
*Exported from Feynman Bot*
