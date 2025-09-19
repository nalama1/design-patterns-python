import os
from .Game import Game

class SolitaireGame(Game):
    def __init__(self, player):
        self.player = player
        self.name_file = __file__
        self.name_base = os.path.basename(self.name_file)

    def start(self):
        print(f"[{self.name_base}] Jugador {self.player} comienza juego de cartas Solitario")

    """ producto concreto: SolitaireGame"""