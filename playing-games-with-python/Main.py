# -*- coding: utf-8 -*-
"""
@author: Aurélien
"""

from Minimax.minimax import Minimax
from Minimax.minimax import Node

from Joueur.Human.human import Human

from Jeu_Nim import Nim


def TurnBased(game, player1, player2, numGames=1, players=['Human', 'Bot']):
    """
    Joueur 1 est le premier joueur à jouer et Joueur 2 est le second
    """

    for numGame in range(numGames):

        i = 0

        player = players[0]  # pour initialiser, le premier joueur est Joueur 1

        while ((game.check_current_state()[1]) == False):

            if i == 0:
                player = players[0]  # human
                print("___ " + player + " ___")

                print("Etat du jeu : " + str(game.current_state()))
                choix = player1.choose_move()
                game.play_move(choix, player)
                print("\n")
            else:
                player = players[1]  # bot
                print("___ " + player + " ___")

                print("Etat du jeu : " + str(game.current_state()))
                currentnode = Node(game, players[1])

                choix = player2.choose_move(currentnode)
                game.play_move(choix, player)
                print("\n")

            i ^= 1

        print(game.gameover())


game = Nim(6)

human = Human()

minimax = Minimax()

TurnBased(game, human, minimax, 10)
