---
lesson_id: 5405
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-02T15:10:28.594025+00:00"
content_hash: 6c7647b94e08
chapter_number: 13
chapter_title: Chapter 13
section_number: 1
section_title: 13Work and Potential Energy (A)
---
# Công và Thế Năng — Phân Tích Chuyên Sâu

*Source: Chapter 13 - Chapter 13 (Section 1) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_13.html)*

# Công và Thế Năng — Phân Tích Chuyên Sâu

## Bước 1: Suy Luận Từ Rơi Tự Do Đến Tổng Quát

Feynman bắt đầu từ trường hợp đơn giản nhất: vật rơi tự do. Ta đã biết:
$$rac{1}{2}mv_2^2 - rac{1}{2}mv_1^2 = mgh$$

Câu hỏi: điều này có còn đúng khi vật di chuyển theo đường cong bất kỳ (không phải rơi thẳng) không?

Xét vật trượt trên mặt phẳng nghiêng không ma sát, sau đó qua đường cong phức tạp — thực nghiệm và lý thuyết đều xác nhận: **kết quả chỉ phụ thuộc vào hiệu độ cao, không phụ thuộc đường đi**.

Đây là gợi ý mạnh về sự tồn tại của thế năng.

## Bước 2: Định Nghĩa Chính Xác Công

Công của lực $ec{F}$ dọc theo đường cong từ điểm 1 đến điểm 2:
$$W_{1	o2} = \int_1^2 ec{F}(s) \cdot dec{s}$$

Tích vô hướng $ec{F} \cdot dec{s} = F\,ds\cos	heta$, trong đó $	heta$ là góc giữa lực và độ dời.

**Tại sao tích vô hướng?** Chỉ thành phần lực song song với chuyển động mới ảnh hưởng đến tốc độ. Thành phần vuông góc chỉ làm thay đổi hướng.

Chứng minh định lý công-động năng:
$$\int_1^2 ec{F} \cdot dec{s} = \int_1^2 mrac{dec{v}}{dt} \cdot ec{v}\,dt = m\int_1^2 rac{d}{dt}\left(rac{v^2}{2}ight)dt = rac{1}{2}mv_2^2 - rac{1}{2}mv_1^2$$

## Bước 3: Điều Kiện Để Thế Năng Tồn Tại

Không phải mọi lực đều có thế năng! Thế năng $U$ tồn tại khi và chỉ khi:

$$\oint ec{F} \cdot dec{s} = 0 \quad 	ext{(mọi đường kín)}$$

Nghĩa là: công thực hiện theo bất kỳ đường kín nào đều bằng 0.

**Tại sao quan trọng?** Nếu tích phân đường kín khác 0, ta có thể tạo ra máy chuyển động vĩnh cửu — điều không thể. Do đó, lực bảo toàn phải thỏa mãn điều kiện này.

Trọng lực $ec{F} = -mg\hat{j}$: tích phân trên đường kín bất kỳ bằng 0 (có thể kiểm tra bằng cách phân tích thành phần ngang và dọc).

Lực hấp dẫn $ec{F} = -GMm/r^2 \hat{r}$: cũng thỏa mãn — chứng minh bằng hệ tọa độ cực.

## Bước 4: Thế Năng Hấp Dẫn — Tính Toán Tường Minh

$$U(r) = -\int_\infty^r ec{F} \cdot dec{r} = -\int_\infty^r \left(-rac{GMm}{r^2}ight)dr = -rac{GMm}{r}\Big|_\infty^r = -rac{GMm}{r}$$

(Chọn mốc thế năng tại vô cực: $U(\infty) = 0$)

**Ứng dụng — vận tốc vũ trụ cấp 1 và 2:**

Vận tốc tối thiểu để vệ tinh bay quanh Trái Đất ở độ cao $h$:
$$rac{1}{2}mv^2 = rac{GMm}{R+h} \Rightarrow v_1 = \sqrt{rac{GM}{R+h}}$$

Vận tốc thoát khỏi Trái Đất (từ mặt đất):
$$rac{1}{2}mv_{thoat}^2 - rac{GMm}{R} = 0 \Rightarrow v_{thoat} = \sqrt{rac{2GM}{R}} pprox 11.2\ km/s$$

## Bước 5: Ứng Dụng Kỹ Thuật — Tính Toán Năng Lượng Robot

**Bài toán thực tế**: Cánh tay robot 6 bậc tự do, mang tải $m_{tải} = 5\ kg$, cánh tay có khối lượng $m_{cánh} = 3\ kg$. Di chuyển từ vị trí thấp $h_1 = 0.3\ m$ đến vị trí cao $h_2 = 1.2\ m$ (đo từ mặt đất).

**Tính năng lượng cần thiết:**

Thế năng cần tăng:
- Tải: $\Delta U_{tải} = m_{tải}g\Delta h = 5 	imes 9.8 	imes 0.9 = 44.1\ J$
- Cánh tay (trọng tâm tại $h_{cm}$, giả sử tăng $0.45\ m$): $\Delta U_{cánh} = 3 	imes 9.8 	imes 0.45 = 13.2\ J$

Tổng: $\Delta U = 57.3\ J$

Nếu di chuyển trong $t = 0.5\ s$, công suất tối thiểu: $P = 57.3/0.5 = 114.6\ W$

Thực tế, motor cần công suất lớn hơn do: hiệu suất cơ học (~85%), gia tốc (động năng), và lực ma sát trong ổ trục.

## Bài Tập Thực Hành

Một robot hàn đặt mối hàn tại vị trí $h = 0.8\ m$ so với nền. Sau khi hàn xong, hạ điện cực xuống $h = 0.2\ m$. Điện cực có khối lượng $m = 2\ kg$.

1. Tính công do trọng lực thực hiện khi hạ điện cực: $W = mg\Delta h = 2 	imes 9.8 	imes 0.6 = 11.76\ J$
2. Nếu không có phanh tái sinh, năng lượng này biến thành nhiệt trong động cơ.
3. Với phanh tái sinh (regenerative braking) ở hiệu suất 70%: thu hồi $0.7 	imes 11.76 = 8.23\ J$

Đây là nguyên lý tiết kiệm năng lượng trong robot công nghiệp hiện đại.

## Điểm Mấu Chốt

Công là cầu nối giữa lực và năng lượng. Thế năng tồn tại khi lực bảo toàn — tức là lực "nhớ" vị trí nhưng "quên" đường đi. Trong kỹ thuật, hiểu thế năng giúp tính toán năng lượng cho robot, thiết kế hệ thống phanh tái sinh, và dự đoán hành vi của hệ cơ học phức tạp.

---
*Exported from Feynman Bot*
