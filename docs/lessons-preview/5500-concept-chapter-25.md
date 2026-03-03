---
lesson_id: 5500
lesson_type: concept
approval_status: approved
exported_at: "2026-03-03T15:33:06.628125+00:00"
content_hash: 4a6bb3db1677
chapter_number: 25
chapter_title: Chapter 25
section_number: 4
section_title: 25–3Oscillations in linear systems
---
# ## Vật Lý Dao Động Nhìn Từ Góc Độ Trực Quan: Tắt Dần Hàm Mũ

*Source: Chapter 25 - Chapter 25 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_25.html)*

## Vật Lý Dao Động Nhìn Từ Góc Độ Trực Quan: Tắt Dần Hàm Mũ

Bạn đã bao giờ nhìn vào màn hình oscilloscope sau khi ngắt nguồn kích thích của một hệ cơ khí và tự hỏi: tại sao biên độ giảm dần theo một quy luật trơn tru như vậy, không phải tuyến tính mà là theo dạng "đuôi" ngày càng hẹp lại? Câu trả lời là: hệ đó đang suy giảm theo hàm mũ - và đây là điều tự nhiên nhất có thể xảy ra với một hệ dao động tuyến tính.

**Tại sao hệ lại dao động?**

Hãy quên toán học đi một lúc. Hãy nghĩ đến một con lắc đơn giản: lò xo và quả nặng. Tại sao nó dao động? Đây là hệ quả của **quán tính** (inertia).

Kéo quả nặng ra, lò xo kéo nó về vị trí cân bằng. Nhưng khi đến vị trí cân bằng, vật không thể dừng đột ngột - nó đang mang theo **động lượng** (momentum). Vì vậy nó tiếp tục đi qua vị trí cân bằng, lò xo lại kéo ngược lại, và chu kỳ cứ thế tiếp diễn. Không có ma sát? Dao động mãi mãi. Có ma sát? Biên độ giảm dần từng chu kỳ.

**Loại ma sát quyết định kiểu tắt dần**

Đây là điểm mấu chốt mà Feynman muốn nhấn mạnh: **không phải loại ma sát nào cũng tạo ra sự tắt dần đẹp (exponential decay)**.

Hãy tưởng tượng một loại ma sát đặc biệt, được "thiết kế" sao cho lực ma sát luôn tỉ lệ với vận tốc của vật:

$$F_{\text{ma sát}} = -\gamma m v = -\gamma m \frac{dx}{dt}$$

Với loại ma sát này, điều kỳ diệu xảy ra: khi biên độ dao động nhỏ dần, lực ma sát cũng nhỏ dần theo **cùng tỉ lệ**. Lực lò xo cũng nhỏ hơn, gia tốc cũng nhỏ hơn, và lực ma sát cũng nhỏ hơn một cách hoàn toàn tương xứng.

Kết quả là: mỗi chu kỳ, biên độ giảm đi **cùng một tỉ lệ phần trăm**, bất kể biên độ hiện tại lớn hay nhỏ.

**Tại sao điều đó dẫn đến hàm mũ?**

Đây là lập luận vật lý đơn giản nhưng sâu sắc. Giả sử sau mỗi chu kỳ, biên độ còn lại 90% so với trước. Thì:
- Chu kỳ 1: $A_0$
- Chu kỳ 2: $0.9 A_0$
- Chu kỳ 3: $0.81 A_0 = (0.9)^2 A_0$
- Chu kỳ $n$: $A_n = A_0 \cdot (0.9)^n$

Nghĩa là biên độ bằng $A = A_0 a^n$ với $a = 0.9$ và $n$ là số chu kỳ. Vì $n \propto t$, ta có thể viết $a^n = e^{n\ln a} = e^{-ct}$ với $c$ là hằng số dương. Kết quả:

$$A(t) = A_0 e^{-\gamma t/2}$$

Và nghiệm đầy đủ kết hợp dao động với suy giảm:

$$x(t) = A_0 e^{-\gamma t/2} \cos(\omega_0 t + \phi)$$

**Phép so sánh với kỹ thuật đo lường**

Hãy nghĩ đến bộ lọc RC trong mạch điện của thiết bị đo lường của bạn. Khi ngắt nguồn, tụ điện xả qua điện trở theo quy luật $V(t) = V_0 e^{-t/RC}$ - hoàn toàn tương tự với dao động tắt dần! Đây không phải ngẫu nhiên: cả hai đều là hệ tuyến tính với "ma sát" tỉ lệ với "vận tốc" (trong mạch RC là dòng điện tỉ lệ với điện áp qua điện trở). Hằng số thời gian $\tau = RC$ trong mạch điện tương đương với $\tau = 2/\gamma$ trong dao động cơ học.

**Khi ma sát không "lý tưởng"**

Ma sát Coulomb (ma sát khô, hằng số) lại khác hoàn toàn. Lực ma sát không thay đổi theo biên độ, nên khi vật chuyển động, mỗi chu kỳ biên độ giảm đi **một lượng cố định** (không phải tỉ lệ cố định). Phương trình không còn tuyến tính, và phải giải số. Đây là lý do vì sao bài toán "simple" trong kỹ thuật thực tế (như hệ truyền động với ma sát Coulomb) lại khó hơn nhiều so với mô hình lý tưởng với ma sát nhớt.

**Điểm mấu chốt**

- Hệ dao động vì quán tính: vật không thể dừng đột ngột tại vị trí cân bằng
- Ma sát nhớt (tỉ lệ vận tốc) tạo ra suy giảm hàm mũ vì mỗi chu kỳ biên độ giảm theo cùng một tỉ lệ
- Nghiệm: $x(t) = A_0 e^{-\gamma t/2} \cos(\omega_0 t + \phi)$ - dao động cosine nhân với bao hàm mũ
- Tần số cộng hưởng $\omega_0$ không thay đổi nhiều khi có cản nhỏ
- Ma sát Coulomb (hằng số) phá vỡ tính tuyến tính và phải giải bằng phương pháp số

---
*Exported from Feynman Bot*
