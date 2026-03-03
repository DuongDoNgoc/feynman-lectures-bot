---
lesson_id: 5573
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:08.281203+00:00"
content_hash: a41a919c10e2
chapter_number: 33
chapter_title: Chapter 33
section_number: 5
section_title: 33–4Polarizers
---
# ## Định luật Malus, Lưỡng Sắc và Hệ Ba Polaroid — Phân tích Chuyên sâu

*Source: Chapter 33 - Chapter 33 (Section 5) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_33.html)*

## Định luật Malus, Lưỡng Sắc và Hệ Ba Polaroid — Phân tích Chuyên sâu

### Cơ chế vi mô của lưỡng sắc

Trong vật liệu lưỡng sắc như polaroid, các phân tử herapathite (muối iốt-quinine) được căn chỉnh song song nhau. Điện tử liên kết trong các phân tử này có thể dao động dọc theo trục dài của phân tử nhưng bị hạn chế mạnh theo trục ngắn.

Khi ánh sáng đến với điện trường $\mathbf{E}$ có thành phần theo trục hấp thụ (absorption axis), điện tử dao động và tạo ra dòng điện trong vật liệu — năng lượng sóng chuyển thành nhiệt. Thành phần theo trục cho qua (pass axis) không kích thích dao động cộng hưởng mạnh, nên truyền qua với ít suy hao.

---

### Suy luận định luật Malus từ phân tích vector

Ánh sáng phân cực tuyến tính chiếu vào polaroid:

$$\mathbf{E}_{tới} = E_0(\cos	heta\,\hat{p} + \sin	heta\,\hat{a})$$

trong đó $\hat{p}$ là trục cho qua (pass axis), $\hat{a}$ là trục hấp thụ (absorption axis), $	heta$ là góc giữa hướng phân cực và $\hat{p}$.

Polaroid hấp thụ hoàn toàn thành phần $\hat{a}$:

$$\mathbf{E}_{ra} = E_0\cos	heta\,\hat{p}$$

Cường độ $I \propto |\mathbf{E}|^2$:

$$I_{ra} = I_0\cos^2	heta$$

Đây là **định luật Malus**. Thật đơn giản nhưng sâu sắc — cường độ ánh sáng sau polaroid phụ thuộc **bình phương** (không phải tuyến tính) của góc.

---

### Ánh sáng tự nhiên qua một polaroid

Ánh sáng tự nhiên (không phân cực) có thể xem là tổ hợp của ánh sáng phân cực tuyến tính theo mọi hướng đồng đều:

$$I_{ra} = \langle I_0\cos^2	heta angle_	heta = I_0 \cdot rac{1}{2\pi}\int_0^{2\pi}\cos^2	heta\,d	heta = rac{I_0}{2}$$

Kết quả quan trọng: **Polaroid lý tưởng giảm cường độ ánh sáng tự nhiên đi một nửa**.

---

### Phân tích hệ ba polaroid: Nghịch lý và giải thích

**Hệ hai polaroid vuông góc** ($	heta_1 = 90°$):

$$I = I_0 \cdot \cos^2(90°) = 0$$

**Thêm polaroid thứ ba ở giữa**, nghiêng $lpha = 45°$ so với polaroid đầu tiên:

Bước 1: Ánh sáng qua polaroid 1 (trục nằm ngang): $I_1 = I_0/2$ (từ ánh sáng tự nhiên), phân cực nằm ngang.

Bước 2: Ánh sáng phân cực nằm ngang gặp polaroid giữa (trục $45°$):
$$I_2 = I_1\cos^2(45°) = rac{I_0}{2} \cdot rac{1}{2} = rac{I_0}{4}$$
Ánh sáng ra phân cực theo $45°$.

Bước 3: Ánh sáng phân cực $45°$ gặp polaroid cuối (trục đứng, tức $90°$ so với nằm ngang):
$$I_3 = I_2\cos^2(45°) = rac{I_0}{4} \cdot rac{1}{2} = rac{I_0}{8}$$

**Kết quả**: $I_3 = I_0/8 
eq 0$ — mặc dù polaroid đầu và cuối vuông góc nhau!

**Ý nghĩa vật lý**: Polaroid giữa không chỉ "lọc" — nó **biến đổi** (transform) trạng thái phân cực. Ánh sáng sau polaroid giữa có hướng phân cực mới (45°), không còn là nằm ngang nữa, nên không bị polaroid cuối chặn hoàn toàn.

---

### Tổng quát hóa: Tối ưu hóa góc để truyền qua nhiều nhất

Với $n$ polaroid ở giữa, mỗi cái nghiêng $\Delta	heta = 90°/n$ so với cái trước:

$$I_{ra} = rac{I_0}{2}\left(\cosrac{90°}{n}ight)^{2n}$$

Khi $n 	o \infty$: $I_{ra} 	o I_0/2$. Điều này có nghĩa là bằng vô số polaroid xoay dần dần, ta có thể **quay hướng phân cực $90°$ mà không mất nhiều cường độ**!

Ví dụ số: $n = 6$ polaroid, mỗi cái nghiêng $15°$:
$$I_{ra} = rac{I_0}{2}(\cos 15°)^{12} = rac{I_0}{2}(0.9659)^{12} pprox rac{I_0}{2} 	imes 0.647 pprox 0.32\,I_0$$

So với $I_0/8 = 0.125\,I_0$ khi chỉ dùng 1 tấm trung gian — hiệu quả hơn nhiều.

---

### Ứng dụng thực tế: Điều khiển độ sáng trong hệ thống quang học

**Biến trở quang học (optical attenuator)**: Trong thiết bị đo lường laser chính xác, cần điều chỉnh cường độ chùm tia liên tục mà không làm suy giảm chất lượng chùm tia. Giải pháp: hai tấm polaroid, một cố định, một quay được. Công thức:

$$I_{ra} = rac{I_0}{2}\cos^2	heta$$

Quay tấm thứ hai một góc $	heta$, điều chỉnh cường độ từ $I_0/2$ (ở $	heta = 0°$) xuống $0$ (ở $	heta = 90°$). Độ phân giải điều chỉnh rất mịn, không có bước nhảy như ND filter.

**Isolator quang học (optical isolator)**: Trong hệ thống laser công suất cao (ví dụ: laser dẫn đường, laser điều khiển vũ khí), ánh sáng phản xạ quay về nguồn có thể phá hủy laser diode. Isolator dùng kết hợp polaroid và rotator Faraday (quay pha $45°$ do từ trường): ánh sáng đi xuôi qua, ánh sáng phản chiếu bị lệch $90°$ và bị chặn.

---

### Bài tập mẫu

**Đề bài**: Một hệ thống đo lường quang học dùng laser phân cực với cường độ $I_0 = 10\,	ext{mW}$. Hai tấm polaroid được đặt trong đường truyền, tấm thứ nhất nghiêng $30°$ so với hướng phân cực laser, tấm thứ hai nghiêng $60°$ so với tấm thứ nhất. Tính cường độ ra $I_{ra}$.

**Lời giải**:

Bước 1: Qua tấm polaroid 1 (góc $	heta_1 = 30°$ so với hướng phân cực ban đầu):
$$I_1 = I_0\cos^2(30°) = 10\,	ext{mW} 	imes (0.866)^2 = 10 	imes 0.75 = 7.5\,	ext{mW}$$

Ánh sáng ra phân cực theo hướng của tấm 1.

Bước 2: Qua tấm polaroid 2 (góc $	heta_2 = 60°$ so với tấm 1):
$$I_{ra} = I_1\cos^2(60°) = 7.5\,	ext{mW} 	imes (0.5)^2 = 7.5 	imes 0.25 = 1.875\,	ext{mW}$$

**Kết quả**: $I_{ra} = 1.875\,	ext{mW}$ — giảm ~81% so với ban đầu.

**Ý nghĩa**: Toàn bộ góc quay là $30° + 60° = 90°$ — nếu dùng một tấm polaroid $90°$ thì $I = 0$. Nhưng qua hai bước, còn 18.75% cường độ — minh chứng cho hiệu ứng "cầu nối" của polaroid trung gian.

---

### Điểm mấu chốt

- Định luật Malus $I = I_0\cos^2	heta$: cường độ ánh sáng sau polaroid phụ thuộc bình phương cosin góc giữa phân cực tới và trục cho qua
- Ánh sáng tự nhiên qua polaroid: luôn giảm đúng $1/2$ cường độ
- Hệ ba polaroid: tấm giữa biến đổi hướng phân cực, cho phép ánh sáng "vượt qua" hai polaroid vuông góc nhau
- Ứng dụng: biến trở quang học, optical isolator trong hệ laser chính xác

---
*Exported from Feynman Bot*
