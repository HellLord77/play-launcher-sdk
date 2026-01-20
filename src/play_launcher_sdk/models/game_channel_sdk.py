from typing import Literal

from pydantic_extra_types.semantic_version import SemanticVersion

from .base import Base
from .game import Game
from .sdk_pkg import SdkPkg


class GameChannelSdk(Base):
    game: Game
    version: SemanticVersion
    channel_sdk_pkg: SdkPkg
    pkg_version_file_name: Literal["sdk_pkg_version"]
