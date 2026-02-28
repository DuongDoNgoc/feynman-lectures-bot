---
lesson_id: 5365
lesson_type: concept
approval_status: pending
exported_at: "2026-02-28T14:08:59.746832+00:00"
content_hash: aecbe003085d
chapter_number: 8
chapter_title: Chapter 8
section_number: 4
section_title: 8–3Speed as a derivative
---
# ## Ký Hiệu Vi Tích Phân — Ngôn Ngữ Của Sự Thay Đổi

*Source: Chapter 8 - Chapter 8 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_08.html)*

## Ký Hiệu Vi Tích Phân — Ngôn Ngữ Của Sự Thay Đổi

Khi bạn lập trình bộ điều khiển chuyển động, bạn viết `error_rate = (error - prev_error) / dt`. Đây chính xác là cách toán học mô tả đạo hàm — nhưng với ký hiệu đẹp hơn và ý nghĩa sâu hơn. Vậy $\Delta t$, $dt$, và $\dfrac{d}{dt}$ thực sự nghĩa là gì, và tại sao chúng khác nhau?

---

### Ký hiệu $\Delta$ và $d$: Hai cấp độ của sự thay đổi

Feynman giải thích tại sao toán học cần hai loại ký hiệu khác nhau để nói về "sự thay đổi":

**$\Delta t$** (delta t): Một khoảng thời gian hữu hạn, đo được được — ví dụ $\Delta t = 0.001\,\text{s}$ giữa hai lần đọc encoder. Tỉ số $\Delta s / \Delta t$ cho vận tốc **trung bình** trên khoảng đó.

**$dt$** (d t): Ký hiệu giới hạn — $\Delta t$ khi nó co lại đến vô cùng nhỏ. Tỉ số $ds/dt$ là vận tốc **tức thời**:

$$\frac{ds}{dt} = \lim_{\Delta t \to 0} \frac{\Delta s}{\Delta t}$$

Điểm then chốt: $\Delta$ là sự xấp xỉ hữu hạn; $d$ là giới hạn toán học chính xác. Trong phần mềm nhúng, ta luôn dùng $\Delta$ vì máy tính không xử lý giới hạn liên tục — nhưng khi $\Delta t$ đủ nhỏ so với hằng số thời gian của hệ, xấp xỉ này rất tốt.

---

### Tại sao $\Delta s/\Delta t \neq s/t$?

Feynman cảnh báo một nhầm lẫn phổ biến: $\Delta s/\Delta t$ là tỉ lệ của **sự thay đổi**, không phải tỉ lệ của **giá trị tuyệt đối**. Cũng như $\sin\theta / \sin 2\theta \neq 1/2$ (vì $\sin$ không tuyến tính), $\Delta s/\Delta t$ phụ thuộc vào vị trí trên đường cong $s(t)$.

---

### Phép so sánh: Bộ khuếch đại vi sai trong mạch đo

Trong mạch đo lường chính xác, **bộ khuếch đại vi sai** đo hiệu điện áp $\Delta V = V_+ - V_-$ — không phải $V_+$ hay $V_-$ riêng lẻ. Đây là $\Delta$-tư duy: ta quan tâm đến **sự thay đổi** giữa hai điểm, không phải giá trị tuyệt đối.

Tương tự, đạo hàm $ds/dt$ là "bộ khuếch đại vi sai theo thời gian" — nó đo sự khác biệt vô cùng nhỏ của $s$ tại hai thời điểm kề nhau, rồi chia cho khoảng thời gian đó.

---

### Quy tắc vi phân thực tế

Một số công thức hay dùng:

- $\dfrac{d}{dt}(t^n) = nt^{n-1}$ (quy tắc lũy thừa)
- $\dfrac{d}{dt}(\sin\omega t) = \omega\cos\omega t$
- $\dfrac{d}{dt}(e^{\alpha t}) = \alpha e^{\alpha t}$

Những công thức này không phải "ma thuật" — chúng đều xuất phát từ định nghĩa giới hạn $\lim_{\Delta t \to 0} \Delta s/\Delta t$.

---

**Điểm mấu chốt:**

- $\Delta t$ = khoảng hữu hạn; $dt$ = giới hạn vô cùng nhỏ.
- Đạo hàm $ds/dt$ = giới hạn của tỉ số $\Delta s / \Delta t$ khi $\Delta t \to 0$.
- $\Delta s/\Delta t \neq s/t$ — đây là tỉ lệ **thay đổi**, không phải tỉ lệ **giá trị**.
- Trong phần mềm nhúng, $\Delta t$ hữu hạn nhỏ xấp xỉ $dt$ — độ chính xác phụ thuộc vào tần số lấy mẫu so với băng thông của tín hiệu.


---
*Exported from Feynman Bot*
