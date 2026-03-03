---
lesson_id: 5380
lesson_type: concept
approval_status: approved
exported_at: "2026-03-03T15:33:03.601623+00:00"
content_hash: 04e914819f6d
chapter_number: 10
chapter_title: Chapter 10
section_number: 5
section_title: 10–4Momentum and energy
---
# ## Va Chạm Đàn Hồi và Bật Lại

*Source: Chapter 10 - Chapter 10 (Section 5) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_10.html)*

## Va Chạm Đàn Hồi và Bật Lại

Bạn đã bao giờ thắc mắc tại sao quả bóng thép nảy gần như hoàn toàn trên nền thép, trong khi quả bóng cao su nảy ít hơn? Hay tại sao trong thiết kế vũ khí, đạn nổ (exploding bullet) phân tán năng lượng khác hẳn đạn cứng? Câu trả lời nằm ở sự khác biệt giữa **va chạm đàn hồi** và **va chạm không đàn hồi**.

---

### Hai loại va chạm

**Va chạm hoàn toàn không đàn hồi:** hai vật dính vào nhau sau va chạm. Động lượng bảo toàn; động năng **không** bảo toàn — một phần biến thành nhiệt, biến dạng.

**Va chạm đàn hồi:** hai vật bật ra sau va chạm, **cả động lượng và động năng đều bảo toàn**. Đây là trường hợp lý tưởng — trong thực tế, các vật rắn cứng (thép, bi-a bi thủy tinh) gần đạt tiêu chuẩn này.

---

### Cơ chế vật lý: Lò xo trong va chạm

Feynman mô tả: ngay cả vật "cứng" khi va chạm cũng trải qua giai đoạn **nén đàn hồi** — như lò xo bị ép. Năng lượng được lưu trữ trong biến dạng đàn hồi, rồi được giải phóng khi hai vật phân ly. Nếu quá trình nén-giãn hoàn toàn thuận nghịch → va chạm đàn hồi. Nếu có biến dạng dư, nhiệt độ tăng, âm thanh → một phần năng lượng mất → va chạm không đàn hồi.

---

### Công thức va chạm đàn hồi 1D

Cho hai vật $m_1$ (vận tốc $v_1$) và $m_2$ (vận tốc $v_2$) va chạm đàn hồi:

$$v_1' = \frac{m_1 - m_2}{m_1 + m_2}v_1 + \frac{2m_2}{m_1 + m_2}v_2$$

$$v_2' = \frac{2m_1}{m_1 + m_2}v_1 + \frac{m_2 - m_1}{m_1 + m_2}v_2$$

Các trường hợp đặc biệt:
- $m_1 = m_2$: vật 1 dừng, vật 2 lấy toàn bộ vận tốc của vật 1 (hiện tượng bi-a).
- $m_1 \gg m_2$: vật nặng hầu như không thay đổi, vật nhẹ bật ngược với $\approx 2v_1$.
- $m_1 \ll m_2$: vật nhẹ bật ngược với tốc độ gần như không đổi (quả bóng nảy tường).

---

### Phép so sánh: Đầu đo tiếp xúc trong CMM

Đầu đo kiểu tiếp xúc (touch probe) trong máy đo tọa độ hoạt động như va chạm đàn hồi: đầu ruby chạm bề mặt, biến dạng cơ học kích hoạt ngắt tín hiệu, rồi đầu đo bật trở về (spring-loaded). Độ hồi phục đàn hồi của đầu đo quyết định độ lặp lại (repeatability) của phép đo — thường $< 1\,\mu\text{m}$. Đây là ứng dụng va chạm đàn hồi điều khiển ở cấp micromet.

---

**Điểm mấu chốt:**

- Va chạm đàn hồi bảo toàn cả $p$ và $KE$; va chạm không đàn hồi chỉ bảo toàn $p$.
- Cơ chế đàn hồi: năng lượng lưu trữ trong biến dạng thuận nghịch.
- Khi $m_1 = m_2$: hoán đổi vận tốc hoàn toàn (hiện tượng lý thú nhất trong va chạm đàn hồi).
- Ứng dụng: đầu đo CMM, khớp nối lò xo, kiểm tra hệ số phục hồi đàn hồi (coefficient of restitution) vật liệu.


---
*Exported from Feynman Bot*
