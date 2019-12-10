# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 12:44:48 2019

@author: Kevin
"""
from Joueur import *

"""
TODO
- play_move qui prend un état, le joueur qui joue et le coup à jouer et qui renvoi l'état après ce coup
- check_current_state qui prend un état du jeu et qui renvoi le vainqueur et si le jeu est terminé/s'il y a une victoire
- check_playable qui prend une case en argument pour savoir si on peut jouer dessus (ex: savoir si la case est vide dans le tic tac toe) on s'est basé sur le tic tac toe
"""

class Plateau():
    """
    Plateau de jeu représenté par une liste de listes (équivalent 
    d'un tableau à deux dimensions) de dimension 19x17.
    """
    
    tab = []
    
    def __init__(self):
        """
        Attributs de la classe Plateau :
            - nombre de colonnes
            - nombre de lignes
            - Joueur 1
            - Joueur 2
        """
        self.ligne = 19
        self.colonne = 17
        self.j1 = Joueur('A', 8, 1)
        self.j2 = Joueur('B', 8, 17)
        

        #Ajout de la liste pour obtenir un tableau à 2 dimensions.

        for i in range(self.ligne):
            self.tab.append([])
            
            """
            Remplissage du tableau :
                5 : zone d'arrivée pour le joueur B
                7 : zone d'arrivée pour le joueur A
                0 : cellule vide (pour les déplacements du joueur)
                m : cellule pour la pose des murs

            PS : schéma à l'appui pour plus de details.
            """
            if(i == 0):
                for c in range(self.colonne):
                    self.tab[i].append(5)
                    
            elif(i == self.ligne - 1):
                for c in range(self.colonne):
                    self.tab[i].append(7)
            elif(i % 2 == 0):
                for c in range(self.colonne):
                    self.tab[i].append('m')
            else:
                for c in range(self.colonne):
                    if(c % 2 == 0):
                        self.tab[i].append(0)
                    else:
                        self.tab[i].append('m')
        

        #Ajout des joueurs au centre de chaque extrémité du plateau.

        self.tab[self.j1.y][self.j1.x] = self.j1.letter
        self.tab[self.j2.y][self.j2.x] = self.j2.letter
        
    
    def findejeu(self):
        """
        On vérifie si l'un des joueur a atteint une zone d'arrivée.
        Autrement dit, si le joueur A a atteint la ligne de 7 ou que
        le joueur B a atteint la ligne de 5.

        return : boolean
        """

        if((self.j1.y == 0) or (self.j2.y == 18)):
            return True
        else:
            return False


    def victoire(self, joueur):
        """
        On affiche le message de victoire.

        arguments : Joueur
        """

        print("\n-------------------------------------------------------------------------------")
        print("Joueur ", joueur.letter, ", vous avez gagné !")
        print("-------------------------------------------------------------------------------\n")
        
    
    def affichejeu(self):
        """
        Affichage du plateau avec numérotation des lignes et des
        colonnes.
        """

        print("\n      ", end=" ")
        for col in range(self.colonne):
            print(col, end="   ")
        
        print("\n       ------------------------------------------------------------------------\n")

        for i in range(self.ligne):
            for j in range(self.colonne):
                if(i < 10):
                    if(j == 0):
                        print("", i, end=" |   ")
                    
                    if(j < 10):
                        print(self.tab[i][j], end="   ")
                    elif(j > 9):
                        print(self.tab[i][j], end="    ")
                    
                elif(i > 9):
                    if(j == 0):
                        print(i, end=" |   ")
                    
                    if(j < 10):
                        print(self.tab[i][j], end="   ")
                    elif(j > 9):
                        print(self.tab[i][j], end="    ")
            
            if i != 18:
                print("\n   |")
            else:
                print("\n")
            
    
    def enleveJoueur(self, joueur):
        """
        Enlève le caractère du joueur de la cellule.

        arguments : Joueur
        """

        self.tab[joueur.y][joueur.x] = 0


    def placeJoueur(self, joueur):
        """
        Ajoute le caractère du joueur sur la cellule.

        arguments : Joueur
        """

        self.tab[joueur.y][joueur.x] = joueur.letter


    def limitesDep(self, joueur, choix):
        """
        Délimite les déplacements du joueur.

        arguments : Joueur, int
        """

        if((joueur.x == 0 and choix == 3) or (joueur.x == self.colonne - 1 and choix == 4)):
            return False
        else:
            return True
    

    def poserMur(self, joueur, murY, murX):
        """
        Pose du mur aux coordonnées choisies par le joueur.

        arguments : Joueur, int, int
        """

        if(self.tab[murY][murX] == 'm'):

            if(murY % 2 != 0 and murX % 2 != 0 and self.tab[murY+1][murX] == 'm'):
                self.tab[murY+1][murX] = 1
            elif(murY % 2 == 0 and murX % 2 == 0 and self.tab[murY][murX+1] == 'm'):
                self.tab[murY][murX+1] = 1
            elif(murY % 2 == 0 and murX % 2 != 0):
                direction = input("Le mur doit-il être posé horizontalement ou verticalement ? (h/v) ")

                if(direction == 'h' or direction == 'H'):
                    if(self.tab[murY][murX+1] == 'm'):
                        self.tab[murY][murX+1] = 1
                    else:
                        print("Vous ne pouvez pas poser de mur à cet endroit-là...")
                        coordonnees = input("Veuillez indiquer d'autres coordonnées : ").split(" ")

                        murYtmp = int(coordonnees[0])
                        murXtmp = int(coordonnees[1])

                        self.poserMur(joueur, murYtmp, murXtmp)
                elif(direction == 'v' or direction == 'V'):
                    if(self.tab[murY+1][murX] == 'm'):
                        self.tab[murY+1][murX] = 1
                    else:
                        print("Vous ne pouvez pas poser de mur à cet endroit-là...")
                        coordonnees = input("Veuillez indiquer d'autres coordonnées : ").split(" ")

                        murYtmp = int(coordonnees[0])
                        murXtmp = int(coordonnees[1])

                        self.poserMur(joueur, murYtmp, murXtmp)
                else:
                    print("Réponse invalide, nous vous prions de recommencer...")
                    self.tour(joueur)

            else:
                print("Vous ne pouvez pas poser de mur à cet endroit-là...")
                coordonnees = input("Veuillez indiquer d'autres coordonnées : ").split(" ")

                murYtmp = int(coordonnees[0])
                murXtmp = int(coordonnees[1])
                
                self.poserMur(joueur, murYtmp, murXtmp)
                
            self.tab[murY][murX] = 1
            joueur.retraitMur()

        else:
            print("Vous ne pouvez pas poser de mur à cet endroit-là...")
            coordonnees = input("Veuillez indiquer d'autres coordonnées : ").split(" ")

            murYtmp = int(coordonnees[0])
            murXtmp = int(coordonnees[1])

            self.poserMur(joueur, murYtmp, murXtmp)


    def tour(self, joueur):
        """
        Tour de jeu pour un joueur (se déplacer ou poser un mur).

        arguments : Joueur
        """

        print("\n-------------------------------------------------------------------------------")
        print("Joueur ", joueur.letter, ", à vous de jouer !")
        print("-------------------------------------------------------------------------------\n")

        # Choix du joueur.
        deplacerPion = input("Voulez-vous déplacer votre pion ? (o/n) ")

        # Si le joueur veut se déplacer.
        if(deplacerPion == 'o' or deplacerPion == 'O'):
            print("Déplacements : Haut (1), Bas (2), Gauche (3), Droite (4)")
            deplacement = int(input("Choisissez un déplacement parmi 1, 2, 3 ou 4 : "))

            if(self.limitesDep(joueur, deplacement) == True):
                self.enleveJoueur(joueur)
                joueur.seDeplacer(deplacement, self)
                self.placeJoueur(joueur)
            else:
                print("Vous êtes à l'extrémité du plateau ! Vous ne pouvez pas vous déplacer à cet endroit-là...")
                self.tour(joueur)

        elif(deplacerPion == 'n' or deplacerPion == "N"):
            coordonnees = input("Donnez les coordonnées du mur à poser (ligne puis colonne) séparées par un espace : ").split(" ")

            murY = int(coordonnees[0])
            murX = int(coordonnees[1])

            self.poserMur(joueur, murY, murX)

        # Dans le cas d'une réponse erronée.
        else:
            print("Réponse invalide, nous vous prions de recommencer...")
            self.tour(joueur)

    # fonction qui copie le plateau
    def copy_game_state(self):
        """
        Arguments : rien
        Retour : Copie du plateau a l'instant T
        """
        new_state = []

        for i in range(self.ligne):
            new_state.append([])

            for j in range(self.colonne):
                new_state[i].append(self.tab[i][j])

        return new_state        

"""
Main.
"""

p = Plateau()

count = 0

print(p.copy_game_state())

while(p.findejeu() == False):
    if(count % 2 == 0):
        p.affichejeu()
        p.tour(p.j1)
    else:
        p.tour(p.j2)

    count += 1

if(count % 2 == 0):
    p.victoire(p.j1)
else:
    p.victoire(p.j2)

