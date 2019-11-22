# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 22:51:50 2019

@author: Kevin
"""

class Nim():
    """
    Constructeur dans lequel on définit
    le nombre d'allumette
    """
    def __init__(self, nbAllumette):
        self.allumette = nbAllumette
        
    """
    Methode qui vérifie s'il reste des allumettes
    """
    def finDeJeu(self):
        if(self.allumette != 0):
            return False
        else:
            return True
    """
    Methode qui enleve un certain nombre d'allumette
    """
    def enleve(self, nbAllumette):
        if(self.allumette - nbAllumette < 0 or nbAllumette == 0):
            print("Vous ne pouvez pas effectuer cette action")
            self.enleve(int(input("Donnez un nombre valide :")))
        else:
            self.allumette -= nbAllumette
    """
    Message de fin de jeu
    """
    def gameover(self):
        return("Il n'y a plus d'allumette")
    
    """
    Message qui donne le nombre d'allumette
    """
    def reste(self):
        return("Il reste {0} allumettes".format(self.allumette))

j = Nim(5)
while(j.finDeJeu() == False):
    print(j.reste())
    choix = int(input("Donner le nombre d'allumette :"))
    j.enleve(choix)
    print("\n")
    
print(j.gameover())
    