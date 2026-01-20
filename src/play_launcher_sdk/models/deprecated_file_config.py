from .base import Base
from .deprecated_file import DeprecatedFile
from .game import Game


class DeprecatedFileConfig(Base):
    game: Game
    deprecated_files: list[DeprecatedFile]
