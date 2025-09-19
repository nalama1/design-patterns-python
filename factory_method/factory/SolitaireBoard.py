from factory_method.products.SolitaireGame import SolitaireGame
from .Board import Board

class SolitaireBoard(Board):

    def __init__(self, players: list[str], difficulty = "normal"):
        super().__init__(players)

        #inicialización propia de SolitaireBoard
        self.difficulty = difficulty

    def create_game(self):
        players = self.get_players()
        player = "Jugador"

        if self._players is not None and len(self._players) > 0:
            player = players[0]

        game = SolitaireGame(player)
        return game

    """ creador concreto: SolitaireBoard"""
        