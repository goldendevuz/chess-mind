from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api.routers.game import router as game_router
from .api.routers.health import router as health_router

app = FastAPI(title="ChessMind API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(health_router)
app.include_router(game_router)
