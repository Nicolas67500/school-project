import pygame
import os
from random import*
import constants

def play_music(music):
    # ------------ Sound Music of the House ---------------- #
    # Sound of the music
    pygame.mixer.music.load(music)
    # Set the volume
    pygame.mixer.music.set_volume(low_volume)
    # Fade the music
    pygame.mixer.music.fadeout(fadeout)
    # Set on the music
    pygame.mixer.music.play()

# / Music of the Game /
house_music = "Sons/home.wav"
outside_music = "Sons/background.wav"

# ------ Music settings-------- #
# / Stop the music /
off = 0
# / Start the music /
on = 1
# / Volume of the music /
normal_volume = 0.4
low_volume = 0.2
# / Fade out the volume on all sounds before stopping /
fadeout = 400


