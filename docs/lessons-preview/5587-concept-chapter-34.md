---
lesson_id: 5587
lesson_type: concept
approval_status: pending
exported_at: "2026-03-03T15:33:08.658898+00:00"
content_hash: 84ebd7463c40
chapter_number: 34
chapter_title: Chapter 34
section_number: 10
section_title: 34–9The momentum of light
---
# ## Áp Suất Bức Xạ: Khi Ánh Sáng Đẩy Vật Chất

*Source: Chapter 34 - Chapter 34 (Section 10) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_34.html)*

## Áp Suất Bức Xạ: Khi Ánh Sáng Đẩy Vật Chất

Bạn có bao giờ nghĩ rằng một chùm laser — thứ không có khối lượng, không có va chạm cơ học — lại có thể đẩy một vật thể vật chất không? Trong các hệ thống đo lường precision mà bạn làm việc hàng ngày, cảm biến interferometric đôi khi phải bù trừ một lực cực nhỏ gây ra bởi chính chùm ánh sáng đo đang chiếu vào gương. Lực đó là áp suất bức xạ — và nó bắt nguồn từ trường từ của ánh sáng, một thứ chúng ta ít khi nhắc đến.

**Tại sao từ trường của ánh sáng lại quan trọng?**

Khi ánh sáng chiếu vào một điện tích (ví dụ electron trong vật liệu), trường điện $E$ của sóng điện từ làm điện tích dao động. Giả sử trường điện nằm theo phương $x$, điện tích sẽ di chuyển theo phương $x$ với vận tốc $v$. Thông thường ta chỉ chú ý đến lực điện, nhưng còn có trường từ $B$ vuông góc với trường điện. Khi điện tích đang chuyển động (vì bị trường điện kéo), trường từ tác dụng lên nó một lực Lorentz $F = qvB$ — và hướng của lực này chính là hướng truyền sóng của ánh sáng!

Đây là cơ chế sinh ra áp suất bức xạ: trường điện rung điện tích lên-xuống, trường từ "đẩy" điện tích đang-rung về phía trước. Hai trường phối hợp như một cặp đôi ăn ý, giống hệt cơ chế của động cơ bước (stepper motor) trong robot CNC của bạn: một cuộn từ làm nhiệm vụ kích thích dao động, cuộn kia chuyển dao động thành chuyển động tịnh tiến.

**Độ lớn của lực: Năng lượng và động lượng của photon**

Tính toán cho thấy lực bức xạ trung bình bằng:

$$\langle F angle = rac{dW/dt}{c}$$

trong đó $dW/dt$ là công suất ánh sáng được hấp thụ và $c$ là tốc độ ánh sáng. Đây là một mối quan hệ vô cùng sâu sắc: **áp lực ánh sáng tác dụng lên vật đúng bằng công suất hấp thụ chia cho $c$**. Vật hấp thụ càng nhiều năng lượng từ ánh sáng, nó bị đẩy càng mạnh về phía trước.

Nếu ánh sáng không bị hấp thụ mà bị phản chiếu hoàn toàn từ gương, lực sẽ gấp đôi — vì động lượng đổi chiều.

Từ quan điểm lượng tử, mỗi photon mang năng lượng $W = \hbar\omega$ và động lượng:

$$p = rac{W}{c} = rac{\hbar\omega}{c} = \hbar k$$

Điều này có nghĩa là ánh sáng không chỉ mang năng lượng mà còn mang động lượng, và hai đại lượng này liên hệ với nhau bởi hệ số $1/c$.

**Ứng dụng thực tế trong đo lường precision**

Trong các hệ interferometer laser độ phân giải nm hoặc sub-nm (như hệ đo vị trí trong máy photolithography), chùm laser đo lường tác dụng một lực nhỏ lên gương phản xạ. Với gương khối lượng $m = 1\,	ext{g}$ và chùm laser $P = 1\,	ext{mW}$:

$$F = rac{2P}{c} = rac{2 	imes 10^{-3}}{3	imes10^8} pprox 6.7 	imes 10^{-12}\,	ext{N} = 6.7\,	ext{pN}$$

Lực pico-Newton này tương đương gia tốc $6.7\,	ext{nm/s}^2$ cho gương 1g — nhỏ nhưng không thể bỏ qua trong hệ thống độ chính xác cao ở thang đo nm/giây trong nhiều giờ.

Trong thiết bị quân sự như hệ ngắm bắn laser, áp suất bức xạ cũng là một yếu tố cần cân nhắc khi tính toán ảnh hưởng tích lũy của chùm laser công suất cao lên các gương điều hướng.

**Sự thống nhất cổ điển và lượng tử**

Điều kỳ diệu nhất trong câu chuyện này là: từ phép tính hoàn toàn cổ điển (lực Lorentz + sóng điện từ), ta đã suy ra đúng công thức $p = \hbar k$ — công thức lượng tử mô tả động lượng photon. Cơ học cổ điển và cơ học lượng tử gặp nhau ở điểm này.

**Điểm mấu chốt**

Ánh sáng tác dụng lực lên vật chất không chỉ qua trường điện mà còn qua trường từ của sóng điện từ. Lực bức xạ trung bình bằng công suất ánh sáng hấp thụ chia cho $c$. Mỗi photon mang động lượng $p = \hbar\omega/c = \hbar k$ theo hướng truyền sóng. Trong hệ đo lường precision laser, áp suất bức xạ — dù rất nhỏ — có thể tích lũy thành sai số đo lường cần bù trừ.

---
*Exported from Feynman Bot*
