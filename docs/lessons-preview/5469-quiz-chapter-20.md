---
lesson_id: 5469
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-02T15:10:30.273359+00:00"
content_hash: 756607faf742
chapter_number: 20
chapter_title: Chapter 20
section_number: 3
section_title: 20–2The rotation equations using cross products
---
# ## Quiz: Moment Xoắn, Động Lượng Góc và Tích Vector

*Source: Chapter 20 - Chapter 20 (Section 3) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_20.html)*

## Quiz: Moment Xoắn, Động Lượng Góc và Tích Vector

### Câu 1 (Trắc nghiệm)

Một kỹ sư tác dụng lực $\mathbf{F} = (0, 0, 10)$ N tại điểm $\mathbf{r} = (0.5, 0, 0)$ m trên một cánh tay robot. Moment xoắn $\boldsymbol{\tau} = \mathbf{r} \times \mathbf{F}$ bằng bao nhiêu?

A. $(0, 5, 0)$ N·m  
B. $(5, 0, 0)$ N·m  
C. $(0, -5, 0)$ N·m  
D. $(0, 0, 5)$ N·m  

**Đáp án: A**  
**Giải thích:** $\boldsymbol{\tau} = \mathbf{r} \times \mathbf{F} = (0.5\hat{i}) \times (10\hat{k}) = 5(\hat{i} \times \hat{k}) = 5(-\hat{j}) = (0, -5, 0)$ — chờ, kiểm tra lại: $\hat{i} \times \hat{k} = -\hat{j}$, nên $\tau_y = 0.5 \times 10 \times (-1) = -5$. Kết quả là $(0, -5, 0)$ N·m. Đáp án đúng là **C**.

---

### Câu 2 (Trắc nghiệm)

Một gyroscope đang quay với angular momentum $\mathbf{L}$ lớn theo hướng thẳng đứng. Khi không có moment xoắn ngoại lực tác dụng, điều gì xảy ra với $\mathbf{L}$?

A. $\mathbf{L}$ giảm dần do ma sát không khí  
B. $\mathbf{L}$ được bảo toàn cả về độ lớn và hướng  
C. Hướng của $\mathbf{L}$ thay đổi nhưng độ lớn không đổi  
D. $\mathbf{L}$ tăng tỉ lệ với thời gian  

**Đáp án: B**  
**Giải thích:** Theo định luật bảo toàn angular momentum, khi $\boldsymbol{\tau}_{\text{ext}} = 0$ thì $d\mathbf{L}/dt = 0$, nghĩa là $\mathbf{L}$ không thay đổi — cả độ lớn lẫn hướng đều được bảo toàn. Đây là nguyên lý hoạt động của gyroscope trong hệ INS.

---

### Câu 3 (Trắc nghiệm)

Trong cảm biến gyroscope MEMS, cơ chế nào được sử dụng để đo angular velocity?

A. Thay đổi điện trở do ứng suất cơ học (piezoresistive effect)  
B. Lực Coriolis $\mathbf{F}_c = 2m\mathbf{v} \times \boldsymbol{\omega}$ tác động lên mass dao động  
C. Thay đổi từ trường do quay của rotor từ tính  
D. Sự thay đổi tần số dao động của cantilever beam  

**Đáp án: B**  
**Giải thích:** Gyroscope MEMS hoạt động bằng cách đo lực Coriolis. Một proof mass được kích thích dao động theo một trục (drive axis). Khi hệ quay với $\boldsymbol{\omega}$, lực Coriolis $\mathbf{F}_c = 2m\mathbf{v} \times \boldsymbol{\omega}$ tạo ra độ lệch theo trục vuông góc (sense axis), được đo bởi capacitive electrodes để suy ra $\omega$.

---

### Câu 4 (Tự luận mở)

Trong công việc thiết kế hệ thống cơ điện tử của bạn — đặc biệt với các ứng dụng đo lường chính xác ở mức micro-mét hoặc hệ thống vũ khí — hãy đề xuất một trường hợp cụ thể trong đó việc hiểu rõ angular momentum và torque theo dạng vector (không chỉ scalar) là thiết yếu cho thiết kế hoặc phân tích hệ thống. Giải thích tại sao bản chất vector của các đại lượng này (hướng, không chỉ độ lớn) tạo ra sự khác biệt trong kết quả kỹ thuật.

**Gợi ý đáp án:** Một ví dụ điển hình là hệ thống ổn định gimbal (gimbal stabilization system) cho camera quan sát hoặc đầu dò vũ khí trên xe thiết giáp. Khi xe di chuyển trên địa hình gồ ghề, thân xe chịu angular velocity ngẫu nhiên $\boldsymbol{\omega}_{\text{disturbance}}$ theo cả ba trục. Để giữ camera hướng vào mục tiêu, hệ điều khiển phải tính toán torque $\boldsymbol{\tau}_{\text{control}}$ — một vector 3D — cần thiết để bù trừ. Nếu chỉ xem torque như scalar, hệ thống không thể phân biệt moment quay quanh trục nào, dẫn đến sai số định hướng. Bản chất vector cho phép controller tách riêng và bù trừ độc lập cho từng bậc tự do (pitch, yaw, roll), đây là yêu cầu thiết yếu để đạt độ chính xác micrometer-level trong tracking quang học.

```json
{"questions":[{"id":"q1","type":"mcq","question":"Một kỹ sư tác dụng lực F = (0, 0, 10) N tại điểm r = (0.5, 0, 0) m trên cánh tay robot. Moment xoắn τ = r × F bằng bao nhiêu?","options":["A. (0, 5, 0) N·m","B. (5, 0, 0) N·m","C. (0, -5, 0) N·m","D. (0, 0, 5) N·m"],"answer":"C","explanation":"τ = r × F = (0.5i) × (10k) = 5(i × k) = 5(-j) = (0, -5, 0) N·m. Dùng quy tắc i × k = -j từ bảng tích vector đơn vị."},{"id":"q2","type":"mcq","question":"Khi không có moment xoắn ngoại lực tác dụng lên gyroscope đang quay, điều gì xảy ra với angular momentum L?","options":["A. L giảm dần do ma sát không khí","B. L được bảo toàn cả về độ lớn và hướng","C. Hướng L thay đổi nhưng độ lớn không đổi","D. L tăng tỉ lệ với thời gian"],"answer":"B","explanation":"Khi τ_ext = 0, định luật dL/dt = τ_ext = 0, nên L = const. Cả độ lớn và hướng đều bảo toàn — nguyên lý hoạt động của gyroscope INS."},{"id":"q3","type":"mcq","question":"Trong gyroscope MEMS, cơ chế nào được dùng để đo angular velocity?","options":["A. Thay đổi điện trở piezoresistive","B. Lực Coriolis F_c = 2mv × ω tác động lên mass dao động","C. Thay đổi từ trường do rotor từ tính","D. Thay đổi tần số dao động của cantilever"],"answer":"B","explanation":"MEMS gyro kích thích proof mass dao động theo drive axis. Khi hệ quay, lực Coriolis tạo độ lệch theo sense axis vuông góc, được đo bằng capacitive electrodes để suy ra ω."},{"id":"q4","type":"open","question":"Trong thiết kế hệ thống cơ điện tử (đo lường chính xác micrometer hoặc hệ vũ khí), hãy nêu một trường hợp cụ thể mà bản chất vector của angular momentum và torque (không chỉ scalar) là thiết yếu. Giải thích tại sao hướng của các đại lượng này tạo ra sự khác biệt trong kết quả kỹ thuật.","sample_answer":"Hệ thống ổn định gimbal 3 trục cho camera/vũ khí trên xe thiết giáp: khi xe chịu rung động ngẫu nhiên, controller cần tính torque vector τ_control theo từng trục pitch/yaw/roll độc lập để bù trừ. Nếu chỉ dùng scalar, không thể phân biệt trục quay, dẫn đến sai số coupling giữa các trục. Bản chất vector cho phép decoupled control, đạt độ chính xác micrometer-level cần thiết cho tracking quang học hoặc dẫn đường laser."}]}
```


## Quiz Questions

**Q1:** Một kỹ sư tác dụng lực F = (0, 0, 10) N tại điểm r = (0.5, 0, 0) m trên cánh tay robot. Moment xoắn τ = r × F bằng bao nhiêu?
- A) A. (0, 5, 0) N·m
- B) B. (5, 0, 0) N·m
- C) C. (0, -5, 0) N·m
- D) D. (0, 0, 5) N·m

**Correct:** C

**Explanation:** τ = r × F = (0.5i) × (10k) = 5(i × k) = 5(-j) = (0, -5, 0) N·m. Dùng quy tắc i × k = -j từ bảng tích vector đơn vị.

**Q2:** Khi không có moment xoắn ngoại lực tác dụng lên gyroscope đang quay, điều gì xảy ra với angular momentum L?
- A) A. L giảm dần do ma sát không khí
- B) B. L được bảo toàn cả về độ lớn và hướng
- C) C. Hướng L thay đổi nhưng độ lớn không đổi
- D) D. L tăng tỉ lệ với thời gian

**Correct:** B

**Explanation:** Khi τ_ext = 0, định luật dL/dt = τ_ext = 0, nên L = const. Cả độ lớn và hướng đều bảo toàn — nguyên lý hoạt động của gyroscope INS.

**Q3:** Trong gyroscope MEMS, cơ chế nào được dùng để đo angular velocity?
- A) A. Thay đổi điện trở piezoresistive
- B) B. Lực Coriolis F_c = 2mv × ω tác động lên mass dao động
- C) C. Thay đổi từ trường do rotor từ tính
- D) D. Thay đổi tần số dao động của cantilever

**Correct:** B

**Explanation:** MEMS gyro kích thích proof mass dao động theo drive axis. Khi hệ quay, lực Coriolis tạo độ lệch theo sense axis vuông góc, được đo bằng capacitive electrodes để suy ra ω.

**Q4:** Trong thiết kế hệ thống cơ điện tử (đo lường chính xác micrometer hoặc hệ vũ khí), hãy nêu một trường hợp cụ thể mà bản chất vector của angular momentum và torque (không chỉ scalar) là thiết yếu. Giải thích tại sao hướng của các đại lượng này tạo ra sự khác biệt trong kết quả kỹ thuật.

**Correct:** N/A


---
*Exported from Feynman Bot*
