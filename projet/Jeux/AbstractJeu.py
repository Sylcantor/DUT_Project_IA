# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

# Abstract base class which outlines the basic functionality


class AbstractJeu:
    __metaclass__ = ABCMeta

    @abstractmethod
    def play_move(self, choice, currentplayer): pass  # utilisé par minmax
    """
    Methode pour jouer au jeu
    """

    @abstractmethod
    def valid_moves(self): pass  # utilisé par minmax
    """
    Methode qui donne sous forme de liste tous les coups jouables possibles
    """

    @abstractmethod
    def check_current_state(self): pass  # utilisé par minmax
    """
    Methode qui vérifie l'état du jeu (victoire/défaite/match nul)
    On renvoit un booléen qui représente si le jeu est terminé: true sinon false
    """

    @abstractmethod
    def winner(self): pass  # utilisé par minmax
    """
    Methode pour récupérer le joueur victorieux
    Si match nul on récupère: "Draw"
    """

    @abstractmethod
    def print_game(self): pass  # utilisé par l'humain et RL
    """
    Return the game board as string.
    """

    @abstractmethod
    def print_rules(self): pass  # utilisé par l'humain
    """
    Return the game rules as string.
    """
