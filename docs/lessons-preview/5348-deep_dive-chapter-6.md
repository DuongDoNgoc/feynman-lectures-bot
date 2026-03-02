---
lesson_id: 5348
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-02T15:10:27.199687+00:00"
content_hash: e4317baabcd5
chapter_number: 6
chapter_title: Chapter 6
section_number: 4
section_title: 6–3The random walk
---
# ## Buoc Di Ngau Nhien (Random Walk) — Phan tich Chuyen sau

*Source: Chapter 6 - Chapter 6 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_06.html)*

## Buoc Di Ngau Nhien (Random Walk) — Phan tich Chuyen sau

### Dinh nghia va mo hinh toan hoc

Buoc di ngau nhien (random walk) la mo hinh: nguoi choi bat dau tai $x = 0$, moi buoc di $+1$ hoac $-1$ voi xac suat $p = 1/2$ moi huong. Goi $D_N$ la vi tri sau $N$ buoc.

**Ky vong:** $\langle D_N \rangle = 0$ (vi doi xung)

**Binh phuong trung binh:** Xet buoc thu $N$:

$$D_N = D_{N-1} + \delta_N$$

trong do $\delta_N = \pm 1$ voi xac suat bang nhau.

$$\langle D_N^2 \rangle = \langle (D_{N-1} + \delta_N)^2 \rangle = \langle D_{N-1}^2 \rangle + 2\langle D_{N-1} \delta_N \rangle + \langle \delta_N^2 \rangle$$

Vi $D_{N-1}$ va $\delta_N$ doc lap, $\langle D_{N-1} \delta_N \rangle = \langle D_{N-1} \rangle \cdot \langle \delta_N \rangle = 0$. Va $\langle \delta_N^2 \rangle = 1$. Do do:

$$\langle D_N^2 \rangle = \langle D_{N-1}^2 \rangle + 1$$

Ap dung de quy voi $\langle D_1^2 \rangle = 1$:

$$\langle D_N^2 \rangle = N$$

Ket qua:

$$D_{\text{rms}} = \sqrt{\langle D_N^2 \rangle} = \sqrt{N}$$

### Mo rong: Buoc co do dai tuy y

Neu moi buoc co do dai $a$ (khong phai 1), thi sau $N$ buoc:

$$D_{\text{rms}} = a\sqrt{N}$$

Day la dang tong quat hon, quan trong cho ung dung vat ly.

### Vi du thuc te: Drift cua con quay INS

He thong INS (Inertial Navigation System) trong ten lua hanh trinh tich phan van toc do de tinh vi tri. Moi buoc tinh phan (sample) co sai so ngau nhien $\epsilon_i$. Sai so vi tri sau $N$ buoc:

$$\Delta x_N = \sum_{i=1}^{N} \epsilon_i \cdot \Delta t$$

Vi $\epsilon_i$ doc lap voi $\langle \epsilon_i \rangle = 0$ va $\langle \epsilon_i^2 \rangle = \sigma^2$:

$$\langle \Delta x_N^2 \rangle = N \sigma^2 (\Delta t)^2 = \sigma^2 \Delta t \cdot (N \Delta t) = \sigma^2 \Delta t \cdot T$$

trong do $T = N \Delta t$ la tong thoi gian bay. Do do:

$$\Delta x_{\text{rms}} = \sigma \sqrt{\Delta t} \cdot \sqrt{T}$$

**Y nghia:** Sai so vi tri tang theo $\sqrt{T}$ — sau 1 gio bay, sai so tan lon gap $\sqrt{60} \approx 7.7$ lan so voi sau 1 phut. Day la ly do he thong GPS update thuong xuyen de reset drift cua INS.

**Bai toan cu the:** MEMS gyroscope co Angle Random Walk (ARW) = 0.1 deg/sqrt(hr). Sau 1 gio bay, sai so goc la:

$$\theta_{\text{rms}} = 0.1 \times \sqrt{1} = 0.1^\circ$$

Sau 4 gio bay:

$$\theta_{\text{rms}} = 0.1 \times \sqrt{4} = 0.2^\circ$$

Chuyen thanh sai so vi tri (bay o cao do 10 km): $\Delta x = 10000 \times \tan(0.2^\circ) \approx 35$ m. Day la tai sao ten lua hanh trinh tam xa can GPS hoac terrain matching de bu drift.

### Lien he voi chuyen dong Brown

Phan tu khi (oxy trong khong khi) va cham voi cac phan tu khac hang $\sim 10^9$ lan/giay. Moi va cham la mot 'buoc' ngau nhien voi do dai trung binh = **duong tu do trung binh** $\lambda \approx 68$ nm (o ap suat khi quyen). Sau $t$ giay, khoang cach khuech tan:

$$D_{\text{rms}} = \sqrt{2Dt}$$

trong do $D$ la he so khuech tan. Voi O2 trong khong khi: $D \approx 2 \times 10^{-5}$ m^2/s. Sau $t = 1$ s: $D_{\text{rms}} = \sqrt{2 \times 2 \times 10^{-5}} \approx 6.3$ mm. Sau $t = 100$ s: $D_{\text{rms}} \approx 63$ mm — tang $\sqrt{100} = 10$ lan, khong phai 100 lan!

### Ung dung: Do nhieu (noise) trong cam bien analog

Nhieu Johnson (thermal noise) trong dien tro la vi du kinh dien cua random walk: cac electron bi tan xa ngau nhien boi phonon (rung dong mang tinh the). Mat do pho cong suat nhieu phang (white noise). Khi tich phan nhieu nay theo thoi gian (trong ADC, tich phan pha), bien do tang theo $\sqrt{f}$ — chinh xac la random walk trong mien tan so.

**Bieu thuc nhieu Johnson:**

$$V_{\text{rms}} = \sqrt{4k_B T R \Delta f}$$

trong do $k_B = 1.38 \times 10^{-23}$ J/K, $T$ la nhiet do, $R$ la dien tro, $\Delta f$ la bang thong. Tang $R$ len 4 lan chi tang noise len 2 lan ($\sqrt{4} = 2$) — dac tinh random walk!

**Diem mau chot:**
- Random walk: $D_{\text{rms}} = \sqrt{N}$ (voi buoc don vi), chung minh tu tinh doc lap cac buoc
- INS drift tang theo $\sqrt{T}$ — can GPS update de bu drift (tan so update phu thuoc yeu cau do chinh xac)
- Chuyen dong Brown: $D_{\text{rms}} = \sqrt{2Dt}$ — he so khuech tan $D$ mo ta toc do khuech tan
- Nhieu Johnson trong dien tro cung la random walk — giai thich tai sao $V_{\text{rms}} \propto \sqrt{\Delta f}$

---
*Exported from Feynman Bot*
