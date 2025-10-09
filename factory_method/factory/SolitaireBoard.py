import os
from factory_method.products.SolitaireGame import SolitaireGame
from .Board import Board
from factory_method.audit.Logger import Logger

class SolitaireBoard(Board):

    def __init__(self, players: list[str], difficulty = "normal", max_moves = 1000):
        super().__init__(players)
        self.name_file = __file__
        self.name_base = os.path.basename(self.name_file)
        print(f"[{self.name_base}]")

        #SolitaireBoard specific initialization
        self.difficulty = difficulty
        self.max_moves= max_moves
        self.current_score = 0
        self.remaining_cards = 52
        self.time_elapsed = 0
        self.moves_made = []


    def create_game(self):
        players = self.get_players()
        player = "Player"

        if self._players is not None and len(self._players) > 0:
            player = players[0]

        game = SolitaireGame(player)

        logger = Logger()
        logger.log(f"A Solitaire game with a player was created: {player}")

        return game

    """ Concrete creator: SolitaireBoard"""
        