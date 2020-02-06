class Player:

    def __init__(self, player, agent, prev_state=None, prev_action=None):
        self.player = player
        self.agent = agent
        self.prev_state = prev_state
        self.prev_action = prev_action

    def __repr__(self):
        """
        Pour récupérer un joueur, si on fait Player(...) on récupère tout ça:
        """
        return str((object.__repr__(self), self.name, self.agent, self.prev_state, self.prev_action))[1:-1]
