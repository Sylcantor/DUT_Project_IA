# q learning with table https://cdancette.fr/2017/08/18/reinforcement-learning-part1/
import numpy as np
from QLearning.QDiagram import QDiagram


class QLearning:
    """
    A class used for the QLearning algorithm
    """

    def __init__(self, game):
        # On définit le nombre d’états, et d’actions pour chaque état
        self.game = game
        self.states_n = game
        self.actions_n = len(game.valid_moves())
        self.generate_QLearning()

    def generate_QLearning(self):
        """
        For generating the QLearning 
        """

        Q = np.zeros([self.states_n, self.actions_n])

        # Set learning parameters
        lr = .85                 # learning rate, c’est la vitesse d’apprentissage
        y = .99                  # détermine l’importance des récompenses futures
        num_episodes = 1000      # nombre de parties que l’on va faire
        cumul_reward_list = []
        actions_list = []
        states_list = []

        # for jusqu'à la fin du nombre de parties que l’on va faire
        for i in range(num_episodes):

            actions = []
            s = self.game.reset()
            states = [s]
            cumul_reward = 0
            d = False
            while True:

                # on choisit une action aléatoire avec une certaine probabilité,
                # qui décroit avec i : 1. / (i +1)
                Q2 = Q[s, :] + \
                    np.random.randn(1, self.actions_n)*(1. / (i + 1))
                a = np.argmax(Q2)

                # on récupère le reward dans le jeu (pas besoins de matrice ici)
                s1, reward, d, _ = self.game.move(a)

                # Fonction de mise à jour de la Q-table
                Q[s, a] = Q[s, a] + lr * \
                    (reward + y * np.max(Q[s1, :]) - Q[s, a])
                cumul_reward += reward
                s = s1
                actions.append(a)
                states.append(s)

                if d == True:
                    break

                self.game.print()  # affichage du jeu en temps réel

            print("Affichage fin:")
            self.game.print()  # affichage du jeu à la fin d'une partie

            states_list.append(states)
            actions_list.append(actions)
            cumul_reward_list.append(cumul_reward)

            print("Score over time: " +
                  str(sum(cumul_reward_list[-100:])/100.0))

        self.game.reset()

        diag = QDiagram(cumul_reward_list)

        def choose_move(self):
            diag = QDiagram(cumul_reward_list)
