---
lesson_id: 5625
lesson_type: quiz
approval_status: pending
exported_at: "2026-03-03T15:33:09.337307+00:00"
content_hash: aea5ee810dae
chapter_number: 37
chapter_title: Chapter 37
section_number: 8
section_title: 37–7First principles of quantum mechanics
---
# ## Quiz: Biên Độ Xác Suất và Nguyên Lý Lượng Tử

*Source: Chapter 37 - Chapter 37 (Section 8) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_37.html)*

## Quiz: Biên Độ Xác Suất và Nguyên Lý Lượng Tử

### Câu 1 (MCQ)

Trong cơ học lượng tử, một electron có thể đến detector theo ba con đường khác nhau với biên độ xác suất $\phi_1 = 0.3$, $\phi_2 = 0.4i$, $\phi_3 = -0.5$ (đây là các số phức). Nếu không có thiết bị nào xác định electron đi theo đường nào, xác suất tổng là:

**A.** $P = |0.3|^2 + |0.4i|^2 + |-0.5|^2 = 0.09 + 0.16 + 0.25 = 0.50$

**B.** $P = |0.3 + 0.4i + (-0.5)|^2 = |-0.2 + 0.4i|^2 = 0.04 + 0.16 = 0.20$

**C.** $P = (0.3 + 0.4 + 0.5)^2 = 1.44$

**D.** $P = 0.3 	imes 0.4i 	imes (-0.5) = -0.06i$

**Đáp án: B**

*Giải thích:* Khi không phân biệt được đường đi, áp dụng quy tắc 2: cộng biên độ trước. $\phi_{	ext{total}} = 0.3 + 0.4i - 0.5 = -0.2 + 0.4i$. Xác suất: $P = |-0.2 + 0.4i|^2 = (-0.2)^2 + (0.4)^2 = 0.04 + 0.16 = 0.20$. Lưu ý: $P = 0.20 
eq 0.50$ — hiệu ứng giao thoa làm xác suất khác với tổng thành phần.

---

### Câu 2 (MCQ)

Hiệu ứng Aharonov-Bohm: electron đi qua hai đường vòng quanh solenoid có từ thông $\Phi_B = \Phi_0/4$ (với $\Phi_0 = h/e$ là lượng tử từ thông). Hiệu pha giữa hai đường đi do từ thông gây ra là:

**A.** $\Deltaarphi = \pi/4$

**B.** $\Deltaarphi = \pi/2$

**C.** $\Deltaarphi = \pi$

**D.** $\Deltaarphi = 2\pi$

**Đáp án: B**

*Giải thích:* $\Deltaarphi = 2\pi\Phi_B/\Phi_0 = 2\pi 	imes (1/4) = \pi/2$. Hiệu pha này hoàn toàn do $\mathbf{A}$ (vector thế), kể cả khi $\mathbf{B} = 0$ trên đường đi của electron. Đây là bằng chứng $\mathbf{A}$ có thực tại vật lý, không chỉ là công cụ toán học.

---

### Câu 3 (MCQ)

Tại sao phương trình Schrödinger đảm bảo nguyên lý superposition lượng tử?

**A.** Vì phương trình Schrödinger chứa hằng số Planck $\hbar$.

**B.** Vì phương trình Schrödinger là phương trình vi phân **tuyến tính** — tổ hợp tuyến tính của các nghiệm cũng là nghiệm.

**C.** Vì phương trình Schrödinger bảo toàn năng lượng.

**D.** Vì phương trình Schrödinger là phương trình bậc hai theo không gian.

**Đáp án: B**

*Giải thích:* $i\hbar\partial_t|\psiangle = \hat{H}|\psiangle$ là phương trình tuyến tính. Nếu $|\psi_1angle$ và $|\psi_2angle$ là nghiệm, thì $lpha|\psi_1angle + eta|\psi_2angle$ ($lpha, eta \in \mathbb{C}$) cũng là nghiệm. Chính tính tuyến tính này tạo ra superposition và giao thoa. Nếu phương trình phi tuyến, hệ thống sẽ hành xử khác hoàn toàn (không có superposition thuần túy).

---

### Câu 4 (Câu hỏi mở)

**SQUID (Superconducting Quantum Interference Device) là sensor từ trường nhạy nhất hiện nay, được dùng trong chẩn đoán y tế (MEG — Magnetoencephalography) và hoa tiêu quán tính. SQUID hoạt động dựa trên hiệu ứng Aharonov-Bohm cho cặp Cooper (Cooper pairs).**

**(a)** Lượng tử từ thông cho cặp Cooper là $\Phi_0 = h/(2e) pprox 2.07 	imes 10^{-15}$ Wb (thay vì $h/e$ cho electron đơn, vì cặp Cooper có điện tích $2e$). Một SQUID đo được thay đổi từ thông $\delta\Phi = 10^{-6}\Phi_0$. Tính $\delta\Phi$ bằng Weber. Nếu diện tích vòng SQUID là $A = 1$ mm², từ trường thay đổi tương ứng $\delta B$ là bao nhiêu Tesla?

**(b)** Trong hệ thống hoa tiêu quán tính cho vũ khí dẫn đường, SQUID được dùng để đo từ trường Trái Đất với độ chính xác cao. Từ trường Trái Đất ở tầm trung bình là $B_E pprox 50$ μT. Để định vị với sai số $\leq 1$ m trên quỹ đạo $1000$ km, cần độ chính xác góc phương vị $\leq 10^{-6}$ rad. Từ trường thay đổi trên quãng đường $1$ m là khoảng $\delta B/\delta x pprox 1$ nT/m. Tính $\delta B$ cần đo, và xác nhận SQUID có đủ độ nhạy không.

**(c)** Giải thích tại sao superconductor "cưỡng bức" từ thông bên trong vòng phải là bội số nguyên của $\Phi_0$ (flux quantization). Điều này liên quan như thế nào đến nguyên lý biên độ xác suất và điều kiện cặp Cooper di chuyển theo vòng kín?

**Gợi ý trả lời:**

(a) $\delta\Phi = 10^{-6} 	imes 2.07 	imes 10^{-15} = 2.07 	imes 10^{-21}$ Wb. $\delta B = \delta\Phi / A = 2.07 	imes 10^{-21} / 10^{-6} = 2.07 	imes 10^{-15}$ T $pprox 2$ fT (femtoTesla). Đây là độ nhạy đặc trưng của SQUID.

(b) $\delta B$ cần đo $= 1$ nT/m $	imes 1$ m $= 1$ nT $= 10^{-9}$ T. SQUID nhạy tới fT → hoàn toàn đủ (nhạy hơn $10^6$ lần so với yêu cầu). Thực tế, giới hạn là nhiễu từ môi trường, không phải độ nhạy SQUID.

(c) Hàm sóng cặp Cooper $\psi = |\psi|e^{i	heta(\mathbf{r})}$ phải đơn trị khi đi vòng kín: $\oint 
abla	heta \cdot d\mathbf{l} = 2\pi n$. Trong superconductor, $
abla	heta = (2e/\hbar)\mathbf{A}$ (do Meissner effect). Suy ra: $\oint (2e/\hbar)\mathbf{A} \cdot d\mathbf{l} = (2e/\hbar)\Phi_B = 2\pi n$ → $\Phi_B = n\Phi_0 = nh/(2e)$. Đây chính là điều kiện biên độ xác suất đơn trị — nguyên lý cơ học lượng tử căn bản!


---
*Exported from Feynman Bot*
