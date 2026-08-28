from pydantic import BaseModel


class MoveRequest(BaseModel):
    uci: str


class GameResponse(BaseModel):
    id: str
    fen: str
    moves: list[str]

