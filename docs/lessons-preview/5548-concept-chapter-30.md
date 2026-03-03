---
lesson_id: 5548
lesson_type: concept
approval_status: approved
exported_at: "2026-03-03T15:33:07.677349+00:00"
content_hash: ef1caf20e800
chapter_number: 30
chapter_title: Chapter 30
section_number: 7
section_title: 30–6Diffraction by opaque screens
---
# ## Nhiễu Xạ Fresnel: Khi Bóng Tối Không Còn Là Bóng Tối

*Source: Chapter 30 - Chapter 30 (Section 7) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_30.html)*

## Nhiễu Xạ Fresnel: Khi Bóng Tối Không Còn Là Bóng Tối

Bạn có bao giờ thắc mắc: nếu dùng dao sắc bén che một nửa chùm tia laser, liệu rìa bóng tối có thực sự sắc nét tuyệt đối không? Câu trả lời sẽ khiến bạn bất ngờ — rìa bóng đó thực ra dao động sáng-tối-sáng-tối, giống như vân giao thoa, ngay cả khi không có khe nào! Đây chính là hiện tượng **nhiễu xạ Fresnel** (Fresnel diffraction), một trong những biểu hiện kỳ diệu nhất của bản chất sóng của ánh sáng.

---

### Lỗ Hổng Trong Tấm Chắn: Nguồn Sáng Ảo Hay Thực?

Hãy tưởng tượng bạn có một tấm kim loại đục không trong suốt, đục một lỗ tròn nhỏ. Ánh sáng chiếu vào một phía. Bạn đặt màn chắn ở phía bên kia để quan sát. Phần lớn mọi người sẽ trả lời ngay: "Ánh sáng chui qua lỗ rồi chiếu lên màn thôi!"

Nhưng Feynman đặt câu hỏi sâu sắc hơn: *Thực chất điều gì đang xảy ra tại cái lỗ đó?*

Thực ra không hề có nguồn sáng nào bên trong lỗ cả. Lỗ chỉ là nơi **không có vật liệu**. Thế nhưng nguyên lý Huygens-Fresnel phát biểu một điều kỳ lạ: ta có thể tính toán chính xác cường độ ánh sáng phía sau tấm chắn bằng cách **coi mỗi điểm trên lỗ hổng như một nguồn sóng thứ cấp** (secondary source), phát sóng đồng pha với sóng tới, và cộng tất cả các đóng góp đó lại.

Kết quả tính toán khớp hoàn hảo với thực nghiệm. Đây là một trong những kết quả "thần kỳ" của vật lý: cách tính toán đúng, mặc dù mô hình vật lý ("có nguồn tại lỗ") về mặt nghĩa đen là **sai**.

---

### Nguyên Lý Babinet: Bổ Sung Kỳ Diệu

Từ cách tiếp cận trên nảy sinh một hệ quả đẹp đẽ gọi là **nguyên lý Babinet** (Babinet's principle).

Xét hai vật chắn "bổ sung" nhau:
- Tấm A: tấm chắn đục lỗ
- Tấm B: đĩa chắn vừa khít che lỗ đó

Nếu không có vật chắn nào ($E_{total}$), sóng truyền tự do. Khi đặt tấm A, chỉ sóng qua lỗ truyền qua, tạo ra trường $E_A$. Khi đặt tấm B, chỉ sóng quanh đĩa truyền qua, tạo ra trường $E_B$.

Nguyên lý Babinet phát biểu:
$$E_A + E_B = E_{total}$$

Nghĩa là: *tấm chắn và vật chắn bổ sung tạo ra cùng hoa văn nhiễu xạ ở xa* (ngoại trừ tia thẳng trực tiếp). Hệ quả: **một đĩa tròn nhỏ sẽ tạo ra điểm sáng ngay chính giữa bóng tối của nó** — gọi là điểm Poisson hay điểm Arago!

---

### Nhiễu Xạ Fresnel Khác Fraunhofer Như Thế Nào?

Trong các bài trước chúng ta học về **nhiễu xạ Fraunhofer** (Fraunhofer diffraction) — xảy ra khi nguồn sáng và màn quan sát đều ở **rất xa** vật chắn (về mặt toán học: khoảng cách $\to \infty$, hay dùng thấu kính hội tụ để mô phỏng điều đó).

**Nhiễu xạ Fresnel** xảy ra khi nguồn sáng, vật chắn, hoặc màn ở **khoảng cách hữu hạn**. Về mặt toán học, điều này phức tạp hơn vì không thể dùng gần đúng pha tuyến tính — phải giữ lại các số hạng bậc hai trong khai triển pha.

Số Fresnel $F$ đặc trưng cho chế độ nhiễu xạ:
$$F = \frac{a^2}{\lambda z}$$

Trong đó $a$ là kích thước đặc trưng của khe/lỗ, $\lambda$ là bước sóng, $z$ là khoảng cách. Khi $F \ll 1$: chế độ Fraunhofer. Khi $F \sim 1$ hoặc lớn hơn: chế độ Fresnel.

---

### Góc Nhìn Của Kỹ Sư Cơ Điện Tử

Bạn thiết kế hệ thống đo lường độ chính xác micro-mét — thì nhiễu xạ Fresnel không phải khái niệm xa xôi mà là **vấn đề thực tế hàng ngày**.

Hãy nghĩ đến **giao thoa kế laser** (laser interferometer) dùng trong đo dịch chuyển micro-mét. Khi chùm tia laser đi qua khẩu độ (aperture) của thấu kính hoặc gương, nếu khoảng cách không đủ lớn so với kích thước khẩu độ, các vân nhiễu xạ Fresnel sẽ xuất hiện trên mặt phẳng đo, tạo ra **sai số có hệ thống** trong phép đo. Kỹ sư phải tính toán số Fresnel để biết liệu hệ thống đang ở chế độ Fraunhofer (an toàn, dễ tính) hay Fresnel (cần hiệu chỉnh phức tạp hơn).

Tương tự trong **lithography quang học** (in mạch vi điện tử): khi chiếu qua mask lên wafer silicon, nhiễu xạ Fresnel quyết định độ sắc nét của các cạnh. Hiểu nhiễu xạ chính xác ở mức micro-mét và nano-mét là sống còn.

---

### Hoa Văn Cường Độ Tại Rìa Bóng

Một trong những kết quả ấn tượng nhất của nhiễu xạ Fresnel là hoa văn cường độ tại rìa của bóng tối:

- **Bên trong vùng tối**: cường độ không phải là $0$ mà dao động nhẹ rồi tắt dần
- **Ngay tại rìa hình học**: cường độ bằng $I_0/4$ (một phần tư cường độ ánh sáng không bị chắn)
- **Bên ngoài vùng sáng**: xuất hiện các vân sáng-tối xen kẽ với cường độ giảm dần

Có thể dùng **đường cong Cornu** (Cornu spiral) để tính toán các hoa văn này bằng tích phân Fresnel:
$$C(u) = \int_0^u \cos\left(\frac{\pi t^2}{2}\right)dt, \quad S(u) = \int_0^u \sin\left(\frac{\pi t^2}{2}\right)dt$$

Kết quả là đường xoắn ốc kép trong không gian phức $(C, S)$, từ đó ta đọc được biên độ và pha của sóng nhiễu xạ.

---

### Điểm Mấu Chốt

- **Nguyên lý Huygens-Fresnel**: mỗi điểm trên mặt sóng (kể cả lỗ hổng) đóng vai trò như nguồn thứ cấp; cộng tất cả đóng góp lại cho kết quả đúng
- **Nguyên lý Babinet**: trường từ tấm chắn + trường từ vật chắn bổ sung = trường tự do; giải thích điểm sáng Poisson-Arago
- **Chế độ nhiễu xạ**: số Fresnel $F = a^2/(\lambda z)$ phân biệt Fresnel ($F \gtrsim 1$) và Fraunhofer ($F \ll 1$)
- **Ứng dụng kỹ thuật**: hiệu chỉnh sai số nhiễu xạ trong giao thoa kế, lithography, và hệ thống quang học chính xác cao

---
*Exported from Feynman Bot*
