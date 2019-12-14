# -*- coding: utf-8 -*-
"""
@author: Aurélien
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
