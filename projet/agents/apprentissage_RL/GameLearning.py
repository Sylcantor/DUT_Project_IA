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

    def __init__(self, args, game, alpha=0.5, gamma=0.9, epsilon=0.1):

        if args.load:
            # load agent
            if args.agent_type == 'q':
                # QLearner
                try:
                    f = open('./qlearner_agent.pkl', 'rb')
                except IOError:
                    print("The agent file does not exist. Quitting.")
                    sys.exit(0)
            else:
                # SarsaLearner
                try:
                    f = open('./sarsa_agent.pkl', 'rb')
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
            # check if agent state file already exists, and ask user whether to overwrite if so
            if ((args.agent_type == "q" and os.path.isfile('./qlearner_agent.pkl')) or
                    (args.agent_type == "s" and os.path.isfile('./qlearner_agent.pkl'))):
                while True:
                    response = input("An agent state is already saved for this type. "
                                     "Are you sure you want to overwrite? [y/n]: ")
                    if response == 'y' or response == 'yes':
                        break
                    elif response == 'n' or response == 'no':
                        print("OK. Quitting.")
                        sys.exit(0)
                    else:
                        print("Invalid input. Please choose 'y' or 'n'.")
            if args.agent_type == "q":
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
