from factory_method.factory.ChessBoard import ChessBoard

class FactoryMethodClient:
    @staticmethod
    def main():
        chess_players = ["Ana", "Pedro"]
        chess_board = ChessBoard(chess_players)
        chess_board.initialize()


if __name__== "__main__":
    FactoryMethodClient.main()
