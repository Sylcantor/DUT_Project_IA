
from numpy.lib.function_base import append


def create_tree(self, game, state, win_value, loss_value):
    """
    Méthode pour créer un arbre de jeu en fonction de l'état du jeu
    https://becominghuman.ai/practical-artificial-intelligence-for-game-development-5b0ebf35993b
    """

    # Nested List
    game_tree = ["Happy", [2, 0, 1, 5]]

    return game_tree




class GameState:

    def __init__(self, stateX, stateY):
        """
        Constructeur dans lequel on définit
        le nombre d'allumette
        """
        self.state = []
        self.stateX = stateX
        self.stateY = stateY

        for i in range(stateY):

            stateRow = []

            for j in range(stateX):

                stateRow.append(' ')

            self.state.append(stateRow)

        print(self.state)

    def Equals(self, game_state):

        for i in range(stateY):

            for j in range(stateX):

                if self.state[i][j] != game_state[i][j]:
                    return False

        return True

    def getState(self):
        return self.state

    def Copy(self, game_state):

        copy_state = []

        for i in range(stateY):

            for j in range(stateX):

                copy_state.append(game_state[i][j])

        return copy_state


class StateNode:

    def __init__(self):
        GameState(3, 4)
        self.children = []  # une liste de StateNode
