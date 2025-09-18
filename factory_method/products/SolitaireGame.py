from .Game import Game

class SolitaireGame(Game):
    def __init__(self, player):
        self.player = player

    def start(self):
        print(f"Jugador {self.player} comienza juego de cartas Solitario")

    """ producto concreto"""