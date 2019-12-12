# -*- coding: utf-8 -*-
"""
@author: Aurélien
"""


class Human():
    def __init__(self):
        """
        Constructeur où on définit l'humain
        """

    def choose_move(self, currentnode, consigne="Entrez votre choix : "):
        """
        Methode faire des choix en tant qu'humain
        """
        print("Etat du jeu : " + str(currentnode.game.current_state()))
        choix = int(input(consigne))
        print("\n")
        return choix

        print("Vous ne pouvez pas effectuer cette action")
        self.play_move(int(input("Donnez un nombre valide : ")),
                       self.players[0])
