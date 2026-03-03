---
lesson_id: 5454
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:05.419640+00:00"
content_hash: c0b1c3d0dd79
chapter_number: 18
chapter_title: Chapter 18
section_number: 4
section_title: 18–3Angular momentum
---
# ## Quiz: Moment Động Lượng và Bảo Toàn

*Source: Chapter 18 - Chapter 18 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_18.html)*

## Quiz: Moment Động Lượng và Bảo Toàn

### Câu 1 (Trắc nghiệm)

Một vệ tinh sử dụng reaction wheel để điều chỉnh hướng. Vệ tinh có $I_{\text{sat}} = 80$ kg·m² và reaction wheel có $I_{\text{wheel}} = 0.4$ kg·m². Nếu wheel tăng tốc từ 0 lên $\omega_{\text{wheel}} = 500$ rad/s, vệ tinh quay với $\omega_{\text{sat}}$ bằng bao nhiêu?

A. $\omega_{\text{sat}} = 2.5$ rad/s (cùng chiều wheel)
B. $\omega_{\text{sat}} = 2.5$ rad/s (ngược chiều wheel)
C. $\omega_{\text{sat}} = 0.0025$ rad/s (ngược chiều wheel)
D. $\omega_{\text{sat}} = 200$ rad/s (cùng chiều wheel)

**Đáp án: B**

*Giải thích:* Bảo toàn angular momentum: $L_{\text{total}} = 0$ ban đầu, nên $I_{\text{sat}}\omega_{\text{sat}} + I_{\text{wheel}}\omega_{\text{wheel}} = 0$. Suy ra $\omega_{\text{sat}} = -I_{\text{wheel}}\omega_{\text{wheel}}/I_{\text{sat}} = -(0.4 \times 500)/80 = -2.5$ rad/s. Dấu âm nghĩa là ngược chiều wheel. Đây là nguyên lý momentum wheel trong attitude control.

---

### Câu 2 (Trắc nghiệm)

Phương trình $\tau = dL/dt$ (mô-men xoắn bằng tốc độ thay đổi angular momentum) là:

A. Định nghĩa của mô-men xoắn
B. Hệ quả chứng minh được từ Newton's second law $F = ma$
C. Một tiên đề độc lập của cơ học quay
D. Chỉ đúng cho vật rắn, không đúng cho hệ hạt

**Đáp án: B**

*Giải thích:* Feynman chứng minh trực tiếp: thay $F_x = m\ddot{x}$, $F_y = m\ddot{y}$ vào $\tau = xF_y - yF_x$, ta được $\tau = m(x\ddot{y} - y\ddot{x}) = d/dt[m(x\dot{y} - y\dot{x})] = dL/dt$. Đây là hệ quả của Newton's laws, không phải định nghĩa mới. Nó đúng cho cả hệ hạt (nội lực triệt tiêu do Newton 3).

---

### Câu 3 (Trắc nghiệm)

Gyroscope trong hệ INS của tên lửa có $I = 0.01$ kg·m² và quay ở $\omega = 20.000$ RPM. Tốc độ tiến động (precession) khi chịu mô-men xoắn nhiễu $\tau = 0.001$ N·m là:

A. $\Omega_{\text{prec}} = 0.477 \times 10^{-3}$ rad/s
B. $\Omega_{\text{prec}} = 0.1$ rad/s
C. $\Omega_{\text{prec}} = 2.09$ rad/s
D. $\Omega_{\text{prec}} = 10$ rad/s

**Đáp án: A**

*Giải thích:* $\omega = 20000 \times 2\pi/60 = 2094$ rad/s. $L = I\omega = 0.01 \times 2094 = 20.94$ kg·m²/s. $\Omega_{\text{prec}} = \tau/L = 0.001/20.94 = 4.77\times10^{-5}$ rad/s $\approx 0.477 \times 10^{-3}$ rad/s. Gyroscope quay nhanh có precession rất chậm — vì vậy cần tốc độ cao để hệ INS chính xác.

---

### Câu 4 (Tự luận)

Trong thiết kế hệ thống attitude control cho UAV trinh sát sử dụng momentum wheel, angular momentum tổng hệ phải bảo toàn khi không có mô-men xoắn ngoại tác. Tuy nhiên, trên thực tế UAV hoạt động trong khí quyển nên có aerodynamic torque. Giải thích cơ chế bảo toàn angular momentum bị "phá vỡ" như thế nào, và đề xuất chiến lược điều khiển để bù lại nhiễu này cho hệ thống định hướng cảm biến chụp ảnh độ phân giải cao.

**Gợi ý trả lời:**

Khi có aerodynamic torque $\tau_{\text{aero}}$: $dL_{\text{total}}/dt = \tau_{\text{aero}} \neq 0$. Angular momentum không bảo toàn nữa.

Chiến lược bù:
1. **Feedforward:** Ước lượng $\tau_{\text{aero}}$ từ mô hình khí động học + đo gió, điều khiển momentum wheel để sinh ra $\tau_{\text{wheel}} = -\tau_{\text{aero}}$ bù trừ.
2. **Feedback:** Đo $\omega_{\text{UAV}}$ bằng IMU (inertial measurement unit), tính $L_{\text{error}} = I_{\text{UAV}}\omega_{\text{UAV}} - L_{\text{ref}}$, điều chỉnh $\omega_{\text{wheel}}$ để giảm $L_{\text{error}}$.
3. **Momentum dumping:** Định kỳ dùng thruster nhỏ để reset $L_{\text{wheel}}$ về giá trị nominal (tránh wheel bão hòa).

Với camera chụp ảnh độ phân giải cao (GSD < 10 cm ở độ cao 500 m), sai số góc cho phép < 0.1 mrad — yêu cầu kiểm soát $L_{\text{total}}$ với độ chính xác tương ứng.

```json
{"questions":[{"id":"q1","type":"mcq","question":"Vệ tinh $I_{sat}=80$ kg·m², reaction wheel $I_{wheel}=0.4$ kg·m². Wheel tăng từ 0 lên 500 rad/s, vệ tinh quay thế nào?","options":["A. 2.5 rad/s cùng chiều wheel","B. 2.5 rad/s ngược chiều wheel","C. 0.0025 rad/s ngược chiều wheel","D. 200 rad/s cùng chiều wheel"],"answer":"B","explanation":"Bảo toàn angular momentum: $I_{sat}\\omega_{sat} = -I_{wheel}\\omega_{wheel}$, suy ra $\\omega_{sat} = -(0.4\\times500)/80 = -2.5$ rad/s. Dấu âm = ngược chiều wheel."},{"id":"q2","type":"mcq","question":"Phương trình $\\tau = dL/dt$ là:","options":["A. Định nghĩa của mô-men xoắn","B. Hệ quả chứng minh được từ Newton second law F=ma","C. Tiên đề độc lập của cơ học quay","D. Chỉ đúng cho vật rắn"],"answer":"B","explanation":"Thay $F_x=m\\ddot{x}$, $F_y=m\\ddot{y}$ vào $\\tau=xF_y-yF_x$, được $\\tau=d/dt[m(x\\dot{y}-y\\dot{x})]=dL/dt$. Đây là hệ quả tất yếu của Newton's laws."},{"id":"q3","type":"mcq","question":"Gyroscope $I=0.01$ kg·m², $\\omega=20000$ RPM, chịu nhiễu $\\tau=0.001$ N·m. Tốc độ precession?","options":["A. 4.77×10⁻⁵ rad/s","B. 0.1 rad/s","C. 2.09 rad/s","D. 10 rad/s"],"answer":"A","explanation":"$L=I\\omega=0.01\\times2094=20.94$ kg·m²/s. $\\Omega_{prec}=\\tau/L=0.001/20.94=4.77\\times10^{-5}$ rad/s. Quay nhanh → precession chậm → INS chính xác hơn."},{"id":"q4","type":"open","question":"Trong UAV sử dụng momentum wheel để ổn định hướng camera, tại sao bảo toàn angular momentum bị phá vỡ trong khí quyển và cần chiến lược điều khiển gì để bù lại?","sample_answer":"Aerodynamic torque $\\tau_{aero}$ làm $dL_{total}/dt\\neq 0$. Chiến lược: (1) Feedforward ước lượng $\\tau_{aero}$ từ mô hình khí động + cảm biến gió, điều khiển wheel bù trừ; (2) Feedback từ IMU đo $\\omega_{UAV}$, điều chỉnh wheel giảm sai số; (3) Momentum dumping định kỳ dùng thruster để tránh wheel bão hòa. Yêu cầu sai số góc < 0.1 mrad cho camera phân giải cao."}]}
```


## Quiz Questions

**Q1:** Vệ tinh $I_{sat}=80$ kg·m², reaction wheel $I_{wheel}=0.4$ kg·m². Wheel tăng từ 0 lên 500 rad/s, vệ tinh quay thế nào?
- A) A. 2.5 rad/s cùng chiều wheel
- B) B. 2.5 rad/s ngược chiều wheel
- C) C. 0.0025 rad/s ngược chiều wheel
- D) D. 200 rad/s cùng chiều wheel

**Correct:** B

**Explanation:** Bảo toàn angular momentum: $I_{sat}\omega_{sat} = -I_{wheel}\omega_{wheel}$, suy ra $\omega_{sat} = -(0.4\times500)/80 = -2.5$ rad/s. Dấu âm = ngược chiều wheel.

**Q2:** Phương trình $\tau = dL/dt$ là:
- A) A. Định nghĩa của mô-men xoắn
- B) B. Hệ quả chứng minh được từ Newton second law F=ma
- C) C. Tiên đề độc lập của cơ học quay
- D) D. Chỉ đúng cho vật rắn

**Correct:** B

**Explanation:** Thay $F_x=m\ddot{x}$, $F_y=m\ddot{y}$ vào $\tau=xF_y-yF_x$, được $\tau=d/dt[m(x\dot{y}-y\dot{x})]=dL/dt$. Đây là hệ quả tất yếu của Newton's laws.

**Q3:** Gyroscope $I=0.01$ kg·m², $\omega=20000$ RPM, chịu nhiễu $\tau=0.001$ N·m. Tốc độ precession?
- A) A. 4.77×10⁻⁵ rad/s
- B) B. 0.1 rad/s
- C) C. 2.09 rad/s
- D) D. 10 rad/s

**Correct:** A

**Explanation:** $L=I\omega=0.01\times2094=20.94$ kg·m²/s. $\Omega_{prec}=\tau/L=0.001/20.94=4.77\times10^{-5}$ rad/s. Quay nhanh → precession chậm → INS chính xác hơn.

**Q4:** Trong UAV sử dụng momentum wheel để ổn định hướng camera, tại sao bảo toàn angular momentum bị phá vỡ trong khí quyển và cần chiến lược điều khiển gì để bù lại?

**Correct:** N/A


---
*Exported from Feynman Bot*
