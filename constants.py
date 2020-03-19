import pygame
import os
from random import*

# Ajout du fichier "constants" par Nicolas le 19.03
pygame.init()

# ===================== Constans ================================= #

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

# ------ Windows ------- #
# / Screen resolution /
WIDTH, HEIGHT = 1280, 598


# ------ Time ------- #
clock = pygame.time.Clock()
FPS = 60

# ------ Game ------- #
# / Speed of the character /
speed = 2