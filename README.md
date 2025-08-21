# Hệ chuyên gia hỗ trợ học tập
## Thông tin cá nhân
  - Họ Tên: Nguyễn Sư Thành Đạt
  - MSSV: 23110089
  - Lớp: ARIN330585_05CLC

## Ứng dụng hệ chuyên gia viết bằng Python + Pygame giúp tự đánh giá tình trạng học tập của mình và nhận lời khuyên phù hợp.
## Tính năng
  - Hỏi nhiều câu hỏi về thói quen học tập, tinh thần, giấc ngủ, tài liệu.
  - Người dùng chọn mức độ (Không / Ít / Thỉnh thoảng / Thường xuyên, …).
  - Suy luận dựa trên tập luật có sẵn và đưa ra lời khuyên theo tập luật đó cho người dùng.
  - Giao diện trực quan với nút bấm, font chữ, ảnh nền đơn giản, dễ sử dụng.

## Cấu trúc thư mục
```
  .
  ├── Assets/
  │   ├── ariali.ttf          # Font chữ
  │   ├── Background.png      # Ảnh nền
  ├── HeChuyenGia.py          # Code chính
  └── README.md               # Tài liệu
```

## Nguyên lý hoạt động
  - Các facts được lưu lại từ câu trả lời của người dùng.
  - Tập luật định nghĩa điều kiện và lời khuyên.
  - Hàm infer() sẽ suy luận, tìm các luật phù hợp và đưa ra lời khuyên.
  - Ví dụ:
    - Nếu bạn thường xuyên khó hiểu bài và thiếu nhiều tài liệu → Lời khuyên: bổ sung tài liệu học tập và ôn lại kiến thức cơ bản.
    - Nếu bạn căng thẳng rất nhiều và áp lực cao → Lời khuyên: nghỉ ngơi, tập thể dục nhẹ, chia sẻ với bạn bè.

## Tập luật
| Điều kiện (facts) | Lời khuyên |
|-------------------|------------|
| khó hiểu bài (Thường xuyên) + thiếu tài liệu (Thiếu nhiều) | Bổ sung tài liệu học tập (sách, slide, bài tập) và ôn lại kiến thức cơ bản |
| khó hiểu bài (Thường xuyên) + thiếu tài liệu (Đủ) | Hãy trao đổi với thầy cô hoặc bạn bè để được giải thích kỹ hơn |
| khó hiểu bài (Ít) + thiếu tài liệu (Thiếu ít) | Tìm thêm tài liệu online hoặc video hướng dẫn để củng cố kiến thức |
| khó hiểu bài (Không) | Bạn đang nắm bài khá tốt, hãy duy trì cách học hiện tại |
| sắp thi (Ngày mai) + chưa ôn bài (Chưa) | Khẩn trương lập dàn ý, ôn nhanh các ý chính và luyện bài tập trọng tâm |
| sắp thi (Sắp tới) + chưa ôn bài (Ít) | Bạn nên phân chia thời gian hợp lý mỗi ngày để ôn dần |
| sắp thi (Còn lâu) | Bạn có thời gian, hãy học từ từ và đừng dồn đến phút cuối |
| mất tập trung (Rất nhiều) + học đêm khuya (Thường xuyên) | Bạn nên thay đổi thói quen, học buổi sáng và ngủ đủ 7-8 tiếng |
| mất tập trung (Thỉnh thoảng) | Bạn nên nghỉ giải lao ngắn sau mỗi 30-45 phút học |
| học đêm khuya (Thỉnh thoảng) | Cố gắng hạn chế thức khuya, chỉ dùng khi thật sự cần thiết |
| học đêm khuya (Không) | Thói quen ngủ sớm rất tốt, hãy tiếp tục duy trì |
| căng thẳng (Rất nhiều) + áp lực cao (Rất cao) | Bạn nên nghỉ ngơi, tập thể dục nhẹ, hoặc chia sẻ với bạn bè để giảm áp lực |
| căng thẳng (Ít) + áp lực cao (Trung bình) | Cân bằng học và giải trí, đừng học quá sức |
| căng thẳng (Không) | Tinh thần bạn đang ổn định, hãy duy trì điều này |
| áp lực cao (Ít) | Áp lực thấp là tốt, bạn có thể tập trung hơn vào việc hoàn thiện kiến thức |
