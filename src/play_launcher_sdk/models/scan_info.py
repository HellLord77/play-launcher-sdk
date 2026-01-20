from .base import Base
from .game_exe import GameExe


class ScanInfo(Base):
    game_id: str
    game_exe_list: list[GameExe]
