---
lesson_id: 5485
lesson_type: concept
approval_status: approved
exported_at: "2026-03-02T15:10:30.777608+00:00"
content_hash: 53c153157ca1
chapter_number: 23
chapter_title: Chapter 23
section_number: 2
section_title: 23–1Complex numbers and harmonic motion
---
# ## Dao động Điều hòa Cưỡng bức và Phương pháp Số Phức

*Source: Chapter 23 - Chapter 23 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_23.html)*

## Dao động Điều hòa Cưỡng bức và Phương pháp Số Phức

### Câu hỏi mở đầu: Tại sao cầu Millennium rung mạnh khi người đi bộ?

Năm 2000, cầu Millennium ở London rung dữ dội ngay sau khai trương phải đóng cửa sửa chữa. Người đi bộ bước vô tình với tần số trùng với tần số tự nhiên của cầu — hiện tượng cộng hưởng (resonance) xuất hiện. Tương tự, trong hệ thống vũ khí của bạn: một ổ đạn dẫn đường bị rung cộng hưởng do động cơ tên lửa có thể phá hủy cảm biến IMU. Làm thế nào ta tính toán và thiết kế hệ thống để tránh cộng hưởng? Câu trả lời nằm ở **dao động điều hòa cưỡng bức** (forced harmonic oscillation) và công cụ số phức.

### Ý tưởng cốt lõi: Biểu diễn số phức cho dao động

Phương trình dao động cưỡng bức:
$$\frac{d^2x}{dt^2} + \frac{k}{m}x = \frac{F_0}{m}\cos\omega t$$

Trong đó $k/m = \omega_0^2$ là bình phương tần số tự nhiên, $F_0$ là biên độ lực cưỡng bức, và $\omega$ là tần số lực cưỡng bức.

**Thủ thuật then chốt:** Thay vì giải trực tiếp với $\cos\omega t$, ta viết:
$$\cos\omega t = \text{Re}\left\{e^{i\omega t}\right\}$$

Rồi giả sử lực phức $\hat{F}e^{i\omega t}$ và tìm nghiệm phức $\hat{x}e^{i\omega t}$. Nghiệm thực là phần thực của nghiệm phức.

**Tại sao thủ thuật này hoạt động?** Vì phương trình vi phân tuyến tính — nếu phần thực và phần ảo của $\hat{F}e^{i\omega t}$ cùng thỏa mãn phương trình độc lập (do tính tuyến tính), ta có thể giải cho phần phức rồi lấy phần thực.

**Phép so sánh với kỹ sư cơ điện tử:** Thủ thuật này giống hệt việc dùng phasor trong phân tích mạch AC. Thay vì giải phương trình vi phân RLC phức tạp với $\cos\omega t$, bạn dùng impedance phức $Z = R + j\omega L + 1/(j\omega C)$ và giải phương trình đại số đơn giản hơn nhiều. Số phức biến vi phân thành nhân $j\omega$ — một phép thần kỳ.

### Biểu diễn số phức trong mặt phẳng phức

Số phức $a = x + iy$ có thể biểu diễn ở hai dạng:
- **Dạng Đề-các:** $a = x + iy$ (thuận tiện cộng/trừ)
- **Dạng cực:** $a = re^{i\theta}$ với $r = \sqrt{x^2+y^2}$, $\theta = \arctan(y/x)$ (thuận tiện nhân/chia)

Quan hệ: $x = r\cos\theta$, $y = r\sin\theta$.

Lực cưỡng bức có pha trễ $\Delta$ viết gọn:
$$F_0\cos(\omega t - \Delta) = \text{Re}\left\{F_0 e^{-i\Delta} \cdot e^{i\omega t}\right\} = \text{Re}\left\{\hat{F} e^{i\omega t}\right\}$$

Trong đó phasor $\hat{F} = F_0 e^{-i\Delta}$ chứa đầy đủ biên độ và pha — một số phức duy nhất thay cho toàn bộ hàm theo thời gian!

Hai công thức quan trọng nhất:
$$x + iy = re^{i\theta} \quad \text{(Euler)}$$
$$e^{i\omega t} = \cos\omega t + i\sin\omega t$$

### Tại sao lại dùng cơ số $e$ thay vì $10$?

Hàm mũ $e^{x}$ là hàm duy nhất không thay đổi khi đạo hàm: $\frac{d}{dt}e^{i\omega t} = i\omega e^{i\omega t}$. Trong phương trình vi phân, đạo hàm bậc 2 của $e^{i\omega t}$ là $(i\omega)^2 e^{i\omega t} = -\omega^2 e^{i\omega t}$ — tức là chỉ nhân một số. Phương trình vi phân biến thành phương trình đại số!

### Ứng dụng: Phân tích hệ thống hấp thụ dao động

Trong hệ thống giảm chấn động (vibration damping) cho bệ súng tự hành (self-propelled howitzer), kỹ sư cần tìm tần số nguy hiểm — tần số cộng hưởng của bệ pháo. Dùng phương pháp số phức:
1. Đo hàm đáp ứng tần số (Frequency Response Function — FRF): $H(\omega) = \hat{x}/\hat{F}$ (phức)
2. Tìm tần số $\omega$ mà $|H(\omega)|$ đạt cực đại — đó là tần số cộng hưởng
3. Thiết kế bộ hấp thụ dao động (dynamic vibration absorber) lệch tần số cộng hưởng đi

Toàn bộ quy trình này hoạt động trong không gian số phức.

**Điểm mấu chốt:**
- Dao động cưỡng bức $F_0\cos\omega t$ được biểu diễn là phần thực của $F_0 e^{i\omega t}$ — một số phức.
- Nghiệm phức $\hat{x}e^{i\omega t}$ của phương trình vi phân cho nghiệm thực bằng cách lấy phần thực.
- Phasor $\hat{F} = F_0 e^{-i\Delta}$ chứa đầy đủ thông tin biên độ + pha trong một số phức duy nhất.
- Thủ thuật số phức biến bài toán vi phân thành bài toán đại số — đây là nền tảng của phân tích tần số, biểu đồ Bode, và toàn bộ lý thuyết điều khiển tự động hiện đại.

---
*Exported from Feynman Bot*
