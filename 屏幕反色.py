import cv2
import pygame
from pygame.locals import *
from pyautogui import screenshot
from random import randint
from time import sleep

screenshot(region = (0,0,1920,1080)).save('sshot.png')
im = pygame.image.load('sshot.png')
pygame.init()
canvas = pygame.display.set_mode((1920,1080))
pygame.display.set_caption('SCREEN')
for i in range(0,100): canvas.blit(im,(0,0))

def f():
    screenshot(region = (0,0,1920,1080)).save('sshots.png')
    img = cv2.imread('sshots.png', 1)
    img_shape = img.shape
    h = img_shape[0]
    w = img_shape[1]
    dst = 255 - img
    x = randint(100000,999999)
    cv2.imwrite("save%d.png" % x,dst,[cv2.IMWRITE_PNG_COMPRESSION,0])
    i = pygame.image.load("save%d.png" % x)
    canvas.blit(i,(0,0))
    cv2.waitKey(0)
    
def h():
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            exit()

while True:
    f()
    h()
    pygame.display.update()
    pygame.time.delay(randint(500,3500))