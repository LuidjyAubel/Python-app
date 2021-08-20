# Créé par luidjy, le 20/08/2021 en Python 3.7
import pygame, sys

pygame.init()
screen = pygame.display.set_mode((600, 600)) #taille de la fenetre
pygame.display.set_caption('app python')
screen.fill((0, 0, 0))                 #couleur de fond de la fenetre

red = (255,0,0)
pygame.draw.rect(screen, red,((50,50),(150,100)),1)
pygame.display.update()
running = True                              #variable booléen pour savoir si le programme est demarré

while running:
    for event in pygame.event.get():        #recupere les differents events existant
        if event.type == pygame.QUIT:       #compare si l'event est la croix pour fermer la fenetre
            running = False
            pygame.quit()
            sys.exit()