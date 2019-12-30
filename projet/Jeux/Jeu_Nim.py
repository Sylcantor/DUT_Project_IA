# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 22:51:50 2019

@author: Kevin
"""

from Jeux.AbstractJeu import AbstractJeu


class Nim(AbstractJeu):
    def __init__(self, size, players=['Player1', 'Player2']):
        """
        Constructeur où on définit le jeu
        """
        self.allumette = size         # le plateau
        self.players = players        # liste des joueurs
        self.currentplayer = None     # caractérise le dernier joueur qui a joué
        return

    def play_move(self, choice, currentplayer):  # utilisé par minmax
        """
        Methode pour jouer au jeu
        """
        self.currentplayer = currentplayer
        if choice in self.valid_moves():        # vérification supplémentaire mais normalement c'est forcément vrai
                                                # si on choisit un move parmis les valid_moves()
            self.allumette -= choice            # si ok on change l'état du jeu

    def valid_moves(self):  # utilisé par minmax
        """
        Methode qui donne sous forme de liste tous les coups jouables possibles
        """
        moves = [
        ]  # tous les coups jouables sous forme de liste de nombres

        # On numérote les coups où l'on peut jouer
        if self.allumette <= 3:
            for i in range(self.minimal_move(),      # on peut choisir au maximum le reste des allumettes
                           self.allumette + 1):      # l'état actuel du jeu
                if (self.check_valid_move(i)):       # vérifie si ce move est valide
                    moves.append(i)
        else:
            for i in range(self.minimal_move(),
                           4):                       # on peut choisir au maximum 3 allumettes
                if (self.check_valid_move(i)):       # vérifie si ce move est valide
                    moves.append(i)

        # print("Coups jouables : " + str(moves))

        return moves

    def check_valid_move(self, choice):
        """
        Methode qui vérifie si le coup est valide
        """
        if (self.allumette - choice < 0):
            return False
        else:
            return True

    def check_current_state(self):  # utilisé par minmax
        """
        Methode qui vérifie l'état du jeu (victoire/défaite/match nul)
        On renvoit un booléen qui représente si le jeu est terminé: true sinon false
        """
        if (self.allumette != 0):
            return False
        else:
            return True

    def winner(self):  # utilisé par minmax
        """
        Methode pour récupérer le joueur victorieux
        """
        # le dernier joueur à avoir tiré la dernière allumette est le perdant
        if self.currentplayer == self.players[0]:
            winner = self.players[1]
        else:
            winner = self.players[0]
        return winner

    def minimal_move(self):
        """
        Le choix minimal qu'on peut faire ici une allumette
        """
        return 1

    def print_game(self):  # utilisé par l'humain
        """
        Pour printer le jeu
        """
        return str("Allumettes restantes : " + str(self.allumette))

    def print_rules(self):
        """
        Prints the game rules as text output.
        """
        return str("\nJeu de Nim:\nÀ tour de rôle saisissez au maximum 3 allumettes. Le gagnant\nest celui qui parviendra ne pas tirer la dernière allumette.\n")
