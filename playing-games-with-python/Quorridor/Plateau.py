# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 12:44:48 2019

@author: Kevin
"""
from Joueur import *

class Plateau():
    """
    Plateau de jeu representé par une liste de liste (equivalent d'un tableau a
    deux dimensions) de dimension 19x17
    """
    
    player = ['A','B'] #=> Joueur1, Joueur2
    tab = []   
    
    def __init__(self):
        self.ligne = 19
        self.colonne = 17
        self.j1 = Joueur(8, 1)
        self.j2 = Joueur(8, 17)
        
        """
        Ajout de liste pour obtenir un tableau a 2 dimensions
        """
        for i in range(self.ligne):
            self.tab.append([])
            
            """
            Remplissage du tableau :
                5 : zone d'arrivé pour le joueur B
                7 : zone d'arrive pour le joueur A
                0 : cellule vide (pour deplacement du joueur)
                3 : cellule pour la pose de mur
            Il y a un schema a l'appui pour plus de details
            """
            if(i == 0):
                for l in range(self.colonne):
                    self.tab[i].append(5)
                    
            elif(i == self.ligne - 1):
                for m in range(self.colonne):
                    self.tab[i].append(7)
            elif(i % 2 == 0):
                for n in range(self.colonne):
                    self.tab[i].append(3)
            else:
                for k in range(self.colonne):
                    if(k % 2 == 0):
                        self.tab[i].append(0)
                    else:
                        self.tab[i].append(3)
        
        """
        Ajout des joueurs sur le plateau au centre de chaque extrémité
        """
        self.tab[self.j1.y][self.j1.x] = self.player[0]
        self.tab[self.j2.y][self.j2.x] = self.player[1]
        
        
    """
    On vérifie si l'un des joueur a atteint une zone d'arrivé.
    Plus précisément, si la cellule du joueur A correspond à 7 ou la cellule
    du joueur B correspond à 5
    """
    def findejeu(self):
        if((self.j1.y == 0)
        or (self.j2.y == 18):
            return True
        else:
            return False
        
    """
    Affichage du plateau
    """   
    def affichejeu(self):     

        for i in range(self.ligne):
            for j in range(self.colonne):
                print(self.tab[i][j], end="")
            print("\n")
            
        
    def enleveJoueur(self,x ,y):
        self.tab[y][x] = 0

    def placeJoueur(self, x, y):
        self.tab[y][x]
            

        
        
p = Plateau()
p.affichejeu()
p.j1.deplacement(1)