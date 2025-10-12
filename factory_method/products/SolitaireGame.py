import datetime
import os
from .Game import Game
from ..audit.Logger import Logger


class SolitaireGame(Game):
    """ Represents a concrete implementation of a Solitaire game.
        Inherits from the abstract class/interface game and logs events.
    """
    def __init__(self, player:str):
        self.player = player
        self.name_file = __file__
        self.name_base = os.path.basename(self.name_file)
        self.start_time: datetime.datetime = datetime.datetime.now()

        # State attributes
        self.score: int = 0
        self.status: str = "In progress"

        # Logger initialization
        self._logger = Logger()

        # Initial log entry
        self._logger.log(
            f"Game started by {self.player} in {self.name_base} at {self.start_time}"
        )

    def start(self) -> None:
        """ Starts the game, updates the status, and logs the event."""
        self.status = "In Progress"
        self.start_time = datetime.datetime.now()

        print("-" * 40)
        print(f"Solitaire game has begun!")
        print(f"Player: {self.player}")
        print("-" * 40)

        self._logger.log(
            f"Solitaire Game STARTED by {self.player}. Time: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')} "
        )

# Concrete product: SolitaireGame