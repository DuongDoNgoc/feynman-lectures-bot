---
lesson_id: 5481
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:06.120336+00:00"
content_hash: ae72fe469134
chapter_number: 22
chapter_title: Chapter 22
section_number: 5
section_title: 22–4Approximating irrational numbers
---
# ## Quiz: Lũy thừa Vô tỉ và Logarithm

*Source: Chapter 22 - Chapter 22 (Section 5) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_22.html)*

## Quiz: Lũy thừa Vô tỉ và Logarithm

### Câu 1 (Trắc nghiệm)

Để tính $10^{\sqrt{2}}$, phương pháp đúng về mặt toán học là:

A. Không thể tính được vì $\sqrt{2}$ là số vô tỉ

B. Lấy giới hạn của dãy $10^{p_n}$ với $p_n$ là dãy số hữu tỉ hội tụ đến $\sqrt{2}$

C. Nhân $10$ với $\sqrt{2}$ lần

D. Dùng công thức $10^{\sqrt{2}} = \sqrt{10^2} = 10$

**Đáp án: B**

*Giải thích:* Lũy thừa vô tỉ được định nghĩa qua giới hạn. Dãy $10^{1.4}, 10^{1.41}, 10^{1.414}, ...$ là dãy lũy thừa hữu tỉ hội tụ đến $10^{\sqrt{2}} \approx 25.9946$. Đây là cơ sở lý thuyết của hàm `pow()` trong vi điều khiển.

### Câu 2 (Trắc nghiệm)

Một cảm biến âm thanh có dải động 80 dB ($20\log_{10}(V/V_0) = 80$). Tỉ số $V/V_0$ bằng:

A. $80$

B. $10^4 = 10000$

C. $10^{80} $

D. $e^{80}$

**Đáp án: B**

*Giải thích:* $20\log_{10}(V/V_0) = 80 \Rightarrow \log_{10}(V/V_0) = 4 \Rightarrow V/V_0 = 10^4 = 10000$. Trong thiết kế ADC cho hệ thống đo lường, 80 dB tương ứng tỉ số tín hiệu/nhiễu 10000:1 — đây là lý do chọn ADC 14-bit (dải động lý thuyết $\approx 86$ dB).

### Câu 3 (Trắc nghiệm)

Biết $\log_{10} 2 \approx 0.301$ và $\log_{10} 3 \approx 0.477$. Giá trị $\log_{10} 6$ bằng:

A. $0.301 \times 0.477 \approx 0.1436$

B. $0.477 - 0.301 = 0.176$

C. $0.301 + 0.477 = 0.778$

D. $\sqrt{0.301 \times 0.477} \approx 0.379$

**Đáp án: C**

*Giải thích:* $\log_{10} 6 = \log_{10}(2 \times 3) = \log_{10} 2 + \log_{10} 3 = 0.301 + 0.477 = 0.778$. Đây là quy tắc $\log_b(ac) = \log_b a + \log_b c$ — biến phép nhân thành phép cộng. Kiểm tra: $10^{0.778} \approx 6.0$ ✓.

### Câu 4 (Tự luận mở)

**Câu hỏi:** Trong hệ thống đo lường laser interferometry mà bạn thiết kế để kiểm tra bề mặt ở độ phân giải micromet, cảm biến photodetector có đặc tính phi tuyến dạng logarithmic: $V_{out} = 2\ln(I_{in}/I_0)$. Khi tích hợp cảm biến này vào MCU (microcontroller), bạn cần thiết kế hàm hiệu chỉnh ngược (inverse calibration). Hãy viết công thức hiệu chỉnh và giải thích tại sao bảng LUT (look-up table) trong ROM thường được dùng thay vì tính trực tiếp hàm `exp()` trong vòng lặp điều khiển thời gian thực.

**Gợi ý trả lời:** Hàm ngược: $I_{in} = I_0 \cdot e^{V_{out}/2}$. Trong vòng lặp điều khiển thời gian thực (ví dụ tần số lấy mẫu 10 kHz), mỗi chu kỳ chỉ có $100\mu s$. Hàm `exp()` trong C thường tốn 50–200 clock cycles tùy MCU — có thể chiếm đến 10–20% CPU time. Bảng LUT pre-computed trong ROM cho phép tra cứu trong 1–3 clock cycles (địa chỉ hóa trực tiếp), đổi lại độ chính xác phụ thuộc kích thước bảng và phương pháp nội suy. Đây chính xác là cách các nhà toán học thế kỷ 17 xây dựng bảng log để tra cứu nhanh hơn tính toán.

```json
{"questions":[{"id":"q1","type":"mcq","question":"Để tính 10^√2, phương pháp đúng về mặt toán học là:","options":["A. Không thể tính được vì √2 là số vô tỉ","B. Lấy giới hạn của dãy 10^(pn) với pn là dãy hữu tỉ hội tụ đến √2","C. Nhân 10 với √2 lần","D. Dùng công thức 10^√2 = √(10²) = 10"],"answer":"B","explanation":"Lũy thừa vô tỉ được định nghĩa qua giới hạn: dãy 10^1.4, 10^1.41, 10^1.414,... hội tụ đến 10^√2 ≈ 25.9946. Đây là cơ sở của hàm pow() trong vi điều khiển."},{"id":"q2","type":"mcq","question":"Một cảm biến âm thanh có dải động 80 dB (20·log₁₀(V/V₀)=80). Tỉ số V/V₀ bằng:","options":["A. 80","B. 10⁴ = 10000","C. 10⁸⁰","D. e⁸⁰"],"answer":"B","explanation":"20·log₁₀(V/V₀)=80 → log₁₀(V/V₀)=4 → V/V₀=10⁴=10000. ADC 14-bit có dải động lý thuyết ≈86 dB tương ứng tỉ số ~20000:1."},{"id":"q3","type":"mcq","question":"Biết log₁₀(2)≈0.301 và log₁₀(3)≈0.477. Giá trị log₁₀(6) bằng:","options":["A. 0.301 × 0.477 ≈ 0.1436","B. 0.477 - 0.301 = 0.176","C. 0.301 + 0.477 = 0.778","D. √(0.301×0.477) ≈ 0.379"],"answer":"C","explanation":"log₁₀(6) = log₁₀(2×3) = log₁₀(2) + log₁₀(3) = 0.301 + 0.477 = 0.778. Quy tắc log_b(ac) = log_b(a) + log_b(c) biến nhân thành cộng."},{"id":"q4","type":"open","question":"Cảm biến photodetector có đặc tính phi tuyến V_out = 2·ln(I_in/I_0). Viết công thức hiệu chỉnh ngược và giải thích tại sao LUT trong ROM thường dùng thay vì tính exp() trực tiếp trong vòng lặp điều khiển thời gian thực.","sample_answer":"Hàm ngược: I_in = I_0·e^(V_out/2). Trong vòng lặp 10 kHz (chu kỳ 100μs), hàm exp() tốn 50-200 clock cycles tùy MCU, có thể chiếm 10-20% CPU time. Bảng LUT pre-computed cho phép tra cứu 1-3 cycles (địa chỉ hóa trực tiếp), đổi lại độ chính xác phụ thuộc kích thước bảng và nội suy. Đây là nguyên lý tương tự bảng log thế kỷ 17: pre-compute để tra nhanh hơn tính toán."}]}
```


## Quiz Questions

**Q1:** Để tính 10^√2, phương pháp đúng về mặt toán học là:
- A) A. Không thể tính được vì √2 là số vô tỉ
- B) B. Lấy giới hạn của dãy 10^(pn) với pn là dãy hữu tỉ hội tụ đến √2
- C) C. Nhân 10 với √2 lần
- D) D. Dùng công thức 10^√2 = √(10²) = 10

**Correct:** B

**Explanation:** Lũy thừa vô tỉ được định nghĩa qua giới hạn: dãy 10^1.4, 10^1.41, 10^1.414,... hội tụ đến 10^√2 ≈ 25.9946. Đây là cơ sở của hàm pow() trong vi điều khiển.

**Q2:** Một cảm biến âm thanh có dải động 80 dB (20·log₁₀(V/V₀)=80). Tỉ số V/V₀ bằng:
- A) A. 80
- B) B. 10⁴ = 10000
- C) C. 10⁸⁰
- D) D. e⁸⁰

**Correct:** B

**Explanation:** 20·log₁₀(V/V₀)=80 → log₁₀(V/V₀)=4 → V/V₀=10⁴=10000. ADC 14-bit có dải động lý thuyết ≈86 dB tương ứng tỉ số ~20000:1.

**Q3:** Biết log₁₀(2)≈0.301 và log₁₀(3)≈0.477. Giá trị log₁₀(6) bằng:
- A) A. 0.301 × 0.477 ≈ 0.1436
- B) B. 0.477 - 0.301 = 0.176
- C) C. 0.301 + 0.477 = 0.778
- D) D. √(0.301×0.477) ≈ 0.379

**Correct:** C

**Explanation:** log₁₀(6) = log₁₀(2×3) = log₁₀(2) + log₁₀(3) = 0.301 + 0.477 = 0.778. Quy tắc log_b(ac) = log_b(a) + log_b(c) biến nhân thành cộng.

**Q4:** Cảm biến photodetector có đặc tính phi tuyến V_out = 2·ln(I_in/I_0). Viết công thức hiệu chỉnh ngược và giải thích tại sao LUT trong ROM thường dùng thay vì tính exp() trực tiếp trong vòng lặp điều khiển thời gian thực.

**Correct:** N/A


---
*Exported from Feynman Bot*
