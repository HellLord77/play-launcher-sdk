from .base import Base
from .scan_info import ScanInfo


class GameScanInfo(Base):
    game_scan_info: list[ScanInfo]
