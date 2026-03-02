---
lesson_id: 5480
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-02T15:10:30.602965+00:00"
content_hash: f5f79972cd25
chapter_number: 22
chapter_title: Chapter 22
section_number: 5
section_title: 22–4Approximating irrational numbers
---
# ## Lũy thừa Vô tỉ, Logarithm và Đổi Cơ số — Phân tích Chuyên sâu

*Source: Chapter 22 - Chapter 22 (Section 5) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_22.html)*

## Lũy thừa Vô tỉ, Logarithm và Đổi Cơ số — Phân tích Chuyên sâu

### Vấn đề căn bản: Khi số học thông thường không đủ

Chúng ta đã biết cách tính $10^2 = 100$, $10^{1/2} = \sqrt{10} \approx 3.162$, hay $10^{7/4} = \sqrt[4]{10^7}$. Nhưng $10^{\sqrt{2}}$ thì sao? Số $\sqrt{2} = 1.41421356...$ là số vô tỉ — không bao giờ kết thúc. Feynman đặt câu hỏi này và trả lời bằng một chiến lược xấp xỉ tuần tự rất thực tế.

### Phương pháp xấp xỉ lũy thừa vô tỉ

Bước nền tảng: ta đã biết từ đại số:
$$a^s \cdot a^t = a^{s+t}, \quad (a^s)^t = a^{st}$$

Vì $\sqrt{2} = 1.41421356...$, ta xấp xỉ bằng dãy số hữu tỉ hội tụ đến $\sqrt{2}$:

| Xấp xỉ | Phân số | Lũy thừa |
|--------|---------|----------|
| $1$ | $1/1$ | $10^1 = 10$ |
| $1.4$ | $14/10$ | $10^{14/10} = 10^{7/5} = \sqrt[5]{10^7} \approx 25.119$ |
| $1.41$ | $141/100$ | $10^{141/100} = \sqrt[100]{10^{141}} \approx 25.704$ |
| $1.414$ | $1414/1000$ | $10^{1414/1000} \approx 25.929$ |
| $1.4142$ | $14142/10000$ | $10^{14142/10000} \approx 25.9946$ |

Dãy này hội tụ đến $10^{\sqrt{2}} \approx 25.9946...$

**Ý nghĩa vật lý của phương pháp này:** Mỗi bước xấp xỉ là một giá trị *tính được chính xác* bằng phép lấy căn hữu hạn. Ta đang "leo" đến giá trị giới hạn bằng các bước nhỏ hơn và nhỏ hơn.

### Tại sao cần bảng logarithm?

Tính $10^{141/100}$ thủ công đòi hỏi lấy căn bậc 100 của $10^{141}$ — gần như bất khả thi. Giải pháp lịch sử: xây dựng bảng logarithm bằng cách tính trước các giá trị:

$$10^{1/2} \approx 3.16228$$
$$10^{1/4} \approx 1.77828$$
$$10^{1/8} \approx 1.33352$$
$$\vdots$$

Khi cần $10^{\sqrt{2}}$, thay vì tính từ đầu, ta dùng tính chất:
$$10^{\sqrt{2}} = 10^{1+0.4+0.01+0.004+\ldots} = 10^1 \cdot 10^{4/10} \cdot 10^{1/100} \cdot 10^{4/1000} \cdots$$

Tra bảng từng thừa số rồi nhân lại — hiệu quả hơn nhiều.

### Quy tắc vàng và chứng minh

**Định lý logarithm:**
$$\log_b(ac) = \log_b a + \log_b c$$

**Chứng minh:**
Gọi $\log_b a = p$ và $\log_b c = q$. Theo định nghĩa:
$$b^p = a \quad \text{và} \quad b^q = c$$

Nhân hai phương trình:
$$b^p \cdot b^q = ac \implies b^{p+q} = ac$$

Lấy logarithm cơ số $b$ hai vế:
$$\log_b(ac) = p + q = \log_b a + \log_b c \quad \square$$

*Ý nghĩa:* Phép nhân trở thành phép cộng — đây là nguyên lý hoạt động của thước log (slide rule), công cụ tính toán của kỹ sư trước thời máy tính.

### Đổi cơ số logarithm: Công thức và ứng dụng

**Công thức đổi cơ số:**
$$\log_x c = \frac{\log_b c}{\log_b x}$$

**Chứng minh:** Gọi $\log_b x = t$, tức là $b^t = x$, suy ra $x = b^t$.

Gọi $\log_x c = a'$, tức là $x^{a'} = c$, hay $(b^t)^{a'} = b^{ta'} = c$.

Nhưng $b^{\log_b c} = c$, nên $ta' = \log_b c$, suy ra:
$$a' = \log_x c = \frac{\log_b c}{t} = \frac{\log_b c}{\log_b x}$$

Kết luận quan trọng: mọi bảng logarithm chỉ cần một cơ số duy nhất. Muốn chuyển sang cơ số khác, nhân toàn bộ bảng với hằng số $1/\log_b x$.

### Ví dụ thực tế: Dải động của cảm biến quang học

Cảm biến quang học (photodetector) trong hệ thống đo lường laser interferometry thường có dải động (dynamic range) 60–80 dB. Đơn vị dB được định nghĩa:
$$\text{dB} = 20 \log_{10}\left(\frac{V}{V_0}\right)$$

Đây chính là ứng dụng trực tiếp của $\log_{10}$. Khi bạn nói "cảm biến có SNR là 60 dB", nghĩa là:
$$\frac{V_{signal}}{V_{noise}} = 10^{60/20} = 10^3 = 1000$$

Lũy thừa hữu tỉ $10^{60/20} = 10^3$ tính được trực tiếp. Nhưng nếu SNR = 63.5 dB thì sao?
$$\frac{V}{V_0} = 10^{63.5/20} = 10^{3.175}$$

Đây là lũy thừa vô tỉ (3.175 = 63.5/20, nhưng trong thực tế thường là số thập phân không kết thúc). Tra bảng log: $10^{0.175} \approx 1.496$, nên $10^{3.175} \approx 1496$.

### Ứng dụng trong hiệu chỉnh cảm biến lực

Cảm biến lực (force sensor) dùng trong hệ thống gia công micro (micro-machining) thường có đáp ứng phi tuyến dạng lũy thừa:
$$F_{measured} = k \cdot F_{actual}^\alpha$$

Trong đó $\alpha \approx 0.95$ (gần tuyến tính nhưng không hoàn toàn). Kỹ sư cần đảo ngược:
$$F_{actual} = \left(\frac{F_{measured}}{k}\right)^{1/\alpha} = \left(\frac{F_{measured}}{k}\right)^{1.0526...}$$

Nếu $\alpha = 0.95 = 19/20$, thì $1/\alpha = 20/19$ là số hữu tỉ — tính được bằng căn số. Nhưng nếu $\alpha$ được xác định từ thực nghiệm và là số vô tỉ, ta phải dùng logarithm:
$$\ln F_{actual} = \frac{1}{\alpha}(\ln F_{measured} - \ln k)$$

VI điều khiển (MCU) trong hệ thống thực hiện phép tính này bằng hàm `log()` và `exp()` — về bản chất là triển khai bảng LUT kết hợp nội suy, giống hệt ý tưởng của Feynman.

### Bài tập mẫu: Hiệu chỉnh encoder logarithmic

**Đề bài:** Một encoder góc (angular encoder) cho hệ thống định vị vũ khí có đáp ứng:
$$\theta_{output} = 1000 \cdot \log_{10}(\theta_{input} + 1) \text{ (đơn vị: counts)}$$

với $\theta_{input}$ tính bằng arcsecond (1° = 3600 arcseconds). Nếu encoder đọc được 2500 counts, góc thực bằng bao nhiêu arcsecond?

**Lời giải từng bước:**

**Bước 1:** Đặt phương trình từ giá trị đã biết.
$$2500 = 1000 \cdot \log_{10}(\theta + 1)$$

*Ý nghĩa:* Ta đang đảo ngược hàm hiệu chỉnh để tìm đầu vào thực.

**Bước 2:** Chia hai vế cho 1000.
$$\log_{10}(\theta + 1) = 2.5$$

**Bước 3:** Lấy lũy thừa 10 hai vế (đảo ngược logarithm).
$$\theta + 1 = 10^{2.5}$$

**Bước 4:** Tính $10^{2.5}$.
$$10^{2.5} = 10^{5/2} = \sqrt{10^5} = \sqrt{100000} \approx 316.228$$

*Đây là lũy thừa hữu tỉ (mũ = 5/2), nên tính được bằng căn bậc hai.*

**Bước 5:** Tìm $\theta$.
$$\theta = 316.228 - 1 = 315.228 \text{ arcseconds} \approx 0.0875°$$

*Ý nghĩa kỹ thuật:* Điều này tương đương độ chính xác định vị $\pm 1$ arcsecond ≈ $\pm 4.85$ microradian — hoàn toàn trong tầm của hệ thống servo chính xác cao.

**Điểm mấu chốt:**
- Lũy thừa vô tỉ được định nghĩa qua giới hạn xấp xỉ hữu tỉ — có thể tính đến bất kỳ độ chính xác nào.
- Bảng logarithm là "look-up table" lịch sử — tiền thân của mọi hàm `log()` trong phần mềm nhúng ngày nay.
- Công thức $\log_b(ac) = \log_b a + \log_b c$ biến nhân thành cộng — cơ sở của đơn vị dB trong đo lường.
- Đổi cơ số logarithm chỉ là nhân hằng số — giải thích vì sao $\ln$, $\log_{10}$, $\log_2$ đều tương đương về mặt bản chất.

---
*Exported from Feynman Bot*
