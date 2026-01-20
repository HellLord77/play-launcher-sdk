from typing import Literal

from pydantic import HttpUrl
from pydantic_extra_types.semantic_version import SemanticVersion

from .audio_pkg import AudioPkg
from .base import Base
from .game_pkg import GamePkg


class Pkg(Base):
    version: SemanticVersion
    game_pkgs: list[GamePkg]
    audio_pkgs: list[AudioPkg]
    res_list_url: Literal[""] | HttpUrl
