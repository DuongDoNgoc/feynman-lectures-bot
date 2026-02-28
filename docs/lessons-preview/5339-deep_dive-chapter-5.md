---
lesson_id: 5339
lesson_type: deep_dive
approval_status: approved
exported_at: "2026-02-28T10:51:40.251803+00:00"
content_hash: d0e271ba3ead
chapter_number: 5
chapter_title: Chapter 5
section_number: 5
section_title: 5–4Long times
---
# ## Đo Thời Gian Dài — Phân tích Chuyên sâu

*Source: Chapter 5 - Chapter 5 (Section 5) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_05.html)*

## Đo Thời Gian Dài — Phân tích Chuyên sâu

### 1. Toán Học Của Phân Rã Phóng Xạ

**Phương trình vi phân cơ bản**:

Tốc độ phân rã tỷ lệ với số nguyên tử hiện có:
$$\frac{dN}{dt} = -\lambda N$$

Giải phương trình vi phân:
$$\int_{N_0}^{N} \frac{dN'}{N'} = -\lambda \int_0^t dt' \implies \ln\frac{N}{N_0} = -\lambda t$$

$$\boxed{N(t) = N_0 e^{-\lambda t}}$$

**Chu kỳ bán rã**: Khi $N = N_0/2$:
$$\frac{1}{2} = e^{-\lambda T_{1/2}} \implies T_{1/2} = \frac{\ln 2}{\lambda} \approx \frac{0.6931}{\lambda}$$

**Hoạt độ phóng xạ** (số phân rã/giây, đơn vị Becquerel):
$$A(t) = \left|\frac{dN}{dt}\right| = \lambda N(t) = \lambda N_0 e^{-\lambda t} = A_0 e^{-\lambda t}$$

### 2. Tính Tuổi Bằng Carbon-14

**Dữ liệu C-14**:
- $T_{1/2} = 5730$ năm
- $\lambda = \frac{\ln 2}{5730} = 1.209 \times 10^{-4}$ năm$^{-1}$
- Tỷ lệ $^{14}C/^{12}C$ trong khí quyển: $r_0 \approx 1.3 \times 10^{-12}$

**Công thức tính tuổi**:
$$t = -\frac{1}{\lambda} \ln\left(\frac{r}{r_0}\right) = \frac{T_{1/2}}{\ln 2} \ln\left(\frac{r_0}{r}\right)$$

**Ví dụ**: Mẫu gỗ còn lại 62.5% hoạt độ C-14 so với mẫu hiện đại:
$$t = \frac{5730}{0.6931} \times \ln\left(\frac{1}{0.625}\right) = 8267 \times 0.470 = 3885 \, \text{năm}$$

→ Mẫu gỗ này có tuổi ~3885 năm trước Công nguyên.

### 3. Uranium-Lead Dating — Đồng Hồ Địa Chất

**Chuỗi phân rã phức tạp hơn** vì U-238 không phân rã trực tiếp thành Pb-206 mà qua 14 bước trung gian. Tuy nhiên, vì tất cả bước trung gian có $T_{1/2}$ << $T_{1/2}(U-238)$, hệ thống nhanh chóng đạt **cân bằng thế kỷ** và có thể xử lý như phân rã trực tiếp.

**Phương trình tuổi đơn giản hóa**:
$$\frac{^{206}Pb}{^{238}U} = e^{\lambda t} - 1$$

$$t = \frac{1}{\lambda_{238}} \ln\left(1 + \frac{^{206}Pb}{^{238}U}\right)$$

Với $\lambda_{238} = 1.551 \times 10^{-10}$ năm$^{-1}$.

**Concordia diagram**: Để kiểm tra tính tin cậy, các nhà địa chất dùng đồng thời U-235/Pb-207 và U-238/Pb-206. Nếu cả hai cho cùng tuổi → mẫu không bị ô nhiễm.

### 4. Ứng Dụng Kỹ Thuật: Mô Phỏng Tuổi Thọ Vật Liệu

Trong ngành vũ khí và thiết bị quân sự, phân rã phóng xạ được dùng để:

**a) Nguồn điện hạt nhân (RTG — Radioisotope Thermoelectric Generator)**:
- Pu-238 ($T_{1/2} = 87.7$ năm) → nhiệt năng → điện năng
- Dùng trong tàu vũ trụ (Voyager, New Horizons) và thiết bị quân sự độc lập
- Công suất sau $t$ năm: $P(t) = P_0 e^{-\lambda t}$

**Bài toán**: RTG Pu-238 ban đầu $P_0 = 4$ kW. Sau 44 năm ($= 0.5 T_{1/2}$), công suất còn lại?

$$P(44) = 4 \times e^{-\frac{\ln 2}{87.7} \times 44} = 4 \times e^{-0.347} = 4 \times 0.707 = 2.83 \, \text{kW}$$

→ Còn ~70.7% công suất sau 44 năm — RTG vẫn hoạt động được.

**b) Kiểm Tra Không Phá Hủy (NDT) Bằng Phóng Xạ**:
- Nguồn Ir-192 ($T_{1/2} = 73.8$ ngày) hay Co-60 ($T_{1/2} = 5.27$ năm) dùng để chụp X-quang công nghiệp
- Kỹ thuật viên phải tính hoạt độ còn lại để tính thời gian phơi sáng chính xác:
$$t_{exposure} = \frac{t_{exposure,0} \times A_0}{A(t)} = t_{exposure,0} \times e^{\lambda t}$$

### 5. Phương Pháp Đồng Hồ Tổng Hợp — Calibration Curves

Vòng cây và C-14 bổ sung cho nhau:

- **Vấn đề**: Tỷ lệ $^{14}C/^{12}C$ trong khí quyển không thực sự hằng số — biến động theo hoạt động Mặt Trời và địa từ
- **Giải pháp**: Xây dựng **đường cong hiệu chuẩn** (calibration curve) dùng mẫu gỗ có tuổi xác định từ vòng cây + đo C-14
- **IntCal20** (2020): đường cong hiệu chuẩn chuẩn quốc tế, kéo dài đến 55,000 năm trước

**Nguyên lý này giống hệt** việc hiệu chuẩn encoder với laser interferometer: dùng tiêu chuẩn độc lập (vòng cây = laser) để hiệu chuẩn thiết bị đo chính (C-14 = encoder).

### 6. Bài Tập Mẫu: Lịch Bảo Trì Nguồn Phóng Xạ

**Bài toán**: Nguồn Ir-192 ($T_{1/2} = 73.8$ ngày) mới nhập có hoạt độ $A_0 = 100$ Ci. Quy định an toàn yêu cầu thay nguồn khi $A < 10$ Ci. Sau bao lâu phải thay?

**Giải**:
$$10 = 100 \times e^{-\lambda t} \implies e^{-\lambda t} = 0.1$$
$$-\lambda t = \ln(0.1) = -2.303 \implies t = \frac{2.303}{\lambda}$$
$$\lambda = \frac{\ln 2}{73.8} = 0.00939 \, \text{ngày}^{-1}$$
$$t = \frac{2.303}{0.00939} = 245 \, \text{ngày} \approx 3.3 T_{1/2}$$

→ Phải thay nguồn sau **245 ngày** (tương đương $\log_{0.5}(0.1) \approx 3.32$ chu kỳ bán rã).

---

**Điểm mấu chốt:**
- Phân rã phóng xạ: $N(t) = N_0 e^{-\lambda t}$, giải từ phương trình vi phân đơn giản $dN/dt = -\lambda N$
- C-14 dating: đo tỷ lệ $^{14}C/^{12}C$ còn lại → tính tuổi đến ~50,000 năm
- RTG dùng phân rã Pu-238 làm nguồn điện dài hạn cho thiết bị quân sự/vũ trụ
- Nguồn phóng xạ công nghiệp có lịch bảo trì tính bằng chu kỳ bán rã

---
*Exported from Feynman Bot*
