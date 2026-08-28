from ...domain.game.entities import Game


def create_game(game_id: str) -> Game:
    return Game(id=game_id)

