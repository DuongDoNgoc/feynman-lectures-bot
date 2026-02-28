---
lesson_id: 5340
lesson_type: quiz
approval_status: approved
exported_at: "2026-02-28T11:31:20.175789+00:00"
content_hash: c6f47f5fa7ba
chapter_number: 5
chapter_title: Chapter 5
section_number: 5
section_title: 5–4Long times
---
# ## Quiz: Đo Thời Gian Dài và Phân Rã Phóng Xạ

*Source: Chapter 5 - Chapter 5 (Section 5) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_05.html)*

## Quiz: Đo Thời Gian Dài và Phân Rã Phóng Xạ

### Câu 1
Một mẫu gỗ cổ đại còn lại 25% hoạt độ Carbon-14 so với mẫu hiện đại ($T_{1/2}(C-14) = 5730$ năm). Tuổi của mẫu gỗ là:

A. 5,730 năm
B. 11,460 năm
C. 17,190 năm
D. 22,920 năm

**Đáp án: B**
*Giải thích: 25% = $(1/2)^2$ → đã trải qua 2 chu kỳ bán rã. $t = 2 \times 5730 = 11,460$ năm.*

### Câu 2
Nguồn phóng xạ RTG Plutonium-238 ($T_{1/2} = 87.7$ năm) có công suất ban đầu 100 W. Sau 175.4 năm (= $2 T_{1/2}$), công suất còn lại là:

A. 50 W
B. 25 W
C. 12.5 W
D. 0 W

**Đáp án: B**
*Giải thích: Sau mỗi $T_{1/2}$, công suất giảm một nửa. Sau 2 chu kỳ: $P = 100 \times (1/2)^2 = 25$ W.*

### Câu 3
Tại sao đồng hồ phóng xạ đáng tin cậy hơn vòng cây để đo thời gian địa chất (hàng triệu năm)?

A. Phóng xạ chính xác hơn vì chu kỳ bán rã ngắn hơn
B. Vòng cây chỉ sống tối đa vài nghìn năm; phân rã phóng xạ tiếp tục không phụ thuộc điều kiện môi trường
C. Phóng xạ không bị ảnh hưởng bởi khí hậu như vòng cây
D. Cả B và C đều đúng

**Đáp án: D**
*Giải thích: Vòng cây giới hạn ~10,000 năm (tuổi thọ cây). Phóng xạ: (1) kéo dài tỷ năm, (2) không phụ thuộc điều kiện môi trường — hai lợi thế bổ sung nhau.*

### Câu 4 (Tự luận)
Như một kỹ sư thiết kế hệ thống có tuổi thọ dài hạn (ví dụ: thiết bị quân sự, cảm biến tự động ngoài hiện trường cần hoạt động 10-20 năm không bảo trì), bạn áp dụng khái niệm "hằng số phân rã" $\lambda$ như thế nào để lên lịch bảo trì hoặc ước tính tuổi thọ của linh kiện? So sánh với phân rã phóng xạ.

*Gợi ý trả lời mẫu: Mô hình Weibull cho tuổi thọ linh kiện: $R(t) = e^{-(t/\eta)^\beta}$, tương tự $N(t) = N_0 e^{-\lambda t}$ khi $\beta=1$ (hỏng ngẫu nhiên). Khác nhau: $\lambda$ linh kiện phụ thuộc điều kiện (nhiệt độ, tải, ăn mòn), còn $\lambda$ phóng xạ là hằng số vật lý. Áp dụng: đo MTBF (Mean Time Between Failures) → tính $\lambda_{component}$ → lên lịch bảo trì trước khi $R(t)$ giảm dưới ngưỡng chấp nhận (thường 90% hay 99.9% tùy yêu cầu an toàn).*

```json
{"questions": [{"id": "q1", "type": "mcq", "question": "Mẫu gỗ còn lại 25% hoạt độ C-14 (T½=5730 năm). Tuổi mẫu gỗ?", "options": ["A. 5,730 năm", "B. 11,460 năm", "C. 17,190 năm", "D. 22,920 năm"], "answer": "B", "explanation": "25% = (1/2)² → 2 chu kỳ bán rã → t = 2×5730 = 11,460 năm"}, {"id": "q2", "type": "mcq", "question": "RTG Pu-238 (T½=87.7 năm) công suất 100W ban đầu. Sau 175.4 năm?", "options": ["A. 50 W", "B. 25 W", "C. 12.5 W", "D. 0 W"], "answer": "B", "explanation": "Sau 2 chu kỳ bán rã: P = 100×(½)² = 25 W"}, {"id": "q3", "type": "mcq", "question": "Tại sao đồng hồ phóng xạ đáng tin cậy hơn vòng cây để đo thời gian địa chất?", "options": ["A. Chu kỳ bán rã ngắn hơn", "B. Vòng cây giới hạn vài nghìn năm; phóng xạ không phụ thuộc môi trường", "C. Phóng xạ không bị ảnh hưởng khí hậu", "D. Cả B và C"], "answer": "D", "explanation": "Vòng cây bị giới hạn tuổi thọ cây; phóng xạ kéo dài tỷ năm và độc lập với điều kiện môi trường."}, {"id": "q4", "type": "open", "question": "Bạn áp dụng khái niệm hằng số phân rã λ như thế nào để ước tính tuổi thọ linh kiện trong hệ thống dài hạn? So sánh với phân rã phóng xạ.", "sample_answer": "Mô hình Weibull R(t)=exp(-(t/η)^β), tương tự N(t)=N₀e^(-λt) khi β=1. Khác: λ linh kiện phụ thuộc điều kiện vận hành, λ phóng xạ là hằng số tuyệt đối. Áp dụng: đo MTBF → tính λ_component → lên lịch bảo trì trước khi R(t) dưới ngưỡng an toàn."}]}
```


## Quiz Questions

**Q1:** Mẫu gỗ còn lại 25% hoạt độ C-14 (T½=5730 năm). Tuổi mẫu gỗ?
- A) A. 5,730 năm
- B) B. 11,460 năm
- C) C. 17,190 năm
- D) D. 22,920 năm

**Correct:** B

**Explanation:** 25% = (1/2)² → 2 chu kỳ bán rã → t = 2×5730 = 11,460 năm

**Q2:** RTG Pu-238 (T½=87.7 năm) công suất 100W ban đầu. Sau 175.4 năm?
- A) A. 50 W
- B) B. 25 W
- C) C. 12.5 W
- D) D. 0 W

**Correct:** B

**Explanation:** Sau 2 chu kỳ bán rã: P = 100×(½)² = 25 W

**Q3:** Tại sao đồng hồ phóng xạ đáng tin cậy hơn vòng cây để đo thời gian địa chất?
- A) A. Chu kỳ bán rã ngắn hơn
- B) B. Vòng cây giới hạn vài nghìn năm; phóng xạ không phụ thuộc môi trường
- C) C. Phóng xạ không bị ảnh hưởng khí hậu
- D) D. Cả B và C

**Correct:** D

**Explanation:** Vòng cây bị giới hạn tuổi thọ cây; phóng xạ kéo dài tỷ năm và độc lập với điều kiện môi trường.

**Q4:** Bạn áp dụng khái niệm hằng số phân rã λ như thế nào để ước tính tuổi thọ linh kiện trong hệ thống dài hạn? So sánh với phân rã phóng xạ.

**Correct:** N/A


---
*Exported from Feynman Bot*
