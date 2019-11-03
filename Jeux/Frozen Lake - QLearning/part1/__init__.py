# q learning with table https://cdancette.fr/2017/08/18/reinforcement-learning-part1/
import numpy as np

import Game
from Game import Game

import QLearning
from QLearning import QLearning


# 0.1 chance to go left or right instead of asked direction
game = Game(4, 4, 0.1)
# On définit le nombre d’états (16), et d’actions pour chaque état (4)
q = QLearning(game, 16, 4)
