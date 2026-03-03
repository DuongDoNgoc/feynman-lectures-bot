---
lesson_id: 5552
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:07.784213+00:00"
content_hash: dd1a5e253870
chapter_number: 31
chapter_title: Chapter 31
section_number: 2
section_title: 31–1The index of refraction
---
# ## Chuyên Sâu: Lý Thuyết Vi Mô Của Chiết Suất — Từ Electron Dao Động Đến Chỉ Số 

*Source: Chapter 31 - Chapter 31 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_31.html)*

## Chuyên Sâu: Lý Thuyết Vi Mô Của Chiết Suất — Từ Electron Dao Động Đến Chỉ Số Khúc Xạ

### 1. Bài Toán Đặt Ra

Xét một tấm thủy tinh mỏng trong suốt, độ dày $\Delta z$, đặt vuông góc với trục quang học $z$. Nguồn sáng $S$ ở xa bên trái, điểm quan sát $P$ ở xa bên phải. Gọi:
- $E_s$ = trường điện từ từ nguồn (sóng phẳng): $E_s = E_0 e^{i\omega(t - z/c)}$
- $E_a$ = trường từ các điện tích trong tấm kính
- $E_{\text{total}} = E_s + E_a$ (nguyên lý chồng chất)

Mục tiêu: tính $E_a$ và chứng minh rằng $E_{\text{total}}$ trông giống như sóng lan truyền với tốc độ $c/n$.

### 2. Mô Hình Dao Động Tử Lorentz

Mô hình Lorentz coi electron trong nguyên tử như khối lượng $m$ gắn vào lò xo với tần số cộng hưởng $\omega_0$. Dưới tác dụng của trường điện tới $E_s$, phương trình chuyển động:

$$m\ddot{x} + m\omega_0^2 x = eE_s = eE_0 e^{i\omega t}$$

(Tại vị trí tấm kính $z=0$: $E_s = E_0 e^{i\omega t}$)

Nghiệm cưỡng bức (steady-state):
$$x(t) = \frac{e/m}{\omega_0^2 - \omega^2} E_0 e^{i\omega t}$$

Gia tốc của electron:
$$\ddot{x}(t) = \frac{-\omega^2 e/m}{\omega_0^2 - \omega^2} E_0 e^{i\omega t}$$

Lưu ý: khi $\omega < \omega_0$: $\ddot{x}$ đồng pha với $E_0$; khi $\omega > \omega_0$: $\ddot{x}$ ngược pha.

### 3. Tính Trường Bức Xạ Từ Tấm Kính

Mỗi electron gia tốc phát ra trường bức xạ. Theo công thức Larmor (trường bức xạ từ điện tích gia tốc, trong vùng xa):

$$E_{\text{rad}} = \frac{q\ddot{x}(t_{\text{ret}})}{4\pi\varepsilon_0 c^2 r}$$

Để tính tổng đóng góp từ toàn bộ tấm kính (xem như tấm phẳng vô hạn với mật độ electron $N$ trên đơn vị thể tích), cần tích phân trên diện tích tấm kính. Feynman thực hiện tích phân này và kết quả:

$$E_a = \frac{i\omega N e \Delta z}{2\varepsilon_0 c} \cdot \hat{x}(t_{\text{ret}})$$

Thay $\hat{x}(t) = (e/m)/(\omega_0^2 - \omega^2) \cdot E_0 e^{i\omega t}$:

$$\boxed{E_a = \frac{iN e^2 \omega \Delta z}{2\varepsilon_0 mc (\omega_0^2 - \omega^2)} E_0 e^{i\omega(t - z/c)}}$$

Yếu tố $i$ (số ảo) rất quan trọng: $E_a$ **lệch pha $90°$** (vuông pha) so với $E_s$ tại cùng vị trí.

### 4. Cộng Trường Và Suy Ra Chiết Suất

Trường tổng tại điểm $P$ (cách tấm kính khoảng $z$):

$$E_{\text{total}} = E_s + E_a = E_0 e^{i\omega(t-z/c)} + \frac{iN e^2 \omega \Delta z}{2\varepsilon_0 mc (\omega_0^2 - \omega^2)} E_0 e^{i\omega(t-z/c)}$$

$$= E_0 e^{i\omega(t-z/c)} \left[1 + \frac{iNe^2\omega\Delta z}{2\varepsilon_0 mc(\omega_0^2-\omega^2)}\right]$$

Gọi $\phi = \frac{Ne^2\omega\Delta z}{2\varepsilon_0 mc(\omega_0^2-\omega^2)}$ là lượng nhỏ (tấm kính mỏng):

$$E_{\text{total}} \approx E_0 e^{i\omega(t-z/c)} \cdot e^{i\phi}$$

Vì $1 + i\phi \approx e^{i\phi}$ khi $\phi \ll 1$.

Hiệu pha $i\phi$ tương đương với tấm kính thêm độ trễ pha vào sóng:
$$e^{i\phi} = e^{i\omega(n-1)\Delta z/c}$$

So sánh:
$$\phi = \frac{(n-1)\omega\Delta z}{c} = \frac{Ne^2\omega\Delta z}{2\varepsilon_0 mc(\omega_0^2-\omega^2)}$$

Rút ra:
$$\boxed{n - 1 = \frac{Ne^2}{2\varepsilon_0 m(\omega_0^2-\omega^2)}}$$

Hoặc đầy đủ hơn:
$$n = 1 + \frac{Ne^2}{2\varepsilon_0 m(\omega_0^2-\omega^2)}$$

Đây là **công thức Lorentz** cho chiết suất — kết quả lịch sử, kết nối hằng số vĩ mô ($n$) với tính chất vi mô ($N, e, m, \omega_0$).

### 5. Phân Tích Tán Sắc (Dispersion)

Công thức trên giải thích **tán sắc** — chiết suất phụ thuộc tần số:

- $\omega \ll \omega_0$ (dưới cộng hưởng): $n > 1$, chiết suất dương và tăng khi $\omega$ tăng (**tán sắc thông thường**, normal dispersion)
- $\omega = \omega_0$: mẫu số $= 0$, cộng hưởng, mô hình cơ bản phân kỳ (thực tế cần thêm số hạng tắt dần)
- $\omega \gg \omega_0$: $n < 1$, chiết suất nhỏ hơn 1! Vận tốc pha $> c$, nhưng vận tốc nhóm (group velocity) vẫn $< c$

Để tính thực tế với tắt dần (damping), phương trình chuyển động có thêm lực cản:
$$m\ddot{x} + m\gamma\dot{x} + m\omega_0^2 x = eE_0 e^{i\omega t}$$

Nghiệm cho chiết suất phức:
$$\tilde{n}^2 = 1 + \frac{Ne^2}{\varepsilon_0 m} \cdot \frac{1}{\omega_0^2 - \omega^2 + i\gamma\omega}$$

Phần thực của $\tilde{n}$ là chiết suất, phần ảo liên quan đến hấp thụ (Beer-Lambert law).

### 6. Ứng Dụng: Đo Chiết Suất Khí Bằng Giao Thoa Kế

Ví dụ thực tế cho kỹ sư đo lường: **giao thoa kế khí** (gas refractometer) để đo nồng độ khí. Nguyên lý: đo sự thay đổi chiết suất của khí theo nồng độ bằng giao thoa laser.

Với không khí ở áp suất chuẩn: $n_{\text{air}} - 1 \approx 2.926 \times 10^{-4}$ (cho $\lambda = 589\,\text{nm}$). Từ công thức Lorentz, $n-1 \propto N$ (mật độ phân tử), do đó tỉ lệ với áp suất $P$:

$$n(P) = 1 + (n_0 - 1)\frac{P}{P_0}$$

Thay đổi mật số vân giao thoa khi thay đổi áp suất trong buồng dài $L$:
$$\Delta m = \frac{\Delta n \cdot L \cdot 2}{\lambda} = \frac{(n_0-1)L}{P_0\lambda}\Delta P$$

Ví dụ: $L = 100\,\text{mm}$, $\lambda = 633\,\text{nm}$, $\Delta P = 1\,\text{Pa}$:
$$\Delta m = \frac{2.926\times10^{-4} \times 0.1}{101325 \times 633\times10^{-9}} \times 1 \approx 4.6\times10^{-4}\,\text{vân}$$

Hệ thống phase-locked interferometry hiện đại phân giải $0.001$ vân, tương đương $\Delta P \approx 0.002\,\text{Pa}$ — độ nhạy áp suất cực cao!

### 7. Mở Rộng: Từ Một Tần Số Cộng Hưởng Đến Phổ Hấp Thụ

Thực tế, mỗi loại nguyên tử/phân tử có nhiều tần số cộng hưởng $\omega_j$ với sức mạnh dao tử $f_j$ (oscillator strength). Công thức tổng quát:

$$n^2 = 1 + \frac{Ne^2}{\varepsilon_0 m}\sum_j \frac{f_j}{\omega_j^2 - \omega^2 + i\gamma_j\omega}$$

Đây là nền tảng của **quang phổ hấp thụ** (absorption spectroscopy): mỗi đỉnh hấp thụ trong phổ tương ứng một $\omega_j$, và từ đó có thể nhận dạng phân tử.

### Tóm Tắt

| Bước | Kết quả |
|---|---|
| Phương trình chuyển động electron | $x = (e/m)E_0/(\omega_0^2-\omega^2) e^{i\omega t}$ |
| Trường bức xạ từ tấm kính | $E_a = (iNe^2\omega\Delta z)/(2\varepsilon_0 mc(\omega_0^2-\omega^2))\cdot E_s$ |
| Trường tổng (cộng) | Sóng với lệch pha $\phi = (n-1)\omega\Delta z/c$ |
| Chiết suất Lorentz | $n = 1 + Ne^2/[2\varepsilon_0 m(\omega_0^2-\omega^2)]$ |
| Tán sắc | $n$ tăng với $\omega$ (normal), $n < 1$ khi $\omega \gg \omega_0$ |

Chiết suất không phải là tính chất bí ẩn của vật liệu — nó là kết quả tất yếu của dao động electron và giao thoa sóng điện từ.

---
*Exported from Feynman Bot*
