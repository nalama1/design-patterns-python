import os
from idlelib.query import Query

from .Board import Board
from factory_method.products.ChessGame import ChessGame
from factory_method.audit.Logger import Logger

class ChessBoard(Board):
    # Constantes
    PLAYER_ONE_COLOR = "White"
    PLAYER_TWO_COLOR = "Black"

    def __init__(self, players, time_per_player = 10):
        super().__init__(players)
        self.name_file = __file__
        self.name_base = os.path.basename(self.name_file)
        print(f"[{self.name_base}]")

        #ChessBoard specific initialization
        self.time_per_player = time_per_player
        self.turn = self.PLAYER_ONE_COLOR
        self.move_history = []
        self.captured_pieces = []
        self.is_check = False
        self.is_checkmate = False

    def create_game(self):
        players = self.get_players()
        player_one = self.PLAYER_ONE_COLOR
        player_two = self.PLAYER_ONE_COLOR

        if players is not None and len(players) == 2:
            player_one = players[0]
            player_two = players[1]

        game = ChessGame(player_one, player_two, self.time_per_player)
        game.turn = self.turn
        game.move_history = self.move_history
        game.captured_pieces = self.captured_pieces

        #Logger
        logger = Logger()
        logger.log(f"A chess game with players was created: {player_one} y {player_two}")

        return game

# Concrete creator: ChessBoard
