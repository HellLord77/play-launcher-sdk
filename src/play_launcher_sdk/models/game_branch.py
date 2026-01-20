from .base import Base
from .branch import Branch
from .game import Game


class GameBranch(Base):
    game: Game
    main: Branch
    pre_download: None
