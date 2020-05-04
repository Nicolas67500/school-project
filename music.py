import pygame
from pygame.locals import *
import os
from random import*
import constants

def play_music(music):
    # ------------ Musique mauison ---------------- #
    # Musique
    pygame.mixer.music.load(music)
    # Volume
    pygame.mixer.music.set_volume(low_volume)
    # Fade de la musique
    pygame.mixer.music.fadeout(fadeout)
    # Lancement musique
    pygame.mixer.music.play()

# ----- Musique du jeu ----- #
house_music = "Sons/home.wav"
outside_music = "Sons/background.wav"

# ------ Réglage musique -------- #
# Eteint
off = 0
# Allumé
on = 1
# Volume
normal_volume = 0.4
low_volume = 0.2
# Réduction du volume avant l'arret
fadeout = 400

# ------------- Bruit de pas ------------ #

# Son des pas dans la maison
footstep_house = pygame.mixer.Sound("Sons/footstep_house.wav")


