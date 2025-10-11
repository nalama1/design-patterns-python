import os
from .Game import Game

class ChessGame(Game):
    """
    Representa una implementación concreta de un juego de Ajedrez.
    Hereda de la clase abstracta/interfaz Game.
    """

    # Constantes
    PLAYER_ONE_COLOR = "Blancas"
    PLAYER_TWO_COLOR = "Negras"

    def __init__(self, player_one, player_two, time_per_player):
        self.player_one = player_one
        self.player_two = player_two
        self.name_file = __file__
        self.name_base = os.path.basename(self.name_file)
        self.time_per_player = time_per_player

    def start(self):
        print("-" * 50)
        print(f" Juego de Ajedrez Iniciado!")
        print(f"Participantes: {self.player_one} ({self.PLAYER_ONE_COLOR}) vs {self.player_two} ({self.PLAYER_TWO_COLOR}) ")
        print(f"Tiempo por jugador: {self.time_per_player} minutos.")
        print(f"[{self.name_base}] Players {self.player_one} and {self.player_two} start chess game")
        print(f"Chess match started between {self.player_one}(White) and {self.player_two}(Black)")
        print("-" * 50)

    """ Concrete product: ChessGame"""
