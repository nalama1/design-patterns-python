import sys
import os
from factory_method.factory.ChessBoard import ChessBoard
from factory_method.factory.SolitaireBoard import SolitaireBoard

class FactoryMethodClient:
    """
    Entry point to demonstrate the use of the Factory Method pattern
    with the ChessBoard and SolitaireBoard classes.
    """

    def __init__(self):
        self._print_execution_source()

    @staticmethod
    def _print_execution_source():
        """ Shows the name of the file from which execution starts."""
        name_file = sys.argv[0]
        name_base = os.path.basename(name_file)
        print(f"Execution starts from: {name_base}")
        print("-" * 50)

    @staticmethod
    def _run_chess_demo():
        """ Demonstration of the chess board's functionality"""
        print(" Starting Chess Game Demo...\n")

        chess_players = ["Ana Castle", "Pedro Rock"]
        chess_board = ChessBoard(chess_players, time_per_player=15)
        chess_board.initialize()

        print(f"Timer per player: {chess_board.time_per_player} minutes.")
        print(f"Initial turn: {chess_board.turn} ")
        print(f"Moves made: {chess_board.move_history} ")
        print(f"Captured pieces: {chess_board.captured_pieces} ")
        print(f"King in check: {"Yes" if chess_board.is_check else "No"} ")
        print(f"Checkmate: { "Yes" if chess_board.is_checkmate else "No"}")
        print(f"-" * 50)

    @staticmethod
    def _run_solitaire_demo():
        """Demonstration of the solitaire board's functionality."""
        print(" Starting Solitaire Game Demo...\n")

        solitaire_player = ["María Antonieta"]
        solitaire_board = SolitaireBoard(solitaire_player, difficulty="hard")
        solitaire_board.initialize()

        print(f"Solitaire game difficulty: {solitaire_board.difficulty}")
        print(f"Maximum moves: {solitaire_board.max_moves}")
        print(f"Current score: {solitaire_board.current_score}")
        print(f"Moves made: {solitaire_board.moves_made}")
        print(f"Remaining cards: ", solitaire_board.remaining_cards)
        print(f"Time elapsed: ", solitaire_board.time_elapsed)
        print(f"-" * 50)

    @classmethod
    def _prompt_user_choice(cls):
        """ Asks the user which demo they want to run"""
        print("\nSelect an option:")
        print("1. Run Chess Game Demo")
        print("2. Run Solitaire Game Demo")
        print("3. Run Both Demos")
        print("0. Exit")

        choice = input("\nEnter your choice (1/2/3/0): ").strip()
        return choice

    @classmethod
    def main(cls):
        """Main method of the program."""
        client = cls()

        while True:
            choice = cls._prompt_user_choice()

            if choice == "1":
                client._run_chess_demo()
            elif choice == "2":
                client._run_solitaire_demo()
            elif choice == "3":
                client._run_chess_demo()
                client._run_solitaire_demo()
            elif choice == "0":
                print("\n Exiting program. \n")
                break
            else:
                print("\n Invalid option. Please enter 1,2,3, or 0. \n")

if __name__== "__main__":
    FactoryMethodClient.main()

# client