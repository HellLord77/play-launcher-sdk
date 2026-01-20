from play_launcher_sdk.enums.game_biz import GameBiz

from .base import Base


class Game(Base):
    id: str
    biz: GameBiz
