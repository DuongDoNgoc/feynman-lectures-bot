---
lesson_id: 5571
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:08.241085+00:00"
content_hash: d047c932c7cb
chapter_number: 33
chapter_title: Chapter 33
section_number: 2
section_title: 33–1The electric vector of light
---
# ## Kiểm tra: Phân cực Ánh sáng

*Source: Chapter 33 - Chapter 33 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_33.html)*

## Kiểm tra: Phân cực Ánh sáng

---

**Câu 1**: Ánh sáng phân cực tròn được tạo thành khi:

A) Hai thành phần $E_x$ và $E_y$ có biên độ bằng nhau và lệch pha $180°$
B) Hai thành phần $E_x$ và $E_y$ có biên độ bằng nhau và lệch pha $90°$
C) Chỉ có một thành phần điện trường $E_x$ (theo một hướng duy nhất)
D) Hai thành phần $E_x$ và $E_y$ cùng pha nhưng biên độ khác nhau

**Đáp án: B**

*Giải thích*: Phân cực tròn đòi hỏi: (1) $E_{0x} = E_{0y}$ — biên độ bằng nhau, và (2) $\delta = \pm 90°$ — lệch pha một phần tư chu kỳ. Khi đó, vector điện trường quay đều như kim đồng hồ với tốc độ góc $\omega$. Nếu $E_{0x} 
eq E_{0y}$ hoặc $\delta 
eq 90°$ (nhưng $
eq 0°, 180°$), ta có phân cực elip.

---

**Câu 2**: Một bản bước sóng $\lambda/4$ (quarter-wave plate) có tác dụng gì khi ánh sáng phân cực tuyến tính đi qua với góc 45° so với trục nhanh?

A) Biến ánh sáng phân cực tuyến tính thành ánh sáng không phân cực
B) Biến ánh sáng phân cực tuyến tính thành ánh sáng phân cực tròn
C) Biến ánh sáng phân cực tuyến tính thành ánh sáng phân cực tuyến tính vuông góc
D) Không thay đổi trạng thái phân cực

**Đáp án: B**

*Giải thích*: Bản $\lambda/4$ tạo ra hiệu pha $\delta = 90°$ giữa thành phần song song và vuông góc với trục nhanh. Khi ánh sáng phân cực 45° đi qua, hai thành phần $E_x = E_y$ ban đầu cùng pha; sau bản $\lambda/4$, hiệu pha trở thành $90°$ và $E_x = E_y$ — đây là điều kiện chính xác của phân cực tròn. Nguyên lý này dùng trong giao thoa kế phân cực để tách tín hiệu vuông góc pha (quadrature detection).

---

**Câu 3**: Trong giao thoa kế laser phân cực dùng để đo dịch chuyển, nếu gương di động dịch chuyển $\Delta x = \lambda/8$ (một phần tám bước sóng), hiệu pha của tín hiệu giao thoa thay đổi bao nhiêu?

A) $45°$
B) $90°$
C) $180°$
D) $360°$

**Đáp án: B**

*Giải thích*: Công thức hiệu pha: $\delta = rac{4\pi\Delta x}{\lambda}$. Với $\Delta x = \lambda/8$: $\delta = rac{4\pi \cdot \lambda/8}{\lambda} = rac{4\pi}{8} = rac{\pi}{2} = 90°$. Hệ số 4 xuất hiện vì ánh sáng đi và về (nhân 2) qua gương, và $\delta$ là hiệu pha (nhân $2\pi/\lambda$ với đường đi). Điều này có nghĩa mỗi $\lambda/8$ dịch chuyển tương ứng $90°$ pha — giúp hệ thống đo với độ phân giải rất cao bằng cách nội suy pha.

---

**Câu 4 — Tự luận**: Trong thiết kế hệ thống encoder tuyến tính cho cánh tay robot phẫu thuật hoặc hệ thống định vị vũ khí chính xác, tại sao việc dùng hai kênh tín hiệu vuông góc pha (quadrature signals) lại quan trọng? Giải thích từ góc độ phân cực ánh sáng và cảm biến giao thoa.

*Gợi ý trả lời*: Tín hiệu giao thoa đơn $I = I_0[1 + \cos(\delta)]$ có vấn đề: tại $\delta = 0°$ hoặc $180°$, đạo hàm $dI/d\delta = 0$ — cảm biến mù với dịch chuyển nhỏ tại các điểm này. Dùng hai kênh lệch pha $90°$: kênh A = $\cos(\delta)$, kênh B = $\sin(\delta)$. Khi A có độ nhạy thấp (gần $\pm 1$), B có độ nhạy cao, và ngược lại. Từ $rctan(B/A)$ ta tính được $\delta$ liên tục và hướng dịch chuyển. Trong thực tế, bản $\lambda/4$ cùng với PBS tạo ra hai tín hiệu vuông góc pha này tự động.


---
*Exported from Feynman Bot*
