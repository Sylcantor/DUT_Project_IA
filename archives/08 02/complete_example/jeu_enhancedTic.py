import random

from games.jeu import Jeu
from games.complete_example.inventory import Inventory


class enhancedTic(Jeu):
    """ The game class. New instance created for each new game. """

    def __init__(self, requested_number_players=3, requested_board_size=4, requested_number_moves=3):

        self.number_players = 3  # sélection nombre de joueurs
        if requested_number_players >= 3 and requested_number_players <= 6:
            self.number_players = requested_number_players

        self.board_size = 4  # sélection taille plateau
        if requested_board_size >= 4 and requested_board_size <= 6:
            self.board_size = requested_board_size

        self.number_moves = 3  # sélection nombre de coups par tour
        if requested_number_moves >= 3 and requested_number_moves <= 4:
            self.number_moves = requested_number_moves

        self.players = []  # liste des joueurs
        for i in range(self.number_players):
            player = "Player"+str(i)
            self.players.append(player)

        self.board = []  # le plateau
        for i in range(self.board_size):
            row = []
            for j in range(self.board_size):
                row.append('-')
            self.board.append(row)

        self.currentplayer = None     # caractérise le dernier joueur qui a joué
        self.inventories = []         # inventaire de chaque joueur
        for i in self.players:
            self.inventories.append(Inventory(i, self.number_moves))
        return

    def play_move(self, choice, currentplayer):  # utilisé par les agents
        """
        Methode pour jouer au jeu
        On change l'état du jeu
        """
        self.currentplayer = currentplayer
        if choice in self.valid_moves():        # vérification supplémentaire mais normalement c'est forcément vrai
                                                # si on choisit un move parmis les valid_moves()
            row, col = int(choice[0]), int(choice[1])

            for i in self.inventories:          # on pose le pion du joueur
                if self.currentplayer == i.player:
                    self.board[row][col] = i.pawn

        self.game_scoring()

    def game_scoring(self):
        """
        Methode qui vérifie l'état du jeu pour donner des points aux joueurs
        """
        general_index = 0
        for i, row in enumerate(self.board):
            for j, elt in enumerate(row):
                if elt is not '-':
                    for h in self.inventories:
                        if elt is h.pawn:
                            if j+1 <= len(row):
                                if general_index+1 <= len(self.board):
                                    if self.board[general_index+1] is elt:
                                        self.board[general_index] = '-'
                                        self.board[general_index+1] = '-'
                                        j.score += 10
                general_index += 1

    def valid_moves(self):  # utilisé par les agents
        """
        Methode qui donne sous forme de liste tous les coups jouables possibles
        """
        moves = []  # tous les coups jouables sous forme de liste de nombres
        # On numérote les coups où l'on peut jouer
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board)):
                if (self.check_valid_move((i, j))):
                    moves.append((i, j))

        # print("Coups jouables : " + str(moves))

        return moves

    def check_valid_move(self, choice):
        """
        Methode qui vérifie si le coup est valide
        """
        if type(choice) is list or tuple:
            row, col = int(choice[0]), int(choice[1])
            # print("test : ", row, col)
            if row not in range(self.board_size) or col not in range(self.board_size) or not self.board[row][col] == '-':
                return False
            else:
                return True
        else:
            return False

    def check_current_state(self):  # utilisé par les agents
        """
        Methode qui vérifie l'état du jeu (victoire/défaite/match nul)
        On renvoit un booléen qui représente si le jeu est terminé: true sinon false
        """
        for i in self.inventories:
            if i.score >= 100:
                return True
        return False

    def winner(self):  # utilisé par les agents
        """
        Methode pour récupérer le joueur victorieux
        Si match nul on récupère: "Draw"
        Si le match est toujours en cours on retourne "None"
        """
        if self.check_current_state():
            for i in self.inventories:
                if i.score >= 100:
                    return i.player
        else:
            return None

    def print_game(self):  # utilisé par l'humain et les algorithmes d'apprentissage
        """
        Return the game board as string.
        Représente l'état du jeu pour le reinforcement learning.
        """
        string = str('    ')
        for i in range(self.board_size):
            string += str('%i   ' % i)
        string += str('\n\n')
        for i, row in enumerate(self.board):
            string += str('%i   ' % i)
            for elt in row:
                string += str('%s   ' % elt)
            string += str('\n\n')
        return string

    def print_rules(self):  # utilisé par l'humain
        """
        Return the game rules as string.
        """
        return str("Player1 -> X\nPlayer2 -> O\n\nSélectionnez une ligne et une colonne de 0 à 2 : \n")
