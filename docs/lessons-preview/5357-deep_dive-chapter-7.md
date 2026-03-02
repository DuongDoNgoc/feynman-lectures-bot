---
lesson_id: 5357
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-02T15:10:27.388460+00:00"
content_hash: d21f168e3be8
chapter_number: 7
chapter_title: Chapter 7
section_number: 6
section_title: 7–5Universal gravitation
---
# ## Hap Dan Newton: Ung Dung — Phan tich Chuyen sau

*Source: Chapter 7 - Chapter 7 (Section 6) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_07.html)*

## Hap Dan Newton: Ung Dung — Phan tich Chuyen sau

### Phan 1: Hinh dang Trai Dat tu hap dan va luc ly tam

Trai Dat quay voi van toc goc $\Omega = 2\pi/86400 \approx 7.27 \times 10^{-5}$ rad/s. O xu dao (vi do $\phi = 0$), luc ly tam tac dong ra ngoai:

$$F_{\text{ly tam}} = m\Omega^2 R_{\text{xu dao}} \approx m \times (7.27 \times 10^{-5})^2 \times 6.378 \times 10^6$$

$$\approx 0.0337 \text{ m/s}^2 \times m$$

So voi gia toc trong truong hap dan: $g \approx 9.81$ m/s^2, luc ly tam la $0.0337/9.81 \approx 0.34\%$ cua g. Day giai thich tai sao $g$ o xu dao ($9.78$ m/s^2) nho hon $g$ o cuc ($9.83$ m/s^2).

**O phong do $\phi$:** Luc ly tam tang dieu o xu dao:

$$F_{\text{ly tam, phap}}(\phi) = m\Omega^2 R \cos^2\phi$$

**Bien dang Trai Dat:** Trai Dat hinh ellipsoid dep voi:

$$\frac{R_{\text{xu dao}} - R_{\text{cuc}}}{R_{\text{xu dao}}} = \frac{5\Omega^2 R}{4g} \approx \frac{1}{297}$$

Tuong duong chenh lech $\approx 21.4$ km — phu hop ket qua thuc do.

**Ung dung GPS:** He thoa WGS-84 dung ellipsoid tham chieu voi $f = 1/298.257$. Sai khac voi geoid thuc (do phan bo khoi luong khong dong nhat) can ban do troi loi (geoid undulation). Vung Viet Nam: geoid undulation $\approx -20$ den $+5$ m. Neu bo qua, cao do GPS sai den 25 m — khong chap nhan duoc cho he thong vu khi chinh xac.

### Phan 2: Luc thuy trieu — Phan tich chinh xac

Luc hap dan cua Mat Trang len phan nuoc o gan (xa Mat Trang: $r - R_E$) la:

$$F_{\text{gan}} = \frac{GM_M m}{(r - R_E)^2}$$

Luc len phan nuoc o xa (xa Mat Trang: $r + R_E$):

$$F_{\text{xa}} = \frac{GM_M m}{(r + R_E)^2}$$

Luc thuy trieu (chenh lech):

$$F_{\text{thuy trieu}} = F_{\text{gan}} - F_{\text{xa}} \approx \frac{2GM_M m R_E}{r^3}$$

(Xap xi bac nhat theo $R_E/r \ll 1$)

**Luc thuy trieu giam theo $1/r^3$** — nhanh hon luc hap dan chinh ($1/r^2$). Day la ly do Mat Troi tao thuy trieu nho hon Mat Trang (du khoi luong Mat Troi lon hon rat nhieu) — vi Mat Troi o xa hon nhieu.

So sanh:

$$\frac{F_{\text{thuy trieu, MT}}}{F_{\text{thuy trieu, MS}}} = \frac{M_{\text{Mat Trang}}}{M_{\text{Mat Troi}}} \times \left(\frac{r_{\text{Mat Troi}}}{r_{\text{Mat Trang}}}\right)^3 = \frac{7.35 \times 10^{22}}{2 \times 10^{30}} \times \left(\frac{1.5 \times 10^{11}}{3.84 \times 10^8}\right)^3 \approx 2.2$$

Mat Trang tao thuy trieu manh gap 2.2 lan Mat Troi!

### Phan 3: Du bao sao Hai Vuong — Tuong thich

Leverrier (1846) giai he phuong trinh nhieu loan (perturbation equations). Sao Thien Vuong bi keo ra khoi quy dao du bao Newton boi mot luong:

$$\delta\theta \sim \text{vai chuc giay cung}$$

Nguyen nhan phai la mot hanh tinh khoi luong $M_x$ o vi tri $(r_x, \theta_x)$. He phuong trinh nhieu loan 2 an, giai bang phuong phap lap:

$$\delta\theta_{\text{ly thuyet}}(M_x, r_x, \theta_x) = \delta\theta_{\text{quan sat}}$$

Sau vai thang tinh toan tay, Leverrier du bao: hanh tinh moi o kinh do $\lambda = 325^\circ$, khoang cach $\sim 30$ AU. Quan sat thay Neptune cach vi tri du bao $0.93^\circ$ — trong gioi han tinh toan!

**Vi du so sanh trong co dien tu:** Day giong bai toan **System Identification** trong dieu khien: quan sat dau ra he thong (nhieu loan quy dao), suy ra tham so he thong (khoi luong + vi tri hanh tinh an). Leverrier dung 'dau ra' la lech vi tri sao Thien Vuong de 'suy ra tham so' la Neptune.

### Phan 4: Ung dung — Gia toc trong truong (g) chinh xac

Trong he thong IMU (Inertial Measurement Unit) cho vu khi chinh xac, accelerometer do luc rieng:

$$\mathbf{f} = \mathbf{a} - \mathbf{g}(\mathbf{r})$$

trong do $\mathbf{g}(\mathbf{r})$ la vector trong truong hap dan tai vi tri $\mathbf{r}$. Vi $g$ khong dong nhat (chenh lech $\sim 50$ mGal giua cac vung), can ban do trong truong hap dan chinh xac (gravity map) de bu:

$$\mathbf{g}(\mathbf{r}) = g_0 + \delta g_{\text{geoid}} + \delta g_{\text{dia hinh}}$$

Sai so $\delta g = 10$ mGal = $10^{-4}$ m/s^2 tich luy trong 100 giay tao sai so vi tri:

$$\delta x = \frac{1}{2} \delta g \cdot t^2 = \frac{1}{2} \times 10^{-4} \times 10^4 = 0.5 \text{ m}$$

**Day la ly do ten lua chinh xac cao can ban do trong truong hap dan (gravity map)**.

**Diem mau chot:**
- Trai Dat dep do luc ly tam: chenh lech $R_{xu dao} - R_{cuc} \approx 21$ km (theo ly thuyet $5\Omega^2 R/4g$)
- Luc thuy trieu $\propto 1/r^3$ — Mat Trang manh gap 2.2 lan Mat Troi du nhe hon nhieu
- Neptune du bao truoc khi quan sat: thanh tuu cua giai phuong trinh nhieu loan Newtonian
- IMU chinh xac can gravity map de bu sai so trong truong — $\delta g = 10$ mGal gay sai so 0.5 m sau 100 giay

---
*Exported from Feynman Bot*
