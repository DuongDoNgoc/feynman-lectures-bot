---
lesson_id: 5349
lesson_type: quiz
approval_status: approved
exported_at: "2026-02-28T14:08:59.368970+00:00"
content_hash: 6987cfcc5398
chapter_number: 6
chapter_title: Chapter 6
section_number: 4
section_title: 6–3The random walk
---
# ## Quiz: Buoc Di Ngau Nhien (Random Walk)

*Source: Chapter 6 - Chapter 6 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_06.html)*

## Quiz: Buoc Di Ngau Nhien (Random Walk)

**Cau 1:** Sau $N$ buoc ngau nhien (moi buoc $\pm 1$ voi xac suat bang nhau), khoang cach trung binh bac hai (root-mean-square) tu goc la:

A. $N$
B. $N/2$
C. $\sqrt{N}$
D. $N^2$

**Dap an: C** — $D_{\text{rms}} = \sqrt{\langle D_N^2 \rangle} = \sqrt{N}$. Do la hau qua cua tinh doc lap cac buoc: phuong sai cong lai, do do $\langle D_N^2 \rangle = N$.

---

**Cau 2:** MEMS gyroscope co Angle Random Walk = $0.1^\circ/\sqrt{\text{hr}}$. Sau 9 gio bay ma khong co GPS update, sai so goc la:

A. $0.1^\circ$
B. $0.3^\circ$
C. $0.9^\circ$
D. $0.01^\circ$

**Dap an: B** — $\theta_{\text{rms}} = 0.1 \times \sqrt{9} = 0.1 \times 3 = 0.3^\circ$. Random walk trong INS: sai so tang theo $\sqrt{t}$ khong phai $t$.

---

**Cau 3:** He so khuech tan cua phan tu khi tang len 4 lan. Khoang cach khuech tan trung binh sau cung mot thoi gian thay doi the nao?

A. Tang 4 lan
B. Tang 2 lan
C. Tang 16 lan
D. Khong thay doi

**Dap an: B** — $D_{\text{rms}} = \sqrt{2Dt}$. Khi $D$ tang 4 lan, $D_{\text{rms}}$ tang $\sqrt{4} = 2$ lan.

---

**Cau 4 (Tu luan):** He thong INS trong ten lua cua ban co gyroscope ARW = 0.05 deg/sqrt(hr) va accelerometer velocity random walk = 0.01 m/s/sqrt(hr). Ban can sai so vi tri sau 30 phut bay khong vuot qua 10 m. He thong hien tai co dap ung yeu cau khong? Neu khong, giai phap nao?

**Goi y tra loi:** Sau 30 phut = 0.5 hr, sai so goc: $0.05 \times \sqrt{0.5} \approx 0.035^\circ$. O cao do 5000 m, sai so vi tri do goc: $5000 \times \tan(0.035^\circ) \approx 3$ m. Sai so tu ARW accelerometer: $0.01 \times \sqrt{0.5} \times 3600 \approx 25$ m (sau khi chuyen don vi). Tong sai so vuot 10 m. Giai phap: (1) GPS/INS integration; (2) Zero-velocity update (ZUPT) neu co thoi diem dung; (3) Terrain matching bang ban do so. Trong thuc te, tat ca ten lua tam xa deu dung GPS + INS de bu drift.

```json
{"questions": [
  {"id": "q1", "type": "mcq", "question": "Sau N buoc ngau nhien (+/-1, xac suat bang nhau), khoang cach rms tu goc la:", "options": ["A. N", "B. N/2", "C. sqrt(N)", "D. N^2"], "answer": "C", "explanation": "D_rms = sqrt(N) vi phuong sai cong lai tuyen tinh theo so buoc."},
  {"id": "q2", "type": "mcq", "question": "MEMS gyro ARW = 0.1 deg/sqrt(hr). Sau 9 gio bay, sai so goc la:", "options": ["A. 0.1 deg", "B. 0.3 deg", "C. 0.9 deg", "D. 0.01 deg"], "answer": "B", "explanation": "theta_rms = 0.1 x sqrt(9) = 0.3 deg. Random walk: sai so tang theo sqrt(t)."},
  {"id": "q3", "type": "mcq", "question": "He so khuech tan tang 4 lan. Khoang cach khuech tan rms thay doi the nao?", "options": ["A. Tang 4 lan", "B. Tang 2 lan", "C. Tang 16 lan", "D. Khong thay doi"], "answer": "B", "explanation": "D_rms = sqrt(2Dt). Khi D tang 4 lan, D_rms tang sqrt(4) = 2 lan."},
  {"id": "q4", "type": "open", "question": "INS voi ARW=0.05 deg/sqrt(hr) va VRW=0.01 m/s/sqrt(hr). Sai so vi tri sau 30 phut co < 10 m khong?", "sample_answer": "Sai so goc ~0.035 deg, vi tri ~3 m tu ARW. Tu VRW: ~25 m. Tong vuot 10 m. Can GPS/INS integration hoac terrain matching."}
]}
```


## Quiz Questions

**Q1:** Sau N buoc ngau nhien (+/-1, xac suat bang nhau), khoang cach rms tu goc la:
- A) A. N
- B) B. N/2
- C) C. sqrt(N)
- D) D. N^2

**Correct:** C

**Explanation:** D_rms = sqrt(N) vi phuong sai cong lai tuyen tinh theo so buoc.

**Q2:** MEMS gyro ARW = 0.1 deg/sqrt(hr). Sau 9 gio bay, sai so goc la:
- A) A. 0.1 deg
- B) B. 0.3 deg
- C) C. 0.9 deg
- D) D. 0.01 deg

**Correct:** B

**Explanation:** theta_rms = 0.1 x sqrt(9) = 0.3 deg. Random walk: sai so tang theo sqrt(t).

**Q3:** He so khuech tan tang 4 lan. Khoang cach khuech tan rms thay doi the nao?
- A) A. Tang 4 lan
- B) B. Tang 2 lan
- C) C. Tang 16 lan
- D) D. Khong thay doi

**Correct:** B

**Explanation:** D_rms = sqrt(2Dt). Khi D tang 4 lan, D_rms tang sqrt(4) = 2 lan.

**Q4:** INS voi ARW=0.05 deg/sqrt(hr) va VRW=0.01 m/s/sqrt(hr). Sai so vi tri sau 30 phut co < 10 m khong?

**Correct:** N/A


---
*Exported from Feynman Bot*
