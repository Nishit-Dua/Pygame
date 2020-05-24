from assets import *
import pygame
pygame.init()


win = pygame.display.set_mode((winSize, winSize))
pygame.display.set_caption('Rectange Moving')

clock = pygame.time.Clock()


walkcount = 0
LEFT = False
RIGHT = False
jump = False

jumpPower = 10
neg = 1
velocity = 10


def drawShit():
    global walkcount
    win.blit(bg, (0, 0))
    if walkcount >= 30:
        walkcount = 0
    if LEFT:
        win.blit(movingLeft[walkcount//3], (x, y))
        walkcount += 1
    elif RIGHT:
        win.blit(movingRight[walkcount//3], (x, y))
        walkcount += 1
    else:
        win.blit(Idle[walkcount//3], (x, y))
        walkcount += 1
    pygame.display.update()


run = True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= velocity
        LEFT = True
        RIGHT = False
    elif keys[pygame.K_RIGHT] and x < winSize - height:
        x += velocity
        LEFT = False
        RIGHT = True
    else:
        LEFT = False
        RIGHT = False
        walkcount = 0
    if not jump:
        if keys[pygame.K_SPACE]:
            jump = True
            LEFT = False
            RIGHT = False
    else:
        if jumpPower < 0:
            neg = -1
        if jumpPower >= -10:
            y -= (jumpPower**2) * 0.5 * neg
            jumpPower -= 1
            walkcount = 0
        else:
            neg = 1
            jump = False
            jumpPower = 10

    drawShit()
