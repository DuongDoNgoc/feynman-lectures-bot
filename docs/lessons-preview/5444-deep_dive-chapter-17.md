---
lesson_id: 5444
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:05.199218+00:00"
content_hash: 2a4e7f0db98d
chapter_number: 17
chapter_title: Chapter 17
section_number: 4
section_title: 17–3Past, present, and future
---
# ## Non Anh Sang va Nhan Qua Trong Khong-Thoi Gian — Phan tich Chuyen sau

*Source: Chapter 17 - Chapter 17 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_17.html)*

## Non Anh Sang va Nhan Qua Trong Khong-Thoi Gian — Phan tich Chuyen sau

### 1. Khoang cach khong-thoi gian va phan loai khoang cach

Cho hai su kien $A$ va $B$ trong khong-thoi gian, khoang cach khong-thoi gian (spacetime interval) duoc dinh nghia:

$$s^2 = c^2(t_B - t_A)^2 - (x_B - x_A)^2 - (y_B - y_A)^2 - (z_B - z_A)^2$$

Day la dai luong bat bien Lorentz — moi nguoi quan sat deu tinh duoc cung gia tri $s^2$.

**Phan loai dua tren dau cua $s^2$:**

- Time-like ($s^2 > 0$): $A$ va $B$ co the co quan he nhan qua; thu tu thoi gian la tuyet doi
- Light-like ($s^2 = 0$): $A$ va $B$ ket noi boi tia sang
- Space-like ($s^2 < 0$): $A$ va $B$ khong the co quan he nhan qua; thu tu thoi gian khong tuyet doi

### 2. Cau truc non anh sang

Non anh sang tai diem $O$ (goc toa do) trong khong-thoi gian 2D $(x, t)$:

$$c^2t^2 - x^2 = 0 \implies x = \pm ct$$

Hai duong thang nay tao thanh hai nhanh: anh sang truyen ve phia $+x$ va anh sang truyen ve phia $-x$.

**Non tuong lai** ($t > 0$): chua tat ca su kien ma $O$ co the anh huong.
**Non qua khu** ($t < 0$): chua tat ca su kien co the anh huong den $O$.
**Vung space-like**: 'ben ngoai' non — khong co quan he nhan qua voi $O$.

### 3. Tinh tuyet doi cua thu tu nhan qua

Dinh ly quan trong: Neu $s^2 > 0$ (time-like) va $t_B > t_A$ trong mot he quy chieu, thi $t'_B > t'_A$ trong **moi** he quy chieu khac.

**Chung minh:** Gia su $\Delta t = t_B - t_A > 0$ va $c^2\Delta t^2 > \Delta x^2$ (time-like). Trong he $S'$ chuyen dong voi van toc $v$:
$$\Delta t' = \gamma\left(\Delta t - \frac{v \Delta x}{c^2}\right)$$

De $\Delta t' < 0$, can: $v > c^2\Delta t/\Delta x$. Nhung $c\Delta t > \Delta x$ (time-like condition), nen $c^2\Delta t/\Delta x > c$. Vay can $v > c$ — vi pham thuyet tuong doi. Mau thuan. (QED)

**He qua:** Quan he nhan qua (cause-effect) duoc bao toan trong moi he quy chieu quan tinh.

### 4. Ung dung: Gioi han toc do truyen tin hieu trong he thong dieu khien

Xet he thong phao phong khong voi cam bien radar o vi tri $A$ (x=0) va he thong khai hoa o vi tri $B$ ($x = 10$ km). Muc tieu bay voi $v_{target} = 300$ m/s. Radar phat hien muc tieu tai thoi diem $t_0$.

**Phan tich nhan qua:**
- Tin hieu dieu khien tu $A$ den $B$ qua cap quang (toc do $\approx 2\times10^8$ m/s): do tre $\Delta t = 10000/(2\times10^8) = 50 \, \mu\text{s}$.
- Trong 50 us, muc tieu di chuyen: $\Delta x_{target} = 300 \times 50\times10^{-6} = 0.015$ m = 1.5 cm.
- Neu yeu cau do chinh xac 10 cm: do tre chap nhan duoc la $0.1/300 = 333 \, \mu\text{s}$ — du voi cap quang.
- Neu thong qua radio 4G (latency ~50 ms): $\Delta x_{target} = 300 \times 0.05 = 15$ m — hoan toan khong chap nhan duoc.

**Day la 'nhan qua ky thuat'** — khong phai gioi han thuyet tuong doi, nhung nguyen ly la giong nhau: do tre truyen thong xac dinh vung 'qua khu nhan qua' cua he thong dieu khien.

### 5. Thach thuc: Dong bo trong he phan tan

Trong he thong do luong phan tan (distributed measurement) voi nhieu cam bien, lam the nao de dong bo thoi gian giua chung? Giao thuc NTP (Network Time Protocol) cho phep dong bo den milli-giay. Giao thuc PTP (Precision Time Protocol, IEEE 1588) dat micro-giay. Nhung ngay ca voi PTP, cac cam bien o xa nhau hang km van co su kien 'dong thoi' phu thuoc vao he quy chieu — dieu nay khong quan trong o toc do thong thuong nhung la nguyen ly quan trong can hieu.

### 6. Bai tap mau: Phan loai khoang cach spacetime

**De bai:** Hai su kien xay ra trong thi nghiem:
- Su kien $A$: tia laser bat luc $t_A = 0$, $x_A = 0$
- Su kien $B$: cam bien thu nhan tin hieu luc $t_B = 10$ ns, $x_B = 2$ m

Hoi $A$ va $B$ co khoang cach time-like hay space-like?

**Giai:**

Buoc 1: Tinh $c \cdot \Delta t = 3\times10^8 \times 10\times10^{-9} = 3$ m

Buoc 2: Tinh $\Delta x = 2$ m

Buoc 3: Tinh spacetime interval:
$$s^2 = c^2\Delta t^2 - \Delta x^2 = (3)^2 - (2)^2 = 9 - 4 = 5 \, \text{m}^2 > 0$$

**Ket luan:** $s^2 > 0$ — time-like interval. Tia sang truyen 3 m trong 10 ns, nhung khoang cach $A$ den $B$ chi 2 m — tin hieu co the truyen tu $A$ den $B$ (thay chi anh sang cung duoc). Quan he nhan qua co the: $A$ co the gay ra $B$.

**Kiem tra them:** Neu $x_B = 5$ m: $s^2 = 9 - 25 = -16 < 0$ — space-like — $A$ khong the gay ra $B$ — khong the la tin hieu nhan qua.

---
*Exported from Feynman Bot*
