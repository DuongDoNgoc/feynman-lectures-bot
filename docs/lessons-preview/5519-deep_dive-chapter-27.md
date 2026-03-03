---
lesson_id: 5519
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:07.037700+00:00"
content_hash: 4e2576f5a755
chapter_number: 27
chapter_title: Chapter 27
section_number: 4
section_title: 27–3The focal length of a lens
---
# ## Thấu Kính Hai Bề Mặt: Phân Tích Chuyên Sâu

*Source: Chapter 27 - Chapter 27 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_27.html)*

## Thấu Kính Hai Bề Mặt: Phân Tích Chuyên Sâu

### 1. Bài toán cơ bản và chiến lược giải

Xét một thấu kính thực tế có hai bề mặt cầu với bán kính cong $R_1$ và $R_2$, vật liệu thuỷ tinh chiết suất $n_2$ nằm giữa hai môi trường chiết suất $n_1$ (thường là không khí, $n_1 = 1$). Điểm vật $O$ nằm ở khoảng cách $s$ trước thấu kính. Chúng ta muốn tìm điểm ảnh $O''$.

**Chiến lược của Feynman:** Thay vì giải hệ phức tạp, ta chia bài toán thành hai bài toán đơn giản hơn, áp dụng tuần tự:

- **Bài toán 1:** Bề mặt thứ nhất (không khí → thuỷ tinh), tìm ảnh trung gian $O'$
- **Bài toán 2:** Bề mặt thứ hai (thuỷ tinh → không khí), lấy $O'$ làm vật, tìm ảnh cuối $O''$

### 2. Chứng minh công thức tổng quát

Cho bề mặt khúc xạ phân cách hai môi trường $n_1$ và $n_2$, ta xuất phát từ **nguyên lý Fermat** (principle of least time).

Xét tia sáng từ $O$ đến điểm $P$ trên bề mặt rồi đến $O'$. Gọi $h$ là khoảng cách từ $P$ đến trục quang. Sử dụng xấp xỉ paraxial ($h \ll s, s'$):

Thời gian đi từ $O$ đến $P$: $t_1 = \frac{n_1}{c}\sqrt{s^2 + h^2} \approx \frac{n_1}{c}\left(s + \frac{h^2}{2s}\right)$

Thời gian đi từ $P$ đến $O'$: $t_2 = \frac{n_2}{c}\left(s' + \frac{h^2}{2s'}\right)$

Độ dày thuỷ tinh tại điểm $P$ so với đỉnh bề mặt: $T(h) \approx \frac{h^2}{2R}$

Để tất cả các tia từ $O$ đến $O'$ mất cùng thời gian (điều kiện hội tụ hoàn hảo), ta cần:

$$\frac{n_1}{c}\left(s + \frac{h^2}{2s}\right) + \frac{n_2}{c}\left(s' + \frac{h^2}{2s'}\right) - \frac{(n_2 - n_1)}{c}\frac{h^2}{2R} = \text{hằng số}$$

Các số hạng chứa $h^2$ phải triệt tiêu nhau:

$$\frac{n_1}{2s} + \frac{n_2}{2s'} = \frac{n_2 - n_1}{2R}$$

Suy ra công thức tổng quát:

$$\boxed{\frac{n_1}{s} + \frac{n_2}{s'} = \frac{n_2 - n_1}{R}}$$

### 3. Áp dụng cho thấu kính mỏng (thin lens)

Với thấu kính có bề dày $T$ rất nhỏ ($T \to 0$), ta áp dụng công thức trên hai lần:

**Bề mặt 1** (không khí $n_1 = 1$ → thuỷ tinh $n_2 = n$, bán kính $R_1$):
$$\frac{1}{s} + \frac{n}{s_1'} = \frac{n-1}{R_1} \quad (1)$$

**Bề mặt 2** (thuỷ tinh $n$ → không khí $1$, bán kính $R_2$). Vật cho bề mặt 2 là ảnh từ bề mặt 1, khoảng cách vật $= -s_1'$ (dấu âm vì $O'$ nằm bên phải bề mặt 1, trở thành vật ảo cho bề mặt 2 khi $T \to 0$):
$$\frac{n}{-s_1'} + \frac{1}{s'} = \frac{1-n}{R_2} \quad (2)$$

Cộng (1) và (2):
$$\frac{1}{s} + \frac{1}{s'} = (n-1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right)$$

Khi $s \to \infty$, thì $s' = f$ (tiêu cự), do đó:
$$\boxed{\frac{1}{f} = (n-1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right)}$$

Đây là **lensmaker's equation** — phương trình căn bản của thiết kế thấu kính.

### 4. Phân tích năng lực hội tụ (optical power)

Định nghĩa **optical power** (công suất quang học): $P = 1/f$ (đơn vị: diopter = $\text{m}^{-1}$)

Khi ghép nhiều thấu kính mỏng đặt tiếp xúc nhau: $P_{tổng} = P_1 + P_2 + \ldots$

Tức là: $\frac{1}{f_{tổng}} = \frac{1}{f_1} + \frac{1}{f_2}$

Đây là kết quả trực tiếp từ việc áp dụng tuần tự công thức khúc xạ.

### 5. Ví dụ thực tế: Thiết kế hệ quang học cho sensor đo vị trí micromet

Trong các hệ thống đo lường chính xác (precision measurement systems) như confocal displacement sensors hay chromatic confocal sensors, kỹ sư cơ điện tử cần thiết kế hệ thấu kính hội tụ chùm laser vào vùng đo nhỏ nhất có thể.

**Bài toán cụ thể:** Thiết kế objective lens hội tụ laser $\lambda = 635$ nm có đường kính chùm $D = 5$ mm vào điểm hội tụ cách thấu kính $f = 10$ mm.

**Bước 1:** Chọn vật liệu thuỷ tinh BK7 ($n = 1.515$ ở 635 nm)

**Bước 2:** Dùng lensmaker's equation với thấu kính lồi-phẳng ($R_2 \to \infty$):
$$\frac{1}{f} = (1.515 - 1)\frac{1}{R_1} \Rightarrow R_1 = 0.515 \times 10 = 5.15 \text{ mm}$$

**Bước 3:** Kiểm tra xấp xỉ paraxial: $h_{max}/f = 2.5/10 = 0.25$ — hơi lớn, cần xét aberration (sẽ thảo luận ở bài tiếp theo).

**Bước 4:** Với thiết kế thực tế, có thể dùng doublet (hai thấu kính ghép) để giảm spherical aberration, với $f_1 = 8$ mm (thuỷ tinh crown) và $f_2 = -40$ mm (thuỷ tinh flint), cho $f_{tổng} \approx 10$ mm.

### 6. Quy ước dấu và bẫy thường gặp

Một nguồn nhầm lẫn phổ biến là quy ước dấu cho $R$. Feynman dùng quy ước:
- $R > 0$: tâm cong nằm về phía ánh sáng đến (bề mặt lõm đối với ánh sáng)
- $R < 0$: tâm cong nằm về phía ánh sáng đi (bề mặt lồi thông thường)

Nhưng nhiều sách dùng quy ước ngược! Kỹ sư cần xác định rõ quy ước dấu trước khi tính toán.

### 7. Giới hạn của mô hình

Toàn bộ phân tích trên chỉ đúng cho **paraxial rays** — tia gần trục quang. Khi tia sáng xa trục (tức là lỗ khẩu thấu kính lớn), các bậc cao hơn trong khai triển $\sin\theta \approx \theta$ không thể bỏ qua, và ta phải xét đến **aberrations** — một chủ đề quan trọng sẽ được thảo luận trong bài tiếp theo.

### Tóm tắt các công thức then chốt

| Công thức | Ý nghĩa |
|-----------|----------|
| $\frac{n_1}{s} + \frac{n_2}{s'} = \frac{n_2-n_1}{R}$ | Bề mặt khúc xạ đơn |
| $\frac{1}{f} = (n-1)\left(\frac{1}{R_1}-\frac{1}{R_2}\right)$ | Phương trình lensmaker |
| $\frac{1}{s} + \frac{1}{s'} = \frac{1}{f}$ | Phương trình thấu kính mỏng |
| $P = P_1 + P_2$ | Ghép thấu kính tiếp xúc |

---
*Exported from Feynman Bot*
