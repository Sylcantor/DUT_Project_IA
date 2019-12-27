"""
@author: Aurelien Castel
"""

import numpy as np

from Algorithmes.AbstractAlgo import AbstractAlgo

from random import randrange

# Agent which selects its actions at random


class Random(AbstractAlgo):

    def choose_move(self, node):
        """
        Methode pour faire des choix aléatoires
        """
        random_index = randrange(len(node.game.valid_moves()))
        print("Coup décidé : " + str(node.game.valid_moves()[random_index]))
        return node.game.valid_moves()[random_index]
