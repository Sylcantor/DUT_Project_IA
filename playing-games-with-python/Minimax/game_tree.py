
from copy import deepcopy


class GameTree:
    # init pour un jeu avec et sans plateau
    def __init__(self, game, check_playable=None, win_value=10, loss_value=-10, players=['Human', 'Bot']):
        # X = Human
        # O = Bot
        """
        On doit avoir: l'état du jeu, la méthode pour jouer, la méthode pour copier le plateau, et la méthode pour vérifier l'état du jeu
        """
        self.game = game

        self.check_playable = check_playable
        self.win_value = win_value
        self.loss_value = loss_value
        self.players = players
        return

    # TODO Mettre en pratique le code

    @classmethod
    def from_board(cls, game, check_playable=" ", win_value=10, loss_value=-10, players=['Human', 'Bot']):
        """
        Constructeur pour les jeux plateau
        """
        g = GameTree(game, None, win_value, loss_value, players)

        g.check_playable = check_playable

        boardSample = g.current_state
        self.boardSizeX = len(boardSample)
        self.boardSizeY = map(len, boardSample)

        return g

    def create_tree(self, game, currentplayer):
        """
        Méthode pour créer un arbre de jeu en fonction de l'état du jeu.
        On fait plein de parties dans cette méthode.
        Return une liste
        """

        self.game = game
        state = game.current_state()

        # Nested List
        game_tree = []

        # try:
        # self.create_node_game_board(self.state, self.players[0])
        # except NameError:
        self.create_node(state, currentplayer)

        return game_tree

    def create_node(self, state, player):
        """
        Méthode pour faire un noeud de l'arbre.
        On joue une partie dans cette méthode.
        Return un noeud
        """

        winner_loser, done = self.game.check_current_state()

    # Si c'est des feuilles: on return la valeur de victoires ou défaite

        # Si le jeu est fini et que l'IA a gagné.
        if done == True and winner_loser == self.players[0]:  # Humain X
            return win_value
        # Si le jeu est fini et que l'IA a perdu.
        elif done == True and winner_loser == self.players[1]:  # IA O
            return loss_value
        # Si le jeu est fini et que personne n'a gagné.
        elif done == "Draw":
            return 0

        moves = []
        empty_cells = []

    # On numérote les coups où l'on peut jouer (pas vides)
        for i in range(state):
            if self.game.check_valide_move(i) == True:
                empty_cells.append(i)

    # Jeux imaginaires
        for empty_cell in empty_cells:
            move = {}
            move['index'] = empty_cell

            # FIXME
            copy_game = deepcopy(self.game)
            new_state = copy_game.current_state()
            copy_game.play_move(empty_cell, player)

            # Si c'est à l'IA de jouer.
            if player == self.players[1]:  # == O
                # make more depth tree for human
                result = self.create_node(new_state, self.players[0])
                move['score'] = result
            # Si c'est à l'humain de jouer.
            else:  # == X
                # make more depth tree for AI
                result = self.create_node(new_state, self.players[1])
                move['score'] = result

            moves.append(move)

    def create_node_game_board(self, state, player):
        """
        Méthode pour faire un noeud de l'arbre.
        On joue une partie dans cette méthode.
        Return un noeud
        """

        winner_loser, done = self.check_current_state.upper(state)

    # Si c'est des feuilles: on return la valeur de victoires ou défaite

        # Si le jeu est fini et que l'IA a gagné.
        if done == "Done" and winner_loser == players[0]:  # Humain X
            return win_value
        # Si le jeu est fini et que l'IA a perdu.
        elif done == "Done" and winner_loser == players[1]:  # IA O
            return loss_value
        # Si le jeu est fini et que personne n'a gagné.
        elif done == "Draw":
            return 0

        moves = []
        empty_cells = []

    # On numérote les cases où l'on peut jouer (pas vides)
        for i in range(self.boardSizeX):
            for j in range(self.boardSizeY):
                if state[i][j] is self.check_playable:  # empty / playable
                    empty_cells.append(i*self.boardSizeX + (j+1))

    # Jeux imaginaires
        for empty_cell in empty_cells:
            move = {}
            move['index'] = empty_cell
            new_state = self.copy_game_state.upper(state)
            self.play_move.upper(new_state, player, empty_cell)

            # Si c'est à l'IA de jouer.
            if player == players[1]:  # == O
                # make more depth tree for human
                result = create_node_game_board(new_state, players[0])
                move['score'] = result
            # Si c'est à l'humain de jouer.
            else:  # == X
                # make more depth tree for AI
                result = create_node_game_board(new_state, players[1])
                move['score'] = result

            moves.append(move)
