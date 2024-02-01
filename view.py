import pygame
import random
import model
pygame.init()
font = pygame.font.SysFont("arial", 27, True)
def taimer():
    global cifri,yr,oz
    straydari = str(model.ydari)
    strur = str(model.ur)
    strhp = str(model.hp)
    cifri = font.render("| осталось "+straydari+" ударов", True, [254, 255, 243])
    yr = font.render("уровень "+strur, True, [254, 255, 243])
    oz = font.render("осталось " + strhp + " жизни", True, [254, 255, 243])

def ekran():
    taimer()
    display.fill([0, 0, 0])
    display.blit(cifri, [200, 55])
    display.blit(yr, [80, 55])
    display.blit(oz, [700, 55])
    pygame.draw.rect(display, [219, 16, 0], model.platforma)
    pygame.draw.rect(display, [140, 209, 243], model.platforma, 3)
    # pygame.draw.rect(display, [140,209,243], model.sharik, 3)
    pygame.draw.circle(display, [17, 255, 15], model.sharik.center, 25)
    pygame.display.flip()


display = pygame.display.set_mode([1000, 1000])
