# -*- coding: utf-8 -*-
"""
@author: Aurélien
"""
from Algorithmes.AbstractAlgo import AbstractAlgo


class Human(AbstractAlgo):
    def __init__(self):
        """
        Constructeur où on définit l'humain
        """

    def choose_move(self, node, consigne="Entrez votre choix : "):
        """
        Methode faire des choix en tant qu'humain
        """

        node.game.print_game()
        print("Coups jouables : " + str(node.game.valid_moves()))
        choix = None

        while choix not in node.game.valid_moves():
            choix = int(input(consigne))

        return choix
