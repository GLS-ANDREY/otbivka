import pygame
import random

platforma = pygame.Rect([400, 400, 107, 107])
sharik = pygame.Rect([600, 500, 50, 50])
platforma.centery = 500
platforma.centerx = 500
speed_x = 4
speed_y = 2
ydari = 5
ur = 1
hp = 3

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
    global speed_y, ydari
    if sharik.colliderect(platforma) and platforma.centery == 972:
        speed_y = -abs(speed_y)
        sharik.bottom = 945
        ydari -= 1
        urovenb()
    elif sharik.colliderect(platforma) and platforma.centery == 27:
        speed_y = abs(speed_y)
        sharik.top = 55
        ydari -= 1
        urovenb()
    if hp > 0:
        sharik.centery += speed_y


def otbiv_levopravo_shar():
    global speed_x, ydari
    if sharik.colliderect(platforma) and platforma.centerx == 972:
        speed_x = -abs(speed_x)
        sharik.right = 945
        ydari -= 1
        urovenb()
    elif sharik.colliderect(platforma) and platforma.centerx == 27:
        speed_x = abs(speed_x)
        sharik.left = 55
        ydari -= 1
        urovenb()
    if hp > 0:
        sharik.centerx += speed_x


def urovenb():
    global ur, ydari, speed_y, speed_x, hp
    if ydari == 0:
        ur += 1
        hp += 1
        ydari = 5
        rr = random.randint(1, 2)
        if rr == 1 and speed_y <= 0:
            speed_y += -1
        elif rr == 1 and speed_y >= 0:
            speed_y += 1
        if rr == 2 and speed_x <= 0:
            speed_x += -1
        elif rr == 2 and speed_x >= 0:
            speed_x += 1

def speed_sharik():
    ssx = str(speed_x)
    ssy = str(speed_y)
    if hp > 0:
        pygame.display.set_caption("x:" + ssx + " y:" + ssy)


def otbiv_ot_granic():
    global speed_y, speed_x, hp
    if sharik.right >= 1000:
        speed_x = -speed_x
        hp -= 1
    if sharik.bottom >= 1000:
        speed_y = -speed_y
        hp -= 1
    if sharik.left <= 0:
        speed_x = -speed_x
        hp -= 1
    if sharik.top <= 0:
        speed_y = -speed_y
        hp -= 1
