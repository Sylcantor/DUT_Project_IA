# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 13:55:19 2019

@author: Kevin
"""

class Joueur():
    
    # Classe joueur qui permet au joueur de se déplacer à travers le plateau.

    
    #liste des déplacements possibles
    deplacement = [[0,-2], [0,2], [-2,0], [2,0]]
    
    #constructeur
    def __init__(self, l, posx, posy):
        """
        Attributs :
            position x
            position y
            caractère
            nombre de mur en possession
        """
        self.letter = l
        self.x = posx
        self.y = posy
        self.nbMur = 10
        
    # Actualise la position du joueur en fonction du choix
    def seDeplacer(self,choix):
        """
        Arguments : choix
        return : rien (void)
        """
        # déplacement vers le haut (1)
        if(choix == 1):
            self.x += self.deplacement[0][0]
            self.y += self.deplacement[0][1]
        
        # déplacement vers le bas (2)
        elif(choix == 2):
            self.x += self.deplacement[1][0]
            self.y += self.deplacement[1][1]
        
        # déplacement vers la gauche (3)
        elif(choix == 3):
            self.x += self.deplacement[2][0]
            self.y += self.deplacement[2][1]
            
        # déplacement vers la droite (4)
        elif(choix == 4):
            self.x += self.deplacement[3][0]
            self.y += self.deplacement[3][1]

        # on invite le joueur à réessayer
        else:
            self.seDeplacer(int(input("Veuillez donner une reponse valide ! ")))
        
