---
lesson_id: 5609
lesson_type: deep_dive
approval_status: pending
exported_at: "2026-03-03T15:33:09.022673+00:00"
content_hash: af3bf3afb914
chapter_number: 36
chapter_title: Chapter 36
section_number: 4
section_title: 36–3The rod cells
---
# ## Deep Dive: Vật Lý Lượng Tử của Thị Giác — Từ Rhodopsin đến Mắt Kép

*Source: Chapter 36 - Chapter 36 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_36.html)*

## Deep Dive: Vật Lý Lượng Tử của Thị Giác — Từ Rhodopsin đến Mắt Kép

### 1. Cơ Học Lượng Tử của Hấp Thụ Photon trong Retinene

Bản chất hấp thụ ánh sáng của retinene có thể được hiểu qua mô hình **"particle in a box"** của cơ học lượng tử. Trong chuỗi conjugated double bonds có $N$ liên kết, electron $\pi$ có thể di chuyển tự do trong chiều dài $L = N \cdot a_0$ (với $a_0 \approx 0.14$ nm là khoảng cách liên kết C-C).

Theo cơ học lượng tử 1D, các mức năng lượng của electron bị nhốt trong hộp chiều dài $L$ là:

$$E_n = \frac{n^2 \pi^2 \hbar^2}{2 m_e L^2}$$

Bước chuyển quang học từ mức $n$ đến $n+1$ tương ứng photon có năng lượng:

$$\Delta E = E_{n+1} - E_n = \frac{(2n+1)\pi^2 \hbar^2}{2 m_e L^2}$$

Với retinene có $N = 11$ liên kết đôi, $L \approx 1.54$ nm, bước chuyển HOMO→LUMO rơi vào vùng ánh sáng nhìn thấy ($\lambda \approx 500$ nm). Đây là lý do tế bào que nhạy nhất với ánh sáng xanh-lục — phù hợp với ánh sáng buổi hoàng hôn/bình minh khi động vật cần nhìn xa nhất!

### 2. Cấu Trúc Đĩa Màng: Quang Học của Hệ Nhiều Lớp

Mỗi tế bào que chứa $\sim 1000$ đĩa màng (membrane discs), mỗi đĩa dày khoảng $d = 6$ nm. Xếp chồng lên nhau, chúng tạo ra hệ thống "multi-pass optical cavity" sinh học.

Xác suất để photon bị hấp thụ sau khi đi qua $N$ đĩa màng:

$$P_{abs} = 1 - (1 - \sigma \rho)^N$$

Trong đó:
- $\sigma$ = tiết diện hấp thụ của một phân tử rhodopsin ($\sigma \approx 10^{-16}$ cm²)
- $\rho$ = mật độ rhodopsin trên đĩa ($\rho \approx 2.5 \times 10^4$ phân tử/μm²)
- $N \approx 1000$ đĩa

Tính ra: $\sigma \rho \approx 2.5 \times 10^{-4}$ mỗi đĩa, và:
$$P_{abs} \approx 1 - e^{-N \sigma \rho} \approx 1 - e^{-0.25} \approx 22\%$$

Hiệu suất 22% nghe có vẻ thấp, nhưng đây là **xác suất hấp thụ một photon đơn lẻ** — và với khoảng 5 triệu tế bào que trong võng mạc, toàn bộ hệ thống có hiệu suất cực kỳ cao.

### 3. Mắt Kép (Compound Eye) của Động Vật Giáp Xác: Nguyên Lý Mảng Cảm Biến

Mắt kép của cua móng ngựa (horseshoe crab) có khoảng $\sim 1000$ **ommatidia** — mỗi ommatidium là một đơn vị thị giác độc lập bao gồm một thấu kính nhỏ (facet lens) và một bó tế bào cảm quang phía sau.

**Độ phân giải góc** của mắt kép được tính qua công thức Abbe:

$$\Delta \phi_{min} = \frac{\lambda}{D}$$

Với $\lambda = 500$ nm (ánh sáng xanh-lục) và đường kính một facet $D \approx 50$ μm:
$$\Delta \phi_{min} \approx \frac{500 \times 10^{-9}}{50 \times 10^{-6}} = 0.01 \text{ rad} \approx 0.57°$$

Đây là giới hạn nhiễu xạ (diffraction limit) — cau móng ngựa bị giới hạn bởi kích thước vật lý của mỗi facet. Để cải thiện, mắt kép cần facet lớn hơn (tăng $D$) hoặc bước sóng ngắn hơn — đó là lý do một số côn trùng nhìn được tia UV!

### 4. Ức Chế Bên (Lateral Inhibition): Thuật Toán Edge Detection Sinh Học

Phát hiện quan trọng nhất từ nghiên cứu mắt cua móng ngựa là cơ chế **lateral inhibition**: mỗi ommatidium không chỉ gửi tín hiệu lên não mà còn **ức chế** các ommatidia lân cận thông qua các sợi thần kinh ngang (lateral plexus).

Nếu ký hiệu $r_p$ là tốc độ spike (số xung/giây) của ommatidium $p$ và $e_p$ là tín hiệu kích thích từ ánh sáng, phương trình cân bằng là:

$$r_p = e_p - k \sum_{q \neq p} r_q \ (\text{với các } q \text{ lân cận})$$

Hệ phương trình này mô tả bộ lọc spatial high-pass: vùng có gradient độ sáng cao (biên cạnh) sẽ được khuếch đại, vùng đồng đều sẽ bị giảm phản ứng.

Đây chính là nguyên lý **Mach band** — hiện tượng con người thấy viền sáng/tối giả tạo tại ranh giới sáng-tối — và cũng là nền tảng của thuật toán edge detection trong xử lý ảnh kỹ thuật số (Sobel filter, Laplacian of Gaussian).

### 5. Ứng Dụng Kỹ Thuật: Sensor Array và Edge Detection

**Trong thiết kế hệ thống đo lường chính xác:**

**(a) CMOS sensor array**: Mỗi pixel trong CMOS image sensor tương tự một ommatidium. Tuy nhiên, CMOS hiện đại dùng **readout circuit** phức tạp thay vì lateral inhibition sinh học. Một số chip vision AI mới đây (Event camera / Dynamic Vision Sensor) hoạt động theo nguyên lý gần với lateral inhibition: chỉ output sự kiện khi có thay đổi độ sáng, không liên tục — giảm bandwidth 1000 lần so với frame camera.

**(b) Gradient-force measurement**: Trong hệ thống đo lực micrometer, ta có thể dùng array cảm biến áp điện với cross-coupling (tương tự lateral inhibition) để nâng cao độ phân giải không gian của bản đồ lực phân bố.

**(c) Thị giác máy trong kiểm tra chip**: Thuật toán lateral inhibition số hóa (Difference of Gaussians — DoG) được dùng rộng rãi trong hệ thống AOI (Automated Optical Inspection) kiểm tra bề mặt wafer bán dẫn, phát hiện khuyết tật ở cấp nanometer.

### 6. Mắt Bạch Tuộc: Giải Pháp Hội Tụ Độc Lập

Một điểm đáng chú ý về kỹ thuật tiến hóa: bạch tuộc (octopus) là động vật không xương sống nhưng đã phát triển mắt gần giống hệt mắt người — có giác mạc, iris, thủy tinh thể, võng mạc. Đây là ví dụ điển hình của **convergent evolution** (tiến hóa hội tụ): hai nhánh tiến hóa độc lập cùng đến một thiết kế tối ưu.

Điểm cải tiến của mắt bạch tuộc: tế bào cảm quang ở **trước** tế bào thần kinh (không "inside-out" như mắt người), tránh được điểm mù (blind spot) do dây thần kinh thị giác xuyên qua võng mạc ở mắt người.

**Ứng dụng engineering**: Nguyên lý convergent evolution cho thấy có những **thiết kế tối ưu toàn cục** trong không gian giải pháp kỹ thuật. Trong tối ưu hóa topology của cơ cấu chấp hành (actuator topology optimization) cho robot cơ điện tử, thuật toán evolutionary computing thường "tái phát minh" các cấu trúc đã có trong tự nhiên — bằng chứng về tính phổ quát của các thiết kế tối ưu.

### Tổng Kết Kỹ Thuật

| Thành phần sinh học | Tương đương kỹ thuật | Thông số điển hình |
|---|---|---|
| Rhodopsin trên đĩa màng | Photodiode trong pixel | $\sigma \approx 10^{-16}$ cm² |
| Chuỗi conjugated double bonds | Quantum well trong LED/detector | $\Delta E \propto 1/L^2$ |
| Stack đĩa màng (1000 lớp) | Anti-reflection coating stack | $P_{abs} \approx 22\%$ mỗi photon |
| Lateral inhibition network | Laplacian filter / DoG | Bandwidth reduction 10-100× |
| Mắt kép (compound eye) | Phased array / aperture synthesis | $\Delta \phi = \lambda/D$ |

---
*Exported from Feynman Bot*
