---
lesson_id: 5553
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-03T15:33:07.813577+00:00"
content_hash: 1bb045478aba
chapter_number: 31
chapter_title: Chapter 31
section_number: 2
section_title: 31–1The index of refraction
---
# ## Quiz: Chiết Suất Vi Mô — Từ Electron Đến Chỉ Số Khúc Xạ

*Source: Chapter 31 - Chapter 31 (Section 2) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_31.html)*

## Quiz: Chiết Suất Vi Mô — Từ Electron Đến Chỉ Số Khúc Xạ

Kiểm tra hiểu biết về cơ chế vi mô của chiết suất và tán sắc ánh sáng.

---

**Câu 1.** Theo lý thuyết vi mô của Feynman, tốc độ pha $c/n$ của ánh sáng trong môi trường vật chất là do:

A. Photon va chạm với nguyên tử và bị làm chậm lại
B. Giao thoa giữa sóng tới từ nguồn và sóng thứ cấp phát ra từ electron dao động trong vật liệu
C. Lực hút giữa photon và electron làm photon mất năng lượng
D. Ánh sáng bị phản xạ qua lại nhiều lần trong vật liệu

**Đáp án: B**
*Giải thích:* Chiết suất là hiệu ứng giao thoa thuần túy: trường tổng $E = E_s + E_a$ (sóng nguồn + sóng thứ cấp từ electron dao động) tạo ra vận tốc pha biểu kiến $c/n$. Không có photon nào thực sự bị làm chậm.

---

**Câu 2.** Trong mô hình dao động tử Lorentz, chiết suất $n$ của vật liệu có mật độ $N$ electron/m³, tần số cộng hưởng $\omega_0$, dưới tác dụng của ánh sáng tần số $\omega < \omega_0$ là:

A. $n = 1 - \frac{Ne^2}{2\varepsilon_0 m(\omega_0^2 - \omega^2)}$ (nhỏ hơn 1)
B. $n = 1 + \frac{Ne^2}{2\varepsilon_0 m(\omega_0^2 - \omega^2)}$ (lớn hơn 1)
C. $n = \frac{Ne^2}{\varepsilon_0 m\omega_0^2}$ (không phụ thuộc $\omega$)
D. $n = c/\omega_0$ (chỉ phụ thuộc cộng hưởng)

**Đáp án: B**
*Giải thích:* Khi $\omega < \omega_0$, mẫu số $(\omega_0^2 - \omega^2) > 0$, nên $n > 1$. Đây là tán sắc thông thường (normal dispersion): ánh sáng tần số cao (xanh) khúc xạ mạnh hơn ánh sáng tần số thấp (đỏ).

---

**Câu 3.** Hiện tượng tán sắc (dispersion) trong thủy tinh — ánh sáng đỏ và xanh bị khúc xạ khác nhau — có nguyên nhân vi mô là:

A. Photon xanh nặng hơn photon đỏ
B. Chiết suất phụ thuộc vào tần số ánh sáng do $n \propto 1/(\omega_0^2 - \omega^2)$
C. Thủy tinh có cấu trúc tinh thể ưu tiên một số bước sóng
D. Bước sóng ngắn bị hấp thụ nhiều hơn

**Đáp án: B**
*Giải thích:* Công thức Lorentz $n = 1 + Ne^2/[2\varepsilon_0 m(\omega_0^2-\omega^2)]$ cho thấy $n$ phụ thuộc $\omega$. Ánh sáng xanh ($\omega$ cao hơn, gần $\omega_0$ hơn) có $n$ lớn hơn ánh sáng đỏ — đây là nguồn gốc vi mô của tán sắc.

---

**Câu 4 (Tự luận).** Trong hệ giao thoa kế laser của bạn, bạn nhận thấy kết quả đo dịch chuyển bị trôi (drift) theo nhiệt độ phòng, dù cơ cấu cơ khí không thay đổi. Hãy giải thích cơ chế vật lý (liên quan đến chiết suất vi mô) và đề xuất biện pháp khắc phục.

**Gợi ý trả lời mẫu:**
Khi nhiệt độ tăng, mật độ không khí $N$ giảm (theo định luật khí lý tưởng: $N \propto P/T$), dẫn đến chiết suất không khí thay đổi: $n_{\text{air}} - 1 \propto N$. Từ công thức Lorentz, $\Delta n \approx (n_0-1)\Delta T/T$. Với $n_0 - 1 \approx 2.93\times10^{-4}$, mỗi thay đổi $1°C$ gây $\Delta n \approx 10^{-6}$, tương đương sai số quang trình $\Delta L \approx 10^{-6} \times L_{\text{đường đo}}$. Với $L = 1\,\text{m}$, sai số là $1\,\mu\text{m}$.
Biện pháp: (1) bọc toàn bộ đường quang học trong buồng kín kiểm soát nhiệt độ, (2) đo nhiệt độ và áp suất liên tục để bù thermo-optic, (3) dùng vacuum interferometer (loại bỏ không khí hoàn toàn), (4) dùng hai màu laser (two-color interferometry) để đo và bù chiết suất.

---

```json
{
  "questions": [
    {"id": "q1", "type": "mcq", "question": "Tốc độ pha c/n của ánh sáng trong vật liệu là do:", "options": ["A. Photon va chạm với nguyên tử bị làm chậm", "B. Giao thoa giữa sóng tới và sóng thứ cấp từ electron dao động", "C. Lực hút photon-electron làm mất năng lượng", "D. Phản xạ qua lại nhiều lần trong vật liệu"], "answer": "B", "explanation": "Chiết suất là hiệu ứng giao thoa: trường tổng E=Es+Ea tạo vận tốc pha biểu kiến c/n."},
    {"id": "q2", "type": "mcq", "question": "Chiết suất Lorentz khi ω < ω₀ là:", "options": ["A. n = 1 - Ne²/[2ε₀m(ω₀²-ω²)] < 1", "B. n = 1 + Ne²/[2ε₀m(ω₀²-ω²)] > 1", "C. n = Ne²/(ε₀mω₀²)", "D. n = c/ω₀"], "answer": "B", "explanation": "Khi ω<ω₀ mẫu số dương, n>1, tán sắc thông thường."},
    {"id": "q3", "type": "mcq", "question": "Nguyên nhân vi mô của tán sắc (ánh sáng đỏ và xanh khúc xạ khác nhau) là:", "options": ["A. Photon xanh nặng hơn", "B. n phụ thuộc ω qua công thức n∝1/(ω₀²-ω²)", "C. Thủy tinh ưu tiên bước sóng nhất định", "D. Bước sóng ngắn bị hấp thụ nhiều hơn"], "answer": "B", "explanation": "Công thức Lorentz: n tăng theo ω, nên ánh sáng xanh (ω cao) có n lớn hơn đỏ."},
    {"id": "q4", "type": "open", "question": "Giao thoa kế laser bị drift theo nhiệt độ phòng dù cơ khí không đổi. Giải thích cơ chế vật lý và đề xuất khắc phục.", "sample_answer": "Nhiệt độ tăng → mật độ N giảm → n_air giảm → quang trình thay đổi. Biện pháp: buồng kín kiểm soát T, bù thermo-optic, vacuum interferometer, hoặc two-color interferometry."}
  ]
}
```


## Quiz Questions

**Q1:** Tốc độ pha c/n của ánh sáng trong vật liệu là do:
- A) A. Photon va chạm với nguyên tử bị làm chậm
- B) B. Giao thoa giữa sóng tới và sóng thứ cấp từ electron dao động
- C) C. Lực hút photon-electron làm mất năng lượng
- D) D. Phản xạ qua lại nhiều lần trong vật liệu

**Correct:** B

**Explanation:** Chiết suất là hiệu ứng giao thoa: trường tổng E=Es+Ea tạo vận tốc pha biểu kiến c/n.

**Q2:** Chiết suất Lorentz khi ω < ω₀ là:
- A) A. n = 1 - Ne²/[2ε₀m(ω₀²-ω²)] < 1
- B) B. n = 1 + Ne²/[2ε₀m(ω₀²-ω²)] > 1
- C) C. n = Ne²/(ε₀mω₀²)
- D) D. n = c/ω₀

**Correct:** B

**Explanation:** Khi ω<ω₀ mẫu số dương, n>1, tán sắc thông thường.

**Q3:** Nguyên nhân vi mô của tán sắc (ánh sáng đỏ và xanh khúc xạ khác nhau) là:
- A) A. Photon xanh nặng hơn
- B) B. n phụ thuộc ω qua công thức n∝1/(ω₀²-ω²)
- C) C. Thủy tinh ưu tiên bước sóng nhất định
- D) D. Bước sóng ngắn bị hấp thụ nhiều hơn

**Correct:** B

**Explanation:** Công thức Lorentz: n tăng theo ω, nên ánh sáng xanh (ω cao) có n lớn hơn đỏ.

**Q4:** Giao thoa kế laser bị drift theo nhiệt độ phòng dù cơ khí không đổi. Giải thích cơ chế vật lý và đề xuất khắc phục.

**Correct:** N/A


---
*Exported from Feynman Bot*
