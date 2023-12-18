import pygame
import random

rect = pygame.Rect([400,400,100,100])
rect2 = pygame.Rect([600,500,50,50])
rect.centery = 500
rect.centerx = 500
speed_y = 3

def ppl():
    rect.left = 0
    rect.y = 0
    rect.height = 1000
    rect.width = 55
def ppp():
    rect.y = 0
    rect.height = 1000
    rect.width = 55
    rect.right = 1000
def ppv():
    rect.top = 0
    rect.x = 0
    rect.width = 1000
    rect.height = 55
def ppn():
    rect.x = 0
    rect.width = 1000
    rect.height = 55
    rect.bottom = 1000

def otbiv_niz_shar():
    global speed_y
    if rect2.colliderect(rect):
        speed_y = -3
    elif speed_y != -3:
        speed_y = 3
    rect2.centery += speed_y
def otbiv_verx_shar():
    global speed_y
    if rect2.colliderect(rect):
        speed_y = 3
    elif speed_y != 3:
        speed_y = -3




















