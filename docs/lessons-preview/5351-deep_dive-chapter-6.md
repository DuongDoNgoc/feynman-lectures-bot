---
lesson_id: 5351
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-02-28T14:08:59.438826+00:00"
content_hash: 9f95ad40885c
chapter_number: 6
chapter_title: Chapter 6
section_number: 6
section_title: 6–5The uncertainty principle
---
# ## Xac Suat Luong Tu va Nguyen Ly Bat Dinh — Phan tich Chuyen sau

*Source: Chapter 6 - Chapter 6 (Section 6) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_06.html)*

## Xac Suat Luong Tu va Nguyen Ly Bat Dinh — Phan tich Chuyen sau

### Tu xac suat co dien den luong tu

Trong co hoc co dien, xac suat la cong cu xu ly phuc tap: ta dung $p(x)$ vi khong the tinh chinh xac vi tri cua $10^{23}$ phan tu. Nhung thuc su, neu biet tat ca, co the tinh chinh xac.

Co hoc luong tu thay doi quan niem nay hoan toan: **khong ton tai** vi tri xac dinh cua electron truoc khi do. Xac suat la ban chat co ban, khong phai cong cu tien loi.

### Buoc 1: Mat do xac suat va ham song

Ham song $\Psi(x, t)$ mo ta trang thai luong tu. Mat do xac suat:

$$p_1(x) = |\Psi(x,t)|^2$$

Xac suat tim thay hat trong $[x, x + \Delta x]$:

$$P = p_1(x) \Delta x = |\Psi(x,t)|^2 \Delta x$$

Dieu kien chuan hoa:

$$\int_{-\infty}^{\infty} |\Psi(x,t)|^2 \, dx = 1$$

### Buoc 2: Chung minh nguyen ly bat dinh

Xet ham song Gaussian (trang thai co do bat dinh nho nhat):

$$\Psi(x) = \left(\frac{1}{2\pi\sigma_x^2}\right)^{1/4} \exp\left(-\frac{x^2}{4\sigma_x^2}\right)$$

Bien doi Fourier sang khong gian dong luong:

$$\tilde{\Psi}(p) = \left(\frac{2\sigma_x^2}{\pi\hbar^2}\right)^{1/4} \exp\left(-\frac{\sigma_x^2 p^2}{\hbar^2}\right)$$

Do bat dinh dong luong: $\sigma_p = \hbar/(2\sigma_x)$

Tich:

$$\sigma_x \cdot \sigma_p = \frac{\hbar}{2}$$

Day la trang thai co $\sigma_x \cdot \sigma_p$ nho nhat co the — **trang thai coherent** (trang thai minimum uncertainty). Moi trang thai khac: $\sigma_x \cdot \sigma_p > \hbar/2$.

**Nguyen ly bat dinh Heisenberg:**

$$\Delta x \cdot \Delta p \geq \frac{\hbar}{2}$$

### Buoc 3: Vi du — Kich thuoc nguyen tu hydrogen

Ta co the **du doan** kich thuoc nguyen tu hydrogen chi tu nguyen ly bat dinh!

Nang luong tong cong cua electron:

$$E = \frac{p^2}{2m} - \frac{e^2}{4\pi\epsilon_0 r}$$

Neu electron bi giam trong vung co kich thuoc $a$, thi $\Delta x \sim a$ va $\Delta p \geq \hbar/(2a)$. Kin tinh $p \sim \hbar/a$. Nang luong la:

$$E \approx \frac{\hbar^2}{2ma^2} - \frac{e^2}{4\pi\epsilon_0 a}$$

Toi thieu hoa theo $a$:

$$\frac{dE}{da} = -\frac{\hbar^2}{ma^3} + \frac{e^2}{4\pi\epsilon_0 a^2} = 0$$

$$a_{\min} = \frac{4\pi\epsilon_0 \hbar^2}{me^2} = a_0 = 0.529 \text{ A}$$

**Day chinh la ban kinh Bohr!** Nguyen ly bat dinh du de du doan kich thuoc nguyen tu — neu electron bi ep qua gan hat nhan, dong nang tang nhanh hon thang the nang giam.

### Buoc 4: Mat do xac suat van toc — Phan phoi Maxwell-Boltzmann

Trong khi ban lam viec voi khi nen trong xy lanh thuy luc, van toc cua phan tu khi tuan theo phan phoi Maxwell-Boltzmann:

$$p_2(v) = 4\pi \left(\frac{m}{2\pi k_B T}\right)^{3/2} v^2 \exp\left(-\frac{mv^2}{2k_B T}\right)$$

Van toc rms: $v_{\text{rms}} = \sqrt{3k_B T/m}$

Van toc trung binh: $\langle v \rangle = \sqrt{8k_B T/(\pi m)}$

**Ung dung:** O nhiet do phong ($T = 300$ K), phan tu N2 co $v_{\text{rms}} \approx 517$ m/s. Ap suat khi nen chinh la tong dong luong tao ra boi hang ti va cham moi giay.

### Bai toan mau: Electron trong day dan nano

**De bai:** Day dan nano (quantum wire) co chieu ngang $a = 5$ nm. Tinh do bat dinh dong luong theo huong ngang va nang luong zero-point tuong ung.

**Giai:**

Do bat dinh vi tri: $\Delta x = a = 5 \times 10^{-9}$ m

Do bat dinh dong luong toi thieu:

$$\Delta p \geq \frac{\hbar}{2\Delta x} = \frac{1.055 \times 10^{-34}}{2 \times 5 \times 10^{-9}} = 1.055 \times 10^{-26} \text{ kg m/s}$$

Nang luong zero-point (nang luong thap nhat co the):

$$E_0 = \frac{(\Delta p)^2}{2m_e} = \frac{(1.055 \times 10^{-26})^2}{2 \times 9.11 \times 10^{-31}} \approx 6.1 \times 10^{-23} \text{ J} \approx 0.38 \text{ meV}$$

**Y nghia:** Nang luong nay lon hon nhiet nang $k_B T$ o nhiet do pha long he (< 4 K). Day la ly do hieu ung luong tu trong transistor 5 nm hien dai quan trong — no quyet dinh nguong dien ap hoat dong va rong o che.

**Diem mau chot:**
- Ham song: $p_1(x) = |\Psi(x)|^2$ la mat do xac suat vi tri
- Nguyen ly bat dinh: $\Delta x \cdot \Delta p \geq \hbar/2$ — ban chat co ban, khong phai han che cong nghe
- Ban kinh Bohr co the suy ra tu nguyen ly bat dinh — kich thuoc nguyen tu la ket qua can bang dong nang va the nang
- Transistor 5 nm: hieu ung luong tu (zero-point energy, tunneling) da tro nen quan trong thuc te

---
*Exported from Feynman Bot*
