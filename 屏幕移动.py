import pygame
from pygame.locals import *
from pyautogui import screenshot
from random import randint

def f():
    global bg
    screenshot(region = (0,0,1920,1080)).save('sshot.png')
    bg = pygame.image.load('sshot.png')

f()
pygame.init()
canvas = pygame.display.set_mode((1920,1080))
canvas.fill((255,255,255))
pygame.display.set_caption('MOVE')

def h():
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            exit()

x1 = 0
y1 = 0
height = 1080
x2 = 0
y2 = -height

x3 = 0
y3 = 0
width = 1920
x4 = 0
y4 = 0
n = randint(0,1)
while True:
    if n:
        canvas.blit(bg,(x1,y1))
        y1 += 3
        canvas.blit(bg,(x2,y2))
        y2 += 3
        if y1 > height:
            y1 = -height
        if y2 > height:
            y2 = -height
    else:
        canvas.blit(bg,(x3,y3))
        x3 += 3
        canvas.blit(bg,(x4,y4))
        x4 += 3
        if x3 > width:
            x3 = -width
        if x4 > width:
            x4 = -width
    h()
    pygame.display.update()