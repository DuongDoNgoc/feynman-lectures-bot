---
lesson_id: 5331
lesson_type: quiz
approval_status: approved
exported_at: "2026-02-28T10:51:40.098963+00:00"
content_hash: 71b63c340d61
chapter_number: 4
chapter_title: Chapter 4
section_number: 1
section_title: 4Conservation of Energy
---
# ## Quiz: Bảo Toàn Năng Lượng (Conservation of Energy)

*Source: Chapter 4 - Chapter 4 (Section 1) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_04.html)*

## Quiz: Bảo Toàn Năng Lượng (Conservation of Energy)

---

### Câu 1 (Trắc nghiệm)

**Định luật bảo toàn năng lượng phát biểu điều gì về bản chất của nó?**

A. Nó mô tả cơ chế cụ thể của các hiện tượng tự nhiên

B. Nó là một đại lượng số (numerical quantity) không thay đổi dù tự nhiên biến đổi như thế nào

C. Nó chỉ áp dụng cho các hệ thống cơ học, không áp dụng cho nhiệt học

D. Nó là một định luật gần đúng với nhiều ngoại lệ đã biết

**✅ Đáp án: B**

> **Giải thích:** Feynman nhấn mạnh rằng bảo toàn năng lượng là một *abstract idea* — không phải mô tả cơ chế, mà là một **sự thật toán học**: tồn tại một đại lượng số mà ta tính được trước và sau khi tự nhiên "diễn trò", kết quả vẫn như nhau. Đây là điều kỳ diệu và chính xác tuyệt đối theo hiểu biết hiện tại — *"no known exception."*

---

### Câu 2 (Trắc nghiệm)

**Trong phép loại suy "Dennis the Menace," người mẹ phát minh ra công thức cân hộp đồ chơi để đếm khối bên trong. Điều này tương ứng với khái niệm nào trong vật lý?**

A. Động năng (Kinetic Energy) $\approx \dfrac{\text{Wt}}{g}\dfrac{v^2}{2}$

B. Thế năng hấp dẫn (Gravitational Potential Energy) $\approx \text{Wt} \cdot \text{Height}$

C. Năng lượng ẩn (hidden energy) không quan sát trực tiếp được, nhưng suy ra gián tiếp qua đại lượng khác

D. Năng lượng nhiệt (thermal energy) từ ma sát

**✅ Đáp án: C**

> **Giải thích:** Người mẹ không thể *nhìn thấy* các khối trong hộp, nhưng **suy ra số lượng** thông qua phép đo trọng lượng hộp. Đây là phép loại suy cho các dạng năng lượng **không quan sát trực tiếp** (ví dụ: năng lượng hạt nhân, năng lượng nội tại). Vật lý cũng vậy — ta không "thấy" năng lượng, mà **tính toán** nó qua các đại lượng đo được. Đây chính là sức mạnh của nguyên lý bảo toàn.

---

### Câu 3 (Trắc nghiệm)

**Biểu thức động năng (Kinetic Energy) $KE = \dfrac{1}{2}mv^2$ có điều kiện áp dụng nào sau đây?**

A. Vật phải chuyển động theo đường thẳng

B. Vận tốc $v$ phải nhỏ hơn nhiều so với tốc độ ánh sáng ($v \ll c$)

C. Khối lượng $m$ phải lớn hơn 1 kg

D. Không có điều kiện nào, công thức áp dụng phổ quát

**✅ Đáp án: B**

> **Giải thích:** Feynman ghi rõ điều kiện: $v \ll \textit{speed of light}$. Khi $v$ tiệm cận tốc độ ánh sáng $c$, phải dùng công thức tương đối tính (relativistic): $KE = (\gamma - 1)mc^2$ với $\gamma = \dfrac{1}{\sqrt{1-v^2/c^2}}$. Trong kỹ thuật cơ điện tử thông thường, $v \ll c$ luôn thỏa mãn, nên $KE = \dfrac{1}{2}mv^2$ hoàn toàn đủ chính xác.

---

### Câu 4 (Tự luận mở)

**Câu hỏi:**

Trong công việc thiết kế hệ thống điều khiển chính xác ở mức micromet (micrometer-level precision control), bạn thường phải đối mặt với các nguồn năng lượng "ẩn" — tương tự như các khối trong hộp đồ chơi mà người mẹ không thể nhìn thấy trực tiếp.

Hãy liên hệ nguyên lý **bảo toàn năng lượng** với ít nhất **2 tình huống thực tế** trong hệ thống automation hoặc vũ khí chính xác của bạn, trong đó:
- Năng lượng "ẩn" hoặc "rò rỉ" gây ra sai số không mong muốn
- Bạn đã (hoặc có thể) áp dụng tư duy bảo toàn năng lượng để **chẩn đoán và bù trừ** sai số đó

---

**💡 Gợi ý trả lời mẫu:**

**Tình huống 1 — Nhiệt năng trong hệ truyền động (Thermal Energy in Actuators):**
Trong hệ thống điều khiển vị trí dùng động cơ servo hoặc piezoelectric actuator, khi hoạt động liên tục, điện năng đầu vào không chuyển hóa hoàn toàn thành cơ năng hữu ích. Một phần bị "ẩn" dưới dạng **nhiệt năng** do điện trở cuộn dây và ma sát. Nhiệt này gây giãn nở nhiệt (thermal expansion) của kết cấu cơ khí, tạo ra **drift** ở mức micromet — phá vỡ độ chính xác. Tư duy bảo toàn năng lượng giúp ta *định lượng* lượng nhiệt sinh ra ($Q = I^2 R \cdot t$), từ đó thiết kế bù nhiệt (thermal compensation) hoặc hệ thống làm mát chủ động.

**Tình huống 2 — Năng lượng đàn hồi trong kết cấu (Elastic Strain Energy):**
Trong hệ thống định vị chính xác (precision positioning stage), lực tác động lên cơ cấu tạo ra **biến dạng đàn hồi** (elastic deformation) — dạng thế năng đàn hồi $U = \dfrac{1}{2}kx^2$ "ẩn" trong kết cấu. Nếu không tính đến, encoder đọc vị trí motor nhưng *đầu công tác* thực tế lệch vị trí do độ đàn hồi của trục, khớp nối. Hiểu bảo toàn năng lượng giúp kỹ sư thiết kế **closed-loop feedback** đo trực tiếp tại đầu công tác, hoặc mô hình hóa độ cứng (stiffness modeling) để bù sai số.

---

```json
{
  "questions": [
    {
      "id": "q1",
      "type": "mcq",
      "question": "Định luật bảo toàn năng lượng phát biểu điều gì về bản chất của nó?",
      "options": [
        "A. Nó mô tả cơ chế cụ thể của các hiện tượng tự nhiên",
        "B. Nó là một đại lượng số (numerical quantity) không thay đổi dù tự nhiên biến đổi như thế nào",
        "C. Nó chỉ áp dụng cho các hệ thống cơ học, không áp dụng cho nhiệt học",
        "D. Nó là một định luật gần đúng với nhiều ngoại lệ đã biết"
      ],
      "answer": "B",
      "explanation": "Feynman nhấn mạnh bảo toàn năng lượng là một abstract idea — không mô tả cơ chế mà là sự thật toán học: tồn tại một đại lượng số tính được trước và sau khi tự nhiên biến đổi, kết quả vẫn như nhau. Không có ngoại lệ nào được biết đến ('no known exception')."
    },
    {
      "id": "q2",
      "type": "mcq",
      "question": "Trong phép loại suy 'Dennis the Menace,' người mẹ phát minh ra công thức cân hộp đồ chơi để đếm khối bên trong. Điều này tương ứng với khái niệm nào trong vật lý?",
      "options": [
        "A. Động năng (Kinetic Energy) ≈ (Wt/g)(v²/2)",
        "B. Thế năng hấp dẫn (Gravitational Potential Energy) ≈ Wt × Height",
        "C. Năng lượng ẩn không quan sát trực tiếp được, nhưng suy ra gián tiếp qua đại lượng khác",
        "D. Năng lượng nhiệt (thermal energy) từ ma sát"
      ],
      "answer": "C",
      "explanation": "Người mẹ không thể nhìn thấy các khối trong hộp nhưng suy ra số lượng qua phép đo trọng lượng. Đây là phép loại suy cho các dạng năng lượng không quan sát trực tiếp (năng lượng hạt nhân, nội năng...). Vật lý cũng vậy — ta không 'thấy' năng lượng mà tính toán nó qua các đại lượng đo được."
    },
    {
      "id": "q3",
      "type": "mcq",
      "question": "Biểu thức động năng KE = (1/2)mv² có điều kiện áp dụng nào sau đây?",
      "options": [
        "A. Vật phải chuyển động theo đường thẳng",
        "B. Vận tốc v phải nhỏ hơn nhiều so với tốc độ ánh sáng (v ≪ c)",
        "C. Khối lượng m phải lớn hơn 1 kg",
        "D. Không có điều kiện nào, công thức áp dụng phổ quát"
      ],
      "answer": "B",
      "explanation": "Feynman ghi rõ điều kiện: v ≪ speed of light. Khi v tiệm cận c, phải dùng công thức tương đối tính KE = (γ-1)mc². Trong kỹ thuật cơ điện tử thông thường, điều kiện v ≪ c luôn thỏa mãn nên KE = (1/2)mv² hoàn toàn đủ chính xác."
    },
    {
      "id": "q4",
      "type": "open",
      "question": "Trong công việc thiết kế hệ thống điều khiển chính xác ở mức micromet (micrometer-level precision control), bạn thường phải đối mặt với các nguồn năng lượng 'ẩn' — tương tự như các khối trong hộp đồ chơi mà người mẹ không thể nhìn thấy trực tiếp. Hãy liên hệ nguyên lý bảo toàn năng lượng với ít nhất 2 tình huống thực tế trong hệ thống automation hoặc vũ khí chính xác của bạn, trong đó năng lượng 'ẩn' hoặc 'rò rỉ' gây ra sai số không mong muốn, và bạn có thể áp dụng tư duy bảo toàn năng lượng để chẩn đoán và bù trừ sai số đó.",


---
*Exported from Feynman Bot*
