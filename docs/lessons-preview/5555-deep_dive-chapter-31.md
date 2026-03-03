---
lesson_id: 5555
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:07.869339+00:00"
content_hash: ba4efa0f615d
chapter_number: 31
chapter_title: Chapter 31
section_number: 3
section_title: 31–2The field due to the material
---
# ## Chuyên Sâu: Tính Toán Chiết Suất Hoàn Chỉnh — Từ Phương Trình Vi Phân Đến Chỉ

*Source: Chapter 31 - Chapter 31 (Section 3) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_31.html)*

## Chuyên Sâu: Tính Toán Chiết Suất Hoàn Chỉnh — Từ Phương Trình Vi Phân Đến Chỉ Số Khúc Xạ

### 1. Nhắc Lại Khung Tính Toán

Chúng ta đang chứng minh rằng trường $E_a$ do các điện tích trong tấm kính tạo ra, khi cộng với $E_s$, tạo ra trường tổng giống hệt sóng lan truyền với tốc độ $c/n$. Nếu điều này đúng, ta tính được $n$ từ các tính chất vi mô.

Các tham số bài toán:
- Tấm kính mỏng, chiều dày $\Delta z$, đặt tại $z = 0$
- Mật độ electron: $N_V$ (số/m³), số trên đơn vị diện tích: $N_a = N_V \Delta z$
- Tần số cộng hưởng electron: $\omega_0$
- Tần số ánh sáng tới: $\omega$
- Trường tới: $E_s = E_0 e^{i\omega t}$ (tại $z=0$)

### 2. Phương Trình Chuyển Động Electron

Electron dao động theo phương $x$ (phân cực sóng), phương trình Newton:
$$m\ddot{x} + m\omega_0^2 x = qE_s = eE_0 e^{i\omega t}$$

Nghiệm phức dừng (complex steady-state solution):
$$\tilde{x}(t) = \frac{eE_0}{m(\omega_0^2 - \omega^2)} e^{i\omega t}$$

Gia tốc:
$$\ddot{x}(t) = \frac{-e\omega^2 E_0}{m(\omega_0^2 - \omega^2)} e^{i\omega t}$$

### 3. Trường Bức Xạ Từ Một Electron

Một điện tích gia tốc $\ddot{x}$ tại gốc tọa độ phát ra trường bức xạ. Ở khoảng cách $r$ theo hướng $z$:

$$E_{\text{one electron}} = \frac{q\ddot{x}(t - r/c)}{4\pi\varepsilon_0 c^2 r} = \frac{e}{4\pi\varepsilon_0 c^2} \cdot \frac{\ddot{x}(t_{\text{ret}})}{r}$$

Trong đó $t_{\text{ret}} = t - r/c$ là thời gian trễ.

### 4. Tích Phân Trên Toàn Bộ Tấm Kính

Xét tấm kính là tấm phẳng vô hạn trong mặt phẳng $z=0$. Mỗi vành đai tròn bán kính $\rho$ đến $\rho + d\rho$ đóng góp:

- Số electron: $dN = N_a \cdot 2\pi\rho\,d\rho$
- Khoảng cách đến điểm $P$ tại $(0,0,z)$: $r = \sqrt{z^2 + \rho^2}$
- Thời gian trễ: $t_{\text{ret}} = t - r/c$

Trường từ vành đai này:
$$dE_a = \frac{eN_a 2\pi\rho\,d\rho}{4\pi\varepsilon_0 c^2} \cdot \frac{\ddot{x}(t - r/c)}{r} \cdot \cos\theta$$

Trong đó $\cos\theta = z/r$ là hình chiếu theo trục $z$ (do hướng bức xạ điện từ lưỡng cực). Thay vào và đổi biến $r = \sqrt{z^2+\rho^2}$, $r\,dr = \rho\,d\rho$:

$$E_a = \frac{eN_a}{2\varepsilon_0 c^2} \int_{z}^{\infty} \ddot{x}\left(t - \frac{r}{c}\right) dr$$

Thay $\ddot{x}(t - r/c) = \frac{-e\omega^2 E_0}{m(\omega_0^2-\omega^2)} e^{i\omega(t-r/c)}$:

$$E_a = \frac{-eN_a}{2\varepsilon_0 c^2} \cdot \frac{e\omega^2 E_0}{m(\omega_0^2-\omega^2)} e^{i\omega t} \int_z^{\infty} e^{-i\omega r/c} dr$$

Tích phân $\int_z^{\infty} e^{-i\omega r/c} dr$ cần điều kiện hội tụ (thêm số hạng tắt dần nhỏ $e^{-\varepsilon r}$ rồi lấy giới hạn $\varepsilon \to 0$):

$$\int_z^{\infty} e^{-i\omega r/c} dr = \frac{c}{i\omega} e^{-i\omega z/c}$$

Kết quả:

$$\boxed{E_a = \frac{iNe^2\omega\Delta z}{2m\varepsilon_0 c(\omega_0^2-\omega^2)} E_0 e^{i\omega(t-z/c)}}$$

(Lưu ý: $N_a = N_V \Delta z$; ký hiệu $N = N_V$ từ đây.)

### 5. Xác Nhận Dạng Sóng Và Rút Ra $n$

Trường tổng tại $P$:
$$E_{\text{total}} = E_0 e^{i\omega(t-z/c)}\left[1 + \frac{iNe^2\omega\Delta z}{2m\varepsilon_0 c(\omega_0^2-\omega^2)}\right]$$

Đây đúng là sóng lan truyền theo $z$ với tốc độ $c$, nhưng nhân thêm hệ số pha. Nếu tấm kính có chiết suất $n$ thực, hiệu pha qua chiều dày $\Delta z$ là:
$$e^{i\omega(n-1)\Delta z/c} \approx 1 + i\omega(n-1)\Delta z/c$$

So sánh:
$$\frac{\omega(n-1)\Delta z}{c} = \frac{Ne^2\omega\Delta z}{2m\varepsilon_0 c(\omega_0^2-\omega^2)}$$

Suy ra:
$$n - 1 = \frac{Ne^2}{2m\varepsilon_0(\omega_0^2-\omega^2)}$$

### 6. Bổ Sung Số Hạng Tắt Dần (Damping)

Mô hình trên bỏ qua hiệu ứng bức xạ ngược (radiation reaction) và va chạm. Bổ sung lực tắt dần $-m\gamma\dot{x}$:

$$m\ddot{x} + m\gamma\dot{x} + m\omega_0^2 x = eE_0 e^{i\omega t}$$

Nghiệm:
$$\tilde{x} = \frac{eE_0/m}{\omega_0^2 - \omega^2 + i\gamma\omega} e^{i\omega t}$$

Chiết suất phức:
$$\tilde{n} = n + i\kappa = 1 + \frac{Ne^2}{2m\varepsilon_0} \cdot \frac{\omega_0^2-\omega^2 - i\gamma\omega}{(\omega_0^2-\omega^2)^2 + \gamma^2\omega^2}$$

Phần thực $n$ là chiết suất; phần ảo $\kappa$ liên quan đến **hệ số hấp thụ** $\alpha = 2\omega\kappa/c$ (Beer-Lambert).

### 7. Đường Cong Tán Sắc Sellmeier

Thực tế, vật liệu có nhiều tần số cộng hưởng $\omega_j$ với sức mạnh dao tử $f_j$ (oscillator strength, với điều kiện tổng $\sum_j f_j = Z$ số electron). **Công thức Sellmeier** (dùng rộng rãi trong công nghiệp quang học):

$$n^2(\lambda) = 1 + \sum_j \frac{B_j \lambda^2}{\lambda^2 - C_j}$$

Đây là dạng thực nghiệm của công thức Lorentz, với $B_j$ và $C_j$ xác định bằng đo đạc. Ví dụ kính BK7 (thủy tinh quang học phổ biến nhất):
$$n^2 = 1 + \frac{1.0396B\lambda^2}{\lambda^2 - 0.006001} + \frac{0.2318B\lambda^2}{\lambda^2 - 0.02001} + \frac{1.0105B\lambda^2}{\lambda^2 - 103.56}$$

(với $\lambda$ tính bằng micromet, các hằng số $B_j, C_j$ từ fitting thực nghiệm)

### 8. Ứng Dụng: Tính Toán Sắc Sai Của Hệ Quang Học

Ví dụ thực tế: bạn cần thiết kế **thấu kính chuẩn trực** (collimating lens) cho laser diode phát ở $\lambda = 780\,\text{nm}$ nhưng có độ rộng phổ $\Delta\lambda = 2\,\text{nm}$.

Sắc sai dọc trục (longitudinal chromatic aberration) của thấu kính tiêu cự $f$:
$$\Delta f = -f^2 \frac{dn}{d\lambda} \cdot \frac{\Delta\lambda}{n-1} \cdot \frac{1}{f} = -\frac{f \cdot (dn/d\lambda)}{n-1} \cdot \Delta\lambda$$

Số Abbe (Abbe number) đặc trưng cho tán sắc:
$$V = \frac{n_d - 1}{n_F - n_C}$$

Với BK7: $V \approx 64$ (tán sắc thấp, tốt). Với SF11 (kính nặng): $V \approx 25$ (tán sắc cao).

Sắc sai dọc: $\Delta f \approx f/V \cdot (\Delta\lambda/\Delta\lambda_{\text{chuẩn}})$

Thấu kính achromatic (ghép hai thấu kính kính khác số Abbe) bù sắc sai này, cơ sở vật lý chính là sự khác biệt trong $dn/d\omega$ của hai vật liệu.

### 9. Đo Chiết Suất Chính Xác Cao: Phương Pháp Giao Thoa Kế

Để đo chiết suất với độ chính xác $\delta n \sim 10^{-7}$ (cần thiết trong hiệu chuẩn giao thoa kế chuẩn), dùng giao thoa kế Mach-Zehnder: đặt mẫu vật liệu vào một nhánh, đo số vân dịch chuyển:

$$\Delta m = \frac{(n-1)L}{\lambda}$$

Với $L = 100\,\text{mm}$, $\lambda = 633\,\text{nm}$, $n-1 = 0.5$:
$$\Delta m = \frac{0.5 \times 0.1}{633\times10^{-9}} \approx 79{,}000\,\text{vân}$$

Đếm vân với độ phân giải $0.001$ vân: $\delta n = 0.001 \times 633\times10^{-9}/0.1 = 6.33\times10^{-9}$. Độ chính xác này đủ để nghiên cứu vật liệu quang học mới!

### Tóm Tắt Chuỗi Lập Luận

```
Phương trình chuyển động electron
       ↓
Biên độ dao động x̃ = (eE₀/m)/(ω₀²-ω²)
       ↓
Gia tốc → trường bức xạ từ một electron
       ↓
Tích phân trên tấm phẳng vô hạn
       ↓
E_a = [iNe²ωΔz/(2mε₀c(ω₀²-ω²))]·E_s
       ↓
So sánh với hiệu pha mong đợi e^{i(n-1)ωΔz/c}
       ↓
n = 1 + Ne²/[2mε₀(ω₀²-ω²)]
```

Chuỗi lập luận này, từ phương trình Newton cho electron đến công thức chiết suất vĩ mô, là một trong những bài tập chứng minh đẹp nhất trong vật lý cổ điển.

---
*Exported from Feynman Bot*
