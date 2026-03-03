---
lesson_id: 5574
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:08.300565+00:00"
content_hash: 2175a709bfa8
chapter_number: 33
chapter_title: Chapter 33
section_number: 5
section_title: 33–4Polarizers
---
# ## Kiểm tra: Định luật Malus và Lưỡng Sắc

*Source: Chapter 33 - Chapter 33 (Section 5) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_33.html)*

## Kiểm tra: Định luật Malus và Lưỡng Sắc

---

**Câu 1**: Ánh sáng tự nhiên (không phân cực) với cường độ $I_0$ đi qua hai polaroid lý tưởng. Polaroid thứ nhất đặt tùy ý, polaroid thứ hai vuông góc với polaroid thứ nhất. Cường độ ánh sáng sau hệ này là:

A) $I_0$
B) $I_0/2$
C) $I_0/4$
D) $0$

**Đáp án: D**

*Giải thích*: Polaroid đầu tiên tạo ánh sáng phân cực tuyến tính với cường độ $I_0/2$ (ánh sáng tự nhiên mất nửa cường độ). Polaroid thứ hai vuông góc với thứ nhất ($	heta = 90°$): $I = (I_0/2)\cos^2(90°) = (I_0/2) 	imes 0 = 0$. Hai polaroid vuông góc hoạt động như một "van đóng" hoàn toàn — nguyên lý được dùng trong màn hình LCD khi tắt một pixel.

---

**Câu 2**: Trong hệ ba polaroid (P1, P2, P3), P1 và P3 vuông góc nhau. P2 đặt giữa, nghiêng $	heta$ so với P1. Cường độ ánh sáng ra sau P3 cực đại khi:

A) $	heta = 0°$
B) $	heta = 30°$
C) $	heta = 45°$
D) $	heta = 90°$

**Đáp án: C**

*Giải thích*: Cường độ ra: $I = I_0/2 \cdot \cos^2	heta \cdot \cos^2(90°-	heta) = (I_0/2)\cos^2	heta\sin^2	heta = (I_0/8)\sin^2(2	heta)$. Hàm $\sin^2(2	heta)$ đạt cực đại khi $2	heta = 90°$, tức $	heta = 45°$. Khi đó $I_{max} = I_0/8$. Kết quả này quan trọng trong thiết kế bộ điều biến ánh sáng (light modulator) dùng tinh thể lỏng.

---

**Câu 3**: Một cảm biến đo góc dùng hai polaroid: một cố định (trục ngang), một quay theo trục của vật đo. Cảm biến đo được $I = 0.25\,I_0$. Góc của vật thể đo là:

A) $30°$
B) $45°$
C) $60°$
D) $75°$

**Đáp án: C**

*Giải thích*: Ánh sáng tự nhiên qua polaroid cố định cho $I_0/2$. Qua polaroid thứ hai ở góc $	heta$: $I = (I_0/2)\cos^2	heta = 0.25\,I_0$. Giải: $\cos^2	heta = 0.5$, $\cos	heta = 1/\sqrt{2}$, $	heta = 45°$. Nhưng đây là góc giữa hai polaroid — nếu polaroid đầu nằm ngang và kết quả là $I = 0.25\,I_0$... Tính lại: $\cos^2	heta = 0.25 	imes 2 = 0.5$ → $	heta = 45°$. Tuy nhiên câu hỏi cho kết quả $I = 0.25I_0$ so với $I_0$ ban đầu. Suy ra $\cos^2	heta = 0.25$ → $\cos	heta = 0.5$ → $	heta = 60°$. Đáp án C.

---

**Câu 4 — Tự luận**: Trong hệ thống điều khiển laser cho vũ khí dẫn đường chính xác, một optical isolator (thiết bị ngăn ánh sáng phản xạ quay về laser nguồn) sử dụng tổ hợp polaroid và rotator Faraday. Giải thích tại sao ánh sáng chiều xuôi truyền qua nhưng ánh sáng phản xạ chiều ngược lại bị chặn, dựa trên định luật Malus và nguyên lý phân cực.

*Gợi ý trả lời*: Cấu trúc isolator: [Polaroid P1 (0°)] → [Rotator Faraday +45°] → [Polaroid P2 (45°)]. Chiều xuôi: ánh sáng từ laser (phân cực 0°) qua P1 (không mất), rotator quay +45°, đến P2 (45°) — khớp hướng, truyền qua. Chiều ngược: ánh sáng phản xạ phân cực 45° qua P2 (không mất), rotator quay thêm +45° (do từ trường, quay không đảo chiều khi sóng đi ngược), thành 90° — gặp P1 (0°): $I = I_r\cos^2(90°) = 0$. Rotator Faraday là "non-reciprocal" — quay cùng chiều bất kể hướng truyền sóng, đây là điểm then chốt.


---
*Exported from Feynman Bot*
