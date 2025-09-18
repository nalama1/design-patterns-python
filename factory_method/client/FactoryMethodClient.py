from factory_method.factory.ChessBoard import ChessBoard
from factory_method.factory.SolitaireBoard import SolitaireBoard

class FactoryMethodClient:
    @staticmethod
    def main():
        chess_players = ["Ana Castle", "Pedro Rock"]
        chess_board = ChessBoard(chess_players)
        chess_board.initialize()
        print(f"Los jugadores son: {chess_players} ")

        solitaire_player = ["María Antonieta"]
        solitaire_board = SolitaireBoard(solitaire_player, difficulty="hard")
        solitaire_board.initialize()
        print("Dificultad de juego: ", solitaire_board.difficulty)

if __name__== "__main__":
    FactoryMethodClient.main()
