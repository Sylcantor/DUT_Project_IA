# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 22:51:50 2019

@author: Kevin
"""

from Minimax.game_tree import GameTree


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


players = ['Human', 'Bot']

nimObj = Nim(5)

gt = GameTree(5, nimObj.enleve, nimObj.reste, nimObj.finDeJeu)

i = 0

while(nimObj.finDeJeu() == False):

    if i == 0:
        player = players[0]
    else:
        player = players[1]

    print(nimObj.reste())
    choix = int(input("Donner le nombre d'allumette :"))
    nimObj.enleve(choix)
    print("\n")

    i ^= 1

print(nimObj.gameover())
