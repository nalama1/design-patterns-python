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
        self.status = "In progress"

        # Record in the log
        logger = Logger()
        logger.log(f"Game started by {self.player} in {self.name_base} at {self.start_time}")


    def start(self):
        print(f"[{self.name_base}] Player {self.player} starts Solitaire card game")

    """ Concrete product: SolitaireGame"""