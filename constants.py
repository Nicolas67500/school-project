import pygame
from pygame.locals import *
import os
from random import*

# Ajout du fichier "constants" par Nicolas le 19.03
pygame.init()

# ===================== Constante ================================= #

# ----Colors------ #
white = ((255,255,255))
blue = ((0,0,255))
green = ((0,255,0))
red = ((255,0,0))
black = ((0,0,0))
orange = ((255,100,10))
yellow = ((255,255,0))
blue_green = ((0,255,170))
marroon = ((115,0,0))
pink = ((255,100,180))
purple = ((240,0,255))
gray = ((127,127,127))
magenta = ((255,0,230))
brown = ((100,40,0))

# ------ Fenetre ------- #
# Résolution écran
WIDTH, HEIGHT = 1280, 598
# ---- Format de l'ecran ----- #
ecran = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF | pygame.HWSURFACE)

# ------ Temps ------- #
clock = pygame.time.Clock()
FPS = 60

# ------ Jeu ------- #
# Vitesse joueur
speed = 2

# --------------------------------------------------------- Image ------------------------------------------------- #

# Icone du jeu
icone = pygame.image.load("Images/icone.jpg").convert_alpha()

# Fond d'écran de la maison
image_house = pygame.image.load("Images/maison.png")

# ---- Ecran d'accueil ----- #
accueil = pygame.image.load("Images/Accueil.png").convert_alpha()
# ------------ Image du joueur : Chargement dans des listes de toutes les images -------------- #
droite_perso = [pygame.image.load('Images/droite' + str(k) + '.png').convert_alpha() for k in range(15)]
gauche_perso = [pygame.image.load('Images/gauche' + str(k) + '.png').convert_alpha() for k in range(15)]
devant_perso = pygame.image.load('Images/face0.png').convert_alpha()

# ---------- PNJ TEST -------------- #
Jean = pygame.image.load("Images/under.png")
Jean = pygame.transform.scale(Jean, (200, 120))

