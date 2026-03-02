---
lesson_id: 5412
lesson_type: quiz
approval_status: approved
exported_at: "2026-03-02T15:10:28.796922+00:00"
content_hash: fd148ccfe3f8
chapter_number: 13
chapter_title: Chapter 13
section_number: 4
section_title: 13–3Summation of energy
---
# Quiz: Hệ Nhiều Vật — Bảo Toàn Năng Lượng

*Source: Chapter 13 - Chapter 13 (Section 4) | [📖 Nguồn](https://www.feynmanlectures.caltech.edu/I_13.html)*

# Quiz: Hệ Nhiều Vật — Bảo Toàn Năng Lượng

## Câu 1

Hệ 3 vật gồm Trái Đất, Mặt Trăng, và tàu Apollo. Số lượng cặp tương tác hấp dẫn cần xét trong tính toán thế năng tổng là:

A) 1 cặp
B) 2 cặp
C) 3 cặp
D) 6 cặp

**Đáp án: C**

*Giải thích: Với $N = 3$ vật, số cặp là $N(N-1)/2 = 3(2)/2 = 3$ cặp: (Đất-Trăng), (Đất-Apollo), (Trăng-Apollo). Thế năng tổng: $U = U_{12} + U_{13} + U_{23}$. Mỗi cặp tính đúng một lần.*

## Câu 2

Trong phương trình chuyển động robot: $M(\vec{q})\ddot{\vec{q}} + C(\vec{q},\dot{\vec{q}})\dot{\vec{q}} + G(\vec{q}) = \vec{\tau}$. Số hạng $G(\vec{q})$ biểu diễn:

A) Lực Coriolis và ly tâm do các khớp quay
B) Gradient thế năng trọng lực theo tọa độ khớp
C) Lực ma sát trong ổ trục
D) Mô-men quán tính của toàn hệ

**Đáp án: B**

*Giải thích: $G(\vec{q}) = \frac{\partial U(\vec{q})}{\partial \vec{q}}$ là gradient thế năng trọng lực theo vector tọa độ khớp $\vec{q}$. Trong điều khiển robot, bù $G(\vec{q})$ real-time là yêu cầu cơ bản để giữ robot ở vị trí mong muốn mà không cần lực khớp liên tục.*

## Câu 3

Điều kiện nào đảm bảo bảo toàn năng lượng trong hệ nhiều vật tương tác?

A) Tất cả vật phải có cùng khối lượng
B) Tất cả lực phải là nội lực (không có ngoại lực)
C) Lực tương tác cặp $(i,j)$ thỏa mãn Newton III và thế năng $U_{ij}$ chỉ phụ thuộc $r_{ij}$
D) Hệ phải có ít hơn 10 vật

**Đáp án: C**

*Giải thích: Hai điều kiện đủ: (1) Newton III: $\vec{F}_{ij} = -\vec{F}_{ji}$ — đảm bảo các công bù nhau theo cặp; (2) $U_{ij} = U(r_{ij})$ — đảm bảo thế năng xác định và đối xứng. Không cần đồng khối lượng hay giới hạn số vật.*

## Câu 4 — Tự Luận

Trong hệ thống robot hàn có 3 link chuyển động (khối lượng $m_1 = 5\,kg$, $m_2 = 3\,kg$, $m_3 = 2\,kg$, độ cao trọng tâm $h_1 = 0.3\,m$, $h_2 = 0.7\,m$, $h_3 = 1.1\,m$ ở tư thế thẳng đứng). Tính thế năng trọng lực tổng. Khi robot gập lại đến tư thế nằm ngang ($h_1' = 0.3\,m$, $h_2' = 0.3\,m$, $h_3' = 0.3\,m$), thế năng giải phóng là bao nhiêu và motor có thể thu hồi năng lượng này không?

*Gợi ý: $U_{tổng} = \sum m_i g h_i$; thế năng giải phóng = $U_{đứng} - U_{nằm}$; thu hồi bằng phanh tái sinh*

```json
{
  "quiz_id": 5412,
  "questions": [
    {"id": 1, "answer": "C", "concept": "số cặp trong hệ N vật = N(N-1)/2"},
    {"id": 2, "answer": "B", "concept": "G(q) = gradient thế năng trọng lực theo khớp"},
    {"id": 3, "answer": "C", "concept": "điều kiện bảo toàn: Newton III + thế năng đối xứng"}
  ]
}
```


## Quiz Questions

**Q1:** No question text

**Correct:** C

**Q2:** No question text

**Correct:** B

**Q3:** No question text

**Correct:** C


---
*Exported from Feynman Bot*
