---
lesson_id: 5441
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-02T15:10:29.524265+00:00"
content_hash: 0dbb3f4053fa
chapter_number: 17
chapter_title: Chapter 17
section_number: 2
section_title: 17–1The geometry of space-time
---
# ## Bien Doi Lorentz va Hinh Hoc Khong-Thoi Gian — Phan tich Chuyen sau

*Source: Chapter 17 - Chapter 17 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_17.html)*

## Bien Doi Lorentz va Hinh Hoc Khong-Thoi Gian — Phan tich Chuyen sau

### 1. Cau truc toan hoc cua bien doi Lorentz

Cho hai he quy chieu quan tinh: $S$ (dung yen) voi toa do $(x, y, z, t)$ va $S'$ (chuyen dong voi van toc $u$ theo chieu $+x$) voi toa do $(x', y', z', t')$. Bien doi Lorentz day du:

$$x' = \gamma(x - ut), \quad y' = y, \quad z' = z, \quad t' = \gamma\left(t - \frac{ux}{c^2}\right)$$

trong do $\gamma = \frac{1}{\sqrt{1 - u^2/c^2}}$ la **he so Lorentz** (Lorentz factor). Khi $u \ll c$, $\gamma \approx 1$ va ta thu lai bien doi Galileo; khi $u \to c$, $\gamma \to \infty$.

**Y nghia vat ly cua tung thanh phan:**
- $x' = \gamma(x - ut)$: vi tri trong $S'$ phu thuoc ca vi tri $x$ va thoi gian $t$ trong $S$ — co rut chieu dai (length contraction)
- $t' = \gamma(t - ux/c^2)$: thoi gian trong $S'$ phu thuoc ca thoi diem $t$ va vi tri $x$ trong $S$ — gian thoi gian (time dilation) va tinh tuong doi cua dong thoi (relativity of simultaneity)

### 2. So sanh doi xung voi phep quay

Phep quay Euclid trong mat phang $(x, y)$ mot goc $\theta$:
$$x' = x\cos\theta + y\sin\theta, \quad y' = -x\sin\theta + y\cos\theta$$

Bat bien: $x'^2 + y'^2 = x^2 + y^2$ (khoang cach bao toan).

Bien doi Lorentz trong mat phang $(x, ct)$ voi $\beta = u/c$:
$$x' = \gamma(x - \beta ct), \quad ct' = \gamma(ct - \beta x)$$

Bat bien: $c^2t'^2 - x'^2 = c^2t^2 - x^2$ (spacetime interval bao toan).

**Su khac biet can ban:** Phep quay Euclid bao toan $x^2 + y^2$ (dau duong cho ca hai). Bien doi Lorentz bao toan $c^2t^2 - x^2$ (dau am cho khong gian). Day la ly do spacetime Minkowski co 'metric' khac voi khong gian Euclid — goi la **metric Minkowski** voi chu ky $(+, -, -, -)$.

### 3. Cac he qua quan trong

**Co rut chieu dai (Length Contraction):**
Mot thanh co chieu dai $L_0$ dung yen trong $S'$. Trong $S$, chieu dai do duoc:
$$L = \frac{L_0}{\gamma} = L_0\sqrt{1 - u^2/c^2} < L_0$$

**Gian thoi gian (Time Dilation):**
Dong ho dung yen trong $S'$ chay voi chu ky $\Delta t_0$. Trong $S$, chu ky do duoc:
$$\Delta t = \gamma \Delta t_0 > \Delta t_0$$

Dong ho chuyen dong chay cham hon — day khong phai ao giac ma la thuc te vat ly da kiem nghiem voi muon trong tia vu tru va dong ho nguyen tu tren may bay.

### 4. Ung dung thuc te: He thong GPS va hieu chinh tuong doi tinh

Ve tinh GPS bay o do cao 20,200 km voi van toc $v \approx 3.87$ km/s. Co hai hieu ung tuong doi tinh:

**Thuyet tuong doi dac biet (SR):** Ve tinh chuyen dong — dong ho tren ve tinh chay **cham hon** dong ho mat dat:
$$\Delta t_{SR} \approx -7.2 \, \mu\text{s/ngay}$$

**Thuyet tuong doi tong quat (GR):** Ve tinh o tren cao, truong hap dan yeu hon — dong ho chay **nhanh hon**:
$$\Delta t_{GR} \approx +45.9 \, \mu\text{s/ngay}$$

Tong hieu chinh: $+45.9 - 7.2 = +38.7 \, \mu\text{s/ngay}$. Neu khong hieu chinh, sai so vi tri tich luy: $38.7 \times 10^{-6} \times 3 \times 10^8 \approx 11.6$ km/ngay — hoan toan vo dung cho dan duong. He thong GPS hieu chinh dong ho ve tinh chay cham hon $38.7 \, \mu\text{s/ngay}$ truoc khi phong len quy dao.

### 5. Bai tap mau: Co rut chieu dai trong dau do laser

**Dat van de:** Mot he thong interferometer dang do chieu dai mot vat. Gia su (trong tu duy thi nghiem) vat di chuyen voi $v = 0.6c$ so voi interferometer. Chieu dai nghi cua vat $L_0 = 100$ mm. Interferometer do duoc chieu dai bao nhieu?

**Buoc 1:** Tinh he so Lorentz:
$$\gamma = \frac{1}{\sqrt{1 - (0.6)^2}} = \frac{1}{0.8} = 1.25$$

**Buoc 2:** Ap dung cong thuc co rut chieu dai:
$$L = \frac{L_0}{\gamma} = \frac{100 \text{ mm}}{1.25} = 80 \text{ mm}$$

**Buoc 3:** Kiem tra bang bat bien spacetime:
Spacetime interval: $s^2 = c^2 \cdot 0^2 - (80)^2 = -6400$ mm$^2 < 0$ (space-like) — nhat quan voi phep do dong thoi hai dau vat.

**Y nghia ky thuat:** Trong thiet ke he thong do luong toc do cao (vi du: do vi tri dan trong nong sung bang sensor quang hoc), can xac dinh ro he quy chieu nao dang duoc su dung de tranh nham lan toa do.

### 6. Lien he voi he thong cam bien da truc

Trong robotics va CNC, ban thuong xuyen chuyen doi toa do giua cac he (tool frame, world frame, camera frame) dung ma tran rotation $R$ va translation $T$ — day la bien doi Galilean thuan tuy. Bien doi Lorentz tong quat hoa dieu nay vao khong-thoi gian 4D: thay vi ma tran $3 \times 3$ cho khong gian, ta can ma tran $4 \times 4$ (Lorentz boost matrix) de bien doi ca khong gian lan thoi gian dong thoi.

---
*Exported from Feynman Bot*
