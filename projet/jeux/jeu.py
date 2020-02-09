# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

# Abstract base class which outlines the basic functionality


class Jeu:
    __metaclass__ = ABCMeta

    @abstractmethod
    def play_move(self, choice, currentplayer): pass  # utilisé par les agents
    """
    Methode pour jouer au jeu
    """

    @abstractmethod
    def valid_moves(self): pass  # utilisé par les agents
    """
    Methode qui donne sous forme de liste tous les coups jouables possibles
    """

    @abstractmethod
    def check_current_state(self): pass  # utilisé par les agents
    """
    Methode qui vérifie l'état du jeu (victoire/défaite/match nul)
    On renvoit un booléen qui représente si le jeu est terminé: true sinon false
    """

    @abstractmethod
    def winner(self): pass  # utilisé par les agents
    """
    Methode pour récupérer le joueur victorieux
    Si match nul on récupère: "Draw"
    Si le match est toujours en cours on retourne "None"
    """

    @abstractmethod
    # utilisé par l'humain et les algorithmes d'apprentissage
    def print_game(self): pass
    """
    Return the game board as string.
    Représente l'état du jeu pour le reinforcement learning.
    """

    @abstractmethod
    def print_rules(self): pass  # utilisé par l'humain
    """
    Return the game rules as string.
    """