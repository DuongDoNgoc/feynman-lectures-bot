---
lesson_id: 5337
lesson_type: quiz
approval_status: approved
exported_at: "2026-02-28T10:51:40.215108+00:00"
content_hash: 83acb95fdff6
chapter_number: 5
chapter_title: Chapter 5
section_number: 1
section_title: 5Time and Distance
---
# ## Quiz: Đo Lường Thời Gian và Khoảng Cách

*Source: Chapter 5 - Chapter 5 (Section 1) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_05.html)*

## Quiz: Đo Lường Thời Gian và Khoảng Cách

### Câu 1
Định nghĩa hiện tại (1983) của 1 mét là:

A. Chiều dài của thanh platinum-iridium chuẩn tại Paris
B. 1/40,000,000 chu vi Trái Đất
C. 1,650,763.73 bước sóng ánh sáng Krypton-86
D. Khoảng cách ánh sáng đi trong chân không trong 1/299,792,458 giây

**Đáp án: D**
*Giải thích: Từ 1983, 1 mét định nghĩa qua tốc độ ánh sáng $c = 299,792,458$ m/s — bất biến, không phụ thuộc vật liệu vật lý cụ thể.*

### Câu 2
Một hệ servo di chuyển với tốc độ $v = 2$ m/s. Đồng hồ lấy mẫu có jitter $\Delta t = 500$ ns. Sai số vị trí do jitter gây ra là:

A. 0.1 μm
B. 1 μm
C. 10 μm
D. 100 μm

**Đáp án: B**
*Giải thích: $\Delta x = v \cdot \Delta t = 2 \times 500 \times 10^{-9} = 10^{-6}$ m = 1 μm.*

### Câu 3
Tại sao đồng hồ trên vệ tinh GPS phải được hiệu chỉnh hiệu ứng tương đối tính?

A. Vì nhiệt độ ngoài vũ trụ làm chậm dao động nguyên tử
B. Vì vệ tinh chuyển động nhanh (làm chậm đồng hồ) và ở trong trường hấp dẫn yếu hơn (làm nhanh đồng hồ), tổng hợp là nhanh hơn ~38 μs/ngày
C. Vì tín hiệu GPS cần bù thời gian truyền qua khí quyển
D. Vì đồng hồ nguyên tử Cs bị ảnh hưởng bởi bức xạ vũ trụ

**Đáp án: B**
*Giải thích: Hiệu ứng tương đối tính đặc biệt (v cao → chậm ~7 μs/ngày) và tổng quát (trường hấp dẫn yếu → nhanh ~45 μs/ngày) cộng lại: đồng hồ GPS nhanh ~38 μs/ngày so với mặt đất. Nếu không hiệu chỉnh, GPS sẽ sai ~10 km/ngày.*

### Câu 4 (Tự luận)
Trong hệ thống đo lường hoặc điều khiển chính xác cao mà bạn đang làm việc (đo lường ở cấp micrometer), yếu tố môi trường nào (nhiệt độ, rung động, v.v.) ảnh hưởng lớn nhất đến độ chính xác của phép đo thời gian hoặc khoảng cách? Bạn xử lý vấn đề này như thế nào trong thực tế?

*Gợi ý trả lời mẫu: Nhiệt độ là yếu tố lớn nhất — biến dạng nhiệt của chi tiết cơ khí ($\alpha \approx 11.7 \times 10^{-6}/°C$ cho thép), thay đổi chỉ số khúc xạ không khí ảnh hưởng laser interferometer. Xử lý bằng: kiểm soát nhiệt phòng ±0.1°C, bù nhiệt tự động qua cảm biến Pt100, đo lường ở 20°C chuẩn (ISO 1).*

```json
{"questions": [{"id": "q1", "type": "mcq", "question": "Định nghĩa hiện tại (1983) của 1 mét là gì?", "options": ["A. Chiều dài thanh platinum-iridium chuẩn tại Paris", "B. 1/40,000,000 chu vi Trái Đất", "C. 1,650,763.73 bước sóng ánh sáng Kr-86", "D. Khoảng cách ánh sáng đi trong chân không trong 1/299,792,458 giây"], "answer": "D", "explanation": "Từ 1983, mét định nghĩa qua tốc độ ánh sáng c=299,792,458 m/s, bất biến và không phụ thuộc vật liệu."}, {"id": "q2", "type": "mcq", "question": "Servo di chuyển v=2 m/s, jitter Δt=500 ns. Sai số vị trí?", "options": ["A. 0.1 μm", "B. 1 μm", "C. 10 μm", "D. 100 μm"], "answer": "B", "explanation": "Δx = v×Δt = 2×500×10⁻⁹ = 10⁻⁶ m = 1 μm"}, {"id": "q3", "type": "mcq", "question": "Tại sao đồng hồ vệ tinh GPS phải được hiệu chỉnh tương đối tính?", "options": ["A. Nhiệt độ vũ trụ làm chậm dao động nguyên tử", "B. Vệ tinh chuyển động nhanh + trường hấp dẫn yếu → nhanh ~38 μs/ngày", "C. Bù thời gian truyền qua khí quyển", "D. Bức xạ vũ trụ ảnh hưởng Cs"], "answer": "B", "explanation": "Hiệu ứng tương đối tính: đặc biệt (-7μs/ngày) + tổng quát (+45μs/ngày) = +38μs/ngày. Không hiệu chỉnh → sai ~10km/ngày."}, {"id": "q4", "type": "open", "question": "Yếu tố môi trường nào ảnh hưởng lớn nhất đến độ chính xác đo lường micromet trong hệ thống của bạn? Cách xử lý?", "sample_answer": "Nhiệt độ: biến dạng nhiệt của chi tiết và thay đổi chỉ số khúc xạ. Xử lý: kiểm soát phòng ±0.1°C, bù nhiệt tự động, đo ở 20°C chuẩn ISO 1."}]}
```


## Quiz Questions

**Q1:** Định nghĩa hiện tại (1983) của 1 mét là gì?
- A) A. Chiều dài thanh platinum-iridium chuẩn tại Paris
- B) B. 1/40,000,000 chu vi Trái Đất
- C) C. 1,650,763.73 bước sóng ánh sáng Kr-86
- D) D. Khoảng cách ánh sáng đi trong chân không trong 1/299,792,458 giây

**Correct:** D

**Explanation:** Từ 1983, mét định nghĩa qua tốc độ ánh sáng c=299,792,458 m/s, bất biến và không phụ thuộc vật liệu.

**Q2:** Servo di chuyển v=2 m/s, jitter Δt=500 ns. Sai số vị trí?
- A) A. 0.1 μm
- B) B. 1 μm
- C) C. 10 μm
- D) D. 100 μm

**Correct:** B

**Explanation:** Δx = v×Δt = 2×500×10⁻⁹ = 10⁻⁶ m = 1 μm

**Q3:** Tại sao đồng hồ vệ tinh GPS phải được hiệu chỉnh tương đối tính?
- A) A. Nhiệt độ vũ trụ làm chậm dao động nguyên tử
- B) B. Vệ tinh chuyển động nhanh + trường hấp dẫn yếu → nhanh ~38 μs/ngày
- C) C. Bù thời gian truyền qua khí quyển
- D) D. Bức xạ vũ trụ ảnh hưởng Cs

**Correct:** B

**Explanation:** Hiệu ứng tương đối tính: đặc biệt (-7μs/ngày) + tổng quát (+45μs/ngày) = +38μs/ngày. Không hiệu chỉnh → sai ~10km/ngày.

**Q4:** Yếu tố môi trường nào ảnh hưởng lớn nhất đến độ chính xác đo lường micromet trong hệ thống của bạn? Cách xử lý?

**Correct:** N/A


---
*Exported from Feynman Bot*
