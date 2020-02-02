# -*- coding: utf-8 -*-
"""
@author: Aurélien
"""
import multiprocessing
import sys
import argparse

# fonctions utilitaires:
from utilities import TurnBased
from utilities import TurnBasedRL
from utilities import TurnBasedRLvsRL
from utilities import PrintResults
from utilities import TurnBasedRL_episodes
from utilities import TurnBasedRL_PrintResults
from utilities import SaveGL

from plot import manuel
from plot import plot_multiple_agents_reward

# ───────────────────────────────── imports agents

# algorithme d'optimisation:
from agents.optimisation_MinMax.minimax import Minimax
# algorithmes d'apprentissage:
from agents.apprentissage_RL.GameLearning import GameLearning

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
                        "AGENT_TYPE='q' for Q-learning and ='s' for Sarsa-learning"
                        "'b' both Sarsa and QLearning and compare them")
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

    assert args.agent_type == 'q' or args.agent_type == 's' or args.agent_type == 'b', \
        "learner type must be either 'q', 's' or 'b'."
    if args.plot:
        assert args.load, "Must load an agent to plot reward."
        assert args.teacher_episodes is None, \
            "Cannot plot and teach concurrently; must chose one or the other."

    # ───────────────────────────────── main

    """
    Mode d'emploi apprentissage:
    1.  importer un jeu (game) suivant la structure du jeu de nim ou le tic tac toe
        Avec sauvegarde (plus long):
            2.  lancer au terminal: python main.py -a q -t 10000 -s
                pour sauvegarder sous forme de fichier la matrice
            3.  lancer au terminal: python main.py -a q -l
                pour lancer le jeux depuis le fichier précédement créé
        Sans sauvegarde (pour faire un rapide test):
            2.  lancer au terminal: python main.py -a q -t 10000
    """  # ───────────────────────────── v changer ci-dessous le jeu (game) souhaité v

    game = TicTacToe()
    # game = Nim(6)

    # algorithmes/agents ou teachers
    human = Human()
    random = Random()
    minimax = Minimax()

    # the game learners
    glQ = GameLearning(args, 'q', game)
    glS = GameLearning(args, 's', game)

    # ───────────────────────────────── apprentissage
    manual_games = 3

    if not args.load and args.teacher_episodes is not None:  # si on ne load pas: on apprend
        if args.agent_type == "b":

            # Création des processus
            p1 = multiprocessing.Process(
                target=TurnBasedRL_episodes, args=(game, glQ, random, args.teacher_episodes,))
            p2 = multiprocessing.Process(
                target=TurnBasedRL_episodes, args=(game, glS, random, args.teacher_episodes,))

            # Lancement des processus
            p1.start()
            p2.start()

            # Attend que les processus se terminent
            p1.join()
            p2.join()

            # plot_multiple_agents_reward(glQ, glS)
            glQ.plot_agent_reward()
            glS.plot_agent_reward()
            TurnBasedRL_PrintResults(game, glQ, human, manual_games)
            TurnBasedRL_PrintResults(game, glS, human, manual_games)
        else:
            if args.agent_type == "q":
                TurnBasedRL_episodes(game, glQ, random, args.teacher_episodes)
                glQ.plot_agent_reward()
                TurnBasedRL_PrintResults(game, glQ, human, manual_games)
            elif args.agent_type == "s":
                TurnBasedRL_episodes(game, glS, random, args.teacher_episodes)
                glS.plot_agent_reward()
                TurnBasedRL_PrintResults(game, glS, human, manual_games)

    # ───────────────────────────────── partie tests à la main

    if len(sys.argv) == 1:  # manuel utilisateur
        manuel()
        TurnBased(game, human, random)

    # TODO régler bug quand on change nom ['Player1', 'Player2'] dans TurnBasedRL
    # TODO nettoyer le code
    # TODO nettoyer les \n dans l'affichage
    # TODO faire plus d'asserts
    # TODO The agent file does not exist. Quitting. class GameLearning(object):
    # TODO Commenter les fonctions

    if args.save:
            # check if agent state file already exists, and ask user whether to overwrite if so
        if args.agent_type == "b":
            SaveGL(glQ, game)
            SaveGL(glS, game)
        else:
            if args.agent_type == "q":
                SaveGL(glQ, game)
            elif args.agent_type == "s":
                SaveGL(glS, game)
