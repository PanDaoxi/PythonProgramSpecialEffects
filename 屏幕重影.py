import pygame
from pygame.locals import *
from pyautogui import screenshot

pygame.init()
canvas = pygame.display.set_mode((800,800))
pygame.display.set_caption('Sshot')
canvas.fill((255,255,255))
screenshot(region = (0,0,800,800)).save('sshot.png')
i = pygame.image.load('sshot.png')
canvas.blit(i,(0,0))

def h():
    for event in pygame.event.get():
        if event.type==KEYDOWN and event.key==K_ESCAPE:
            pygame.quit()
            exit()

while True:
    canvas.blit(i,(0,0))
    screenshot(region = (0,0,800,800)).save('sshot.png')
    i = pygame.image.load('sshot.png')
    h()
    pygame.display.update()