from fastapi import APIRouter, WebSocket

from ...application.game.create_game import create_game
from ...application.game.make_move import make_move
from ..schemas import GameResponse, MoveRequest

router = APIRouter(prefix="/games", tags=["games"])
games: dict[str, object] = {}


@router.post("/{game_id}", response_model=GameResponse)
async def new_game(game_id: str) -> GameResponse:
    game = create_game(game_id)
    games[game_id] = game
    return GameResponse(id=game.id, fen=game.fen, moves=game.moves)


@router.post("/{game_id}/move", response_model=GameResponse)
async def move(game_id: str, request: MoveRequest) -> GameResponse:
    game = games[game_id]
    make_move(game, request.uci)
    return GameResponse(id=game.id, fen=game.fen, moves=game.moves)


@router.websocket("/{game_id}/ws")
async def game_ws(websocket: WebSocket, game_id: str) -> None:
    await websocket.accept()
    game = games.get(game_id) or create_game(game_id)
    games[game_id] = game
    while True:
        data = await websocket.receive_text()
        make_move(game, data)
        await websocket.send_json({"id": game.id, "fen": game.fen, "moves": game.moves})

