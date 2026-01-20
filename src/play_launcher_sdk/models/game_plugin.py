from .base import Base
from .game import Game
from .plugin import Plugin


class GamePlugin(Base):
    game: Game
    plugins: list[Plugin]
