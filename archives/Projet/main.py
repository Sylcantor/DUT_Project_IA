
from Games.FrozenLake.Game import Game
from api.QLearning.QLearning import QLearning

# Choisissez un jeu
game = Game(4, 4, 0.1)
# Choisissez un type d'IA
q = QLearning(game, 16, 4)