import os
from .Board import Board
from factory_method.products.ChessGame import ChessGame
from factory_method.factory.Logger import Logger

class ChessBoard(Board):
    def __init__(self, players, time_per_player = 10):
        super().__init__(players)
        self.name_file = __file__
        self.name_base = os.path.basename(self.name_file)
        print(f"[{self.name_base}]")

        #inicialización propia de ChessBoard
        self.time_per_player = time_per_player
        self.turn = "white"

    def create_game(self):
        players = self.get_players()
        player_one = "Blanco"
        player_two = "Negro"

        if players is not None and len(players) == 2:
            player_one = players[0]
            player_two = players[1]

        game = ChessGame(player_one, player_two, self.time_per_player)

        #Logger
        logger = Logger()
        logger.log(f"Se creó un juego de ajedrez con jugadores: {player_one} y {player_two}")

        return game

    """ creador concreto: ChessBoard"""
