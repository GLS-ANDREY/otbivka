import pygame
import random

rect = pygame.Rect([400,400,100,100])
rect.centery = 500
rect.centerx = 500

def ppl():
    rect.left = 0
    if rect.left == 0:
        rect.y = 0
        rect.height += 1000