import pygame
import random
import model


def ekran():
    display.fill([0, 0, 0])
    pygame.draw.rect(display,[219,16,0],model.rect)
    pygame.draw.rect(display,[140,209,243],model.rect,3)
    pygame.display.flip()


display = pygame.display.set_mode([1000, 1000])
