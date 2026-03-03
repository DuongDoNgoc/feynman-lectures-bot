---
lesson_id: 5479
lesson_type: concept
approval_status: approved
exported_at: "2026-03-03T15:33:06.052038+00:00"
content_hash: 82fa56047e00
chapter_number: 22
chapter_title: Chapter 22
section_number: 5
section_title: 22–4Approximating irrational numbers
---
# ## Lũy thừa Vô tỉ và Logarithm — Khi Số Học Gặp Giới Hạn

*Source: Chapter 22 - Chapter 22 (Section 5) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_22.html)*

## Lũy thừa Vô tỉ và Logarithm — Khi Số Học Gặp Giới Hạn

### Câu hỏi mở đầu: Máy tính của bạn tính $10^{\sqrt{2}}$ như thế nào?

Khi bạn nhập $10^{1.4142}$ vào máy tính của encoder quang học hay bộ điều khiển DSP, kết quả hiện ra gần như tức thì: $25.9946...$. Nhưng bạn có bao giờ tự hỏi: máy tính đang làm gì bên trong? $\sqrt{2} = 1.41421356...$  là một số vô tỉ — nó không bao giờ kết thúc, không bao giờ lặp lại. Vậy làm thế nào để nâng 10 lên một lũy thừa *vô tận* như vậy?

Đây không phải câu hỏi triết học — đây là câu hỏi kỹ thuật cốt lõi mà các nhà toán học thế kỷ 17 đã phải giải quyết để tạo ra bảng logarithm, tiền thân của mọi công cụ tính toán kỹ thuật số ngày nay.

### Ý tưởng cốt lõi: Xấp xỉ tuần tự

Ta đã biết tính $10^{3/4}$ (căn bậc 4 của $10^3$) hay $10^{7/5}$ (căn bậc 5 của $10^7$). Mấu chốt là: mọi lũy thừa *hữu tỉ* đều tính được bằng các phép lấy căn lặp đi lặp lại.

Với lũy thừa *vô tỉ* như $10^{\sqrt{2}}$, ý tưởng là xấp xỉ $\sqrt{2}$ bằng dãy phân số:
$$\sqrt{2} \approx 1, \; 1.4, \; 1.41, \; 1.414, \; 1.4142, \; \ldots$$

Mỗi bước xấp xỉ cho một lũy thừa hữu tỉ:
$$10^1 = 10, \quad 10^{14/10} = 10^{1.4}, \quad 10^{141/100} = 10^{1.41}, \quad \ldots$$

Dãy số này hội tụ đến một giá trị xác định. Ta *định nghĩa* giá trị đó là $10^{\sqrt{2}}$. Không có gì "thần kỳ" — chỉ là giới hạn của một dãy tính được.

### Logarithm: Bảng tra cứu thiên tài

Vì tính $10^{\sqrt{2}}$ thủ công đòi hỏi hàng nghìn bước lấy căn, các nhà toán học xây dựng **bảng logarithm** (logarithm tables): một danh sách số $x$ và giá trị $\log_{10} x$ tương ứng.

Quy tắc vàng của logarithm:
$$\log_b(ac) = \log_b a + \log_b c$$

Đây là phép **biến tích thành tổng** — phép cộng đơn giản hơn phép nhân rất nhiều. Trong thời đại trước máy tính, thủy thủ hàng hải, kỹ sư pháo binh, và nhà thiên văn dùng bảng log để nhân hai số 6 chữ số chỉ trong vài giây.

**Phép so sánh với kỹ sư cơ điện tử:** Bảng logarithm giống như bảng tra *look-up table* (LUT) trong vi điều khiển của bạn. Thay vì tính $\sin\theta$ từ đầu mỗi lần, bạn nạp sẵn giá trị vào ROM và tra cứu trong $O(1)$ thời gian. Bảng log thế kỷ 17 là LUT tương tự — pre-computed để tiết kiệm thời gian tính toán.

### Thay đổi cơ số logarithm

Không quan trọng bạn dùng cơ số nào ($10$, $e$, $2$...) — tất cả chỉ khác nhau một hằng số tỷ lệ:
$$\log_x c = \frac{\log_b c}{\log_b x}$$

Đây là lý do tại sao trong kỹ thuật ta dùng:
- $\log_{10}$ (logarithm thập phân): decibel trong âm thanh và tín hiệu — $\text{dB} = 20\log_{10}(V/V_0)$
- $\log_2$ (logarithm nhị phân): lý thuyết thông tin, mã hóa dữ liệu encoder
- $\ln = \log_e$ (logarithm tự nhiên): phương trình vi phân, điều khiển tự động

Việc chuyển đổi giữa các cơ số chỉ là nhân một hằng số — không thay đổi bản chất.

### Ứng dụng trong đo lường độ chính xác cao

Trong hệ thống đo lường laser interferometry để kiểm tra bề mặt ở độ phân giải micromet, đường cong hiệu chỉnh (calibration curve) của cảm biến thường có dạng logarithmic hoặc lũy thừa. Ví dụ, cảm biến áp suất piezoelectric có đáp ứng:
$$V_{out} = k \cdot P^\alpha$$

Để tuyến tính hóa, ta lấy logarithm hai vế:
$$\log V_{out} = \log k + \alpha \log P$$

Nhiệm vụ hiệu chỉnh trở thành bài toán hồi quy tuyến tính đơn giản — chính là ứng dụng của quy tắc $\log_b(ac) = \log_b a + \log_b c$.

**Điểm mấu chốt:**
- Lũy thừa vô tỉ $a^x$ (với $x$ vô tỉ) được định nghĩa qua giới hạn của dãy xấp xỉ hữu tỉ — không phải là khái niệm mới, chỉ là phép lấy giới hạn.
- Logarithm là phép nghịch đảo của lũy thừa: $\log_b(b^x) = x$, và biến phép nhân thành phép cộng.
- Mọi cơ số logarithm đều tương đương — chỉ khác một hằng số tỷ lệ, nên chọn cơ số nào là tùy thuận tiện.
- Trong đo lường kỹ thuật, logarithm là công cụ để tuyến tính hóa quan hệ lũy thừa, mở rộng dải động (dynamic range), và biểu diễn biên độ tín hiệu theo đơn vị dB.

---
*Exported from Feynman Bot*
