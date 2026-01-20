from .base import Base
from .game_info import GameInfo


class AllGameBasicInfo(Base):
    game_info_list: list[GameInfo]
