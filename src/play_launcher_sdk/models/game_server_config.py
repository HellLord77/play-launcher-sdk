from typing import Literal

from .base import Base


class GameServerConfig(Base):
    i18n_name: str
    i18n_description: str
    package_name: str
    auto_scan_registry_key: str
    package_detection_info: str
    game_id: str
    reservation: None
    display_status: Literal["LAUNCHER_GAME_DISPLAY_STATUS_AVAILABLE"]
