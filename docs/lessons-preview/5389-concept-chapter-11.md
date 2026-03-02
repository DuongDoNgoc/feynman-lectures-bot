---
lesson_id: 5389
lesson_type: concept
approval_status: approved
exported_at: "2026-03-02T15:10:28.202851+00:00"
content_hash: 551e6c18ace1
chapter_number: 11
chapter_title: Chapter 11
section_number: 7
section_title: 11–6Newton’s laws in vector notation
---
# ## Định luật Newton Dạng Vectơ và Vectơ Gia tốc

*Source: Chapter 11 - Chapter 11 (Section 7) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_11.html)*

## Định luật Newton Dạng Vectơ và Vectơ Gia tốc

Khi một drone bay theo quỹ đạo cong, tốc độ của nó có thể không đổi — nhưng gia tốc vẫn khác không. Điều này có vẻ mâu thuẫn, nhưng thực ra chỉ cần hiểu đúng **vectơ gia tốc**. Gia tốc không chỉ là "thay đổi tốc độ" mà là "thay đổi vectơ vận tốc" — bao gồm cả thay đổi hướng.

### Vectơ Gia tốc — Định nghĩa Chính xác

Vận tốc $\mathbf{v}$ là đạo hàm của vectơ vị trí $\mathbf{r}$ theo thời gian. Gia tốc là đạo hàm của vận tốc:

$$\mathbf{a} = \frac{d\mathbf{v}}{dt} = \frac{d^2\mathbf{r}}{dt^2}$$

Theo thành phần:

$$a_x = \frac{d^2x}{dt^2}, \quad a_y = \frac{d^2y}{dt^2}, \quad a_z = \frac{d^2z}{dt^2}$$

Từ đó định luật Newton viết gọn thành một phương trình vectơ:

$$m\mathbf{a} = \mathbf{F}$$

Hay tương đương: $m\dfrac{d^2\mathbf{r}}{dt^2} = \mathbf{F}$

### Gia tốc Theo Quỹ đạo Cong

Khi vật chuyển động trên đường cong, vectơ vận tốc thay đổi **cả độ lớn lẫn hướng**. Hiệu hai vectơ vận tốc tại hai thời điểm liên tiếp $\Delta\mathbf{v} = \mathbf{v}_2 - \mathbf{v}_1$ có hai thành phần:

- **Gia tốc tiếp tuyến** $a_\parallel = dv/dt$: thay đổi tốc độ (độ lớn)
- **Gia tốc pháp tuyến** $a_\perp = v^2/R$: thay đổi hướng, hướng vào tâm cong bán kính $R$

$$a_{\perp} = v\frac{d\theta}{dt} = \frac{v^2}{R}$$

### Phép So Sánh: Hệ Điều Khiển Servo

Trong vòng lặp điều khiển vận tốc (velocity loop), bộ điều khiển PID liên tục tính:

$$\mathbf{a}_{cmd} = K_p(\mathbf{v}_{ref} - \mathbf{v}_{actual})$$

Đây chính là gia tốc vectơ: hiệu của hai vectơ vận tốc. Khi robot chạy theo đường tròn với tốc độ không đổi, $\mathbf{a}_{cmd}$ luôn hướng vào tâm — gia tốc hướng tâm (centripetal). Motor phải liên tục tạo lực hướng tâm dù tốc độ không thay đổi.

**Sai lầm phổ biến:** Lập trình vòng điều khiển chỉ bù sai số tốc độ **độ lớn**, bỏ qua thay đổi hướng → sai số bám (tracking error) khi chạy đường cong cao tốc.

### Ưu Điểm của Ký Hiệu Vectơ

Trước khi có ký hiệu vectơ, mỗi bài toán phải viết ba phương trình riêng. Bây giờ:

$$m\mathbf{a} = \mathbf{F}$$

Một phương trình này **chứa cả ba** và đúng trong **mọi hệ tọa độ**. Khi giải bài toán trong hệ tọa độ cực $(r, \theta)$ hay hệ hình trụ, ta chỉ cần biểu diễn $\mathbf{a}$ và $\mathbf{F}$ theo hệ tọa độ đó — phương trình vectơ không thay đổi.

### Điểm Mấu Chốt

- **Gia tốc** = đạo hàm của **vectơ vận tốc** — thay đổi cả độ lớn lẫn hướng
- **Gia tốc hướng tâm** $a_\perp = v^2/R$ tồn tại dù tốc độ không đổi
- **$m\mathbf{a} = \mathbf{F}$** là một phương trình thay thế ba, đúng mọi hệ tọa độ
- Trong điều khiển chuyển động, bỏ qua thành phần hướng của gia tốc gây sai số bám

---
*Exported from Feynman Bot*
