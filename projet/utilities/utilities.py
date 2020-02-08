# -*- coding: utf-8 -*-
"""
@author: Aurélien
"""
import sys
import os
import random
import pickle
from copy import deepcopy

# les noeuds:
from agents.node import Node
from utilities.player import Player

# asserts:
from agents.agent import Agent
from agents.apprentissage_RL.agent import Learner

# plot:
from utilities.plot import plot_winrate

"""
fonctions utilitaires appelées depuis main.py
"""


def TurnBased(inital_game, agents):
    """
    Permet de jouer avec n'importe quel agent et n'importe quel nombre d'agent selon
    le nombre de joueurs dans la liste players du jeu entré.
    Les objets de type Learner apprennent durant chaque fin de partie.
    """
    for i in agents:
        try:
            isinstance(i, Agent)
        except AttributeError:
            sys.exit("AttributeError")

    game = deepcopy(inital_game)

    # liste de string qui représente les joueurs dans le jeu et définit le nombre de joueurs
    players = game.players

    if len(players) > len(agents):
        sys.exit("List index out of range: not enough agents to play")
    elif len(players) < len(agents):
        print("Too much agents: I will only take the firsts")

        # liste qui définit chaque joueurs et sauvegarde leurs informations
        # permet de faire le parallèle entre les players et les agents
        # PlayerList sera de la taille de players
    PlayerList = []
    for i, j in zip(players, agents):
        PlayerList.append(Player(i, j))

    # During teaching, chose who goes first randomly with equal probability
    playerIndex = random.randrange(len(PlayerList))

    print("#_______#NEW_GAME#_______#\n")

    currentnode = Node(game)

    # Initialize the learner's state and action
    for i in PlayerList:
        if isinstance(i.agent, Learner):
            i.prev_state = game.print_game()
            i.prev_action = i.agent.choose_move(currentnode, i.prev_state)

    # iterate until game is over
    while True:

        print("\n")
        print("___", PlayerList[playerIndex].player,
              PlayerList[playerIndex].agent.__class__.__name__, "___")

        # execute oldAction, observe reward and state
        if isinstance(PlayerList[playerIndex].agent, Learner):
            game.play_move(
                PlayerList[playerIndex].prev_action, PlayerList[playerIndex].player)
        else:
            currentnode = Node(game)
            choix = PlayerList[playerIndex].agent.choose_move(
                currentnode)
            game.play_move(choix, PlayerList[playerIndex].player)

        print("\n")

        # game is over. +10 reward if win, -10 if loss, 0 if draw
        if not game.winner() == None:
            break  # break car sinon updatera pour 0 à un état final

        # game continues. 0 reward
        reward = 0

        # change player
        playerIndex += 1
        if playerIndex >= len(players):
            playerIndex = 0

        for i in PlayerList:
            if isinstance(i.agent, Learner):
                # partie mise à jour des learners
                new_state = game.print_game()

                currentnode = Node(game)  # the new node after playing

                # determine new action (epsilon-greedy)
                new_action = i.agent.choose_move(currentnode, new_state)
                # update Q-values
                i.agent.update(currentnode, i.prev_state, new_state,
                               i.prev_action, new_action, reward)
                # reset "previous" values
                i.prev_state = new_state
                i.prev_action = new_action
                # append reward

    # Game over. Perform final update, game is over. +10 reward if win, -10 if loss, 0 if draw
    for i in PlayerList:
        if isinstance(i.agent, Learner):
            if game.winner() == i.player:
                i.agent.update(currentnode, i.prev_state, None,
                               i.prev_action, None, 10)
            elif game.winner() == 'Draw':  # it's a draw
                i.agent.update(currentnode, i.prev_state, None,
                               i.prev_action, None, 0)
            else:  # another player wins
                i.agent.update(currentnode, i.prev_state, None,
                               i.prev_action, None, -10)

    print("#________________________#")
    print("Le gagnant est : " + game.winner() + "\n")

    print("Affichage de fin : ")
    print(game.print_game())

    return game.winner()


def TurnBased_episodes(game, number_games, *agents):
    """
    Permet de faire plusieurs appels de TurnBased, utilisé pour l'entrainement
    On peut mettre plusieurs agents les uns à la suite des autres
    en argument de cette fonction. On a aussi besoins du jeu
    et le nombre de fois qu'on veut faire de jeux.
    """

    for i in range(number_games):

        sys.stdout = open(os.devnull, 'w')  # disable print out
        TurnBased(game, agents)
        sys.stdout = sys.__stdout__  # restore print out

        # Monitor progress
        if i % 1000 == 0:
            print("Games played: %i" % i)


def TurnBased_results(game, number_games, *agents):
    """
    Comme TurnBased_episodes sauf qu'on veut mettre sous forme de diagramme
    les résultats des parties gagnées grâce à plot_winrate.
    Fonction utile pour faire des tests manuels par exemple.
    """
    # TODO dissocier les games_won_J1 selon le nombre de joueurs
    games_won_J1 = 0
    games_won_J2 = 0
    draw = 0

    # liste de string qui représente les joueurs dans le jeu et définit le nombre de joueurs
    players = game.players

    for i in range(number_games):  # pour tester manuellement des parties après l'entrainement
        returned_winner = TurnBased(game, agents)

        if returned_winner == players[0]:
            games_won_J1 += 1
        elif returned_winner == players[1]:
            games_won_J2 += 1
        else:
            draw += 1

    plot_winrate([games_won_J1, games_won_J2, draw], [
                 'learner', 'agent', 'draw'], number_games)

# ──────────────────────────────────────────────────────────────────────────────── save & load


def save_learner(game, learner):
    """
    Save one game learner
    """
    # TODO mettre dans un dossier et numéroter
    if len(learner.rewards) != 0:
        while True:
            print(str(game.__class__.__name__) + "_" +
                  str(learner.__class__.__name__) + ".pkl" +
                  " Q matrix's size: " + str(len(learner.rewards)))
            response = input(
                "Do you want you want to save this learner ? [y/n]: ")
            if response == 'y' or response == 'yes':
                learner.save_agent(
                    './'+game.__class__.__name__+"_"+learner.__class__.__name__+'.pkl')
                break
            elif response == 'n' or response == 'no':
                print("OK. Learner not saved.")
                break
            else:
                print("Invalid input. Please choose 'y' or 'n'.")


def load_learner(file_name):
    """
    Load one game learner
    """
    try:
        f = open(file_name, 'rb')
    except IOError:
        print("The learner file does not exist. Quitting.")
        sys.exit(0)
    learner = pickle.load(f)
    f.close()
    return learner
