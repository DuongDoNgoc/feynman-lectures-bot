---
lesson_id: 5507
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:06.784616+00:00"
content_hash: 248fb3c2fcbd
chapter_number: 26
chapter_title: Chapter 26
section_number: 4
section_title: 26–3Fermat’s principle of least time
---
# ## Nguyên Lý Thời Gian Cực Tiểu (Fermat's Principle) — Phân tích Chuyên sâu

*Source: Chapter 26 - Chapter 26 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_26.html)*

## Nguyên Lý Thời Gian Cực Tiểu (Fermat's Principle) — Phân tích Chuyên sâu

### Từ Quan Sát đến Nguyên Lý: Con Đường của Ánh Sáng

Trong sự phát triển của khoa học, chúng ta không chỉ dừng lại ở công thức. Quá trình nhận thức đi từ quan sát → đo đạc → định luật → nguyên lý tư duy. Bước nhảy vọt cuối cùng — tìm ra "cách tư duy" khiến định luật trở nên hiển nhiên — chính là đỉnh cao của khoa học. Fermat đã đạt được điều đó vào năm 1650 với **Nguyên lý Thời gian Cực tiểu** (Principle of Least Time): trong tất cả các đường đi có thể từ điểm này sang điểm khác, ánh sáng chọn đường đi tốn ít thời gian nhất.

### Bước 1: Chứng Minh Định Luật Phản Xạ từ Nguyên Lý Fermat

Xét hai điểm $A$ và $B$ với gương phẳng $MM'$ ở giữa. Bài toán: tìm điểm $C$ trên gương sao cho tổng thời gian $t = t_{AC} + t_{CB}$ là nhỏ nhất.

Vì ánh sáng truyền với vận tốc không đổi $c$ trong không khí, tối thiểu hóa thời gian tương đương với tối thiểu hóa tổng độ dài đường đi $AC + CB$.

**Mẹo hình học của Fermat:** Dựng điểm ảo $B'$ đối xứng với $B$ qua gương $MM'$. Khi đó $CB = CB'$ với mọi điểm $C$ trên gương. Vậy:
$$AC + CB = AC + CB'$$

Tổng này nhỏ nhất khi $A$, $C$, $B'$ thẳng hàng — tức là khi $C$ nằm trên đường thẳng nối $A$ với $B'$. Tại điểm $C$ đó:
- Góc tới $= $ góc giữa $AC$ và pháp tuyến gương
- Góc phản xạ $= $ góc giữa $CB$ và pháp tuyến gương

Vì $AB'$ cắt $MM'$ tại $C$ và $B'$ đối xứng với $B$, hai góc này **bằng nhau**. Đây chính là định luật phản xạ! Nguyên lý Fermat đã sinh ra định luật phản xạ một cách tự nhiên.

**Ý nghĩa vật lý:** Ánh sáng không "chọn" đường theo nghĩa có ý thức. Thực ra, ánh sáng là sóng điện từ và truyền theo mọi hướng. Chỉ những đường đi mà thời gian là cực trị (stationary) mới có sự giao thoa tăng cường — đây là cái nhìn lượng tử sâu hơn mà Feynman sẽ giới thiệu sau.

### Bước 2: Chứng Minh Định Luật Khúc Xạ (Snell's Law)

Xét ánh sáng đi từ môi trường 1 (vận tốc $v_1$, chiết suất $n_1$) sang môi trường 2 (vận tốc $v_2$, chiết suất $n_2$), với $v = c/n$.

Thời gian đi qua tổng đường là:
$$t = \frac{\sqrt{x^2 + a^2}}{v_1} + \frac{\sqrt{(d-x)^2 + b^2}}{v_2}$$

Tối thiểu hóa theo $x$ (vị trí điểm tới mặt phân cách):
$$\frac{dt}{dx} = 0 \Rightarrow \frac{x}{v_1 \sqrt{x^2+a^2}} - \frac{(d-x)}{v_2 \sqrt{(d-x)^2+b^2}} = 0$$

Nhận ra rằng $\frac{x}{\sqrt{x^2+a^2}} = \sin\theta_1$ và $\frac{d-x}{\sqrt{(d-x)^2+b^2}} = \sin\theta_2$:
$$\frac{\sin\theta_1}{v_1} = \frac{\sin\theta_2}{v_2} \Rightarrow n_1\sin\theta_1 = n_2\sin\theta_2$$

Đây chính là **Định luật Snell**! Fermat đã suy ra nó từ giả thuyết ánh sáng đi chậm hơn trong môi trường đặc hơn — đúng ngược lại với giả thuyết của Newton.

### Ví Dụ Thực Tế: Thiết Kế Gương trong Hệ Thống Đo Lường Quân Sự

Trong hệ thống đo lường laser interferometry dùng cho kiểm soát vị trí cấp micromet (như trong hệ servo của bạn), gương phẳng cao độ chính xác đóng vai trò thiết yếu. Khi thiết kế **laser tracker** hay **interferometer** để đo dịch chuyển, bạn cần đảm bảo:

1. **Góc tới = Góc phản xạ** chính xác đến phần triệu radian — sai lệch $\Delta\theta = 1\,\mu\text{rad}$ trên đường đi $L = 1\,\text{m}$ gây ra lỗi vị trí $\delta = L\cdot\Delta\theta = 1\,\mu\text{m}$.

2. **Retroreflector** (lăng kính góc khối) dùng trong các cảm biến tuyến tính hoạt động dựa trên nguyên lý phản xạ ba lần, đảm bảo tia phản xạ luôn song song với tia tới bất kể góc nghiêng nhỏ — trực tiếp ứng dụng định luật phản xạ.

### Bài Tập Mẫu: Tính Đường Đi Tối Ưu

**Đề bài:** Một cảm biến laser đặt tại $A = (0, 10)\,\text{cm}$ cần đo điểm $B = (20, 10)\,\text{cm}$ qua gương phẳng nằm trên trục $x$. Tìm điểm phản xạ $C$ tối ưu và xác nhận định luật phản xạ.

**Lời giải:**

*Bước 1:* Dựng ảnh $B' = (20, -10)\,\text{cm}$ (đối xứng $B$ qua trục $x$).

*Bước 2:* Đường thẳng $AB'$: đi từ $(0,10)$ đến $(20,-10)$, phương trình:
$$y - 10 = \frac{-10-10}{20-0}(x-0) \Rightarrow y = 10 - x$$

*Bước 3:* Giao với trục $x$ ($y=0$): $x = 10$. Vậy $C = (10, 0)\,\text{cm}$.

*Bước 4:* Kiểm tra góc tới: $\vec{AC} = (10,-10)$, góc với pháp tuyến (trục $y$) là $\arctan(10/10) = 45°$.
Góc phản xạ: $\vec{CB} = (10,10)$, góc với pháp tuyến là $\arctan(10/10) = 45°$. Bằng nhau — xác nhận!

*Ý nghĩa:* Trong hệ interferometer, nếu đặt gương sai lệch 1mm theo phương ngang, điểm phản xạ dịch chuyển và đường quang sai lệch, gây sai số đo.

### Cầu Nối sang Cơ Học Hamilton

Nguyên lý Fermat là tiền thân của **Nguyên lý Tác dụng Cực tiểu** (Principle of Least Action) trong cơ học Hamilton. Đây là nền tảng của cơ học giải tích, điều khiển tối ưu (optimal control), và lý thuyết lượng tử. Trong tự động hóa và điều khiển servo, bài toán tối ưu hóa quỹ đạo robot cũng chia sẻ cùng tư tưởng toán học này.

Nguyên lý Fermat không chỉ là một định luật quang học — đó là một nguyên lý triết học sâu sắc về cách tự nhiên vận hành theo con đường "tối ưu".

---
*Exported from Feynman Bot*
