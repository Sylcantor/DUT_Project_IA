# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

# Abstract base class which outlines the basic functionality


class AbstractAlgo:
    __metaclass__ = ABCMeta

    @abstractmethod
    def choose_move(self): pass
