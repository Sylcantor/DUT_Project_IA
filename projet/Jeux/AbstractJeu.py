# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

# Abstract base class which outlines the basic functionality


class AbstractJeu:
    __metaclass__ = ABCMeta

    @abstractmethod
    def play_move(self, choice, currentplayer): pass  # utilisé par minmax

    @abstractmethod
    def valid_moves(self): pass  # utilisé par minmax

    @abstractmethod
    def check_current_state(self): pass  # utilisé par minmax

    @abstractmethod
    def winner(self): pass  # utilisé par minmax

    @abstractmethod
    def print_game(self): pass  # utilisé par l'humain
