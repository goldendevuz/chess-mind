from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "ChessMind API"
    database_url: str = "postgresql+asyncpg://postgres:postgres@postgres:5432/chessmind"
    redis_url: str = "redis://redis:6379/0"
    jwt_secret: str = "change-me"


settings = Settings()

