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

# 4 Mars, mise en place de la hitbox du perso, de la maison.
W, H = 1280, 598  # Définition de l'écran
silencieux = 0  # Son coupé



pygame.init()

    # Ecran définition
ecran = pygame.display.set_mode((W, H), pygame.DOUBLEBUF | pygame.HWSURFACE| pygame.FULLSCREEN)

    # Icone -------
icone = pygame.image.load("Images/icone.jpg").convert_alpha()
pygame.display.set_icon(icone)
    # Titre -------
pygame.display.set_caption("The Story of Gerald")

    # Time -------------
clock = pygame.time.Clock()

accueil = pygame.image.load("Accueil.png").convert_alpha()

ROUGE = (255,0,0)

# MENU DU JEU ------------------------

def fade():
    fade = pygame.Surface((W, H))
    fade.fill((0, 0, 0))
    for alpha in range(0, 300, 2):
        fade.set_alpha(alpha)
        ecran.blit(accueil, (0, -100))
        ecran.blit(fade, (0, 0))
        pygame.display.update()

def menu():
    run = True
    pygame.mixer.music.load("Sons/campfire.wav")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.fadeout(400)
    pygame.mixer.music.play()
    while run:
        ecran.blit(accueil, (0, -100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    fade()
                    run = False

        pygame.display.flip()
# -----------------------------------

# Classe du personnage -----------------
class personnage():
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.nombredepas = 0
            self.jumpCount = 8
            self.jump = False
            # Rect(left, top, width, height) -> Rect
            self.hitbox = (self.x + 17, self.y + 16, 53, 85)


        def mouvement(self,ImagePerso):
            self.ImagePerso = ImagePerso
            ecran.blit(ImagePerso[self.nombredepas // 3], (self.x, self.y))
            self.nombredepas += 1

            if self.nombredepas + 1 >= 45:
                self.nombredepas = 0

        def affichagehitbox(self, ecran):
            # Rect(left, top, width, height) -> Rect
            self.hitbox = (self.x + 17, self.y + 16, 53, 85)
            pygame.draw.rect(ecran, (255, 0, 0), self.hitbox, 2)
            # rect(surface, color, rect, width=0) -> Rect
            # if width == 0, (default) fill the rectangle
            # if width > 0, used for line thickness
            # if width < 0, nothing will be drawn
# Personnage ---------------

# Personnage dans la fôret
persomain = personnage(600, 430)
# Personnage dans la maison
persohouse = personnage(600,376)

# test villageois
persojean = personnage(400, 430)



# Intérieur de la maison
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
    fond = [pygame.image.load('Images/Fond/Fond' + str(k) + '.png').convert_alpha() for k in range(11)]
    X = [0 for k in range(11)]
    X2 = [928 for k in range(11)]
    X3 = [1856 for k in range(11)]

    # Personnage --------------
    droite_perso = [pygame.image.load('Images/droite' + str(k) + '.png').convert_alpha() for k in range(15)]
    gauche_perso = [pygame.image.load('Images/gauche' + str(k) + '.png').convert_alpha() for k in range(15)]
    devant_perso = pygame.image.load('Images/face0.png').convert_alpha()

    def screenmain():
        for k in range(11):
            ecran.blit(fond[k], (X[k],-203))
            ecran.blit(fond[k], (X2[k], -203))
            ecran.blit(fond[k], (X3[k], -203))


        # Affichage du perso'
        ecran.blit(Jean, (persojean.x, persojean.y))

        # Affichage de la hitbox du perso principal
        persomain.affichagehitbox(ecran)



    def house():
        house = True
        ou = pygame.image.load("maison.png")
        # Sons pas ----------------

        joue = silencieux


        while house:
            keys = pygame.key.get_pressed()


            ecran.fill([0,0,0])
            ecran.blit(ou, (240, 250))

            # persohouse.affichagehitbox(ecran) permettant d'afficher la hitbox du perso principal
            # bruit de pas intérieur à mettre

            if keys[pygame.K_RIGHT] and persohouse.x <=1020:
                persohouse.mouvement(droite_perso)
                persohouse.x += 1.5


            elif keys[pygame.K_LEFT]and persohouse.x >225:
                persohouse.mouvement(gauche_perso)
                persohouse.x -= 1.5


            else:
                ecran.blit(devant_perso, (persohouse.x, persohouse.y))
            clock.tick(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == pygame.K_ESCAPE):
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_RETURN and persohouse.x < 230:
                        house = False

            pygame.display.update()

    # Boucle principale -----------------------------
    run = True
    house()

    while run:
        keys = pygame.key.get_pressed()

        clock.tick(60)
        # Image affichage ----------------
        screenmain()

        # Bruit de pas -----------
        if (keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]):
            if joue == silencieux:
                sonpas.play(-1)
                joue = 1

            elif joue == 1:
                pygame.mixer.unpause()
        else:
            pygame.mixer.pause()


        # JUMP
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


        elif keys[pygame.K_q] and 300<persojean.x<600:
            house()
            pygame.display.flip()


        else:
            ecran.blit(devant_perso, (persomain.x, persomain.y))


        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == pygame.K_ESCAPE):
                run = False



        pygame.display.flip()

    pygame.quit()

    quit()


menu()

main()

