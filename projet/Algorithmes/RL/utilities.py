# -*- coding: utf-8 -*-
"""
@author: Aurélien
"""
import random
from copy import deepcopy

# les algorithmes:
from Algorithmes.Minimax.node import Node

# Reinforcement learning:
from Algorithmes.RL.GameLearning import GameLearning


def TurnBasedRL(inital_game,
                teacher,
                gl,
                players=['Player1', 'Player2']):
    """
    Player1 -> 'X' -> teacher
    Player2 -> 'O' -> gl.agent
    """

    game = deepcopy(inital_game)

    # During teaching, chose who goes first randomly with equal probability
    if random.random() < 0.5:
        i = 0
    else:
        i = 1

    # Initialize the agent's state and action
    prev_state = game.getStateKey(game.board)
    prev_action = gl.agent.get_action(prev_state)

    # iterate until game is over
    while True:
        # execute oldAction, observe reward and state

        if i == 0:
            player = players[0]  # teacher
            currentnode = Node(game, player)
            teacher.choose_move(currentnode)
        else:
            player = players[1]  # agent
            game.agentMove(prev_action)

        i ^= 1

        if not game.winner() == None:
            # game is over. +10 reward if win, -10 if loss, 0 if draw
            if game.winner() == players[1]:
                reward = 10
            elif game.winner() == players[0]:
                reward = -10
            else:
                reward = 0
            break

        # game continues. 0 reward
        reward = 0

        new_state = game.getStateKey(game.board)

        # determine new action (epsilon-greedy)
        new_action = gl.agent.get_action(new_state)
        # update Q-values
        gl.agent.update(prev_state, new_state,
                        prev_action, new_action, reward)
        # reset "previous" values
        prev_state = new_state
        prev_action = new_action
        # append reward

    # Game over. Perform final update
    gl.agent.update(prev_state, None, prev_action, None, reward)
