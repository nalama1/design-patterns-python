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
        print("Parámetro 'time_per_player' (tiempo asignado por jugador)", chess_board.time_per_player, "minutos.")
        print("Atributo 'turn': Turno inicial ", chess_board.turn)
        print("Registro: Jugadas realizadas ", chess_board.move_history)
        print("Colección: Piezas capturadas ", chess_board.captured_pieces)
        print("Booleano 'is_check': Rey en jaque mate ", "Si" if chess_board.is_check else "No")
        print("Booleano 'is_checkmate': Jaque mate ", "Si" if chess_board.is_checkmate else "No")
        print(f"---------------- ")

        solitaire_player = ["María Antonieta"]
        solitaire_board = SolitaireBoard(solitaire_player, difficulty="hard")
        solitaire_board.initialize()
        print("Parámetro 'difficulty': Dificultad de juego Solitario ", solitaire_board.difficulty)
        print("Límite 'max_moves': Movimientos máximos ", solitaire_board.max_moves)
        print("Variable 'current_score': Puntaje actual ", solitaire_board.current_score)
        print("Contador 'moves_made': Movimientos realizados ", solitaire_board.moves_made)
        print("Conjunto 'remaining_cards': Cartas restantes ", solitaire_board.remaining_cards)
        print("Métrica 'time_elapsed': Tiempo transcurrido ", solitaire_board.time_elapsed)



if __name__== "__main__":
    FactoryMethodClient.main()
