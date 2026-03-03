---
lesson_id: 5624
lesson_type: deep_dive
approval_status: pending
exported_at: "2026-03-03T15:33:09.316014+00:00"
content_hash: d4ec5f8cea55
chapter_number: 37
chapter_title: Chapter 37
section_number: 8
section_title: 37–7First principles of quantum mechanics
---
# ## Toán Học Đầy Đủ: Biên Độ Xác Suất và Cấu Trúc Cơ Học Lượng Tử

*Source: Chapter 37 - Chapter 37 (Section 8) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_37.html)*

## Toán Học Đầy Đủ: Biên Độ Xác Suất và Cấu Trúc Cơ Học Lượng Tử

### 1. Không gian Hilbert và trạng thái lượng tử

Mọi trạng thái của hệ lượng tử được biểu diễn bởi một vector trong không gian Hilbert phức $\mathcal{H}$. Dùng ký hiệu Dirac:

- Ket $|\psiangle \in \mathcal{H}$: trạng thái lượng tử
- Bra $\langle\psi| \in \mathcal{H}^*$: trạng thái đối ngẫu (dual)
- Tích vô hướng: $\langle\phi|\psiangle \in \mathbb{C}$

Biên độ xác suất để tìm hệ ở trạng thái $|\chiangle$ khi hệ đang ở trạng thái $|\psiangle$:

$$\phi = \langle\chi|\psiangle$$

Xác suất tương ứng:

$$P = |\langle\chi|\psiangle|^2$$

### 2. Khai triển theo cơ sở và quy tắc superposition

Chọn cơ sở trực chuẩn $\{|iangle\}$ của $\mathcal{H}$: $\langle i|jangle = \delta_{ij}$, $\sum_i |iangle\langle i| = \hat{I}$.

Bất kỳ trạng thái nào đều khai triển được:

$$|\psiangle = \sum_i c_i |iangle, \quad c_i = \langle i|\psiangle$$

Hệ số $c_i$ chính là biên độ xác suất để tìm hệ ở trạng thái cơ sở $|iangle$. Xác suất tương ứng:

$$P_i = |c_i|^2 = |\langle i|\psiangle|^2$$

Chuẩn hóa đảm bảo: $\sum_i P_i = \sum_i |c_i|^2 = \langle\psi|\psiangle = 1$.

### 3. Biên độ truyền và nguyên lý superposition đường đi

Trong thí nghiệm hai khe, hạt đi từ nguồn $S$ đến detector $D$ có thể qua khe 1 hoặc khe 2. Biên độ tổng:

$$\phi(S 	o D) = \phi(S 	o 1 	o D) + \phi(S 	o 2 	o D)$$

**Quy tắc nhân biên độ (chained propagation):**

$$\phi(S 	o j 	o D) = \phi(S 	o j) \cdot \phi(j 	o D)$$

Đây là quy tắc quan trọng: biên độ theo một đường đi cụ thể bằng tích các biên độ của từng đoạn. Tổng quát hóa cho $n$ bước trung gian:

$$\phi(A 	o B) = \sum_{	ext{all paths}} \prod_{	ext{segments}} \phi(	ext{segment})$$

Đây là nền tảng của **Feynman path integral** — tổng trên tất cả đường đi có thể!

### 4. Tính toán tường minh: Thí nghiệm hai khe

Electron từ nguồn $S = (0, 0)$, hai khe tại $(L_1, \pm d/2)$, detector tại $D = (L_1 + L_2, x)$.

Biên độ tự do cho hạt không tương tác propagate từ $(x_1, y_1)$ đến $(x_2, y_2)$ trong thời gian $t$:

$$\phi(1 	o 2) = \left(rac{m}{2\pi i\hbar t}ight)^{1/2} \exp\!\left(rac{im r^2}{2\hbar t}ight)$$

với $r = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$ là khoảng cách.

Trong giới hạn $L_1, L_2 \gg d, x$, biên độ đến khe $j$ tại $y_j = \pm d/2$:

$$\phi(S 	o j) pprox A e^{ikr_j^S}, \quad r_j^S = \sqrt{L_1^2 + y_j^2} pprox L_1 + rac{y_j^2}{2L_1}$$

Biên độ từ khe $j$ đến detector:

$$\phi(j 	o D) pprox B e^{ikr_j^D}, \quad r_j^D pprox L_2 + rac{(x-y_j)^2}{2L_2}$$

Biên độ tổng:

$$\phi_{12}(x) = AB\left[e^{ik(r_1^S + r_1^D)} + e^{ik(r_2^S + r_2^D)}ight]$$

Hiệu pha:

$$\delta = k\left[(r_1^S + r_1^D) - (r_2^S + r_2^D)ight] pprox k\cdotrac{dx}{L_2} = rac{2\pi dx}{\lambda L_2}$$

Xác suất:

$$P_{12}(x) = 2|AB|^2 \left[1 + \cos\!\left(rac{2\pi dx}{\lambda L_2}ight)ight]$$

### 5. Cấu trúc toán học của ba quy tắc Feynman

**Quy tắc 1:** $P = |\phi|^2$ — Đây là Born rule, được postulate trực tiếp. Không thể suy ra từ nguyên tắc đơn giản hơn — đây là định đề căn bản.

**Quy tắc 2:** $\phi = \phi_1 + \phi_2$ — Đây là hệ quả của tính tuyến tính của phương trình Schrödinger:

$$i\hbarrac{\partial|\psiangle}{\partial t} = \hat{H}|\psiangle$$

Nếu $|\psi_1angle$ và $|\psi_2angle$ là nghiệm, thì $lpha|\psi_1angle + eta|\psi_2angle$ cũng là nghiệm → tính chất superposition là căn bản.

**Quy tắc 3:** $P = P_1 + P_2$ khi đo được — Đây là hệ quả của **decoherence** (mất kết hợp lượng tử):

Khi môi trường (photon, phonon,...) entangle với hệ theo:

$$|\Psiangle = |\phi_1angle|e_1angle + |\phi_2angle|e_2angle$$

với $\langle e_1|e_2angle pprox 0$ (môi trường phân biệt được), ma trận mật độ của hệ:

$$ho = 	ext{Tr}_{	ext{env}}|\Psiangle\langle\Psi| pprox |\phi_1angle\langle\phi_1| + |\phi_2angle\langle\phi_2|$$

Số hạng giao thoa biến mất → hành vi cổ điển.

### 6. Bất biến gauge và pha vật lý

Biên độ $\phi$ phụ thuộc vào gauge (quy ước pha). Nhưng xác suất $P = |\phi|^2$ là bất biến gauge. Tuy nhiên, **hiệu pha** giữa hai đường đi là vật lý và có thể đo được!

**Hiệu ứng Aharonov-Bohm:** Electron đi qua hai đường quanh một solenoid có từ thông $\Phi_B$. Kể cả khi $\mathbf{B} = 0$ trên đường đi của electron, vector thế $\mathbf{A}$ vẫn ảnh hưởng đến biên độ xác suất:

$$\phi_j 	o \phi_j \cdot \exp\!\left(rac{ie}{\hbar}\int_{	ext{path}_j} \mathbf{A}\cdot d\mathbf{l}ight)$$

Hiệu pha:

$$\Deltaarphi_{AB} = rac{e}{\hbar}\oint \mathbf{A}\cdot d\mathbf{l} = rac{e\Phi_B}{\hbar} = rac{2\pi\Phi_B}{\Phi_0}$$

với $\Phi_0 = h/e pprox 4.136 	imes 10^{-15}$ Wb là lượng tử từ thông (flux quantum).

**Ứng dụng:** SQUID (Superconducting QUantum Interference Device) đo chính xác $\Phi_B$ bằng cách đo hiệu pha Aharonov-Bohm giữa hai đường đi của cặp Cooper. Độ nhạy đạt $\sim 10^{-6}\Phi_0$ — sensor từ trường nhạy nhất hiện nay.

### 7. Feynman Path Integral — tổng quát hóa

Biên độ từ điểm $\mathbf{r}_a$ lúc $t_a$ đến $\mathbf{r}_b$ lúc $t_b$:

$$\phi(\mathbf{r}_b, t_b; \mathbf{r}_a, t_a) = \int_{\mathbf{r}(t_a)=\mathbf{r}_a}^{\mathbf{r}(t_b)=\mathbf{r}_b} \mathcal{D}[\mathbf{r}(t)] \exp\!\left(rac{i}{\hbar}S[\mathbf{r}(t)]ight)$$

trong đó $S = \int_{t_a}^{t_b} \mathcal{L}\, dt$ là action và tích phân lấy trên **tất cả đường đi** nối $\mathbf{r}_a$ và $\mathbf{r}_b$.

**Giới hạn cổ điển:** Khi $\hbar 	o 0$, tích phân bị dominate bởi đường đi làm cực trị $S$ (stationary phase approximation). Đây chính là nguyên lý tác dụng tối thiểu (Maupertuis/Hamilton's principle) — vật lý cổ điển!

$$\delta S = 0 \Rightarrow 	ext{Phương trình Euler-Lagrange} \Rightarrow F = ma$$

### 8. Ứng dụng kỹ thuật: Propagator trong thiết kế radar/LIDAR

Trong hệ thống LIDAR cho xe tự lái hoặc vũ khí dẫn đường, tín hiệu laser tán xạ từ mục tiêu. Biên độ tán xạ phụ thuộc vào:

- Biên độ truyền từ phát đến mục tiêu: $\phi_{	ext{prop}} \propto e^{ikr}/r$
- Biên độ tán xạ của mục tiêu: $f(	heta, \phi)$ (hàm tán xạ)
- Biên độ thu về detector: $\phi_{	ext{recv}} \propto e^{ikr'}/r'$

Cường độ tín hiệu thu:

$$I \propto |\phi_{	ext{prop}} \cdot f \cdot \phi_{	ext{recv}}|^2 = rac{|f|^2 \sigma}{r^2 r'^2}$$

Đây chính là radar equation, được suy ra từ nguyên lý lượng tử (Born rule + propagator)!

### Tổng kết cấu trúc

```
Thực tại vật lý → Trạng thái |ψ⟩ ∈ Hilbert space
                      ↓
Biên độ xác suất: φ = ⟨χ|ψ⟩ ∈ ℂ
                      ↓
Superposition (nếu không đo): φ = Σᵢ φᵢ
Decoherence (nếu có đo):       P = Σᵢ |φᵢ|²
                      ↓
Xác suất quan sát được: P = |φ|² ∈ ℝ⁺
```

---
*Exported from Feynman Bot*
