import pygame
import random
import model
pygame.init()
font = pygame.font.SysFont("arial", 100, True)
print(pygame.font.get_fonts())
def taimer():
    global cifri,risur,rishp,risgo
    straydari = str(model.ydari)
    strur = str(model.ur)
    strhp = str(model.hp)
    cifri = font.render("| осталось "+straydari+" ударов", True, [254, 255, 243])
    risur = font.render("уровень " + strur, True, [254, 255, 243])
    rishp = font.render("осталось " + strhp + " жизни", True, [254, 255, 243])
    risgo = font.render("GAME OVER",True,[255,255,255])

def ekran():
    taimer()
    display.fill([0, 0, 0])
    if model.hp != 0:
        display.blit(cifri, [200, 55])
        display.blit(risur, [80, 55])
        display.blit(rishp, [700, 55])
        display.blit(risgo,[396,469])
        pygame.draw.rect(display, [219, 16, 0], model.platforma)
        pygame.draw.rect(display, [140, 209, 243], model.platforma, 3)
        # pygame.draw.rect(display, [140,209,243], model.sharik, 3)
        pygame.draw.circle(display, [17, 255, 15], model.sharik.center, 25)
    k = risgo.get_width()
    l = risgo.get_height()
    print(k)
    print(l)
    pygame.display.flip()


display = pygame.display.set_mode([1000, 1000])
