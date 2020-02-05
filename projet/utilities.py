# -*- coding: utf-8 -*-
"""
@author: Aurélien
"""
import sys
import os
import random
from copy import deepcopy

# les noeuds:
from agents.node import Node

# asserts:
from agents.apprentissage_RL.agent import Learner
from agents.AbstractAgent import AbstractAgent

"""
fonctions utilitaires
"""


def TurnBased(inital_game,  # AgentvsAgent
              agent1,
              agent2,
              players=['Player1', 'Player2']):
    """
    Agent avec un agent.
    Fonction pour jouer à tour de role en permettant à un objet de
    type GameLearning d'apprendre.
    Joueur 1 est le premier joueur à jouer et Joueur 2 est le second.
    Player1 -> 'X' -> agent1
    Player2 -> 'O' -> agent2
    """
    assert agent1 is not isinstance(agent1, AbstractAgent)
    assert agent2 is not isinstance(agent2, AbstractAgent)

    game = deepcopy(inital_game)

    # During teaching, chose who goes first randomly with equal probability
    if random.random() < 0.5:
        i = 0
    else:
        i = 1

    print("#_______#NEW_GAME#_______#\n")

    # iterate until game is over
    while True:
        # execute oldAction, observe reward and state

        print("\n")

        if i == 0:

            player = players[0]  # agent1 - Player1
            print("___ " + player + " ___")
            currentnode = Node(game, player)
            choix = agent1.choose_move(currentnode)
            game.play_move(choix, player)

        else:

            player = players[1]  # agent2 - Player2
            print("___ " + player + " ___")
            currentnode = Node(game, player)
            choix = agent2.choose_move(currentnode)
            game.play_move(choix, player)

        if not game.winner() == None:
            # game is over. +10 reward if win, -10 if loss, 0 if draw
            if game.winner() == players[0]:  # Player1 -> 'X' -> gl.agent
                reward = 10
            elif game.winner() == players[1]:  # Player2 -> 'O' -> teacher
                reward = -10
            else:
                reward = 0
            break

        print("\n")
        i ^= 1

    # Game over.
    print("#________________________#")
    print("Le gagnant est : " + game.winner() + "\n")

    print("Affichage de fin : ")
    print(game.print_game())

    return game.winner()


def TurnBasedRL(inital_game,  # vsAgent
                gl,
                teacher,
                players=['Player1', 'Player2']):
    """
    Reinforcement learning avec un agent.
    Fonction pour jouer à tour de role en permettant à un objet de
    type GameLearning d'apprendre.
    Joueur 1 est le premier joueur à jouer et Joueur 2 est le second.
    Player1 -> 'X' -> gl.agent
    Player2 -> 'O' -> teacher
    """
    assert gl is not isinstance(gl, Learner)
    assert teacher is not isinstance(teacher, AbstractAgent)

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

        # partie mise à jour

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
    Double reinforcement learning.
    Fonction pour jouer à tour de role en permettant à deux objets de
    type GameLearning d'apprendre.
    Joueur 1 est le premier joueur à jouer et Joueur 2 est le second.
    Player1 -> 'X' -> gl1.agent
    Player2 -> 'O' -> gl2.agent
    """

    assert gl1 is not isinstance(gl1, Learner)
    assert gl2 is not isinstance(gl2, Learner)

    game = deepcopy(inital_game)

    print("#_______#NEW_GAME#_______#\n")

    currentnode = Node(game, players[0])  # ajouté

    # Initialize the agent's state and action
    prev_state = game.print_game()

    # pour initialiser
    prev_action1 = gl1.agent.choose_move(currentnode, prev_state)
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
                reward1 = 10
                reward2 = -10
            elif game.winner() == players[1]:  # Player2 -> 'O' -> teacher
                reward1 = -10
                reward2 = 10
            else:
                reward1 = reward2 = 0
            break

        # game continues. 0 reward
        reward1 = reward2 = 0

        new_state = game.print_game()

        # partie mise à jour
        if i == 0:
            currentnode = Node(game, players[0])  # ajouté

            # determine new action (epsilon-greedy)
            new_action1 = gl1.agent.choose_move(currentnode, new_state)
            # update Q-values
            gl1.agent.update(currentnode, prev_state, new_state,
                             prev_action1, new_action1, reward1)
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
                             prev_action2, new_action2, reward2)
            # reset "previous" values
            prev_state = new_state
            prev_action2 = new_action2
            # append reward

        i ^= 1

    # Game over. Perform final update
    gl1.agent.update(currentnode, prev_state, None,
                     prev_action1, None, reward1)

    gl2.agent.update(currentnode, prev_state, None,
                     prev_action2, None, reward2)

    print("#________________________#")
    print("Le gagnant est : " + game.winner() + "\n")

    print("Affichage de fin : ")
    print(game.print_game())

    return game.winner()


def TurnBasedRL_episodes(game, gl, agent, teacher_episodes):

    for i in range(teacher_episodes):

        sys.stdout = open(os.devnull, 'w')  # disable print out
        TurnBasedRL(game, gl, agent)
        sys.stdout = sys.__stdout__  # restore print out

        # Monitor progress
        if i % 1000 == 0:
            print("Games played: %i" % i)


def TurnBasedRLvsRL_episodes(game, gl1, gl2, teacher_episodes):

    for i in range(args.teacher_episodes):

        sys.stdout = open(os.devnull, 'w')  # disable print out
        TurnBasedRLvsRL(game, gl1, gl2)
        sys.stdout = sys.__stdout__  # restore print out

        # Monitor progress
        if i % 1000 == 0:
            print("Games played: %i" % i)


def TurnBasedRL_PrintResults(game, gl, agent, number_games):
    games_won_J1 = 0
    games_won_J2 = 0
    draw = 0

    players = ['Player1', 'Player2']

    for i in range(number_games):  # pour tester manuellement des parties après l'entrainement
        # changer ici se besoins l'agent
        returned_winner = TurnBasedRL(game, gl, agent)

        if returned_winner == players[0]:
            games_won_J1 += 1
        elif returned_winner == players[1]:
            games_won_J2 += 1
        else:
            draw += 1

    PrintResults(games_won_J1, games_won_J2, draw,
                 number_games, ['learner', 'agent'])


def PrintResults(*names, *results, number_games):
    # les résultats en % des parties gagnées sur le nombre total de parties
    print("Win rate :")

    for i, j in zip(names, results): 
    print(i, ":",(j/number_games)*100,"%")


def SaveGL(gl, game):
    if os.path.isfile('./'+gl.agent.__class__.__name__+"_"+game.__class__.__name__+'.pkl'):
        while True:
            response = input("An agent state is already saved for this type. "
                             "Are you sure you want to overwrite? [y/n]: ")
            if response == 'y' or response == 'yes':
                gl.agent.save_agent(
                    './'+gl.agent.__class__.__name__+game.__class__.__name__+'.pkl')
                break
            elif response == 'n' or response == 'no':
                print("OK. Quitting.")
                break
            else:
                print("Invalid input. Please choose 'y' or 'n'.")
    else:
        gl.agent.save_agent(
            './'+gl.agent.__class__.__name__+"_"+game.__class__.__name__+'.pkl')
