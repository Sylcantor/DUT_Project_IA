# q learning with table https://cdancette.fr/2017/08/18/reinforcement-learning-part1/
import numpy as np
from QLearning.QDiagram import QDiagram

from Minimax.minimax import Minimax
from Minimax.node import Node

from copy import deepcopy

import sys
import os


class QLearning:
    """
    A class used for the QLearning algorithm
    """

    def __init__(self, game, states_n, win_value=10, loss_value=-10, players=['Player1', 'Player2']):
        """
        Constructeur.
        On définit le nombre d’états, et d’actions pour chaque état.
        """
        self.game = deepcopy(game)

        self.states_n = states_n
        self.actions_n = len(game.valid_moves())

        self.win_value = win_value
        self.loss_value = loss_value
        self.players = players

    def training(self, trainer):
        """
        For training the QLearning
        """

        Q = np.zeros([self.states_n, self.actions_n])

        # Set learning parameters
        lr = .85                 # learning rate, c’est la vitesse d’apprentissage
        y = .99                  # détermine l’importance des récompenses futures
        num_episodes = 1000      # nombre de parties que l’on va faire
        cumul_reward_list = []
        actions_list = []
        states_list = []

        # ─────────────────────────────────────────────────────────────────
        # for jusqu'à la fin du nombre de parties que l’on va faire
        for i in range(num_episodes):

            actions = []

            copy_game = deepcopy(self.game)
            s = copy_game.get_current_state()  # reset self.game.reset()

            states = [s]
            cumul_reward = 0

            # pour initialiser, le premier joueur est Joueur 1
            player = self.players[0]

            while ((copy_game.check_current_state()) == False):

                if i == 0:
                    player = self.players[0]  # qlearning
                    print("___ " + player + " ___")

                    # on choisit une action aléatoire avec une certaine probabilité,
                    # qui décroit avec i : 1. / (i +1)
                    Q2 = Q[s, :] + \
                        np.random.randn(1, self.actions_n)*(1. / (i + 1))
                    a = np.argmax(Q2)

                    # on récupère le reward dans le jeu (pas besoins de matrice ici)
                    copy_game.play_move(a, player)
                    s1 = copy_game.get_current_state()

                    print("\n")
                else:
                    player = self.players[1]  # bot
                    print("___ " + player + " ___")

                    currentnode = Node(copy_game, player)
                    blockPrint()
                    choix = trainer.choose_move(currentnode)
                    copy_game.play_move(choix, player)
                    enablePrint()
                    print("\n")

                copy_game.print_game()  # affichage du jeu en temps réel

                i ^= 1

                print("#________________________#")
                print("Le gagnant est : " + copy_game.winner())
                print("#________________________#\n")

                reward = 0
                if copy_game.winner() == self.players[0]:
                    reward = self.win_value
                else:
                    reward = self.loss_value
                # ─────────────────────────────────────────────────────────────────

                # Fonction de mise à jour de la Q-table
                Q[s, a] = Q[s, a] + lr * \
                    (reward + y * np.max(Q[s1, :]) - Q[s, a])
                cumul_reward += reward
                # s = s1
                actions.append(a)
                states.append(s)

                states_list.append(states)
                actions_list.append(actions)
                cumul_reward_list.append(cumul_reward)

                print("Score over time: " +
                      str(sum(cumul_reward_list[-100:])/100.0))

        diag = QDiagram(cumul_reward_list)

    def choose_move(self):
        return 0


def blockPrint():
    # Disable
    sys.stdout = open(os.devnull, 'w')


def enablePrint():
    # Restore
    sys.stdout = sys.__stdout__
