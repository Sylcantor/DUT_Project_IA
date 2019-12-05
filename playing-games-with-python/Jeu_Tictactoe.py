import numpy as np
from math import inf as infinity

from Minimax.game_tree import GameTree
from Minimax.minimax import Minimax


players = ['Human', 'Bot']

class Tictactoe():

    def __init__(self,firstplayer,game_state):
        self.currentplayer = firstplayer
        self.game_state = game_state
    

    def play_move(self, block_choice, currentplayer):
        self.currentplayer = currentplayer

        if(self.check_valid_move(block_choice)):
            self.game_state[int((block_choice - 1) / 3)][(block_choice - 1) % 3] = currentplayer
        else:
            block_choice = int(input("La case choisie n'est pas vide ! Choisissez-en une autre : "))
            self.play_move(block_choice, currentplayer)


    def check_valid_move(self,block_choice):
        # On regarde si la case choisie est vide.
        
        if self.game_state[int((block_choice - 1) / 3)][(block_choice - 1) % 3] is ' ':
            return True
        else:
            return False
    
    def invalid_moves(self):
        """
        Methode qui renvoie les coups impossibles
        """
        invalid = []
        for i in range(1,9):
            if self.game_state[int((i - 1) / 3)][(i - 1) % 3] is not ' ':  # si la case choisie n'est pas dans le plateau
                invalid.append(i)

        print("invalid moves" + str(invalid))
        return invalid

    def check_current_state(self):
        """
        On regarde si le jeu est terminé.

        Paramètre : état du jeu.
        """

        # On vérifie tous les cas où la partie est finie (victoire horizontale, verticale, diagonale).
        # Si dans une ligne ou colonne ou diagonale on a case1 == case2 et case2 == case3 avec cases non vides
        # (X == X == X ou O == O == O),
        # Alors on retourne l'état de l'une des case de la suite et 'Done' (le jeu est fini).

        # Victoire horizontale (3 lignes)
        if (self.game_state[0][0] == self.game_state[0][1] and self.game_state[0][1] == self.game_state[0][2] and self.game_state[0][0] is not ' '):
            return self.game_state[0][0], True
        if (self.game_state[1][0] == self.game_state[1][1] and self.game_state[1][1] == self.game_state[1][2] and self.game_state[1][0] is not ' '):
            return self.game_state[1][0], True
        if (self.game_state[2][0] == self.game_state[2][1] and self.game_state[2][1] == self.game_state[2][2] and self.game_state[2][0] is not ' '):
            return self.game_state[2][0], True

        # Victoire verticale (3 colonnes)
        if (self.game_state[0][0] == self.game_state[1][0] and self.game_state[1][0] == self.game_state[2][0] and self.game_state[0][0] is not ' '):
            return self.game_state[0][0], True
        if (self.game_state[0][1] == self.game_state[1][1] and self.game_state[1][1] == self.game_state[2][1] and self.game_state[0][1] is not ' '):
            return self.game_state[0][1], True
        if (self.game_state[0][2] == self.game_state[1][2] and self.game_state[1][2] == self.game_state[2][2] and self.game_state[0][2] is not ' '):
            return self.game_state[0][2], True

        # Victoire diagonale (2 diagonales)
        if (self.game_state[0][0] == self.game_state[1][1] and self.game_state[1][1] == self.game_state[2][2] and self.game_state[0][0] is not ' '):
            return self.game_state[1][1], True
        if (self.game_state[2][0] == self.game_state[1][1] and self.game_state[1][1] == self.game_state[0][2] and self.game_state[2][0] is not ' '):
            return self.game_state[1][1], True
            
        # On regarde si la partie s'est terminée sur une égalité.
        draw_flag = 0

        for i in range(3):
            for j in range(3):
                if self.game_state[i][j] is ' ':
                    draw_flag = 1
        
        if draw_flag is 0:
            return None, "Draw"

        # Aucun vainqueur, partie non terminée.
        return None, "Not Done"

    def current_state(self):
        return 9 # nombre de cases

    def print_board(self):
        """
        On affiche le jeu.

        Paramètre : état du jeu.
        """

        print('----------------')
        print('| ' + str(self.game_state[0][0]) + ' || ' + str(self.game_state[0][1]) + ' || ' + str(self.game_state[0][2]) + ' |')
        print('----------------')
        print('| ' + str(self.game_state[1][0]) + ' || ' + str(self.game_state[1][1]) + ' || ' + str(self.game_state[1][2]) + ' |')
        print('----------------')
        print('| ' + str(self.game_state[2][0]) + ' || ' + str(self.game_state[2][1]) + ' || ' + str(self.game_state[2][2]) + ' |')
        print('----------------')

    def minimal_move(self):
        return 1



# Démarrage du jeu.
play_again = 'Y'

while play_again == 'Y' or play_again == 'y':
    # Préparation du jeu.
    game_state = [[' ', ' ', ' '],
                  [' ', ' ', ' '],
                  [' ', ' ', ' ']]

    game = Tictactoe(players[0],game_state)

    gtree = GameTree(game)

    tictactoe_tree = gtree.create_tree(game, players[0])
    
    current_state = "Not Done"
    print("\nNouvelle partie !")
    game.print_board()
    winner = None

    # Tant que le jeu n'est pas terminé.
    while current_state == "Not Done":

        # game.currentplayer est un booléen (si 0 alors c'est au tour de l'humain de jouer).
        if game.currentplayer == 0:
            block_choice = int(input("C'est à vous de jouer, humain ! Choisissez une case à jouer (1 à 9) : "))
            # On donne : l'état du jeu, le joueur (X ou O) et le choix de la case.
            game.play_move(block_choice, players[game.currentplayer])

        # game.currentplayer == 1 donc l'humain ne joue pas.
        else:
            # L'IA choisit le meilleur coup en prenant en compte l'état du jeu et en indiquant si le joueur est X ou O.

            #block_choice = getBestMove(game_state, players[game.currentplayer])

            # L'IA peut jouer après avoir parcouru l'arbre et décidé d'une case à jouer.
            game.play_move(block_choice, players[game.currentplayer])
            print("L'IA joue : " + str(block_choice))

        # On affiche le jeu et on vérifie que la partie est terminée.
        game.print_board()
        winner, current_state = game.check_current_state()

        # On affiche s'il y a un gagnant.
        if winner is not None:
            print(str(winner) + " gagne !")
        else:
            game.currentplayer = (game.currentplayer + 1) % 2

        # Egalité !
        if current_state is "Draw":
            print("Egalité !")

        # On recommence le jeu ou non.
        play_again = input('Voulez-vous rejouer ? (Y/N) : ')
        if play_again == 'N':
            print('A bientôt !')