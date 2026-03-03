---
lesson_id: 5566
lesson_type: concept
approval_status: approved
exported_at: "2026-03-03T15:33:08.136716+00:00"
content_hash: 4c4854ff29af
chapter_number: 32
chapter_title: Chapter 32
section_number: 6
section_title: 32–5Scattering of light
---
# ## Tán Xạ Rayleigh: Tại Sao Bầu Trời Xanh và Hoàng Hôn Đỏ?

*Source: Chapter 32 - Chapter 32 (Section 6) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_32.html)*

## Tán Xạ Rayleigh: Tại Sao Bầu Trời Xanh và Hoàng Hôn Đỏ?

Bạn đã bao giờ hỏi: tại sao bầu trời ban ngày có màu xanh, nhưng khi mặt trời lặn lại chuyển sang đỏ và cam? Và tại sao mặt trời nhìn thẳng lại vàng, trong khi ánh sáng nó phát ra thực chất là trắng? Câu trả lời nằm trong một cơ chế gọi là **tán xạ Rayleigh** - và nó giải thích cho cả những ứng dụng quan trọng trong thiết kế hệ thống quang học.

### Nguyên Lý: Ánh Sáng Làm Nguyên Tử "Nhảy" Và Tái Bức Xạ

Khi ánh sáng đi qua không khí, điện trường của sóng điện từ làm electron trong các nguyên tử (N$_2$, O$_2$) dao động lên xuống. Những electron đang dao động này chính là các "antenna" nhỏ - chúng bức xạ lại ánh sáng theo mọi hướng.

Nhưng không phải mọi nguyên tử đều tái bức xạ theo cùng hướng. Nếu các nguyên tử được sắp xếp hoàn hảo theo một mạng tinh thể đều đặn, ánh sáng tái bức xạ từ mọi nguyên tử sẽ **giao thoa hủy nhau** ở tất cả các hướng trừ hướng tới - kết quả là chùm sáng tiếp tục đi thẳng (đây là nguồn gốc của chỉ số khúc xạ trong chất rắn kết tinh).

Nhưng trong **khí**, các nguyên tử phân bố **ngẫu nhiên** và chuyển động hỗn loạn. Pha của ánh sáng tái bức xạ từ các nguyên tử khác nhau cũng ngẫu nhiên. Kết quả: **không có giao thoa hủy** - và ta phải cộng cường độ (chứ không phải biên độ) từ mỗi nguyên tử. Tổng cường độ tán xạ bằng N lần cường độ tán xạ từ một nguyên tử đơn lẻ.

### Sự Phụ Thuộc Vào Tần Số: $\omega^4$ Quyết Định Màu Sắc Bầu Trời

Một nguyên tử bị ánh sáng kích thích dao động và tái bức xạ năng lượng. Cường độ tán xạ từ một nguyên tử đơn lẻ tuân theo:

$$I_{\text{tán xạ}} \propto \omega^4$$

Đây là hệ quả trực tiếp của công thức Larmor: công suất bức xạ tỉ lệ với $\omega^4$. Ánh sáng tần số cao (màu xanh, $\lambda \approx 450\,\text{nm}$, $\omega$ lớn) bị tán xạ mạnh hơn ánh sáng tần số thấp (màu đỏ, $\lambda \approx 700\,\text{nm}$, $\omega$ nhỏ) theo tỉ lệ:

$$\frac{I_{\text{xanh}}}{I_{\text{đỏ}}} = \left(\frac{\omega_{\text{xanh}}}{\omega_{\text{đỏ}}}\right)^4 = \left(\frac{700}{450}\right)^4 \approx 5.6$$

Ánh sáng xanh bị tán xạ mạnh gấp **5.6 lần** ánh sáng đỏ! Khi bạn nhìn bầu trời theo bất kỳ hướng nào không phải hướng mặt trời, bạn đang thấy ánh sáng tán xạ - chủ yếu là màu xanh.

### Tại Sao Hoàng Hôn Đỏ?

Lúc mặt trời lặn, ánh sáng phải xuyên qua **lớp khí quyển dày hơn nhiều** (vì góc xiên). Trong hành trình dài đó, phần lớn ánh sáng xanh đã bị tán xạ ra tứ phía và không còn đến mắt bạn nữa. Chỉ còn lại ánh sáng đỏ và cam (tần số thấp, tán xạ ít) tiếp tục đi thẳng đến mắt bạn. Kết quả: mặt trời lặn có màu đỏ.

### Phép So Sánh Với Hệ Thống Đo Lường Chính Xác

Là kỹ sư làm việc với thiết bị đo lường chính xác cao, bạn gặp hiệu ứng này trong thực tế. Hãy xét **LIDAR** (Light Detection and Ranging) hoặc **laser rangefinder** quân sự:

Khi bắn chùm laser qua khí quyển, một phần năng lượng bị tán xạ Rayleigh ra các hướng khác - đây là **tổn thất tín hiệu** và nguồn gốc của **clutter** (nhiễu nền). Tổn thất này tỉ lệ thuận với $\omega^4$, nên:
- **Laser hồng ngoại** (1064 nm) bị tán xạ ít hơn laser xanh lá (532 nm) khoảng $(532/1064)^4 = 1/16$ lần
- Đây là lý do LIDAR xa tầm (long-range) thường dùng bước sóng hồng ngoại dài, còn lidar độ phân giải cao ngắn tầm mới dùng bước sóng ngắn hơn

Ngược lại, hệ thống **LIDAR đo mật độ khí quyển** (meteorological lidar) có thể tận dụng chính sự tán xạ Rayleigh này để đo mật độ không khí theo độ cao - cường độ tán xạ ngược (backscatter) tỉ lệ với số nguyên tử $N$, vì vậy đo $I_{\text{backscatter}}$ cho biết $N(h)$ theo độ cao $h$.

### Điểm Mấu Chốt

- Khí có nguyên tử phân bố ngẫu nhiên, nên ánh sáng bị tán xạ theo mọi hướng mà không giao thoa hủy
- Cường độ tán xạ Rayleigh tỉ lệ với **$\omega^4$** - tần số cao bị tán xạ mạnh hơn nhiều
- Bầu trời xanh và hoàng hôn đỏ là biểu hiện thực tế nhất của tán xạ Rayleigh trong cuộc sống
- Trong kỹ thuật quang học và LIDAR, hiểu $\omega^4$ giúp chọn bước sóng tối ưu để cân bằng giữa tổn thất tán xạ và độ phân giải của hệ thống

---
*Exported from Feynman Bot*
