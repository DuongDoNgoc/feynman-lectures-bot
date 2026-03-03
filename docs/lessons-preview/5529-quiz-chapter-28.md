---
lesson_id: 5529
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:07.226857+00:00"
content_hash: c4fd94e55c28
chapter_number: 28
chapter_title: Chapter 28
section_number: 3
section_title: 28–2Radiation
---
# ## Kiểm Tra: Bức Xạ Điện Từ và Điện Tích Chuyển Động

*Source: Chapter 28 - Chapter 28 (Section 3) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_28.html)*

## Kiểm Tra: Bức Xạ Điện Từ và Điện Tích Chuyển Động

**Câu 1:** Trường điện của điện tích chuyển động có thành phần bức xạ giảm theo quy luật nào với khoảng cách $r$?

A) Tỉ lệ nghịch với $r^3$
B) Tỉ lệ nghịch với $r^2$
C) Tỉ lệ nghịch với $r$
D) Không phụ thuộc vào $r$

**Đáp án: C**
Giải thích: Đây là điểm mấu chốt phân biệt thành phần bức xạ (radiation field) với thành phần Coulomb. Thành phần Coulomb giảm theo $1/r^2$, nên ở khoảng cách lớn sẽ nhỏ hơn rất nhiều so với thành phần bức xạ giảm theo $1/r$. Chính sự giảm chậm theo $1/r$ này cho phép sóng điện từ truyền năng lượng đến vô cùng — đây là cơ sở vật lý của truyền thông vô tuyến và radar tầm xa.

---

**Câu 2:** Theo định luật bức xạ Feynman, điện trường bức xạ tỉ lệ với đại lượng nào của điện tích nguồn?

A) Vận tốc của điện tích
B) Vị trí của điện tích tại thời điểm quan sát
C) Gia tốc của vector đơn vị hướng từ điện tích đến điểm quan sát (tại thời điểm trễ)
D) Động năng của điện tích

**Đáp án: C**
Giải thích: Công thức Feynman $\mathbf{E} = \frac{-q}{4\pi\varepsilon_0 c^2 r} \frac{d^2\hat{e}_{r'}}{dt^2}$ cho thấy trường bức xạ phụ thuộc vào gia tốc của vector đơn vị $\hat{e}_{r'}$ — tức là cách mà "hướng nhìn" từ điểm quan sát đến điện tích thay đổi. Quan trọng: đây là gia tốc tại *thời điểm trễ* $t' = t - r/c$, không phải thời điểm hiện tại $t$.

---

**Câu 3:** Một điện tích dao động theo trục thẳng đứng. Bức xạ điện từ phát ra sẽ có cường độ tối đa theo hướng nào?

A) Dọc theo trục dao động (phía trên và phía dưới)
B) Vuông góc với trục dao động (theo phương nằm ngang)
C) Theo hướng 45° so với trục dao động
D) Đồng đều theo mọi hướng

**Đáp án: B**
Giải thích: Cường độ bức xạ tỉ lệ với $\sin^2\theta$, trong đó $\theta$ là góc giữa hướng quan sát và trục dao động. Tại $\theta = 90°$ (vuông góc): $\sin^2(90°) = 1$, cường độ cực đại. Tại $\theta = 0°$ hay $180°$ (dọc theo trục): $\sin^2(0°) = 0$, không có bức xạ. Đây là lý do anten dipole thu tín hiệu tốt nhất khi đặt vuông góc với hướng đến của sóng.

---

**Câu 4 (Tự luận):** Trong công việc thiết kế hệ thống tự động hóa và vũ khí quân sự đòi hỏi độ chính xác micro-mét, bạn thường xuyên gặp vấn đề nhiễu điện từ (EMI) từ các motor servo, bộ chuyển đổi DC-DC switching, hay mạch điều khiển xung (PWM). Dựa trên nguyên lý bức xạ của Feynman (điện tích tăng tốc thì bức xạ sóng điện từ), hãy giải thích:

a) Tại sao bộ chuyển đổi switching tần số cao lại gây ra EMI mạnh hơn so với nguồn DC thuần?
b) Tại sao dây dẫn bị uốn cong đột ngột (sharp bend) trên PCB lại là nguồn EMI tiềm tàng?
c) Đề xuất ít nhất hai giải pháp kỹ thuật để giảm EMI, giải thích cơ chế vật lý của từng giải pháp dựa trên định luật bức xạ.

**Hướng dẫn trả lời:**
a) Bộ switching tạo ra dòng điện biến đổi rất nhanh (rise time ngắn = gia tốc lớn của điện tích). Công suất bức xạ $P \propto a^2$, nên tần số switching cao hơn đồng nghĩa gia tốc của điện tích lớn hơn, EMI mạnh hơn. Nguồn DC thuần có dòng không đổi — điện tích chuyển động đều, không có gia tốc, nên không bức xạ.

b) Tại điểm uốn cong đột ngột, hướng dòng điện thay đổi trong khoảng không gian rất nhỏ — đây tương đương với gia tốc lớn theo hướng pháp tuyến. Trường bức xạ tỉ lệ với gia tốc này, nên bend sắc là nguồn EMI cục bộ. Thiết kế PCB tốt dùng arc (cung tròn) thay vì góc vuông.

c) Giải pháp 1: Tụ bypass và ferrite bead — làm chậm thay đổi dòng điện (giảm gia tốc), do đó giảm biên độ bức xạ. Giải pháp 2: Twisted pair — hai dây song song mang dòng ngược chiều nhau, trường bức xạ triệt tiêu nhau (destructive interference). Giải pháp 3: Shielding bằng vỏ kim loại — tạo màn chắn Faraday, phản xạ và hấp thụ sóng điện từ.


---
*Exported from Feynman Bot*
