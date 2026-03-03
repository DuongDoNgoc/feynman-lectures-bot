---
lesson_id: 5549
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:07.702264+00:00"
content_hash: 9ea7d8794033
chapter_number: 30
chapter_title: Chapter 30
section_number: 7
section_title: 30–6Diffraction by opaque screens
---
# ## Chuyên Sâu: Nhiễu Xạ Fresnel — Toán Học Và Ứng Dụng Đo Lường Chính Xác

*Source: Chapter 30 - Chapter 30 (Section 7) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_30.html)*

## Chuyên Sâu: Nhiễu Xạ Fresnel — Toán Học Và Ứng Dụng Đo Lường Chính Xác

### 1. Từ Huygens Đến Fresnel: Nền Tảng Lý Thuyết

Nguyên lý Huygens (1678) phát biểu: mỗi điểm trên mặt sóng là một nguồn sóng thứ cấp hình cầu. Fresnel (1818) bổ sung yếu tố **giao thoa** giữa các nguồn thứ cấp này, tạo ra lý thuyết nhiễu xạ hoàn chỉnh. Công thức tích phân Huygens-Fresnel cho trường điện tại điểm quan sát $P$:

$$E(P) = \frac{-i}{\lambda} \iint_{\text{aperture}} E_0(Q) \frac{e^{ikr}}{r} K(\theta) \, dS$$

Trong đó:
- $r$ = khoảng cách từ điểm nguồn thứ cấp $Q$ đến điểm quan sát $P$
- $k = 2\pi/\lambda$ = số sóng
- $K(\theta)$ = hệ số nghiêng (inclination factor), xấp xỉ 1 với góc nhỏ
- Tích phân thực hiện trên diện tích khẩu độ mở

### 2. Gần Đúng Fresnel: Khai Triển Pha Bậc Hai

Gọi $z$ là khoảng cách từ khẩu độ đến màn quan sát (dọc theo trục quang học), $(x, y)$ là tọa độ trên khẩu độ, $(X, Y)$ là tọa độ trên màn. Khoảng cách thực:

$$r = \sqrt{z^2 + (X-x)^2 + (Y-y)^2} \approx z + \frac{(X-x)^2 + (Y-y)^2}{2z}$$

Gần đúng này (giữ đến bậc hai) chính là **gần đúng Fresnel**, hợp lệ khi:
$$\frac{\pi}{4\lambda z^3}\left[(X-x)^2 + (Y-y)^2\right]^2_{\max} \ll 1$$

Khi gần đúng này áp dụng, tích phân nhiễu xạ trở thành:

$$E(X,Y) = \frac{e^{ikz}}{i\lambda z} e^{i\frac{k}{2z}(X^2+Y^2)} \iint_{\text{aperture}} E_0(x,y)\, e^{i\frac{k}{2z}(x^2+y^2)} e^{-i\frac{k}{z}(Xx+Yy)} dx\, dy$$

Đây là **tích phân Fresnel** — khác với Fraunhofer ở chỗ giữ thêm số hạng bậc hai $e^{i\frac{k}{2z}(x^2+y^2)}$ bên trong tích phân.

### 3. Trường Hợp 1D: Rìa Dao Và Tích Phân Fresnel

Xét ánh sáng nhiễu xạ qua rìa thẳng (half-plane). Bài toán rút gọn về 1 chiều. Định nghĩa biến không thứ nguyên:

$$u = x\sqrt{\frac{2}{\lambda z}}$$

Cường độ tại điểm quan sát $X$ trên màn:

$$I(X) = \frac{I_0}{2}\left[\left(C(u_2) - C(u_1)\right)^2 + \left(S(u_2) - S(u_1)\right)^2\right]$$

Trong đó $C(u)$ và $S(u)$ là **tích phân Fresnel**:

$$C(u) = \int_0^u \cos\left(\frac{\pi t^2}{2}\right)dt, \qquad S(u) = \int_0^u \sin\left(\frac{\pi t^2}{2}\right)dt$$

Các hàm này không có dạng giải tích đóng, phải tính số. Giới hạn: $C(\infty) = S(\infty) = 1/2$.

### 4. Đường Cong Cornu (Cornu Spiral)

Vẽ đường cong tham số $(C(u), S(u))$ trong mặt phẳng phức — ta được **xoắn ốc Cornu** (Cornu spiral), xoắn vào hai điểm cực $(\pm 1/2, \pm 1/2)$. Ý nghĩa hình học:

- Biên độ trường tại $X$ tỉ lệ với **độ dài dây cung** nối hai điểm trên xoắn ốc
- Pha của trường là **góc nghiêng** của dây cung đó
- Cường độ $I \propto$ (độ dài dây cung)$^2$

Kết quả quan trọng:
- **Chính giữa bóng tối** ($u_2 = 0$, $u_1 \to -\infty$): $I = I_0/4$
- **Trong vùng sáng xa rìa**: $I \approx I_0$ (nhưng dao động nhẹ)
- **Cực đại thứ nhất bên ngoài bóng**: $I \approx 1.37 I_0$ — sáng hơn ánh sáng không nhiễu xạ!

### 5. Nguyên Lý Babinet Và Điểm Poisson-Arago

Xét hai vật chắn bổ sung: tấm chắn có lỗ (khẩu độ $A$) và đĩa chắn đặc (đĩa $B$ vừa che lỗ đó). Vì tổng trường bằng trường tự do:

$$E_A + E_B = E_{\text{không chắn}}$$

Nếu nguồn và màn đủ xa (điều kiện Fraunhofer) và bỏ qua tia thẳng thẳng: $|E_A|^2 = |E_B|^2$, tức là **hoa văn nhiễu xạ cường độ của tấm chắn lỗ và đĩa chắn giống hệt nhau**.

Hệ quả kỳ lạ: một đĩa tròn đặc nhỏ sẽ tạo ra **điểm sáng tại chính giữa bóng tối**. Poisson cho rằng điều này vô lý để bác bỏ lý thuyết sóng của Fresnel năm 1818, nhưng Arago đã kiểm chứng thực nghiệm ngay lập tức — điểm sáng Poisson/Arago có thật!

**Tại sao?** Tất cả sóng nhiễu xạ vòng quanh đĩa có cùng khoảng cách đến tâm bóng, nên chúng đến tâm **đồng pha** và cộng hưởng xây dựng (constructive interference).

### 6. Ứng Dụng Thực Tế: Kiểm Soát Khẩu Độ Trong Hệ Đo Micro-Mét

Ví dụ cụ thể: bạn thiết kế **giao thoa kế Michelson** dùng laser He-Ne ($\lambda = 632.8\,\text{nm}$) để đo dịch chuyển với độ phân giải $10\,\text{nm}$. Chùm tia đi qua khẩu độ tròn đường kính $a = 5\,\text{mm}$, khoảng cách đến detector $z = 500\,\text{mm}$.

Số Fresnel:
$$F = \frac{a^2}{\lambda z} = \frac{(2.5 \times 10^{-3})^2}{632.8 \times 10^{-9} \times 0.5} = \frac{6.25 \times 10^{-6}}{3.164 \times 10^{-7}} \approx 19.7$$

Vì $F \gg 1$, hệ đang ở **chế độ Fresnel mạnh**. Điều này có nghĩa:
1. Tại tâm trục quang, cường độ dao động mạnh khi thay đổi $z$ — gây sai số đo
2. Phân bố cường độ trên mặt detector không đều, ảnh hưởng đến độ chính xác đo pha
3. Phải dùng thấu kính chuẩn trực (collimating lens) để đưa về chế độ Fraunhofer ($F \ll 1$)

Thu nhỏ khẩu độ xuống $a = 0.5\,\text{mm}$: $F = 0.197 < 1$ — vào chế độ Fraunhofer, hoa văn ổn định hơn nhiều. Nhưng flux quang học giảm, signal-to-noise ratio giảm. Đây là trade-off điển hình trong thiết kế hệ đo quang học chính xác.

### 7. Vùng Fresnel (Fresnel Zones)

Công cụ hình học quan trọng để phân tích nhiễu xạ Fresnel là **vùng Fresnel** (Fresnel zones). Chia mặt phẳng khẩu độ thành các vành đai đồng tâm, sao cho khoảng cách từ mép ngoài vùng thứ $m$ đến điểm quan sát $P$ là $r_m = r_0 + m\lambda/2$:

$$r_m = \sqrt{z^2 + \rho_m^2} \Rightarrow \rho_m \approx \sqrt{m\lambda z}$$

Mỗi vùng Fresnel đóng góp biên độ xấp xỉ bằng nhau nhưng **đổi dấu** giữa vùng lẻ và vùng chẵn (vì lệch pha $\pi$). Kết quả cho khẩu độ vô hạn (không chắn):

$$E_{\text{total}} = \frac{E_1}{2}$$

Nếu đĩa chắn che $m$ vùng Fresnel đầu tiên, chỉ còn các vùng từ $m+1$ trở đi đóng góp — trường tại tâm xấp xỉ $E_{m+1}$, thường **lớn hơn** $E_1/2$ (vì các vùng đầu bị loại). Điều này giải thích tại sao **đĩa Zone Plate** (đĩa che các vùng chẵn) hoạt động như thấu kính hội tụ!

### 8. Zone Plate: Thấu Kính Nhiễu Xạ

Zone plate che các vùng Fresnel chẵn (hoặc lẻ), chỉ cho sóng từ các vùng cùng pha truyền qua — kết quả là hội tụ ánh sáng tại tiêu điểm $f \approx r_1^2/\lambda$. Zone plate là nền tảng của:
- Kính hiển vi tia X (X-ray microscopy)
- Quang học EUV trong lithography bán dẫn
- Hệ thống ảnh đồng vị phóng xạ trong y tế

### Tóm Tắt Toán Học

| Đại lượng | Công thức | Ý nghĩa |
|---|---|---|
| Số Fresnel | $F = a^2/(\lambda z)$ | Phân biệt chế độ nhiễu xạ |
| Bán kính vùng Fresnel thứ $m$ | $\rho_m \approx \sqrt{m\lambda z}$ | Xây dựng zone plate |
| Tích phân Fresnel | $C(u), S(u)$ | Tính cường độ qua rìa |
| Cường độ tại rìa hình học | $I = I_0/4$ | Kết quả chuẩn |
| Cực đại thứ nhất ngoài bóng | $I \approx 1.37 I_0$ | Cực đại overshoot |

Nhiễu xạ Fresnel không chỉ là lý thuyết đẹp — nó là công cụ thiết yếu cho bất kỳ kỹ sư nào làm việc với hệ quang học ở thang đo bước sóng ánh sáng.

---
*Exported from Feynman Bot*
