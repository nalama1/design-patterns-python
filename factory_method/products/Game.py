from abc import ABC, abstractmethod
from typing import Optional
from factory_method.audit.Logger import Logger

class Game(ABC):
    """
    Abstract base class representing a generic game.
    Defines the common interface that all concrete games must implement.
    """
    def __init__(
            self,
            player: Optional[str]= None,
            logger: Optional[Logger] = None
    ) -> None:
        # Common properties for all games
        self.player = player or "Player"
        self.is_started = False

        #Dependency Injection for logging
        self.logger = logger or Logger()
        self.logger.log(
            f"[INIT] Game base initialized for player: {self.player}"
        )

    @abstractmethod
    def start(self) -> None:
        """
        Starts the game. Must be implemented by subclasses.
        """
        pass