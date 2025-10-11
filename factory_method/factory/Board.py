import os
from abc import ABC, abstractmethod
from factory_method.products.Game import Game

class Board(ABC):
    def __init__(self, players):
        self._game:Game | None = None
        self._players = players
        self.name_file = __file__
        self.name_base = os.path.basename(self.name_file)
        print(f"[{self.name_base}]")

    @abstractmethod
    def create_game(self):
        pass

    def initialize(self):
        self._game = self.create_game()
        self._game.start()

    def get_players(self):
        return self._players

# Control Panel: Board