import pygame
from pygame.locals import *
from random import randint

pygame.init()
canvas = pygame.display.set_mode((1920,1080))
pygame.display.set_caption("Computer Dance")
canvas.fill((255,255,255))

def h():
    for event in pygame.event.get():
        if event.type==KEYDOWN and event.key==K_ESCAPE:
            pygame.quit()
            exit()
            
while True:
    r,g,b = randint(0,255),randint(0,255),randint(0,255)
    rgb = (r,g,b)
    canvas.fill(rgb)
    h()
    pygame.display.update()