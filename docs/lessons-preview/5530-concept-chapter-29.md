---
lesson_id: 5530
lesson_type: concept
approval_status: approved
exported_at: "2026-03-03T15:33:07.248171+00:00"
content_hash: 28def9564195
chapter_number: 29
chapter_title: Chapter 29
section_number: 2
section_title: 29–1Electromagnetic waves
---
# ## Trường Bức Xạ trong Không Gian: Bức Ảnh Tức Thời của Sóng Điện Từ

*Source: Chapter 29 - Chapter 29 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_29.html)*

## Trường Bức Xạ trong Không Gian: Bức Ảnh Tức Thời của Sóng Điện Từ

Tưởng tượng bạn đang kiểm tra một hệ thống servo motor với oscilloscope — màn hình hiện sóng theo trục thời gian, cho thấy tín hiệu thay đổi như thế nào tại một điểm cố định. Nhưng nếu thay vì nhìn một điểm theo thời gian, bạn chụp ảnh toàn bộ đường dây tín hiệu tại một thời điểm cố định thì sao? Bạn sẽ thấy cả một "bức tranh không gian" của sóng. Đây chính xác là cách chúng ta phân tích trường bức xạ điện từ trong chương này — không phải nhìn theo thời gian, mà nhìn một snapshot của toàn bộ không gian.

**Trường bức xạ: Từ công thức đến hình ảnh không gian**

Khi một điện tích dao động dọc theo một trục, trường điện tại khoảng cách $r$, góc $\theta$ so với trục dao động được cho bởi:

$$E(r, t) = \frac{-q \, a(t - r/c) \sin\theta}{4\pi\varepsilon_0 c^2 r}$$

Nhìn vào $a(t - r/c)$ — đây là gia tốc tại *thời điểm trễ*. Sóng điện từ mang "lịch sử" chuyển động của điện tích. Khi ta chụp snapshot toàn bộ không gian tại thời điểm $t$, tại điểm xa $r_1$ ta thấy gia tốc mà điện tích có vào lúc $t - r_1/c$; tại điểm xa hơn $r_2 > r_1$ ta thấy gia tốc của thời điểm còn xa hơn trong quá khứ $t - r_2/c$. Toàn bộ lịch sử chuyển động của điện tích được "đóng băng" trong không gian dưới dạng sóng điện từ.

**Thí nghiệm tư duy: Điện tích dao động ngắn**

Hãy hình dung điện tích ban đầu đứng yên, sau đó dao động một lúc rồi dừng lại. Snapshot không gian lúc này cho thấy:
- Gần điện tích: trường Coulomb tĩnh, giảm theo $1/r^2$
- Xa hơn: vùng trường bức xạ hình xuyến (toroidal), đại diện cho thời gian điện tích đang dao động
- Còn xa hơn nữa: lại trở về trường Coulomb tĩnh, vì ánh sáng chưa mang thông tin về sự dao động đến đây

Vùng trường bức xạ chạy ra ngoài với tốc độ ánh sáng $c$. Năng lượng bị "nhốt" trong vùng này và không bao giờ quay lại — đây là ý nghĩa của bức xạ: năng lượng thực sự thoát ra khỏi điện tích.

**Phép so sánh với hệ thống cơ điện tử**

Hãy nghĩ đến hệ thống truyền thông CAN bus trong robot tự động. Khi một node gửi một bit thông tin (dòng điện thay đổi đột ngột), xung điện chạy dọc cáp với vận tốc gần bằng tốc độ ánh sáng. Khi bạn nhìn oscilloscope đo nhiều điểm dọc cáp cùng lúc (hoặc dùng thước đo TDR — Time Domain Reflectometry), bạn thấy xung đang di chuyển — đó là snapshot không gian của thông tin đang truyền đi.

Sóng điện từ trong không gian tự do hoàn toàn tương tự, nhưng không cần cáp: điện tích dao động tạo ra "xung thông tin" lan ra theo mọi hướng với tốc độ $c = 3 \times 10^8$ m/s. Bức tranh snapshot của trường bức xạ là bức tranh của "xung thông tin" này đang lan rộng ra không gian.

**Hướng của trường bức xạ**

Một đặc điểm quan trọng: trường bức xạ $\mathbf{E}$ luôn vuông góc với đường nối điện tích đến điểm quan sát (tức là vuông góc với hướng lan truyền sóng). Đây không phải ngẫu nhiên — đây là hệ quả của phương trình Maxwell và nguyên tắc bảo toàn năng lượng. Trường $\mathbf{E}$ nằm trong mặt phẳng chứa trục dao động và đường nhìn, vuông góc với đường nhìn.

Đặc biệt hơn: trường $\mathbf{B}$ (từ trường) đi kèm luôn vuông góc với cả $\mathbf{E}$ lẫn hướng lan truyền, và $|\mathbf{B}| = |\mathbf{E}|/c$. Ba vector này tạo thành tam diện vuông góc — đây là cấu trúc của sóng điện từ phẳng.

**Phân cực (Polarization) của ánh sáng**

Sóng điện từ từ một dipole dao động theo trục $z$ sẽ có $\mathbf{E}$ luôn nằm trong mặt phẳng chứa trục $z$ — ta gọi là ánh sáng phân cực tuyến tính. Kính phân cực (polarizer) trong camera hay kính râu chỉ cho qua ánh sáng có $\mathbf{E}$ theo hướng nhất định.

Trong đo lường laser interferometry chính xác (ví dụ: hệ thống đo dịch chuyển micro-mét trong máy CNC), người ta sử dụng kính phân cực để tách và phân tích hai chùm tia, tạo ra giao thoa. Hiểu được phân cực là hiểu được cấu trúc không gian của trường bức xạ.

**Điểm mấu chốt**

- Trường bức xạ có thể nhìn nhận như snapshot không gian: tại mỗi điểm trong không gian, trường phản ánh gia tốc của điện tích tại thời điểm trễ $t - r/c$
- Hướng của trường điện $\mathbf{E}$ luôn vuông góc với hướng lan truyền sóng, nằm trong mặt phẳng chứa trục dao động và đường nhìn
- Biên độ tỉ lệ với $\sin\theta / r$: cực đại vuông góc với trục dao động, bằng không dọc trục
- Sóng điện từ mang theo "bộ nhớ" về lịch sử chuyển động của điện tích — năng lượng bức xạ một khi đã thoát ra không bao giờ quay lại điện tích nguồn

---
*Exported from Feynman Bot*
