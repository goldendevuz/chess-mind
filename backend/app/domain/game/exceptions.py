class GameError(Exception):
    pass


class InvalidMoveError(GameError):
    pass


class GameOverError(GameError):
    pass

