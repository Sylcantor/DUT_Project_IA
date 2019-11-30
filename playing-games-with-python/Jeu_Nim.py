# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 22:51:50 2019

@author: Kevin
"""

from Minimax.game_tree import GameTree

players = ['Human', 'Bot']


class Nim():

    def __init__(self, nbAllumette, firstplayer):
        """
        Constructeur dans lequel on définit
        le nombre d'allumette
        """
        self.allumette = nbAllumette
        self.currentplayer = firstplayer

    def play_move(self, choice, currentplayer):
        """
        Methode qui enleve un certain nombre d'allumette
        """
        self.currentplayer = currentplayer
        if(self.allumette - choice < 0 or self.allumette == 0):
            print("Vous ne pouvez pas effectuer cette action")
            self.play_move(int(input("Donnez un nombre valide : ")))
        else:
            self.allumette -= choice

    def check_valide_move(self, choice):
        """
        Methode qui vérifie si le coup est valide (sans changer l'objet)
        """
        if(self.allumette - choice < 0 or self.allumette == 0):
            return False
        else:
            return True

    def check_current_state(self):
        """
        Methode qui vérifie s'il reste des allumettes
        """
        if(self.allumette != 0):
            return self.currentplayer, False
        else:
            return self.currentplayer, True

    def current_state(self):
        """
        Message qui donne le nombre d'allumette
        """
        return self.allumette

    def gameover(self):
        """
        Message de fin de jeu
        """
        return("Il n'y a plus d'allumette, victoire à " + str(self.check_current_state()[0]))


game = Nim(5, players[0])

gtree = GameTree(game)

# FIXME
nim_tree = gtree.create_tree(game, players[0])

i = 0

while((game.check_current_state()[1]) == False):

    if i == 0:
        player = players[0]
    else:
        player = players[1]

    print("___ " + player + " ___")

    print("Nombre restant d'allumettes " + str(game.current_state()))
    choix = int(input("Donner le nombre d'allumette : "))
    game.play_move(choix, player)
    print("\n")

    i ^= 1

print(game.gameover())
