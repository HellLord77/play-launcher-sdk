from .base import Base
from .game_status import GameStatus


class Games(Base):
    games: list[GameStatus]
