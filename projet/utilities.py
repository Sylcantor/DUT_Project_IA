# -*- coding: utf-8 -*-
"""
@author: Aurélien
"""
import random
from copy import deepcopy

# les noeuds:
from agents.node import Node


def TurnBasedRLvsAgent(inital_game,
                       gl,
                       teacher,
                       players=['Player1', 'Player2']):
    """
    Fonction pour jouer à tour de role en permettant à un objet de
    type GameLearning d'apprendre.
    Joueur 1 est le premier joueur à jouer et Joueur 2 est le second.
    Player1 -> 'X' -> gl.agent
    Player2 -> 'O' -> teacher
    """

    game = deepcopy(inital_game)

    # During teaching, chose who goes first randomly with equal probability
    if random.random() < 0.5:
        i = 0
    else:
        i = 1

    print("#_______#NEW_GAME#_______#\n")

    currentnode = Node(game, players[0])  # ajouté

    # Initialize the agent's state and action
    prev_state = game.print_game()
    prev_action = gl.agent.choose_move(currentnode, prev_state)

    # iterate until game is over
    while True:
        # execute oldAction, observe reward and state

        print("\n")

        if i == 0:

            player = players[0]  # agent - Player1
            print("___ " + player + " ___")
            game.play_move(prev_action, player)

        else:

            player = players[1]  # teacher - Player2
            print("___ " + player + " ___")
            currentnode = Node(game, player)
            choix = teacher.choose_move(currentnode)
            game.play_move(choix, player)

        print("\n")
        i ^= 1

        if not game.winner() == None:
            # game is over. +10 reward if win, -10 if loss, 0 if draw
            if game.winner() == players[0]:  # Player1 -> 'X' -> gl.agent
                reward = 10
            elif game.winner() == players[1]:  # Player2 -> 'O' -> teacher
                reward = -10
            else:
                reward = 0
            break

        # game continues. 0 reward
        reward = 0

        new_state = game.print_game()

        currentnode = Node(game, players[0])  # ajouté

        # determine new action (epsilon-greedy)
        new_action = gl.agent.choose_move(currentnode, new_state)
        # update Q-values
        gl.agent.update(currentnode, prev_state, new_state,
                        prev_action, new_action, reward)
        # reset "previous" values
        prev_state = new_state
        prev_action = new_action
        # append reward

    # Game over. Perform final update
    gl.agent.update(currentnode, prev_state, None, prev_action, None, reward)

    print("#________________________#")
    print("Le gagnant est : " + game.winner() + "\n")

    print("Affichage de fin : ")
    print(game.print_game())

    return game.winner()


def TurnBasedRLvsRL(inital_game,
                    gl1,
                    gl2,
                    players=['Player1', 'Player2']):
    """
    Fonction pour jouer à tour de role en permettant à un objet de
    type GameLearning d'apprendre.
    Joueur 1 est le premier joueur à jouer et Joueur 2 est le second.
    Player1 -> 'X' -> gl.agent
    Player2 -> 'O' -> teacher
    """

    game = deepcopy(inital_game)

    print("#_______#NEW_GAME#_______#\n")

    currentnode = Node(game, players[0])  # ajouté

    # Initialize the agent's state and action
    prev_state = game.print_game()

    prev_action1 = gl1.agent.choose_move(
        currentnode, prev_state)  # pour initialiser
    prev_action2 = gl2.agent.choose_move(currentnode, prev_state)

    # During teaching, chose who goes first randomly with equal probability
    if random.random() < 0.5:
        i = 0
    else:
        i = 1

    # iterate until game is over
    while True:
        # execute oldAction, observe reward and state

        print("\n")

        if i == 0:

            player = players[0]  # gl1 - Player1
            print("___ " + player + " ___")
            game.play_move(prev_action1, player)

        else:

            player = players[1]  # gl2 - Player2
            print("___ " + player + " ___")
            game.play_move(prev_action2, player)

        print("\n")

        if not game.winner() == None:
            # game is over. +10 reward if win, -10 if loss, 0 if draw
            if game.winner() == players[0]:  # Player1 -> 'X' -> gl.agent
                reward = 10
            elif game.winner() == players[1]:  # Player2 -> 'O' -> teacher
                reward = -10
            else:
                reward = 0
            break

        # game continues. 0 reward
        reward = 0

        new_state = game.print_game()

        if i == 0:
            currentnode = Node(game, players[0])  # ajouté

            # determine new action (epsilon-greedy)
            new_action1 = gl1.agent.choose_move(currentnode, new_state)
            # update Q-values
            gl1.agent.update(currentnode, prev_state, new_state,
                             prev_action1, new_action1, reward)
            # reset "previous" values
            prev_state = new_state
            prev_action1 = new_action1
            # append reward
        else:
            currentnode = Node(game, players[1])  # ajouté

            # determine new action (epsilon-greedy)
            new_action2 = gl2.agent.choose_move(currentnode, new_state)
            # update Q-values
            gl2.agent.update(currentnode, prev_state, new_state,
                             prev_action2, new_action2, reward)
            # reset "previous" values
            prev_state = new_state
            prev_action2 = new_action2
            # append reward

        i ^= 1

    # Game over. Perform final update
    gl1.agent.update(currentnode, prev_state, None,
                     prev_action1, None, reward)

    gl2.agent.update(currentnode, prev_state, None,
                     prev_action2, None, reward)

    print("#________________________#")
    print("Le gagnant est : " + game.winner() + "\n")

    print("Affichage de fin : ")
    print(game.print_game())

    return game.winner()


def PrintResults(resultsJ1, resultsJ2, draw, number_games, players=['Player1', 'Player2']):
    # les résultats en % des parties gagnées sur le nombre total de parties
    print("Win rate " + players[0] + " : " +
          str((resultsJ1/number_games)*100) + " %" +
          " | "+"Win rate " + players[1] + " : " +
          str((resultsJ2/number_games)*100) + " % "
          " | "+"Draw rate " + " : " +
          str((draw/number_games)*100) + " % ")
