# coding=utf-8

from random import *


class Joueur():
    """Classe Joueur

    Deux joueurs sont créés et positionnés aux extrémités du plateau de jeu.
    """

    # Liste des déplacements possibles
    # -4 : à gauche ou en haut (saute-mouton)
    # -3 : à gauche ou en haut (saute-mouton proche de la ligne d'arrivée)
    # -2 : à gauche ou en haut
    # -1 : en haut (pour atteindre la ligne d'arrivée)
    # 1 : en bas (pour atteindre la ligne d'arrivée)
    # 2 : à droite ou en bas
    # 3 : à droite ou en bas (saute-mouton proche de la ligne d'arrivée)
    # 4 : à droite ou en bas (saute-mouton)
    deplacements = [-4, -3, -2, -1, 1, 2, 3, 4]

    def __init__(self, name, pawn, finishline, phasenumber, y, x):
        """Constructeur de la classe Joueur

        Un joueur possède:
            - un nom permettant de le distinguer,
            - un pion permettant de suivre ses déplacements,
            - une ligne d'arrivee à franchir pour gagner,
            - une position x (colonne),
            - une position y (ligne),
            - un nombre de mur à poser.
        """

        self.nom = name
        self.pion = pawn
        self.arrivee = finishline
        self.posY = y
        self.posX = x
        self.nbMurs = 10

        # Compteur de phases
        self.numerophase = phasenumber

    def seDeplacer(self, choix, plateau):
        """Méthode seDeplacer

        Actualise la position du joueur en fonction :
            - de son choix,
            - des murs posés,
            - des limites du plateau.
        """

        # Efface l'ancienne position du joueur sur le plateau de jeu
        plateau.tabDeJeu[self.posY][self.posX] = 0

        # Cas d'un déplacement vers le haut
        if(choix == "haut"):

            # Pour atteindre la ligne d'arrivée (concerne le joueur 2)
            if(self.nom == plateau.players[1] and self.posY == 1):
                self.posY += self.deplacements[3]

            elif(self.posY != 1):
                # Cas général
                if(plateau.tabDeJeu[self.posY-1][self.posX] != 1):
                    if(plateau.tabDeJeu[self.posY-2][self.posX] == 0):
                        self.posY += self.deplacements[2]

                    # Cas où le joueur adverse se trouve sur la case choisie
                    else:
                        # Cas du saute-mouton proche de la ligne d'arrivée (concerne le joueur 2)
                        if(self.nom == plateau.players[1] and self.posY == 3):
                            self.posY += self.deplacements[1]

                        # Cas du saute-mouton de base
                        elif(plateau.tabDeJeu[self.posY-3][self.posX] != 1):
                            self.posY += self.deplacements[0]

        # Cas d'un déplacement vers le bas
        elif(choix == "bas"):

            # Pour atteindre la ligne d'arrivée (concerne le joueur 1)
            if(self.nom == plateau.players[0] and self.posY == plateau.ligne-2):
                self.posY += self.deplacements[4]

            elif(self.posY != plateau.ligne-2):
                # Cas général
                if(plateau.tabDeJeu[self.posY+1][self.posX] != 1):
                    if(plateau.tabDeJeu[self.posY+2][self.posX] == 0):
                        self.posY += self.deplacements[5]

                    # Cas où le joueur adverse se trouve sur la case choisie
                    else:
                        # Cas du saute-mouton proche de la ligne d'arrivée (concerne le joueur 1)
                        if(self.nom == plateau.players[0] and self.posY == plateau.ligne-4):
                            self.posY += self.deplacements[6]

                        # Cas du saute-mouton de base
                        elif(plateau.tabDeJeu[self.posY+3][self.posX] != 1):
                            self.posY += self.deplacements[7]

        # Cas d'un déplacement vers la gauche
        elif(choix == "gauche"):

            # Cas général
            if(self.posX != 0):
                if(plateau.tabDeJeu[self.posY][self.posX-1] != 1):
                    if(plateau.tabDeJeu[self.posY][self.posX-2] == 0):
                        self.posX += self.deplacements[2]

                    # Cas où le joueur adverse se trouve sur la case choisie
                    elif(self.posX != 2 and plateau.tabDeJeu[self.posY][self.posX-3] != 1):
                        self.posX += self.deplacements[0]

        # Cas d'un déplacement vers la droite
        elif(choix == "droite"):

            # Cas général
            if(self.posX != plateau.colonne-1):
                if(plateau.tabDeJeu[self.posY][self.posX+1] != 1):
                    if(plateau.tabDeJeu[self.posY][self.posX+2] == 0):
                        self.posX += self.deplacements[5]

                    # Cas où le joueur adverse se trouve sur la case choisie
                    elif(self.posX != plateau.colonne-3 and plateau.tabDeJeu[self.posY][self.posX+3] != 1):
                        self.posX += self.deplacements[7]

        # Ajoute la nouvelle position du joueur sur le plateau de jeu
        plateau.tabDeJeu[self.posY][self.posX] = self.pion

    def poserMur(self, murs, num, plateau):
        """Méthode poserMur

        Pose un mur sur la case dont le numéro est celui choisi.
        """

        murY = murs[num-1]['y']
        murX = murs[num-1]['x']
        #print("y : ", murY, " x : ", murX)

        if(plateau.tabDeJeu[murY][murX] == 'm'):

            # Si le joueur peut poser un mur verticalement et horizontalement
            if(plateau.tabDeJeu[murY+1][murX] == 'm' and plateau.tabDeJeu[murY][murX+1] == 'm'):

                # On choisit pour le joueur au hasard
                direction = randint(1, 2)

                # Verticalement
                if(direction == 1):
                    plateau.tabDeJeu[murY+1][murX] = 1

                # Horizontalement
                else:
                    plateau.tabDeJeu[murY][murX+1] = 1

            # Si le joueur peut poser un mur horizontalement
            elif(plateau.tabDeJeu[murY][murX+1] == 'm'):
                plateau.tabDeJeu[murY][murX+1] = 1

            # Si le joueur peut poser un mur verticalement
            elif(plateau.tabDeJeu[murY+1][murX] == 'm'):
                plateau.tabDeJeu[murY+1][murX] = 1

            # Si le joueur ne peut pas poser de mur ni horizontalement ni verticalement (à cause de la deuxième case)
            else:
                print("Vous ne pouvez pas poser de mur à cet endroit-là...")
                self.poserMur(murs, int(input(
                    "Veuillez indiquer un autre numéro pour la position du mur à poser : ")), plateau)

            # Lorsqu'au moins l'une des conditions ci-dessus est satisfaite
            plateau.tabDeJeu[murY][murX] = 1
            self.retraitMur()

        # Si le joueur ne peut pas poser de mur (à cause de la première case)
        else:
            print("Vous ne pouvez pas poser de mur à cet endroit-là...")
            self.poserMur(murs, int(input(
                "Veuillez indiquer un autre numéro pour la position du mur à poser : ")), plateau)

    def retraitMur(self):
        """Méthode retraitMur

        Décrémente le stock des murs à poser du joueur.
        """

        self.nbMurs -= 1
        print("Joueur ", self.pion, ", il vous reste ", self.nbMurs, " murs.")


############### Méthodes utilisées par la méthode valid_moves de la classe Plateau ###############


    def check_moves(self, choix, plateau):
        """Méthode check_moves

        Renvoie True si le déplacement choisi est possible et False sinon.
        """

        #print(plateau.ligne)
        #print(plateau.colonne)

        # Cas d'un déplacement vers le haut
        if(choix == "haut"):

            # Cas de la ligne d'arrivée pour le joueur 2
            if((self.nom == plateau.players[1] and self.posY == 1)
                    or
                ((self.posY != 1 and plateau.tabDeJeu[self.posY-1][self.posX] != 1)
                    and
                        # Cas général
                        (plateau.tabDeJeu[self.posY-2][self.posX] == 0
                            or

                        # Cas du saute-mouton proche de la ligne d'arrivée pour le joueur 2
                        (plateau.tabDeJeu[self.posY-2][self.posX] != 0 and (self.nom == plateau.players[1] and self.posY == 3))
                            or

                        # Cas du saute-mouton de base
                        (plateau.tabDeJeu[self.posY-2][self.posX] != 0 and plateau.tabDeJeu[self.posY-3][self.posX] != 1)))):

                return True

            else:
                return False

        # Cas d'un déplacement vers le bas
        elif(choix == "bas"):

            # Cas de la ligne d'arrivée pour le joueur 1
            if((self.nom == plateau.players[0] and self.posY == plateau.ligne-2)
                    or
                ((self.posY != plateau.ligne-2 and plateau.tabDeJeu[self.posY+1][self.posX] != 1)
                    and
                        # Cas général
                        (plateau.tabDeJeu[self.posY+2][self.posX] == 0
                            or

                        # Cas du saute-mouton proche de la ligne d'arrivée pour le joueur 1
                        (plateau.tabDeJeu[self.posY+2][self.posX] != 0 and (self.nom == plateau.players[0] and self.posY == plateau.ligne-4))
                            or

                        # Cas du saute-mouton de base
                        (plateau.tabDeJeu[self.posY+2][self.posX] != 0 and plateau.tabDeJeu[self.posY+3][self.posX] != 1)))):

                return True

            else:
                return False

        # Cas d'un déplacement vers la gauche
        elif(choix == "gauche"):
            if((self.posX != 0 and plateau.tabDeJeu[self.posY][self.posX-1] != 1)
                and
                    # Cas général
                    (plateau.tabDeJeu[self.posY][self.posX-2] == 0
                        or

                    # Cas où le joueur adverse se trouve sur la case choisie
                    (self.posX != 2 and plateau.tabDeJeu[self.posY][self.posX-3] != 1))):

                return True

            else:
                return False

        # Cas d'un déplacement vers la droite
        elif(choix == "droite"):
            if((self.posX != plateau.colonne-1 and plateau.tabDeJeu[self.posY][self.posX+1] != 1)
                and
                    # Cas général
                    (plateau.tabDeJeu[self.posY][self.posX+2] == 0
                        or

                    # Cas où le joueur adverse se trouve sur la case choisie
                    (self.posX != plateau.colonne-3 and plateau.tabDeJeu[self.posY][self.posX+3] != 1))):

                return True

            else:
                return False

        # Cas où le joueur entre une autre valeur que celles autorisées
        else:
            return False

    def check_laying_walls(self, murs, num, plateau):
        """Méthode check_laying_walls

        Renvoie True si le placement du mur est possible et False sinon.
        """

        murY = murs[num-1]['y']
        murX = murs[num-1]['x']

        if(plateau.tabDeJeu[murY][murX] == 'm'
            and
                # Verticalement et horizontalement
                ((plateau.tabDeJeu[murY+1][murX] == 'm' and plateau.tabDeJeu[murY][murX+1] == 'm')
                    or

                # Horizontalement
                plateau.tabDeJeu[murY][murX+1] == 'm'
                    or

                # Verticalement
                plateau.tabDeJeu[murY+1][murX] == 'm')):

            return True

        else:
            return False
