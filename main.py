import pygame

pygame.init()
window = pygame.display.set_mode((480, 320))

button1 = pygame.Rect(110, 110, 100, 50)
button2 = pygame.Rect(270, 110, 100, 50)

button1_pressed = False
button2_pressed = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.FINGERDOWN:
            touch_pos = (event.x * window.get_width(), event.y * window.get_height())
            if button1.collidepoint(touch_pos):
                button1_pressed = True
            elif button2.collidepoint(touch_pos):
                button2_pressed = True
        elif event.type == pygame.FINGERUP:
            touch_pos = (event.x * window.get_width(), event.y * window.get_height())
            if button1.collidepoint(touch_pos):
                button1_pressed = False
            elif button2.collidepoint(touch_pos):
                button2_pressed = False
    
    if button1_pressed and button2_pressed:
        print("Both buttons are pressed!")

    window.fill((255, 255, 255))  # 화면을 흰색으로 채움
    pygame.draw.rect(window, (255, 0, 0) if button1_pressed else (0, 255, 0), button1)  # 버튼1을 그림
    pygame.draw.rect(window, (255, 0, 0) if button2_pressed else (0, 255, 0), button2)  # 버튼2를 그림
    pygame.display.flip()

pygame.quit()