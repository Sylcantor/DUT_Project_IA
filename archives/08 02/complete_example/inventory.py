class Inventory:
    """
    Classe qui permet de caractériser chaque joueur. Elle lie aussi les joueurs à
    leurs objets durant la partie (son score, son nombre de coups possibles, son pion).
    """

    # l'inventaire du joueur
    def __init__(self, player, moves):
        self.player = player
        self.moves = moves
        self.pawn = player[-1]  # le pion du joueur
        self.score = 0

    def __repr__(self):
        """
        Pour récupérer un inventaire, si on fait Inventory(...) on récupère tout ça:
        """
        return str((object.__repr__(self), self.player, self.moves, self.score))[1:-1]
