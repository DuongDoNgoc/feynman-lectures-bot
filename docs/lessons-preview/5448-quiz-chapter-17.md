---
lesson_id: 5448
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:05.298984+00:00"
content_hash: 935227ae0e97
chapter_number: 17
chapter_title: Chapter 17
section_number: 6
section_title: 17–5Four-vector algebra
---
# ## Quiz: Four-Vectors và Ký Hiệu Không-Thời Gian

*Source: Chapter 17 - Chapter 17 (Section 6) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_17.html)*

## Quiz: Four-Vectors và Ký Hiệu Không-Thời Gian

### Câu 1 (Trắc nghiệm)

Four-vector động lượng-năng lượng $p_\mu$ trong thuyết tương đối hẹp có bao nhiêu thành phần và chúng là gì?

A. 3 thành phần: $p_x, p_y, p_z$
B. 4 thành phần: $E/c, p_x, p_y, p_z$ — trong đó $E$ là năng lượng toàn phần
C. 4 thành phần: $m, p_x, p_y, p_z$ — trong đó $m$ là khối lượng nghỉ
D. 4 thành phần: $t, x, y, z$ — tọa độ không-thời gian

**Đáp án: B**

*Giải thích:* Four-vector động lượng $p_\mu = (E/c, p_x, p_y, p_z)$. Thành phần thời gian được đồng nhất với năng lượng chia cho $c$. Đây không phải tọa độ không-thời gian (đó là four-vector vị trí $x_\mu$), cũng không phải chỉ động lượng ba chiều.

---

### Câu 2 (Trắc nghiệm)

Tích vô hướng bất biến Lorentz của four-vector $A_\mu$ được tính theo công thức nào?

A. $A_t^2 + A_x^2 + A_y^2 + A_z^2$
B. $A_t^2 - A_x^2 - A_y^2 - A_z^2$
C. $-A_t^2 + A_x^2 + A_y^2 + A_z^2$
D. $A_x^2 + A_y^2 + A_z^2 - A_t^2/c^2$

**Đáp án: B**

*Giải thích:* Metric Minkowski có dấu $(+,-,-,-)$: thành phần thời gian dương, ba thành phần không gian âm. Đây là điểm khác biệt cơ bản so với metric Euclid (mọi dấu dương). Đại lượng này bất biến nghĩa là giống nhau trong mọi hệ quy chiếu quán tính.

---

### Câu 3 (Trắc nghiệm)

Một kỹ sư thiết kế hệ thống GPS cần hiệu chỉnh sai số tương đối tính. Vệ tinh GPS bay ở vận tốc $v \approx 3.87$ km/s. Đại lượng nào **bảo toàn** (bất biến Lorentz) cho four-vector động lượng của vệ tinh?

A. Năng lượng toàn phần $E$
B. Độ lớn động lượng $|\vec{p}|$
C. Khối lượng nghỉ $m_0$ (vì $E^2/c^2 - |\vec{p}|^2 = m_0^2 c^2$)
D. Vận tốc $v$ của vệ tinh

**Đáp án: C**

*Giải thích:* Bất biến Lorentz của four-vector động lượng là $(m_0 c)^2 = E^2/c^2 - |\vec{p}|^2$. Khối lượng nghỉ $m_0$ giống nhau trong mọi hệ quy chiếu. Năng lượng $E$ và động lượng $|\vec{p}|$ riêng lẻ đều thay đổi khi chuyển hệ quy chiếu.

---

### Câu 4 (Tự luận)

Trong hệ thống đo lường laser interferometry mà bạn sử dụng cho gia công độ chính xác micrometer, ánh sáng laser có four-vector sóng $k_\mu = (\omega/c, k_x, k_y, k_z)$. Khi đầu đo chuyển động với vận tốc $v$ dọc theo hướng laser, tần số quan sát được thay đổi theo hiệu ứng Doppler tương đối tính. Hãy giải thích tại sao cần dùng four-vector (thay vì công thức Doppler phi tương đối tính) và trình bày cách tính tần số dịch chuyển cho trường hợp đầu đo chuyển động với $v = 10$ m/s trong hệ laser He-Ne ($\lambda = 633$ nm).

**Gợi ý trả lời:**

Công thức Doppler phi tương đối tính: $f' = f_0(1 \pm v/c)$ — chỉ đúng khi $v \ll c$.

Công thức Doppler tương đối tính (từ phép biến đổi Lorentz của $k_\mu$):
$$f' = f_0 \sqrt{\frac{1 \pm \beta}{1 \mp \beta}}, \quad \beta = v/c$$

Với $v = 10$ m/s, $\beta = 10/(3 \times 10^8) = 3.33 \times 10^{-8}$:
- Phi tương đối tính: $\Delta f/f_0 = \beta = 3.33 \times 10^{-8}$
- Tương đối tính: $\Delta f/f_0 = \beta + \beta^2/2 + ... \approx 3.33 \times 10^{-8}$ (sai lệch ở bậc $\beta^2 \approx 10^{-15}$, không đáng kể ở $v = 10$ m/s)

Tuy nhiên, với hệ thống đo lường tuyệt đối dùng laser ổn định tần số (frequency-stabilized laser, $\Delta f/f < 10^{-12}$), sai số tương đối tính bậc hai $\beta^2/2$ có thể cần xét đến khi đầu đo chuyển động với vận tốc cao hơn (m/s đến hàng chục m/s trong máy CNC tốc độ cao).

```json
{"questions":[{"id":"q1","type":"mcq","question":"Four-vector động lượng-năng lượng $p_\\mu$ trong thuyết tương đối hẹp có bao nhiêu thành phần và chúng là gì?","options":["A. 3 thành phần: $p_x, p_y, p_z$","B. 4 thành phần: $E/c, p_x, p_y, p_z$ — trong đó $E$ là năng lượng toàn phần","C. 4 thành phần: $m, p_x, p_y, p_z$ — trong đó $m$ là khối lượng nghỉ","D. 4 thành phần: $t, x, y, z$ — tọa độ không-thời gian"],"answer":"B","explanation":"Four-vector động lượng $p_\\mu = (E/c, p_x, p_y, p_z)$. Thành phần thời gian được đồng nhất với năng lượng chia cho $c$. Đây không phải tọa độ không-thời gian (đó là four-vector vị trí $x_\\mu$), cũng không phải chỉ động lượng ba chiều."},{"id":"q2","type":"mcq","question":"Tích vô hướng bất biến Lorentz của four-vector $A_\\mu$ được tính theo công thức nào?","options":["A. $A_t^2 + A_x^2 + A_y^2 + A_z^2$","B. $A_t^2 - A_x^2 - A_y^2 - A_z^2$","C. $-A_t^2 + A_x^2 + A_y^2 + A_z^2$","D. $A_x^2 + A_y^2 + A_z^2 - A_t^2/c^2$"],"answer":"B","explanation":"Metric Minkowski có dấu (+,-,-,-): thành phần thời gian dương, ba thành phần không gian âm. Đây là điểm khác biệt cơ bản so với metric Euclid (mọi dấu dương). Đại lượng này bất biến nghĩa là giống nhau trong mọi hệ quy chiếu quán tính."},{"id":"q3","type":"mcq","question":"Đại lượng nào bảo toàn (bất biến Lorentz) cho four-vector động lượng?","options":["A. Năng lượng toàn phần $E$","B. Độ lớn động lượng $|\\vec{p}|$","C. Khối lượng nghỉ $m_0$ (vì $E^2/c^2 - |\\vec{p}|^2 = m_0^2 c^2$)","D. Vận tốc $v$ của vật"],"answer":"C","explanation":"Bất biến Lorentz của four-vector động lượng là $(m_0 c)^2 = E^2/c^2 - |\\vec{p}|^2$. Khối lượng nghỉ $m_0$ giống nhau trong mọi hệ quy chiếu. Năng lượng $E$ và động lượng $|\\vec{p}|$ riêng lẻ đều thay đổi khi chuyển hệ quy chiếu."},{"id":"q4","type":"open","question":"Trong hệ thống đo lường laser interferometry độ chính xác micrometer, tại sao cần hiểu four-vector sóng ánh sáng $k_\\mu = (\\omega/c, k_x, k_y, k_z)$ khi tính hiệu ứng Doppler tương đối tính? Trình bày cho trường hợp đầu đo chuyển động $v = 10$ m/s.","sample_answer":"Công thức Doppler tương đối tính: $f' = f_0\\sqrt{(1\\pm\\beta)/(1\\mp\\beta)}$. Với $v=10$ m/s, $\\beta=3.33\\times10^{-8}$, sai lệch so với công thức phi tương đối tính ở bậc $\\beta^2\\approx10^{-15}$ — không đáng kể ở vận tốc này nhưng trở nên quan trọng với laser ổn định tần số ($\\Delta f/f < 10^{-12}$) hoặc khi đầu đo chuyển động nhanh hơn."}]}
```


## Quiz Questions

**Q1:** Four-vector động lượng-năng lượng $p_\mu$ trong thuyết tương đối hẹp có bao nhiêu thành phần và chúng là gì?
- A) A. 3 thành phần: $p_x, p_y, p_z$
- B) B. 4 thành phần: $E/c, p_x, p_y, p_z$ — trong đó $E$ là năng lượng toàn phần
- C) C. 4 thành phần: $m, p_x, p_y, p_z$ — trong đó $m$ là khối lượng nghỉ
- D) D. 4 thành phần: $t, x, y, z$ — tọa độ không-thời gian

**Correct:** B

**Explanation:** Four-vector động lượng $p_\mu = (E/c, p_x, p_y, p_z)$. Thành phần thời gian được đồng nhất với năng lượng chia cho $c$. Đây không phải tọa độ không-thời gian (đó là four-vector vị trí $x_\mu$), cũng không phải chỉ động lượng ba chiều.

**Q2:** Tích vô hướng bất biến Lorentz của four-vector $A_\mu$ được tính theo công thức nào?
- A) A. $A_t^2 + A_x^2 + A_y^2 + A_z^2$
- B) B. $A_t^2 - A_x^2 - A_y^2 - A_z^2$
- C) C. $-A_t^2 + A_x^2 + A_y^2 + A_z^2$
- D) D. $A_x^2 + A_y^2 + A_z^2 - A_t^2/c^2$

**Correct:** B

**Explanation:** Metric Minkowski có dấu (+,-,-,-): thành phần thời gian dương, ba thành phần không gian âm. Đây là điểm khác biệt cơ bản so với metric Euclid (mọi dấu dương). Đại lượng này bất biến nghĩa là giống nhau trong mọi hệ quy chiếu quán tính.

**Q3:** Đại lượng nào bảo toàn (bất biến Lorentz) cho four-vector động lượng?
- A) A. Năng lượng toàn phần $E$
- B) B. Độ lớn động lượng $|\vec{p}|$
- C) C. Khối lượng nghỉ $m_0$ (vì $E^2/c^2 - |\vec{p}|^2 = m_0^2 c^2$)
- D) D. Vận tốc $v$ của vật

**Correct:** C

**Explanation:** Bất biến Lorentz của four-vector động lượng là $(m_0 c)^2 = E^2/c^2 - |\vec{p}|^2$. Khối lượng nghỉ $m_0$ giống nhau trong mọi hệ quy chiếu. Năng lượng $E$ và động lượng $|\vec{p}|$ riêng lẻ đều thay đổi khi chuyển hệ quy chiếu.

**Q4:** Trong hệ thống đo lường laser interferometry độ chính xác micrometer, tại sao cần hiểu four-vector sóng ánh sáng $k_\mu = (\omega/c, k_x, k_y, k_z)$ khi tính hiệu ứng Doppler tương đối tính? Trình bày cho trường hợp đầu đo chuyển động $v = 10$ m/s.

**Correct:** N/A


---
*Exported from Feynman Bot*
