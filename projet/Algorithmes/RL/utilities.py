# -*- coding: utf-8 -*-
"""
@author: Aurélien
"""
from copy import deepcopy

# Reinforcement learning:
from Algorithmes.RL.GameLearning import GameLearning


def TurnBasedRL(inital_game,
                player1,
                player2,
                numGames=1,
                players=['Player1', 'Player2']):
    """
    Fonction pour jouer à tour de role
    Joueur 1 est le premier joueur à jouer et Joueur 2 est le second
    """
    if isinstance(player1, GameLearning):
        gl = player1
    elif isinstance(player2, GameLearning):
        gl = player2
    else:
        exit(0)

    # Initialize the agent's state and action
    prev_state = getStateKey(self.board)
    prev_action = self.agent.get_action(prev_state)

    # iterate until game is over
    while True:
        # execute oldAction, observe reward and state
        self.agentMove(prev_action)
        check = self.checkForEnd('O')
        if not check == -1:
            # game is over. +1 reward if win, 0 if draw
            reward = check
            break
        self.playerMove()
        check = self.checkForEnd('X')
        if not check == -1:
            # game is over. -1 reward if lose, 0 if draw
            reward = -1*check
            break
        else:
            # game continues. 0 reward
            reward = 0
        new_state = getStateKey(self.board)

        # determine new action (epsilon-greedy)
        new_action = self.agent.get_action(new_state)
        # update Q-values
        self.agent.update(prev_state, new_state,
                          prev_action, new_action, reward)
        # reset "previous" values
        prev_state = new_state
        prev_action = new_action
        # append reward

    # Game over. Perform final update
    self.agent.update(prev_state, None, prev_action, None, reward)

    games_won_J1 = 0
    games_won_J2 = 0
    draw = 0

    for numGame in range(numGames):

        i = 0

        game = deepcopy(inital_game)

        player = players[0]  # pour initialiser, le premier joueur est Joueur 1

        print("#_______#NEW_GAME#_______#")

        while ((game.check_current_state()) == False):

            if i == 0:
                player = players[0]  # human
                print("___ " + player + " ___")

                currentnode = Node(game, player)

                choix = player1.choose_move(currentnode)
                game.play_move(choix, player)
                print("\n")
            else:
                player = players[1]  # bot
                print("___ " + player + " ___")

                currentnode = Node(game, player)

                choix = player2.choose_move(currentnode)
                game.play_move(choix, player)
                print("\n")

            i ^= 1
        print("#________________________#")
        print("Le gagnant est : " + game.winner() + "\n")

        print("Affichage de fin : ")
        print(game.print_game())

        if game.winner() == players[0]:
            games_won_J1 += 1
        elif game.winner() == players[1]:
            games_won_J2 += 1
        else:
            draw += 1

    return games_won_J1, games_won_J2, draw
