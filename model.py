import pygame
import random

platforma = pygame.Rect([400, 400, 107, 107])
sharik = pygame.Rect([600, 500, 50, 50])
platforma.centery = 500
platforma.centerx = 500
speed_y = 3
# speed_x = 3

def ppl():
    platforma.left = 0
    platforma.y = 0
    platforma.height = 1000
    platforma.width = 55
def ppp():
    platforma.y = 0
    platforma.height = 1000
    platforma.width = 55
    platforma.right = 1000
def ppv():
    platforma.top = 0
    platforma.x = 0
    platforma.width = 1000
    platforma.height = 55
def ppn():
    platforma.x = 0
    platforma.width = 1000
    platforma.height = 55
    platforma.bottom = 1000

def otbiv_niz_shar():
    global speed_y
    if sharik.colliderect(platforma) and platforma.centery >= sharik.centery:
        speed_y = -3
    elif sharik.colliderect(platforma) and platforma.centery <= sharik.centery:
        speed_y = 3
    sharik.centery += speed_y

def otbiv_pravo_shar():
    global speed_x
    if sharik.colliderect(platforma):
        speed_x = -3
    sharik.centerx += speed_x
def otbiv_levo_shar():
    global speed_x
    if sharik.colliderect(platforma):
        speed_x = 3




















