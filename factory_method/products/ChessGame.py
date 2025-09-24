import os
from .Game import Game

class ChessGame(Game):

    def __init__(self, player_one, player_two, time_per_player):
        self.player_one = player_one
        self.player_two = player_two
        self.name_file = __file__
        self.name_base = os.path.basename(self.name_file)
        self.time_per_player = time_per_player


    def start(self):
        print(f"[{self.name_base}] Jugadores {self.player_one} y {self.player_two} comienza juego de ajedrez")
        print(f"Partida de ajedrez iniciada entre {self.player_one}(blancas) y {self.player_two}(negras)")

    """ producto concreto: ChessGame"""