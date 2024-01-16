import pygame
import random

platforma = pygame.Rect([400, 400, 107, 107])
sharik = pygame.Rect([600, 500, 50, 50])
platforma.centery = 500
platforma.centerx = 500
speed_y = 2
# speed_x = 4

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

def otbiv_verxniz_shar():
    global speed_y
    if sharik.colliderect(platforma) and platforma.centery >= sharik.centery:
        speed_y = -abs(speed_y)
    elif sharik.colliderect(platforma) and platforma.centery <= sharik.centery:
        speed_y = abs(speed_y)
    sharik.centery += speed_y

# def otbiv_levopravo_shar():
#     global speed_x
#     if sharik.colliderect(platforma) and platforma.centerx >= sharik.centerx:
#         speed_x = -abs(speed_x)
#     elif sharik.colliderect(platforma) and platforma.centerx <= sharik.centerx:
#         speed_x = abs(speed_x)
#     sharik.centerx += speed_x

def otbiv_ot_granic():
    global speed_y
    global speed_x
    if sharik.right >= 1000:
        speed_x = -speed_x
    if sharik.bottom >= 1000:
        speed_y = -speed_y
    if sharik.left <= 0:
        speed_x = -speed_x
    if sharik.top <= 0:
        speed_y = -speed_y