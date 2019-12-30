import random

from Jeux.AbstractJeu import AbstractJeu

class TicTacToe(AbstractJeu):
    """ The game class. New instance created for each new game. """
    """
    Player1 -> 'X'
    Player2 -> 'O'
    """

    def __init__(self, players=['Player1', 'Player2']):
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
                                      # le plateau
        self.players = players        # liste des joueurs
        self.currentplayer = None     # caractérise le dernier joueur qui a joué
        return

    def play_move(self, choice, currentplayer):
        """
        Methode pour jouer au jeu
        """
        self.currentplayer = currentplayer
        if choice in self.valid_moves():        # vérification supplémentaire mais normalement c'est forcément vrai
                                                # si on choisit un move parmis les valid_moves()
            row, col = int(choice[0]), int(choice[1])

            if self.currentplayer == self.players[0]:
                self.board[row][col] = 'X'
            else: 
                self.board[row][col] = 'O'
        # print("test : ", self.board)
                
    def valid_moves(self):  # utilisé par minmax
        """
        Methode qui donne sous forme de liste tous les coups jouables possibles
        """
        moves = [
        ]  # tous les coups jouables sous forme de liste de nombres
        # On numérote les coups où l'on peut jouer           
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board)):
                if (self.check_valid_move((i,j))):
                    moves.append((i,j))

        # print("Coups jouables : " + str(moves))

        return moves

    def check_valid_move(self, choice):
        """
        Methode qui vérifie si le coup est valide
        """
        if type(choice) is list or tuple:
            row, col = int(choice[0]), int(choice[1])
            # print("test : ", row, col)
            if row not in range(3) or col not in range(3) or not self.board[row][col] == '-':
                return False
            else:
                return True
        else:
            return False
        
    def check_current_state(self):
        """
        Methode qui vérifie l'état du jeu (victoire/défaite/match nul)
        On renvoit un booléen qui représente si le jeu est terminé: true sinon false
        """
        if self.currentplayer == self.players[0]:
            key = 'X'
        else:
            key = 'O'
        
        if self.checkForWin(key):
            return True
        elif self.checkForDraw():
            return True
        return False

    def winner(self):  # utilisé par minmax
        """
        Methode pour récupérer le joueur victorieux
        Si match nul on récupère: "Draw"
        """
        if self.check_current_state():
            if self.currentplayer == self.players[0]:
                key = 'X'
            else:
                key = 'O'
            
            if self.checkForWin(key):
                
                    if key == 'X':
                        # print("Player wins!")
                        return self.players[0]
                    else:
                        # print("RL agent wins!")
                        return self.players[1]
            elif self.checkForDraw():
                
                    # print("It's a draw!")
                    return "Draw"
        else:
            return None

    def checkForWin(self, key):
        """
        Check to see whether the player/agent with token 'key' has won.
        Returns a boolean holding truth value.

        Parameters
        ----------
        key : string
            token of most recent player. Either 'O' or 'X'
        """
        # check for player win on diagonals
        a = [self.board[0][0], self.board[1][1], self.board[2][2]]
        b = [self.board[0][2], self.board[1][1], self.board[2][0]]
        if a.count(key) == 3 or b.count(key) == 3:
            return True
        # check for player win on rows/columns
        for i in range(3):
            col = [self.board[0][i], self.board[1][i], self.board[2][i]]
            row = [self.board[i][0], self.board[i][1], self.board[i][2]]
            if col.count(key) == 3 or row.count(key) == 3:
                return True
        return False

    def checkForDraw(self):
        """
        Check to see whether the game has ended in a draw. Returns a
        boolean holding truth value.
        """
        draw = True
        for row in self.board:
            for elt in row:
                if elt == '-':
                    draw = False
        return draw

    def print_game(self):
        """
        Return the game board as string.
        """   
        string = str('    0   1   2')   
        string += str('\n\n')      
        for i, row in enumerate(self.board):
            string += str('%i   ' % i)
            for elt in row:
                string += str('%s   ' % elt)
            string += str('\n\n')
        return string
    
    def print_rules(self):
        """
        Return the game rules as string.
        """ 
        return str("Player1 -> X\nPlayer2 -> O\n\nSélectionnez une ligne et une colonne de 0 à 2 : \n")
        
            
    # ────────────────────────────────────────────────────────────────────────────────

    def getStateKey(self, board):
        """
        Converts 2D list representing the board state into a string key
        for that state. Keys are used for Q-value hashing.

        Parameters
        ----------
        board : list of lists
            the current game board
        """
        key = ''
        for row in board:
            for elt in row:
                key += elt
        return key
        
    def checkForEnd(self, key):
        """
        Checks if player/agent with token 'key' has ended the game. Returns -1
        if the game is still going, 0 if it is a draw, and 1 if the player/agent
        has won.

        Parameters
        ----------
        key : string
            token of most recent player. Either 'O' or 'X'
        """
        if self.checkForWin(key):
            return 1
        elif self.checkForDraw():
            return 0
        return -1

