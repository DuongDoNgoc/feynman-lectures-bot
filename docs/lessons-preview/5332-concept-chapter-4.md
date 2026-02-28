---
lesson_id: 5332
lesson_type: concept
approval_status: approved
exported_at: "2026-02-28T14:08:58.960804+00:00"
content_hash: 7feb05f1f715
chapter_number: 4
chapter_title: Chapter 4
section_number: 4
section_title: 4–3Kinetic energy
---
# ## Động Năng: Khi Chuyển Động Trở Thành Năng Lượng

*Source: Chapter 4 - Chapter 4 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_04.html)*

## Động Năng: Khi Chuyển Động Trở Thành Năng Lượng

Bạn đã bao giờ thắc mắc tại sao một con lắc đơn có thể tiếp tục dao động mãi mà không cần thêm năng lượng bên ngoài (trong điều kiện lý tưởng)? Hay tại sao một flywheel đang quay trong động cơ servo lại cần lực phanh rất lớn để dừng lại? Câu trả lời nằm ở một dạng năng lượng đặc biệt: **động năng** (kinetic energy).

### Con Lắc — Ví Dụ Kinh Điển Về Chuyển Hóa Năng Lượng

Hãy hình dung một con lắc đơn: một quả cầu treo trên dây. Khi kéo quả cầu lên một bên rồi thả ra, điều gì xảy ra?

- Ở vị trí cao nhất: quả cầu đứng yên, mọi năng lượng ở dạng **thế năng hấp dẫn** $U = mgh$
- Xuống đến điểm thấp nhất: quả cầu chuyển động nhanh nhất, thế năng biến mất — nhưng nó đi đâu?
- Lại lên đến độ cao ban đầu: quả cầu dừng lại, mọi năng lượng quay lại dạng thế năng

Năng lượng không tự sinh ra hay mất đi — nó chuyển hóa. Khi thế năng giảm, một dạng năng lượng khác xuất hiện để bù vào. Đó chính là **động năng** — năng lượng của chuyển động.

### Công Thức Động Năng

Công thức cho động năng được Feynman dẫn xuất từ nguyên lý máy thuận nghịch:

$$KE = \frac{1}{2}mv^2$$

Trong đó:
- $m$ = khối lượng của vật (kg)
- $v$ = vận tốc tại thời điểm đó (m/s)

Đây là công thức đơn giản nhưng cực kỳ mạnh mẽ. Lưu ý rằng động năng tỷ lệ với **bình phương** vận tốc — tăng vận tốc gấp đôi sẽ tăng động năng lên **4 lần**.

### Bảo Toàn Năng Lượng — Nguyên Lý Nền Tảng

Tổng năng lượng cơ học của con lắc được bảo toàn:

$$E_{total} = KE + PE = \frac{1}{2}mv^2 + mgh = \text{const}$$

Đây là một trong những định luật quan trọng nhất của vật lý. Ở bất kỳ vị trí nào trong quá trình dao động, tổng này luôn bằng nhau.

### Góc Nhìn Kỹ Sư Cơ Điện Tử

Trong hệ thống tự động hóa và servo, động năng là khái niệm sống còn khi thiết kế hệ thống điều khiển:

**Flywheel và quán tính quay**: Một rotor động cơ servo đang quay ở $v = r\omega$ có động năng $KE = \frac{1}{2}I\omega^2$ (với $I$ là mô men quán tính). Khi cần dừng khẩn cấp, toàn bộ động năng này phải được tiêu tán — qua phanh điện tử (regenerative braking) hoặc điện trở xả. Nếu tính toán sai, hệ thống có thể hỏng cơ học.

**Đạn và vũ khí**: Trong thiết kế vũ khí, động năng $KE = \frac{1}{2}mv^2$ của đạn quyết định khả năng xuyên giáp. Tăng vận tốc đầu đạn từ 800 m/s lên 1600 m/s sẽ tăng động năng lên 4 lần — đây là lý do đạn sabot tốc độ cao có khả năng xuyên phá lớn hơn rất nhiều so với đạn nổ thông thường.

**Phép so sánh với encoder**: Con lắc dao động giống như encoder đang đọc vị trí — ở điểm cực biên (vị trí cao nhất), vận tốc = 0, thông tin vị trí rõ ràng nhất; ở điểm giữa (vị trí thấp nhất), vận tốc cực đại, encoder phải đọc nhanh nhất. Hệ điều khiển servo phải xử lý cả hai trạng thái này một cách linh hoạt.

### Ứng Dụng Thực Tế: Cân Bằng Năng Lượng Trong Hệ Servo

Khi thiết kế hệ thống cánh tay robot với servo motor:
1. **Tăng tốc** → motor cung cấp năng lượng, chuyển hóa thành động năng của cánh tay
2. **Duy trì tốc độ** → chỉ cần bù ma sát
3. **Giảm tốc** → động năng phải được hấp thụ, dùng regenerative braking để thu hồi

Tính toán chính xác KE giúp chọn đúng công suất motor và kích thước resistor xả.

---

**Điểm mấu chốt:**
- Động năng $KE = \frac{1}{2}mv^2$ là năng lượng của chuyển động
- Con lắc minh họa sự chuyển hóa qua lại liên tục giữa thế năng và động năng
- Tổng $KE + PE$ được bảo toàn trong hệ không có ma sát
- Trong kỹ thuật, việc tính đúng động năng quyết định thiết kế hệ thống phanh, servo, và vũ khí

---
*Exported from Feynman Bot*
