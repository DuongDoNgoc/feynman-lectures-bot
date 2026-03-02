---
lesson_id: 5510
lesson_type: deep_dive
approval_status: pending
exported_at: "2026-03-02T15:10:31.383128+00:00"
content_hash: e12205c3c2ea
chapter_number: 26
chapter_title: Chapter 26
section_number: 5
section_title: 26–4Applications of Fermat’s principle
---
# ## Hệ Quả Nguyên Lý Fermat: Thuận Nghịch, Ảo Ảnh và Hội Tụ — Phân tích Chuyên sâ

*Source: Chapter 26 - Chapter 26 (Section 5) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_26.html)*

## Hệ Quả Nguyên Lý Fermat: Thuận Nghịch, Ảo Ảnh và Hội Tụ — Phân tích Chuyên sâu

### Nguyên Lý Thuận Nghịch (Reciprocity)

Hệ quả đầu tiên và căn bản nhất của nguyên lý Fermat là tính **thuận nghịch quang học** (optical reciprocity). Nếu đường đi tốn ít thời gian nhất từ $A$ đến $B$ là đường $\gamma$, thì đường từ $B$ về $A$ cũng là $\gamma$ (giả sử ánh sáng truyền với vận tốc như nhau theo cả hai chiều). Do đó, nếu ánh sáng có thể đi từ $A$ đến $B$, nó cũng có thể đi ngược lại.

**Ứng dụng trong cơ điện tử:** Trong các hệ thống đo lường laser interferometer, nguyên lý thuận nghịch đảm bảo rằng nếu bạn thiết kế đường quang để ánh sáng đi từ nguồn đến gương đo được, thì ánh sáng phản xạ cũng trở về nguồn theo đúng đường đó. Đây là cơ sở của **retroreflector** và các thiết kế **common-path interferometer** giúp giảm thiểu nhiễu do rung động môi trường.

### Phân Tích Khối Kính Song Song

Khi ánh sáng đi từ điểm $A$ (trong không khí) qua khối kính phẳng song song đến điểm $B$ (trong không khí), định luật Snell áp dụng tại cả hai mặt:

- Mặt vào: $\sin\theta_1 = n\sin\theta_2$ (không khí → kính)
- Mặt ra: $n\sin\theta_2 = \sin\theta_3$ (kính → không khí)

Suy ra $\theta_3 = \theta_1$: tia ra song song với tia vào! Chùm tia chỉ bị **dịch chuyển ngang** một đoạn:
$$d = \frac{t\sin(\theta_1 - \theta_2)}{\cos\theta_2}$$

trong đó $t$ là bề dày khối kính.

**Ứng dụng thực tế:** Trong thiết bị đo giao thoa (Fabry-Pérot interferometer) dùng trong cảm biến áp suất hoặc cảm biến gia tốc MEMS, khối kính song song (etalon) tạo ra nhiều chùm phản xạ với độ trễ pha cố định. Sai số bề dày $\delta t = 1\,\mu\text{m}$ gây ra sai số độ trễ pha $\delta\phi = 2\pi n \delta t / \lambda$, cần được kiểm soát chặt.

### Giải Thích Ảo Ảnh và Hoàng Hôn Muộn

Khí quyển Trái Đất có mật độ giảm dần theo độ cao, dẫn đến chiết suất $n(h)$ giảm dần (ánh sáng nhanh hơn ở độ cao cao hơn). Theo nguyên lý Fermat, ánh sáng tối ưu hóa thời gian bằng cách uốn cong về phía vùng đặc hơn (chậm hơn) khi cần, hoặc tránh vùng đó khi có lợi.

**Hiện tượng hoàng hôn muộn:** Ánh sáng mặt trời (khi mặt trời đã dưới đường chân trời) uốn cong theo khí quyển đặc dần, làm ta vẫn nhìn thấy mặt trời. Độ lệch góc khoảng $0.5°$, tương ứng với đường kính góc của mặt trời, nên khi ta thấy mặt trời "chạm" chân trời, nó thực sự đã lặn hoàn toàn.

**Hiện tượng mirage (ảo ảnh nước):** Mặt đường nóng tạo ra lớp không khí loãng (nhanh hơn) ngay trên mặt đường. Ánh sáng từ bầu trời hướng xuống mặt đường có thể "tiết kiệm thời gian" bằng cách uốn cong xuống vào vùng nhanh, rồi vòng lên lại đến mắt người xem. Kết quả: ta "nhìn thấy" bầu trời trên mặt đường — y như nhìn thấy nước!

Gradient chiết suất tuân theo phương trình eikonal:
$$\nabla n = \frac{d}{ds}\left(n\frac{d\mathbf{r}}{ds}\right)$$

trong đó $s$ là tọa độ dọc theo tia sáng.

### Điều Kiện Hội Tụ: Cơ Sở Thiết Kế Thấu Kính

Bài toán then chốt: làm thế nào để tất cả tia sáng từ điểm $P$ hội tụ tại $P'$? Nguyên lý Fermat cho đáp án rõ ràng: **thời gian đi theo mọi đường phải bằng nhau**.

Xét tia thẳng $PP'$ (không qua thấu kính) và tia qua điểm $Q$ trên thấu kính:
- Đường thẳng $PP'$ (toàn trong không khí): thời gian $t_0 = |PP'|/c$
- Đường $PQP'$ qua kính dày $e(Q)$: thời gian $t = \frac{|PQ| + |QP'| - e(Q)}{c} + \frac{n \cdot e(Q)}{c}$

Điều kiện $t = t_0$ cho:
$$|PQ| + |QP'| + (n-1)e(Q) = |PP'|$$
$$\Rightarrow e(Q) = \frac{|PP'| - |PQ| - |QP'|}{n-1}$$

Đây là phương trình xác định **hình dạng bề mặt thấu kính** để tạo ra hội tụ hoàn hảo (với gần đúng paraxial)!

### Bài Tập Mẫu: Thiết Kế Thấu Kính Hội Tụ Laser

**Đề bài:** Một chùm laser cần được hội tụ từ nguồn điểm $P$ (cách thấu kính $f_o = 100\,\text{mm}$) đến tiêu điểm $P'$ (cách thấu kính $f_i = 50\,\text{mm}$). Thấu kính làm bằng kính có $n = 1.5$. Tính bề dày $e$ cần thiết tại điểm $Q$ nằm ở bán kính $r = 5\,\text{mm}$ từ trục quang.

**Lời giải từng bước:**

*Bước 1:* Tính khoảng cách $|PQ|$ và $|QP'|$:
$$|PQ| = \sqrt{f_o^2 + r^2} = \sqrt{100^2 + 5^2} \approx 100.125\,\text{mm}$$
$$|QP'| = \sqrt{f_i^2 + r^2} = \sqrt{50^2 + 5^2} \approx 50.250\,\text{mm}$$

*Bước 2:* Tổng đường đi qua $Q$ (không có kính):
$$|PQ| + |QP'| \approx 150.375\,\text{mm}$$

*Bước 3:* Đường thẳng $|PP'| = 150\,\text{mm}$.

*Bước 4:* Bề dày kính cần bù:
$$e = \frac{150.375 - 150}{1.5 - 1} = \frac{0.375}{0.5} = 0.75\,\text{mm}$$

*Ý nghĩa:* Thấu kính cần dày thêm $0.75\,\text{mm}$ tại $r = 5\,\text{mm}$ so với tâm, để ánh sáng đi qua cạnh tốn thêm đúng lượng thời gian bằng tia trung tâm. Đây là nguyên lý của aspheric lens design trong đầu đọc DVD và cảm biến laser.

### Ứng Dụng: Thiết Kế Hệ Thống Quang Học Vũ Khí Chính Xác

Trong hệ thống ngắm quang học (optical sight) hay đầu dẫn laser (laser seeker) của vũ khí dẫn đường:
1. Thấu kính **objective** thu ánh sáng mục tiêu và hội tụ tại tiêu diện.
2. Điều kiện Fermat đảm bảo mọi tia từ cùng một điểm mục tiêu đến cùng một điểm ảnh — đây là điều kiện **diffraction-limited performance**.
3. Sai số hình dạng bề mặt thấu kính (surface figure error) làm vi phạm điều kiện thời gian bằng nhau, gây ra **wavefront aberration** đo bằng $\lambda/10$ hoặc nhỏ hơn trong hệ thống cao cấp.

---
*Exported from Feynman Bot*
