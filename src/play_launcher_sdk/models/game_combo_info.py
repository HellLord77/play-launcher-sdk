from .base import Base
from .deprecated_file_config import DeprecatedFileConfig
from .game_branch import GameBranch
from .game_channel_sdk import GameChannelSdk
from .game_package import GamePackage
from .launch_config import LaunchConfig


class GameComboInfo(Base):
    launch_configs: list[LaunchConfig]
    game_branches: list[GameBranch]
    game_packages: list[GamePackage]
    game_channel_sdks: list[GameChannelSdk]
    deprecated_file_configs: list[DeprecatedFileConfig]
