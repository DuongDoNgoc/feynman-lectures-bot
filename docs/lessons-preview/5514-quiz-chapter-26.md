---
lesson_id: 5514
lesson_type: quiz
approval_status: pending
exported_at: "2026-03-02T15:10:31.466276+00:00"
content_hash: c1a1c3200106
chapter_number: 26
chapter_title: Chapter 26
section_number: 6
section_title: 26–5A more precise statement of Fermat’s principle
---
# ## Kiểm Tra: Nguyên Lý Stationary Time và Nhiễu Xạ Ánh Sáng

*Source: Chapter 26 - Chapter 26 (Section 6) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_26.html)*

## Kiểm Tra: Nguyên Lý Stationary Time và Nhiễu Xạ Ánh Sáng

### Câu 1 (Trắc nghiệm)

Phát biểu chính xác nhất của nguyên lý Fermat là:

A. Ánh sáng luôn đi theo đường có thời gian truyền ngắn nhất tuyệt đối
B. Ánh sáng đi theo đường mà thời gian là cực trị (stationary), tức là không có thay đổi bậc nhất khi perturbation nhỏ
C. Ánh sáng chọn đường có độ dài ngắn nhất trong môi trường đồng nhất
D. Ánh sáng đi theo đường mà năng lượng là nhỏ nhất

**Đáp án: B**

*Giải thích:* Phát biểu "thời gian nhỏ nhất" không đúng trong trường hợp gương lõm, nơi tia phản xạ đi theo đường dài hơn đường thẳng nhưng vẫn thỏa mãn điều kiện stationary ($\delta t = 0$). Đây là điểm cực đại địa phương về thời gian, không phải cực tiểu.

---

### Câu 2 (Trắc nghiệm)

Tại sao khe hẹp trong thí nghiệm với sóng radio lại cho phép sóng truyền đến điểm $D'$ (lệch khỏi trục) nhiều hơn khe rộng?

A. Khe hẹp có ít vật chắn hơn nên sóng truyền qua dễ hơn
B. Khe hẹp loại bỏ các đường đi có thời gian khác nhau, giảm giao thoa phá, sóng lan rộng ra theo nhiều hướng
C. Khe hẹp tập trung năng lượng vào một chùm hẹp hướng về $D'$
D. Bề mặt cạnh khe hẹp phản xạ sóng về phía $D'$

**Đáp án: B**

*Giải thích:* Khe rộng cho phép nhiều đường đi qua, nhưng các đường từ các phần khác nhau của khe đến $D'$ có thời gian (pha) khác nhau → giao thoa phá → tín hiệu yếu. Khe hẹp chỉ để lại một vùng Fresnel → không có giao thoa phá → sóng phân tán rộng (nhiễu xạ), đến được $D'$.

---

### Câu 3 (Trắc nghiệm)

Giới hạn nhiễu xạ (diffraction limit) của một hệ thống quang học với thấu kính đường kính $D = 50\,\text{mm}$, tiêu cự $f = 100\,\text{mm}$, bước sóng $\lambda = 500\,\text{nm}$ là:

A. $0.61\,\mu\text{m}$
B. $1.22\,\mu\text{m}$
C. $2.44\,\mu\text{m}$
D. $0.5\,\mu\text{m}$

**Đáp án: B**

*Giải thích:* $\Delta x = 1.22 \frac{\lambda f}{D} = 1.22 \times \frac{500 \times 10^{-6} \times 100}{50} = 1.22 \times 10^{-3}\,\text{mm} = 1.22\,\mu\text{m}$. Đây là độ phân giải nhỏ nhất có thể theo tiêu chí Rayleigh.

---

### Câu 4 (Tự luận mở)

**Câu hỏi:** Trong hệ thống encoder quang học tuyến tính (linear optical encoder) dùng để đo vị trí với độ phân giải $1\,\mu\text{m}$ mà bạn tích hợp vào hệ servo, bước sóng laser là $\lambda = 635\,\text{nm}$. Nếu aperture đọc (reading aperture) có chiều rộng $a = 0.5\,\text{mm}$ và khoảng cách từ vạch chia đến aperture là $d = 2\,\text{mm}$, hãy tính bán kính Fresnel và nhận xét xem hiệu ứng nhiễu xạ có ảnh hưởng đáng kể đến phép đọc không. Bạn sẽ thiết kế aperture như thế nào để tối ưu?

*Gợi ý trả lời:* $r_F = \sqrt{\lambda d} = \sqrt{635 \times 10^{-9} \times 2 \times 10^{-3}} \approx 35\,\mu\text{m}$. Aperture $0.5\,\text{mm}$ lớn hơn nhiều so với $r_F$, nên nhiễu xạ không đáng kể — đây là chế độ quang học hình học (ray optics). Nhưng nếu bước vạch $p = 20\,\mu\text{m}$, cần xem xét moiré và diffraction order.

```json
{
  "quiz_id": "q5514",
  "topic": "Stationary Time Principle and Diffraction",
  "questions": [
    {"id": 1, "type": "mcq", "answer": "B"},
    {"id": 2, "type": "mcq", "answer": "B"},
    {"id": 3, "type": "mcq", "answer": "B"},
    {"id": 4, "type": "open", "topic": "Fresnel zone and optical encoder design"}
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
