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
        chess_board = ChessBoard(chess_players, time_per_player=15)
        chess_board.initialize()
        print("Tiempo por jugador:", chess_board.time_per_player, "minutos.")
        print("Turno inicial: ", chess_board.turn)
        print("Movimientos realizados: ", chess_board.move_history)
        print("Piezas capturadas: ", chess_board.captured_pieces)
        print("Rey en jaque: ", "Si" if chess_board.is_check else "No")
        print("Jaque mate: ", "Si" if chess_board.is_checkmate else "No")
        print(f"---------------- ")

        solitaire_player = ["María Antonieta"]
        solitaire_board = SolitaireBoard(solitaire_player, difficulty="difícil")
        solitaire_board.initialize()
        print("Dificultad del juego de Solitario: ", solitaire_board.difficulty)
        print("Movimientos máximos: ", solitaire_board.max_moves)
        print("Puntuación actual: ", solitaire_board.current_score)
        print("Movimientos realizados: ", solitaire_board.moves_made)
        print("Cartas restantes: ", solitaire_board.remaining_cards)
        print("Tiempo transcurrido: ", solitaire_board.time_elapsed)



if __name__== "__main__":
    FactoryMethodClient.main()
