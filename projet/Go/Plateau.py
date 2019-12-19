# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 01:15:48 2019

@author: Nicolas
"""

"""
TODO
- coupe qui verifie si il y a une coupe
- victoire qui compte les points de chaque joueur et qui renvoie le gagnant
"""

class Plateau():
    """
    Plateau de jeu représenté par une liste de listes (équivalent 
    d'un tableau à deux dimensions) de dimension 19x19.
    """
    
    tab = []
    
    def __init__(self):
        """
        Attributs de la classe Plateau :
            - nombre de colonnes
            - nombre de lignes
            - Joueur 1
            - Joueur 2
            - etat du jeu
        """
        self.ligne = 19
        self.colonne = 19
        self.j1 = 'A'
        self.j2 = 'B'
        self.fin = 0;

        # Ajout de la liste pour obtenir un tableau à 2 dimensions.

        for i in range(self.ligne):
            self.tab.append([0])

    def afficheJeu(self):
        """
        Affichage du plateau
        """

        print()
        
        print("\n       ------------------------------------------------------------------------\n")

        for i in range(self.ligne):
            for j in range(self.colonne):
                print(self.tab[i][j], end='')
            print()

    def verifChoix(self,ligne,colonne):
        """
        Délimite le placement de la pierre.

        Arguments : int, int
        """
        if(self.tab[ligne][colonne]==0):
            return True
        else:
            return False

    def placerPierre(self,ligne,colonne,joueur):
        """
        Ajoute le caractère du joueur sur la case.

        Arguments : int, int, String
        """
        self.tab[ligne][colonne]=joueur

    def finDeJeu(self):
        if fin==2:
            return True
        else:
            return False

    def coupe(self):
        #TODO verifier si il y a une coupe sur le plateau

    def victoire(self): #TODO

    def tour(self, joueur):
        """
        Tour de jeu pour un joueur (poser une pierre).

        Arguments : String
        """

        print("\n-------------------------------------------------------------------------------")
        print("Joueur ", joueur, ", à vous de jouer !")
        print("-------------------------------------------------------------------------------\n")

        # Choix du joueur.
        choix = input("Voulez vous jouer votre tour ? (o/n")
        while True:
            if(choix=='o'):
                self.fin=0

                placerPierre = input("Ou placez-vous votre pierre ? (ligne,colonne)")

                while lens(placePierre)<2:
                    placerPierre = input("Respecter la syntaxe (ligne,colonne)")

                ligne = placePierre[0]
                colonne = placePierre[3]

                while True:
                    if(self.verifChoix(ligne,colonne)):
                        self.placerPierre(ligne,colonne,joueur)
                        break
                    else:
                        placerPierre = input("Cette case est dejà occupé, ou placez-vous votre pierre ? (ligne,colonne)")

                self.coupe()

            else if choix != 'o' or choix != 'n' :
                input("Veuillez respecter la syntaxe (o/n)")
            else:
                self.fin+=1
                break
"""
Main.
"""

p = Plateau()

count = 0

#print(p.copy_game_state())

while p.finDeJeu() == False:
    if count % 2 == 0:
        p.afficheJeu()
        p.tour(p.j1)
        if p.finDeJeu():
            break 
    else:
        p.tour(p.j2)

    count += 1

p.victoire()
