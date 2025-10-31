import pytest

from factory_method.factory.ChessBoard import ChessBoard
from factory_method.factory.SolitaireBoard import SolitaireBoard
from factory_method.products.ChessGame import ChessGame
from factory_method.products.SolitaireGame import SolitaireGame

def test_chessboard_create_game() -> None:
    """
    Ensure ChessBoard creates a ChessGame instance correctly
    with the specified players and time per player.
    """
    players: list[str] = ["Alice", "Bob"]
    chess_board = ChessBoard(players=players, time_per_player=15)
    chess_board.initialize()
    game = chess_board.get_game()

    assert isinstance(game, ChessGame)
    assert game.player_one == "Alice"
    assert game.player_two == "Bob"
    assert game.time_per_player == 15

def test_chessboard_default_game() -> None:
    """
    Ensure ChessBoard creates a ChessGame instance with default player names
    when no players are provided, by setting default players before initialization.
    """
    chess_board = ChessBoard()
    chess_board.set_players(["White", "Black"])  # Set default players
    chess_board.initialize()
    game = chess_board.get_game()

    assert isinstance(game, ChessGame)
    assert game.player_one == "White"
    assert game.player_two == "Black"

def test_solitaireboard_create_game() -> None:
    """
    Ensure SolitaireBoard creates a SolitaireGame instance correctly
    for the first available player.
    """
    players: list[str] = ["Charlie"]
    solitaire_board = SolitaireBoard(players=players, difficulty="hard", max_moves=500)
    solitaire_board.initialize()
    game = solitaire_board.get_game()

    assert isinstance(game, SolitaireGame)
    assert game.player == "Charlie"

def test_solitaireboard_default_game() -> None:
    """
    Ensure SolitaireBoard creates a SolitaireGame instance with default player
    when no players are provided, by setting a default player before initialization.
    """
    solitaire_board = SolitaireBoard()
    solitaire_board.set_players(["Player"])  # Set default player
    solitaire_board.initialize()
    game = solitaire_board.get_game()

    assert isinstance(game, SolitaireGame)
    assert game.player == "Player"
