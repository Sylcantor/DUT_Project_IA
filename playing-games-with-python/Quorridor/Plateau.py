# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 12:44:48 2019

@author: Kevin
"""
from Joueur import *

class Plateau():
    """
    Plateau de jeu représenté par une liste de listes (équivalent 
    d'un tableau à deux dimensions) de dimension 19x17.
    """
    
    tab = []
    
    def __init__(self):
        self.ligne = 19
        self.colonne = 17
        self.j1 = Joueur('A', 8, 1)
        self.j2 = Joueur('B', 8, 17)
        
        """
        Ajout de la liste pour obtenir un tableau à 2 dimensions.
        """
        for i in range(self.ligne):
            self.tab.append([])
            
            """
            Remplissage du tableau :
                5 : zone d'arrivée pour le joueur B
                7 : zone d'arrivée pour le joueur A
                0 : cellule vide (pour déplacement du joueur)
                3 : cellule pour la pose de murs

            Il y a un schéma à l'appui pour plus de details.
            """
            if(i == 0):
                for c in range(self.colonne):
                    self.tab[i].append(5)
                    
            elif(i == self.ligne - 1):
                for c in range(self.colonne):
                    self.tab[i].append(7)
            elif(i % 2 == 0):
                for c in range(self.colonne):
                    self.tab[i].append(3)
            else:
                for c in range(self.colonne):
                    if(c % 2 == 0):
                        self.tab[i].append(0)
                    else:
                        self.tab[i].append(3)
        
        """
        Ajout des joueurs sur le plateau au centre de chaque extrémité.
        """
        self.tab[self.j1.y][self.j1.x] = self.j1.letter
        self.tab[self.j2.y][self.j2.x] = self.j1.letter
        
        
    """
    On vérifie si l'un des joueur a atteint une zone d'arrivée.
    Plus précisément, si la cellule du joueur A correspond à 7 ou la cellule
    du joueur B correspond à 5.
    """
    def findejeu(self):
        if((self.j1.y == 0) or (self.j2.y == 18)):
            return True
        else:
            return False
        
    """
    Affichage du plateau.
    """   
    def affichejeu(self):     

        for i in range(self.ligne):
            for j in range(self.colonne):
                print(self.tab[i][j], end="")
            print("\n")
            
        
    def enleveJoueur(self, joueur):
        self.tab[joueur.y][joueur.x] = 0

    def placeJoueur(self, joueur):
        self.tab[joueur.y][joueur.x] = joueur.letter
    
    def tour(self, joueur):
        print("\n-----------------------------------------------------")
        print("Joueur ", joueur.letter, ", à vous de jouer !")
        print("-----------------------------------------------------\n")

        deplacerPion = input("Voulez-vous déplacer votre pion ? (o/n) ")

        if(deplacerPion == 'o' or deplacerPion == 'O'):
            print("Déplacements : Haut (1), Bas (2), Gauche (3), Droite (4)")
            deplacement = int(input("Choisissez un déplacement parmi 1, 2, 3 ou 4 : "))

            self.enleveJoueur(joueur)
            joueur.seDeplacer(deplacement)
            self.placeJoueur(joueur)

        elif(deplacerPion == 'n' or deplacerPion == "N"):
            poserMur = input("Voulez-vous poser un mur ? (o/n) ")

            if(poserMur == 'o' or poserMur == 'O'):
                print("Méthode \"poser un mur\" non implémentée...")
            elif(poserMur == 'n' or poserMur == "N"):
                print("Vous êtes trop gentil...")
            else:
                print("Réponse invalide, nous vous prions de recommencer...")
                self.tour(joueur)

        else:
            print("Réponse invalide, nous vous prions de recommencer...")
            self.tour(joueur)


p = Plateau()
p.affichejeu()

count = 0

while(p.findejeu() == False):
    if(count % 2 == 0):
        p.tour(p.j1)
    else:
        p.tour(p.j2)

    count += 1
    p.affichejeu()

