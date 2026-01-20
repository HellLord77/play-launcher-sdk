from typing import Literal

from play_launcher_sdk.enums.game_biz import GameBiz

from .base import Base
from .game_display import GameDisplay
from .game_server_config import GameServerConfig


class GameStatus(Base):
    id: str
    biz: GameBiz
    display: GameDisplay
    reservation: None
    display_status: Literal["LAUNCHER_GAME_DISPLAY_STATUS_AVAILABLE"]
    game_server_configs: list[GameServerConfig]
