import os
from .Game import Game

class ChessGame(Game):

    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two
        self.name_file = __file__
        self.name_base = os.path.basename(self.name_file)


    def start(self):
        print(f"[{self.name_base}] Jugadores {self.player_one} y {self.player_two} comienza juego de ajedrez")

    """ producto concreto: ChessGame"""