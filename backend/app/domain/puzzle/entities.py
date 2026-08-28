from dataclasses import dataclass


@dataclass
class Puzzle:
    id: str
    fen: str
    best_move: str

