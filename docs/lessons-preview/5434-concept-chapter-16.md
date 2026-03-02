---
lesson_id: 5434
lesson_type: concept
approval_status: approved
exported_at: "2026-03-02T15:10:29.329354+00:00"
content_hash: 7343a71a0918
chapter_number: 16
chapter_title: Chapter 16
section_number: 4
section_title: 16–3Transformation of velocities
---
# ## Phép Biến Đổi Lorentz và Cộng Vận Tốc Tương Đối Tính

*Source: Chapter 16 - Chapter 16 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_16.html)*

## Phép Biến Đổi Lorentz và Cộng Vận Tốc Tương Đối Tính

### Đặt vấn đề

Tên lửa A bay với vận tốc 100,000 dặm/giây. Bên trong tên lửa, một vật thể nhỏ phóng với vận tốc 100,000 dặm/giây so với tên lửa. Theo vật lý thông thường (Newton/Galileo), vật thể đó chuyển động với 200,000 dặm/giây so với mặt đất — nhưng tốc độ ánh sáng chỉ là 186,000 dặm/giây! Điều gì đang xảy ra? Câu trả lời nằm trong phép biến đổi Lorentz.

### Phép biến đổi Lorentz — Dạng chuẩn

Phép biến đổi Lorentz (cho chuyển động dọc theo trục $x$) là:

$$x' = rac{x-ut}{\sqrt{1-u^2/c^2}}, \quad y'=y, \quad z'=z, \quad t' = rac{t-ux/c^2}{\sqrt{1-u^2/c^2}}$$

Và chiều ngược lại (từ hệ chuyển động nhìn về hệ đứng yên):

$$x = rac{x'+ut'}{\sqrt{1-u^2/c^2}}, \quad y=y', \quad z=z', \quad t = rac{t'+ux'/c^2}{\sqrt{1-u^2/c^2}}$$

Lưu ý tính đối xứng đẹp: chiều ngược lại có cùng dạng công thức, chỉ đổi dấu $u$. Điều này hoàn toàn hợp lý vì nếu Moe nói anh ta "đứng yên" và Joe "chuyển động", anh ta chỉ cần đổi dấu vận tốc tương đối. Nếu điều này không đúng, nguyên lý tương đối bị vi phạm.

### Phép so sánh với kỹ sư robot và hệ tọa độ

Trong robotics, khi bạn chuyển đổi tọa độ điểm từ frame của cánh tay robot sang frame của base, bạn dùng ma trận biến đổi thuần nhất (homogeneous transformation matrix):

$$egin{pmatrix} x_{base} \ 1 \end{pmatrix} = egin{pmatrix} R & t \ 0 & 1 \end{pmatrix} egin{pmatrix} x_{arm} \ 1 \end{pmatrix}$$

Phép biến đổi Lorentz là phép biến đổi tọa độ trong không-thời gian 4 chiều (4D spacetime). Thay vì chỉ mix không gian, Lorentz mix cả không gian và thời gian với nhau. Đây là "ma trận biến đổi" của không-thời gian tương đối tính.

### Quy tắc cộng vận tốc tương đối tính

Giả sử vật thể trong tàu vũ trụ chuyển động với vận tốc $v_{x'}$ theo người trong tàu, và tàu chuyển động với vận tốc $u$ so với mặt đất. Theo người trên mặt đất, vận tốc của vật thể là bao nhiêu?

Trong tàu: $x' = v_{x'} t'$

Thay vào phép biến đổi ngược $x = (x'+ut')/\sqrt{1-u^2/c^2}$ và $t = (t'+ux'/c^2)/\sqrt{1-u^2/c^2}$:

$$v_x = rac{x}{t} = rac{v_{x'} + u}{1 + v_{x'} u/c^2}$$

Đây là **quy tắc cộng vận tốc tương đối tính**. Hãy kiểm tra:
- Nếu $v_{x'} \ll c$ và $u \ll c$: $v_x pprox v_{x'} + u$ — khớp với Newton
- Nếu $v_{x'} = c$ (ánh sáng): $v_x = (c+u)/(1+u/c) = c(c+u)/(c+u) = c$ — ánh sáng luôn đi với $c$ mọi hệ!
- Nếu $v_{x'} = 100{,}000$ dặm/s và $u = 100{,}000$ dặm/s: $v_x = 200{,}000/(1 + 10^{10}/c^2)$ — không bao giờ đạt $2c$!

### Điểm mấu chốt

- Phép biến đổi Lorentz là "từ điển dịch ngôn ngữ" giữa hai hệ quy chiếu quán tính, trộn lẫn không gian và thời gian — giống ma trận biến đổi trong robotics nhưng trong 4D spacetime.
- Chiều ngược lại của biến đổi Lorentz có cùng dạng, chỉ đổi dấu $u$ — phản ánh tính đối xứng của nguyên lý tương đối.
- Quy tắc cộng vận tốc $v_x = (v_{x'}+u)/(1+v_{x'}u/c^2)$ đảm bảo không bao giờ vượt tốc độ ánh sáng, và ánh sáng luôn có vận tốc $c$ trong mọi hệ.

---
*Exported from Feynman Bot*
