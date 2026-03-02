---
lesson_id: 5304
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-02T15:10:26.470688+00:00"
content_hash: b4fdcd5e3921
chapter_number: 1
chapter_title: "https://www.feynmanlectures.caltech.edu/I_01.html"
section_number: 1
section_title: 1Atoms in Motion1
---
# ## Quiz: Atoms in Motion – Nền Tảng Vật Lý và Phương Pháp Khoa Học

*Source: Chapter 1 - https://www.feynmanlectures.caltech.edu/I_01.html (Section 1) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_01.html)*

## Quiz: Atoms in Motion – Nền Tảng Vật Lý và Phương Pháp Khoa Học

---

### Câu 1 (Trắc nghiệm)

**Theo Feynman, tiêu chí duy nhất để kiểm chứng tính đúng đắn của một lý thuyết vật lý là gì?**

- A. Sự đồng thuận của cộng đồng khoa học quốc tế
- B. Tính nhất quán toán học của lý thuyết
- C. Thí nghiệm (experiment)
- D. Nguồn gốc và xuất xứ của ý tưởng

**✅ Đáp án: C**

> **Giải thích:** Feynman phát biểu rõ ràng: *"The test of all knowledge is experiment. Experiment is the sole judge of scientific truth."* Dù ý tưởng đến từ đâu – trực giác, giấc mơ, hay suy luận toán học – chỉ có thực nghiệm mới phán xét được tính đúng sai. Đây là nền tảng của phương pháp khoa học (scientific method).

---

### Câu 2 (Trắc nghiệm)

**Đường kính xấp xỉ của một nguyên tử (atom) theo mô tả trong bài là bao nhiêu?**

- A. $10^{-5}$ cm
- B. $10^{-8}$ cm
- C. $10^{-10}$ cm
- D. $10^{-12}$ cm

**✅ Đáp án: B**

> **Giải thích:** Feynman mô tả các nguyên tử có đường kính vào khoảng $10^{-8}$ cm, tức là khoảng $1$ Ångström ($1$ Å $= 10^{-10}$ m). Đây là thang kích thước quan trọng trong vật lý nguyên tử và hóa học. Lưu ý: $10^{-8}$ cm $= 10^{-10}$ m $= 1$ Å, con số rất quen thuộc trong spectroscopy và crystallography.

---

### Câu 3 (Trắc nghiệm)

**Feynman đưa ra lý do nào khiến vật lý KHÔNG thể được dạy bằng cách liệt kê toàn bộ định luật cơ bản ngay từ đầu (giống như hình học Euclid)?**

- A. Các định luật vật lý quá đơn giản, không cần thiết phải trình bày hệ thống
- B. Chúng ta chưa biết hết tất cả các định luật cơ bản, và các định luật đúng đắn đòi hỏi toán học rất phức tạp để diễn đạt
- C. Vật lý không có hệ thống tiên đề (axioms) như toán học
- D. Các thí nghiệm vật lý luôn cho kết quả mâu thuẫn nhau

**✅ Đáp án: B**

> **Giải thích:** Feynman nêu **hai lý do** cụ thể: *(1)* Chúng ta chưa biết hết tất cả các định luật cơ bản – *"there is an expanding frontier of ignorance"*; *(2)* Phát biểu chính xác các định luật vật lý đòi hỏi các khái niệm xa lạ và toán học nâng cao. Điều này khác hoàn toàn với hình học Euclid vốn có hệ tiên đề đóng và hoàn chỉnh trong phạm vi của nó.

---

### Câu 4 (Tự luận mở)

**Câu hỏi:**

Feynman mô tả các nguyên tử có ba tính chất cơ bản: *(1)* chuyển động không ngừng, *(2)* liên kết với nhau theo các cấu hình phức tạp, và *(3)* kháng lại khi bị ép quá gần nhau. Với vai trò là một kỹ sư cơ điện tử (mechatronics engineer) thiết kế hệ thống điều khiển độ chính xác ở cấp độ micromet (micrometer-level precision), bạn hãy phân tích: **Tính chất nào trong ba tính chất trên ảnh hưởng trực tiếp và thực tế nhất đến công việc thiết kế của bạn? Cơ chế ảnh hưởng đó là gì, và bạn xử lý nó như thế nào trong thực tế?**

---

**💡 Gợi ý đáp án mẫu:**

**Tính chất ảnh hưởng trực tiếp nhất: Chuyển động nhiệt không ngừng (thermal motion) → Giãn nở nhiệt (thermal expansion)**

Ở cấp độ điều khiển micromet, chuyển động nhiệt của nguyên tử biểu hiện vĩ mô thành **giãn nở nhiệt** – một nguồn sai số (error source) nghiêm trọng. Ví dụ:

- **Thanh thép dài 1 m** với hệ số giãn nở nhiệt $\alpha \approx 12 \times 10^{-6}$ °C$^{-1}$: chỉ cần nhiệt độ thay đổi $\Delta T = 1°C$ đã gây ra sai lệch $\Delta L = \alpha \cdot L \cdot \Delta T = 12\,\mu m$ – **vượt quá ngưỡng sai số cho phép** trong hệ thống precision control.

- Trong hệ thống **vũ khí quân sự** (military weapons) yêu cầu độ chính xác cao, giãn nở nhiệt của nòng súng, cơ cấu ngắm, hay sensor mount đều phải được bù trừ.

**Cách xử lý thực tế:**
1. **Vật liệu Invar** (Fe-Ni, $\alpha \approx 1.2 \times 10^{-6}$ °C$^{-1}$) cho các chi tiết cơ khí chính xác
2. **Temperature compensation** trong phần mềm điều khiển: đọc sensor nhiệt độ và bù offset theo thời gian thực
3. **Thermal stabilization**: kiểm soát nhiệt độ môi trường trong phòng đo (thường $\pm 0.1°C$)
4. **Differential measurement** với encoder hoặc interferometer laser để loại bỏ sai số chung (common-mode rejection)

**Tính chất (3) – kháng lại khi bị ép gần** cũng liên quan đến **contact mechanics** và **Hertzian contact stress** trong thiết kế bearing và guide rail của hệ thống linear motion, nhưng ảnh hưởng ít tức thì hơn so với giãn nở nhiệt trong vận hành hàng ngày.

---

```json
{
  "questions": [
    {
      "id": "q1",
      "type": "mcq",
      "question": "Theo Feynman, tiêu chí duy nhất để kiểm chứng tính đúng đắn của một lý thuyết vật lý là gì?",
      "options": [
        "A. Sự đồng thuận của cộng đồng khoa học quốc tế",
        "B. Tính nhất quán toán học của lý thuyết",
        "C. Thí nghiệm (experiment)",
        "D. Nguồn gốc và xuất xứ của ý tưởng"
      ],
      "answer": "C",
      "explanation": "Feynman phát biểu rõ ràng: 'The test of all knowledge is experiment. Experiment is the sole judge of scientific truth.' Dù ý tưởng đến từ đâu, chỉ có thực nghiệm mới phán xét được tính đúng sai. Đây là nền tảng của phương pháp khoa học (scientific method)."
    },
    {
      "id": "q2",
      "type": "mcq",
      "question": "Đường kính xấp xỉ của một nguyên tử (atom) theo mô tả trong bài là bao nhiêu?",
      "options": [
        "A. 10^(-5) cm",
        "B. 10^(-8) cm",
        "C. 10^(-10) cm",
        "D. 10^(-12) cm"
      ],
      "answer": "B",
      "explanation": "Feynman mô tả các nguyên tử có đường kính vào khoảng 10^(-8) cm, tức là khoảng 1 Ångström (1 Å = 10^(-10) m). Đây là thang kích thước quan trọng trong vật lý nguyên tử. Lưu ý: 10^(-8) cm = 10^(-10) m = 1 Å."
    },
    {
      "id": "q3",
      "type": "mcq",
      "question": "Feynman đưa ra lý do nào khiến vật lý KHÔNG thể được dạy bằng cách liệt kê toàn bộ định luật cơ bản ngay từ đầu (giống như hình học Euclid)?",
      "options": [
        "A. Các định luật vật lý quá đơn giản, không cần thiết phải trình bày hệ thống",
        "B. Chúng ta chưa biết hết tất cả các định luật cơ bản, và các định luật đúng đắn đòi hỏi toán học rất phức tạp để diễn đạt",
        "C. Vật lý không có hệ thống tiên đề (axioms) như toán học",
        "D. Các thí nghiệm vật lý luôn cho kết quả mâu thuẫn nhau"
      ],
      "answer": "B",
      "explanation": "Feynman nêu hai lý do: (1) Chúng ta chưa biết hết tất cả các định luật cơ bản – 'there is an expanding frontier of ignorance'; (2) Phát biểu chính xác các định luật vật lý đòi hỏi các khái niệm xa lạ và toán học nâng cao, khác hoàn toàn với hình học Euclid."
    },
    {
      "id": "q4",
      "type": "open",
      "question": "Feynman mô tả các nguyên tử có ba tính chất cơ bản: (1) chuyển động không ngừng, (2) liên kết với nhau theo các cấu hình phức tạp, và (3) kháng lại khi bị ép quá gần nhau. Với vai trò là kỹ sư cơ điện tử thiết kế hệ thống điều khiển độ chính xác ở cấp độ micromet, bạn hãy phân tích: Tính chất nào trong ba tính chất trên ảnh hưởng trực tiếp và thực tế nhất đến công việc thiết kế của bạn? Cơ chế ảnh hưởng đó là gì, và bạn xử lý nó như thế nào trong thực tế?",
      "sample_answer": "Tính chất ảnh hưởng trực tiếp nhất là chuyển động nhiệt không ngừng (thermal motion), biểu hiện vĩ mô thành giãn nở nhiệt (thermal expansion). Ở cấp micromet, thay đổi nhiệt độ 1°C trên thanh thép dài 1m gây sai lệch ~12 µm – vượt ngưỡng cho phép. Cách xử lý: dùng vật liệu Invar (α thấp), bù nhiệt độ trong phần mềm điều khiển theo thời gian thực, kiểm soát nhiệt độ môi trường ±0.1°C, và dùng encoder laser với differential measurement để loại bỏ sai số chung (common-mode rejection). Tính chất (3) cũng liên quan đến contact mechanics trong thi


---
*Exported from Feynman Bot*
