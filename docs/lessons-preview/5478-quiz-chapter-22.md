---
lesson_id: 5478
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:06.019201+00:00"
content_hash: 0bf64ef4711e
chapter_number: 22
chapter_title: Chapter 22
section_number: 2
section_title: 22–1Addition and multiplication
---
# ## Quiz: Đại số Phức và Công thức Euler

*Source: Chapter 22 - Chapter 22 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_22.html)*

## Quiz: Đại số Phức và Công thức Euler

### Câu 1 (Trắc nghiệm)

Quy tắc lũy thừa nào sau đây là ĐÚNG trong đại số phức?

A. $e^{i\alpha} \cdot e^{i\beta} = e^{i(\alpha \cdot \beta)}$

B. $e^{i\alpha} \cdot e^{i\beta} = e^{i(\alpha + \beta)}$

C. $e^{i\alpha} + e^{i\beta} = e^{i(\alpha + \beta)}$

D. $(e^{i\alpha})^2 = e^{i\alpha/2}$

**Đáp án: B**

*Giải thích:* Quy tắc lũy thừa cơ bản: $a^s \cdot a^t = a^{s+t}$ áp dụng cho cả số phức. Do đó $e^{i\alpha} \cdot e^{i\beta} = e^{i(\alpha+\beta)}$. Đây chính là cơ sở của phép nhân phasor: nhân hai số phức ở dạng cực tương đương cộng các góc pha.

### Câu 2 (Trắc nghiệm)

Trong mặt phẳng phức (complex plane), phép nhân một số phức $z$ với $e^{i\pi/2}$ tương đương với:

A. Tăng modulus của $z$ lên 2 lần

B. Phản chiếu $z$ qua trục thực

C. Xoay vector $z$ một góc 90° ngược chiều kim đồng hồ

D. Lấy liên hợp phức (complex conjugate) của $z$

**Đáp án: C**

*Giải thích:* $e^{i\pi/2} = \cos(90°) + i\sin(90°) = i$. Nhân $z = re^{i\theta}$ với $e^{i\pi/2}$ cho kết quả $re^{i(\theta + \pi/2)}$ — vector xoay thêm 90° mà không thay đổi độ lớn. Tính chất này cực kỳ quan trọng trong điều khiển động cơ: phép tích phân tín hiệu sine tương đương dịch pha 90°.

### Câu 3 (Trắc nghiệm)

Một phasor điện áp là $\hat{V} = 5e^{i\pi/4}$ (volt). Giá trị tức thời $v(t) = \text{Re}\{\hat{V}e^{i\omega t}\}$ tại thời điểm $\omega t = \pi/4$ bằng:

A. $5\cos(\pi/2) = 0$ V

B. $5\cos(\pi/4) \approx 3.54$ V

C. $5$ V

D. $5\cos(\pi/8) \approx 4.62$ V

**Đáp án: C**

*Giải thích:* $v(t) = \text{Re}\{5e^{i\pi/4} \cdot e^{i\pi/4}\} = \text{Re}\{5e^{i\pi/2}\} = 5\cos(\pi/2) = 5\cos(90°) = 0$... Khoan, tính lại: $5e^{i(\pi/4 + \pi/4)} = 5e^{i\pi/2} = 5(\cos 90° + i\sin 90°) = 5i$. Phần thực = 0. *Đáp án đúng thực ra là A.* Lưu ý: câu này kiểm tra khả năng tính $\text{Re}\{\cdot\}$ cẩn thận. Đáp án A đúng: $v = 5\cos(\pi/2) = 0$ V.

*[Đính chính: Đáp án đúng là A — 0 V]*

### Câu 4 (Tự luận mở)

**Câu hỏi:** Trong công việc thiết kế hệ thống đo lường độ chính xác cao (laser interferometry, encoder quang học), bạn thường gặp tín hiệu dạng $A\cos(\omega t + \phi)$. Hãy giải thích tại sao biểu diễn phasor (số phức) lại thuận tiện hơn khi phân tích và thiết kế bộ lọc số cho những tín hiệu này? Cho ví dụ cụ thể từ ít nhất một thiết bị bạn đã/có thể sẽ thiết kế.

**Gợi ý trả lời:** Phasor $\hat{A} = Ae^{i\phi}$ nén thông tin biên độ và pha vào một số phức duy nhất. Khi cộng $N$ tín hiệu cùng tần số, phép cộng phasor (vector) thay thế $N$ phép cộng lượng giác phức tạp. Trong bộ lọc số FIR/IIR cho encoder quang học: đáp ứng tần số $H(e^{j\omega})$ là số phức — biên độ cho biết độ khuếch đại, pha cho biết độ trễ nhóm (group delay). Kỹ sư đọc biểu đồ Bode (Bode plot) chính là đọc modulus và argument của $H(j\omega)$ theo tần số. Ví dụ: thiết kế bộ lọc Kalman cho IMU, ma trận covariance $P$ liên quan đến phổ công suất — đều cần xử lý số phức.

```json
{"questions":[{"id":"q1","type":"mcq","question":"Quy tắc lũy thừa nào sau đây là ĐÚNG trong đại số phức?","options":["A. e^(iα) · e^(iβ) = e^(i·α·β)","B. e^(iα) · e^(iβ) = e^(i(α+β))","C. e^(iα) + e^(iβ) = e^(i(α+β))","D. (e^(iα))² = e^(iα/2)"],"answer":"B","explanation":"Quy tắc a^s · a^t = a^(s+t) áp dụng cho cả số phức. e^(iα)·e^(iβ) = e^(i(α+β)). Phép nhân phasor tương đương cộng các góc pha."},{"id":"q2","type":"mcq","question":"Trong mặt phẳng phức, phép nhân một số phức z với e^(iπ/2) tương đương với:","options":["A. Tăng modulus của z lên 2 lần","B. Phản chiếu z qua trục thực","C. Xoay vector z một góc 90° ngược chiều kim đồng hồ","D. Lấy liên hợp phức của z"],"answer":"C","explanation":"e^(iπ/2) = i. Nhân z = re^(iθ) với e^(iπ/2) cho re^(i(θ+π/2)) — vector xoay 90° ngược chiều kim đồng hồ, modulus không đổi."},{"id":"q3","type":"mcq","question":"Phasor \u0111i\u1ec7n áp \u0302V = 5e^(iπ/4) V. Giá tr\u1ecb t\u1ee9c th\u1eddi v(t)=Re{\u0302V·e^(iωt)} t\u1ea1i ωt = π/4 bằng:","options":["A. 0 V","B. 5cos(π/4) ≈ 3.54 V","C. 5 V","D. 5cos(π/8) ≈ 4.62 V"],"answer":"A","explanation":"v = Re{5e^(iπ/4)·e^(iπ/4)} = Re{5e^(iπ/2)} = 5cos(π/2) = 5·0 = 0 V. Tổng góc pha = π/2, cos(π/2)=0."},{"id":"q4","type":"open","question":"Trong thiết kế hệ thống đo lường độ chính xác cao (laser interferometry, encoder quang học), tại sao biểu diễn phasor (số phức) lại thuận tiện hơn khi phân tích và thiết kế bộ lọc số? Cho ví dụ cụ thể.","sample_answer":"Phasor Â = Ae^(iφ) nén biên độ và pha vào một số duy nhất. Cộng N tín hiệu cùng tần số trở thành cộng N vector trên mặt phẳng phức — đơn giản hơn N phép lượng giác. Đáp ứng tần số H(e^(jω)) của bộ lọc số FIR/IIR là số phức: |H| cho biên độ, angle(H) cho trễ pha. Khi thiết kế bộ lọc Kalman cho IMU trong vũ khí dẫn đường, phổ nhiễu và tín hiệu đều được mô tả qua hàm mật độ phổ công suất (PSD) — tất cả đều xử lý qua biến đổi Fourier, tức là số phức."}]}
```


## Quiz Questions

**Q1:** Quy tắc lũy thừa nào sau đây là ĐÚNG trong đại số phức?
- A) A. e^(iα) · e^(iβ) = e^(i·α·β)
- B) B. e^(iα) · e^(iβ) = e^(i(α+β))
- C) C. e^(iα) + e^(iβ) = e^(i(α+β))
- D) D. (e^(iα))² = e^(iα/2)

**Correct:** B

**Explanation:** Quy tắc a^s · a^t = a^(s+t) áp dụng cho cả số phức. e^(iα)·e^(iβ) = e^(i(α+β)). Phép nhân phasor tương đương cộng các góc pha.

**Q2:** Trong mặt phẳng phức, phép nhân một số phức z với e^(iπ/2) tương đương với:
- A) A. Tăng modulus của z lên 2 lần
- B) B. Phản chiếu z qua trục thực
- C) C. Xoay vector z một góc 90° ngược chiều kim đồng hồ
- D) D. Lấy liên hợp phức của z

**Correct:** C

**Explanation:** e^(iπ/2) = i. Nhân z = re^(iθ) với e^(iπ/2) cho re^(i(θ+π/2)) — vector xoay 90° ngược chiều kim đồng hồ, modulus không đổi.

**Q3:** Phasor điện áp ̂V = 5e^(iπ/4) V. Giá trị tức thời v(t)=Re{̂V·e^(iωt)} tại ωt = π/4 bằng:
- A) A. 0 V
- B) B. 5cos(π/4) ≈ 3.54 V
- C) C. 5 V
- D) D. 5cos(π/8) ≈ 4.62 V

**Correct:** A

**Explanation:** v = Re{5e^(iπ/4)·e^(iπ/4)} = Re{5e^(iπ/2)} = 5cos(π/2) = 5·0 = 0 V. Tổng góc pha = π/2, cos(π/2)=0.

**Q4:** Trong thiết kế hệ thống đo lường độ chính xác cao (laser interferometry, encoder quang học), tại sao biểu diễn phasor (số phức) lại thuận tiện hơn khi phân tích và thiết kế bộ lọc số? Cho ví dụ cụ thể.

**Correct:** N/A


---
*Exported from Feynman Bot*
