import pygame
import model

def allsobitiya():
    s = pygame.event.get()


    for a in s:
        if a.type == pygame.KEYDOWN and (a.key == pygame.K_a or a.key == pygame.K_LEFT):
            model.ppl()
        if a.type == pygame.KEYDOWN and (a.key == pygame.K_d or a.key == pygame.K_RIGHT):
            model.ppp()
        if a.type == pygame.KEYDOWN and (a.key == pygame.K_w or a.key == pygame.K_UP):
            model.ppv()
        if a.type == pygame.KEYDOWN and (a.key == pygame.K_s or a.key == pygame.K_DOWN):
            model.ppn()
        if a.type == pygame.QUIT:
            exit()