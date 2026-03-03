---
lesson_id: 5567
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:08.158819+00:00"
content_hash: 44651ed19df0
chapter_number: 32
chapter_title: Chapter 32
section_number: 6
section_title: 32–5Scattering of light
---
# ## Tán xạ Rayleigh và Bầu Trời Xanh — Phân tích Chuyên sâu

*Source: Chapter 32 - Chapter 32 (Section 6) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_32.html)*

## Tán xạ Rayleigh và Bầu Trời Xanh — Phân tích Chuyên sâu

### Tại sao bầu trời màu xanh?

Đây là một trong những câu hỏi vật lý đẹp nhất mà Feynman từng giảng. Câu trả lời nằm ở cơ chế **tán xạ Rayleigh** (Rayleigh scattering) — hiện tượng khi ánh sáng tương tác với các phân tử khí có kích thước nhỏ hơn nhiều so với bước sóng ánh sáng.

---

### Cơ chế vật lý: Điện tử bị kích thích và bức xạ lại

Khi một chùm ánh sáng mặt trời đi qua không khí, điện trường $\mathbf{E}$ của sóng điện từ tác động lên các điện tử trong phân tử khí. Điện tử bị buộc dao động theo:

$$\mathbf{E}_{tới} = \hat{\mathbf{E}}_0 e^{i(\omega t - kz)}$$

Điện tử dao động gia tốc, và theo lý thuyết bức xạ cổ điển, điện tích dao động gia tốc **bức xạ năng lượng ra mọi hướng**. Đây là cơ chế tán xạ.

**Điểm then chốt**: Nếu các nguyên tử sắp xếp đều đặn (tinh thể hoàn hảo), các sóng tán xạ từ mỗi nguyên tử sẽ **giao thoa triệt tiêu nhau** ở mọi hướng khác ngoài hướng truyền thẳng. Nhưng trong chất khí, các phân tử phân bố **ngẫu nhiên** và chuyển động nhiệt làm pha tương đối liên tục thay đổi — do đó các số hạng giao thoa cos trung bình bằng 0.

Kết quả: **Cường độ tán xạ tổng cộng = N × cường độ tán xạ của một nguyên tử** (N là số nguyên tử).

---

### Công thức tán xạ Rayleigh: Suy luận từng bước

**Bước 1**: Cường độ bức xạ từ điện tích gia tốc tỉ lệ với bình phương gia tốc:

$$I \propto a^2 \propto \omega^4$$

vì gia tốc $a = -\omega^2 x_0$ đối với dao động điều hòa biên độ $x_0$.

**Bước 2**: Biên độ dao động của điện tử dưới tác dụng điện trường $E_0$:

$$x_0 = rac{eE_0/m}{\omega_0^2 - \omega^2}$$

với $\omega_0$ là tần số cộng hưởng của nguyên tử, $\omega$ là tần số ánh sáng tới.

**Bước 3**: Với $\omega \ll \omega_0$ (ánh sáng khả kiến vs tần số cộng hưởng UV), mẫu số $pprox \omega_0^2$, và cường độ tán xạ:

$$I_{tán xạ} \propto rac{\omega^4}{\omega_0^4} I_0$$

**Bước 4**: Vì $\omega = 2\pi c/\lambda$, ta có:

$$oxed{I_{tán xạ} \propto rac{1}{\lambda^4}}$$

Đây là **định luật Rayleigh**: cường độ tán xạ tỉ lệ nghịch với $\lambda^4$.

---

### Tại sao bầu trời xanh, hoàng hôn đỏ?

Ánh sáng xanh ($\lambda pprox 450\,	ext{nm}$) bị tán xạ mạnh hơn ánh sáng đỏ ($\lambda pprox 700\,	ext{nm}$) theo tỉ lệ:

$$rac{I_{xanh}}{I_{đỏ}} = \left(rac{700}{450}ight)^4 pprox 5.5$$

Ánh sáng xanh bị tán xạ gấp ~5.5 lần so với ánh sáng đỏ! Khi nhìn lên bầu trời (vuông góc với hướng mặt trời), ta thấy ánh sáng bị tán xạ — tức là thấy màu xanh. Khi mặt trời lặn, ánh sáng đi qua tầng khí quyển dày hơn nhiều, ánh sáng xanh bị tán xạ gần hết, chỉ còn lại ánh sáng đỏ/cam.

---

### Ứng dụng thực tế: Cảm biến đo bụi và hạt lơ lửng

Trong lĩnh vực cơ điện tử và đo lường chính xác, tán xạ Rayleigh/Mie là nguyên lý của **cảm biến đo nồng độ hạt (particle counter)**:

**Lidar (Light Detection And Ranging)**: Bắn xung laser vào khí quyển, đo tín hiệu tán xạ ngược về. Cường độ tín hiệu tỉ lệ với mật độ phân tử/hạt bụi theo $1/\lambda^4$.

**Cảm biến đo độ trong suốt quang học (turbidimeter)**: Trong hệ thống kiểm soát chất lượng nước công nghiệp, đo ánh sáng tán xạ $90°$ so với chùm tới để xác định độ đục (turbidity). Công thức:

$$	ext{Turbidity} = k \cdot rac{I_{tán xạ}}{I_0}$$

**Hệ thống đo độ sạch phòng sạch (cleanroom)**: Trong sản xuất thiết bị quân sự và vi điện tử, cần ISO Class 5 (< 3,520 hạt/m³ cỡ ≥ 0.5 µm). Máy đếm hạt dùng laser 660 nm, đo tán xạ Mie để phân biệt kích thước hạt từ 0.1 µm trở lên.

---

### Bài tập mẫu

**Đề bài**: Một cảm biến đo bụi dùng laser bước sóng $\lambda_1 = 450\,	ext{nm}$ (xanh lam) và $\lambda_2 = 900\,	ext{nm}$ (cận hồng ngoại). Nếu cảm biến xanh đo được cường độ tán xạ $I_1 = 1\,	ext{mW/sr}$, tính cường độ tán xạ $I_2$ của cảm biến hồng ngoại từ cùng mật độ hạt, giả sử các hạt nhỏ hơn bước sóng (chế độ Rayleigh).

**Lời giải**:

Bước 1: Áp dụng định luật Rayleigh $I \propto 1/\lambda^4$:

$$rac{I_1}{I_2} = rac{\lambda_2^4}{\lambda_1^4} = \left(rac{900}{450}ight)^4 = 2^4 = 16$$

Bước 2: Tính $I_2$:

$$I_2 = rac{I_1}{16} = rac{1\,	ext{mW/sr}}{16} = 0.0625\,	ext{mW/sr}$$

**Ý nghĩa vật lý**: Cảm biến hồng ngoại kém nhạy hơn 16 lần trong chế độ Rayleigh. Tuy nhiên trong thực tế, các hệ thống quân sự thường dùng IR vì ánh sáng IR ít bị tán xạ hơn trong khói/sương mù — đây chính là ứng dụng ngược lại của định luật Rayleigh: IR "xuyên qua" môi trường nhiễu loạn tốt hơn.

**Bước 3**: Kiểm tra: khi $\lambda$ tăng gấp đôi, $I$ giảm $2^4 = 16$ lần. Kết quả hợp lý.

---

### Điểm mấu chốt

- Tán xạ Rayleigh xảy ra khi hạt tán xạ nhỏ hơn nhiều so với bước sóng ($d \ll \lambda$)
- Cường độ tán xạ $\propto \omega^4 \propto 1/\lambda^4$ — bước sóng ngắn tán xạ mạnh hơn rất nhiều
- Trong chất khí ngẫu nhiên: cường độ tổng = N × cường độ một nguyên tử (không có giao thoa)
- Ứng dụng: cảm biến đo hạt, lidar, đo độ trong suốt — nền tảng của đo lường chính xác trong môi trường khí

---
*Exported from Feynman Bot*
