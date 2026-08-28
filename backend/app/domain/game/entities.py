from dataclasses import dataclass, field

import chess

from .events import GameEnded, MoveMade
from .exceptions import GameOverError, InvalidMoveError


@dataclass
class Game:
    id: str
    board: chess.Board = field(default_factory=chess.Board)
    moves: list[str] = field(default_factory=list)
    events: list[object] = field(default_factory=list)

    def make_move(self, uci: str) -> None:
        if self.board.is_game_over():
            raise GameOverError("Game is already over")
        try:
            move = self.board.parse_uci(uci)
        except ValueError as exc:
            raise InvalidMoveError(str(exc)) from exc
        if move not in self.board.legal_moves:
            raise InvalidMoveError("Illegal move")
        self.board.push(move)
        self.moves.append(uci)
        self.events.append(MoveMade(self.id, uci))
        if self.board.is_game_over():
            self.events.append(GameEnded(self.id, self.board.result(claim_draw=True)))

    @property
    def fen(self) -> str:
        return self.board.fen()

