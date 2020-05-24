import pygame
from pygame.transform import flip, scale

movingRight = []
movingLeft = []
Idle = []

winSize = (650)
x, y = 0, (winSize-80 - 46)
height, width = 80, 80


walkcount = 0
LEFT = False
RIGHT = False
jump = False

jumpPower = 10
neg = 1
velocity = 10


for n in range(1, 11):
    movingRight.append(
        scale(pygame.image.load(f'assets/Walk{n}.png'), (height, width)))
    movingLeft.append(scale(flip(pygame.image.load(
        f'assets/Walk{n}.png'), True, False), (width, height)))
    Idle.append(scale(pygame.image.load(
        f'assets/Idle{n}.png'), (width, height)))

bg = scale(pygame.image.load('assets/img.jpg'), (winSize, winSize))
