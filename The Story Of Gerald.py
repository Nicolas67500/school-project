# ============== PROGRAMME PRINCIPAL ================= #

# Import pygame module
import pygame
from pygame.locals import *
# Import local module
from fichier_class import *
from fichier_fonction import  *
from constants import *
from music import *
# Import python module
import os
import sys
import math


# MAJ :  4 Mars, mise en place de la hitbox du perso, de la maison par Nicolas le 13.03
# MAJ : Commentaire du code, ajout du module musique et constants, ajout de la musique et des bruits de pas selon la situation par Nicolas le 19.03
# MAJ : Simplification de la class perso (j'ai retiré l'argument "ImagePerso" de la fonction "perso_mouvement" et j'ai mis un booléen afin d'optimiser le code et son fonctionnement par Nicolas 27/03
# + J'ai créé la classe PNJ avec leur hitbox, permettant de faciliter l'affichage des bulles de dialogue.
# 04/04 Simplfication du code

# ========= Lancement de Pygame ========== #
pygame.init()
# ----- Icone ------- #
pygame.display.set_icon(icone)
# ----- Titre ----- #
pygame.display.set_caption("The Story of Gerald")


# =========== Fonction Principale ======= #
def main():
    # ----------- Défilement fond d'écran -------------- #
    # Fond d'écran
    fond = [pygame.image.load('Images/Fond/Fond' + str(k) + '.png').convert_alpha() for k in range(11)]
    # X première image
    X = [0 for k in range(11)]
    # X deuxième image
    X2 = [928 for k in range(11)]
    # X troisième image
    X3 = [1856 for k in range(11)]

    # == Fonction "screenmain" : Affiche tout ce qu'il y à a affiché dans la forêt == #
    def screenmain():
        # Boucle qui affiche les 11 images du fond d'écran
        for k in range(11):
            ecran.blit(fond[k], (X[k], -203))
            ecran.blit(fond[k], (X2[k], -203))
            ecran.blit(fond[k], (X3[k], -203))

        ecran.blit(persojean.pnj_image, (persojean.x, persojean.y))
        # Affichage de la hit.box du joueur
        persomain.perso_hitbox()
        persojean.pnj_hitbox()


    # ===== Fonction "house" ===== #
    def house():
        # Importation de la musique de la maison depuis "music.py"
        play_music(house_music)
        # Boucle des bruits de pas
        joue = off
        # Volume des pas dans la maison
        footstep_house.set_volume(normal_volume)
        # Boucle de la maison
        house = True

        while house:
            keys = pygame.key.get_pressed()
            # Remplissage de l'écran
            ecran.fill(black)
            # Affichage du fond d'écran
            ecran.blit(image_house, (240, 250))

            # Bruit de pas quand on se déplace
            if keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
                # Quand on appuie pour la première sur la touche de déplacement
                if joue == off:
                    # On lance les bruits de pas
                    footstep_house.play(-1)
                    # On allume la boucle des bruits de pas
                    joue = on
                # Si elle est deja allumé, on réactive les bruits de pas
                elif joue == on:
                    pygame.mixer.unpause()
            # Si on appuie plus sur une touche, on met les bruits de pas en pause
            else:
                pygame.mixer.pause()

            # Si on appuie sur la flèche de droite, le joueur va à droite
            if keys[pygame.K_RIGHT] and persohouse.x <= 1020:
                # Affichage des pas vers la droite
                persohouse.perso_mouvement(True)
                # Augmentation coordonnée X du joueur
                persohouse.x += speed

            # Si on appuie sur la flèche de gauche, le joueur va à gauche
            elif keys[pygame.K_LEFT] and persohouse.x > 225:
                # Affichage des pas vers la gauche
                persohouse.perso_mouvement(False)
                # Diminution coordonnée X du joueur
                persohouse.x -= speed


            else:
                # Si on appuie sur aucune flèche, on affiche l'image du joueur arreté
                ecran.blit(devant_perso, (persohouse.x, persohouse.y))
            clock.tick(FPS)
            if persohouse.x < 230:
                # Cela permet d'afficher les bulles de dialogue dans la maison
                msgmaison1.bulle_texte()
                msgmaison2.bulle_texte()

            for event in pygame.event.get():
                # Si on appuie sur "Echap", on quitte le jeu
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == pygame.K_ESCAPE):
                        pygame.quit()
                        quit()
                    # Si on appuie sur "Entrer" lorsque le joueur a sa coordonnée X en dessous de 230
                    if event.key == pygame.K_RETURN and persohouse.x < 230:
                        # Les bruits de pas s'arrête
                        footstep_house.stop()
                        # La musique s'arrête
                        pygame.mixer.stop()
                        # La boucle de la maison s'arrête
                        house = False

            pygame.display.update()

    # =============== Boucle principale ================== #

    run = True

    # Musique extérieure

    play_music(outside_music)
    joue = off

    # Bruit de pas extérieure
    footstep_outside = pygame.mixer.Sound("Sons/footstep_outside.wav")
    # Volume des pas
    footstep_outside.set_volume(normal_volume)

    # Appele de la fonction "house"
    house()

    while run:
        keys = pygame.key.get_pressed()

        # FPS du jeu
        clock.tick(FPS)

        # Appele de la fonction "screenmain"
        screenmain()

        if persojean.rect.colliderect(persomain.hitbox):
            # On affiche les bulles de dialogue dehors lorqu'il y a une interaction avec le PNJ
            msgdehors1.bulle_texte()

        # Bruit de pas dans la forêt
        if (keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]):
            if joue == off:
                footstep_outside.play(-1)
                joue = on
            elif joue == on:
                pygame.mixer.unpause()
        else:
            pygame.mixer.pause()

        # Saut : Si la boucle n'est pas activé
        if not (persomain.jump):
            # Si on appuie sur "Espace"
            if keys[pygame.K_SPACE]:
                # On active la boucle
                persomain.jump = True

        # Si elle est deja activé:
        else:
            # Tant que le compteur du saut est supérieur à -8
            if persomain.jumpCount >= -8:
                # Valeur qui définie si on monte ou on descend : ici on monte
                neg = 1
                # Si le compteur est inférieur à 0
                if persomain.jumpCount < 0:
                    # "neg" devient négatif
                    neg = -1
                # Chnagement de la coordonnée Y du joueur en fonction du compteur et de la valeur "neg"
                persomain.y -= (persomain.jumpCount ** 2) * 0.2 * neg
                # Réduction du compteur
                persomain.jumpCount -= 0.5
            # Si il est égale à -8: le saut est fini
            else:
                # On eteint la boucle de saut
                persomain.jump = False
                # On remet le compteur à 8
                persomain.jumpCount = 8

        # Le joueur va à droite
        if keys[pygame.K_RIGHT]:
            persomain.perso_mouvement(True)
            persojean.pnj_mouvement(True)

            # Boucle qui change la coordonnée X des 11 fonds à différente vitesse pour donner de la profondeur
            for k in range(11):
                X[k] -= k / 4
                X2[k] -= k / 4
                X3[k] -= k / 4
            # Boucle qui remet à ca place l'image quand elle c'est décalée de sa largeur
            for k in range(11):
                if X[k] < -928:
                    X[k] = 0
                if X2[k] < 0:
                    X2[k] = 928
                if X3[k] < 928:
                    X3[k] = 1856

        # Le joueur va à gauche
        elif keys[pygame.K_LEFT]:
            persomain.perso_mouvement(False)
            persojean.pnj_mouvement(False)

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

        # Quand on appuie sur "q" quand la coordonnée X du joueur est entre 300 et 600:
        elif keys[pygame.K_q] and 300 < persojean.x < 600:
            # Musique s'arrete
            pygame.mixer.stop()
            # Bruits de pas extérieurs s'arrete
            footstep_outside.stop()
            # Appele de la fonction "house" pour rentrer dans la maison
            house()
            pygame.display.flip()
        # Quand on ne se déplace pas, affichage du joueur de face
        else:
            ecran.blit(devant_perso, (persomain.x, persomain.y))
        # On quitte quand on appuie sur "echap"
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == pygame.K_ESCAPE):
                run = False

        pygame.display.flip()

    pygame.quit()
    quit()


menu()
main()

