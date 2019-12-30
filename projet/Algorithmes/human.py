# -*- coding: utf-8 -*-
"""
@author: Aurélien
"""
from Algorithmes.AbstractAlgo import AbstractAlgo


class Human(AbstractAlgo):

    def __init__(self):
        self.rules = True     # Booléen pour printer ou non les règles
        return

    def choose_move(self, node, consigne="Entrez votre choix : "):
        """
        Methode pour faire des choix en tant qu'humain
        """

        if self.rules:
            print(node.game.print_rules())
            self.rules = False

        print(node.game.print_game())
        print("[Aide] Choix disponibles :")
        # ───────────────────────────────────────────────────────────────── coups jouables
        i = 0
        j = 0
        while i < len(node.game.valid_moves()):
            print(i, ":", node.game.valid_moves()[i], end="")
            i += 1
            j += 1
            if j == 4:
                print("")
                j = 0
            elif i != len(node.game.valid_moves()):
                print(" | ", end="")
        print("")
        # ─────────────────────────────────────────────────────────────────
        print("[Aide] Choisissez selon l'index : de",
              0, "à", len(node.game.valid_moves())-1,)

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
