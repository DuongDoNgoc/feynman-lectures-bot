---
lesson_id: 5346
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:00.062712+00:00"
content_hash: 97a4bc92aced
chapter_number: 6
chapter_title: Chapter 6
section_number: 1
section_title: 6Probability
---
# ## Quiz: Xac Suat va Su Ngau Nhien

*Source: Chapter 6 - Chapter 6 (Section 1) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_06.html)*

## Quiz: Xac Suat va Su Ngau Nhien

**Cau 1:** Neu do mot dai luong vat ly $N$ lan va lay trung binh, sai so thong ke thay doi theo:

A. Ti le thuan voi $N$
B. Ti le thuan voi $\sqrt{N}$
C. Ti le nghich voi $\sqrt{N}$
D. Khong thay doi theo $N$

**Dap an: C** — Sai so cua trung binh (Standard Error of Mean) = $\sigma/\sqrt{N}$. Do cang nhieu lan, sai so thong ke cang nho theo $1/\sqrt{N}$.

---

**Cau 2:** Trong phan phoi Poisson voi ky vong $\lambda$, do lech chuan bang:

A. $\lambda$
B. $\lambda^2$
C. $\sqrt{\lambda}$
D. $1/\lambda$

**Dap an: C** — Phan phoi Poisson co tinh chat: phuong sai bang ky vong, do do $\sigma = \sqrt{\lambda}$.

---

**Cau 3:** Hai he thong an toan doc lap, moi cai xac suat hong la 0.05. Xac suat ca hai deu hong la:

A. 0.10
B. 0.05
C. 0.0025
D. 0.0050

**Dap an: C** — $P(\text{ca hai hong}) = 0.05 \times 0.05 = 0.0025$. Redundancy giam xac suat that bai tu 5% xuong 0.25%.

---

**Cau 4 (Tu luan):** Trong he thong do luong do chinh xac cao cua ban (encoder, cam bien luc), noise do luong co phan phoi Gaussian. Ban dung ky thuat gi de giam noise? Luc nao tang so lan do khong con hieu qua?

**Goi y tra loi:** Averaging $N$ mau giam noise theo $1/\sqrt{N}$. Gioi han: (1) Nhieu he thong (systematic error, drift) khong giam duoc bang averaging; (2) Neu tin hieu thay doi nhanh, averaging nhieu lam mo tin hieu thuc; (3) Trade-off giua bandwidth va noise. Thuc te: Kalman filter toi uu hon vi vua loc noise vua giu dynamic response.

```json
{"questions": [
  {"id": "q1", "type": "mcq", "question": "Neu do mot dai luong N lan va lay trung binh, sai so thong ke thay doi theo quy luat nao?", "options": ["A. Ti le thuan voi N", "B. Ti le thuan voi sqrt(N)", "C. Ti le nghich voi sqrt(N)", "D. Khong thay doi theo N"], "answer": "C", "explanation": "Sai so cua trung binh = sigma/sqrt(N). Do cang nhieu lan, sai so thong ke cang giam theo 1/sqrt(N)."},
  {"id": "q2", "type": "mcq", "question": "Trong phan phoi Poisson voi ky vong lambda, do lech chuan bang:", "options": ["A. lambda", "B. lambda^2", "C. sqrt(lambda)", "D. 1/lambda"], "answer": "C", "explanation": "Phan phoi Poisson: phuong sai bang ky vong, sigma = sqrt(lambda)."},
  {"id": "q3", "type": "mcq", "question": "Hai he thong an toan doc lap, moi cai xac suat hong 0.05. Xac suat ca hai hong la:", "options": ["A. 0.10", "B. 0.05", "C. 0.0025", "D. 0.0050"], "answer": "C", "explanation": "P = 0.05 x 0.05 = 0.0025. Redundancy giam xac suat that bai tu 5% xuong 0.25%."},
  {"id": "q4", "type": "open", "question": "Trong do luong chinh xac cao, ban dung ky thuat gi de giam noise? Khi nao tang so lan do khong hieu qua?", "sample_answer": "Averaging giam noise theo 1/sqrt(N), nhung khong giam systematic error. Khi tin hieu thay doi nhanh, averaging lam mo tin hieu. Kalman filter toi uu hon vi vua loc noise vua giu bandwidth."}
]}
```


## Quiz Questions

**Q1:** Neu do mot dai luong N lan va lay trung binh, sai so thong ke thay doi theo quy luat nao?
- A) A. Ti le thuan voi N
- B) B. Ti le thuan voi sqrt(N)
- C) C. Ti le nghich voi sqrt(N)
- D) D. Khong thay doi theo N

**Correct:** C

**Explanation:** Sai so cua trung binh = sigma/sqrt(N). Do cang nhieu lan, sai so thong ke cang giam theo 1/sqrt(N).

**Q2:** Trong phan phoi Poisson voi ky vong lambda, do lech chuan bang:
- A) A. lambda
- B) B. lambda^2
- C) C. sqrt(lambda)
- D) D. 1/lambda

**Correct:** C

**Explanation:** Phan phoi Poisson: phuong sai bang ky vong, sigma = sqrt(lambda).

**Q3:** Hai he thong an toan doc lap, moi cai xac suat hong 0.05. Xac suat ca hai hong la:
- A) A. 0.10
- B) B. 0.05
- C) C. 0.0025
- D) D. 0.0050

**Correct:** C

**Explanation:** P = 0.05 x 0.05 = 0.0025. Redundancy giam xac suat that bai tu 5% xuong 0.25%.

**Q4:** Trong do luong chinh xac cao, ban dung ky thuat gi de giam noise? Khi nao tang so lan do khong hieu qua?

**Correct:** N/A


---
*Exported from Feynman Bot*
