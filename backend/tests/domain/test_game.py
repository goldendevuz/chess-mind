import pytest

from app.domain.game.entities import Game
from app.domain.game.exceptions import InvalidMoveError


def test_game_make_move_updates_board_and_events() -> None:
    game = Game(id="g1")
    game.make_move("e2e4")

    assert game.moves == ["e2e4"]
    assert game.fen.startswith("rnbqkbnr/pppppppp")
    assert len(game.events) == 1


def test_game_rejects_illegal_move() -> None:
    game = Game(id="g1")
    with pytest.raises(InvalidMoveError):
        game.make_move("e2e5")

