from fastapi import FastAPI

from .api.routers.game import router as game_router
from .api.routers.health import router as health_router

app = FastAPI(title="ChessMind API")
app.include_router(health_router)
app.include_router(game_router)

