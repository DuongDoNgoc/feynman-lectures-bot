---
lesson_id: 5525
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:07.158383+00:00"
content_hash: b0ebeee9ccfe
chapter_number: 28
chapter_title: Chapter 28
section_number: 2
section_title: 28–1Electromagnetism
---
# ## Bức Xạ Điện Từ và Phương Trình Maxwell: Phân Tích Chuyên Sâu

*Source: Chapter 28 - Chapter 28 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_28.html)*

## Bức Xạ Điện Từ và Phương Trình Maxwell: Phân Tích Chuyên Sâu

### 1. Bối cảnh lịch sử và tổng hợp Maxwell

Trước năm 1860, vật lý học có bốn định luật cơ bản về điện từ:

1. **Định luật Gauss điện:** $\nabla \cdot \vec{E} = \rho/\varepsilon_0$ (điện tích tạo ra trường điện)
2. **Định luật Gauss từ:** $\nabla \cdot \vec{B} = 0$ (không có từ tích đơn)
3. **Định luật Faraday:** $\nabla \times \vec{E} = -\partial\vec{B}/\partial t$ (từ trường biến thiên tạo trường điện)
4. **Định luật Ampère:** $\nabla \times \vec{B} = \mu_0 \vec{J}$ (dòng điện tạo ra trường từ)

Maxwell nhận ra rằng định luật Ampère không nhất quán: khi lấy divergence của cả hai vế, vế trái bằng 0 (vì $\nabla \cdot (\nabla \times \vec{B}) = 0$), nhưng vế phải $\nabla \cdot \vec{J} = -\partial\rho/\partial t \neq 0$ trong trường hợp tổng quát.

Để sửa chữa, Maxwell thêm **dòng điện dịch** (*displacement current*):
$$\nabla \times \vec{B} = \mu_0 \vec{J} + \mu_0\varepsilon_0 \frac{\partial\vec{E}}{\partial t}$$

Số hạng $\mu_0\varepsilon_0 \partial\vec{E}/\partial t$ là "dòng điện dịch" — không phải dòng điện thực nhưng có tác dụng tương tự về mặt từ học.

### 2. Suy ra phương trình sóng điện từ

Từ phương trình Maxwell trong chân không ($\rho = 0$, $\vec{J} = 0$):

Lấy curl của phương trình Faraday:
$$\nabla \times (\nabla \times \vec{E}) = -\frac{\partial}{\partial t}(\nabla \times \vec{B})$$

Dùng đồng nhất vector: $\nabla \times (\nabla \times \vec{E}) = \nabla(\nabla \cdot \vec{E}) - \nabla^2\vec{E} = -\nabla^2\vec{E}$ (vì $\nabla \cdot \vec{E} = 0$ trong chân không)

Thay phương trình Ampère-Maxwell vào vế phải:
$$-\nabla^2\vec{E} = -\mu_0\varepsilon_0 \frac{\partial^2\vec{E}}{\partial t^2}$$

Suy ra **phương trình sóng điện từ**:
$$\boxed{\nabla^2\vec{E} = \mu_0\varepsilon_0 \frac{\partial^2\vec{E}}{\partial t^2}}$$

Đây là phương trình sóng với vận tốc:
$$c = \frac{1}{\sqrt{\mu_0\varepsilon_0}} = \frac{1}{\sqrt{(4\pi \times 10^{-7})(8.85 \times 10^{-12})}} \approx 3 \times 10^8 \text{ m/s}$$

Đúng bằng vận tốc ánh sáng đo được thực nghiệm! Maxwell đã chứng minh ánh sáng là sóng điện từ.

### 3. Trường bức xạ của điện tích gia tốc

Phương trình Maxwell dự đoán rằng điện tích gia tốc sẽ bức xạ năng lượng. Giải phương trình Maxwell cho điện tích $q$ chuyển động, ta thu được hai thành phần trường:

**Trường Coulomb** (static/near-field): $E \propto \frac{q}{r^2}$ — giảm nhanh, "gắn liền" với điện tích

**Trường bức xạ** (radiation/far-field): $E \propto \frac{q\ddot{\theta}}{c^2 r}$ — giảm chậm, lan truyền độc lập

Công thức đầy đủ của trường bức xạ:
$$\vec{E}_{rad} = -\frac{q}{4\pi\varepsilon_0 c^2} \frac{\ddot{e}_{r'}(t_{ret})}{r'}$$

Trong đó $t_{ret} = t - r'/c$ là **thời điểm phát xạ trễ** (retarded time) — trường ta quan sát tại thời điểm $t$ thực ra được phát ra từ vị trí của điện tích tại thời điểm sớm hơn $r'/c$.

### 4. Công suất bức xạ: Công thức Larmor

Năng lượng bức xạ trên đơn vị thời gian của điện tích gia tốc:

$$P = \frac{q^2 a^2}{6\pi\varepsilon_0 c^3}$$

Đây là **công thức Larmor** (Larmor radiation formula). Một số điểm quan trọng:
- Công suất bức xạ tỉ lệ với **bình phương gia tốc** $a^2$
- Tỉ lệ với $c^{-3}$ — trong môi trường có chiết suất $n > 1$, vận tốc pha giảm, bức xạ tăng (hiệu ứng Cherenkov)
- Điện tích chuyển động đều (gia tốc = 0) **không bức xạ** — điều này quan trọng trong cơ học lượng tử

### 5. Anten dipole và phân bố bức xạ

Xét anten dipole thẳng (linear dipole antenna) với dòng điện dao động tần số $\omega$:
$$I(t) = I_0 \cos(\omega t)$$

Công suất bức xạ theo hướng góc $\theta$ so với trục anten:
$$\frac{dP}{d\Omega} \propto \sin^2\theta$$

Bức xạ **cực đại** theo phương vuông góc với anten ($\theta = 90°$) và **bằng 0** theo phương dọc theo anten ($\theta = 0°$). Đây là **radiation pattern** của dipole antenna.

### 6. Ứng dụng thực tế: Anten và hệ thống radar

Với kỹ sư thiết kế hệ thống quân sự và tự động hoá, bức xạ điện từ xuất hiện trong nhiều ứng dụng quan trọng:

**Radar (Radio Detection And Ranging):**
Hệ radar phát sóng điện từ tần số $f$ (thường $1-100$ GHz) với công suất $P_t$ từ anten gain $G_t$. Công suất thu được từ mục tiêu diện tích phản xạ radar (RCS — Radar Cross Section) $\sigma$ ở khoảng cách $R$:

$$P_r = \frac{P_t G_t G_r \sigma \lambda^2}{(4\pi)^3 R^4}$$

**Radar Equation** này là hệ quả trực tiếp của trường bức xạ $\propto 1/r$: cường độ $\propto 1/r^2$ từ anten đến mục tiêu, rồi lại $1/r^2$ từ mục tiêu trở về anten → tổng cộng $1/R^4$.

**Bài toán thiết kế:** Muốn phát hiện mục tiêu RCS $\sigma = 1$ m² ở $R = 10$ km với $P_r > -100$ dBm:
$$P_t G_t G_r = \frac{P_r (4\pi)^3 R^4}{\sigma \lambda^2}$$

Với $\lambda = 3$ cm ($f = 10$ GHz), $G_t = G_r = 30$ dBi = $10^3$:
$$P_t = \frac{10^{-13} \times (4\pi)^3 \times 10^{16}}{10^6 \times (0.03)^2} \approx 22 \text{ W}$$

**Electromagnetic Interference (EMI):** Trong hệ thống điều khiển chính xác, động cơ servo và mạch điện cao tần bức xạ nhiễu điện từ. Hiểu bức xạ dipole giúp kỹ sư thiết kế shielding và filtering hiệu quả.

### 7. Phân cực sóng điện từ và ứng dụng

Sóng điện từ phẳng có vector $\vec{E}$ dao động trong mặt phẳng vuông góc với phương truyền. **Phân cực** (polarization) mô tả hướng dao động của $\vec{E}$:

- **Phân cực thẳng** (linear polarization): $\vec{E}$ dao động theo một hướng cố định
- **Phân cực tròn** (circular polarization): $\vec{E}$ quay tròn — dùng trong GPS, thông tin vệ tinh
- **Phân cực elip** (elliptical): tổng quát nhất

Trong hệ thống lidar (Light Detection And Ranging) dùng trong tự động hoá, phân tích phân cực ánh sáng phản xạ từ bề mặt cho biết thông tin về vật liệu và kết cấu bề mặt.

### 8. Vận tốc ánh sáng và hệ quy chiếu

Một hệ quả sâu sắc từ phương trình sóng: vận tốc ánh sáng $c = 1/\sqrt{\mu_0\varepsilon_0}$ là hằng số, không phụ thuộc vào hệ quy chiếu. Đây là xuất phát điểm của thuyết tương đối hẹp (special relativity) của Einstein.

### Tóm tắt

- Maxwell thêm dòng điện dịch $\varepsilon_0 \partial\vec{E}/\partial t$ vào phương trình Ampère để bảo đảm nhất quán
- Từ bốn phương trình Maxwell, suy ra phương trình sóng với $c = 1/\sqrt{\mu_0\varepsilon_0}$
- Trường bức xạ $\propto 1/r$ (không phải $1/r^2$) cho phép sóng lan truyền xa
- Công thức Larmor: $P = q^2 a^2 / (6\pi\varepsilon_0 c^3)$
- Ứng dụng: radar, anten, EMI, lidar trong tự động hoá và hệ thống quân sự

---
*Exported from Feynman Bot*
