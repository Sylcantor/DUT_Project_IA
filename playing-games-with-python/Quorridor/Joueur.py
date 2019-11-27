# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 13:55:19 2019

@author: Kevin
"""

class Joueur():
    """
    Classe joueur qui permet au joueur de se déplacer a travers le plateau
    """
    
    """
    Liste des mouvement possibles
    """
    deplacement = [[0,-2], [0,2], [-2,0], [2,0]]
    
    
    def __init__(self, posx, posy):
        self.x = posx
        self.y = posy
        self.nbMur = 10
        
    
    def seDeplacer(self,choix):
        #deplacement vers le haut
        if(choix == 1):
            self.x += self.deplacement[0][0]
            self.y += self.deplacement[0][1]
        
        #deplacement vers le bas
        elif(choix == 2):
            self.x += self.deplacement[1][0]
            self.y += self.deplacement[1][1]
        
        #deplacement vers la gauche
        elif(choix == 3):
            self.x += self.deplacement[2][0]
            self.y += self.deplacement[2][1]
            
        #deplacement vers la droite
        elif(choix == 4):
            self.x += self.deplacement[3][0]
            self.y += self.deplacement[3][1]
        #on invite le joueur a réessayer
        else:
            self.seDeplacer(int(input("Veuillez donner une reponse valide !")))
            
        
    #def poserMur(x,y):