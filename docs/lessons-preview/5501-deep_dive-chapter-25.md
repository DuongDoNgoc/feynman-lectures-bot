---
lesson_id: 5501
lesson_type: deep_dive
approval_status: pending
exported_at: "2026-03-02T15:10:31.188521+00:00"
content_hash: 62b7487b6194
chapter_number: 25
chapter_title: Chapter 25
section_number: 4
section_title: 25–3Oscillations in linear systems
---
# ## Phân Tích Sâu: Vật Lý Dao Động Tắt Dần - Từ Trực Quan Đến Định Lượng

*Source: Chapter 25 - Chapter 25 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_25.html)*

## Phân Tích Sâu: Vật Lý Dao Động Tắt Dần - Từ Trực Quan Đến Định Lượng

### 1. Vật lý của dao động: Tại sao hệ cứ dao động?

Trước khi đi vào toán học, hãy hiểu rõ cơ chế vật lý. Một hệ lò xo-quả nặng dao động vì sự tương tác giữa hai xu hướng đối lập:

**Lực phục hồi** (restoring force): Lò xo luôn muốn kéo vật về vị trí cân bằng với lực $F_{lò xo} = -kx$

**Quán tính** (inertia): Vật có khối lượng $m$ không thể thay đổi vận tốc đột ngột; nó tiếp tục chuyển động qua vị trí cân bằng dù lực đã đổi chiều

Hai hiệu ứng này tạo ra vòng phản hồi liên tục: lực đẩy vật về trung tâm, quán tính đưa nó vượt qua, lực lại đẩy ngược lại... Kết quả là dao động tuần hoàn.

**Điều kiện để tần số không thay đổi:** Đây là điều tinh tế mà Feynman nhấn mạnh. Với ma sát nhớt (viscous damping, $F = -b\dot{x}$), tất cả các lực đều tỉ lệ với biên độ:
- Lực lò xo: $\propto A$ (biên độ)
- Lực quán tính: $\propto A$ (gia tốc $\propto A$)
- Lực ma sát: $\propto A$ (vận tốc $\propto A$)

Kết quả: khi biên độ giảm đi, tất cả các lực đều giảm theo cùng tỉ lệ. Hệ vẫn "nhìn như cũ", chỉ là nhỏ hơn. Do đó tần số dao động $\omega$ không thay đổi theo biên độ.

### 2. Từ vật lý đến phương trình

Phương trình Newton cho hệ có ma sát nhớt:

$$m\ddot{x} + b\dot{x} + kx = 0$$

Chuẩn hóa: đặt $\gamma = b/m$ (tần số cản), $\omega_0^2 = k/m$ (tần số tự nhiên bình phương):

$$\ddot{x} + \gamma\dot{x} + \omega_0^2 x = 0$$

Thử nghiệm $x = e^{i\omega t}$ (chú ý: $\omega$ có thể phức):

$$-\omega^2 e^{i\omega t} + i\gamma\omega e^{i\omega t} + \omega_0^2 e^{i\omega t} = 0$$

$$\omega^2 - i\gamma\omega - \omega_0^2 = 0$$

Giải phương trình bậc hai:

$$\omega = \frac{i\gamma \pm \sqrt{-\gamma^2 + 4\omega_0^2}}{2} = \frac{i\gamma}{2} \pm \sqrt{\omega_0^2 - \frac{\gamma^2}{4}}$$

Đặt $\omega_1 = \sqrt{\omega_0^2 - \gamma^2/4}$ (tần số dao động thực), ta có:

$$\omega = \frac{i\gamma}{2} \pm \omega_1$$

### 3. Nghiệm và ý nghĩa vật lý từng trường hợp

**Trường hợp 1: Cản nhỏ (underdamped), $\gamma < 2\omega_0$**

$\omega_1$ là thực dương. Nghiệm:

$$x(t) = e^{-\gamma t/2}\left(C_1 e^{i\omega_1 t} + C_2 e^{-i\omega_1 t}\right) = A_0 e^{-\gamma t/2}\cos(\omega_1 t + \phi)$$

Đây là dao động cosine (tần số $\omega_1$ hơi thấp hơn $\omega_0$) với biên độ suy giảm hàm mũ. Hằng số thời gian: $\tau = 2/\gamma$.

**Trường hợp 2: Cản tới hạn (critically damped), $\gamma = 2\omega_0$**

$\omega_1 = 0$, hai nghiệm trùng nhau. Nghiệm:

$$x(t) = (C_1 + C_2 t)e^{-\gamma t/2}$$

Hệ trở về cân bằng nhanh nhất có thể mà không dao động. Đây là chế độ lý tưởng cho nhiều ứng dụng điều khiển!

**Trường hợp 3: Quá cản (overdamped), $\gamma > 2\omega_0$**

$\omega_1$ thuần ảo, hai nghiệm thực âm. Hệ trở về cân bằng chậm hơn critically damped, cũng không dao động.

### 4. Ứng dụng thực tế: Thiết kế hệ servo

Trong hệ servo điều khiển vị trí micrometer, việc chọn hệ số cản $\gamma$ (hay hệ số cản tương đương $\zeta = \gamma/(2\omega_0)$) là quyết định thiết kế quan trọng:

**$\zeta < 1$ (underdamped):** Đáp ứng nhanh nhưng có overshoot. Với $\zeta = 0.7$ (tiêu chuẩn Butterworth), ta có cân bằng tốt giữa tốc độ và độ ổn định. Vấn đề: với hệ đo micrometer, overshoot có thể gây va chạm cơ học.

**$\zeta = 1$ (critically damped):** Không overshoot, trở về vị trí nhanh nhất. Thường được ưu tiên trong thiết kế cơ khí chính xác.

**$\zeta > 1$ (overdamped):** An toàn, không overshoot, nhưng chậm. Thường gặp khi tăng hệ số cản quá mức (ví dụ: tăng gain tỉ lệ P quá cao trong PID làm hệ dao động, tăng gain vi phân D làm hệ overdamped).

### 5. Hệ số phẩm chất Q và ứng dụng trong đo lường

Hệ số phẩm chất (quality factor) định nghĩa:

$$Q = \frac{\omega_0}{\gamma}$$

Ý nghĩa vật lý: $Q = 2\pi \times \frac{\text{năng lượng tích trữ}}{\text{năng lượng tiêu tán mỗi chu kỳ}}$

Trong đo lường:
- Cảm biến MEMS (Micro-Electro-Mechanical Systems) gia tốc kế: $Q$ thấp (~1-10) để tránh ringing
- Con quay hồi chuyển (gyroscope) MEMS: cần $Q$ cao (~10,000-1,000,000) để tăng độ nhạy
- Đồng hồ thạch anh (quartz crystal): $Q \approx 10^5$, đây là lý do tại sao đồng hồ thạch anh rất chính xác

### 6. So sánh ma sát nhớt và Coulomb

| Đặc điểm | Ma sát nhớt ($F = -b\dot{x}$) | Ma sát Coulomb ($F = \pm \mu N$) |
|---|---|---|
| Phụ thuộc biên độ | Tỉ lệ | Không phụ thuộc |
| Phương trình | Tuyến tính | Phi tuyến |
| Kiểu tắt dần | Hàm mũ, vô hạn | Tuyến tính, dừng hẳn |
| Tần số dao động | Thay đổi nhẹ ($\omega_1 < \omega_0$) | Không thay đổi |
| Phân tích | Giải tích được | Phải giải số hoặc từng nửa chu kỳ |

**Ví dụ thực tế:** Trong hệ truyền động chính xác, stiction (ma sát tĩnh Coulomb) gây ra hiện tượng "limit cycle" - hệ dao động quanh điểm đặt với biên độ nhỏ không tắt dần. Giải pháp: dither (thêm rung động nhỏ tần số cao để vượt qua ma sát tĩnh), bù ma sát feedforward, hay dùng ổ trục không ma sát (air bearing, magnetic bearing).

**Kết luận:** Tính tuyến tính của ma sát nhớt là điều kiện để áp dụng toàn bộ công cụ phân tích tần số, hàm truyền, và superposition. Đây là lý do kỹ sư điều khiển luôn cố gắng tuyến tính hóa hệ thực tế trong vùng hoạt động.

---
*Exported from Feynman Bot*
