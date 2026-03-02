---
lesson_id: 5403
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-02T15:10:28.527564+00:00"
content_hash: f2d83f764996
chapter_number: 12
chapter_title: Chapter 12
section_number: 6
section_title: 12–5Pseudo forces
---
# Quiz: Lực Giả

*Source: Chapter 12 - Chapter 12 (Section 6) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_12.html)*

# Quiz: Lực Giả

## Câu 1

Một thang máy đang tăng tốc đi lên với gia tốc $a = 2\ m/s^2$. Một người có khối lượng $m = 70\ kg$ đứng trong thang máy. Lực giả tác dụng lên người (theo quan sát từ hệ quy chiếu thang máy) có độ lớn và hướng là:

A) $140\ N$ hướng lên
B) $140\ N$ hướng xuống
C) $686\ N$ hướng xuống
D) $826\ N$ hướng xuống

**Đáp án: B**

*Giải thích: Lực giả luôn ngược chiều gia tốc của hệ quy chiếu. Thang máy tăng tốc lên, nên lực giả hướng xuống: $F_{\text{giả}} = ma = 70 \times 2 = 140\ N$ hướng xuống. Người trong thang cảm nhận trọng lượng biểu kiến $= mg + ma = 70(9.8+2) = 826\ N$.*

## Câu 2

Đặc tính nào của lực giả là manh mối Einstein dùng để đề xuất nguyên lý tương đương?

A) Lực giả không phụ thuộc vào vị trí
B) Lực giả tỷ lệ thuận với khối lượng của vật, giống như trọng lực
C) Lực giả chỉ xuất hiện trong hệ quay
D) Lực giả không thể đo được bằng dụng cụ

**Đáp án: B**

*Giải thích: Cả lực giả ($F = ma$) và trọng lực ($F = mg$) đều tỷ lệ với khối lượng $m$. Điều này có nghĩa là mọi vật đều có cùng gia tốc trong hệ phi quán tính — giống hệt như mọi vật rơi tự do với cùng gia tốc $g$. Einstein nhận ra đây không phải trùng hợp và xây dựng Nguyên lý Tương Đương từ đó.*

## Câu 3

Hệ thống dẫn đường quán tính (INS) trong tên lửa sử dụng accelerometer. Accelerometer thực chất đo:

A) Gia tốc tuyệt đối so với không gian quán tính
B) Lực giả tác dụng lên khối lượng thử nghiệm bên trong
C) Vận tốc của tên lửa so với mặt đất
D) Cả trọng lực và gia tốc động cơ riêng biệt

**Đáp án: B**

*Giải thích: Accelerometer hoạt động bằng cách đo lực tác dụng lên một khối lượng thử nghiệm nhỏ bên trong hộp kín. Trong hệ quy chiếu tên lửa (phi quán tính), khối lượng thử nghiệm chịu lực giả $-ma$. Accelerometer đo lực này và tính ngược lại gia tốc $a$. Vì không thể phân biệt trọng lực với lực giả (nguyên lý tương đương), INS cần dữ liệu bổ sung (GPS, bản đồ trọng trường) để tách riêng hai thành phần.*

## Câu 4 — Tự Luận

Trong thiết kế robot công nghiệp, khi cánh tay robot quay nhanh và mang tải nặng, các kỹ sư cần bù "lực giả" trong thuật toán điều khiển. Hãy giải thích: tại sao việc bỏ qua lực giả (ly tâm và Coriolis) sẽ dẫn đến sai số trong gia công chính xác? Và trong hệ thống đo lực lắp trên đầu robot, cần hiệu chỉnh như thế nào?

*Gợi ý trả lời: Lực ly tâm $m\omega^2r$ và Coriolis $2m\omega v$ làm lệch vị trí đầu công cụ khỏi quỹ đạo lập trình. Trong đo lực: nếu không bù, cảm biến sẽ báo lực = lực thực + lực giả, gây sai số đo.*

```json
{
  "quiz_id": 5403,
  "questions": [
    {"id": 1, "answer": "B", "concept": "lực giả hướng ngược gia tốc hệ quy chiếu"},
    {"id": 2, "answer": "B", "concept": "tỷ lệ với khối lượng - nền tảng nguyên lý tương đương"},
    {"id": 3, "answer": "B", "concept": "accelerometer đo lực giả trong hệ phi quán tính"}
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


---
*Exported from Feynman Bot*
