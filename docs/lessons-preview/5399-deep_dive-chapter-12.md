---
lesson_id: 5399
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-02T15:10:28.443986+00:00"
content_hash: 3bfd929b80bc
chapter_number: 12
chapter_title: Chapter 12
section_number: 4
section_title: 12–3Molecular forces
---
# ## Lực Phân Tử — Phân tích Chuyên sâu

*Source: Chapter 12 - Chapter 12 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_12.html)*

## Lực Phân Tử — Phân tích Chuyên sâu

### 1. Thế Năng Lennard-Jones

Mô hình phổ biến nhất cho lực phân tử là thế năng Lennard-Jones (LJ):

$$U(r) = 4\epsilon\left[\left(\frac{\sigma}{r}\right)^{12} - \left(\frac{\sigma}{r}\right)^6\right]$$

Lực tương ứng:

$$F(r) = -\frac{dU}{dr} = 4\epsilon\left[\frac{12\sigma^{12}}{r^{13}} - \frac{6\sigma^6}{r^7}\right]$$

Trong đó:
- $\sigma$ = khoảng cách khi $U = 0$ (kích thước hiệu dụng của nguyên tử)
- $\epsilon$ = độ sâu giếng thế (năng lượng liên kết)
- Số mũ 12: lực đẩy ngắn hạn (do Pauli exclusion principle)
- Số mũ 6: lực hút van der Waals dài hạn

**Điểm cân bằng** $r_0$ (khi $F = 0$):

$$r_0 = 2^{1/6}\sigma \approx 1.122\sigma$$

**Tuyến tính hóa quanh $r_0$:** Đặt $r = r_0 + x$ với $x \ll r_0$:

$$F \approx -\frac{d^2U}{dr^2}\bigg|_{r_0} x = -kx$$

với $k = \frac{d^2U}{dr^2}\bigg|_{r_0} = \frac{72\epsilon}{r_0^2}$

Đây là nguồn gốc của **định luật Hooke** — tuyến tính hóa của lực phân tử phi tuyến!

### 2. Lực van der Waals và Liên Kết Phân Tử

Đối với các phân tử không phân cực (O₂, N₂, Ar), lực van der Waals (London dispersion) xuất phát từ tương tác lưỡng cực tức thời:

$$U_{vdW} \approx -\frac{C_6}{r^6}$$

Hằng số $C_6$ phụ thuộc vào polarizability $\alpha$ của phân tử:
$$C_6 \approx \frac{3}{4}\frac{\alpha^2 I}{(4\pi\epsilon_0)^2}$$

với $I$ = năng lượng ion hóa đầu tiên.

**Ý nghĩa:** Phân tử lớn hơn (polarizability cao hơn) có lực van der Waals mạnh hơn. Giải thích tại sao dầu nhớt (phân tử hydrocarbon lớn) "dính" hơn nước (phân tử nhỏ).

### 3. Ứng Dụng: Tiếp Xúc Hertz và Lực Dính trong Đo Lường

**Mô hình tiếp xúc Hertz:** Khi đầu đo ruby (bán kính $R = 1.5$ mm) tiếp xúc với bề mặt phẳng bằng thép với lực $F = 0.1$ N:

Bán kính vùng tiếp xúc:
$$a = \left(\frac{3FR}{4E^*}\right)^{1/3}$$

với $E^* = \left(\frac{1-\nu_1^2}{E_1} + \frac{1-\nu_2^2}{E_2}\right)^{-1}$

Với ruby: $E_1 = 400$ GPa, $\nu_1 = 0.27$; thép: $E_2 = 210$ GPa, $\nu_2 = 0.3$:
$$E^* \approx 157 \text{ GPa}$$

$$a = \left(\frac{3 \times 0.1 \times 0.0015}{4 \times 1.57\times10^{11}}\right)^{1/3} \approx 1.3 \text{ μm}$$

Vùng tiếp xúc chỉ $\sim 1.3$ μm — nhỏ hơn bước sóng ánh sáng!

**Lực dính (adhesion) JKR model:**

$$F_{adhesion} = \frac{3}{2}\pi W_{12} R$$

với $W_{12}$ = năng lượng bề mặt ($W_{12} \approx 0.1-1$ J/m² tùy vật liệu/bề mặt).

Với $W_{12} = 0.3$ J/m², $R = 1.5$ mm:
$$F_{adhesion} = \frac{3}{2}\pi \times 0.3 \times 0.0015 \approx 2.1 \text{ mN}$$

Đây là lực dính phân tử giữ đầu đo ruby và bề mặt — không đáng kể so với lực đo 0.1 N, nhưng quan trọng ở tốc độ đo cao hay khi lực đo rất nhỏ (scanning probe microscopy).

### 4. Bài Tập: Hằng Số Đàn Hồi Tinh Thể từ Lực Phân Tử

**Bài toán:** Tinh thể NaCl có khoảng cách ion $r_0 = 0.282$ nm, năng lượng liên kết $\epsilon = 1.27$ eV. Sử dụng mô hình đơn giản lực phân tử $U \approx -A/r + B/r^n$, ước tính hằng số đàn hồi $k$ cho mỗi cặp ion Na-Cl.

**Giải:**

Từ mô hình LJ, $k = 72\epsilon/r_0^2$ (tuyến tính hóa tại điểm cân bằng):

$$k = \frac{72 \times 1.27 \times 1.6\times10^{-19}}{(0.282\times10^{-9})^2}$$

$$= \frac{72 \times 2.03\times10^{-19}}{7.95\times10^{-20}} \approx 184 \text{ N/m}$$

**Ý nghĩa:** Module đàn hồi Young của NaCl tính được từ $k$ và khoảng cách mạng tinh thể — so sánh với giá trị thực nghiệm $E_{NaCl} \approx 40$ GPa cho kết quả trong cùng bậc độ lớn.

### 5. Lực Phân Tử trong Kỹ Thuật Màng Mỏng

Trong sản xuất MEMS (Micro-Electro-Mechanical Systems):

- **Stiction** (static friction ở micro-scale): lực van der Waals giữ cấu trúc micro kết dính vào đế → phá hủy thiết bị. Giải pháp: phủ lớp self-assembled monolayer (SAM) giảm năng lượng bề mặt
- **Capillary force**: nước ngưng tụ tại khe hở micro tạo lực mao dẫn lớn → stiction. Đây là vấn đề nghiêm trọng trong CMM tại độ ẩm cao

**Công thức lực mao dẫn** tại khe hở $d$, bề mặt diện tích $A$:

$$F_{cap} = \frac{2\gamma A \cos\theta}{d}$$

với $\gamma$ = sức căng bề mặt nước (0.072 N/m), $\theta$ = góc tiếp xúc.

Ở $d = 10$ nm, $A = 1$ μm², $\theta = 0$: $F_{cap} = 2 \times 0.072 \times 10^{-12}/10^{-8} = 14.4$ μN — lực đáng kể cho cấu trúc MEMS!

### Tóm Tắt

| Lực | Phụ thuộc $r$ | Nguồn gốc | Ứng dụng |
|-----|-------------|-----------|---------|
| LJ repulsion | $r^{-13}$ | Pauli exclusion | Độ cứng vật liệu |
| van der Waals | $r^{-7}$ | Lưỡng cực tức thời | Ma sát, kết dính |
| Capillary | $d^{-1}$ | Sức căng bề mặt | Stiction MEMS |
| Hooke $kx$ | Tuyến tính | Tuyến tính hóa LJ | Mô hình đàn hồi |

---
*Exported from Feynman Bot*
