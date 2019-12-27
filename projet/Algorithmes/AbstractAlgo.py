# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

# Abstract base class which outlines the basic functionality


class AbstractAlgo:
    __metaclass__ = ABCMeta

    @abstractmethod
    def choose_move(self): pass
    """
    Methode pour faire des choix selon l'agent
    Les argurments n'ont pas d'importantce
    """


"""
RL: Reinforcement Learning
Let’s get introduced to some terminologies.
1. Agent: The problem solver, can perform some actions.
2. Environment: An agent resides here. An environment provides responses to an agent based on the actions it performs.
3. Reward: When an agent performs an action in an environment, there is an associated reward; rewards can be positive, negative(punishment) or zero.
4. State: An agent’s action may cause it to enter a state which is a snapshot of the environment. (Like checkmate (state) on a chess board (environment))
5. Policy: Defines an agent’s behavior, can answer questions like what action should be performed in this state?
6. Value: Tracks the long-term impact of the action. Provides a portion of reward to intermediate states that led to a final positive state.
"""
