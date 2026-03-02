---
lesson_id: 5503
lesson_type: concept
approval_status: pending
exported_at: "2026-03-02T15:10:31.237330+00:00"
content_hash: 5bd4c9683c7f
chapter_number: 26
chapter_title: Chapter 26
section_number: 2
section_title: 26–1Light
---
# ## Phổ Bức Xạ Điện Từ và Quang Học Hình Học: Ánh Sáng Chỉ Là Một Phần Nhỏ

*Source: Chapter 26 - Chapter 26 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_26.html)*

## Phổ Bức Xạ Điện Từ và Quang Học Hình Học: Ánh Sáng Chỉ Là Một Phần Nhỏ

Bạn có biết rằng khi radar trên tàu chiến hay hệ dẫn đường tên lửa phóng sóng ra không gian, về bản chất nó đang dùng chính loại sóng giống với ánh sáng mà bạn đang dùng để đọc trang này không? Sóng radar và ánh sáng nhìn thấy được đều là **bức xạ điện từ** (electromagnetic radiation) - chúng chỉ khác nhau ở một thứ duy nhất: **bước sóng** (wavelength).

**Phổ bức xạ điện từ - Một dải liên tục vô tận**

Nếu chúng ta dàn trải tất cả các loại bức xạ điện từ theo bước sóng từ dài đến ngắn, chúng ta sẽ có:

- **Sóng radio:** bước sóng hàng trăm mét đến vài mét (đài AM/FM)
- **Sóng radar:** cỡ cm đến dm (dải $X, K_u, K_a$ trong radar quân sự)
- **Sóng milimét:** ~1-10 mm (radar tần số mm, cảm biến ô tô tự lái)
- **Hồng ngoại (infrared):** ~1 mm đến 700 nm (camera nhiệt, seeker tên lửa nhiệt)
- **Ánh sáng nhìn thấy:** ~400-700 nm (từ đỏ đến tím)
- **Tử ngoại (ultraviolet):** ~10-400 nm
- **Tia X:** ~$10^{-10}$ m đến $10^{-8}$ m
- **Tia gamma ($\gamma$):** ngắn hơn $10^{-10}$ m

Không có ranh giới sắc nét giữa các vùng - thiên nhiên không vẽ đường phân chia. Đây là điều Feynman nhấn mạnh: "nature did not present us with sharp edges."

**Ba chế độ xấp xỉ của điện từ học**

Đây là điểm cốt lõi mà bạn cần nắm: tùy theo mối quan hệ giữa bước sóng $\lambda$ và kích thước hệ thống $d$, ta dùng ba phương pháp khác nhau:

1. **Quang học hình học (Geometrical Optics):** khi $\lambda \ll d$
   - Bỏ qua tính chất sóng, ánh sáng đi theo tia thẳng
   - Công cụ: định luật phản xạ, khúc xạ, thấu kính, gương
   - Ứng dụng: thiết kế kính ngắm súng, hệ quang học camera

2. **Quang học sóng (Wave Optics):** khi $\lambda \sim d$
   - Phải xét hiện tượng nhiễu xạ, giao thoa
   - Công cụ: phương trình Maxwell, lý thuyết sóng điện từ
   - Ứng dụng: thiết kế anten radar (bước sóng radar $\sim$ kích thước anten)

3. **Quang học photon (Photon Optics):** khi $\lambda \ll d$ nhưng năng lượng photon lớn
   - Ánh sáng là hạt photon với năng lượng $E = h\nu$
   - Ứng dụng: tia X y tế, cảm biến photon đơn, LIDAR

**Phép so sánh với kỹ thuật radar quân sự**

Hãy nghĩ đến radar phòng không: anten radar có kích thước $d \approx 1-5$ m, bước sóng $\lambda \approx 3$ cm (băng X). Vì $\lambda \ll d$ ($3$ cm $\ll$ 1 m), ta có thể dùng quang học hình học để giải thích tại sao anten radar định hướng chùm tia theo một hướng cụ thể. Nhưng các hiệu ứng nhiễu xạ (độ phân giải góc $\theta \approx \lambda/d$) vẫn quan trọng trong tính toán độ chính xác.

Ngược lại, cảm biến radar milimét trên xe tự lái có bước sóng $\lambda \approx 4$ mm và anten nhỏ $d \approx 5$ cm, nên $\lambda/d \approx 0.08$ - hiệu ứng sóng bắt đầu đáng kể.

**Quang học hình học - Xấp xỉ hay đủ tốt?**

Feynman có một câu nói sâu sắc: quang học hình học là một trong những chương mà chúng ta sẽ phải "học lại" sau này. Đó là xấp xỉ, nhưng là xấp xỉ cực kỳ hữu ích.

Trong thiết kế hệ thống vũ khí hay thiết bị đo lường quang học của bạn, khi bạn dùng thấu kính hội tụ, gương cầu, hay prism để định hướng ánh sáng laser - bạn đang dùng quang học hình học. Và nó hoạt động tốt vì bước sóng laser ($\lambda \approx 600-1064$ nm) rất nhỏ so với kích thước các chi tiết quang học (cỡ mm đến cm).

Nhưng khi bạn cần độ chính xác cực cao - ví dụ thiết kế kính ngắm phân giải milirad hay hệ đo giao thoa laser (interferometer) để đo vị trí micrometer - thì các hiệu ứng sóng như nhiễu xạ và giao thoa không thể bỏ qua.

**Điểm mấu chốt**

- Ánh sáng nhìn thấy, sóng radar, tia X đều là bức xạ điện từ - chỉ khác bước sóng $\lambda$
- Ba chế độ xấp xỉ: hình học ($\lambda \ll d$), sóng ($\lambda \sim d$), photon (năng lượng cao)
- Quang học hình học: ánh sáng đi thẳng theo tia, hợp lệ khi $\lambda \ll$ kích thước dụng cụ
- Không có ranh giới sắc nét giữa các vùng phổ - đây là liên tục
- Việc chọn mô hình phù hợp ($\lambda$ so với $d$) là kỹ năng quan trọng của kỹ sư quang học

---
*Exported from Feynman Bot*
