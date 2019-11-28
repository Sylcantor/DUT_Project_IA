
class GameTree:
    def __init__(self, state, play_move, copy_game_state, check_current_state, check_playable=" ", win_value=10, loss_value=-loss_value, players=['Human', 'Bot']):
        # X = Human
        # O = Bot
        """
        On doit avoir: l'état du jeu, la méthode pour jouer, la méthode pour copier le plateau, et la méthode pour vérifier l'état du jeu
        """
        self.state = state

        self.play_move = play_move
        self.copy_game_state = copy_game_state
        self.check_current_state = check_current_state

        boardSample = check_current_state.upper(state)
        self.boardSizeX = len(boardSample)
        self.boardSizeY = map(len, boardSample)

        self.check_playable = check_playable
        self.win_value = win_value
        self.loss_value = loss_value
        self.players = players
        return

    # TODO Finir l'arbre et les noeuds

    def create_tree(self):
        """
        Méthode pour créer un arbre de jeu en fonction de l'état du jeu.
        On fait plein de parties dans cette méthode.
        Return une liste
        """
        # self.play_move.upper()            # play_move(state, player, block_num)
        # self.copy_game_state.upper()      # copy_game_state(state)
        # self.check_current_state.upper()  # check_current_state(game_state)

        # Nested List
        game_tree = []

        game_tree.append(create_node(self.state, players[0]))

        return game_tree

    def create_node(self, state, player):
        """
        Méthode pour faire un noeud de l'arbre.
        On joue une partie dans cette méthode.
        Return un noeud
        """

        winner_loser, done = self.check_current_state.upper(state)

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
                    empty_cells.append(i*3 + (j+1))

    # Jeux imaginaires
        for empty_cell in empty_cells:
            move = {}
            move['index'] = empty_cell
            new_state = self.copy_game_state.upper(state)
            self.play_move.upper(new_state, player, empty_cell)

            # Si c'est à l'IA de jouer.
            if player == 'O':
                # make more depth tree for human
                result = create_node(new_state, players[0])
                move['score'] = result
            # Si c'est à l'humain de jouer.
            else:
                # make more depth tree for AI
                result = create_node(new_state, players[1])
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
                        print("IA", "score", best,
                              "index", move['index'], "\n")
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
                        print("Humain", "score", best,
                              "index", move['index'], "\n")
                    # On récupère l'index de la pire case pour l'humain.
                    best_move = move['index']

        return best_move
