# -*- coding: utf-8 -*-
"""
@author: Aurélien
"""
import multiprocessing
import sys
import argparse

# fonctions utilitaires: sont toutes dans utilities.py
from utilities import TurnBased_episodes
from utilities import TurnBased_PrintResults
from utilities import SaveGL

# plotting: pour créer des graphiques mathplotlib sont toutes dans plot.py
from plot import manual
from plot import plot_multiple_agents_reward

# ───────────────────────────────── imports agents

# algorithme d'optimisation:
from agents.optimisation_MinMax.minimax import Minimax
# algorithmes d'apprentissage:
from agents.apprentissage_RL.agent import Qlearner
from agents.apprentissage_RL.agent import SARSAlearner

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
        description="Reinforcement learning options.")
    parser.add_argument("-s", "--save",
                        help="whether to save all trained agents")
    parser.add_argument("-l", "--load", nargs="+",
                        help="whether to load one or multiple trained agents"
                        "enter your files *.pkl after -l each separated by"
                        "one space")
    parser.add_argument("-t", "--teacher_episodes", default=None, type=int,
                        help="employ teacher agent who knows the optimal "
                        "strategy and will play for TEACHER_EPISODES games")
    parser.add_argument("-p", "--plot",
                        help="whether to plot reward vs. episode of stored agent")

    args = parser.parse_args()

    if args.plot:
        assert args.load, "Must load an agent to plot reward."
        assert args.teacher_episodes is None, \
            "Cannot plot and teach concurrently; must chose one or the other."

    # ───────────────────────────────── main

    # v changer ci-dessous le jeu (game) souhaité v
    game = TicTacToe()
    # game = Nim(6)

    # algorithmes/agents ou teachers
    # on peut rajouter autant qu'on veut d'agents ou teachers ici:
    human = Human()
    random = Random()
    minimax = Minimax()

    # the game learners : ne pas toucher la partie load
    learners = []  # <-- tous contenus ici
    if args.load:
        for i in args.load:
            loaded_agent = LoadGL(i)
            if args.plot:  # If plotting, show plot
                loaded_agent.plot_agent_reward()
            learners.append(loaded_agent)

    # sinon on peut rajouter autant qu'on veut de learners ici:
    glQ = Qlearner(game.valid_moves())
    learners.append(glQ)
    glS = SARSAlearner(game.valid_moves())
    learners.append(glS)

    manual_games = 3  # nombre de jeux tests à la main après l'entrainement

    # ───────────────────────────────── apprentissage

    if args.teacher_episodes is not None:  # on apprend puis tests à la main
        TurnBased_episodes(game, args.teacher_episodes, glS, random)
        glS.plot_agent_reward()
        TurnBased_PrintResults(game, manual_games, glS, human)

    # ───────────────────────────────── manuel utilisateur

    if len(sys.argv) == 1:
        manuel()
        TurnBased_PrintResults(game, manual_games, human, random)
        exit(0)

    # ───────────────────────────────── partie save

    if args.save:
        for i in learners:
            SaveGL(i)

    # TODO nettoyer le code
    # TODO nettoyer les \n dans l'affichage
    # TODO faire plus d'asserts
    # TODO réparer # plot_multiple_agents_reward(glQ, glS)
    # TODO faire fonctionner QLearning plot
    # TODO faire fonctionner MinMax
    # TODO documenter + manuel
    # TODO tester jeu nim
    # TODO faire nouveau jeu
