import os
from .Game import Game

class ChessGame(Game):
    """
    Represents a concrete implementation of a Chess Game.
    Inherits from the abstract class/interface Game.
    """

    # Constantes
    PLAYER_ONE_COLOR = "White"
    PLAYER_TWO_COLOR = "Black"

    def __init__(self, player_one, player_two, time_per_player):
        self.player_one = player_one
        self.player_two = player_two
        self.name_file = __file__
        self.name_base = os.path.basename(self.name_file)
        self.time_per_player = time_per_player

    def start(self):
        print("-" * 30)
        print(f" Chess Game Started!")
        print(f"Participants: {self.player_one} ({self.PLAYER_ONE_COLOR}) vs {self.player_two} ({self.PLAYER_TWO_COLOR}) ")
        print(f"Time per player: {self.time_per_player} minutes.")
        print(f"[{self.name_base}] Players {self.player_one} and {self.player_two} start chess game")
        print(f"Chess match started between {self.player_one}({self.PLAYER_ONE_COLOR}) and {self.player_two}({self.PLAYER_TWO_COLOR})")
        print("-" * 30)

# Concrete product: ChessGame
