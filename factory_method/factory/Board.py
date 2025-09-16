from abc import ABC, abstractmethod
from factory_method.products.Game import Game

class Board(ABC):
    def __init__(self, players):
        self._game:Game | None = None
        self._players = players

    @abstractmethod
    def create_game(self):
        pass

    def initialize(self):
        self._game = self.create_game()
        self._game.start()

    def get_players(self):
        return self._players