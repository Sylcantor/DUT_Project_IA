import numpy as np
from math import inf as infinity

# ───Constantes─────────────────────────────────────────────────────────────────────────────


game_state = [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']]

players = ['X', 'O']
# X = Human
# O = Bot


# ───Méthodes───────────────────────────────────────────────────────────────────────────────


def play_move(state, player, block_num):
    """
    Méthode pour jouer.

    Paramètres :
    
    Etat du jeu,
    Joueur qui joue,
    Case dans laquelle on veut jouer.
    """

    # On regarde si la case choisie est vide.
    # Conversion du nombre choisi (1 à 9) en 2 nombres (numéro de ligne et colonne).
    if state[int((block_num - 1) / 3)][(block_num - 1) % 3] is ' ':

        # Sur cette case on met alors un X ou un O (0 ou 1).
        state[int((block_num - 1) / 3)][(block_num - 1) % 3] = player

    # Comme l'IA prendra toujours un coup juste on ne revérifie pas.
    # Par contre, le joueur peut se tromper donc on remet un input.
    else:
        block_num = int(input("La case choisie n'est pas vide ! Choisissez-en une autre : "))
        play_move(state, player, block_num)


def copy_game_state(state):
    new_state = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    for i in range(3):
        for j in range(3):
            new_state[i][j] = state[i][j]
    
    return new_state


def check_current_state(game_state):
    """
    On regarde si le jeu est terminé.

    Paramètre : état du jeu.
    """

    # On vérifie tous les cas où la partie est finie (victoire horizontale, verticale, diagonale).
    # Si dans une ligne ou colonne ou diagonale on a case1 == case2 et case2 == case3 avec cases non vides
    # (X == X == X ou O == O == O),
    # Alors on retourne l'état de l'une des case de la suite et 'Done' (le jeu est fini).

    # Victoire horizontale (3 lignes)
    if (game_state[0][0] == game_state[0][1] and game_state[0][1] == game_state[0][2] and game_state[0][0] is not ' '):
        return game_state[0][0], "Done"
    if (game_state[1][0] == game_state[1][1] and game_state[1][1] == game_state[1][2] and game_state[1][0] is not ' '):
        return game_state[1][0], "Done"
    if (game_state[2][0] == game_state[2][1] and game_state[2][1] == game_state[2][2] and game_state[2][0] is not ' '):
        return game_state[2][0], "Done"

    # Victoire verticale (3 colonnes)
    if (game_state[0][0] == game_state[1][0] and game_state[1][0] == game_state[2][0] and game_state[0][0] is not ' '):
        return game_state[0][0], "Done"
    if (game_state[0][1] == game_state[1][1] and game_state[1][1] == game_state[2][1] and game_state[0][1] is not ' '):
        return game_state[0][1], "Done"
    if (game_state[0][2] == game_state[1][2] and game_state[1][2] == game_state[2][2] and game_state[0][2] is not ' '):
        return game_state[0][2], "Done"

    # Victoire diagonale (2 diagonales)
    if (game_state[0][0] == game_state[1][1] and game_state[1][1] == game_state[2][2] and game_state[0][0] is not ' '):
        return game_state[1][1], "Done"
    if (game_state[2][0] == game_state[1][1] and game_state[1][1] == game_state[0][2] and game_state[2][0] is not ' '):
        return game_state[1][1], "Done"

    # On regarde si la partie s'est terminée sur une égalité.
    draw_flag = 0

    for i in range(3):
        for j in range(3):
            if game_state[i][j] is ' ':
                draw_flag = 1
    
    if draw_flag is 0:
        return None, "Draw"

    # Aucun vainqueur, partie non terminée.
    return None, "Not Done"


def print_board(game_state):
    """
    On affiche le jeu.

    Paramètre : état du jeu.
    """

    print('----------------')
    print('| ' + str(game_state[0][0]) + ' || ' + str(game_state[0][1]) + ' || ' + str(game_state[0][2]) + ' |')
    print('----------------')
    print('| ' + str(game_state[1][0]) + ' || ' + str(game_state[1][1]) + ' || ' + str(game_state[1][2]) + ' |')
    print('----------------')
    print('| ' + str(game_state[2][0]) + ' || ' + str(game_state[2][1]) + ' || ' + str(game_state[2][2]) + ' |')
    print('----------------')


def getBestMove(state, player):
    """
    L'algorithme Minimax (celui de l'IA).

    Paramètres :

    Etat du jeu,
    Joueur qui joue.
    """

    # Vérification de l'état du jeu par l'IA.
    winner_loser, done = check_current_state(state)

    # Si le jeu est fini et que l'IA a gagné.
    if done == "Done" and winner_loser == 'O':
        return 1
    # Si le jeu est fini et que l'IA a perdu.
    elif done == "Done" and winner_loser == 'X':
        return -1
    # Si le jeu est fini et que personne n'a gagné.
    elif done == "Draw":
        return 0

    moves = []
    empty_cells = []
    
    # On numérote les cases vides.
    for i in range(3):
        for j in range(3):
            if state[i][j] is ' ':
                empty_cells.append(i*3 + (j+1))

    for empty_cell in empty_cells:
        move = {}
        move['index'] = empty_cell
        new_state = copy_game_state(state)
        play_move(new_state, player, empty_cell)

        # Si c'est à l'IA de jouer.
        if player == 'O':
            # make more depth tree for human
            result = getBestMove(new_state, 'X')
            move['score'] = result
        # Si c'est à l'humain de jouer.
        else:
            # make more depth tree for AI
            result = getBestMove(new_state, 'O')
            move['score'] = result

        moves.append(move)

    # Cherche le meilleur coup.
    best_move = None

    # Si c'est à l'IA de jouer.
    if player == 'O':
        best = -infinity
        for move in moves:
            # On récupère le max.
            if move['score'] > best:
                best = move['score']
                if best > 8:
                    print("IA", "score", best, "index", move['index'], "\n")
                # On récupère l'index de la meilleure case pour l'IA.
                best_move = move['index']
    # Si c'est à l'humain de jouer.
    else:
        best = infinity
        for move in moves:
            # On récupère le min.
            if move['score'] < best:
                best = move['score']
                if best < 0:
                    print("Humain", "score", best, "index", move['index'], "\n")
                # On récupère l'index de la pire case pour l'humain.
                best_move = move['index']

    return best_move


# ──Main────────────────────────────────────────────────────────────────────────────────────


# Démarrage du jeu.
play_again = 'Y'

# Recommencer le jeu.
while play_again == 'Y' or play_again == 'y':

    # Préparation du jeu.
    game_state = [[' ', ' ', ' '],
                  [' ', ' ', ' '],
                  [' ', ' ', ' ']]
    
    current_state = "Not Done"
    print("\nNouvelle partie !")
    print_board(game_state)

    player_choice = input("Choisissez le joueur qui commence - X (vous) ou O (l'IA) : ")
    winner = None

    # Si on joue en premier ou deuxième.
    if player_choice == 'X' or player_choice == 'x':
        # X == 0
        # L'humain joue en premier.
        current_player_idx = 0
    else:
        # X == 1
        # L'humain joue en deuxième.
        current_player_idx = 1

    # Tant que le jeu n'est pas terminé.
    while current_state == "Not Done":

        # current_player_idx est un booléen (si 0 alors c'est au tour de l'humain de jouer).
        if current_player_idx == 0:
            block_choice = int(input("C'est à vous de jouer, humain ! Choisissez une case à jouer (1 à 9) : "))
            # On donne : l'état du jeu, le joueur (X ou O) et le choix de la case.
            play_move(game_state, players[current_player_idx], block_choice)

        # current_player_idx == 1 donc l'humain ne joue pas.
        else:
            # L'IA choisit le meilleur coup en prenant en compte l'état du jeu et en indiquant si le joueur est X ou O.
            block_choice = getBestMove(game_state, players[current_player_idx])

            # L'IA peut jouer après avoir parcouru l'arbre et décidé d'une case à jouer.
            play_move(game_state, players[current_player_idx], block_choice)
            print("L'IA joue : " + str(block_choice))

        # On affiche le jeu et on vérifie que la partie est terminée.
        print_board(game_state)
        winner, current_state = check_current_state(game_state)

        # On affiche s'il y a un gagnant.
        if winner is not None:
            print(str(winner) + " gagne !")
        else:
            current_player_idx = (current_player_idx + 1) % 2

        # Egalité !
        if current_state is "Draw":
            print("Egalité !")

    # On recommence le jeu ou non.
    play_again = input('Voulez-vous rejouer ? (Y/N) : ')
    if play_again == 'N':
        print('A bientôt !')