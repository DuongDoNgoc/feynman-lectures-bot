---
lesson_id: 5619
lesson_type: quiz
approval_status: pending
exported_at: "2026-03-03T15:33:09.211744+00:00"
content_hash: 071e56dea4de
chapter_number: 37
chapter_title: Chapter 37
section_number: 5
section_title: 37–4An experiment with electrons
---
# ## Quiz: Thí Nghiệm Giao Thoa Hai Khe Với Electron

*Source: Chapter 37 - Chapter 37 (Section 5) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_37.html)*

## Quiz: Thí Nghiệm Giao Thoa Hai Khe Với Electron

### Câu 1 (MCQ)

Trong thí nghiệm hai khe với electron, khi cả hai khe đều mở và không có thiết bị quan sát nào, phân bố electron $P_{12}(x)$ trên màn dò:

**A.** Bằng đúng tổng $P_1(x) + P_2(x)$ của hai phân bố khi từng khe mở riêng lẻ.

**B.** Cho thấy vân giao thoa — có những vùng $P_{12}(x) < P_1(x) + P_2(x)$ và những vùng $P_{12}(x) > P_1(x) + P_2(x)$.

**C.** Bằng không tại mọi vị trí trừ hai vạch hẹp ngay sau hai khe.

**D.** Phụ thuộc vào tốc độ bắn electron — bắn chậm thì tạo giao thoa, bắn nhanh thì không.

**Đáp án: B**

*Giải thích:* $P_{12}(x) = |\phi_1 + \phi_2|^2 = P_1 + P_2 + 2	ext{Re}(\phi_1^*\phi_2)$. Số hạng giao thoa $2	ext{Re}(\phi_1^*\phi_2)$ tạo ra các vùng tăng cường và triệt tiêu. Kết quả không phụ thuộc vào tốc độ bắn — ngay cả khi bắn từng electron một, vân giao thoa vẫn hình thành dần dần.

---

### Câu 2 (MCQ)

Electron được tăng tốc qua điện thế $V = 150$ V. Bước sóng de Broglie tương ứng gần nhất là:

**A.** $\lambda pprox 1$ mm (vô tuyến)
**B.** $\lambda pprox 500$ nm (ánh sáng nhìn thấy)
**C.** $\lambda pprox 100$ pm $= 1$ Å (tia X mềm)
**D.** $\lambda pprox 10$ fm (hạt nhân)

**Đáp án: C**

*Giải thích:* $E_k = eV = 1.6 	imes 10^{-17}$ J, $p = \sqrt{2m_e E_k} pprox 6.6 	imes 10^{-24}$ kg·m/s, $\lambda = h/p = 6.626 	imes 10^{-34} / 6.6 	imes 10^{-24} pprox 100$ pm. Đây là lý do electron phù hợp để nhiễu xạ từ tinh thể (khoảng cách mạng $\sim$ vài Å).

---

### Câu 3 (MCQ)

Trong thí nghiệm hai khe, khi ta thêm nguồn sáng mạnh giữa hai khe để xem electron đi qua khe nào, điều gì xảy ra với vân giao thoa?

**A.** Vân giao thoa trở nên rõ hơn vì ta có thêm thông tin.

**B.** Vân giao thoa biến mất — phân bố trở thành $P_{12} = P_1 + P_2$.

**C.** Vân giao thoa dịch chuyển về phía nguồn sáng.

**D.** Không có gì thay đổi — nguồn sáng không ảnh hưởng đến electron.

**Đáp án: B**

*Giải thích:* Photon ánh sáng tán xạ từ electron truyền "which-path information" — ta biết electron qua khe nào. Quá trình tán xạ này tạo ra nhiễu loạn động lượng ngẫu nhiên $\Delta p \sim h/\lambda_{	ext{light}}$, phá vỡ tương quan pha giữa $\phi_1$ và $\phi_2$. Trung bình theo nhiễu loạn ngẫu nhiên: $\langle	ext{Re}(\phi_1^*\phi_2)angle = 0$, vân giao thoa biến mất hoàn toàn.

---

### Câu 4 (Câu hỏi mở)

**Trong thiết kế hệ thống đo lường chính xác cao (ví dụ: sensor laser interferometry đo dịch chuyển cấp nanometer), nhiễu lượng tử (quantum noise) là một giới hạn căn bản. Dựa trên nguyên lý bất định Heisenberg và hiện tượng mất giao thoa khi quan sát (which-path measurement), hãy giải thích:**

**(a)** Tại sao việc "đo" chính xác hơn vị trí của một hạt lượng tử (để giảm nhiễu vị trí) lại làm tăng nhiễu động lượng? Điều này ảnh hưởng như thế nào đến hệ thống servo điều khiển vị trí?

**(b)** Trong giao thoa kế laser Michelson, photon đóng vai trò gì và tại sao nhiễu shot noise (photon counting noise) là giới hạn căn bản tương tự như trong thí nghiệm electron? Liên hệ với công thức $P_{12} = |\phi_1 + \phi_2|^2$.

**(c)** Một kỹ sư đề xuất dùng electron thay laser để xây dựng giao thoa kế đo dịch chuyển. Cho $\lambda_{	ext{electron}} = 10$ pm và $L = 1$ m, khoảng cách hai khe $d = 100$ nm. Tính khoảng vân $\Delta x$. Ưu và nhược điểm của phương pháp này so với laser interferometry là gì?

**Gợi ý trả lời:**

(a) Nguyên lý bất định: $\Delta x \cdot \Delta p_x \geq \hbar/2$. Khi hệ điều khiển đo vị trí với độ chính xác $\Delta x$, nó tạo ra bất định động lượng $\Delta p \geq \hbar/(2\Delta x)$. Trong chu kỳ điều khiển tiếp theo, bất định động lượng này làm vị trí bị lệch thêm $\delta x \sim \Delta p \cdot \Delta t / m$ — đây là Standard Quantum Limit (SQL) của hệ servo lượng tử.

(b) Photon trong giao thoa kế: mỗi photon phản xạ là một "sự kiện" lượng tử. Shot noise xuất phát từ tính rời rạc của photon — sau $N$ photon, độ lệch chuẩn pha là $\deltaarphi \sim 1/\sqrt{N}$. Tương đương với $P_{12} = |\phi_1 + \phi_2|^2$: nhiễu là do bất định trong biên độ $\phi$, không phải trong cơ cấu đo.

(c) $\Delta x = \lambda L / d = 10 	imes 10^{-12} 	imes 1 / (100 	imes 10^{-9}) = 0.1$ mm. Ưu điểm: $\lambda$ ngắn hơn $10^4$ lần so với laser $ightarrow$ độ phân giải góc cao hơn. Nhược điểm: khó duy trì chùm electron trong không khí (cần chân không), điện tử học phức tạp hơn, tốc độ đo chậm hơn.


---
*Exported from Feynman Bot*
