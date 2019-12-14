"""
@author: Aurelien Castel
"""

import numpy as np

from Algorithmes.AbstractAlgo import AbstractAlgo

# Agent which selects its actions at random


class Random(AbstractAlgo):

    def choose_move(self, node):
        rand = np.random.choice(node.game.valid_moves())
        print("Coup décidé : " + str(rand))
        return rand
