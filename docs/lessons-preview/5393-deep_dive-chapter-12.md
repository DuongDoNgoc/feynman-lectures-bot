---
lesson_id: 5393
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:03.954781+00:00"
content_hash: 9b88d37e98f6
chapter_number: 12
chapter_title: Chapter 12
section_number: 1
section_title: 12Characteristics of Force
---
# ## Đặc Tính của Lực — Phân tích Chuyên sâu

*Source: Chapter 12 - Chapter 12 (Section 1) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_12.html)*

## Đặc Tính của Lực — Phân tích Chuyên sâu

### 1. Phân Loại Hệ thống theo Tính Phức tạp của Lực

Feynman phân chia lực thành ba nhóm với tính phức tạp tăng dần:

**Nhóm 1: Lực trường cơ bản** — đơn giản, chính xác cao
- Lực hấp dẫn: $\mathbf{F} = -GmM/r^2 \hat{r}$
- Lực điện: $\mathbf{F} = q\mathbf{E}$
- Lực từ: $\mathbf{F} = q\mathbf{v}\times\mathbf{B}$

**Nhóm 2: Lực phân tử/đàn hồi** — phức tạp, cần QM để hiểu đầy đủ, nhưng có mô hình tốt
- Lực lò xo Hooke: $F = -kx$ (gần đúng trong giới hạn đàn hồi)
- Lực liên kết hóa học: phức tạp

**Nhóm 3: Lực thực nghiệm** — hiện tượng luận, xấp xỉ
- Lực cản: $F \approx cv^2$
- Lực ma sát: $F \approx \mu_k N$

### 2. Khái niệm Trường — Tại Sao Lực Cơ Bản Đơn Giản

Ý tưởng trường là: thay vì nói "vật A tác dụng lực lên vật B", ta nói "vật A tạo ra **trường** trong không gian xung quanh, và trường đó tác dụng lực lên B".

Trường điện $\mathbf{E}$ do điện tích $Q$ tại gốc tọa độ:

$$\mathbf{E}(\mathbf{r}) = \frac{Q}{4\pi\epsilon_0 r^2}\hat{r}$$

Lực lên điện tích $q$ tại điểm $\mathbf{r}$:

$$\mathbf{F} = q\mathbf{E}(\mathbf{r})$$

Phân tách rõ: $\mathbf{E}$ phụ thuộc **chỉ** vào nguồn $Q$ và vị trí; $\mathbf{F}$ phụ thuộc vào $q$. Khi $q \to 0$, $\mathbf{E}$ không đổi. Đây là định nghĩa chính xác của trường.

### 3. Lực Ma Sát — Độ Phức Tạp Thực Sự

Mô hình Coulomb: $F_f = \mu_k N$ — đơn giản nhưng thiếu sót nghiêm trọng:

- $\mu_k$ thay đổi theo nhiệt độ (đặc biệt quan trọng trong ổ trục vũ khí)
- Ở tốc độ thấp: ma sát tĩnh (static friction) khác ma sát động — gây **stick-slip**
- Bề mặt mài mòn thay đổi $\mu_k$ theo thời gian

**Mô hình LuGre** (dùng trong điều khiển servo chính xác):

$$F_f = \sigma_0 z + \sigma_1 \dot{z} + \sigma_2 v$$

$$\dot{z} = v - \frac{|v|}{g(v)}z, \quad g(v) = F_c + (F_s - F_c)e^{-(v/v_s)^2}$$

Mô hình này nắm bắt được stick-slip, hysteresis, và creep — quan trọng khi điều khiển ở độ phân giải micro-mét.

### 4. Ví dụ: Phân tích Lực trong Bàn Định Vị Piezo

Bàn định vị piezo (piezo stage) có các lực:

| Lực | Loại | Công thức xấp xỉ | Đặc điểm |
|-----|------|-----------------|----------|
| Lực piezo | Cơ bản (điện) | $F = d_{33}E \cdot A_{eff}$ | Tuyến tính theo điện áp |
| Lực đàn hồi flexure | Đàn hồi | $F = k\cdot x$ | Tuyến tính trong range |
| Lực creep | Thực nghiệm | Phức tạp, logarithmic | Phi tuyến, phụ thuộc lịch sử |
| Lực hysteresis piezo | Thực nghiệm | 10-15% của stroke | Phi tuyến, vòng kín |

Lực điện (piezo) có thể tính từ hằng số vật liệu, nhưng creep và hysteresis đòi hỏi bù trừ thực nghiệm hoặc mô hình Preisach.

### 5. Bài Tập: Phân tích Lực trong Hệ Ổ Đỡ Từ Trường

**Bài toán:** Ổ trục từ trường (magnetic bearing) giữ trục quay bằng lực từ. Nam châm điện tạo lực:
$$F = k\frac{i^2}{x^2}$$
với $i$ = dòng điện, $x$ = khe hở, $k$ = hằng số.

Tại điểm làm việc $x_0 = 0.5$ mm, $i_0 = 1$ A. Tính lực nhiễu $\delta F$ khi $x = x_0 + \delta x$, $i = i_0 + \delta i$.

**Giải (tuyến tính hóa):**

$$F = k\frac{i^2}{x^2}$$

$$\delta F = \frac{\partial F}{\partial i}\delta i + \frac{\partial F}{\partial x}\delta x = \frac{2ki_0}{x_0^2}\delta i - \frac{2ki_0^2}{x_0^3}\delta x$$

**Ý nghĩa vật lý:**
- Hệ số $\frac{2ki_0}{x_0^2} > 0$: tăng dòng → tăng lực (ổn định, điều khiển được)
- Hệ số $-\frac{2ki_0^2}{x_0^3} < 0$: tăng khe hở → giảm lực (bất ổn định → cần vòng lặp điều khiển bắt buộc)

Đây là ví dụ lực từ trường — cơ bản, tính toán được — nhưng hành vi hệ thống (bất ổn định) đòi hỏi phân tích cẩn thận.

### Tóm Tắt Kỹ Thuật

| Loại lực | Ví dụ kỹ thuật | Mô hình hóa | Điều khiển |
|----------|---------------|-------------|------------|
| Trường EM | Motor, bearing từ, piezo | Chính xác từ lý thuyết | Model-based control |
| Đàn hồi | Lò xo, flexure | Hooke (tuyến tính) | Bù offset |
| Ma sát | Vít me, đường ray | Coulomb, LuGre | Friction compensation |
| Lực cản | Damper khí/lỏng | $cv^2$, $cv$ | Look-up table, adaptive |

---
*Exported from Feynman Bot*
