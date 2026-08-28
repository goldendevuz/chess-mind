from dataclasses import dataclass


@dataclass(frozen=True)
class Square:
    value: str


@dataclass(frozen=True)
class PieceColor:
    value: str

