from .background import Background
from .base import Base
from .game import Game


class GameInfo(Base):
    game: Game
    backgrounds: list[Background]
