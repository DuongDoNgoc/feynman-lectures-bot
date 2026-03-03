---
lesson_id: 5420
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:04.615909+00:00"
content_hash: 81a95be51b58
chapter_number: 14
chapter_title: Chapter 14
section_number: 5
section_title: 14–4Nonconservative forces
---
# Lực "Không Bảo Toàn" — Phân Tích Chuyên Sâu

*Source: Chapter 14 - Chapter 14 (Section 5) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_14.html)*

# Lực "Không Bảo Toàn" — Phân Tích Chuyên Sâu

## Bước 1: Tại Sao Mọi Lực Cơ Bản Đều Bảo Toàn?

Trong vật lý hiện đại, chỉ có 4 lực cơ bản:
1. **Hấp dẫn** — bảo toàn (thế năng hấp dẫn)
2. **Điện từ** — bảo toàn (thế năng điện từ)
3. **Lực hạt nhân mạnh** — bảo toàn (thế năng sắc lực)
4. **Lực hạt nhân yếu** — bảo toàn (thế năng yếu)

Mọi hiện tượng vĩ mô (ma sát, nhiệt, hóa học, cơ học) đều là biểu hiện của bốn lực này. Do đó, bảo toàn năng lượng là **định luật tuyệt đối** — không có ngoại lệ trong tự nhiên đã biết.

## Bước 2: Ma Sát — Phân Tích Cấp Độ Vi Mô

**Mô hình đơn giản**: Vật trượt trên bề mặt. Các đỉnh (asperity) vi mô của hai bề mặt va chạm.

Tại mỗi va chạm vi mô:
- Cặp nguyên tử va chạm đàn hồi (bảo toàn năng lượng vi mô)
- Năng lượng phân tán ra nhiều hướng → dao động nhiệt

**Kết quả vĩ mô**: 
$$Q = \mu_k mg \cdot d \quad \text{(nhiệt sinh ra)}$$

Trong đó $\mu_k$ là hệ số ma sát động (thực nghiệm), $d$ là quãng đường trượt.

**Kiểm tra bảo toàn**:
$$\Delta K + Q = 0 \quad \Leftrightarrow \quad \frac{1}{2}mv_2^2 - \frac{1}{2}mv_1^2 + \mu_k mg \cdot d = 0$$

Hoặc tổng quát: $K_1 + Q_{cung\,cấp} = K_2 + Q_{tỏa\,ra}$.

## Bước 3: Hóa Năng — Thế Năng Điện Ở Cấp Độ Phân Tử

**Liên kết hóa học** = Thế năng Coulomb giữa electron và hạt nhân.

Phản ứng đốt cháy methane:
$$CH_4 + 2O_2 \to CO_2 + 2H_2O + \Delta H$$

$\Delta H < 0$: thế năng điện của sản phẩm thấp hơn chất phản ứng → năng lượng giải phóng.

**Năng lượng liên kết** tiêu biểu:
- C-H: 413 kJ/mol
- O=O: 498 kJ/mol  
- C=O: 799 kJ/mol
- O-H: 463 kJ/mol

Tất cả đều là **thế năng điện từ Coulomb** ở cấp độ electron.

## Bước 4: Nhiệt Năng — Động Năng Vi Mô

Nhiệt độ $T$ của vật = trung bình động năng vi mô:
$$\langle\frac{1}{2}mv_{phân\,tử}^2\rangle = \frac{3}{2}k_B T$$

Khi vật nóng lên $\Delta T$, năng lượng nhiệt tích lũy:
$$Q = mc\Delta T \quad \text{($c$ = nhiệt dung riêng)}$$

Đây là **động năng** của hàng tỷ tỷ nguyên tử dao động — hoàn toàn bảo toàn ở cấp độ vi mô.

## Bước 5: Ứng Dụng — Phân Tích Nhiệt Hệ Thống CNC

**Bài toán thực tế**: Máy CNC gia công thép với:
- Lực cắt $F = 800\,N$
- Tốc độ cắt $v = 2\,m/s$
- Hiệu suất gia công (năng lượng vào phoi): 15%

**Cân bằng năng lượng:**
- Công suất cơ học vào: $P_{vào} = F \cdot v = 800 \times 2 = 1600\,W$
- Năng lượng vào phoi (biến dạng dẻo + phá vỡ liên kết): $15\% \times 1600 = 240\,W$
- Nhiệt sinh ra tại vùng cắt: $85\% \times 1600 = 1360\,W$

Nhiệt phân phối:
- Phoi mang đi: ~75% → $1020\,W$
- Dụng cụ cắt hấp thụ: ~20% → $272\,W$
- Phôi hấp thụ: ~5% → $68\,W$

**Tác động kỹ thuật**: Nhiệt trong dụng cụ cắt làm mòn nhanh hơn; nhiệt trong phôi gây biến dạng nhiệt → sai số gia công. Bảo toàn năng lượng là công cụ định lượng chính xác dòng nhiệt.

## Bài Tập: Hiệu Suất Của Hệ Truyền Động

Hộp số bánh răng có 3 cấp, mỗi cấp hiệu suất $\eta = 98\%$. Công suất vào: $P_{vào} = 5\,kW$.

Công suất ra: $P_{ra} = P_{vào} \times \eta^3 = 5000 \times 0.98^3 \approx 4706\,W$

Tổn thất nhiệt: $P_{nhiệt} = 5000 - 4706 = 294\,W$

Nguồn nhiệt: ma sát bánh răng + ma sát ổ trục + khuấy dầu bôi trơn. Tất cả là chuyển đổi cơ năng → nhiệt năng theo bảo toàn năng lượng.

**Nhiệt độ tăng trong thời gian $t = 1\,h = 3600\,s$** (giả sử hộp số $m = 20\,kg$ thép, $c = 500\,J/kg\cdot K$, không có tản nhiệt):
$$\Delta T = \frac{P_{nhiệt} \cdot t}{mc} = \frac{294 \times 3600}{20 \times 500} = 106\,K$$

→ Cần hệ thống làm mát! Bảo toàn năng lượng giúp thiết kế đúng dung tích làm mát.

## Điểm Mấu Chốt

"Lực không bảo toàn" là khái niệm vĩ mô gần đúng. Ở cấp độ vi mô, tất cả tương tác đều bảo toàn. Bảo toàn năng lượng TỔNG (cơ + nhiệt + hóa + điện + ...) là định luật tuyệt đối trong kỹ thuật và vật lý — công cụ thiết yếu để phân tích tổn thất và thiết kế hệ thống làm mát.

---
*Exported from Feynman Bot*
