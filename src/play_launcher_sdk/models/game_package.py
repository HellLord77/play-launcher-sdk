from .base import Base
from .game import Game
from .package import Package
from .pre_download import PreDownload


class GamePackage(Base):
    game: Game
    main: Package
    pre_download: PreDownload
