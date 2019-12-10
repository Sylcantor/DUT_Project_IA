##########################
######   MINI-MAX   ######
##########################

from copy import deepcopy

# https://tonypoer.io/2016/10/28/implementing-minimax-and-alpha-beta-pruning-using-python/
# -*- coding: utf-8 -*-
"""
@author: Aurelien
"""


class Node:
    """
    Class qui caractérise un noeud qui a:
    game, player, move=None, leaf_value=None
    leaf_value est à none au début pour les noeuds. On fait remonter
    le leaf_value des feuilles vers le haut de l'arbre dans l'algorithme Minimax.
    """

    def __init__(self, game, player, move=None, leaf_value=None):
        self.game = game
        self.player = player
        self.move = move
        self.value = leaf_value

    def __repr__(self):
        """
        Pour récupérer un noeud, si on fait Node(...) on récupère tout ça:
        """
        return str((object.__repr__(self), self.game, self.player, self.move,
                    self.value))[1:-1]

    # return str((object.__repr__(self), self.name, self.my_id, self.parent, self.children))[1:-1]
    # return str((object.__repr__(self), self.name, self.my_id, self.parent))[1:-1]


class Minimax:
    """
    Minimax sans besoin de game tree sous forme de liste à fournir (plus optimisé)
    """

    def __init__(self, win_value=10, loss_value=-10, players=['Human', 'Bot']):
        """
        Constructeur.
        """
        self.win_value = win_value
        self.loss_value = loss_value
        self.players = players
        return

    # ────────────────────────────────────────────────────────────────────────────────

    def choose_move(self, node):
        """
        Méthode principale à appeler, on demande un noeud de l'arbre.
        """

        print("~~~ Start MiniMax ~~~")
        """
          p     : 0 (max) (current) (with no move to choose from because this is a root)
         / \          v
        s   s   : 1 (min) (with no moves to choose from because they are node/leaf)
            on prend donc le max des min... et ainsi de suite.
        """

        # successeurs en dessous à du jeu actuel n + 1
        successors_states = self.getSuccessors(node)

        print(" the current children: " + str(successors_states))

        infinity = float('inf')
        # on part de - l'infini pour trouver quelque chose de meilleur à chaque fois
        max_value = -infinity

        for state in successors_states:  # start of MinMax here
            """
            On fait donc une succession de max, min, max, min... Car dans min_value() on demandera max_value().
            Il n'y a pas de récursivité car on part de max_value() puis on demande min_value() puis max_value() et ainsi de suite.
            On fait remonter les valeurs avec isTerminal(), getUtility(). Les noeuds ne return pas de valeur.
            Le programme fonctionne de façon naturelle : voir Plminmax.gif, MinMax.png.
            """
            max_value = max(max_value, self.min_value(state))
            print(" MAX: max_value: " + str(max_value))
            state.value = max_value  # ---> propagate values up tree

        # second, find the node which HAS that max value
        #  --> means we need to propagate the values back up the
        #      tree as part of our minimax algorithm
        print(" MiniMax:  Utility Value of Root Node: = " + str(max_value))

        # find the node with our best move
        best_move = None

        for state in successors_states:
            """
            On cherche parmis nos élements lequel est celui avec la valeur max de max_value et on fait un break puis on la return
            """
            print(" successors at n + 1 from the actual game : " + str(state))

            if state.value == max_value:
                best_move = state
                break

        # return that best value that we've found
        print(" == > MiniMax: Choosen move " + str(best_move))
        print("~~~~ End MiniMax ~~~~")
        return best_move.move

    # ────────────────────────────────────────────────────────────────────────────────

    def max_value(self, node):
        print("MiniMax --> MAX: Visited Node (move choice) :: " +
              str(node.move))
        if self.isTerminal(node):  # si c'est une feuille
            return self.getUtility(node)

        infinity = float('inf')
        # on part de - l'infini pour trouver quelque chose de meilleur à chaque fois
        max_value = -infinity

        # successeurs en dessous à n + 1
        successors_states = self.getSuccessors(node)
        """
          p     : 0 (max) (current)
         / \          v
        s   s   : 1 (min)
            on prend donc le max
        """
        for state in successors_states:
            max_value = max(max_value, self.min_value(state))
            print(" MAX: max_value: " + str(max_value))

        print(" choosen max: " + str(max_value))
        node.value = max_value
        print(" print node pour remonter les values max: " + str(node) +
              " le move décidé: " + str(node.move))
        return max_value

    def min_value(self, node):
        print("MiniMax --> MIN: Visited Node (move choice) :: " +
              str(node.move))
        if self.isTerminal(node):
            return self.getUtility(node)

        infinity = float('inf')
        # on part de + l'infini pour trouver quelque chose de pire à chaque fois
        min_value = infinity

        # successeurs en dessous à n + 1
        successor_states = self.getSuccessors(node)
        """
          p     : 0 (min) (current)
         / \          v
        s   s   : 1 (max)
            on prend donc le min
        """
        for state in successor_states:
            min_value = min(min_value, self.max_value(state))
            print(" MIN: min_value: " + str(min_value))

        print(" choosen min: " + str(min_value))
        node.value = min_value
        print(" print node pour remonter les values min: " + str(node) +
              " le move décidé: " + str(node.move))
        return min_value

    #                     #
    #   UTILITY METHODS   #
    #                     #

    # successor states in a game tree are the child nodes...
    def getSuccessors(self, node):  # les enfants d'en dessous à n + 1
        """
        avoir les successeurs
        """
        assert node is not None

        game = node.game  # current game
        player = node.player  # current player

        new_nodes = []  # the next nodes at n + 1

        empty_cells = [
        ]  # l'ensemble des cases vides : tous les coups jouables en général

        # On numérote les coups où l'on peut jouer (pas vides)
        for i in range(game.minimal_move(),
                       game.current_state() + 1):  # l'état actuel du jeu
            if game.check_valid_move(i) == True:
                empty_cells.append(i)
        print("empty_cells " + str(empty_cells))

        # Jeux imaginaires : tous les coups de jeu possibles selon le jeu que l'on a donné dans node
        for empty_cell in [
                x for x in empty_cells if x not in game.invalid_moves()
        ]:

            print("empty_cell " + str(empty_cell))

            copy_game = deepcopy(game)  # on copie le jeu
            # on fait le coup sur cette copie de jeu
            copy_game.play_move(empty_cell, player)

            # Si c'est à l'IA de jouer.    players = ['Human', 'Bot']
            if player == self.players[1]:  # == O
                # make more depth tree for human
                constructingnode = Node(copy_game, self.players[0], empty_cell)
                # au tours de human à jouer
                print("constructed node : " + str(constructingnode))

            # Si c'est à l'humain de jouer.
            if player == self.players[0]:  # == X
                # make more depth tree for AI
                constructingnode = Node(copy_game, self.players[1], empty_cell)
                # au tours de bot à jouer
                print("constructed node : " + str(constructingnode))

            new_nodes.append(constructingnode)

        return new_nodes

    # return true if the node has NO children (successor states)
    # return false if the node has children (successor states)

    def isTerminal(self, node):
        """
        si c'est une feuille
        """
        assert node is not None
        winner_loser, done = node.game.check_current_state()
        return done == True or done == "Draw"

    def getUtility(self, node):
        """
        lorsqu'on veut return la valeur pour une feuille
        """
        assert node is not None

        # Si c'est une feuille: on return la valeur de victoire ou défaite

        game = node.game  # current game

        leaf_value = self.create_leaf_value(game)

        print("leaf : " + str(leaf_value))

        return leaf_value

    def create_leaf_value(self, game):
        """
        Return the value of a leaf
        """

        # Si c'est des feuilles: on return la valeur de victoires ou défaite
        winner_loser, done = game.check_current_state()
        """
        players = ['X', 'O']
        # X = Human
        # O = Bot

        # Si le jeu est fini et que l'IA a gagné.
        if done == "Done" and winner_loser == 'O':
            return 1
        # Si le jeu est fini et que l'IA a perdu.
        elif done == "Done" and winner_loser == 'X':
            return -1
        # Si le jeu est fini et que personne n'a gagné.
        elif done == "Draw":
            return 0
        """

        # Si le jeu est fini et que l'IA a gagné.
        if done == True and winner_loser == self.players[1]:  # IA O
            return self.win_value
        # Si le jeu est fini et que l'IA a perdu.
        elif done == True and winner_loser == self.players[0]:  # Humain X
            return self.loss_value
        # Si le jeu est fini et que personne n'a gagné.
        elif done == "Draw":
            return 0
