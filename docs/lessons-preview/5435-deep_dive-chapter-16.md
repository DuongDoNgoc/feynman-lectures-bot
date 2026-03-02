---
lesson_id: 5435
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-02T15:10:29.353547+00:00"
content_hash: 9e6834487396
chapter_number: 16
chapter_title: Chapter 16
section_number: 4
section_title: 16–3Transformation of velocities
---
# ## Phép Biến Đổi Lorentz Đảo Nghịch và Cộng Vận Tốc Tương Đối Tính — Phân tích C

*Source: Chapter 16 - Chapter 16 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_16.html)*

## Phép Biến Đổi Lorentz Đảo Nghịch và Cộng Vận Tốc Tương Đối Tính — Phân tích Chuyên sâu

### 1. Cấu trúc đầy đủ của phép biến đổi Lorentz

**Chiều thuận** (từ hệ $S$ sang $S'$ — Joe sang Moe):
$$x' = rac{x-ut}{\sqrt{1-u^2/c^2}}, \quad y'=y, \quad z'=z, \quad t' = rac{t-ux/c^2}{\sqrt{1-u^2/c^2}}$$

**Chiều đảo** (từ hệ $S'$ sang $S$ — Moe sang Joe):
$$x = rac{x'+ut'}{\sqrt{1-u^2/c^2}}, \quad y=y', \quad z=z', \quad t = rac{t'+ux'/c^2}{\sqrt{1-u^2/c^2}}$$

**Quan sát quan trọng**: Chiều đảo có cùng cấu trúc toán học với chiều thuận, chỉ thay $u 	o -u$. Đây không phải ngẫu nhiên — đây là hệ quả bắt buộc của nguyên lý tương đối: nếu Moe muốn mô tả Joe bằng phép biến đổi của mình, anh ta chỉ việc nói "Joe chuyển động với vận tốc $-u$ so với tôi", và thu được cùng dạng công thức.

**Kiểm tra tính nhất quán**: Thay chiều đảo vào chiều thuận, ta phải thu về $x' = x', t' = t'$ (tức là $f^{-1}(f(x)) = x$). Việc đại số xác nhận điều này là bài kiểm tra tính tự nhất quán của phép biến đổi.

### 2. Phép biến đổi Lorentz dưới dạng ma trận (4×4)

Đặt $eta = u/c$, $\gamma = 1/\sqrt{1-eta^2}$, và dùng tọa độ $(ct, x, y, z)$. Phép biến đổi Lorentz viết dưới dạng ma trận:

$$egin{pmatrix} ct' \ x' \ y' \ z' \end{pmatrix} = egin{pmatrix} \gamma & -\gammaeta & 0 & 0 \ -\gammaeta & \gamma & 0 & 0 \ 0 & 0 & 1 & 0 \ 0 & 0 & 0 & 1 \end{pmatrix} egin{pmatrix} ct \ x \ y \ z \end{pmatrix}$$

*Ý nghĩa kỹ thuật*: Đây là ma trận $4	imes4$ hoạt động trong không-thời gian Minkowski. Tương tự như ma trận biến đổi thuần nhất (homogeneous transformation) trong robotics hoạt động trong không gian 3D. Nhưng "góc quay" ở đây là góc hyperbolic (rapidity $\phi = 	anh^{-1}(eta)$) thay vì góc thông thường.

### 3. Suy dẫn quy tắc cộng vận tốc

**Bài toán**: Vật thể trong tàu vũ trụ (hệ $S'$) chuyển động với vận tốc $v_{x'}$ theo người trong tàu. Tàu chuyển động với vận tốc $u$ so với mặt đất (hệ $S$). Tính vận tốc $v_x$ của vật thể theo người trên mặt đất.

**Bước 1**: Viết quan hệ trong hệ $S'$:
$$x' = v_{x'} t'$$
(vật thể di chuyển $v_{x'}$ mét mỗi giây theo Moe)

**Bước 2**: Dùng phép biến đổi Lorentz đảo để tìm $x$ và $t$ theo $x', t'$:
$$x = rac{x' + ut'}{\sqrt{1-u^2/c^2}} = rac{v_{x'}t' + ut'}{\sqrt{1-u^2/c^2}} = rac{(v_{x'} + u)t'}{\sqrt{1-u^2/c^2}}$$
$$t = rac{t' + ux'/c^2}{\sqrt{1-u^2/c^2}} = rac{t' + u(v_{x'}t')/c^2}{\sqrt{1-u^2/c^2}} = rac{t'(1 + v_{x'}u/c^2)}{\sqrt{1-u^2/c^2}}$$

**Bước 3**: Tính vận tốc theo Joe:
$$v_x = rac{x}{t} = rac{(v_{x'} + u)t'/\sqrt{1-u^2/c^2}}{t'(1 + v_{x'}u/c^2)/\sqrt{1-u^2/c^2}} = rac{v_{x'} + u}{1 + v_{x'}u/c^2}$$

$$oxed{v_x = rac{v_{x'} + u}{1 + v_{x'} u/c^2}}$$

*Ý nghĩa vật lý bước 3*: Tử số là "cộng vận tốc thông thường". Mẫu số $1 + v_{x'}u/c^2$ là "hệ số giảm tốc" do tương đối tính — luôn lớn hơn 1 (với $v_{x'}, u > 0$), nên $v_x < v_{x'} + u$.

**Kiểm tra các trường hợp giới hạn**:

*Giới hạn Newton* ($v_{x'}, u \ll c$): $1 + v_{x'}u/c^2 pprox 1$ → $v_x pprox v_{x'} + u$ (cộng vận tốc Galileo)

*Trường hợp ánh sáng* ($v_{x'} = c$):
$$v_x = rac{c + u}{1 + cu/c^2} = rac{c + u}{1 + u/c} = rac{c(c + u)}{c + u} = c$$

Ánh sáng luôn đi với vận tốc $c$ trong mọi hệ quy chiếu — chính xác như yêu cầu!

### 4. Ví dụ thực tế: Bù vận tốc trong hệ đo lường laser Doppler

**Laser Doppler Vibrometer (LDV)** là thiết bị đo rung động bề mặt bằng cách phân tích tần số Doppler của ánh sáng phản xạ. Trong đo lường chính xác cơ học, bạn gắn đầu đo LDV lên một robot di chuyển để quét bề mặt chi tiết đang rung.

**Vấn đề**: Đầu đo di chuyển với vận tốc $v_{robot}$ theo hướng đo. Bề mặt chi tiết rung với vận tốc $v_{surface}$ (cần đo). Tín hiệu Doppler bạn thu được phản ánh vận tốc tổng hợp của cả hai.

**Bù vận tốc Galileo (thông thường)**:
$$v_{measured} = v_{surface} + v_{robot}$$
$$\Rightarrow v_{surface} = v_{measured} - v_{robot}$$

Đây là phép tính đơn giản dùng trong thực tế (với robot công nghiệp).

**Nếu đầu đo di chuyển rất nhanh** (ví dụ: đầu đo gắn trên tên lửa, đo rung động cánh tên lửa ở $u = 0.01c = 3000$ km/s):

Cần dùng quy tắc cộng vận tốc tương đối:
$$v_x = rac{v_{surface} + v_{robot}}{1 + v_{surface} \cdot v_{robot}/c^2}$$

Với $v_{robot} = 0.01c$ và $v_{surface} = 100$ m/s:
$$	ext{Hiệu chỉnh} = 1 + rac{100 	imes 3	imes10^6}{(3	imes10^8)^2} = 1 + 3.33	imes10^{-9} pprox 1$$

Ở vận tốc này hiệu chỉnh là $3 	imes 10^{-9}$ — hoàn toàn không đáng kể. Nhưng ở $v_{robot} = 0.9c$, hiệu chỉnh là ~50% — rất quan trọng (như trong máy gia tốc hạt).

### 5. Bài tập mẫu có lời giải

**Bài toán**: Hai tàu vũ trụ A và B đang bay ngược chiều nhau. Người quan sát trên mặt đất thấy A đi với $v_A = 0.8c$ và B đi với $v_B = 0.7c$ (theo chiều ngược lại, tức $-0.7c$). Theo người trên tàu A, tàu B đang tiến lại với vận tốc bao nhiêu?

**Lời giải từng bước**:

*Bước 1*: Xác định bài toán. Từ góc nhìn của mặt đất (hệ $S$): $v_A = +0.8c$, $v_B = -0.7c$ (chiều âm). Từ góc nhìn của tàu A (hệ $S'$, chuyển động $u = +0.8c$ so với mặt đất), tàu B có vận tốc $v_{B,A}$ là bao nhiêu?

*Bước 2*: Dùng quy tắc cộng vận tốc với $v_{x} = v_B = -0.7c$ (vận tốc B theo mặt đất) và $u = 0.8c$ (vận tốc của hệ A theo mặt đất):

$$v_{B,A} = v_{x'} = rac{v_x - u}{1 - v_x u/c^2} = rac{-0.7c - 0.8c}{1 - (-0.7c)(0.8c)/c^2}$$

$$= rac{-1.5c}{1 + 0.56} = rac{-1.5c}{1.56} = -0.962c$$

*Bước 3*: Kiểm tra ý nghĩa. Theo người A, B tiến lại với vận tốc $0.962c$ — nhanh hơn $0.7c$ theo Newton nhưng vẫn nhỏ hơn $c$!

Theo vật lý Newton cổ điển: $v_{B,A} = 0.7c + 0.8c = 1.5c$ — vượt tốc độ ánh sáng!

Theo tương đối tính: $v_{B,A} = 0.962c$ — luôn nhỏ hơn $c$.

*Bước 4*: Ứng dụng thực tế. Quy tắc này quan trọng trong thiết kế radar và hệ thống dẫn đường: khi tính tốc độ tiếp cận giữa hai vật thể bay nhanh, cần dùng quy tắc cộng vận tốc tương đối tính để có kết quả chính xác. Với vật thể bay Mach 5 (~ $1700$ m/s $pprox 5.7	imes10^{-6}c$), hiệu chỉnh là $\sim 3	imes10^{-11}$ — không đáng kể. Nhưng với hạt trong máy gia tốc, hiệu chỉnh là quan trọng sống còn.

### 6. Tổng kết

Phép biến đổi Lorentz và quy tắc cộng vận tốc tương đối tính:
1. **Có tính đối xứng hoàn hảo**: chiều đảo có cùng dạng, chỉ đổi dấu $u$
2. **Quy về Newton ở vận tốc thấp**: đảm bảo nhất quán với thực nghiệm cũ
3. **Bảo toàn bất biến $c$**: ánh sáng luôn đi với $c$ trong mọi hệ
4. **Ứng dụng kỹ thuật**: quan trọng trong GPS, radar, máy gia tốc hạt và mọi hệ đo lường điện từ học

---
*Exported from Feynman Bot*
