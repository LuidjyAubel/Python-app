# Créé par luidjy, le 20/08/2021 en Python 3.7
import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480), RESIZABLE) #taille de la fenetre
pygame.display.set_caption('app python')
screen.fill((0, 0, 0))                 #couleur de fond de la fenetre

red = (255,0,0)
"""pygame.draw.rect(screen, red,((50,50),(100,100)),1)
pygame.display.update()"""
#chargement du xwing
perso = pygame.image.load("xwing.png").convert_alpha()
#screen.blit(perso, (300,240))
#déplacement xwing
posXW = perso.get_rect()
screen.blit(perso, posXW)
pygame.display.flip()                      #update la fenetre entiere

running = True                              #variable booléen pour savoir si le programme est demarré

while running:
    for event in pygame.event.get():      #recupere les differents events existant
        if event.type == KEYDOWN:         #Gestion des touches
            if event.key == K_LEFT:
              print("left")
              posXW = posXW.move(-10,0)
            if event.key == K_RIGHT:
              print("right")
              posXW = posXW.move(10,0)
        if event.type == pygame.QUIT:       #compare si l'event est la croix pour fermer la fenetre
            running = False
            pygame.quit()
            sys.exit()

    #collage
    screen.blit(perso, posXW)
    pygame.display.flip()