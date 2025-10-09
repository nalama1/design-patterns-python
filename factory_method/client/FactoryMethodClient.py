import sys
import os
from factory_method.factory.ChessBoard import ChessBoard
from factory_method.factory.SolitaireBoard import SolitaireBoard

class FactoryMethodClient:
    name_file = sys.argv[0]
    name_base = os.path.basename(name_file)
    print(f"Execution starts from:")
    print({name_base})

    @staticmethod
    def main():
        chess_players = ["Ana Castle", "Pedro Rock"]
        chess_board = ChessBoard(chess_players, time_per_player=15)
        chess_board.initialize()
        print("Timer per player:", chess_board.time_per_player, "minutes.")
        print("Initial turn: ", chess_board.turn)
        print("Moves made: ", chess_board.move_history)
        print("Captured pieces: ", chess_board.captured_pieces)
        print("King in check: ", "Yes" if chess_board.is_check else "No")
        print("Checkmate: ", "Yes" if chess_board.is_checkmate else "No")
        print(f"---------------- ")

        solitaire_player = ["María Antonieta"]
        solitaire_board = SolitaireBoard(solitaire_player, difficulty="hard")
        solitaire_board.initialize()
        print("Solitaire game difficulty: ", solitaire_board.difficulty)
        print("Maximum moves: ", solitaire_board.max_moves)
        print("Current score: ", solitaire_board.current_score)
        print("Moves made: ", solitaire_board.moves_made)
        print("Remaining cards: ", solitaire_board.remaining_cards)
        print("Time elapsed: ", solitaire_board.time_elapsed)



if __name__== "__main__":
    FactoryMethodClient.main()
