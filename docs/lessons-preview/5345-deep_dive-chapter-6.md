---
lesson_id: 5345
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-02T15:10:27.113730+00:00"
content_hash: 7d4246671538
chapter_number: 6
chapter_title: Chapter 6
section_number: 1
section_title: 6Probability
---
# ## Xac Suat va Su Ngau Nhien — Phan tich Chuyen sau

*Source: Chapter 6 - Chapter 6 (Section 1) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_06.html)*

## Xac Suat va Su Ngau Nhien — Phan tich Chuyen sau

### Nen tang: Dinh nghia xac suat tan suat

Feynman bat dau Chuong 6 voi cau trich dan cua Maxwell: 'Logic thuc su cua the gioi nay nam trong phep tinh xac suat.' Dinh nghia tan suat: neu trong $N$ lan thu, su kien $A$ xay ra $N_A$ lan:

$$P(A) = \lim_{N \to \infty} \frac{N_A}{N}$$

**Dieu kien thiet yeu:** Moi lan thu phai tu trang thai **xuat phat tuong duong** — cung muc do khong biet truoc. Trong thuc nghiem, neu co correlation giua cac lan do (nhiet do phong tang dan), ket qua se bi bias — day la nguyen nhan chinh cua sai so he thong trong do luong.

### Buoc 1: Phan phoi nhi thuc (Binomial distribution)

Xet bai toan tung dong xu: $N$ lan, xac suat ngua moi lan la $p$. Xac suat nhan duoc dung $k$ lan ngua:

$$P(k; N, p) = \binom{N}{k} p^k (1-p)^{N-k}$$

- Gia tri ky vong: $\langle k \rangle = Np$
- Do lech chuan: $\sigma = \sqrt{Np(1-p)}$

**Y nghia:** Sai so tuong doi giam dan:

$$\frac{\sigma}{\langle k \rangle} = \sqrt{\frac{1-p}{Np}} \propto \frac{1}{\sqrt{N}}$$

Day la ly do do nhieu lan roi lay trung binh se giam noise theo $1/\sqrt{N}$.

### Buoc 2: Vi du thuc te — Dem phong xa trong thiet bi kiem tra vat lieu

Bo dem Geiger kiem tra vat lieu phong xa dem so phan ra trong 10 giay. Gia su toc do phan ra trung binh la $\lambda = 20$ lan/10 giay. Phan phoi so dem tuan theo Poisson:

$$P(k) = \frac{\lambda^k e^{-\lambda}}{k!}$$

- Ky vong: $\langle k \rangle = \lambda = 20$
- Do lech chuan: $\sigma = \sqrt{\lambda} = \sqrt{20} \approx 4.47$

**Ung dung ky thuat:** Phan biet tin hieu thuc ($k = 25$) voi nhieu nen ($\lambda_0 = 20$), tinh z-score:

$$z = \frac{k - \lambda_0}{\sqrt{\lambda_0}} = \frac{25 - 20}{\sqrt{20}} \approx 1.12$$

Voi $z = 1.12$, xac suat su kien nay xay ra ngau nhien la $\sim 26\%$ — **khong du tin cay** de ket luan co nguon phong xa. Can do lau hon de tich luy statistics.

### Buoc 3: Bai tap mau — He thong kiem soat chat luong

**De bai:** Day chuyen san xuat dau dan co ti le loi $p = 0.01$ (1%). Kiem tra lo 500 san pham. Tinh:
(a) So loi ky vong; (b) Do lech chuan; (c) Xac suat co it nhat 10 san pham loi

**Giai:**

(a) Ky vong: $\langle k \rangle = Np = 500 \times 0.01 = 5$

(b) Do lech chuan: $\sigma = \sqrt{Np(1-p)} = \sqrt{500 \times 0.01 \times 0.99} \approx 2.22$

(c) Voi $\lambda = 5$ (Poisson), xac suat $k \geq 10$:

$$P(k \geq 10) = 1 - \sum_{k=0}^{9} \frac{5^k e^{-5}}{k!} \approx 1 - 0.9682 = 3.18\%$$

**Y nghia:** Xac suat 3.2% khong nho trong san xuat hang loat — neu co 100 lo hang, trung binh 3 lo se co $\geq 10$ san pham loi. Day la co so thiet ke acceptance sampling plan theo tieu chuan MIL-STD-1916.

### Buoc 4: Xac suat trong co hoc luong tu

Khac voi thong ke co dien, co hoc luong tu khang dinh xac suat la **ban chat co ban**. Ham song $\Psi(x,t)$ cho biet mat do xac suat tim thay hat tai vi tri $x$:

$$P(x) = |\Psi(x,t)|^2$$

Day khong phai su thieu hieu biet — **khong ton tai** quy dao xac dinh cua electron truoc khi do.

**He qua cong nghe:** Transistor (nen tang cua moi vi mach dieu khien vu khi) hoat dong dua tren hieu ung tunnel luong tu — electron 'xuyen qua' hang rao the nang voi xac suat $P \neq 0$. Neu xac suat la 0, transistor khong hoat dong!

**Diem mau chot:**
- Xac suat tan suat: $P(A) = N_A/N$ — can dieu kien thu nghiem tuong duong
- Nhi thuc: $P(k) = C(N,k)p^k(1-p)^{N-k}$, sai so tuong doi giam theo $1/\sqrt{N}$
- Poisson: gioi han cua nhi thuc khi su kien hiem — $P(k) = \lambda^k e^{-\lambda}/k!$
- Co hoc luong tu nang xac suat tu cong cu tien loi len ban chat vat ly khong the loai bo

---
*Exported from Feynman Bot*
