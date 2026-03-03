---
lesson_id: 5570
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:08.221210+00:00"
content_hash: 9ba0b676d15a
chapter_number: 33
chapter_title: Chapter 33
section_number: 2
section_title: 33–1The electric vector of light
---
# ## Phân cực Ánh sáng — Phân tích Chuyên sâu

*Source: Chapter 33 - Chapter 33 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_33.html)*

## Phân cực Ánh sáng — Phân tích Chuyên sâu

### Mô tả toán học đầy đủ trạng thái phân cực

Ánh sáng truyền theo trục $z$ có điện trường:

$$\mathbf{E}(z,t) = \left[E_{0x}\cos(\omega t - kz)\,\hat{x} + E_{0y}\cos(\omega t - kz + \delta)\,\hat{y}ight]$$

với $\delta$ là hiệu pha giữa hai thành phần. Đây là phương trình tổng quát của mọi trạng thái phân cực.

---

### Phân loại trạng thái phân cực

**1. Phân cực tuyến tính** ($\delta = 0$ hoặc $\delta = \pi$):

$$\mathbf{E} = (E_{0x}\hat{x} + E_{0y}\hat{y})\cos(\omega t - kz)$$

Vector điện trường dao động dọc theo một đường thẳng. Góc phân cực: $	heta = rctan(E_{0y}/E_{0x})$.

**2. Phân cực tròn** ($\delta = \pm\pi/2$, $E_{0x} = E_{0y} = E_0$):

$$\mathbf{E} = E_0\left[\cos(\omega t - kz)\,\hat{x} \pm \sin(\omega t - kz)\,\hat{y}ight]$$

Điện trường vẽ đường tròn bán kính $E_0$ trong mặt phẳng $xy$. Dấu $+$: phân cực trái (left circular); dấu $-$: phân cực phải (right circular).

**3. Phân cực elip**: Trường hợp tổng quát. Điện trường vẽ hình elip với bán trục:

$$a = \sqrt{E_{0x}^2\cos^2lpha + E_{0y}^2\sin^2lpha}, \quad b = |E_{0x}E_{0y}\sin\delta|/\sqrt{E_{0x}^2 + E_{0y}^2}$$

---

### Ma trận Jones: Công cụ mô tả phân cực

Trong quang học hiện đại, trạng thái phân cực được biểu diễn bằng **vector Jones**:

$$\mathbf{J} = egin{pmatrix} E_{0x} \ E_{0y}e^{i\delta} \end{pmatrix}$$

Tác dụng của các phần tử quang học lên trạng thái phân cực được mô tả bằng **ma trận Jones** $2	imes 2$:

| Phần tử | Ma trận Jones |
|---------|--------------|
| Tấm phân cực theo $x$ | $egin{pmatrix}1 & 0\0 & 0\end{pmatrix}$ |
| Tấm bước sóng 1/4 (trục $x$) | $egin{pmatrix}1 & 0\0 & i\end{pmatrix}$ |
| Tấm bước sóng 1/2 | $egin{pmatrix}1 & 0\0 & -1\end{pmatrix}$ |

Hệ thống nhiều phần tử: $\mathbf{J}_{out} = M_n \cdots M_2 M_1 \cdot \mathbf{J}_{in}$

---

### Tính lưỡng chiết (Birefringence): Cơ chế vi mô

Trong vật liệu dị hướng (anisotropic), các phân tử có hình dạng bất đối xứng. Điện tử bị buộc dao động theo trục dài của phân tử dễ hơn theo trục ngắn — dẫn đến **hằng số điện môi tensor** $arepsilon_{ij}$:

$$D_i = arepsilon_0 \sum_j arepsilon_{ij} E_j$$

Điều này dẫn đến **chỉ số khúc xạ khác nhau** cho hai hướng phân cực:
- $n_o$ (ordinary ray): phân cực vuông góc trục quang học
- $n_e$ (extraordinary ray): phân cực song song trục quang học

Sự khác biệt $\Delta n = n_e - n_o$ tạo ra **hiệu pha** giữa hai thành phần khi qua bản dày $d$:

$$\delta = rac{2\pi}{\lambda}(n_e - n_o)d$$

Đây là nguyên lý của **bản bước sóng** (wave plate): tấm $\lambda/4$ tạo $\delta = 90°$, tấm $\lambda/2$ tạo $\delta = 180°$.

---

### Ứng dụng thực tế: Giao thoa kế phân cực cho đo lường cấp nm

**Nguyên lý giao thoa kế Michelson phân cực** (dùng trong máy đo tọa độ CMM và encoder tuyến tính):

Bước 1: Laser phân cực tuyến tính 45° chiếu vào bộ chia chùm phân cực (PBS):
$$\mathbf{J}_{in} = rac{1}{\sqrt{2}}egin{pmatrix}1\1\end{pmatrix}$$

PBS tách thành 2 chùm: $\mathbf{J}_x = egin{pmatrix}1\0\end{pmatrix}$ đến gương đứng yên, $\mathbf{J}_y = egin{pmatrix}0\1\end{pmatrix}$ đến gương di động.

Bước 2: Gương di động dịch chuyển $\Delta x$, tạo hiệu đường quang học $2\Delta x$, do đó hiệu pha:
$$\delta = rac{4\pi\Delta x}{\lambda}$$

Bước 3: Hai chùm phản xạ về kết hợp qua PBS, tạo phân cực elip. Sau khi qua tấm phân tích 45°, cường độ:

$$I(\Delta x) = I_0\left[1 + \cos\left(rac{4\pi\Delta x}{\lambda}ight)ight]$$

Độ phân giải lý thuyết: $\lambda/2 pprox 316\,	ext{nm}$ cho laser HeNe ($\lambda = 633\,	ext{nm}$). Với nội suy điện tử 1000 lần, đạt độ phân giải 0.3 nm — vượt xa yêu cầu cấp micromet.

---

### Bài tập mẫu

**Đề bài**: Trong hệ thống đo vị trí laser dùng giao thoa kế phân cực với laser $\lambda = 633\,	ext{nm}$, bộ điều khiển đọc được thay đổi pha $\delta = 126°$. Tính dịch chuyển $\Delta x$ của gương di động.

**Lời giải**:

Bước 1: Đổi pha sang radian: $\delta = 126° = 126 	imes rac{\pi}{180} = 2.199\,	ext{rad}$

Bước 2: Áp dụng công thức: $\delta = rac{4\pi\Delta x}{\lambda}$

Bước 3: Giải $\Delta x$:
$$\Delta x = rac{\delta \lambda}{4\pi} = rac{2.199 	imes 633\,	ext{nm}}{4\pi} = rac{1392\,	ext{nm}}{12.566} = 110.8\,	ext{nm}$$

**Ý nghĩa**: Chỉ cần đo pha thay đổi $126°$ là đủ để xác định dịch chuyển $pprox 111\,	ext{nm}$ — nhỏ hơn 1/5 bước sóng. Đây là sức mạnh của phép đo giao thoa phân cực.

---

### Điểm mấu chốt

- Trạng thái phân cực được mô tả đầy đủ bởi vector Jones; hệ quang học tác động qua ma trận Jones
- Lưỡng chiết ($\Delta n 
eq 0$) là cơ sở của bản bước sóng ($\lambda/4$, $\lambda/2$) — công cụ kiểm soát phân cực
- Giao thoa kế phân cực cho phép đo dịch chuyển với độ phân giải sub-nm bằng cách theo dõi hiệu pha $\delta = 4\pi\Delta x/\lambda$
- Trong cơ điện tử quân sự và đo lường chính xác, hiểu biết sâu về phân cực ánh sáng là yêu cầu thiết yếu

---
*Exported from Feynman Bot*
