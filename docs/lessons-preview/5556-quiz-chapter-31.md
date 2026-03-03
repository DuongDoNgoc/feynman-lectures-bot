---
lesson_id: 5556
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:07.897732+00:00"
content_hash: fd956538ee89
chapter_number: 31
chapter_title: Chapter 31
section_number: 3
section_title: 31–2The field due to the material
---
# ## Quiz: Tính Toán Chiết Suất Từ Đầu — Kiểm Tra Toàn Diện

*Source: Chapter 31 - Chapter 31 (Section 3) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_31.html)*

## Quiz: Tính Toán Chiết Suất Từ Đầu — Kiểm Tra Toàn Diện

Bài kiểm tra này đánh giá hiểu biết về cách tính chiết suất từ tính chất vi mô của vật liệu, dựa trên phân tích của Feynman trong Lectures on Physics.

---

**Câu 1.** Khi tính trường $E_a$ phát ra từ tấm kính mỏng (do electron dao động), kết quả cho thấy $E_a$ lệch pha so với trường tới $E_s$ là:

A. Đồng pha (lệch $0°$)
B. Lệch pha $180°$ (ngược pha hoàn toàn)
C. Lệch pha $90°$ (vuông pha — thể hiện qua hệ số $i$ trong công thức)
D. Lệch pha tùy thuộc vào chiều dày tấm kính

**Đáp án: C**
*Giải thích:* Kết quả tích phân cho $E_a \propto i \cdot E_s$, nghĩa là lệch pha $90°$ so với $E_s$. Điều này xuất phát từ tích phân $\int_z^\infty e^{-i\omega r/c}dr = (c/i\omega)e^{-i\omega z/c}$, trong đó $1/i = -i$ tạo ra lệch pha $90°$.

---

**Câu 2.** Bước cuối để rút ra công thức $n = 1 + Ne^2/[2m\varepsilon_0(\omega_0^2-\omega^2)]$ là so sánh:

A. Cường độ trường $|E_a|$ với $|E_s|$
B. Tần số của $E_a$ và $E_s$
C. Lệch pha do $E_a$ gây ra với lệch pha mong đợi từ tấm vật liệu chiết suất $n$
D. Vận tốc nhóm (group velocity) của hai sóng

**Đáp án: C**
*Giải thích:* Trường tổng $E_s + E_a$ có pha lệch thêm một lượng; ta so sánh lượng lệch pha này với lệch pha mong đợi $\omega(n-1)\Delta z/c$ từ một tấm vật liệu chiết suất $n$, từ đó rút ra $n$.

---

**Câu 3.** Nếu bổ sung lực tắt dần (damping) vào phương trình chuyển động electron, chiết suất $\tilde{n}$ trở thành số phức. Phần ảo $\kappa$ của $\tilde{n} = n + i\kappa$ tương ứng với:

A. Sự phản xạ ánh sáng tại bề mặt
B. Sự hấp thụ ánh sáng (attenuation) trong vật liệu
C. Sự tán sắc nhóm (group velocity dispersion)
D. Sự biến đổi phân cực (polarization rotation)

**Đáp án: B**
*Giải thích:* Chiết suất phức $\tilde{n} = n + i\kappa$ trong sóng phẳng: $e^{i\omega(t - \tilde{n}z/c)} = e^{i\omega(t-nz/c)} \cdot e^{-\omega\kappa z/c}$. Số hạng $e^{-\omega\kappa z/c}$ là suy giảm theo chiều dài Beer-Lambert, tương ứng hấp thụ.

---

**Câu 4 (Tự luận).** Bạn đang hiệu chuẩn một giao thoa kế laser độ chính xác cao cho dây chuyền sản xuất của một hệ thống vũ khí dẫn đường. Chiết suất không khí $n_{\text{air}} \approx 1 + 2.926 \times 10^{-4}$ (tại điều kiện chuẩn) thay đổi theo nhiệt độ, áp suất, và độ ẩm. Hãy: (1) Ước tính sai số đo dịch chuyển do chiết suất không khí gây ra khi áp suất thay đổi $\Delta P = 10\,\text{Pa}$ trên đường quang học dài $L = 500\,\text{mm}$. (2) Giải thích tại sao hệ thống vũ khí dẫn đường yêu cầu bù chiết suất, và phương pháp bù thường dùng.

**Gợi ý trả lời mẫu:**
(1) Từ lý thuyết Lorentz: $n-1 \propto N \propto P/(k_BT)$. Thay đổi chiết suất do $\Delta P$:
$$\Delta n = (n_0-1)\frac{\Delta P}{P_0} = 2.926\times10^{-4} \times \frac{10}{101325} \approx 2.9\times10^{-8}$$
Sai số quang trình: $\Delta L_{\text{err}} = \Delta n \times L = 2.9\times10^{-8} \times 0.5 = 14.5\,\text{nm}$.
Với $\lambda = 633\,\text{nm}$, sai số pha: $\Delta\phi = 2\pi \times 14.5/633 \approx 0.144\,\text{rad}$ — tương đương $0.023$ vân, hoàn toàn đáng kể!
(2) Trong hệ thống dẫn đường IMU (Inertial Measurement Unit) dùng laser gyroscope (ring laser gyro), chiết suất không khí ảnh hưởng trực tiếp đến tần số cộng hưởng của vòng laser. Bù chiết suất bằng: (a) bịt kín buồng laser (sealed cavity) và kiểm soát áp suất, (b) dùng cảm biến $P, T, H$ (áp suất, nhiệt độ, độ ẩm) và tính $n$ theo phương trình Ciddor/Edlén thời gian thực, (c) dùng hai bước sóng laser để đo và bù $n$ đồng thời với đo dịch chuyển.

---

```json
{
  "questions": [
    {"id": "q1", "type": "mcq", "question": "Trường E_a từ tấm kính dao động lệch pha so với E_s là:", "options": ["A. Đồng pha (0°)", "B. Ngược pha (180°)", "C. Lệch pha 90° (hệ số i trong công thức)", "D. Phụ thuộc chiều dày tấm kính"], "answer": "C", "explanation": "Tích phân ∫e^{-iωr/c}dr = (c/iω)e^{-iωz/c}, hệ số 1/i = -i tạo lệch pha 90°."},
    {"id": "q2", "type": "mcq", "question": "Bước rút ra n = 1 + Ne²/[2mε₀(ω₀²-ω²)] là so sánh:", "options": ["A. Cường độ |E_a| với |E_s|", "B. Tần số của E_a và E_s", "C. Lệch pha do E_a với lệch pha mong đợi từ tấm chiết suất n", "D. Vận tốc nhóm của hai sóng"], "answer": "C", "explanation": "So sánh lệch pha tính được với ω(n-1)Δz/c mong đợi để rút ra n."},
    {"id": "q3", "type": "mcq", "question": "Phần ảo κ của chiết suất phức ñ = n + iκ tương ứng với:", "options": ["A. Phản xạ tại bề mặt", "B. Hấp thụ (attenuation) trong vật liệu", "C. Tán sắc nhóm", "D. Biến đổi phân cực"], "answer": "B", "explanation": "e^{-ωκz/c} là suy giảm Beer-Lambert, tương ứng hấp thụ trong vật liệu."},
    {"id": "q4", "type": "open", "question": "Hiệu chuẩn giao thoa kế laser (L=500mm) khi áp suất thay đổi ΔP=10Pa: ước tính sai số và đề xuất bù chiết suất cho hệ dẫn đường.", "sample_answer": "Δn = 2.9×10⁻⁸, sai số ΔL=14.5nm (0.023 vân). Bù bằng: sealed cavity, cảm biến P/T/H + phương trình Ciddor, hoặc two-color interferometry."}
  ]
}
```


## Quiz Questions

**Q1:** Trường E_a từ tấm kính dao động lệch pha so với E_s là:
- A) A. Đồng pha (0°)
- B) B. Ngược pha (180°)
- C) C. Lệch pha 90° (hệ số i trong công thức)
- D) D. Phụ thuộc chiều dày tấm kính

**Correct:** C

**Explanation:** Tích phân ∫e^{-iωr/c}dr = (c/iω)e^{-iωz/c}, hệ số 1/i = -i tạo lệch pha 90°.

**Q2:** Bước rút ra n = 1 + Ne²/[2mε₀(ω₀²-ω²)] là so sánh:
- A) A. Cường độ |E_a| với |E_s|
- B) B. Tần số của E_a và E_s
- C) C. Lệch pha do E_a với lệch pha mong đợi từ tấm chiết suất n
- D) D. Vận tốc nhóm của hai sóng

**Correct:** C

**Explanation:** So sánh lệch pha tính được với ω(n-1)Δz/c mong đợi để rút ra n.

**Q3:** Phần ảo κ của chiết suất phức ñ = n + iκ tương ứng với:
- A) A. Phản xạ tại bề mặt
- B) B. Hấp thụ (attenuation) trong vật liệu
- C) C. Tán sắc nhóm
- D) D. Biến đổi phân cực

**Correct:** B

**Explanation:** e^{-ωκz/c} là suy giảm Beer-Lambert, tương ứng hấp thụ trong vật liệu.

**Q4:** Hiệu chuẩn giao thoa kế laser (L=500mm) khi áp suất thay đổi ΔP=10Pa: ước tính sai số và đề xuất bù chiết suất cho hệ dẫn đường.

**Correct:** N/A


---
*Exported from Feynman Bot*
