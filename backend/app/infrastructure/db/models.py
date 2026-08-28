from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class GameModel(Base):
    __tablename__ = "games"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    fen: Mapped[str] = mapped_column(String)

