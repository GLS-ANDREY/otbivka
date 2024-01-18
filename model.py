import pygame
import random

platforma = pygame.Rect([400, 400, 107, 107])
sharik = pygame.Rect([600, 500, 50, 50])
platforma.centery = 500
platforma.centerx = 500
speed_y = 2
speed_x = 4
a = 1


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
    if sharik.colliderect(platforma) and platforma.centery == 972:
        speed_y = -abs(speed_y)  # poletit vverx
        sharik.bottom = 945
    elif sharik.colliderect(platforma) and platforma.centery == 27:
        speed_y = abs(speed_y)  # poletit vniz
        sharik.top = 55
    sharik.centery += speed_y


def otbiv_levopravo_shar():
    global speed_x
    if sharik.colliderect(platforma) and platforma.centerx == 972:
        speed_x = -abs(speed_x)  # poletit vlevo
        sharik.right = 945
    elif sharik.colliderect(platforma) and platforma.centerx == 27:
        speed_x = abs(speed_x)  # poletit vpravo
        sharik.left = 55
    sharik.centerx += speed_x


def schet():
    global a
    if sharik.colliderect(platforma):
        print(a)
        a += 1

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
