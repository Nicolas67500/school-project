# ============== PROGRAMME PRINCIPAL ================= #

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

# MAJ :  4 Mars, mise en place de la hitbox du perso, de la maison par Nicolas le 13.03
# MAJ : Commentaire du code, ajout du module musique et constants, ajout de la musique et des bruits de pas selon la situation par Nicolas le 19.03

# ========= Initialization of Pygame ========== #
pygame.init()

# ---- Display mode ----- #
ecran = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT),
                                pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.FULLSCREEN)
# ----- Icone ------- #
icone = pygame.image.load("Images/icone.jpg").convert_alpha()
pygame.display.set_icon(icone)
# ----- Title ------- #
pygame.display.set_caption("The Story of Gerald")

# ========== MENU DU JEU ============= #

# ---- Background of the menu ----- #
accueil = pygame.image.load("Accueil.png").convert_alpha()


# -- Function Fade: Transition from the menu to the game with a black background -- #
def fade():
    fade = pygame.Surface((constants.WIDTH, constants.HEIGHT))
    fade.fill(constants.black)
    for alpha in range(0, 300, 2):
        fade.set_alpha(alpha)
        ecran.blit(accueil, (0, -100))
        ecran.blit(fade, (0, 0))
        pygame.display.update()


# ------------- Function Menu ------------- #
def menu():
    run = True
    # Sound of the campfire
    pygame.mixer.music.load("Sons/campfire.wav")
    # Set the volume
    pygame.mixer.music.set_volume(music.normal_volume)
    # Fade the music
    pygame.mixer.music.fadeout(music.fadeout)
    # Set on the music
    pygame.mixer.music.play()
    while run:
        # Display the image of the menu
        ecran.blit(accueil, (0, -100))
        for event in pygame.event.get():
            # If we press the button "ESCAPE", it will closs the game.
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()
            # If we press the button "ENTER", it will activate the function "Fade" and will go into the house.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    fade()
                    run = False

        pygame.display.flip()


# ============= Class of the character =============== #
class personnage():
    def __init__(self, x, y):
        # x coordinates of the player
        self.x = x
        # y coordinates of the player
        self.y = y
        # Initializes the character movement images
        self.nombredepas = 0
        # CORENTIN -->>> commente le jump
        self.jumpCount = 8
        self.jump = False
        # that makes a rectangle allowing to realize the hitbox by "Rect(left, top, width, height) -> Rect"
        self.hitbox = (self.x + 17, self.y + 16, 53, 85)

    def mouvement(self, ImagePerso):
        self.ImagePerso = ImagePerso
        ecran.blit(ImagePerso[self.nombredepas // 3], (self.x, self.y))
        self.nombredepas += 1

        if self.nombredepas + 1 >= 45:
            self.nombredepas = 0

    def affichagehitbox(self, ecran):
        # Rect(left, top, width, height) -> Rect
        self.hitbox = (self.x + 17, self.y + 16, 53, 85)
        pygame.draw.rect(ecran, constants.red, self.hitbox, 2)
        # rect(surface, color, rect, width=0) -> Rect
        # if width == 0, (default) fill the rectangle
        # if width > 0, used for line thickness
        # if width < 0, nothing will be drawn


# ============ Character ============== #

# Personnage dans la fôret
persomain = personnage(600, 430)
# Personnage dans la maison
persohouse = personnage(600, 376)
# test villageois
persojean = personnage(400, 430)

# =========== Constants of the main ======= #
def main():

    # ---------- PNJ TEST -------------- #
    Jean = pygame.image.load("Images/under.png")
    Jean = pygame.transform.scale(Jean, (200, 120))


    # ----------- Background scroll -------------- #
    fond = [pygame.image.load('Images/Fond/Fond' + str(k) + '.png').convert_alpha() for k in range(11)]
    X = [0 for k in range(11)]
    X2 = [928 for k in range(11)]
    X3 = [1856 for k in range(11)]

    # ------------ Image of the principal character -------------- #
    droite_perso = [pygame.image.load('Images/droite' + str(k) + '.png').convert_alpha() for k in range(15)]
    gauche_perso = [pygame.image.load('Images/gauche' + str(k) + '.png').convert_alpha() for k in range(15)]
    devant_perso = pygame.image.load('Images/face0.png').convert_alpha()

    # == Function "screenmain" : Display the background, pnj and hitbox == #
    def screenmain():
        for k in range(11):
            ecran.blit(fond[k], (X[k], -203))
            ecran.blit(fond[k], (X2[k], -203))
            ecran.blit(fond[k], (X3[k], -203))

        # Affichage du perso'
        ecran.blit(Jean, (persojean.x, persojean.y))

        # Affichage de la hitbox du perso principal
        persomain.affichagehitbox(ecran)

# ===== function "house" ===== #
    def house():
        # Import the function "music_house" from music.py file =  load the music and play it
        music.play_music(music.house_music)
        # -------- Sound of the footsteps in the house ---------------- #
        footstep_house = pygame.mixer.Sound("Sons/footstep_house.wav")
        joue = music.off
        # -- Volume of the footsteps in the house -- #
        footstep_house.set_volume(music.normal_volume)

        house = True
        image_house = pygame.image.load("maison.png")

        while house:
            keys = pygame.key.get_pressed()

            # Black background
            ecran.fill(constants.black)
            # It will blit the image of the house
            ecran.blit(image_house, (240, 250))
            # Display the hitbox of the character
            persohouse.affichagehitbox(ecran)  # permettant d'afficher la hitbox du perso principal

            # Commentaire : bruit de pas intérieur à mettre

            if keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
                if joue == music.off:
                    footstep_house.play(-1)
                    joue = music.on
                elif joue == music.on:
                    pygame.mixer.unpause()
            else:
                pygame.mixer.pause()
            # If you press the "left" key, the character will go to the right
            if keys[pygame.K_RIGHT] and persohouse.x <= 1020:
                persohouse.mouvement(droite_perso)
                persohouse.x += constants.speed

            # If you press the "left" key, the character will go to the left
            elif keys[pygame.K_LEFT] and persohouse.x > 225:
                persohouse.mouvement(gauche_perso)
                persohouse.x -= constants.speed


            else:
                # If you are not moving, it will diplay the character image when he is stopped
                ecran.blit(devant_perso, (persohouse.x, persohouse.y))
            constants.clock.tick(constants.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    # If we press the button "ESCAPE", it will closs the game.
                    if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == pygame.K_ESCAPE):
                        pygame.quit()
                        quit()
                    # If you press the "ENTER" key under x = 230, you go outside.
                    if event.key == pygame.K_RETURN and persohouse.x < 230:
                        # Stop the house music
                        footstep_house.stop()
                        pygame.mixer.music.stop()
                        house = False

            pygame.display.update()

# =============== Main loop ================== #

    run = True
    house()

    # ------------ Sound Music Outside ---------------- #
    music.play_music(music.outside_music)
    joue = music.off
    # -------- Sound of the footsteps outside ---------------- #
    footstep_outside = pygame.mixer.Sound("Sons/footstep_outside.wav")
    # -- Volume of the footsteps outside -- #
    footstep_outside.set_volume(music.normal_volume)

    while run:
        keys = pygame.key.get_pressed()

        # -- FPS of the game -- #
        constants.clock.tick(constants.FPS)

        # -------- call the screenmain function ---------------- #
        screenmain()

        # ------- Bruit de pas dans la fôret ----------- #
        if (keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]):
            if joue == music.off:
                footstep_outside.play(-1)
                joue = music.on
            elif joue == music.on:
                pygame.mixer.unpause()
        else:
            pygame.mixer.pause()


        # JUMP CORETIN A COMMENTER
        if not (persomain.jump):
            if keys[pygame.K_SPACE]:
                persomain.jump = True

        else:
            if persomain.jumpCount >= -8:
                neg = 1
                if persomain.jumpCount < 0:
                    neg = -1
                persomain.y -= (persomain.jumpCount ** 2) * 0.2 * neg
                persomain.jumpCount -= 0.5
            else:

                persomain.jump = False
                persomain.jumpCount = 8

        # When the character goes on the right
        if keys[pygame.K_RIGHT]:
            persomain.mouvement(droite_perso)
            persojean.x -= 2.5

            for k in range(11):
                X[k] -= k / 4
                X2[k] -= k / 4
                X3[k] -= k / 4

            for k in range(11):
                if X[k] < -928:
                    X[k] = 0
                if X2[k] < 0:
                    X2[k] = 928
                if X3[k] < 928:
                    X3[k] = 1856
        # When the character goes on the left
        elif keys[pygame.K_LEFT]:
            persomain.mouvement(gauche_perso)
            persojean.x += 2.5

            for k in range(11):
                X[k] += k / 4
                X2[k] += k / 4
                X3[k] += k / 4

            for k in range(11):

                if X[k] > 0:
                    X[k] = -928
                if X2[k] > 928:
                    X2[k] = 0
                if X3[k] > 1856:
                    X3[k] = 928

        # If you press the "Q" key between x = 300 and x = 600, you return to the house.
        elif keys[pygame.K_q] and 300 < persojean.x < 600:
            pygame.mixer.music.stop()
            footstep_outside.stop()
            house()
            pygame.display.flip()
        # If you are not moving, it will diplay the character image when he is stopped
        else:
            ecran.blit(devant_perso, (persomain.x, persomain.y))
        # If we press the button "ESCAPE", it will closs the game.
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == pygame.K_ESCAPE):
                run = False

        pygame.display.flip()

    pygame.quit()
    quit()


menu()
main()

