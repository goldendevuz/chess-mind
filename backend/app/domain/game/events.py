from dataclasses import dataclass


@dataclass(frozen=True)
class MoveMade:
    game_id: str
    uci: str


@dataclass(frozen=True)
class GameEnded:
    game_id: str
    result: str

