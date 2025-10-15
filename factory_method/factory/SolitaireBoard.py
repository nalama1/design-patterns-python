import os
from typing import List, Optional

from factory_method.products.SolitaireGame import SolitaireGame
from factory_method.audit.Logger import Logger
from .Board import Board

class SolitaireBoard(Board):
    """
    Represents a concrete board for the solitaire game.
    It is responsible for creating and registering the game.
    """

    def __init__(
            self,
            players: List[str],
            difficulty:str = "normal",
            max_moves:int = 1000,
            logger: Optional[Logger]=None
    ):
        super().__init__(players)

        self.name_file = __file__
        self.name_base = os.path.basename(self.name_file)

        #SolitaireBoard specific initialization
        self.difficulty = difficulty
        self.max_moves= max_moves
        self.current_score = 0
        self.remaining_cards = 52
        self.time_elapsed = 0
        self.moves_made: List[str] = []

        # Inyection Dependency (DIP)
        self.logger = logger or Logger()

        # Initialization Log
        self.logger.log(f"[INIT] Board initialized: {self.name_base}, difficulty={self.difficulty}")


    def create_game(self)  -> SolitaireGame:
        """
        Creates a solitaire game instance for the first available player.
        Logs the event.
        """
        players = self.get_players() or []
        player = players[0] if players else "Player"

        try:
            game = SolitaireGame(player)
            self.logger.log(f"[CREATE] Solitaire game created for player: {player}")
            return game
        except Exception as e:
            self.logger.log(f"[ERROR] Failed to create Solitaire game: {e}")
            raise

# Concrete creator: SolitaireBoard
        