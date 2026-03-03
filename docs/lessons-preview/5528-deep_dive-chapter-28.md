---
lesson_id: 5528
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:07.209694+00:00"
content_hash: fbff0bf25c2f
chapter_number: 28
chapter_title: Chapter 28
section_number: 3
section_title: 28–2Radiation
---
# ## Phân Tích Sâu: Định Luật Bức Xạ Feynman và Trường Điện Từ của Điện Tích Chuyể

*Source: Chapter 28 - Chapter 28 (Section 3) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_28.html)*

## Phân Tích Sâu: Định Luật Bức Xạ Feynman và Trường Điện Từ của Điện Tích Chuyển Động

### Bức tranh toàn cảnh: Ba thành phần của trường điện

Khi phân tích điện trường sinh ra bởi một điện tích chuyển động, phương trình tổng quát (phương trình Liénard-Wiechert) có ba thành phần riêng biệt:

1. **Thành phần Coulomb** (trường tĩnh): giảm theo $1/r^2$, tồn tại ngay cả khi điện tích đứng yên
2. **Thành phần hiệu chỉnh vận tốc** (velocity field): cũng giảm theo $1/r^2$, là hiệu chỉnh do trễ lan truyền
3. **Thành phần bức xạ** (radiation field / acceleration field): giảm theo $1/r$, chỉ xuất hiện khi điện tích có gia tốc

Feynman chỉ ra rằng ở khoảng cách lớn, chỉ thành phần thứ ba là quan trọng. Hai thành phần đầu giảm theo $1/r^2$ nên ở khoảng cách đủ xa chúng nhỏ hơn rất nhiều so với thành phần $1/r$. Đây là **định luật bức xạ Feynman**:

$$\mathbf{E}(t) = \frac{-q}{4\pi\varepsilon_0 c^2 r} \frac{d^2\hat{e}_{r'}}{dt^2}$$

Trong đó:
- $q$: điện tích nguồn
- $r$: khoảng cách từ điện tích đến điểm quan sát
- $\hat{e}_{r'}$: vector đơn vị từ điểm quan sát đến vị trí *trễ* của điện tích
- $c$: tốc độ ánh sáng
- $\varepsilon_0$: hằng số điện môi chân không

### Suy luận vật lý: Tại sao lại là gia tốc của vector đơn vị?

Hãy hiểu rõ cơ chế vật lý. Giả sử điện tích nằm ở điểm $O$ và điểm quan sát $P$ cách $O$ một khoảng $r$. Ta chiếu vị trí của điện tích lên mặt cầu đơn vị tâm $P$ — điểm chiếu này là $\hat{e}_{r'}$ (gọi là "bóng" của điện tích).

Khi điện tích đứng yên: bóng đứng yên, không có gia tốc, không có bức xạ.

Khi điện tích chuyển động đều: bóng di chuyển đều trên mặt cầu, không có gia tốc góc, không có bức xạ. (Thực ra điều này chỉ đúng gần đúng cho vận tốc thấp, nhưng cho mục đích giải thích thì hợp lý.)

Khi điện tích *tăng tốc*: bóng có gia tốc — đây chính là nguồn gốc của bức xạ. Trường điện tại $P$ tỉ lệ trực tiếp với gia tốc của bóng đó.

### Thời gian trễ và quan hệ nhân quả

Một khái niệm cực kỳ quan trọng: **thời gian trễ** (retarded time). Trường điện mà ta quan sát tại điểm $P$ vào thời điểm $t$ phụ thuộc vào trạng thái của điện tích vào thời điểm $t' = t - r/c$. Nghĩa là thông tin về gia tốc của điện tích phải mất thời gian $r/c$ để truyền đến $P$.

Đây không phải là chi tiết kỹ thuật nhỏ — đây là biểu hiện của nguyên lý nhân quả: không có thông tin nào truyền nhanh hơn ánh sáng. Công thức viết đầy đủ:

$$\mathbf{E}(\mathbf{r}, t) = \frac{-q}{4\pi\varepsilon_0 c^2 r} \left.\frac{d^2\hat{e}_{r'}}{dt'^2}\right|_{t' = t - r/c}$$

### Hình học bức xạ: Phụ thuộc góc

Khi điện tích dao động theo trục $z$ với gia tốc $a(t)$, trường bức xạ tại góc $\theta$ so với trục $z$ là:

$$E(r, t) = \frac{-q \, a(t - r/c) \sin\theta}{4\pi\varepsilon_0 c^2 r}$$

Hãy phân tích hình học này:
- Tại $\theta = 0$ hoặc $\theta = 180°$ (dọc theo trục dao động): $\sin\theta = 0$, không có bức xạ
- Tại $\theta = 90°$ (vuông góc với trục dao động): $\sin\theta = 1$, bức xạ cực đại

Cường độ bức xạ (energy flux) tỉ lệ với $E^2$, nên:
$$I \propto \sin^2\theta$$

Đây là **đặc trưng bức xạ của dipole**. Hình dạng của nó như hai quả bóng nằm hai bên trục dao động — đây là lý do anten dipole bức xạ mạnh nhất theo phương vuông góc với thân anten.

### Ví dụ thực tế: Anten radar điều hướng pha

Trong radar quân sự hiện đại (như hệ thống AESA - Active Electronically Scanned Array), người ta sử dụng hàng nghìn phần tử anten nhỏ, mỗi phần tử là một dipole radiator. Bằng cách điều khiển pha của tín hiệu cấp vào từng phần tử, ta có thể điều hướng chùm sóng mà không cần quay anten cơ học.

Hãy xét trường hợp đơn giản: hai anten dipole cách nhau khoảng cách $d$, cùng tần số $\omega$, nhưng có độ lệch pha $\delta$ được điều khiển. Trường tổng hợp theo góc $\theta$ (tính từ pháp tuyến):

Contribution từ anten 1: $E_1 \propto e^{i\omega t}$
Contribution từ anten 2: $E_2 \propto e^{i(\omega t + \delta + kd\sin\theta)}$

Trong đó $k = 2\pi/\lambda$ và $kd\sin\theta$ là độ lệch pha do sai khác đường đi. Khi ta muốn chùm tia chỉ về hướng $\theta_0$, ta đặt:
$$\delta = -kd\sin\theta_0$$

Sao cho tại $\theta = \theta_0$, hai đóng góp cộng pha nhau (constructive interference). Đây chính là nguyên lý phased array, ứng dụng trực tiếp định luật bức xạ Feynman.

### Năng lượng bức xạ: Công thức Larmor

Công suất tổng do điện tích bức xạ có thể tính bằng cách tích phân $E^2$ trên toàn bộ mặt cầu:

$$P = \frac{q^2 a^2}{6\pi\varepsilon_0 c^3}$$

Đây là **công thức Larmor** — một trong những kết quả quan trọng nhất của điện động học cổ điển. Chú ý:
- Công suất tỉ lệ với $a^2$ (gia tốc bình phương)
- Công suất tỉ lệ với $q^2$ (điện tích bình phương)
- Công suất tỉ lệ nghịch với $c^3$ — ở vũ trụ có tốc độ ánh sáng lớn hơn, bức xạ sẽ yếu hơn nhiều

Công thức Larmor giải thích tại sao electron trong nguyên tử không thể ổn định theo mô hình cổ điển: nếu electron quay quanh hạt nhân, nó liên tục tăng tốc hướng tâm, sẽ liên tục bức xạ năng lượng và nhanh chóng rơi vào hạt nhân trong vài nano giây. Paradox này đòi hỏi phải có cơ học lượng tử.

### Ứng dụng trong đo lường chính xác

Trong hệ thống đo lường laser interferometry (ví dụ: hệ thống đo vị trí chính xác micro-mét), ta sử dụng photon — lượng tử của trường điện từ. Nhưng ở cấp độ cổ điển, laser hoạt động nhờ dipole oscillation của electron trong môi trường laser bị kích thích, và mỗi electron oscillating phát ra một photon. Định luật bức xạ Feynman là nền tảng để hiểu tại sao laser phát ra ánh sáng kết hợp (coherent) và định hướng tốt.

### Tóm tắt các điểm then chốt

1. **Chỉ có gia tốc mới tạo ra bức xạ** — thành phần $1/r$ của trường điện chỉ xuất hiện khi điện tích tăng tốc
2. **Thời gian trễ** $t' = t - r/c$ phản ánh nguyên lý nhân quả — không gì nhanh hơn ánh sáng
3. **Phụ thuộc góc** $\sin^2\theta$ — bức xạ mạnh nhất vuông góc với trục dao động, triệt tiêu dọc theo trục
4. **Công thức Larmor** $P = q^2 a^2 / (6\pi\varepsilon_0 c^3)$ — công suất bức xạ tỉ lệ với bình phương gia tốc
5. **Ứng dụng kỹ thuật**: phased array radar, anten dipole, EMI trong mạch điện tử tốc độ cao đều dựa trên cùng một nguyên lý này

---
*Exported from Feynman Bot*
