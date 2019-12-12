# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 22:51:50 2019

@author: Kevin
"""


class Nim():
    def __init__(self, nbAllumette, players=['Player1', 'Player2'], firstplayer=None):
        """
        Constructeur où on définit le jeu
        """
        self.allumette = nbAllumette
        self.players = players
        self.currentplayer = firstplayer

    def play_move(self, choice, currentplayer):
        """
        Methode pour jouer au jeu
        """
        self.currentplayer = currentplayer
        if self.choice in self.valid_moves():   # vérification supplémentaire mais normalement c'est forcément vrai
                                                # si on choisit un move parmis les valid_moves()
            self.allumette -= choice            # si ok on change l'état du jeu

    def valid_moves(self):
        """
        Methode qui donne sous forme de liste tous les coups jouables actuellement
        """
        moves = [
        ]  # tous les coups jouables sous forme de liste de nombres

        # On numérote les coups où l'on peut jouer
        if self.allumette <= 3:                      # on peut choisir au maximum 3 alluemettes
            for i in range(self.minimal_move(),
                           self.current_state()):    # l'état actuel du jeu
                if (self.check_valid_move(i)):       # vérifie si ce move est valide
                    moves.append(i)
        else:
            for i in range(self.minimal_move(), 3):  # l'état actuel du jeu
                if (self.check_valid_move(i)):       # vérifie si ce move est valide
                    moves.append(i)

        print("Coups jouables : " + str(moves))

        return moves

    def check_valid_move(self, choice):
        """
        Methode qui vérifie si le coup est valide
        """
        if (self.allumette - choice < 0):  # or self.allumette == 0):
            return False
        else:
            return True

    def check_current_state(self):
        """
        Methode qui vérifie l'état du jeu (victoire/défaite/match nul)
        """
        if (self.allumette != 0):
            return self.currentplayer, False
        else:
            # return le joueur courant: donc le gagnant et un booléen True: la partie est finie
            return self.currentplayer, True

    def current_state(self):
        """
        Pour connaitre l'état du jeu actuel
        """
        return self.allumette

    def minimal_move(self):
        """
        Le coup minimal qu'on peut faire
        """
        return 1
