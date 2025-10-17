import os
from typing import List, Optional

from .Board import Board
from factory_method.products.ChessGame import ChessGame
from factory_method.audit.Logger import Logger

class ChessBoard(Board):
    """
    Represents the concrete board for a game of chess. It is responsible for initializing the state
    of the board and creating the associated game.
    """

    # Player Color Constants
    PLAYER_ONE_COLOR = "White"
    PLAYER_TWO_COLOR = "Black"

    def __init__(
            self,
            players: Optional[List[str]] = None,
            time_per_player: int = 10,
            logger: Optional[Logger] = None,
    ) -> None:
        """
        Initializes an instance of the chest board.
        :param players: list of players (expects 2 elements)
        :param time_per_player: time alloted per player in minutes
        :param logger: injected Logger instance(optional)
        """
        super().__init__(players)

        # Avoid re-declaring name_file/name_base (they already exist in Board)
        self.time_per_player = time_per_player
        self.turn = self.PLAYER_ONE_COLOR
        self.move_history: List[str] = []
        self.captured_pieces: List[str] = []
        self.is_check = False
        self.is_checkmate = False

        # Dependency Injection (DIP)
        self.logger = logger or Logger()

        # Initial Log
        self.logger.log(
            f"[INIT] ChessBoard initialized ({self.name_base}), time_per_player={self.time_per_player} min"
        )

    def create_game(self) -> ChessGame:
        """
        Creates a chess game instance.
        Returns a ChessGame object ready to be initialized
        """
        players = self.get_players() or []
        player_one = players[0] if len(players) > 0 else self.PLAYER_ONE_COLOR
        player_two = players[1] if len(players) > 1 else self.PLAYER_TWO_COLOR

        try:
            game = ChessGame(player_one, player_two, self.time_per_player)

            # Configure game state
            game.turn = self.turn
            game.move_history = list(self.move_history)
            game.captured_pieces = list(self.captured_pieces)

            # Log creation event
            self.logger.log(
                f"[CREATE] Chess game created for {player_one} ({self.PLAYER_ONE_COLOR}) vs {player_two} ({self.PLAYER_TWO_COLOR})"
            )

            return game

        except Exception as e:
            self.logger.log(f"[ERROR] Failed to create ChessGame: {e}")
            raise

# Concrete creator: ChessBoard
