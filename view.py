import pygame
import model
pygame.init()
font = pygame.font.SysFont("arial", 27, True)
fontgo = pygame.font.SysFont("comicsansms", 80, True)
risgo = fontgo.render("GAME OVER", True, [255, 255, 255])
wgo = risgo.get_width()
hgo = risgo.get_height()
go = pygame.Rect([600,500, wgo,hgo])
go.centery = 500
go.centerx = 500

def taimer():
    global cifri,risur,rishp,risgo
    straydari = str(model.ydari)
    strur = str(model.ur)
    strhp = str(model.hp)
    cifri = font.render("| осталось "+straydari+" ударов", True, [254, 255, 243])
    risur = font.render("уровень " + strur, True, [254, 255, 243])
    rishp = font.render("осталось " + strhp + " жизни", True, [254, 255, 243])

def ekran():
    taimer()
    display.fill([0, 0, 0])
    if model.hp >= 0:
        display.blit(cifri, [200, 55])
        display.blit(risur, [80, 55])
        display.blit(rishp, [700, 55])
        pygame.draw.rect(display, [5, 211, 255], model.platforma)
        pygame.draw.rect(display, [140, 209, 243], model.platforma, 3)
        pygame.draw.circle(display, [255, 105, 0], model.sharik.center, 25)
    if model.hp < 0:
        display.blit(risgo, go)
        pygame.display.set_caption("GAME OVER")
    pygame.display.flip()

display = pygame.display.set_mode([1000, 1000])
