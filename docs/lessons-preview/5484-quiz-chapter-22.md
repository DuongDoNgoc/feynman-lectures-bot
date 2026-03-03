---
lesson_id: 5484
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:06.223532+00:00"
content_hash: 0f3f88a72f9b
chapter_number: 22
chapter_title: Chapter 22
section_number: 6
section_title: 22–5Complex numbers
---
# ## Quiz: Số Phức — Đại số và Hình học

*Source: Chapter 22 - Chapter 22 (Section 6) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_22.html)*

## Quiz: Số Phức — Đại số và Hình học

### Câu 1 (Trắc nghiệm)

Kết quả của $(3 + 2i)(1 - i)$ bằng:

A. $3 - 2i^2 = 3 + 2 = 5$

B. $(3\cdot1 - 2\cdot(-1)) + i(3\cdot(-1) + 2\cdot1) = 5 - i$

C. $3 + 2i - 3i - 2i^2 = 5 - i$

D. Cả B và C đều đúng

**Đáp án: D**

*Giải thích:* $(3+2i)(1-i) = 3-3i+2i-2i^2 = 3 - i - 2(-1) = 3 + 2 - i = 5 - i$. Dùng công thức $(r+is)(p+iq) = (rp-sq) + i(rq+sp)$ với $r=3, s=2, p=1, q=-1$: thực $= 3(1) - 2(-1) = 5$; ảo $= 3(-1) + 2(1) = -1$. Kết quả: $5-i$. Cả B và C đều dẫn đến kết quả đúng.

### Câu 2 (Trắc nghiệm)

Trong mặt phẳng phức, số $z = 1 + i\sqrt{3}$ có modulus $r$ và argument $\theta$ (góc pha) bằng:

A. $r = \sqrt{2}$, $\theta = 45°$

B. $r = 2$, $\theta = 60°$

C. $r = 2$, $\theta = 30°$

D. $r = \sqrt{4} = 2$, $\theta = 45°$

**Đáp án: B**

*Giải thích:* $r = \sqrt{1^2 + (\sqrt{3})^2} = \sqrt{1+3} = \sqrt{4} = 2$. $\theta = \arctan(\sqrt{3}/1) = \arctan(\sqrt{3}) = 60°$. Vậy $z = 2e^{i\pi/3}$. Trong phân tích mạch 3 pha (motor drive của hệ thống servo), các phasor điện áp lệch nhau đúng 120° — biểu diễn trong mặt phẳng phức rất tự nhiên.

### Câu 3 (Trắc nghiệm)

Định lý cơ bản của đại số phát biểu rằng mọi phương trình đa thức bậc $n$ (với hệ số thực hoặc phức, $n \geq 1$):

A. Có đúng $n$ nghiệm thực

B. Có ít nhất một nghiệm trong tập số phức $\mathbb{C}$, và tổng cộng đúng $n$ nghiệm (kể nghiệm bội)

C. Chỉ có nghiệm nếu $n$ là số chẵn

D. Không có nghiệm khi hệ số là số phức

**Đáp án: B**

*Giải thích:* Đây là Định lý Cơ bản của Đại số (Fundamental Theorem of Algebra). Trong $\mathbb{C}$, phương trình bậc $n$ có đúng $n$ nghiệm (tính cả nghiệm bội). Đây là lý do Feynman nói "số phức là phát minh cuối cùng" — không cần mở rộng thêm. Ứng dụng trực tiếp: đặc trưng hệ thống điều khiển là nghiệm phức của phương trình đặc trưng $\det(sI - A) = 0$ (eigenvalues của ma trận trạng thái $A$).

### Câu 4 (Tự luận mở)

**Câu hỏi:** Trong hệ thống điều khiển servo của máy đo tọa độ CMM (Coordinate Measuring Machine) với độ phân giải sub-micromet, các kỹ sư điều khiển phân tích ổn định bằng cách xem xét vị trí các cực (poles) trong mặt phẳng phức. Giải thích: (a) Cực là gì về mặt toán học? (b) Tại sao cực phải có phần thực âm để hệ thống ổn định? (c) Phần ảo của cực liên quan đến gì trong ứng xử thực tế của hệ thống?

**Gợi ý trả lời:** (a) Cực là nghiệm phức $s = \sigma + j\omega$ của phương trình đặc trưng $1 + G(s)H(s) = 0$ — tức là nghiệm của đa thức mẫu số. (b) Đáp ứng thời gian chứa thành phần $e^{st} = e^{\sigma t} \cdot e^{j\omega t}$. Khi $\sigma < 0$: $e^{\sigma t} \to 0$ khi $t \to \infty$ — hệ thống tắt dần (ổn định). Khi $\sigma > 0$: $e^{\sigma t} \to \infty$ — hệ thống không ổn định. (c) Phần ảo $\omega$ là tần số dao động tắt dần (damped natural frequency). Cực $s = -2 \pm 5j$ nghĩa là hệ dao động với tần số $5$ rad/s và tắt dần với hằng số thời gian $\tau = 1/2 = 0.5s$. Trong CMM, chọn cực sao cho đáp ứng bước nhanh, không dao động quá, và sai số định vị nhỏ hơn 1 micromet.

```json
{"questions":[{"id":"q1","type":"mcq","question":"Kết quả của (3 + 2i)(1 - i) bằng:","options":["A. 3 - 2i² = 5","B. (3·1 - 2·(-1)) + i(3·(-1) + 2·1) = 5 - i","C. 3 + 2i - 3i - 2i² = 5 - i","D. Cả B và C đều đúng"],"answer":"D","explanation":"(3+2i)(1-i) = 3-3i+2i-2i² = 3-i+2 = 5-i. Cả hai cách tính B và C đều cho kết quả đúng 5-i."},{"id":"q2","type":"mcq","question":"Số z = 1 + i√3 có modulus r và argument θ bằng:","options":["A. r=√2, θ=45°","B. r=2, θ=60°","C. r=2, θ=30°","D. r=2, θ=45°"],"answer":"B","explanation":"r = √(1² + (√3)²) = √4 = 2. θ = arctan(√3/1) = 60°. Vậy z = 2e^(iπ/3). Trong phân tích mạch 3 pha cho motor drive, phasor lệch 120° biểu diễn tự nhiên trong mặt phẳng phức."},{"id":"q3","type":"mcq","question":"Định lý cơ bản của đại số phát biểu rằng mọi phương trình đa thức bậc n (n≥1):","options":["A. Có đúng n nghiệm thực","B. Có ít nhất một nghiệm phức, và tổng cộng đúng n nghiệm (kể nghiệm bội)","C. Chỉ có nghiệm nếu n là số chẵn","D. Không có nghiệm khi hệ số là số phức"],"answer":"B","explanation":"Định lý Cơ bản Đại số: trong C, phương trình bậc n có đúng n nghiệm. Số phức là 'phát minh cuối cùng'. Ứng dụng: eigenvalues của ma trận trạng thái hệ điều khiển là nghiệm phức của det(sI-A)=0."},{"id":"q4","type":"open","question":"Trong hệ thống servo CMM (độ phân giải sub-micromet), giải thích: (a) Cực là gì về mặt toán học? (b) Tại sao cực phải có phần thực âm để hệ thống ổn định? (c) Phần ảo của cực liên quan đến gì?","sample_answer":"(a) Cực là nghiệm phức s=σ+jω của phương trình đặc trưng 1+G(s)H(s)=0. (b) Đáp ứng chứa e^(st)=e^(σt)·e^(jωt): khi σ<0 thì e^(σt)→0 (ổn định); khi σ>0 thì e^(σt)→∞ (mất ổn định). (c) Phần ảo ω là tần số dao động tắt dần. Cực s=-2±5j: hệ dao động 5 rad/s, tắt dần τ=0.5s. Thiết kế CMM cần cực có phần thực âm đủ lớn (tắt nhanh) và phần ảo kiểm soát để sai số vị trí < 1 micromet."}]}
```


## Quiz Questions

**Q1:** Kết quả của (3 + 2i)(1 - i) bằng:
- A) A. 3 - 2i² = 5
- B) B. (3·1 - 2·(-1)) + i(3·(-1) + 2·1) = 5 - i
- C) C. 3 + 2i - 3i - 2i² = 5 - i
- D) D. Cả B và C đều đúng

**Correct:** D

**Explanation:** (3+2i)(1-i) = 3-3i+2i-2i² = 3-i+2 = 5-i. Cả hai cách tính B và C đều cho kết quả đúng 5-i.

**Q2:** Số z = 1 + i√3 có modulus r và argument θ bằng:
- A) A. r=√2, θ=45°
- B) B. r=2, θ=60°
- C) C. r=2, θ=30°
- D) D. r=2, θ=45°

**Correct:** B

**Explanation:** r = √(1² + (√3)²) = √4 = 2. θ = arctan(√3/1) = 60°. Vậy z = 2e^(iπ/3). Trong phân tích mạch 3 pha cho motor drive, phasor lệch 120° biểu diễn tự nhiên trong mặt phẳng phức.

**Q3:** Định lý cơ bản của đại số phát biểu rằng mọi phương trình đa thức bậc n (n≥1):
- A) A. Có đúng n nghiệm thực
- B) B. Có ít nhất một nghiệm phức, và tổng cộng đúng n nghiệm (kể nghiệm bội)
- C) C. Chỉ có nghiệm nếu n là số chẵn
- D) D. Không có nghiệm khi hệ số là số phức

**Correct:** B

**Explanation:** Định lý Cơ bản Đại số: trong C, phương trình bậc n có đúng n nghiệm. Số phức là 'phát minh cuối cùng'. Ứng dụng: eigenvalues của ma trận trạng thái hệ điều khiển là nghiệm phức của det(sI-A)=0.

**Q4:** Trong hệ thống servo CMM (độ phân giải sub-micromet), giải thích: (a) Cực là gì về mặt toán học? (b) Tại sao cực phải có phần thực âm để hệ thống ổn định? (c) Phần ảo của cực liên quan đến gì?

**Correct:** N/A


---
*Exported from Feynman Bot*
