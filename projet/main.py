# -*- coding: utf-8 -*-
"""
@author: Aurélien
"""
import sys
import argparse

from copy import deepcopy

# les algorithmes:
from Algorithmes.Minimax.minimax import Minimax
from Algorithmes.Minimax.node import Node
# from Algorithmes.QLearning.qLearning import QLearning

# pour jouer en tant qu'utilisateur ou random:
from Algorithmes.human import Human
from Algorithmes.random import Random

# les jeux à importer:
from Jeux.Jeu_Nim import Nim
from Jeux.Jeu_TicTacToe import TicTacToe

# ────────────────────────────────────────────────────────────────────────────────
# utilities:


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
    draw = 0

    for numGame in range(numGames):

        i = 0

        game = deepcopy(inital_game)

        player = players[0]  # pour initialiser, le premier joueur est Joueur 1

        print("#_______#NEW_GAME#_______#")

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
        print("Le gagnant est : " + game.winner() + "\n")

        print("Affichage de fin : ")
        print(game.print_game())

        if game.winner() == players[0]:
            games_won_J1 += 1
        elif game.winner() == players[1]:
            games_won_J2 += 1
        else:
            draw += 1

    return games_won_J1, games_won_J2, draw


def PrintResults(resultsJ1, resultsJ2, draw, number_games):
    # les résultats en % des parties gagnées sur le nombre total de parties
    print("Win rate " + players[0] + " : " +
          str((resultsJ1/number_games)*100) + " %" +
          " | "+"Win rate " + players[1] + " : " +
          str((resultsJ2/number_games)*100) + " % "
          " | "+"Draw rate " + " : " +
          str((draw/number_games)*100) + " % ")


# ────────────────────────────────────────────────────────────────────────────────
# main:

if __name__ == "__main__":

    if len(sys.argv) == 1:  # sans argument: lancement normal

        """
        Mode d'emploi:
        1.  importer deux algorithmes ou un algorithme et la classe human
            tous contenant la méthode choose_move()
        2.  importer un jeu suivant la structure du jeu de nim ou le tic tac toe
        3.  dans TurnBased() y mettant en argument le jeu, le joueur n°1, le joueur n°2
            et le nombre de parties
        4.  vous pouvez récupérer les résultats des parties gagnées grâce à la méthode 
            PrintResults()
        """

        players = ['Player1', 'Player2']

        game = TicTacToe()
        #game = Nim(6)

        human = Human()
        random = Random()
        minimax = Minimax()

        # qlearning = QLearning(game, 6)
        # qlearning.training(minimax)

        number_games = 3

        resultsJ1, resultsJ2, draw = TurnBased(
            game, human, human, number_games, players)
        PrintResults(resultsJ1, resultsJ2, draw, number_games)

# ────────────────────────────────────────────────────────────────────────────────

    else:  # avec argument: lancement des options du reinforcement learning

        parser = argparse.ArgumentParser(
            description="Options du reinforcement learning.")
        parser.add_argument('-a', "--agent_type", type=str, default="q",
                            help="Specify the computer agent learning algorithm. "
                            "AGENT_TYPE='q' for Q-learning and ='s' for Sarsa-learning")
        parser.add_argument("-l", "--load", action="store_true",
                            help="whether to load trained agent")
        parser.add_argument("-t", "--teacher_episodes", default=None, type=int,
                            help="employ teacher agent who knows the optimal "
                            "strategy and will play for TEACHER_EPISODES games")
        parser.add_argument("-p", "--plot", action="store_true",
                            help="whether to plot reward vs. episode of stored agent "
                            "and quit")

        args = parser.parse_args()

        assert args.agent_type == 'q' or args.agent_type == 's', \
            "learner type must be either 'q' or 's'."

        if args.plot:
            assert args.load, "Must load an agent to plot reward."
            assert args.teacher_episodes is None, \
                "Cannot plot and teach concurrently; must chose one or the other."

        gl = GameLearning(args)
        if args.teacher_episodes is not None:
            gl.beginTeaching(args.teacher_episodes)
