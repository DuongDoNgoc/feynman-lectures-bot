---
lesson_id: 5568
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:08.181190+00:00"
content_hash: 7ef7040b8c50
chapter_number: 32
chapter_title: Chapter 32
section_number: 6
section_title: 32–5Scattering of light
---
# ## Kiểm tra: Tán xạ Rayleigh và Bầu Trời Xanh

*Source: Chapter 32 - Chapter 32 (Section 6) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_32.html)*

## Kiểm tra: Tán xạ Rayleigh và Bầu Trời Xanh

---

**Câu 1**: Theo định luật Rayleigh, cường độ ánh sáng tán xạ bởi các phân tử khí tỉ lệ với:

A) $\lambda^4$
B) $1/\lambda^2$
C) $1/\lambda^4$
D) $1/\lambda$

**Đáp án: C**

*Giải thích*: Điện tử dao động với gia tốc $a \propto \omega^2 x_0$, và cường độ bức xạ $I \propto a^2 \propto \omega^4$. Vì $\omega = 2\pi c/\lambda$, ta có $I \propto 1/\lambda^4$. Đây chính là lý do ánh sáng xanh (bước sóng ngắn) bị tán xạ mạnh hơn ánh sáng đỏ.

---

**Câu 2**: Tại sao trong chất khí ngẫu nhiên, cường độ tán xạ tổng cộng bằng N lần cường độ tán xạ của một nguyên tử (thay vì $N^2$ lần như trong trường hợp giao thoa cùng pha)?

A) Vì các nguyên tử khí không tán xạ ánh sáng
B) Vì các nguyên tử chuyển động nhiệt làm pha tương đối thay đổi ngẫu nhiên, các số hạng giao thoa triệt tiêu trung bình
C) Vì ánh sáng trong khí quyển không phải ánh sáng kết hợp (coherent)
D) Vì tần số cộng hưởng của các nguyên tử khác nhau hoàn toàn

**Đáp án: B**

*Giải thích*: Khi các nguyên tử phân bố ngẫu nhiên và chuyển động nhiệt, pha tương đối giữa hai nguyên tử bất kỳ liên tục thay đổi. Các số hạng giao thoa $\cos(\Delta\phi)$ trung bình thời gian bằng 0. Kết quả: $I_{tổng} = N \cdot I_{1}$, không có giao thoa xây dựng hay phá hủy.

---

**Câu 3**: Một cảm biến lidar sử dụng hai bước sóng laser: $\lambda_1 = 355\,	ext{nm}$ (UV) và $\lambda_2 = 1064\,	ext{nm}$ (IR). Tỉ lệ cường độ tán xạ Rayleigh $I_{UV}/I_{IR}$ xấp xỉ bằng:

A) 3
B) 30
C) 100
D) 1000

**Đáp án: C**

*Giải thích*: $I_{UV}/I_{IR} = (\lambda_2/\lambda_1)^4 = (1064/355)^4 pprox (3)^4 = 81 pprox 100$. Tính chính xác: $(2.996)^4 pprox 80.5$. Đáp án C (100) gần nhất. Đây là lý do tại sao hệ thống lidar UV rất nhạy trong đo mật độ khí quyển, nhưng hệ thống IR lại phù hợp hơn để xuyên qua mây/sương (ít tán xạ hơn).

---

**Câu 4 — Tự luận**: Trong thiết kế hệ thống cảm biến quang học cho ứng dụng đo lường chính xác (ví dụ: đo độ sạch phòng sạch trong sản xuất thiết bị vi điện tử quân sự, hoặc hệ thống lidar nhắm mục tiêu), bạn sẽ chọn bước sóng laser như thế nào để tối ưu hóa độ nhạy trong điều kiện nồng độ hạt thấp, và bước sóng nào để tối ưu hóa khả năng xuyên qua khói/sương? Giải thích dựa trên nguyên lý tán xạ Rayleigh.

*Gợi ý trả lời*: Để tối ưu độ nhạy (phát hiện hạt nhỏ ở mật độ thấp): chọn bước sóng ngắn (UV/xanh lam, 355–450 nm) vì $I \propto 1/\lambda^4$ — tín hiệu tán xạ mạnh hơn nhiều. Nhược điểm: bị suy hao nhanh trong môi trường nhiều hạt. Để xuyên qua khói/sương (ứng dụng quân sự, dẫn đường): chọn IR (1–10 µm) vì tán xạ Rayleigh yếu, sóng IR ít bị tán xạ bởi các hạt nhỏ. Đây là lý do các thiết bị ngắm nhiệt (thermal imaging) hoạt động tốt trong khói chiến trường — không phụ thuộc vào tán xạ Rayleigh mà dùng bức xạ nhiệt.


---
*Exported from Feynman Bot*
