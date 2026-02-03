from .base import Base
from .game import Game
from .package import Package
from .package_pre_download import PackagePreDownload


class GamePackage(Base):
    game: Game
    main: Package
    pre_download: PackagePreDownload
