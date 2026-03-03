---
lesson_id: 5423
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-03-03T15:33:04.690704+00:00"
content_hash: a03a848b947c
chapter_number: 15
chapter_title: Chapter 15
section_number: 2
section_title: 15–1The principle of relativity
---
# Tương Đối Hẹp — Phân Tích Chuyên Sâu

*Source: Chapter 15 - Chapter 15 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_15.html)*

# Tương Đối Hẹp — Phân Tích Chuyên Sâu

## Bước 1: Biến Đổi Lorentz — Suy Luận Từ $c$ = Hằng Số

Xét hệ S (Joe đứng yên) và S' (Moe chuyển động với vận tốc $u$ theo $x$). Tại $t = t' = 0$, hai gốc trùng nhau. Ánh sáng phát ra từ gốc.

**Trong S**: Mặt cầu sáng: $x^2 + y^2 + z^2 = c^2t^2$
**Trong S'**: $x'^2 + y'^2 + z'^2 = c^2t'^2$

Biến đổi phải tuyến tính (không gian đồng nhất) và giữ $c^2t^2 - x^2 - y^2 - z^2$ bất biến.

Giải hệ phương trình → Biến đổi Lorentz:
$$x' = \gamma(x - ut),\quad t' = \gamma(t - ux/c^2)$$
$$y' = y,\quad z' = z$$

Trong đó: $\gamma = \frac{1}{\sqrt{1 - u^2/c^2}} \geq 1$

## Bước 2: Hệ Quả Vật Lý

### Giãn Thời Gian
Xét đồng hồ đứng yên trong S' ($\Delta x' = 0$). Khoảng thời gian trong S:
$$\Delta t = \gamma \Delta t'$$

Đồng hồ chuyển động chạy chậm hơn hệ số $\gamma > 1$.

### Co Độ Dài
Thanh đứng yên trong S' có độ dài $L_0 = \Delta x'$. Đo trong S (đồng thời, $\Delta t = 0$):
$$\Delta x = \Delta x'/\gamma = L_0/\gamma < L_0$$

Thanh chuyển động ngắn hơn hệ số $\gamma$.

### Cộng Vận Tốc Tương Đối
Vận tốc $v'$ trong S' → vận tốc trong S:
$$v = \frac{v' + u}{1 + v'u/c^2}$$

Nếu $v' = c$: $v = \frac{c + u}{1 + u/c} = c$ (ánh sáng vẫn $c$ trong mọi hệ!)

## Bước 3: Năng Lượng và Động Lượng Tương Đối

Định nghĩa tương đối đúng:
$$\vec{p} = \gamma m_0\vec{v}, \quad E = \gamma m_0c^2$$

Với $m_0$ là khối lượng nghỉ.

Quan hệ năng lượng-động lượng:
$$E^2 = (pc)^2 + (m_0c^2)^2$$

Giới hạn không tương đối ($v \ll c$, $\gamma \approx 1 + v^2/2c^2$):
$$E \approx m_0c^2 + \frac{1}{2}m_0v^2$$

Động năng Newton $\frac{1}{2}mv^2$ là số hạng hiệu chỉnh nhỏ so với năng lượng nghỉ $m_0c^2$!

## Bước 4: $E = mc^2$ — Ý Nghĩa Thực Tế

Năng lượng nghỉ của $1\,g$ vật chất: $E = 10^{-3} \times (3\times10^8)^2 = 9\times10^{13}\,J = 90\,TJ$

Bom nguyên tử Hiroshima giải phóng $\approx 63\,TJ$ từ $\sim 1\,g$ phân hạch thực sự.

**Trong kỹ thuật hạt nhân**: phản ứng phân hạch $U^{235}$ hay $Pu^{239}$ chuyển ~0.1% khối lượng thành năng lượng (độ hụt khối). Bảo toàn $E = mc^2$ là công cụ tính năng lượng phóng ra.

## Bước 5: Ứng Dụng Kỹ Thuật Đo Lường

**Đồng hồ nguyên tử và GPS**: Đã trình bày ở bài concept.

**Máy gia tốc hạt**: CERN gia tốc proton đến $v = 0.9999997\,c$, $\gamma \approx 1836$. Năng lượng mỗi proton $= \gamma m_p c^2 = 1836 \times 938\,MeV \approx 1.72\,TeV$. Không có công thức Newton nào có thể mô tả đúng — phải dùng tương đối hẹp.

**Spectroscopy Doppler tương đối**: Đo vận tốc vật thể thiên văn qua dịch chuyển tần số sóng điện từ. Công thức Doppler tương đối: $f_{obs} = f_0\sqrt{\frac{1-v/c}{1+v/c}}$. Trong đo độ dịch vận tốc vệ tinh bằng laser Doppler velocimetry (LDV), phải tính hiệu chỉnh tương đối ở độ chính xác cao.

## Bài Tập Có Hướng Dẫn

Electron trong đèn hình CRT cũ được gia tốc qua hiệu điện thế $V = 25\,kV$.

**Năng lượng của electron:**
$eV = 25\,000 \times 1.6\times10^{-19} = 4\times10^{-15}\,J = 25\,keV$

**Năng lượng nghỉ của electron:** $m_e c^2 = 0.511\,MeV = 511\,keV$

**Tỉ lệ:** $25\,keV / 511\,keV \approx 4.9\%$ → hiệu chỉnh tương đối nhỏ nhưng không tầm thường.

**Vận tốc (tương đối):**
$\gamma = 1 + 25/511 \approx 1.049$
$v = c\sqrt{1 - 1/\gamma^2} = c\sqrt{1 - 0.909} \approx 0.302\,c \approx 9\times10^7\,m/s$

**So với Newton:** $v_{Newton} = \sqrt{2eV/m_e} \approx 0.296\,c$ — sai số ~2%.

## Điểm Mấu Chốt

Tương đối hẹp không phá hủy cơ học Newton — nó mở rộng cơ học Newton đến vùng $v \to c$. Biến đổi Lorentz thay thế Galilean. Năng lượng $E = \gamma mc^2$ thu về $\frac{1}{2}mv^2 + mc^2$ ở vận tốc thấp. Trong kỹ thuật: GPS, máy gia tốc, cảm biến Doppler laser độ chính xác cao — tất cả cần tương đối hẹp.

---
*Exported from Feynman Bot*
