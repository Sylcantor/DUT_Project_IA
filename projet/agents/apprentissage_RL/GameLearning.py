import os
import pickle
import sys
import numpy as np
import matplotlib.pylab as plt

from agents.apprentissage_RL.agent import Qlearner, SARSAlearner

from agents.AbstractAgent import AbstractAgent
# les noeuds:
from agents.node import Node


class GameLearning(object):
    """
    A class that holds the state of the learning process. Learning
    agents are created/loaded here, and a count is kept of the
    games that have been played.
    """

    def __init__(self, args, agent_type, game, alpha=0.5, gamma=0.9, epsilon=0.1):

        if args.load:
            # load agent
            if agent_type == 'q':
                # QLearner
                try:
                    f = open('./qlearner_agent_' +
                             game.__class__.__name__+'.pkl', 'rb')
                except IOError:
                    print("The agent file does not exist. Quitting.")
                    sys.exit(0)
            elif agent_type == 's':
                # SarsaLearner
                try:
                    f = open('./sarsa_agent_' +
                             game.__class__.__name__+'.pkl', 'rb')
                except IOError:
                    print("The agent file does not exist. Quitting.")
                    sys.exit(0)
            self.agent = pickle.load(f)
            f.close()
            # If plotting, show plot and quit
            if args.plot:
                self.plot_agent_reward()
                sys.exit(0)
        else:
            if agent_type == "q":
                self.agent = Qlearner(game.valid_moves(),
                                      alpha, gamma, epsilon)
            else:
                self.agent = SARSAlearner(game.valid_moves(),
                                          alpha, gamma, epsilon)

    def plot_agent_reward(self):
        """ Function to plot agent's accumulated reward vs. iteration """
        plt.plot(np.cumsum(self.agent.rewards))
        plt.title('Agent Cumulative Reward vs. Iteration')
        plt.ylabel('Reward')
        plt.xlabel('Episode')
        plt.show()
