---
lesson_id: 5344
lesson_type: concept
approval_status: approved
exported_at: "2026-02-28T14:08:59.194135+00:00"
content_hash: 48eddba33d36
chapter_number: 6
chapter_title: Chapter 6
section_number: 1
section_title: 6Probability
---
# ## Xac Suat va Su Ngau Nhien trong Vat Ly

*Source: Chapter 6 - Chapter 6 (Section 1) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_06.html)*

## Xac Suat va Su Ngau Nhien trong Vat Ly

Tai sao radar cua he thong phong thu ten lua khong the xac dinh chinh xac 100% vi tri muc tieu, du cong nghe da cuc ky tien tien? Tai sao cam bien ap suat trong he thong thuy luc luon co noise nhat dinh du da loc tin hieu can than? Cau tra loi nam o khai niem nen tang: **xac suat va su ngau nhien** — khong phai su yeu kem cong nghe, ma la ban chat cua tu nhien.

### Xac suat la gi?

Xac suat la cach ta dinh luong **muc do khong chac chan** ve mot su kien. Neu tung dong xu $N$ lan va mat ngua xuat hien $N_A$ lan, xac suat mat ngua la:

$$P = \frac{N_A}{N}$$

Khi $N \to \infty$, ti le nay hoi tu den gia tri thuc su cua xac suat. Day la **dinh nghia tan suat** cua xac suat. Quan trong: moi lan quan sat phai trong dieu kien tuong duong, khong co thong tin tien nghiem (nhu nhin bai doi thu trong poker).

### Phep so sanh voi ky su co dien tu

Hay nghi den **encoder goc quay** trong servo motor. Moi lan doc encoder, ban nhan duoc gia tri vi tri voi mot luong noise nhat dinh. Neu do 1000 lan o cung vi tri, ban se nhan phan phoi Gaussian xung quanh gia tri thuc. Khong phai motor sai, khong phai encoder hong — day la ban chat thong ke cua phep do. **Xac suat chinh la cong cu mo ta hanh vi he thong trong su bat dinh.**

Tuong tu, khi thiet ke he thong kiem soat vu khi voi vong lap PID, sai so steady-state khong bao gio bang dung 0 — luon co fluctuation ngau nhien do nhieu dien, rung dong co hoc, thay doi nhiet do. Mo hinh xac suat giup phan tich va toi uu he thong.

### Tu dong xu den nguyen tu

Feynman dat cau hoi: xac suat co phai chi la cong cu tien loi khi thieu thong tin, hay la ban chat thuc su cua tu nhien?

Co hoc luong tu tra loi: **xac suat la ban chat thuc su**. Khong phai vi ta khong biet vi tri electron — ma vi electron **thuc su khong co** vi tri xac dinh truoc khi do. Day la buoc nhay triet hoc lon.

O thang vi mo (sensor, servo, robot), ta dung xac suat vi qua nhieu bien so de tinh het. O thang vi mo (nguyen tu, electron), xac suat la **bat buoc ve mat vat ly**.

### Quy tac to hop xac suat

Hai quy tac co ban:
- **Cong (OR):** $P(A \text{ hoac } B) = P(A) + P(B)$ (neu xung khac)
- **Nhan (AND):** $P(A \text{ va } B) = P(A) \times P(B)$ (neu doc lap)

**Vi du:** He thong an toan vu khi co 2 co che doc lap, moi cai xac suat hoat dong dung 99%. Xac suat ca hai deu hoat dong dung:

$$P = 0.99 \times 0.99 = 0.9801$$

Xac suat it nhat mot cai hoat dong dung:

$$P = 1 - (1-0.99)^2 = 1 - 0.0001 = 0.9999$$

Day la co so thiet ke **redundancy** trong he thong an toan vu khi va tu dong hoa.

**Diem mau chot:**
- Xac suat dinh luong su khong chac chan: $P = N_A/N$ khi so lan thu $N$ du lon
- Dieu kien quan trong: moi quan sat phai trong dieu kien tuong duong, khong co thong tin tien nghiem
- O thang vi mo: xac suat la cong cu xu ly phuc tap; o thang luong tu: xac suat la ban chat tu nhien
- Quy tac nhan (AND) cho su kien doc lap la nen tang thiet ke du phong trong vu khi va tu dong hoa

---
*Exported from Feynman Bot*
