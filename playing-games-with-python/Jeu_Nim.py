# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 22:51:50 2019

@author: Kevin
"""


class Nim():

    def __init__(self, nbAllumette):
        """
        Constructeur dans lequel on définit
        le nombre d'allumette
        """
        self.allumette = nbAllumette

    def finDeJeu(self):
        """
        Methode qui vérifie s'il reste des allumettes
        """
        if(self.allumette != 0):
            return False
        else:
            return True

    def enleve(self, nbAllumette):
        """
        Methode qui enleve un certain nombre d'allumette
        """
        if(self.allumette - nbAllumette < 0 or nbAllumette == 0):
            print("Vous ne pouvez pas effectuer cette action")
            self.enleve(int(input("Donnez un nombre valide :")))
        else:
            self.allumette -= nbAllumette

    def gameover(self):
        """
        Message de fin de jeu
        """
        return("Il n'y a plus d'allumette")

    def reste(self):
        """
        Message qui donne le nombre d'allumette
        """
        return("Il reste {0} allumettes".format(self.allumette))


j = Nim(5)
while(j.finDeJeu() == False):
    print(j.reste())
    choix = int(input("Donner le nombre d'allumette :"))
    j.enleve(choix)
    print("\n")

print(j.gameover())
