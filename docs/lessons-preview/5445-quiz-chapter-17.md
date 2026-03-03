---
lesson_id: 5445
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:05.225214+00:00"
content_hash: d1efce45030c
chapter_number: 17
chapter_title: Chapter 17
section_number: 4
section_title: 17–3Past, present, and future
---
# ## Quiz: Non Anh Sang va Nhan Qua Trong Khong-Thoi Gian

*Source: Chapter 17 - Chapter 17 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_17.html)*

## Quiz: Non Anh Sang va Nhan Qua Trong Khong-Thoi Gian

### Cau 1

Khoang cach khong-thoi gian giua hai su kien la $s^2 = c^2\Delta t^2 - \Delta x^2 < 0$ (space-like). Dieu do co nghia la:

A. Hai su kien xay ra cung luc
B. Hai su kien co the co quan he nhan qua
C. Hai su kien khong the co quan he nhan qua
D. Hai su kien ket noi voi nhau boi mot tia sang

**Dap an: C**
*Giai thich:* Space-like interval ($s^2 < 0$) co nghia la khoang cach khong gian $\Delta x > c\Delta t$ — khong co tin hieu nao (ke ca anh sang) co the truyen tu su kien nay den su kien kia trong thoi gian do. Do do khong the co quan he nhan qua. Thu tu thoi gian cua hai su kien khong tuyet doi — tuy he quy chieu, su kien nao cung co the xay ra 'truoc.'

---

### Cau 2

Neu hai su kien co khoang cach time-like ($s^2 > 0$) va $t_B > t_A$ trong he $S$, thi trong he $S'$ dang chuyen dong:

A. $t'_B$ co the nho hon $t'_A$ — thu tu thoi gian co the dao nguoc
B. $t'_B > t'_A$ luon luon — thu tu nhan qua duoc bao toan
C. $t'_B = t'_A$ — hai su kien dong thoi trong $S'$
D. Khong xac dinh duoc

**Dap an: B**
*Giai thich:* Voi time-like interval, thu tu thoi gian la tuyet doi — moi nguoi quan sat dong y $B$ xay ra sau $A$. Dieu nay bao dam tinh nhan qua: neu $A$ gay ra $B$, khong he quy chieu nao thay $B$ xay ra truoc $A$. Chung minh: de dao nguoc thu tu can van toc $v > c$ — vi pham thuyet tuong doi.

---

### Cau 3

Radar tai $x = 0$ phat hien muc tieu luc $t = 0$. He thong khai hoa o $x = 1$ m. Toc do truyen tin hieu dien trong cap: $v_{signal} = 2\times10^8$ m/s. Su kien 'lenh khai hoa den he thong' va su kien 'radar phat hien' co khoang cach loai gi?

A. Space-like — khong the co quan he nhan qua
B. Light-like — tin hieu truyen dung bang toc do anh sang
C. Time-like — co the co quan he nhan qua
D. Khong xac dinh duoc tu thong tin da cho

**Dap an: C**
*Giai thich:* Thoi gian tin hieu truyen 1 m voi $v = 2\times10^8$ m/s: $\Delta t = 5$ ns. Trong thoi gian do, anh sang truyen $c \cdot \Delta t = 1.5$ m $> 1$ m = $\Delta x$. Vay $s^2 = (1.5)^2 - (1)^2 = 1.25 > 0$ — time-like. Tin hieu truyen cham hon anh sang la duoc — van co quan he nhan qua.

---

### Cau 4 (Tu luan)

**Cau hoi:** Trong thiet ke he thong dieu khien cho vu khi dan duong, khai niem 'non anh sang' co ung dung thuc te nhu the nao? Hay giai thich tai sao do tre truyen thong (communication latency) la mot rang buoc vat ly co ban chu khong chi la gioi han ky thuat, va lien he voi thiet ke he thong real-time cua ban.

**Goi y tra loi mau:** Do tre truyen thong xuat phat tu gioi han toc do truyen tin hieu (toi da la $c$). Voi he thong dieu khien phan tan: cam bien do tai vi tri $A$ luc $t_0$, thong tin chi co the den bo dieu khien o $B$ sau thoi gian $\Delta t \geq d_{AB}/c$ — gioi han vat ly bat kha xam pham. Trong thuc te, tin hieu dien trong day dong truyen voi $v \approx 0.6c$, song radio $\approx 0.95c$, nen gioi han thuc te ngat hon ly thuyet. He qua thiet ke: dung model du doan (predictive control — MPC, Kalman filter) de bu dap latency von co — khong the 'tat' latency, chi co the du doan. Tuong tu nhu viec khong the lien lac tuc thi voi cac su kien trong vung space-like cua non anh sang.

---

```json
{
  "questions": [
    {
      "id": "q1",
      "type": "mcq",
      "question": "Khoang cach khong-thoi gian $s^2 = c^2\\Delta t^2 - \\Delta x^2 < 0$ (space-like) co nghia la:",
      "options": [
        "A. Hai su kien xay ra cung luc",
        "B. Hai su kien co the co quan he nhan qua",
        "C. Hai su kien khong the co quan he nhan qua",
        "D. Hai su kien ket noi boi mot tia sang"
      ],
      "answer": "C",
      "explanation": "Space-like: $\\Delta x > c\\Delta t$ — khong tin hieu nao truyen kip. Thu tu thoi gian khong tuyet doi, khong co quan he nhan qua. Tuy he quy chieu, su kien nao cung co the 'truoc.'"
    },
    {
      "id": "q2",
      "type": "mcq",
      "question": "Hai su kien co khoang cach time-like ($s^2 > 0$) va $t_B > t_A$ trong he $S$. Trong he $S'$ dang chuyen dong:",
      "options": [
        "A. $t'_B$ co the nho hon $t'_A$ — thu tu dao nguoc",
        "B. $t'_B > t'_A$ luon luon — thu tu nhan qua duoc bao toan",
        "C. $t'_B = t'_A$ — dong thoi trong $S'$",
        "D. Khong xac dinh duoc"
      ],
      "answer": "B",
      "explanation": "Time-like interval: thu tu thoi gian tuyet doi. De dao nguoc can $v > c$ — bat kha thi. Tinh nhan qua duoc bao toan trong moi he quy chieu quan tinh."
    },
    {
      "id": "q3",
      "type": "mcq",
      "question": "Radar o $x=0$ phat hien muc tieu luc $t=0$. Lenh truyen qua cap den $x=1$ m voi toc do $2\\times10^8$ m/s. Khoang cach spacetime giua hai su kien la:",
      "options": [
        "A. Space-like — khong the co quan he nhan qua",
        "B. Light-like — truyen dung bang $c$",
        "C. Time-like — co the co quan he nhan qua",
        "D. Khong xac dinh"
      ],
      "answer": "C",
      "explanation": "$\\Delta t = 5$ ns, $c\\Delta t = 1.5$ m $> \\Delta x = 1$ m => $s^2 = (1.5)^2 - (1)^2 = 1.25 > 0$ => time-like. Tin hieu truyen cham hon $c$ van du de co quan he nhan qua."
    },
    {
      "id": "q4",
      "type": "open",
      "question": "Trong thiet ke he thong dieu khien cho vu khi dan duong, tai sao do tre truyen thong (communication latency) la rang buoc vat ly co ban? Lien he voi non anh sang va thiet ke he thong real-time.",
      "sample_answer": "Do tre truyen thong la he qua truc tiep cua gioi han toc do truyen tin hieu <= c. Thong tin tu cam bien o $A$ den bo dieu khien o $B$ can it nhat $\\Delta t_{min} = d_{AB}/c$ — gioi han vat ly bat kha xam pham. Cap dong truyen ~0.6c, song radio ~0.95c. He qua thiet ke: dung predictive control (MPC, Kalman filter) de du doan trang thai tuong lai va bu dap latency von co — khong the xoa bo, chi co the du doan."
    }
  ]
}
```


## Quiz Questions

**Q1:** Khoang cach khong-thoi gian $s^2 = c^2\Delta t^2 - \Delta x^2 < 0$ (space-like) co nghia la:
- A) A. Hai su kien xay ra cung luc
- B) B. Hai su kien co the co quan he nhan qua
- C) C. Hai su kien khong the co quan he nhan qua
- D) D. Hai su kien ket noi boi mot tia sang

**Correct:** C

**Explanation:** Space-like: $\Delta x > c\Delta t$ — khong tin hieu nao truyen kip. Thu tu thoi gian khong tuyet doi, khong co quan he nhan qua. Tuy he quy chieu, su kien nao cung co the 'truoc.'

**Q2:** Hai su kien co khoang cach time-like ($s^2 > 0$) va $t_B > t_A$ trong he $S$. Trong he $S'$ dang chuyen dong:
- A) A. $t'_B$ co the nho hon $t'_A$ — thu tu dao nguoc
- B) B. $t'_B > t'_A$ luon luon — thu tu nhan qua duoc bao toan
- C) C. $t'_B = t'_A$ — dong thoi trong $S'$
- D) D. Khong xac dinh duoc

**Correct:** B

**Explanation:** Time-like interval: thu tu thoi gian tuyet doi. De dao nguoc can $v > c$ — bat kha thi. Tinh nhan qua duoc bao toan trong moi he quy chieu quan tinh.

**Q3:** Radar o $x=0$ phat hien muc tieu luc $t=0$. Lenh truyen qua cap den $x=1$ m voi toc do $2\times10^8$ m/s. Khoang cach spacetime giua hai su kien la:
- A) A. Space-like — khong the co quan he nhan qua
- B) B. Light-like — truyen dung bang $c$
- C) C. Time-like — co the co quan he nhan qua
- D) D. Khong xac dinh

**Correct:** C

**Explanation:** $\Delta t = 5$ ns, $c\Delta t = 1.5$ m $> \Delta x = 1$ m => $s^2 = (1.5)^2 - (1)^2 = 1.25 > 0$ => time-like. Tin hieu truyen cham hon $c$ van du de co quan he nhan qua.

**Q4:** Trong thiet ke he thong dieu khien cho vu khi dan duong, tai sao do tre truyen thong (communication latency) la rang buoc vat ly co ban? Lien he voi non anh sang va thiet ke he thong real-time.

**Correct:** N/A


---
*Exported from Feynman Bot*
