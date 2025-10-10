import datetime
import os
from .Game import Game
from ..audit.Logger import Logger


class SolitaireGame(Game):
    def __init__(self, player):
        self.player = player
        self.name_file = __file__
        self.name_base = os.path.basename(self.name_file)
        self.start_time = datetime.datetime.now()
        self.score = 0
        self.status = "En curso"

        # Registrar en el log
        logger = Logger()
        logger.log(f"Juego iniciado por {self.player} en {self.name_base} a las {self.start_time}")


    def start(self):
        print(f"[{self.name_base}] Jugador {self.player} comienza juego de cartas Solitario")

    """ producto concreto"""