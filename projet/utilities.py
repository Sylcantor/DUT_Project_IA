# -*- coding: utf-8 -*-
"""
@author: Aurélien
"""
from copy import deepcopy

# les noeuds:
from agents.node import Node


def TurnBased(inital_game,  # ne fait qu'une seule partie
              player1,
              player2,
              players=['Player1', 'Player2']):
    """
    Fonction pour jouer à tour de role.
    Joueur 1 est le premier joueur à jouer et Joueur 2 est le second.
    """

    game = deepcopy(inital_game)

    i = 0  # pour initialiser, le premier joueur est Joueur 1

    print("#_______#NEW_GAME#_______#\n")

    while (game.check_current_state()) == False:

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
    print("Le gagnant est : " + game.winner() + "\n")

    print("Affichage de fin : ")
    print(game.print_game())

    return game.winner()


def PrintResults(resultsJ1, resultsJ2, draw, number_games, players=['Player1', 'Player2']):
    # les résultats en % des parties gagnées sur le nombre total de parties
    print("Win rate " + players[0] + " : " +
          str((resultsJ1/number_games)*100) + " %" +
          " | "+"Win rate " + players[1] + " : " +
          str((resultsJ2/number_games)*100) + " % "
          " | "+"Draw rate " + " : " +
          str((draw/number_games)*100) + " % ")
