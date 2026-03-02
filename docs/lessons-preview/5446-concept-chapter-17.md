---
lesson_id: 5446
lesson_type: concept
approval_status: approved
exported_at: "2026-03-02T15:10:29.663089+00:00"
content_hash: 434778206a04
chapter_number: 17
chapter_title: Chapter 17
section_number: 6
section_title: 17–5Four-vector algebra
---
# ## Four-Vector: Ky Hieu Thong Nhat Cho Khong Gian Va Thoi Gian

*Source: Chapter 17 - Chapter 17 (Section 6) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_17.html)*

## Four-Vector: Ky Hieu Thong Nhat Cho Khong Gian Va Thoi Gian

Khi ban lap trinh cho robot voi nhieu khop, ban dung vector 3D $\mathbf{p} = (p_x, p_y, p_z)$ de bieu dien vi tri. Nhung trong thuyet tuong doi, khong gian va thoi gian khong the tach roi — can mot vector 4 chieu de mo ta day du. Day la y tuong dang sau **four-vector** — va Feynman noi rat dung: dung coi thuong ky hieu, hay phat minh ra chung, vi toan hoc phan lon la nghe thuat phat minh ky hieu tot hon.

### Tu vector 3D den vector 4D

Trong khong gian 3D thong thuong, vector dong luong duoc viet $\mathbf{p}$ voi ba thanh phan $p_x, p_y, p_z$. Ta cung viet $p_i$ de noi 'thanh phan thu $i$', voi $i = x, y, z$.

Trong khong-thoi gian 4D, ta dinh nghia **four-vector dong luong-nang luong** $p_\mu$ voi bon thanh phan, trong do $\mu$ chay qua $t, x, y, z$:

$$p_\mu = (p_t, p_x, p_y, p_z) = \left(\frac{E}{c}, p_x, p_y, p_z\right)$$

Thanh phan 'thoi gian' $p_t = E/c$ chinh la nang luong chia cho $c$ — day khong phai quy uoc tuy tien, ma la he qua tat yeu cua cau truc khong-thoi gian. Tuong tu nhu khi quay he truc toa do, $x$ va $y$ tron lan nhau; khi 'quay' trong khong-thoi gian (bien doi Lorentz), $p_x$ va $p_t = E/c$ tron lan vao nhau.

### Tich vo huong trong khong-thoi gian

Trong khong gian 3D, tich vo huong (dot product) $\mathbf{A} \cdot \mathbf{B} = A_x B_x + A_y B_y + A_z B_z$ bat bien duoi phep quay. Trong khong-thoi gian, dai luong tuong tu la **tich vo huong Minkowski**:

$$\sideset{}{'}{\sum_\mu} A_\mu A_\mu = A_t^2 - A_x^2 - A_y^2 - A_z^2$$

Dau nhay tren $\sum'$ nhac nho: so hang thoi gian co dau duong, ba so hang khong gian co dau am. Day khong phai loi ky hieu — day la ban chat metric Minkowski cua khong-thoi gian.

Ap dung cho four-vector dong luong:

$$p_\mu p_\mu = \frac{E^2}{c^2} - p_x^2 - p_y^2 - p_z^2 = m_0^2 c^2$$

Day la **quan he nang luong-dong luong tuong doi tinh** — bat bien Lorentz, dung trong moi he quy chieu.

### An du: Ma tran chuyen doi he toa do trong robotics

Trong he thong robot hay may do CMM (Coordinate Measuring Machine) cua ban, ban thuong xuyen chuyen doi giua cac he toa do: tool frame, world frame, camera frame. Moi phep chuyen doi la mot ma tran $4\times4$ (homogeneous transformation matrix) gom ma tran quay $3\times3$ va vector dich chuyen.

Four-vector trong thuyet tuong doi dong vai tro tuong tu — nhung thay vi chuyen doi he toa do khong gian, ta chuyen doi he quy chieu khong-thoi gian. Bien doi Lorentz la ma tran $4\times4$ (Lorentz boost matrix) tac dong len four-vector. Diem mau chot: cung nhu homogeneous transformation bao toan khoang cach Euclid, bien doi Lorentz bao toan tich vo huong Minkowski.

### Bao toan four-vector dong luong-nang luong

Dinh luat bao toan nang luong va bao toan dong luong, viet dang four-vector:

$$\sum_{i} p_{i\mu} = \sum_{j} p_{j\mu}$$

trong do $i$ la cac hat di vao, $j$ la cac hat di ra, va $\mu = t, x, y, z$. Day la **mot** dinh luat bao toan duy nhat trong khong-thoi gian, thay vi bon dinh luat rieng le trong vat ly co dien.

Dieu nay giai thich tai sao trong thuyet tuong doi, bao toan nang luong va bao toan dong luong khong the tach roi: chung la bon thanh phan cua cung mot four-vector, giong nhu $p_x, p_y, p_z$ la ba thanh phan cua cung mot vector 3D. Ban khong the bao toan $p_x$ ma khong bao toan $p_y$ — cung khong the bao toan dong luong ma khong bao toan nang luong trong khong-thoi gian tuong doi tinh.

### Suc manh cua ky hieu tot

Feynman nhan manh: 'Dung cuoi nhat ky hieu; hay phat minh ra chung, chung rat manh me.' Ky hieu four-vector $p_\mu$ cho phep:
1. Viet dinh luat vat ly theo cach bat bien Lorentz mot cach tu dong
2. Kiem tra ngay lap tuc xem mot phuong trinh co tuong thich voi thuyet tuong doi hay khong
3. Kham pha cac dai luong bat bien moi bang cach tinh tich vo huong Minkowski

---

**Diem mau chot:**
- Four-vector $p_\mu = (E/c, p_x, p_y, p_z)$ thong nhat nang luong va dong luong thanh mot doi tuong toan hoc duy nhat trong khong-thoi gian.
- Tich vo huong Minkowski $A_t^2 - A_x^2 - A_y^2 - A_z^2$ la bat bien Lorentz — dai luong vat ly thuc su.
- Dinh luat bao toan nang luong + dong luong viet gon thanh mot phuong trinh four-vector $\sum_i p_{i\mu} = \sum_j p_{j\mu}$.
- Ky hieu tot khong chi la tien loi — no tiet lo cau truc sau cua vat ly va cho phep suy luan hieu qua hon.

---
*Exported from Feynman Bot*
