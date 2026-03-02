---
lesson_id: 5512
lesson_type: concept
approval_status: pending
exported_at: "2026-03-02T15:10:31.423408+00:00"
content_hash: d7bb6227764c
chapter_number: 26
chapter_title: Chapter 26
section_number: 6
section_title: 26–5A more precise statement of Fermat’s principle
---
# ## Nguyên Lý Stationary Time: Ánh Sáng "Ngửi" Đường Đi

*Source: Chapter 26 - Chapter 26 (Section 6) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_26.html)*

## Nguyên Lý Stationary Time: Ánh Sáng "Ngửi" Đường Đi

### Mở Đầu: Ánh Sáng Có Biết "Suy Nghĩ" Không?

Hãy đặt một câu hỏi lạ: khi ánh sáng gặp gương, làm sao nó "biết" phải phản xạ theo góc nào? Nếu nguyên lý Fermat nói ánh sáng chọn đường ít thời gian nhất, thì ánh sáng phải "xem xét" tất cả các đường có thể rồi chọn ra đường tốt nhất — nghe có vẻ như ánh sáng phải có ý thức! Thực ra, câu trả lời tinh tế hơn nhiều, và liên quan đến bản chất sóng của ánh sáng.

### Phát Biểu Đúng: Stationary Time, Không Phải Minimum Time

Phát biểu chính xác của nguyên lý Fermat không phải là "thời gian nhỏ nhất" mà là **"thời gian cực trị"** (stationary time). Điều này có nghĩa: một tia sáng đi theo đường $\gamma$ sao cho nếu ta thay đổi đường đó một chút (perturbation nhỏ), thời gian thay đổi chỉ theo bậc hai — không có thay đổi bậc nhất.

Ví dụ với gương lõm: đường đi từ $A$ đến $B$ qua gương lõm có thể là đường **dài nhất** trong vùng lân cận! Đường thẳng $AB$ (không qua gương) ngắn hơn. Nhưng đường qua gương lõm vẫn thỏa mãn điều kiện stationary — mọi đường lân cận cũng tốn gần đúng cùng thời gian.

Tương tự trong toán học tối ưu: hàm $f(x)$ có điểm cực trị (stationary point) khi $f'(x) = 0$, có thể là cực tiểu, cực đại, hoặc điểm yên ngựa (saddle point).

### Cơ Chế Vật Lý: Ánh Sáng "Ngửi" Đường Đi

Vậy cơ chế thực sự là gì? Feynman giải thích một cách thiên tài: ánh sáng thực ra là sóng và truyền theo **mọi đường có thể** cùng một lúc. Tuy nhiên, chỉ những đường nào mà các đường lân cận có cùng thời gian (stationary) mới có sự **giao thoa xây dựng** (constructive interference) — các sóng từ các đường lân cận đến cùng pha và tăng cường nhau. Ở các đường khác, các sóng đến với pha khác nhau và triệt tiêu nhau.

Đây là lý do tại sao bước sóng $\lambda$ quyết định "tầm ngửi" của ánh sáng: ánh sáng cần xem xét các đường trong vùng $\Delta r \sim \sqrt{\lambda \cdot L}$ (vùng Fresnel). Với ánh sáng khả kiến ($\lambda \approx 500\,\text{nm}$) và $L = 1\,\text{m}$, vùng này rộng khoảng $\sqrt{500\times10^{-9} \times 1} \approx 0.7\,\text{mm}$. Đây là tại sao hiệu ứng nhiễu xạ (diffraction) chỉ rõ ràng khi khe hở có kích thước vài mm hoặc nhỏ hơn.

### Thí Nghiệm Minh Họa: Sóng Radio qua Khe

Feynman mô tả thí nghiệm dùng sóng radio $\lambda = 3\,\text{cm}$: nếu có khe hẹp giữa nguồn $S$ và detector $D$, sóng đi qua khe theo đường thẳng. Khi dịch detector sang bên ($D'$), với khe rộng, sóng không đến được $D'$ vì các đường lân cận đến với pha khác nhau (thời gian khác nhau) và triệt tiêu nhau. Nhưng khi khe thu hẹp lại, chỉ còn một đường khả dụng — và sóng bây giờ lại đến được $D'$! Khe hẹp hơn → nhiều sóng đến $D'$ hơn. Đây chính là **nhiễu xạ** (diffraction).

Với ánh sáng thường, bạn có thể thấy điều này bằng cách nhìn qua khe giữa hai ngón tay: hình ảnh điểm sáng xa giãn thành vệt dài khi khe nhỏ dần.

### Ý Nghĩa Triết Học: Tính Nhân Quả vs Nguyên Lý Tổng Thể

Nguyên lý Fermat đại diện cho một triết lý hoàn toàn khác so với định luật Snell:
- **Định luật Snell (nhân quả):** Ánh sáng đến mặt phân cách → mặt phân cách tác dụng lực → ánh sáng bẻ cong. Chuỗi nguyên nhân-kết quả địa phương.
- **Nguyên lý Fermat (tổng thể):** Ánh sáng "biết" điểm đến và chọn đường tối ưu. Đây là nguyên lý toàn cục (global principle).

Như một kỹ sư cơ điện tử, bạn có thể liên tưởng: điều khiển phản hồi (feedback control) là "nhân quả" — hệ thống phản ứng với sai lệch hiện tại. Trong khi đó, điều khiển tối ưu (optimal control, MPC) là "toàn cục" — hệ thống "biết trước" mục tiêu và tối ưu hóa toàn bộ quỹ đạo. Cả hai đều đúng, nhưng cách nhìn "toàn cục" thường mạnh hơn.

### Kết Luận

Nguyên lý "stationary time" không phải là sự thần bí về ý thức của ánh sáng — nó là hệ quả toán học của bản chất sóng. Ánh sáng thực sự "ngửi" các đường lân cận thông qua hiệu ứng giao thoa. Bước sóng đặt ra thang đo của "tầm ngửi" này. Khi bước sóng tiến về 0 (giới hạn hình học), nguyên lý này thu gọn thành quang học tia — giống như cơ học lượng tử thu gọn thành cơ học cổ điển khi $\hbar \to 0$.

---
*Exported from Feynman Bot*
