import datetime
import os
from typing import  Optional

from .Game import Game
from factory_method.audit.ILogger import ILogger
from factory_method.audit.Logger import Logger


class SolitaireGame(Game):
    """ Represents a concrete implementation of a Solitaire game.
        Inherits from the abstract class/interface game and logs events.
    """

    def __init__(
            self,
            player:str,
            logger: Optional[ILogger] = None
    ) -> None:
        if not player.strip():
            raise ValueError("The player name cannot be empty")

        super().__init__()

        self.player = player
        self.name_file = __file__
        self.name_base = os.path.basename(self.name_file)
        self.start_time: datetime.datetime = datetime.datetime.now()
        self.status: str = "Initialized"
        self.score: int = 0

        # Dependency Injection (DIP)
        self._logger: ILogger = logger or Logger()
        self._logger.log(
            f"[INIT] Game created for player '{self.player}' in {self.name_base}"
            f" at {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}"
        )

    def start(self) -> None:
        """
        Starts the game, updates the status, and logs the event.
        """
        self.status = "In Progress"
        self.start_time = datetime.datetime.now()

        self._logger.log(
            f"[START] Solitaire Game started by {self.player} at {self.start_time.strftime('%Y-%m-%d %H:%M:%S')} "
        )

    def end(self, final_score: int) -> None:
        """
        Ends the game, saves the final score, and logs the event
        """
        self.status = "Finished"
        self.score = final_score
        end_time = datetime.datetime.now()

        self._logger.log(
            f"[END] Game finished by '{self.player}' with score {self.score} at {end_time.strftime('%Y-%m-%d %H:%M:%S')} "
        )


# Concrete product: SolitaireGame


