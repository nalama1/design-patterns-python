import os
from typing import List, Optional

from  factory_method.products.Game import Game
from factory_method.audit.ILogger import ILogger
from factory_method.audit.Logger import Logger

class ChessGame(Game):
    """
    Represents a concrete implementation of a Chess Game.
    Inherits from the abstract class/interface Game.
    """

    def __init__(
            self,
            player_one: str,
            player_two: str,
            time_per_player: int,
            player_one_color: str,
            player_two_color: str,
            logger: Optional[ILogger] = None,
            turn: str = "White",
            move_history: Optional[List[str]] = None,
            captured_pieces: Optional[List[str]] = None
    ) -> None:

        super().__init__()

        self.player_one = player_one
        self.player_two = player_two
        self.time_per_player = time_per_player

        # We save the colors obtained from the Board
        self.player_one_color = player_one_color
        self.player_two_color = player_two_color

        #Game state
        self.turn = turn
        self.move_history: List[str] = move_history or []
        self.captured_pieces: List[str] = captured_pieces or []

        #File/Class Attributes
        self.name_file = __file__
        self.name_base = os.path.basename(self.name_file)

        #Dependency Injection for the Logger
        self.logger: ILogger = logger or Logger()
        self.logger.log(f"[INIT] ChessGame initialized for player.")

    def start(self) -> None:
        """
        Implements the abstract start method from the base Game class.
        Starts the game and logs the event.
        """
        message = (
            "-" * 40 + "\n"
            f" Chess Game Started ({self.name_base})\n"
            f" Participants: {self.player_one} ({self.player_one_color}) vs {self.player_two} ({self.player_two_color})\n"
            f" Time per player: {self.time_per_player} minutes.\n" +
            "-" * 40
        )

        print(message)

        self.logger.log(
            f"[START] Chess match started: {self.player_one} ({self.player_one_color})"
            f"vs {self.player_two} ({self.player_two_color})"
        )

# Concrete product: ChessGame
