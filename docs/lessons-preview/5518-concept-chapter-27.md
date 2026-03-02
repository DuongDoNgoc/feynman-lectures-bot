---
lesson_id: 5518
lesson_type: concept
approval_status: pending
exported_at: "2026-03-02T15:10:31.561737+00:00"
content_hash: 1c3ad952286c
chapter_number: 27
chapter_title: Chapter 27
section_number: 4
section_title: 27–3The focal length of a lens
---
# ## Thấu Kính Hai Bề Mặt: Khi Ánh Sáng Đi Qua Thuỷ Tinh

*Source: Chapter 27 - Chapter 27 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_27.html)*

## Thấu Kính Hai Bề Mặt: Khi Ánh Sáng Đi Qua Thuỷ Tinh

### Mở đầu: Tại sao kính của bạn không chỉ là một miếng thuỷ tinh phẳng?

Hãy nhìn vào chiếc kính cận hoặc kính lúp bạn đang dùng. Nó có hai bề mặt cong — không phải một. Tại sao vậy? Và làm thế nào mà hai bề mặt cong đó lại phối hợp để tạo ra ảnh rõ nét đúng chỗ bạn muốn? Đây chính là vấn đề chúng ta sẽ giải quyết hôm nay.

### Ý tưởng cốt lõi: Giải từng bề mặt một

Feynman đưa ra một nguyên tắc đẹp và thực dụng: **đừng cố giải cả hệ cùng một lúc**. Thay vào đó, hãy xử lý từng bề mặt khúc xạ một cách tuần tự.

Giả sử ánh sáng từ điểm vật $O$ đi vào thấu kính hai bề mặt. Bước đi như sau:

**Bước 1:** Áp dụng công thức khúc xạ cho bề mặt thứ nhất (bỏ qua bề mặt thứ hai hoàn toàn). Kết quả cho ta một điểm ảnh trung gian $O'$ — điểm mà ánh sáng *sẽ hội tụ hoặc phân kỳ* nếu không có bề mặt thứ hai.

**Bước 2:** Lấy $O'$ này làm điểm vật mới cho bề mặt thứ hai. Áp dụng lại công thức khúc xạ. Ta thu được điểm ảnh cuối cùng $O''$.

Đơn giản vậy thôi! Nguyên tắc này mở rộng cho bất kỳ số bề mặt nào — 5 bề mặt, 10 bề mặt — chỉ cần lặp lại cùng một công thức.

### Công thức quan trọng

Công thức tổng quát cho một bề mặt khúc xạ phân cách hai môi trường chiết suất $n_1$ và $n_2$:

$$\frac{n_1}{s} + \frac{n_2}{s'} = \frac{n_2 - n_1}{R}$$

Trong đó $s$ là khoảng cách từ vật đến bề mặt, $s'$ là khoảng cách từ bề mặt đến ảnh, $R$ là bán kính cong của bề mặt.

Đặc biệt, với thấu kính mỏng (thin lens) — khi hai bề mặt rất gần nhau đến mức ta có thể bỏ qua độ dày — công thức trở nên đặc biệt thanh lịch:

$$\frac{1}{f} = (n-1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right)$$

Đây là **phương trình lensmaker** (công thức người chế tạo thấu kính). Nó nói với bạn: tiêu cự $f$ của thấu kính phụ thuộc vào chiết suất $n$ của thuỷ tinh và hình dạng hai bề mặt ($R_1$, $R_2$).

### Phép so sánh trực quan

Hãy tưởng tượng bạn đang chơi trò truyền tin qua nhiều người. Người đầu tiên nghe tin từ nguồn $O$ và "diễn giải lại" thành tin $O'$. Người thứ hai nhận tin $O'$ và truyền tiếp thành $O''$. Mỗi người (mỗi bề mặt) chỉ biết về người trước đó — không quan tâm đến nguồn gốc ban đầu hay người phía sau. Cứ thế mà ánh sáng "truyền tin" qua từng bề mặt thuỷ tinh.

### Tại sao thấu kính mỏng lại hữu ích?

Khi hai bề mặt rất gần nhau, ta có thể cộng trực tiếp tác dụng của chúng. Vật lý học thú vị ở chỗ: dù phải chứng minh qua nhiều bước, kết quả cuối cùng lại rất đơn giản — tiêu cự chỉ phụ thuộc vào $R_1$, $R_2$, và $n$.

Với kỹ sư thiết kế hệ thống quang học, điều này có nghĩa: bạn có thể dự đoán nơi ảnh sẽ hình thành mà không cần theo dõi từng tia sáng riêng lẻ. Chỉ cần biết tiêu cự $f$, rồi dùng phương trình thấu kính:

$$\frac{1}{s} + \frac{1}{s'} = \frac{1}{f}$$

### Ý nghĩa thực tế cho kỹ sư

Nguyên lý "giải tuần tự từng bề mặt" không chỉ là mẹo toán học. Nó phản ánh cách các kỹ sư quang học hiện đại dùng phần mềm ray-tracing như Zemax hay CODE V: máy tính theo dõi từng tia sáng qua từng bề mặt một, áp dụng định luật Snell tại mỗi điểm, và tìm nơi các tia hội tụ.

Với hệ đo lường chính xác micromet, việc hiểu rõ từng bề mặt đóng góp như thế nào vào quang trình tổng thể là điều thiết yếu để đảm bảo chùm laser hội tụ đúng điểm cần đo.

### Tóm tắt

- Thấu kính hai bề mặt được xử lý bằng cách áp dụng công thức khúc xạ **tuần tự** từ bề mặt này sang bề mặt khác
- Công thức tổng quát: $\frac{n_1}{s} + \frac{n_2}{s'} = \frac{n_2 - n_1}{R}$
- Thấu kính mỏng có tiêu cự: $\frac{1}{f} = (n-1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right)$
- Nguyên tắc này mở rộng cho bất kỳ hệ quang học nhiều bề mặt nào

---
*Exported from Feynman Bot*
