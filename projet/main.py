# -*- coding: utf-8 -*-
"""
@author: Aurélien
"""
from copy import deepcopy

from human import Human

from Minimax.minimax import Minimax
from Minimax.node import Node

from QLearning.QLearning import QLearning

from Jeux.Jeu_Nim import Nim


def TurnBased(inital_game,
              player1,
              player2,
              numGames=1,
              players=['Player1', 'Player2']):
    """
    Fonction pour jouer à tour de role
    Joueur 1 est le premier joueur à jouer et Joueur 2 est le second
    """
    games_won_J1 = 0
    games_won_J2 = 0

    for numGame in range(numGames):

        i = 0

        game = deepcopy(inital_game)

        player = players[0]  # pour initialiser, le premier joueur est Joueur 1

        while ((game.check_current_state()) == False):

            if i == 0:
                player = players[0]  # human
                print("___ " + player + " ___")

                currentnode = Node(game, player)

                choix = player1.choose_move(currentnode)
                game.play_move(choix, player)
                print("\n")
            else:
                player = players[1]  # bot
                print("___ " + player + " ___")

                currentnode = Node(game, player)

                choix = player2.choose_move(currentnode)
                game.play_move(choix, player)
                print("\n")

            i ^= 1
        print("#________________________#")
        print("Le gagnant est : " + game.winner())
        print("#________________________#\n")

        if game.winner() == players[0]:
            games_won_J1 += 1
        else:
            games_won_J2 += 1

    return games_won_J1, games_won_J2


players = ['Player1', 'Player2']

game = Nim(6)

human = Human()
minimax = Minimax()

# qlearning = QLearning(game, minimax, 6)
# qlearning.training(minimax)

number_games = 5

resultsJ1, resultsJ2 = TurnBased(game, human, minimax, number_games, players)

print("Win rate " + players[0] + " : " + str((resultsJ1/number_games)*100) + " %" +
      " | "+"Win rate " + players[1] + " : " + str((resultsJ2/number_games)*100) + " % ")
