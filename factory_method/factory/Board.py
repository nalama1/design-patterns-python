import os
from abc import ABC, abstractmethod
from typing import List, Optional

from factory_method.products.Game import Game

class Board(ABC):
    """
    Base (abstract) class for game boards. Responsabilities:
    * Maintain the list of players
    * Orchestrate the creation and initialization of the concrete Game instance Concrete
    implementations must provide cerate_game().
    """

    def __init__(self, players: Optional[List[str]] = None) -> None:
        """
        :param players: list of player names (optional)
        """
        self._game: Optional[Game] = None
        # Normalize players to an empty list if None is passed
        self._players: List[str] = list(players or [])
        self.name_file = __file__
        self.name_base = os.path.basename(self.name_file)

    @abstractmethod
    def create_game(self) -> Game:
        """
        Must be implemented by the subclasses to return a Game instance.
        :return: Game instance (not None)
        """
        raise NotImplementedError

    def initialize(self) -> None:
        """
        Orchestrates the creation and start of the game. Validates that there are players
        before creating the game. Raises exceptions in case of error for the caller to handle.
        """
        if not self._players:
            raise ValueError("No players provided to initialize the board.")

        self._game = self.create_game()
        if self._game is None:
            raise RuntimeError("create_game returned None")

        # We attempt to start the game; if it fails, we let the exception up
        self._game.start()

    def get_players(self) -> List[str]:
        """Returns a copy of the list of players to prevent external mutations."""
        return list(self._players)

    def set_players(self, players: List[str]) -> None:
        """Replaces the list of players with basic validation."""
        if players is None:
            raise ValueError("players must be a list, not None")
        if not isinstance(players, list):
            raise TypeError("players must be a list of strings")
        self._players = list(players)

    def get_game(self) -> Optional[Game]:
        """Returns the created Game instance or None if it has not been created yet"""
        return self._game

# Control Panel: Board