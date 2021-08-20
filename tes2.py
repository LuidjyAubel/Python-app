import pygame, sys
from pygame.locals import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480))
pygame.display.set_caption('app python')

#Chargement et collage du fond
fond = pygame.image.load("background.png").convert()
fenetre.blit(fond, (0,0))

#Chargement et collage du personnage
perso = pygame.image.load("xwing.png").convert_alpha()
position_perso = perso.get_rect()
fenetre.blit(perso, position_perso)

#Rafraîchissement de l'écran
pygame.display.flip()

#BOUCLE INFINIE
running = True
while running:
    for event in pygame.event.get():      #recupere les differents events existant
        if event.type == KEYDOWN:         #Gestion des touches
            if event.key == K_LEFT:
              print("left")
              position_perso = position_perso.move(-10,0)
            if event.key == K_RIGHT:
              print("right")
              position_perso = position_perso.move(10,0)
        if event.type == pygame.QUIT:       #compare si l'event est la croix pour fermer la fenetre
            running = False
            pygame.quit()
            sys.exit()
    fenetre.blit(fond, (0,0))
    fenetre.blit(perso, position_perso)
    pygame.display.flip()
