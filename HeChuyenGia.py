import pygame, sys, os
os.system('pip install pygame')

pygame.init()

# Cửa sổ
WIDTH, HEIGHT = 700, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hệ chuyên gia - Hỗ trợ học tập")

# Font chữ
font_question = pygame.font.Font("./Assets/ariali.ttf", 28)
font_answer = pygame.font.Font("./Assets/ariali.ttf", 24)

# Ảnh nền
background = pygame.image.load("./Assets/Background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Câu hỏi, lựa chọn
questions = [
    ("Bạn có đang gặp khó khăn hiểu bài không?", "khó hiểu bài",
     ["Không", "Ít", "Thỉnh thoảng", "Thường xuyên"]),
    ("Bạn có đủ tài liệu học tập không?", "thiếu tài liệu",
     ["Thiếu nhiều", "Thiếu ít", "Đủ"]),
    ("Bạn có sắp làm bài thi không?", "sắp thi",
     ["Không", "Còn lâu", "Sắp tới", "Ngày mai"]),
    ("Bạn đã ôn bài chưa?", "chưa ôn bài",
     ["Chưa", "Ít", "Đang ôn", "Ôn kỹ"]),
    ("Bạn có hay mất tập trung không?", "mất tập trung",
     ["Không", "Ít", "Thỉnh thoảng", "Rất nhiều"]),
    ("Bạn có thức khuya học bài không?", "học đêm khuya",
     ["Không", "Thỉnh thoảng", "Thường xuyên"]),
    ("Bạn có cảm thấy căng thẳng không?", "căng thẳng",
     ["Không", "Ít", "Thỉnh thoảng", "Rất nhiều"]),
    ("Bạn có cảm thấy áp lực học tập không?", "áp lực cao",
     ["Không", "Ít", "Trung bình", "Rất cao"])
]

# Rules
rules = [
    # Hiểu bài + Tài liệu
    {
        'conditions': {'khó hiểu bài': "Thường xuyên", 'thiếu tài liệu': "Thiếu nhiều"},
        'advice': 'Bạn nên bổ sung tài liệu học tập (sách, slide, bài tập) và ôn lại kiến thức cơ bản.'
    },
    {
        'conditions': {'khó hiểu bài': "Thường xuyên", 'thiếu tài liệu': "Đủ"},
        'advice': 'Hãy trao đổi với thầy cô hoặc bạn bè để được giải thích kỹ hơn.'
    },
    {
        'conditions': {'khó hiểu bài': "Ít", 'thiếu tài liệu': "Thiếu ít"},
        'advice': 'Bạn có thể tìm thêm tài liệu online hoặc video hướng dẫn để củng cố kiến thức.'
    },
    {
        'conditions': {'khó hiểu bài': "Không"},
        'advice': 'Bạn đang nắm bài khá tốt, hãy duy trì cách học hiện tại.'
    },

    # Ôn thi
    {
        'conditions': {'sắp thi': "Ngày mai", 'chưa ôn bài': "Chưa"},
        'advice': 'Khẩn trương lập dàn ý, ôn nhanh các ý chính và luyện bài tập trọng tâm.'
    },
    {
        'conditions': {'sắp thi': "Sắp tới", 'chưa ôn bài': "Ít"},
        'advice': 'Bạn nên phân chia thời gian hợp lý mỗi ngày để ôn dần.'
    },
    {
        'conditions': {'sắp thi': "Còn lâu"},
        'advice': 'Bạn có thời gian, hãy học từ từ và đừng dồn đến phút cuối.'
    },

    # Tập trung + Giấc ngủ
    {
        'conditions': {'mất tập trung': "Rất nhiều", 'học đêm khuya': "Thường xuyên"},
        'advice': 'Bạn nên thay đổi thói quen, học buổi sáng và ngủ đủ 7-8 tiếng.'
    },
    {
        'conditions': {'mất tập trung': "Thỉnh thoảng"},
        'advice': 'Bạn nên nghỉ giải lao ngắn sau mỗi 30-45 phút học.'
    },
    {
        'conditions': {'học đêm khuya': "Thỉnh thoảng"},
        'advice': 'Cố gắng hạn chế thức khuya, chỉ dùng khi thật sự cần thiết.'
    },
    {
        'conditions': {'học đêm khuya': "Không"},
        'advice': 'Thói quen ngủ sớm rất tốt, hãy tiếp tục duy trì.'
    },

    # Tinh thần + Áp lực
    {
        'conditions': {'căng thẳng': "Rất nhiều", 'áp lực cao': "Rất cao"},
        'advice': 'Bạn nên nghỉ ngơi, tập thể dục nhẹ, hoặc chia sẻ với bạn bè để giảm áp lực.'
    },
    {
        'conditions': {'căng thẳng': "Ít", 'áp lực cao': "Trung bình"},
        'advice': 'Cân bằng học và giải trí, đừng học quá sức.'
    },
    {
        'conditions': {'căng thẳng': "Không"},
        'advice': 'Tinh thần bạn đang ổn định, hãy duy trì điều này.'
    },
    {
        'conditions': {'áp lực cao': "Ít"},
        'advice': 'Áp lực thấp là tốt, bạn có thể tập trung hơn vào việc hoàn thiện kiến thức.'
    }
]

# Biến toàn cục
facts = {}
current_question = 0
results = []
state = "menu"
option_btns = []

# Hàm suy luận
def infer(facts):
    applied = []
    for rule in rules:
        if all(facts.get(k) == v for k, v in rule['conditions'].items()):
            applied.append(rule['advice'])
    return applied

# Hàm cắt từ xuống dòng
def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines, current_line = [], ""
    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    lines.append(current_line.strip())
    return lines

# Hàm vẽ nút
def draw_button(text, x, y, w, h, color, text_color=(0,0,0)):
    pygame.draw.rect(screen, color, (x, y, w, h), border_radius=10)
    label = font_answer.render(text, True, text_color)
    rect = label.get_rect(center=(x + w//2, y + h//2))
    screen.blit(label, rect)
    return pygame.Rect(x, y, w, h)

# Begin
running = True
while running:
    screen.blit(background, (0, 0))
    mx, my = pygame.mouse.get_pos()

    # Nút Thoát
    quit_btn = draw_button("Thoát", WIDTH - 100, 20, 80, 40, (255,100,100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if quit_btn.collidepoint(mx, my):
                running = False

            if state == "menu":
                if start_btn.collidepoint(mx, my):
                    facts = {}
                    current_question = 0
                    results = []
                    state = "asking"

            elif state == "asking":
                for btn, opt in option_btns:
                    if btn.collidepoint(mx, my):
                        facts[questions[current_question][1]] = opt
                        current_question += 1
                        if current_question >= len(questions):
                            results = infer(facts)
                            state = "result"

            elif state == "result":
                if end_btn.collidepoint(mx, my):
                    state = "menu"

    if state == "menu":
        title = font_question.render("Hệ chuyên gia hỗ trợ học tập", True, (0,0,0))
        rect = title.get_rect(center=(WIDTH//2, HEIGHT//3))
        screen.blit(title, rect)
        start_btn = draw_button("Bắt đầu", WIDTH//2 - 80, HEIGHT//2, 160, 60, (144,238,144))

    elif state == "asking":
        wrapped = wrap_text(questions[current_question][0], font_question, WIDTH - 100)
        y = HEIGHT//4
        for line in wrapped:
            q_text = font_question.render(line, True, (0,0,0))
            q_rect = q_text.get_rect(center=(WIDTH//2, y))
            screen.blit(q_text, q_rect)
            y += 40

        # Vẽ các lựa chọn
        options = questions[current_question][2]
        option_btns = []
        start_y = HEIGHT//2 - (len(options) * 60)//2
        for i, opt in enumerate(options):
            btn = draw_button(opt, WIDTH//2 - 100, start_y + i*70, 200, 50, (173,216,230))
            option_btns.append((btn, opt))

    elif state == "result":
        if results:
            y = 150
            for advice in results:
                wrapped = wrap_text("- " + advice, font_answer, WIDTH - 100)
                for line in wrapped:
                    line_text = font_answer.render(line, True, (0,0,0))
                    rect = line_text.get_rect(center=(WIDTH//2, y))
                    screen.blit(line_text, rect)
                    y += 35
                y += 15
        else:
            msg = font_answer.render("Không phát hiện vấn đề. Hãy duy trì thói quen tốt!", True, (0,0,0))
            rect = msg.get_rect(center=(WIDTH//2, HEIGHT//2))
            screen.blit(msg, rect)

        end_btn = draw_button("Kết thúc", WIDTH//2 - 80, HEIGHT - 100, 160, 60, (144,238,144))

    pygame.display.flip()

pygame.quit()
sys.exit()