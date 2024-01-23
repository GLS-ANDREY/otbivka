import pygame
import random
import model
pygame.init()
font = pygame.font.SysFont("arial", 27, True)
def taimer():
    global cifri
    cifri = font.render("model.a", True, [254, 255, 243])


def ekran():
    display.fill([0, 0, 0])
    display.blit(cifri, [500, 55])
    pygame.draw.rect(display, [219, 16, 0], model.platforma)
    pygame.draw.rect(display, [140, 209, 243], model.platforma, 3)
    # pygame.draw.rect(display, [140,209,243], model.sharik, 3)
    pygame.draw.circle(display, [17, 255, 15], model.sharik.center, 25)
    pygame.display.flip()


display = pygame.display.set_mode([1000, 1000])
