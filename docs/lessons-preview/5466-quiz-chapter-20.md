---
lesson_id: 5466
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:05.716475+00:00"
content_hash: 25b13fa896e7
chapter_number: 20
chapter_title: Chapter 20
section_number: 2
section_title: 20–1Torques in three dimensions
---
# ## Quiz: Moment Động Lượng 3D và Con Quay Hồi Chuyển

*Source: Chapter 20 - Chapter 20 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_20.html)*

## Quiz: Moment Động Lượng 3D và Con Quay Hồi Chuyển

Bài kiểm tra về moment động lượng vector, torque 3D và hiện tượng tuế sai gyroscopic trong ứng dụng kỹ thuật.

---

**Câu 1.** Moment động lượng của một hạt trong không gian 3D được định nghĩa là:

A. $\mathbf{L} = \mathbf{r} \cdot \mathbf{p}$ (tích vô hướng)

B. $\mathbf{L} = \mathbf{r} \times \mathbf{p}$ (tích có hướng)

C. $\mathbf{L} = m(\mathbf{r} + \mathbf{v})$

D. $\mathbf{L} = \nabla \times \mathbf{p}$

**Đáp án: B**
*Giải thích:* $\mathbf{L} = \mathbf{r} \times \mathbf{p} = m(\mathbf{r} \times \mathbf{v})$. Tích có hướng cho vector vuông góc với mặt phẳng chứa $\mathbf{r}$ và $\mathbf{p}$, hướng theo quy tắc bàn tay phải. Thành phần $L_z = xp_y - yp_x$ là kết quả 2D quen thuộc. Trong 3D, $L_x = yp_z - zp_y$ và $L_y = zp_x - xp_z$ xuất hiện thêm.

---

**Câu 2.** Con quay hồi chuyển có moment quán tính $I = 4 \times 10^{-4}\,\text{kg·m}^2$, quay với $\omega = 2000\,\text{rad/s}$. Trọng tâm rotor lệch $r = 2\,\text{cm}$ khỏi điểm tựa, khối lượng $M = 100\,\text{g}$. Vận tốc tuế sai $\Omega_p$ là:

A. $\Omega_p \approx 0.245\,\text{rad/s}$

B. $\Omega_p \approx 2.45\,\text{rad/s}$

C. $\Omega_p \approx 24.5\,\text{rad/s}$

D. $\Omega_p \approx 0.0245\,\text{rad/s}$

**Đáp án: A**
*Giải thích:* $\tau = Mgr = 0.1 \times 9.8 \times 0.02 = 0.0196\,\text{N·m}$. $L = I\omega = 4 \times 10^{-4} \times 2000 = 0.8\,\text{kg·m}^2/\text{s}$. $\Omega_p = \tau/L = 0.0196/0.8 = 0.0245\,\text{rad/s}$. *Lưu ý: đáp án đúng là D!* $\Omega_p \approx 0.0245\,\text{rad/s}$.

*Lưu ý chỉnh lại:* **Đáp án: D**
*Giải thích:* $\Omega_p = \dfrac{Mgr}{I\omega} = \dfrac{0.1 \times 9.8 \times 0.02}{4\times10^{-4} \times 2000} = \dfrac{0.0196}{0.8} = 0.0245\,\text{rad/s}$. Tuế sai nhỏ vì $L = I\omega = 0.8\,\text{kg·m}^2/\text{s}$ lớn — đây là mục tiêu thiết kế: $L$ lớn giúp gyroscope ổn định hơn.

---

**Câu 3.** Phương trình $\boldsymbol{\tau} = d\mathbf{L}/dt$ trong 3D có nghĩa là: torque vuông góc với vector $\mathbf{L}$ sẽ:

A. Làm tăng độ lớn $|\mathbf{L}|$ nhưng không đổi hướng.

B. Làm giảm độ lớn $|\mathbf{L}|$.

C. Làm thay đổi hướng của $\mathbf{L}$ mà không thay đổi độ lớn — dẫn đến hiện tượng tuế sai.

D. Không có tác dụng gì vì vuông góc với $\mathbf{L}$.

**Đáp án: C**
*Giải thích:* Khi $\boldsymbol{\tau} \perp \mathbf{L}$, vector $d\mathbf{L} = \boldsymbol{\tau}\,dt$ vuông góc với $\mathbf{L}$. Giống như lực hướng tâm không đổi tốc độ mà đổi hướng vận tốc trong chuyển động tròn, torque vuông góc không đổi $|\mathbf{L}|$ mà làm trục quay xoay — đó là tuế sai. Đây là nền tảng hoạt động của con quay hồi chuyển và đầu đạn xoắn.

---

**Câu 4 (Tự luận).** Trong thiết kế hệ ổn định quang học (optical stabilizer) cho camera trinh sát trên drone quân sự, hoặc hệ dẫn đường quán tính (INS) cho tên lửa, kỹ sư phải đối mặt với hiện tượng tuế sai gyroscopic và drift. Hãy phân tích: (a) tại sao drift rate thấp là yêu cầu quan trọng, (b) giải pháp kỹ thuật hiện đại nào được dùng để đạt drift rate $< 0.01\,°/\text{hr}$, và (c) vai trò của độ chính xác gia công (cấp micromet) trong việc giảm drift.

*Gợi ý trả lời:*
(a) Drift rate cao tích lũy sai số góc theo thời gian. Sau 1 giờ bay, gyro với drift $1\,°/\text{hr}$ tạo sai lệch vị trí hàng km ở tốc độ Mach 1. Với INS không có GPS backup, drift rate $< 0.01\,°/\text{hr}$ tương đương sai vị trí $< 18\,\text{m/hr}$ — chấp nhận được.
(b) Ring Laser Gyroscope (RLG): drift $\sim 0.001{-}0.01\,°/\text{hr}$, dùng hiệu ứng Sagnac với ánh sáng laser. Fiber Optic Gyroscope (FOG): tương tự nhưng dùng sợi quang dài để tăng độ nhạy. MEMS gyro kết hợp GPS (GPS/INS fusion): Kalman filter hợp nhất tín hiệu, drift hiệu dụng $< 0.001\,°/\text{hr}$.
(c) Drift do lệch tâm rotor: $\Omega_p \propto r$ (khoảng cách lệch tâm). Giảm $r$ từ $0.5\,\text{mm}$ xuống $1\,\mu\text{m}$ giảm drift $500$ lần. Cần gia công cân bằng động (dynamic balancing) ở cấp $< 0.1\,\mu\text{g·m}$ residual unbalance và kiểm soát độ tròn trục (roundness) $< 0.5\,\mu\text{m}$.

```json
{"questions":[{"id":"q1","type":"mcq","question":"Moment động lượng của một hạt trong không gian 3D được định nghĩa là:","options":["A. L = r·p (tích vô hướng)","B. L = r×p (tích có hướng)","C. L = m(r+v)","D. L = ∇×p"],"answer":"B","explanation":"L = r×p = m(r×v). Tích có hướng cho vector vuông góc mặt phẳng (r,p), hướng bàn tay phải. Lz=xpy-ypx là kết quả 2D, Lx=ypz-zpy và Ly=zpx-xpz xuất hiện trong 3D."},{"id":"q2","type":"mcq","question":"Con quay I=4×10⁻⁴ kg·m², ω=2000 rad/s, lệch tâm r=2 cm, M=100 g. Vận tốc tuế sai Ωp?","options":["A. Ωp ≈ 0.245 rad/s","B. Ωp ≈ 2.45 rad/s","C. Ωp ≈ 24.5 rad/s","D. Ωp ≈ 0.0245 rad/s"],"answer":"D","explanation":"τ=Mgr=0.1×9.8×0.02=0.0196 N·m. L=Iω=4×10⁻⁴×2000=0.8 kg·m²/s. Ωp=τ/L=0.0196/0.8=0.0245 rad/s. L lớn nên tuế sai nhỏ — mục tiêu thiết kế gyroscope ổn định."},{"id":"q3","type":"mcq","question":"Torque vuông góc với vector L sẽ:","options":["A. Tăng độ lớn |L| không đổi hướng","B. Giảm độ lớn |L|","C. Thay đổi hướng L không thay đổi độ lớn — gây tuế sai","D. Không có tác dụng"],"answer":"C","explanation":"dL=τ·dt vuông góc với L → |L| không đổi nhưng hướng xoay. Tương tự lực hướng tâm đổi hướng v mà không đổi |v|. Đây là nền tảng của tuế sai gyroscopic và ổn định đầu đạn xoắn."},{"id":"q4","type":"open","question":"Trong thiết kế hệ INS cho tên lửa hoặc camera ổn định trên drone quân sự: (a) tại sao drift rate thấp quan trọng, (b) giải pháp kỹ thuật hiện đại để đạt <0.01°/hr, (c) vai trò độ chính xác gia công cấp micromet trong giảm drift?","sample_answer":"(a) Drift tích lũy sai số góc theo thời gian, 1°/hr → sai vị trí hàng km/hr ở Mach 1. (b) RLG drift ~0.001-0.01°/hr dùng hiệu ứng Sagnac; FOG dùng sợi quang dài; MEMS+GPS với Kalman filter đạt <0.001°/hr. (c) Drift ∝ r (lệch tâm rotor): giảm r từ 0.5mm xuống 1μm giảm drift 500 lần; cần cân bằng động <0.1μg·m và roundness trục <0.5μm."}]}
```


## Quiz Questions

**Q1:** Moment động lượng của một hạt trong không gian 3D được định nghĩa là:
- A) A. L = r·p (tích vô hướng)
- B) B. L = r×p (tích có hướng)
- C) C. L = m(r+v)
- D) D. L = ∇×p

**Correct:** B

**Explanation:** L = r×p = m(r×v). Tích có hướng cho vector vuông góc mặt phẳng (r,p), hướng bàn tay phải. Lz=xpy-ypx là kết quả 2D, Lx=ypz-zpy và Ly=zpx-xpz xuất hiện trong 3D.

**Q2:** Con quay I=4×10⁻⁴ kg·m², ω=2000 rad/s, lệch tâm r=2 cm, M=100 g. Vận tốc tuế sai Ωp?
- A) A. Ωp ≈ 0.245 rad/s
- B) B. Ωp ≈ 2.45 rad/s
- C) C. Ωp ≈ 24.5 rad/s
- D) D. Ωp ≈ 0.0245 rad/s

**Correct:** D

**Explanation:** τ=Mgr=0.1×9.8×0.02=0.0196 N·m. L=Iω=4×10⁻⁴×2000=0.8 kg·m²/s. Ωp=τ/L=0.0196/0.8=0.0245 rad/s. L lớn nên tuế sai nhỏ — mục tiêu thiết kế gyroscope ổn định.

**Q3:** Torque vuông góc với vector L sẽ:
- A) A. Tăng độ lớn |L| không đổi hướng
- B) B. Giảm độ lớn |L|
- C) C. Thay đổi hướng L không thay đổi độ lớn — gây tuế sai
- D) D. Không có tác dụng

**Correct:** C

**Explanation:** dL=τ·dt vuông góc với L → |L| không đổi nhưng hướng xoay. Tương tự lực hướng tâm đổi hướng v mà không đổi |v|. Đây là nền tảng của tuế sai gyroscopic và ổn định đầu đạn xoắn.

**Q4:** Trong thiết kế hệ INS cho tên lửa hoặc camera ổn định trên drone quân sự: (a) tại sao drift rate thấp quan trọng, (b) giải pháp kỹ thuật hiện đại để đạt <0.01°/hr, (c) vai trò độ chính xác gia công cấp micromet trong giảm drift?

**Correct:** N/A


---
*Exported from Feynman Bot*
