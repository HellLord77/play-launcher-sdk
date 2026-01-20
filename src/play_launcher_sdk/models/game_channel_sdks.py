from .base import Base
from .game_channel_sdk import GameChannelSdk


class GameChannelSdks(Base):
    game_channel_sdks: list[GameChannelSdk]
