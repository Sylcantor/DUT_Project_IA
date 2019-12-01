
from copy import deepcopy
from collections import deque


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

    def create_tree(self, currentgame, currentplayer='Bot'):
        """
        Méthode pour créer un arbre de jeu en fonction de l'état du jeu.
        On fait plein de parties dans cette méthode.
        Return une liste
        """
        # pour ne pas mélanger les variables current : c'est le jeu réel
        game = currentgame
        player = currentplayer

        # La liste à return
        game_tree = []

        primary_key = 0

        # chaque noeud contient son jeu, le joueur qui a joué
        currentnode = [game, player, primary_key, primary_key]

        # la queue, on ititialise la file avec l'état du jeu et le joueur qui joue
        queue = deque()

        queue.append(currentnode)
        game_tree.append(currentnode)

        while len(queue) != 0:  # while is not empty

            currentnode = queue.pop()

            game = currentnode[0]
            player = currentnode[1]
            parent_key = currentnode[2]

            constructingnode = []  # the next node

            # Si c'est une feuille: on return la valeur de victoire ou défaite
            winner_loser, done = game.check_current_state()
            if done == True or done == "Draw":

                primary_key += 1

                constructingnode = [game, player, primary_key, parent_key,
                                    self.create_leaf(game)]
                print("leaf : " + str(constructingnode))
                game_tree.append(constructingnode)
                continue  # skip over the part of the loop

            moves = []
            empty_cells = []

            # On numérote les coups où l'on peut jouer (pas vides)
            for i in range(game.minimal_move(), game.current_state() + 1):  # l'état actuel du jeu
                if game.check_valid_move(i) == True:
                    empty_cells.append(i)
            print("empty_cells " + str(empty_cells))

            # Jeux imaginaires
            for empty_cell in [x for x in empty_cells if x not in game.invalid_moves()]:

                print("empty_cell " + str(empty_cell))

                primary_key += 1

                copy_game = deepcopy(game)  # on copie le jeu
                # on fait le coup sur cette copie de jeu
                copy_game.play_move(empty_cell, player)

                # Si c'est à l'IA de jouer.
                if player == self.players[1]:  # == O
                    # make more depth tree for human
                    constructingnode = [copy_game,
                                        self.players[0], primary_key, parent_key]
                    print("constructed node : " + str(constructingnode))
                    queue.append(constructingnode)

                # Si c'est à l'humain de jouer.
                if player == self.players[0]:  # == X
                    # make more depth tree for AI
                    constructingnode = [copy_game,
                                        self.players[1], primary_key, parent_key]
                    print("constructed node : " + str(constructingnode))
                    queue.append(constructingnode)

                game_tree.append(constructingnode)

        # while not queue.empty():
         #   game_tree.append(queue.pop())

        # try:
        # self.create_node_game_board(self.state, self.players[0])
        # except NameError:
        # self.create_node(state, currentplayer)

        print("___ FINAL TREE ___")
        print(game_tree)

        return game_tree

    def create_leaf(self, game):
        """
        Return the value of a leaf
        """

        # Si c'est des feuilles: on return la valeur de victoires ou défaite
        winner_loser, done = game.check_current_state()

        # Si le jeu est fini et que l'IA a gagné.
        if done == True and winner_loser == self.players[0]:  # Humain X
            return self.win_value
        # Si le jeu est fini et que l'IA a perdu.
        elif done == True and winner_loser == self.players[1]:  # IA O
            return self.loss_value
        # Si le jeu est fini et que personne n'a gagné.
        elif done == "Draw":
            return 0

    def create_node(self, game, player):
        """
        Méthode pour faire un noeud de l'arbre.
        On joue une partie dans cette méthode.
        Return un noeud
        """

        # Si c'est des feuilles: on return la valeur de victoires ou défaite
        winner_loser, done = game.check_current_state()
        if done == True or done == "Draw":
            self.create_leaf(game, player)

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
