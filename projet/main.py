# -*- coding: utf-8 -*-
"""
@author: Aurélien
"""
import sys
import os
import argparse

from copy import deepcopy

# fonctions utilitaires:
from utilities import TurnBased
from utilities import PrintResults

# ───────────────────────────────── imports agents

# algorithme d'optimisation:
from agents.optimisation_MinMax.minimax import Minimax
# algorithmes d'apprentissage:
from agents.apprentissage_RL.GameLearning import GameLearning
from agents.apprentissage_RL.utilities import TurnBasedRL

# pour jouer en tant qu'utilisateur ou random:
from agents.human import Human
from agents.random import Random

# ───────────────────────────────── imports jeux

# les jeux à importer:
from jeux.Jeu_Nim import Nim
from jeux.Jeu_TicTacToe import TicTacToe


# ──────────────────────────────────────────────────────────────────────────────── main
# lancement des jeux avec les algorithmes

if __name__ == "__main__":

    # ───────────────────────────────── arguments

    parser = argparse.ArgumentParser(
        description="Options du reinforcement learning.")
    parser.add_argument('-a', "--agent_type", type=str, default="q",
                        help="Specify the computer agent learning algorithm. "
                        "AGENT_TYPE='q' for Q-learning and ='s' for Sarsa-learning")
    parser.add_argument("-s", "--save", action="store_true",
                        help="whether to save trained agent")
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

    # ───────────────────────────────── main

    """
    (1) Mode d'emploi apprentissage:
    1.  importer un professeur: algorithme aléatoire par exemple
    2.  importer un jeu suivant la structure du jeu de nim ou le tic tac toe
    3.  dans TurnBasedRL() y mettant en argument le jeu, le professeur et l'agent
    4.  vous pouvez récupérer les résultats des récompenses grâce à la méthode
        plot_agent_reward() de la classe GameLearning en rapport avec l'objet
        GameLearning créé
    5.  lancer au terminal: python main.py -a q -t 100000 -s
        pour sauvegarder sous forme de fichier la matrice
    6.  lancer au terminal: python main.py -a q -l
        pour lancer le jeux depuis le fichier précédement créé
    7.  vous pouvez récupérer les résultats des parties gagnées grâce à la méthode
        PrintResults()     
    """  # ───────────────────────────── v changer ci-dessous v

    game = TicTacToe()
    # game = Nim(6)

    # algorithmes/agents ou teachers
    human = Human()
    random = Random()
    minimax = Minimax()

    # the game learner
    gl = GameLearning(args, game)

    games_played = 0

    # ───────────────────────────────── apprentissage

    if not args.load and args.teacher_episodes is not None:  # si on ne load pas: on apprend

        while games_played < args.teacher_episodes:

            sys.stdout = open(os.devnull, 'w')  # disable print out
            TurnBasedRL(game, gl, random)
            sys.stdout = sys.__stdout__  # restore print out

            # Monitor progress
            if games_played % 1000 == 0:
                print("Games played: %i" % games_played)

            games_played += 1

        gl.plot_agent_reward()

        if args.save:
            # check if agent state file already exists, and ask user whether to overwrite if so
            if os.path.isfile('./qlearner_agent_'+game.__class__.__name__+'.pkl'):
                while True:
                    response = input("An agent state is already saved for this type. "
                                     "Are you sure you want to overwrite? [y/n]: ")
                    if response == 'y' or response == 'yes':
                        gl.agent.save_agent(
                            './qlearner_agent_'+game.__class__.__name__+'.pkl')
                        break
                    elif response == 'n' or response == 'no':
                        print("OK. Quitting.")
                        break
                    else:
                        print("Invalid input. Please choose 'y' or 'n'.")
            else:
                gl.agent.save_agent(
                    './qlearner_agent_'+game.__class__.__name__+'.pkl')

    # ───────────────────────────────── lancement normal

    for i in range(3):  # pour tester manuellement des parties après l'entrainement
        TurnBasedRL(game, gl, human)

"""
    games_won_J1 = 0
    games_won_J2 = 0
    draw = 0

    players = ['Player1', 'Player2']

    number_games = 3
    games_played = 0

    while games_played < number_games:

        returned_winner = TurnBased(game, human, random, players)

        if returned_winner == players[0]:
            games_won_J1 += 1
        elif returned_winner == players[1]:
            games_won_J2 += 1
        else:
            draw += 1

        games_played += 1

    PrintResults(games_won_J1, games_won_J2, draw, number_games)
"""
