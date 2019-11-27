
from numpy.lib.function_base import append


def create_tree(self, game, state, win_value, loss_value):
    """
    Méthode pour créer un arbre de jeu en fonction de l'état du jeu
    https://becominghuman.ai/practical-artificial-intelligence-for-game-development-5b0ebf35993b
    """

    # Nested List
    game_tree = ["Happy", [2, 0, 1, 5]]

    return game_tree


class GameState():

    def __init__(self, stateX, stateY):
        """
        Constructeur dans lequel on définit
        le nombre d'allumette
        """
        self.state = []

        for i in range(stateY):

            stateRow = []

            for j in range(stateX):

                stateRow.append(' ')

            self.state.append(stateRow)

        print(self.state)


GameState(3, 4)
