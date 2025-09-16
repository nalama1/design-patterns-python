from .Game import Game

class ChessGame(Game):
    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two

    def start(self):
        print("Juego de ajedrez")