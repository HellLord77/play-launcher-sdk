from .base import Base
from .game_branch import GameBranch


class GameBranches(Base):
    game_branches: list[GameBranch]
