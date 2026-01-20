from .base import Base
from .game_plugin import GamePlugin


class GamePlugins(Base):
    plugin_releases: list[GamePlugin]
