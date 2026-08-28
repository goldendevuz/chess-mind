from ...domain.game.entities import Game
from .models import GameModel


class GameRepository:
    def to_model(self, game: Game) -> GameModel:
        return GameModel(id=game.id, fen=game.fen)

