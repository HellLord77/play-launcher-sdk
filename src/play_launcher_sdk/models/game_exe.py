from pydantic_extra_types.semantic_version import SemanticVersion

from play_launcher_sdk.types import HexMd5

from .base import Base


class GameExe(Base):
    version: SemanticVersion
    md5: HexMd5
