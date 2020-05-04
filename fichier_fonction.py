# Import pygame module
import pygame
from pygame.locals import *
# Import local module
import constants
import music
# Import python module
import os
import sys
import math


# ================== MENU ========================= #

# -- Fonction Fade : Transition du menu au jeu -- #
def fade():
    # On créer une surface
    fade = pygame.Surface((constants.WIDTH, constants.HEIGHT))
    # On la colorie en noir
    fade.fill(constants.black)
    # Cette boucle va changer l'opacité de notre surface
    for alpha in range(0, 300, 2):
        # Augmentation de l'opacité de la surface
        fade.set_alpha(alpha)
        # Affichage fond d'écran d'accueil
        constants.ecran.blit(constants.accueil, (0, -100))
        # Affichage surface
        constants.ecran.blit(fade, (0, 0))
        # Rafraichissement écran
        pygame.display.update()


# ------------- Fonction Menu ------------- #
def menu():
    run = True
    # Son feu de camp
    pygame.mixer.music.load("Sons/campfire.wav")
    # Volume
    pygame.mixer.music.set_volume(music.normal_volume)
    # Musique Fade
    pygame.mixer.music.fadeout(music.fadeout)
    # Jouer la musique
    pygame.mixer.music.play()
    while run:
        # Affichage fond d'écran menu
        constants.ecran.blit(constants.accueil, (0, -100))
        for event in pygame.event.get():
            # Si on appuye sur "Echap" on quitte le jeu.
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()
            # Si on appuye sur "Entrer" on quitte le menu et on entre dans la maison.
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Fonction fade pour la transition
                fade()
                # On arrête la boucle du menu
                run = False
        pygame.display.flip()