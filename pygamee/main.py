import pygame

pygame.init()
OX = 600
OY = 600
win = pygame.display.set_mode((OX, OY))

pygame.display.set_caption("COMPUTER TRAINING CENTER GAME")

x = 10
width = 30
height = 30
speed = 25
y =  OY - speed - height


isJump = False
jumpCount = 10
left = False
right = False
animcount = 0

run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > speed:
        x -= speed
    elif keys[pygame.K_RIGHT] and x < OX - speed - width:
        x += speed
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2)/2
            else:
                y -= (jumpCount ** 2)/2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10


    win.fill((0,0,0))
    pygame.draw.rect(win, (0 , 0, 255), (x, y , width, height))
    pygame.display.update()

pygame.quit()
