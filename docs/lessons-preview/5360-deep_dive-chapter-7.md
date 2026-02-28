---
lesson_id: 5360
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-02-28T14:08:59.606823+00:00"
content_hash: ca7c3573d6b0
chapter_number: 7
chapter_title: Chapter 7
section_number: 8
section_title: 7–7What is gravity?
---
# ## Luc Hap Dan va Luc Dien Tu: So Sanh Cuong Do — Phan tich Chuyen sau

*Source: Chapter 7 - Chapter 7 (Section 8) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_07.html)*

## Luc Hap Dan va Luc Dien Tu: So Sanh Cuong Do — Phan tich Chuyen sau

### Phan 1: Tinh toan dinh luong ti so F_e / F_g

Xet hai electron, khoang cach $r$. Ca hai luc deu ty le $1/r^2$, nen ti so **khong phu thuoc r**.

**Luc Coulomb:**

$$F_e = \frac{e^2}{4\pi\epsilon_0 r^2}$$

- $e = 1.602 \times 10^{-19}$ C
- $4\pi\epsilon_0 = 1.113 \times 10^{-10}$ C^2/(N m^2)
- Tu so: $e^2/(4\pi\epsilon_0) = (1.602 \times 10^{-19})^2 / (1.113 \times 10^{-10}) = 2.307 \times 10^{-28}$ N m^2

**Luc hap dan:**

$$F_g = \frac{Gm_e^2}{r^2}$$

- $G = 6.674 \times 10^{-11}$ N m^2/kg^2
- $m_e = 9.109 \times 10^{-31}$ kg
- Tu so: $Gm_e^2 = 6.674 \times 10^{-11} \times (9.109 \times 10^{-31})^2 = 5.54 \times 10^{-71}$ N m^2

**Ti so:**

$$\frac{F_e}{F_g} = \frac{2.307 \times 10^{-28}}{5.54 \times 10^{-71}} = 4.17 \times 10^{42}$$

Day la **hang so khong thich nghi** (dimensionless constant) — ket hop cac hang so co ban cua tu nhien ($e, m_e, G, \epsilon_0$). Con so nay 'xuat hien tu hu' — khoa hoc hien tai khong co ly giai.

### Phan 2: Tai sao hap dan thong tri vu tru mac du rat yeu?

**Nguyen nhan:** Dien tich co hai dau duong am, co the trung hoa. Khoi luong chi co mot dau (duong).

Xet hai khoi vat lieu trung hoa ve dien, moi khoi co $N$ nguyen tu (dien tich net = 0):
- Luc dien tu giua hai khoi: $F_e^{\text{net}} = 0$ (trung hoa)
- Luc hap dan giua hai khoi: $F_g = G(Nm_u)^2/r^2 > 0$ (luon ton tai)

Khi $N$ tang, $F_g \propto N^2$ tang khong gioi han. Trong khi $F_e$ chi xuat hien neu co chenh lech dien tich. Cau truc vu tru lon (thien ha, sao) hinh thanh tu hap dan.

**Tinh cuong do luc dien do chenh lech dien tich nho:**

Neu trong $N$ hat nhan cua mot vat co mot phan $\alpha$ proton dung (khong co electron bu), luc dien tu xuong gap o met:

$$F_e = k_e \frac{(\alpha N e)^2}{r^2}$$

Cho $F_e = F_g$:

$$k_e (\alpha N e)^2 = G (N m_p)^2$$

$$\alpha = \frac{m_p}{e} \sqrt{\frac{G}{k_e}} = \frac{1.67 \times 10^{-27}}{1.6 \times 10^{-19}} \times \sqrt{\frac{6.67 \times 10^{-11}}{9 \times 10^9}} \approx 10^{-18}$$

Chi can $10^{-18}$ phan cua dien tich khong trung hoa la du de luc dien bang luc hap dan! Day la do chinh xac trung hoa dien tich trong vat chat — rat cao nhung huu han.

### Phan 3: Bai tap mau — Cam bien luc tu tinh so voi hap dan

**Bai toan:** Cam bien dung luong (capacitive sensor) dien tich $A = 1$ cm^2, khe ho $d = 10$ $\mu$m, dien ap $V = 100$ V. Tinh:
(a) Luc dien tu giua hai ban cuc
(b) Luc hap dan giua hai ban cuc thep (khoi luong moi ban $m = 50$ g, khoang cach $d = 10$ $\mu$m)
(c) Ti so $F_e / F_g$

**Giai:**

(a) Luc dien giua hai ban cuc tu:

$$F_e = \frac{\epsilon_0 A V^2}{2d^2} = \frac{8.85 \times 10^{-12} \times 10^{-4} \times 10^4}{2 \times (10^{-5})^2}$$

$$= \frac{8.85 \times 10^{-12}}{2 \times 10^{-10}} = 0.0443 \text{ N} \approx 44 \text{ mN}$$

(b) Luc hap dan giua hai ban thep:

$$F_g = \frac{Gm^2}{d^2} = \frac{6.674 \times 10^{-11} \times (0.05)^2}{(10^{-5})^2}$$

$$= \frac{6.674 \times 10^{-11} \times 2.5 \times 10^{-3}}{10^{-10}} = 1.67 \times 10^{-3} \text{ N} \approx 1.67 \text{ mN}$$

(c) Ti so:

$$\frac{F_e}{F_g} = \frac{44 \text{ mN}}{1.67 \text{ mN}} \approx 26$$

Luc dien manh gap 26 lan luc hap dan o khe ho 10 micromet. Trong thiet ke cam bien, luc hap dan thuong bo qua so voi luc dien (chi tro nen quan trong khi dien ap rat thap va khoi luong rat lon).

### Phan 4: Ban chat tru tuong cua dinh luat vat ly

Feynman dua ra nhan xet sau sac: cac dinh luat vat ly la nhung tuyen bo **toan hoc tru tuong** ve cac dai luong phai duoc do va tinh toan — khong co 'co che' ben trong.

**Vi du:** Dinh luat bao toan nang luong noi rang mot con so nhat dinh giu nguyen sau bat ky qua trinh nao — nhung khong noi nang luong 'la gi' theo nghia vat chat. Tuong tu, $F = Gmm'/r^2$ mo ta hanh vi, khong giai thich tai sao hap dan ton tai hoac truyen qua vac-uum nhu the nao.

Tuy nhien, **su tru tuong la suc manh**: mot cong thuc $F = Gmm'/r^2$ mo ta ca mat trang quay quanh Trai Dat, hanh tinh quay quanh Mat Troi, ten lua bay, tao trieu — tat ca bang mot cong thuc.

**Ung dung thiet ke:** Trong thiet ke he thong dieu khien, ban cung dung cac mo hinh tru tuong: $G(s) = K/(s^2 + 2\zeta\omega_n s + \omega_n^2)$ mo ta hanh vi he thong ma khong can biet chi tiet tat ca linh kien ben trong. Su tru tuong cho phep thiet ke robust, tong quat.

**Diem mau chot:**
- $F_e/F_g = 4.17 \times 10^{42}$ giua hai electron — hang so khong thich nghi chua co giai thich
- Hap dan chi phoi vu tru vi khoi luong khong co dau am (luon cong), con dien tich trung hoa
- Cam bien dung luong 10 micromet: $F_e \approx 44$ mN, $F_g \approx 1.67$ mN — luc dien manh hon 26 lan
- Dinh luat vat ly la tuyen bo toan hoc tru tuong (mo ta hanh vi, khong co co che) — su tru tuong la suc manh

---
*Exported from Feynman Bot*
