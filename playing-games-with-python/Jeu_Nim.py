# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 22:51:50 2019

@author: Kevin
"""

from Minimax.game_tree import GameTree
from Minimax.minimax import Minimax

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
        if (self.check_valid_move(choice)) and (choice not in self.invalid_moves()):
            self.allumette -= choice
        else:
            print("Vous ne pouvez pas effectuer cette action")
            self.play_move(int(input("Donnez un nombre valide : ")), player[0])

    def check_valid_move(self, choice):
        """
        Methode qui vérifie si le coup est valide
        """
        if(self.allumette - choice < 0 or self.allumette == 0):
            return False
        else:
            return True

    def minimal_move(self):
        return 1

    def invalid_moves(self):
        """
        Methode qui renvoie les coups impossibles
        """
        invalid = []
        invalid.append(0)
        if(self.allumette > 1):  # s'il reste une allumette alors on peut jouer le coup de 1
            invalid.append(self.allumette)

        print("invalid moves" + str(invalid))
        return invalid

    def check_current_state(self):
        """
        Methode qui vérifie s'il reste des allumettes
        """
        if(self.allumette != 0):
            return self.currentplayer, False
        else:
            # return le joueur courant: donc le gagnant et un booléen True: la partie est finie
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


game = Nim(6, players[0])

gtree = GameTree(game)

nim_tree = gtree.create_tree(game, players[0])  # le premier joueur est humain

minimax = Minimax(nim_tree)

i = 0

player = players[0]

while((game.check_current_state()[1]) == False):

    if i == 0:
        player = players[0]  # human
        print("___ " + player + " ___")

        print("Nombre restant d'allumettes " + str(game.current_state()))
        choix = int(input("Donner le nombre d'allumette : "))
        game.play_move(choix, player)
        print("\n")
    else:
        player = players[1]  # bot
        print("___ " + player + " ___")

        nim_tree = gtree.create_tree(game, players[1])
        choix = minimax.choose_move(nim_tree)
        game.play_move(choix, player)
        print("\n")

    i ^= 1


print(game.gameover())
