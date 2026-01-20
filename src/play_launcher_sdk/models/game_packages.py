from .base import Base
from .game_package import GamePackage


class GamePackages(Base):
    game_packages: list[GamePackage]
