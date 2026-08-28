from ...domain.game.entities import Game


def make_move(game: Game, uci: str) -> Game:
    game.make_move(uci)
    return game

