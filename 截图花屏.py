# Author:PanDaoxi 
import pyautogui as pag
import pygame
from pygame.locals import *
from random import randint

def make(x1,y1,x2,y2):
    pag.screenshot(region=(x1,y1,x2,y2)).save('make.png')
    return pygame.image.load('make.png')
    
w,h = pag.size()
pygame.init()
l = make(0,0,w,h)
canvas = pygame.display.set_mode((w,h))
pygame.display.set_caption('SCREEN')
canvas.fill((255,255,255))
canvas.blit(l,(0,0))

def handle():
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            exit()
def save():
    x1,y1 = randint(50,w+100),randint(50,h+100)
    x2,y2 = randint(50,w-300),randint(50,h-300)
    x3,y3 = randint(0,w),randint(0,h)
    s = make(x1,y1,x2,y2)
    canvas.blit(s,(x3,y3))   

while True:
    if randint(1,5) == 5:
        canvas.blit(l,(0,0))
    if randint(1,20) == 10:
        canvas.fill((randint(0,255),randint(0,255),randint(0,255)))
    save()    
    handle()
    pygame.display.update()
    pygame.time.delay(randint(0,1000))