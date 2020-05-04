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

# ============= Class du personnage principal =============== #
class personnage():

    def __init__(self, x, y, imagepersodroite, imagepersogauche):
        # Coordonnée X du joueur
        self.x = x
        # Coordonnée Y du joueur
        self.y = y
        # Nombre de pas qui va définir l'image du joueur à afficher
        self.nombredepas = 0
        # Compteur du saut qui permet de définir la  hauteur du personnage
        self.jumpCount = 8
        # Boucle du saut
        self.jump = False
        # Cela va charger les images du personnage quand il marche vers la droite
        self.imagepersodroite = imagepersodroite  # Question au professeur: est-ce mieux de mettre directement les images ici ?
        # Cela va charger les images du personnage quand il marche vers la gauche
        self.imagepersogauche = imagepersogauche
        self.hitbox = (self.x + 17, self.y + 16, 53, 85)

    # Fonction mouvement du personnage
    def perso_mouvement(self, Droite):
        # Image du joueur
        if Droite:
            # Affiche de l'image du joueur qui marche vers la droite
            constants.ecran.blit(self.imagepersodroite[self.nombredepas // 3], (self.x, self.y))
            # Augmentation du compteur de pas
            self.nombredepas += 1
            # Retour à 0 du compteur lorsque sa valeur est trop élevée
        else:
            # Affiche de l'image du joueur qui marche vers la gauche
            constants.ecran.blit(self.imagepersogauche[self.nombredepas // 3], (self.x, self.y))
            # Augmentation du compteur de pas
            self.nombredepas += 1
            # Retour à 0 du compteur lorsque sa valeur est trop élevée
        if self.nombredepas + 1 >= 45:
            self.nombredepas = 0

    # Fonction affichage de la hitbox
    def perso_hitbox(self):  # def perso_hitbox(self, ecran):
        # Rect(left, top, width, height) -> Rect
        self.hitbox = (self.x + 17, self.y + 16, 53, 85)
        pygame.draw.rect(constants.ecran, constants.red, self.hitbox, 2)

        # rect(surface, color, rect, width=0) -> Rect
        # Si width == 0, (defaut) le rectangle est rempli
        # Si width > 0, il n'y a que les contours du rectangle
        # Si width < 0, il n'y a pas de rectangle


# ============= Class des PNJ. =============== #
class PNJ():

    def __init__(self, x, y, pnj_image):
        # Coordonnée X du joueur
        self.x = x
        # Coordonnée Y du joueur
        self.y = y
        # Afficher le personnage
        self.pnj_image = pnj_image
        self.rect = pygame.Rect(self.pnj_image.get_rect(topleft=(self.x, self.y)))

    # Fonction mouvement du personnage
    def pnj_mouvement(self, Droite):
        # Image du joueur
        if Droite:
            persojean.x -= 2.5
        else:
            persojean.x += 2.5

    # Fonction affichage de la hitbox
    def pnj_hitbox(self):  # def pnj_hitbox(self, ecran):
        # Rect(left, top, width, height) -> Rect
        self.rect = pygame.Rect(self.pnj_image.get_rect(topleft=(self.x, self.y)))
        pygame.draw.rect(constants.ecran, constants.red, self.rect, 2)

        # rect(surface, color, rect, width=0) -> Rect
        # Si width == 0, (defaut) le rectangle est rempli
        # Si width > 0, il n'y a que les contours du rectangle
        # Si width < 0, il n'y a pas de rectangle


# ============ Personnages ============== #

# Personnage dans la fôret
persomain = personnage(600, 430, constants.droite_perso, constants.gauche_perso)
# Personnage dans la maison
persohouse = personnage(600, 376, constants.droite_perso, constants.gauche_perso)
# test villageois
persojean = PNJ(400, 430, constants.Jean)



# ============= Class du Texte permettant d'afficher des bulles de dialogue =============== #

class Texte():
    def __init__(self, x, y, texte):
        # Coordonnée X du texte
        self.x = x
        # Coordonnée Y du texte
        self.y = y
        # Input du texte
        self.texte = texte
        # Police du texte
        self.font = pygame.font.Font("Ecriture/pixel2.otf", 15)
        # Ecrit le texte sur une surface
        self.text = self.font.render(self.texte, True, constants.black)
        # Rectangle de la taille de la surface du texte
        self.textRect = self.text.get_rect(topleft=(self.x + 20, self.y + 3))

    def bulle_texte(self):
        # Largeur de la bulle
        self.largeur = self.textRect[2] + 20
        # Hauteur de la bulle
        self.hauteur = self.textRect[3] - 10
        # Boucle permettant de tracer la bulle en utilisant un range de 2 pour changer les coordonnées d'un rectangle et le retracer
        for k in range(2):
            # Ensemble des rectangle à tracer pour faire le contour bulle
            pygame.draw.rect(constants.ecran, constants.black, (self.x + (self.largeur + 12) * k, self.y + 8, 4, self.hauteur), 0)
            pygame.draw.rect(constants.ecran, constants.black, (self.x + 8, self.y + (self.hauteur + 12) * k, self.largeur, 4), 0)
            pygame.draw.rect(constants.ecran, constants.black, (self.x + 4 + self.largeur + 4, self.y + 4 + (self.hauteur + 4) * k, 4, 4), 0)
            pygame.draw.rect(constants.ecran, constants.black, (self.x + 4, self.y + 4 + (self.hauteur + 4) * k, 4, 4), 0)
        # Intérieur de la bulle
        pygame.draw.rect(constants.ecran, constants.white, (self.x + 4, self.y + 8, self.largeur + 8, self.hauteur), 0)
        pygame.draw.rect(constants.ecran, constants.white, (self.x + 8, self.y + 4, self.largeur, self.hauteur + 8), 0)
        # Permet d'afficher le texte dans la bulle
        self.affichage_bulle = constants.ecran.blit(self.text ,(self.x + 16 , self.y + 2))



# On appelle des bulles de dialogue dans la maison.
msgmaison1 = Texte(200,210, "Veux-tu sortir?")
msgmaison2 = Texte(200,240, "Si oui, appuie sur la touche entrée")
# On appelle des bulles de dialogue dehors.
msgdehors1 = Texte(persojean.x - 100, persojean.y - 70, "Bonjour à toi jeune homme !")