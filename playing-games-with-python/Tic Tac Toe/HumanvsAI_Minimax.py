import numpy as np
from math import inf as infinity

# ───Constantes─────────────────────────────────────────────────────────────────────────────


game_state = [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']]
players = ['X', 'O']
# X = Human
# O = Bot

# ───Méthodes─────────────────────────────────────────────────────────────────────────────


def play_move(state, player, block_num):
    """
    Méthode pour jouer.
    On prend l'état du jeu,
    Le joueur qui est en train de joueur,
    Le numéro du coup (la case) qu'on veut jouer.
    """
    # On vérifie si la case est vide
    if state[int((block_num-1)/3)][(block_num-1) % 3] is ' ':

        # Sur cette case alors on met un X ou O (0 ou 1)
        state[int((block_num-1)/3)][(block_num-1) % 3] = player

    # Comme l'IA prendra toujours un coup juste on ne revérifie pas, par contre
    # le joueur peut se tromper alors on remet un input
    else:
        block_num = int(
            input("Block is not empty, ya blockhead! Choose again: "))
        play_move(state, player, block_num)


def copy_game_state(state):
    new_state = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    for i in range(3):
        for j in range(3):
            new_state[i][j] = state[i][j]
    return new_state


def check_current_state(game_state):
    """
    On vérifie si le jeu est terminé.
    On prend l'état du jeu.
    """
    # Check if draw
    draw_flag = 0
    for i in range(3):
        for j in range(3):
            if game_state[i][j] is ' ':
                draw_flag = 1
    if draw_flag is 0:
        return None, "Draw"

    # On vérifie chaque cas si la partie est finie (horizontales, verticales, diagonales)
    # Si c'est terminé :
    # (s'il y a une ligne avec X == X et que
    # le suivant est aussi X == X (donc une ligne de X X X par exemple)
    # et que tous les 3 sont pas vides (' '))
    # Alors on retourne le type (X ou O) d'une des case de la ligne et que le jeu est fini ('Done')

    # Check horizontals
    if (game_state[0][0] == game_state[0][1] and game_state[0][1] == game_state[0][2] and game_state[0][0] is not ' '):
        return game_state[0][0], "Done"
    if (game_state[1][0] == game_state[1][1] and game_state[1][1] == game_state[1][2] and game_state[1][0] is not ' '):
        return game_state[1][0], "Done"
    if (game_state[2][0] == game_state[2][1] and game_state[2][1] == game_state[2][2] and game_state[2][0] is not ' '):
        return game_state[2][0], "Done"

    # Check verticals
    if (game_state[0][0] == game_state[1][0] and game_state[1][0] == game_state[2][0] and game_state[0][0] is not ' '):
        return game_state[0][0], "Done"
    if (game_state[0][1] == game_state[1][1] and game_state[1][1] == game_state[2][1] and game_state[0][1] is not ' '):
        return game_state[0][1], "Done"
    if (game_state[0][2] == game_state[1][2] and game_state[1][2] == game_state[2][2] and game_state[0][2] is not ' '):
        return game_state[0][2], "Done"

    # Check diagonals
    if (game_state[0][0] == game_state[1][1] and game_state[1][1] == game_state[2][2] and game_state[0][0] is not ' '):
        return game_state[1][1], "Done"
    if (game_state[2][0] == game_state[1][1] and game_state[1][1] == game_state[0][2] and game_state[2][0] is not ' '):
        return game_state[1][1], "Done"

    return None, "Not Done"


def print_board(game_state):
    """
    Printer le jeu.
    On prend l'état du jeu.
    """
    print('----------------')
    print('| ' + str(game_state[0][0]) + ' || ' +
          str(game_state[0][1]) + ' || ' + str(game_state[0][2]) + ' |')
    print('----------------')
    print('| ' + str(game_state[1][0]) + ' || ' +
          str(game_state[1][1]) + ' || ' + str(game_state[1][2]) + ' |')
    print('----------------')
    print('| ' + str(game_state[2][0]) + ' || ' +
          str(game_state[2][1]) + ' || ' + str(game_state[2][2]) + ' |')
    print('----------------')


def getBestMove(state, player):
    '''
    Minimax Algorithm, L'algorithme de l'IA.
    On prend l'état du jeu,
    Le type de l'IA (si elle est X ou O).
    '''
    # Vérification de l'état du jeu par l'IA
    winner_loser, done = check_current_state(state)

    # Si le jeu est fini et que l'IA a gagné
    if done == "Done" and winner_loser == 'O':  # If AI won
        return 1
    # Si le jeu est fini et que l'IA a perdu
    elif done == "Done" and winner_loser == 'X':  # If Human won
        return -1
    elif done == "Draw":    # Draw condition
        return 0

    moves = []
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if state[i][j] is ' ':
                empty_cells.append(i*3 + (j+1))

    for empty_cell in empty_cells:
        move = {}
        move['index'] = empty_cell
        new_state = copy_game_state(state)
        play_move(new_state, player, empty_cell)

        if player == 'O':    # If AI
            # make more depth tree for human
            result = getBestMove(new_state, 'X')
            move['score'] = result
        else:
            # make more depth tree for AI
            result = getBestMove(new_state, 'O')
            move['score'] = result

        moves.append(move)

    # Find best move
    best_move = None
    if player == 'O':   # If AI player
        best = -infinity
        for move in moves:
            if move['score'] > best:
                best = move['score']
                best_move = move['index']
    else:
        best = infinity
        for move in moves:
            if move['score'] < best:
                best = move['score']
                best_move = move['index']

    return best_move

# ──Main──────────────────────────────────────────────────────────────────────────────


# PLaying
play_again = 'Y'

# Recommencer le jeu
while play_again == 'Y' or play_again == 'y':

    # Préparation du jeu
    game_state = [[' ', ' ', ' '],
                  [' ', ' ', ' '],
                  [' ', ' ', ' ']]
    current_state = "Not Done"
    print("\nNew Game!")
    print_board(game_state)

    player_choice = input(
        "Choose which player goes first - X (You - the petty human) or O(The mighty AI): ")
    winner = None

    # Si on joue en premier ou deuxième
    if player_choice == 'X' or player_choice == 'x':
        # X = 0
        # L'humain joue en premier
        current_player_idx = 0
    else:
        # X = 1
        # L'humain joue en deuxième
        current_player_idx = 1

    # Tant que le jeu n'est pas terminé
    while current_state == "Not Done":

        # current_player_idx est un booléen et si 0 alors l'humain peut jouer
        if current_player_idx == 0:  # Human's turn
            # Input comme un scanner en java
            block_choice = int(
                input("Oye Human, your turn! Choose where to place (1 to 9): "))
            # on donne: l'etat du jeu, le joueur (s'il est X ou O) et le choix
            play_move(game_state, players[current_player_idx], block_choice)

        # (current_player_idx == 1) l'humain ne joue pas
        else:  # AI's turn
            # L'IA prend le meilleur choix en prenant en compte l'etat du jeu et en indiquant si le joueur est X ou O
            block_choice = getBestMove(game_state, players[current_player_idx])

            # Comme l'IA a parcouru l'arbre et a décidé d'un choix elle peut jouer
            play_move(game_state, players[current_player_idx], block_choice)
            print("AI plays move: " + str(block_choice))

        # On print le jeu et on vérifie si la partie est terminée
        print_board(game_state)
        winner, current_state = check_current_state(game_state)

        # S'il y a un gagnant
        if winner is not None:
            print(str(winner) + " won!")
        else:
            current_player_idx = (current_player_idx + 1) % 2

        # Draw !
        if current_state is "Draw":
            print("Draw!")

    # On recommence le jeu ou pas
    play_again = input('Wanna try again BIYTACH?(Y/N) : ')
    if play_again == 'N':
        print('Suit yourself bitch!')
