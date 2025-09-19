import sys
import os
from factory_method.factory.ChessBoard import ChessBoard
from factory_method.factory.SolitaireBoard import SolitaireBoard

class FactoryMethodClient:
    name_file = sys.argv[0]
    name_base = os.path.basename(name_file)
    print(f"Inicia ejecución desde:")
    print({name_base})

    @staticmethod
    def main():
        chess_players = ["Ana Castle", "Pedro Rock"]
        chess_board = ChessBoard(chess_players)
        chess_board.initialize()
        print(f"---------------- ")

        solitaire_player = ["María Antonieta"]
        solitaire_board = SolitaireBoard(solitaire_player, difficulty="hard")
        solitaire_board.initialize()
        print("Dificultad de juego Solitario: ", solitaire_board.difficulty)
        print("Movimientos máximos: ", solitaire_board.max_moves)

if __name__== "__main__":
    FactoryMethodClient.main()
