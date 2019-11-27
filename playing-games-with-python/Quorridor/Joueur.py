# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 13:55:19 2019

@author: Kevin
"""

class Joueur():
    """
    Classe joueur qui permet au joueur de se déplacer à travers le plateau.
    """
    
    """
    Liste des mouvements possibles.
    """
    deplacement = [[0,-2], [0,2], [-2,0], [2,0]]
    
    
    def __init__(self, l, posx, posy):
        self.letter = l
        self.x = posx
        self.y = posy
        self.nbMur = 10
        
    
    def seDeplacer(self,choix):
        # déplacement vers le haut
        if(choix == 1):
            self.x += self.deplacement[0][0]
            self.y += self.deplacement[0][1]
        
        # déplacement vers le bas
        elif(choix == 2):
            self.x += self.deplacement[1][0]
            self.y += self.deplacement[1][1]
        
        # déplacement vers la gauche
        elif(choix == 3):
            self.x += self.deplacement[2][0]
            self.y += self.deplacement[2][1]
            
        # déplacement vers la droite
        elif(choix == 4):
            self.x += self.deplacement[3][0]
            self.y += self.deplacement[3][1]
        # on invite le joueur à réessayer
        else:
            self.seDeplacer(int(input("Veuillez donner une reponse valide ! ")))
        
