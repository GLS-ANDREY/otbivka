import pygame
import random

rect = pygame.Rect([400,400,100,100])
rect2 = pygame.Rect([600,50,50,50])
rect.centery = 500
rect.centerx = 500

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

def rect_shar():
    speed_y = 3
    rect2.centery += speed_y