import datetime
import os
from .Game import Game
from ..audit.Logger import Logger


class SolitaireGame(Game):
    """ Representa una implementación concreta de un juego de Solitario.
        Hereda de la clase abstracta/interfaz Game y registra eventos.
    """
    def __init__(self, player:str):
        self.player = player
        self.name_file = __file__
        self.name_base = os.path.basename(self.name_file)
        self.start_time: datetime.datetime = datetime.datetime.now()

        # Atributos de estado
        self.score: int = 0
        self.status = "No iniciado"

        # Inicialización de Logger
        self._logger = Logger()

        # Registro inicial
        self._logger.log(f"Game started by {self.player} in {self.name_base} at {self.start_time}")


    def start(self) -> None:
        """ Inicia el juego, actualiza el estado y registra el evento"""
        self.status = "En curso"
        self.start_time = datetime.datetime.now()

        print("-" * 40)
        print(f" El juego de Solitario ha comenzado")
        print(f"Jugador: {self.player}")
        print("-" * 40)

        self._logger.log(
            f"Juego de Solitario INICIADO por {self.player}. Tiempo: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}")


# Concrete product: SolitaireGame