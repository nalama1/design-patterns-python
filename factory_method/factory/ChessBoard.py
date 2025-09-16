from .Board import Board
from factory_method.products.ChessGame import ChessGame

class ChessBoard(Board):
    def __init__(self, players):
        super().__init__(players)

    def create_game(self):
        players = self.get_players()
        player_one = "Blanco"
        player_two = "Negro"

        if players is not None and len(players) == 2:
            player_one = players[0]
            player_two = players[1]

        game = ChessGame(player_one, player_two)
        return game
