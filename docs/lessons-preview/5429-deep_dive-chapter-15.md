---
lesson_id: 5429
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-02T15:10:29.212360+00:00"
content_hash: 6ce4f6475b9e
chapter_number: 15
chapter_title: Chapter 15
section_number: 6
section_title: 15–5The Lorentz contraction
---
# ## Phép Biến Đổi Lorentz và Sự Thất Bại của Đồng Thời — Phân tích Chuyên sâu

*Source: Chapter 15 - Chapter 15 (Section 6) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_15.html)*

## Phép Biến Đổi Lorentz và Sự Thất Bại của Đồng Thời — Phân tích Chuyên sâu

### 1. Bối cảnh: Hai hệ quy chiếu Joe và Moe

Xét hai hệ quy chiếu quán tính:
- Hệ $S$ với tọa độ $(x, y, z, t)$ — "Joe đứng yên"
- Hệ $S'$ với tọa độ $(x', y', z', t')$ — "Moe chuyển động" với vận tốc $u$ dọc trục $x$

Câu hỏi trung tâm: nếu Moe quan sát một sự kiện tại tọa độ $(x', t')$, Joe sẽ ghi nhận sự kiện đó tại tọa độ nào $(x, t)$?

### 2. Suy luận phép biến đổi — Từ co Lorentz đến phương trình

**Bước 1: Co Lorentz theo trục $x$**

Thí nghiệm Michelson-Morley yêu cầu nhánh ngang $BC$ không đổi chiều dài (theo nguyên lý tương đối), trong khi nhánh dọc $BE$ phải co lại để cho kết quả null. Hệ số co là $\sqrt{1-u^2/c^2}$.

**Bước 2: Đo chiều dài trong hai hệ quy chiếu**

Moe dùng thước đo $x'$ lần — anh nghĩ khoảng cách là $x'$ mét. Nhưng theo Joe, thước của Moe đã bị co (Lorentz contraction):

$$	ext{Khoảng cách thực theo Joe} = x' \sqrt{1-u^2/c^2}$$

Cộng thêm khoảng dịch chuyển $ut$ của hệ $S'$ xa hệ $S$:

$$x = x'\sqrt{1-u^2/c^2} + ut$$

Giải ngược lại để tìm $x'$:

$$oxed{x' = rac{x - ut}{\sqrt{1-u^2/c^2}}}$$

*Ý nghĩa vật lý*: Công thức này nói rằng để đo tọa độ trong hệ đang chuyển động, ta phải trừ đi quãng đường hệ đó đã đi ($ut$) rồi "mở rộng" lại thước đã bị co. Đây là dạng tổng quát hóa của phép biến đổi Galileo cổ điển $x' = x - ut$, với hệ số co Lorentz bổ sung.

**Bước 3: Biến đổi thời gian — phần bất ngờ nhất**

Phương trình thứ tư của biến đổi Lorentz (biến đổi thời gian) có dạng:

$$t' = rac{t - ux/c^2}{\sqrt{1-u^2/c^2}}$$

Số hạng $ux/c^2$ trong tử số là hoàn toàn mới và không có trong vật lý cổ điển. Ý nghĩa của nó là gì?

### 3. Sự thất bại của đồng thời tuyệt đối

**Tình huống**: Moe trong hệ $S'$ quan sát hai sự kiện:
- Sự kiện 1: xảy ra tại $x_1$, thời điểm $t_0$
- Sự kiện 2: xảy ra tại $x_2$, thời điểm $t_0$ (cùng lúc với sự kiện 1 theo Moe)

Theo phương trình biến đổi thời gian Lorentz, Joe trong hệ $S$ đo được hiệu thời gian:

$$t_2' - t_1' = rac{u(x_1 - x_2)/c^2}{\sqrt{1-u^2/c^2}}$$

Vì $x_1 
eq x_2$ và $u 
eq 0$, Joe thấy hai sự kiện này KHÔNG đồng thời!

**Bước suy luận trực quan**: Moe trên tàu vũ trụ đặt hai đồng hồ ở hai đầu, đồng bộ hoá bằng xung ánh sáng từ điểm giữa:
- Moe: tín hiệu đến hai đồng hồ đồng thời → hai đồng hồ đồng bộ
- Joe đứng ngoài: tàu tiến về phía trước → đồng hồ mũi "chạy trốn" khỏi tín hiệu (ánh sáng phải đi xa hơn) → tín hiệu đến đồng hồ đuôi TRƯỚC
- Kết luận Joe: hai đồng hồ của Moe không đồng bộ!

Cả hai đều đúng trong hệ quy chiếu riêng. Đây không phải mâu thuẫn — đây là bản chất của không-thời gian (spacetime).

### 4. Ví dụ thực tế: Đồng bộ hoá cảm biến trong hệ đo lường phân tán

Trong thiết kế hệ thống đo lường với nhiều sensor đặt tại các vị trí khác nhau (ví dụ: mạng encoder dọc theo trục máy CNC dài 10 mét), vấn đề đồng bộ hoá thời gian là quan trọng hàng đầu.

**Vấn đề thực tế**: Nếu hai encoder cách nhau $\Delta x = 10$ m và hệ thống đọc dữ liệu qua bus với tốc độ truyền tín hiệu hữu hạn (ví dụ EtherCAT với độ trễ lan truyền ~5 ns/m), sự kiện "đọc đồng thời" thực ra có độ lệch thời gian:

$$\Delta t_{truyền} = rac{\Delta x}{v_{tín hiệu}} = rac{10 	ext{ m}}{2 	imes 10^8 	ext{ m/s}} = 50 	ext{ ns}$$

Ở tốc độ máy công nghiệp (ví dụ: trục chạy 1 m/s), trong 50 ns, máy đã dịch chuyển:
$$\Delta x_{lỗi} = 1 	ext{ m/s} 	imes 50 	imes 10^{-9} 	ext{ s} = 50 	ext{ nm}$$

Đây là sai số **50 nm** — hoàn toàn quan trọng trong đo lường micromet! Nguyên lý đằng sau y hệt "failure of simultaneity": thứ tự và tính đồng thời của sự kiện "đọc sensor" phụ thuộc vào điểm tham chiếu thời gian. Giải pháp: dùng IEEE 1588 Precision Time Protocol (PTP) để đồng bộ hoá đồng hồ tất cả node về cùng "hệ quy chiếu thời gian" — chính xác đến nanosecond.

### 5. Bài tập mẫu có lời giải

**Bài toán**: Một tên lửa (hệ $S'$) bay với vận tốc $u = 0.6c$ so với mặt đất (hệ $S$). Tên lửa dài $L' = 100$ m theo người trong tên lửa. Người trên mặt đất đo chiều dài tên lửa là bao nhiêu? Nếu người trong tên lửa ghi nhận hai sự kiện tại hai đầu tên lửa ($\Delta x' = 100$ m) xảy ra đồng thời ($\Delta t' = 0$), người trên mặt đất đo được hiệu thời gian giữa hai sự kiện là bao nhiêu?

**Lời giải từng bước**:

*Bước 1*: Tính hệ số Lorentz $\gamma$:
$$\gamma = rac{1}{\sqrt{1-u^2/c^2}} = rac{1}{\sqrt{1-0.36}} = rac{1}{\sqrt{0.64}} = rac{1}{0.8} = 1.25$$

*Bước 2*: Co Lorentz — chiều dài tên lửa theo người mặt đất:
$$L = rac{L'}{\gamma} = rac{100 	ext{ m}}{1.25} = 80 	ext{ m}$$
*Ý nghĩa*: Tên lửa bị "nén" theo hướng chuyển động. Người mặt đất đo 80 m, người tên lửa đo 100 m — cả hai đều đúng trong hệ quy chiếu của mình.

*Bước 3*: Sự thất bại đồng thời — hiệu thời gian theo người mặt đất:

Dùng phương trình biến đổi ngược (từ $S'$ sang $S$):
$$\Delta t = \gamma \left(\Delta t' + rac{u \cdot \Delta x'}{c^2}ight) = 1.25 \left(0 + rac{0.6c 	imes 100 	ext{ m}}{c^2}ight)$$
$$\Delta t = 1.25 	imes rac{60 	ext{ m}}{c} = 1.25 	imes rac{60}{3	imes10^8} 	ext{ s} = 2.5 	imes 10^{-7} 	ext{ s} = 250 	ext{ ns}$$

*Ý nghĩa*: Hai sự kiện mà người tên lửa thấy "đồng thời" thực ra cách nhau 250 ns theo người mặt đất. Trong hệ thống GPS, các vệ tinh bay với $u pprox 4 	ext{ km/s} pprox 1.3	imes10^{-5}c$ nên hiệu ứng tương đối hẹp tích lũy khoảng 7 µs/ngày — đủ gây sai số định vị ~2 km nếu không hiệu chỉnh!

### 6. Tóm tắt

Phép biến đổi Lorentz không phải trừu tượng — nó có hệ quả đo lường thực tế. Hai kỹ thuật quan trọng cho kỹ sư đo lường:
1. **Co Lorentz** ảnh hưởng đến các hệ đo lường cực nhanh (hạt trong máy gia tốc, GPS)
2. **Failure of simultaneity** ảnh hưởng đến đồng bộ hoá sensor phân tán — nguyên lý vật lý tương tự cần được hiệu chỉnh ở mọi hệ đo lường có khoảng cách không gian giữa các sensor

---
*Exported from Feynman Bot*
