---
lesson_id: 5622
lesson_type: quiz
approval_status: pending
exported_at: "2026-03-03T15:33:09.275191+00:00"
content_hash: 91d93daa7283
chapter_number: 37
chapter_title: Chapter 37
section_number: 7
section_title: 37–6Watching the electrons
---
# ## Quiz: Quan Sát Electron và Nguyên Lý Bổ Sung

*Source: Chapter 37 - Chapter 37 (Section 7) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_37.html)*

## Quiz: Quan Sát Electron và Nguyên Lý Bổ Sung

### Câu 1 (MCQ)

Trong thí nghiệm hai khe electron có nguồn sáng để theo dõi which-path, khi bước sóng ánh sáng $\lambda_{	ext{light}}$ rất lớn so với khoảng cách hai khe $d$ ($\lambda_{	ext{light}} \gg d$):

**A.** Vân giao thoa hoàn toàn biến mất vì photon năng lượng thấp không thể tán xạ từ electron.

**B.** Vân giao thoa vẫn xuất hiện vì ánh sáng không đủ độ phân giải để phân biệt electron đi khe nào.

**C.** Electron bị hút về phía nguồn sáng, phân bố thay đổi không theo quy luật nào.

**D.** Vân giao thoa biến mất vì photon bước sóng dài mang nhiều năng lượng hơn, làm rối electron mạnh hơn.

**Đáp án: B**

*Giải thích:* Độ phân giải không gian của ánh sáng $\sim \lambda_{	ext{light}}$. Khi $\lambda_{	ext{light}} \gg d$, ta không thể phân biệt chớp sáng ở khe 1 hay khe 2 — không có "which-path information". Photon bước sóng dài thực ra mang ít năng lượng hơn ($E = hc/\lambda$) và truyền xung động lượng nhỏ hơn, nên ít làm nhiễu electron hơn. Kết quả: giao thoa được bảo toàn.

---

### Câu 2 (MCQ)

Biểu thức toán học nào đúng nhất mô tả nguyên lý bổ sung (complementarity principle) dưới dạng định lượng?

**A.** $\mathcal{V} + \mathcal{D} = 1$ (tổng visibility và distinguishability bằng 1)

**B.** $\mathcal{V}^2 + \mathcal{D}^2 \leq 1$ (tổng bình phương không vượt quá 1)

**C.** $\mathcal{V} 	imes \mathcal{D} = \hbar/2$ (tích bằng hằng số Planck rút gọn)

**D.** $\mathcal{V} = \mathcal{D}$ (luôn bằng nhau)

**Đáp án: B**

*Giải thích:* Đây là bất đẳng thức bổ sung tổng quát do Englert và Wootters-Zurek chứng minh: $\mathcal{V}^2 + \mathcal{D}^2 \leq 1$. Đẳng thức xảy ra khi nguồn photon hoàn toàn thuần nhất (pure state). Không thể đồng thời có $\mathcal{V} = 1$ (giao thoa hoàn hảo) và $\mathcal{D} = 1$ (phân biệt khe hoàn hảo).

---

### Câu 3 (MCQ)

Trong thí nghiệm "quantum eraser": sau khi đặt phân cực $0°$ và $90°$ trước hai khe (vân giao thoa biến mất), ta đặt thêm phân cực $45°$ trước detector. Điều gì xảy ra?

**A.** Không có gì thay đổi — thông tin which-path đã bị ghi vào electron vĩnh viễn.

**B.** Trong tập con các sự kiện mà photon liên đới cũng đi qua phân cực $45°$, vân giao thoa xuất hiện trở lại.

**C.** Vân giao thoa xuất hiện trở lại cho tất cả các electron, kể cả những electron đến trước khi đặt phân cực $45°$.

**D.** Phân cực $45°$ làm tăng gấp đôi số electron đến detector.

**Đáp án: B**

*Giải thích:* Phân cực $45°$ không phân biệt photon phân cực $0°$ hay $90°$ — cả hai đều có xác suất $50\%$ đi qua. Bằng cách chọn lọc (post-selection) chỉ các sự kiện mà photon liên đới truyền qua phân cực $45°$, ta "xóa" thông tin which-path trong tập con đó. Vân giao thoa xuất hiện trong tập con này. Quan trọng: ta không thể dùng điều này để truyền thông tin nhanh hơn ánh sáng vì cần tương quan với photon (đòi hỏi kênh thông tin cổ điển).

---

### Câu 4 (Câu hỏi mở)

**Trong hệ thống điều khiển servo chính xác cao, "back-action" là một vấn đề thực tế: khi sensor đo vị trí của đối tượng, sensor ảnh hưởng ngược lại lên đối tượng, gây nhiễu. Dựa trên phân tích thí nghiệm electron có quan sát:**

**(a)** Phân tích tương đồng giữa "photon tán xạ từ electron" trong thí nghiệm Feynman và "back-action noise" của sensor quang học trong hệ servo. Điểm tương đồng và khác biệt cụ thể là gì?

**(b)** Standard Quantum Limit (SQL) cho sensor vị trí liên tục là $\Delta x_{	ext{SQL}} = \sqrt{\hbar	au/m}$. Tính $\Delta x_{	ext{SQL}}$ cho một thanh silicon MEMS ($m = 1$ ng $= 10^{-12}$ kg) trong vòng lặp điều khiển $	au = 10$ μs. So sánh với độ chính xác nm-level của hệ servo thông thường — giới hạn SQL có thực sự quan trọng ở đây không?

**(c)** Kỹ thuật "back-action evasion" (BAE) dùng "squeezed states" để nén bất định vị trí xuống dưới SQL ở một chiều, chấp nhận tăng bất định ở chiều kia (vẫn thỏa $\Delta x \cdot \Delta p \geq \hbar/2$). Giải thích tại sao điều này khả thi về mặt nguyên lý và áp dụng được cho hệ thống nào trong kỹ thuật cơ điện tử thực tế?

**Gợi ý trả lời:**

(a) Điểm tương đồng: cả hai đều truyền năng lượng/động lượng vào hệ được đo. Sự khác biệt: trong thí nghiệm lượng tử, back-action là căn bản và không thể tránh (nguyên lý bất định); trong hệ servo cổ điển, back-action có thể giảm bằng thiết kế sensor tốt hơn. Tuy nhiên ở giới hạn lượng tử, chúng hợp nhất.

(b) $\Delta x_{	ext{SQL}} = \sqrt{1.055	imes10^{-34} 	imes 10^{-5} / 10^{-12}} = \sqrt{1.055	imes10^{-27}} pprox 3.25	imes10^{-14}$ m $pprox 32$ fm. Độ chính xác nm-level là $10^{-9}$ m, lớn hơn SQL $\sim 10^5$ lần → SQL chưa quan trọng ở đây. Chỉ quan trọng với MEMS siêu nhẹ ($\sim$ fg) và thời gian đo dài trong thiết bị gravitational wave detector.

(c) Squeezed states: phân phối bất định trong không gian phase $(x, p)$ được nén thành hình elip thay vì hình tròn. Áp dụng thực tế: LIGO dùng squeezed light để giảm shot noise xuống dưới SQL ở tần số cao. Trong MEMS: squeezed mechanical states đã được tạo ra trong lab nhưng chưa ứng dụng công nghiệp.


---
*Exported from Feynman Bot*
