---
lesson_id: 5354
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-02T15:10:27.344321+00:00"
content_hash: 415cae2174ea
chapter_number: 7
chapter_title: Chapter 7
section_number: 1
section_title: 7The Theory of Gravitation
---
# ## Luat Hap Dan Newton va Cac Dinh Luat Kepler — Phan tich Chuyen sau

*Source: Chapter 7 - Chapter 7 (Section 1) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_07.html)*

## Luat Hap Dan Newton va Cac Dinh Luat Kepler — Phan tich Chuyen sau

### Buoc 1: Tu quan sat Kepler den dinh luat Newton

Kepler (1609-1619) mat 20 nam de ru ra 3 dinh luat tu du lieu quan sat cua Tycho Brahe. Newton (1687) mo ta tat ca bang mot luat:

$$\mathbf{F} = -G\frac{mm'}{r^2}\hat{r}$$

Dau tru chi luc hut (huong vao). Hang so hap dan:

$$G = 6.674 \times 10^{-11} \text{ N m}^2/\text{kg}^2$$

**Buoc suy luan:** Newton da chung minh rang luat $F \propto 1/r^2$ chinh xac keo theo ca 3 dinh luat Kepler. Day la thanh tuu kho hon tuong: tu mot gia thiet sinh ra ca 3 ket qua doc lap.

### Buoc 2: Chung minh dinh luat 2 Kepler (Dinh luat dien tich)

Dinh luat dien tich Kepler: vector vi tri quet dien tich deu.

Goi $\mathbf{r}$ la vector vi tri hanh tinh, $\mathbf{v} = d\mathbf{r}/dt$ la van toc.

Momen dong luong:

$$\mathbf{L} = \mathbf{r} \times m\mathbf{v}$$

Dao ham theo thoi gian:

$$\frac{d\mathbf{L}}{dt} = \mathbf{r} \times m\mathbf{a} = \mathbf{r} \times \mathbf{F}$$

Vi luc hap dan di theo huong $\mathbf{r}$ (huong vao Mat Troi), nen $\mathbf{r} \times \mathbf{F} = 0$. Do do $d\mathbf{L}/dt = 0$: **momen dong luong bao toan**.

Dien tich quet trong thoi gian $dt$:

$$dA = \frac{1}{2}|\mathbf{r} \times \mathbf{v}| dt = \frac{L}{2m} dt$$

Vi $L$ = const, $dA/dt = L/(2m)$ = const. **Day chinh la dinh luat 2 Kepler** — hau qua truc tiep cua bao toan momen dong luong!

### Buoc 3: Dinh luat 3 Kepler — Suy ra tu luc huong tam

Xet quy dao tron don gian (truong hop dac biet cua elip):

Luc hap dan bang luc huong tam:

$$G\frac{mM}{r^2} = m\frac{v^2}{r} = m\frac{4\pi^2 r}{T^2}$$

Giai ra $T^2$:

$$T^2 = \frac{4\pi^2}{GM} r^3$$

**Day chinh la dinh luat 3 Kepler!** Chu ky binh phuong ti le voi ban kinh (= ban truc lon) lap phuong. He so ti le $4\pi^2/(GM)$ chi phu thuoc vao khoi luong Mat Troi — khong phu thuoc vao hanh tinh.

### Buoc 4: Vi du thuc te — Tinh khoi luong Trai Dat

**Bai toan:** Su dung chu ky quay cua Mat Trang quanh Trai Dat de tinh khoi luong Trai Dat.

Du lieu:
- Chu ky Mat Trang: $T = 27.3$ ngay $= 2.36 \times 10^6$ s
- Khoang cach Mat Trang — Trai Dat: $r = 3.84 \times 10^8$ m
- Hang so hap dan: $G = 6.674 \times 10^{-11}$ N m^2/kg^2

**Giai:**

Tu dinh luat 3 Kepler:

$$M_{\text{Trai Dat}} = \frac{4\pi^2 r^3}{GT^2}$$

$$M = \frac{4\pi^2 \times (3.84 \times 10^8)^3}{6.674 \times 10^{-11} \times (2.36 \times 10^6)^2}$$

$$M \approx \frac{4 \times 9.87 \times 5.66 \times 10^{25}}{6.674 \times 10^{-11} \times 5.57 \times 10^{12}}$$

$$M \approx \frac{2.23 \times 10^{27}}{3.72 \times 10^2} \approx 6.0 \times 10^{24} \text{ kg}$$

Ket qua chinh xac! Chi tu quan sat chu ky va khoang cach Mat Trang, ta tinh duoc khoi luong Trai Dat.

**Y nghia ky thuat:** Cung phuong phap nay, NASA tinh khoi luong Mars bang cach quan sat chu ky ve tinh nhan tao. Tuan tu: phong ve tinh vao quy dao, do chu ky, suy ra khoi luong hanh tinh. Rat chinh xac vi vat ly Newtonian dung o thang hanh tinh.

### Buoc 5: Quy dao ten lua dan dao

Ten lua dan dao (ICBM) sau khi tat dong co (boostphase) bay tren quy dao dan dao — chinh la phan cung cua elip voi tam Trai Dat o tieu diem.

Phuong trinh quy dao elip (he toa do cuc):

$$r = \frac{a(1-e^2)}{1 + e\cos\theta}$$

trong do $a$ la ban truc lon, $e$ la do lech tam (eccentricity).

De dat muc tieu cach xa $d$ km, can giai nguoc bai toan: tu $d$ va goc phuong vi ban de, tinh goc va van toc phong can thiet. Day la bai toan bien gioi (boundary value problem) cua phuong trinh vi phan Newton — duoc may tinh tinh toan trong vai mili giay.

**Vi du so:** ICBM tam xa 10000 km: ban truc lon elip quy dao $a \approx 9000$ km (tinh tu tam Trai Dat), thoi gian bay $T_{\text{bay}} \approx 30$ phut. Van toc o nut phong: $v_0 \approx 7$ km/s (xap xi van toc quy dao thap).

**Diem mau chot:**
- Bao toan momen dong luong chung minh dinh luat 2 Kepler (dinh luat dien tich)
- Dinh luat 3 Kepler: $T^2 = 4\pi^2 r^3/(GM)$ — suy ra truc tiep tu $F = Gmm'/r^2$
- Co the tinh khoi luong thien the tu chu ky ve tinh — phuong phap chuan trong ky thuat vu tru
- Quy dao ten lua dan dao la elip Newton — cung phuong trinh mo ta hanh tinh va ICBM

---
*Exported from Feynman Bot*
