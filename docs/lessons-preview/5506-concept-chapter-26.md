---
lesson_id: 5506
lesson_type: concept
approval_status: pending
exported_at: "2026-03-02T15:10:31.298658+00:00"
content_hash: 49da9d2e90ff
chapter_number: 26
chapter_title: Chapter 26
section_number: 4
section_title: 26–3Fermat’s principle of least time
---
# ## Nguyên Lý Thời Gian Ngắn Nhất của Fermat: Ánh Sáng "Thông Minh" Hay Toán Học 

*Source: Chapter 26 - Chapter 26 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_26.html)*

## Nguyên Lý Thời Gian Ngắn Nhất của Fermat: Ánh Sáng "Thông Minh" Hay Toán Học Kỳ Diệu?

Bạn có thấy kỳ lạ không khi một viên đạn được bắn theo đường thẳng - vì nó phải tuân theo định luật Newton từng khoảnh khắc một - nhưng ánh sáng lại "biết" trước đường đi nhanh nhất từ điểm A đến điểm B qua một gương, và lựa chọn đúng đường đó? Đây không phải ma thuật - đây là **nguyên lý Fermat**, một trong những ý tưởng đẹp nhất trong lịch sử vật lý.

**Câu chuyện lịch sử**

Pierre de Fermat, nhà toán học người Pháp, đề xuất vào khoảng năm 1650: ánh sáng, trong tất cả các đường có thể đi từ điểm này đến điểm khác, luôn chọn đường đòi hỏi **thời gian ngắn nhất**. Đây được gọi là **nguyên lý thời gian ngắn nhất** (principle of least time) hay **nguyên lý Fermat** (Fermat's principle).

Thú vị hơn, Hero of Alexandria đã có ý tưởng tương tự từ trước - nhưng ông nói ánh sáng chọn **đường ngắn nhất** (not least time). Điều đó đúng với gương phẳng (đường thẳng và đường phản xạ có cùng độ dài tổng nếu tính đúng), nhưng sai với khúc xạ. Fermat mở rộng thành thời gian ngắn nhất, và điều đó đúng cả cho khúc xạ.

**Phản xạ trên gương phẳng - Chứng minh hình học**

Xét hai điểm A và B, và một gương phẳng MM'. Ánh sáng từ A phản xạ trên gương rồi đến B. Đường nào là nhanh nhất?

Mẹo hình học của Fermat: dựng điểm B' là hình chiếu đối xứng của B qua gương (cùng khoảng cách, bên kia gương). Khi đó mọi đường từ A đến gương rồi đến B đều có tổng chiều dài $AE + EB = AE + EB'$ (vì $EB = EB'$ theo đối xứng).

Đường ngắn nhất từ A đến B' là đường thẳng $AB'$. Đường thẳng này cắt gương tại điểm C - đó chính là điểm phản xạ tối ưu!

Tại điểm C trên đường thẳng $AB'$: góc tới (giữa AE và pháp tuyến gương) bằng góc phản xạ (giữa EB và pháp tuyến). Đây chính xác là **định luật phản xạ** ($\theta_i = \theta_r$)!

**Khúc xạ và định luật Snell**

Bây giờ hãy xét ánh sáng đi từ không khí vào thủy tinh. Tốc độ ánh sáng trong không khí là $c$, trong thủy tinh là $c/n$ (với $n > 1$ là chiết suất). Để tìm đường nhanh nhất, ta phải tính thời gian:

$$t = \frac{\text{khoảng cách trong không khí}}{c} + \frac{\text{khoảng cách trong thủy tinh}}{c/n}$$

Tối thiểu hóa $t$ theo vị trí điểm vào mặt phân cách cho ra:

$$n_1 \sin\theta_1 = n_2 \sin\theta_2$$

Đây là **định luật Snell-Descartes** (Snell's law) - một công thức mà bạn chắc chắn đã dùng trong thiết kế quang học. Và nguyên lý Fermat sinh ra nó một cách tự nhiên!

**Phép so sánh với thiết kế hệ thống tối ưu**

Hãy nghĩ đến bài toán định tuyến tín hiệu trong mạng truyền thông quân sự của bạn: tín hiệu từ đài A cần đến đài B qua một relay C. Nếu relay C có thể đặt ở nhiều vị trí khác nhau, bạn cần chọn vị trí nào để **tổng thời gian trễ** (latency) nhỏ nhất? Đây chính xác là bài toán Fermat, nhưng với tốc độ truyền tin thay vì tốc độ ánh sáng!

Hoặc hình ảnh quen thuộc hơn: người lính cứu người đuối nước. Chạy trên cát nhanh hơn bơi trong nước. Đường đi tối ưu (thời gian ngắn nhất để đến nạn nhân) không phải đường thẳng, mà phải "khúc xạ" tại bờ biển - và góc khúc xạ tuân theo đúng định luật Snell!

**Ý nghĩa sâu xa hơn**

Nguyên lý Fermat không chỉ là mẹo toán học. Nó gợi ra một câu hỏi triết học: ánh sáng có "biết" trước đường đi tối ưu không? Câu trả lời của cơ học lượng tử (qua công trình của Feynman về tích phân đường - path integral): ánh sáng thực sự đi theo **tất cả các đường** đồng thời, và các đường gần đường cực tiểu thời gian cộng nhau có pha gần giống nhau (constructive interference), còn các đường khác triệt tiêu nhau. Đường ta quan sát chính là đường mà các pha cộng lại mạnh nhất.

**Điểm mấu chốt**

- Nguyên lý Fermat (1650): ánh sáng đi theo đường đòi hỏi thời gian ngắn nhất
- Chứng minh hình học bằng phản xạ: dùng điểm đối xứng B', đường thẳng $AB'$ cho điểm phản xạ tối ưu - suy ra $\theta_i = \theta_r$
- Khúc xạ: tối thiểu hóa thời gian tổng suy ra định luật Snell: $n_1\sin\theta_1 = n_2\sin\theta_2$
- Nguyên lý cực tiểu (stationary action) là nền tảng của toàn bộ vật lý lý thuyết hiện đại
- Giải thích đầy đủ từ cơ học lượng tử: ánh sáng đi theo mọi đường, nhưng đường cực tiểu thời gian có giao thoa xây dựng mạnh nhất

---
*Exported from Feynman Bot*
