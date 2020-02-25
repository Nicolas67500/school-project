import pygame

from pygame.locals import *
import os
import sys
import math

# from Images import *

# 16 Janvier. Corentin et Nicolas: On a réussi à faire défiler le sol et le fond à différente vitesse lorque l'on
# presse les touches.

# 17 Janvier. Nicolas: Mise en place du personnage et animation en fonction des touches
# Problème à régler: Bug d'animation quand le personnage va à droite
# 18 Janvier. Nicolas: Animation du personnage faite et ajout de la musique d'ambiance et des bruits de pas
# Problème à régler: le bruit des pas ne se fait qu'une seul fois et ne recommence pas quand j'appuie sur une touche

W, H = 1280, 720  # Définition de l'écran
silencieux = 0  # Son coupé



pygame.init()

    # Ecran définition
ecran = pygame.display.set_mode((W, H))

    # Icone -------
icone = pygame.image.load("Images/icone.jpeg")
pygame.display.set_icon(icone)
    # Titre -------
pygame.display.set_caption("The Story of Gerald")

    # Time -------------
clock = pygame.time.Clock()

accueil = pygame.image.load("Accueil.png")

def fade():
    fade = pygame.Surface((W, H))
    fade.fill((0, 0, 0))
    for alpha in range(0, 300, 2):
        fade.set_alpha(alpha)
        ecran.blit(accueil, (0, 0))
        ecran.blit(fade, (0, 0))
        pygame.display.update()

def menu():
    run = True
    pygame.mixer.music.load("Sons/campfire.wav")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.fadeout(400)
    pygame.mixer.music.play()
    while run:
        ecran.blit(accueil, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    fade()
                    run = False

        pygame.display.flip()

def main():
    # Sons pas ----------------
    sonpas = pygame.mixer.Sound("Sons/sonpas.wav")
    sonpas.set_volume(0.4)
    joue = silencieux

    # Jean le png
    Jean = pygame.image.load("Images/under.png")
    Jean = pygame.transform.scale(Jean, (200, 120))

    # Son arrière plan ----------------
    pygame.mixer.music.load("Sons/background.wav")
    pygame.mixer.music.set_volume(0.02)
    pygame.mixer.music.fadeout(400)
    pygame.mixer.music.play()

    # Arrière plan --------------
    fond = pygame.image.load("Images/fond.png").convert()
    fond = pygame.transform.scale(fond, (W, H))
    fondX = 0
    fondX2 = fond.get_width()

    # Premier plan (sol) ----------
    sol = pygame.image.load("Images/sol.png").convert()
    sol = pygame.transform.scale(sol, (1280, 167))
    solX = 0
    solX2 = sol.get_width()

    # Personnage --------------
    droite_perso = [pygame.image.load('Images/R' + str(k) + '.png') for k in range(9)]
    gauche_perso = [pygame.image.load('Images/L' + str(k) + '.png') for k in range(9)]
    devant_perso = pygame.image.load('Images/standing.png')

    # Classe du personnage -----------------
    class personnage():
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.nombredepas = 0

    def screen():
        ecran.blit(fond, (fondX, 0))
        ecran.blit(fond, (fondX2, 0))
        ecran.blit(sol, (solX, 550))
        ecran.blit(sol, (solX2, 550))
        ecran.blit(Jean, (persojean.x, persojean.y))



    def defilement(ImagePerso):

        # Déplacement perso-------------
        ecran.blit(ImagePerso[perso.nombredepas // 3], (perso.x, perso.y))
        perso.nombredepas += 1

        if perso.nombredepas + 1 >= 27:
            perso.nombredepas = 0


    # Variable Jump
    jump = False
    jumpCount = 10

    # Boucle principale -----------------------------
    run = True

    # Personnage ---------------
    perso = personnage(600, 520)
    persojean = personnage(1400, 480)

    while run:
        keys = pygame.key.get_pressed()

        clock.tick(32)
        # Image afficher ----------------
        screen()

        # Bruit de pas -----------
        if (keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]):
            if joue == silencieux:
                sonpas.play(-1)
                joue = 1

            elif joue == 1:
                pygame.mixer.unpause()
        else:
            pygame.mixer.pause()

        # deplacement du pnj
        if keys[pygame.K_RIGHT]:
            persojean.x -= 2
        if keys[pygame.K_LEFT]:
            persojean.x += 2

        # JUMP
        if not (jump):
            if keys[pygame.K_SPACE]:
                jump = True
        else:
            if jumpCount >= -10:
                neg = 1
                if jumpCount < 0:
                    neg = -1
                perso.y -= (jumpCount ** 2) * 0.2 * neg
                jumpCount -= 1
            else:
                jump = False
                jumpCount = 10

        if keys[pygame.K_RIGHT]:
            defilement(droite_perso)

            fondX -= 1; fondX2 -= 1; solX -= 2; solX2 -= 2

            if fondX < fond.get_width() * -1:
                fondX = fond.get_width()
            if fondX2 < fond.get_width() * -1:
                fondX2 = fond.get_width()

            if solX < sol.get_width() * -1:
                solX = sol.get_width()
            if solX2 < sol.get_width() * -1:
                solX2 = sol.get_width()




        elif keys[pygame.K_LEFT]:
            defilement(gauche_perso)

            fondX += 1; fondX2 += 1; solX += 2; solX2 += 2

            if fondX > fond.get_width():
                fondX = fond.get_width() * -1
            if fondX2 > fond.get_width():
                fondX2 = fond.get_width() * -1

            if solX > sol.get_width():
                solX = sol.get_width() * -1
            if solX2 > sol.get_width():
                solX2 = sol.get_width() * -1


        else:
            ecran.blit(devant_perso, (perso.x, perso.y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.flip()

    pygame.quit()
    quit()

menu()
main()