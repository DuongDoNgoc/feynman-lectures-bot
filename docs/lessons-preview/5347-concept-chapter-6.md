---
lesson_id: 5347
lesson_type: concept
approval_status: approved
exported_at: "2026-02-28T14:08:59.298421+00:00"
content_hash: ac821c4ce4d0
chapter_number: 6
chapter_title: Chapter 6
section_number: 4
section_title: 6–3The random walk
---
# ## Buoc Di Ngau Nhien (Random Walk)

*Source: Chapter 6 - Chapter 6 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_06.html)*

## Buoc Di Ngau Nhien (Random Walk)

Trong he thong dieu huong INS (Inertial Navigation System) cua ten lua hanh trinh, sau vai phut bay sai so vi tri tang khong theo ti le thuan voi thoi gian ma theo can bac hai. Tai sao? Day khong phai bug trong code — day la ban chat toan hoc cua **buoc di ngau nhien** (random walk).

### Mo hinh co ban

Tuong tuong mot nguoi bat dau tai vi tri $x = 0$. Moi buoc, nguoi do di nguoc hoac xuoi voi xac suat bang nhau (1/2). Sau $N$ buoc, nguoi do o dau?

Ket qua trung binh: $\langle D_N \rangle = 0$ (vi moi huong co xac suat bang nhau, nen trung binh van o goc). Nhung do lech chuan thu vi hon:

$$D_{\text{rms}} = \sqrt{\langle D_N^2 \rangle} = \sqrt{N}$$

Sau $N$ buoc, nguoi do **trung binh** cach goc $\sqrt{N}$ buoc — khong phai $N$ buoc!

### Phep so sanh voi ky su co dien tu

Day giong het voi **drift trong con quay hoi chuyuen (gyroscope)** cua he thong dan duong INS. Moi buoc tinh tich phan van toc de tinh vi tri co mot sai so nho ngau nhien. Sau $N$ buoc tinh tich phan, sai so vi tri tich luy khong phai $N \times \epsilon$ ma la $\sqrt{N} \times \epsilon$ — do la tai sao INS drift tang ty le voi can bac hai thoi gian bay.

Tuong tu, trong **chuyen dong Brown (Brownian motion)** cua phan tu khi: phan tu O2 trong khong khi va cham vao phan tu N2 hang ti lan moi giay, moi va cham la mot 'buoc' ngau nhien. Sau thoi gian $t$ giay, phan tu O2 khuech tan trung binh mot khoang $\sqrt{t}$ (khong phai $t$).

### Y nghia toan hoc: Tai sao la $\sqrt{N}$?

Goi $D_N$ la vi tri sau $N$ buoc. Moi buoc them $\pm 1$:

$$D_N = D_{N-1} + (\pm 1)$$

Binh phuong trung binh:

$$\langle D_N^2 \rangle = \langle D_{N-1}^2 \rangle + 2\langle D_{N-1}\rangle\langle (\pm 1) \rangle + \langle (\pm 1)^2 \rangle$$

Vi $\langle (\pm 1) \rangle = 0$ (trung binh bang 0) va $\langle (\pm 1)^2 \rangle = 1$:

$$\langle D_N^2 \rangle = \langle D_{N-1}^2 \rangle + 1$$

Uy bien nay co nghia $\langle D_N^2 \rangle = N$, do do $D_{\text{rms}} = \sqrt{N}$.

### Lien he voi tung dong xu

Random walk va tung dong xu la **toan hoc giong het nhau**. Sau $N$ lan tung, so lan chenh lech giua nguoc va xui tich luy theo $\sqrt{N}$ — chinh xac nhu random walk.

**Diem mau chot:**
- Random walk: sau $N$ buoc, khoang cach goc trung binh la $D_{\text{rms}} = \sqrt{N}$ (khong phai $N$)
- INS drift tang theo $\sqrt{t}$ vi sai so vi tri tich phan la random walk theo thoi gian
- Brownian motion (khuech tan) cung tuan theo luat $\sqrt{t}$ — chung minh thuc nghiem cua Feynman
- He so khuech tan: $D_{\text{rms}} = \sqrt{2Dt}$ trong chuyen dong Brown 3D

---
*Exported from Feynman Bot*
