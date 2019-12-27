# -*- coding: utf-8 -*-
"""
@author: Aurélien
"""
from Algorithmes.AbstractAlgo import AbstractAlgo


class Human(AbstractAlgo):

    def choose_move(self, node, consigne="Entrez votre choix : "):
        """
        Methode pour faire des choix en tant qu'humain
        """

        node.game.print_game()
        print("Coups jouables : " + str(node.game.valid_moves()))
        print("[Help] Choisissez selon l'index : de ",
              0, "à", len(node.game.valid_moves())-1)
        choix = input(consigne)

        while True:

            if choix.isdigit():
                choix = int(choix)
                if 0 <= choix < len(node.game.valid_moves()):
                    return node.game.valid_moves()[choix]
                else:
                    choix = input(consigne)
            else:
                choix = input(consigne)
