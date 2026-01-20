from .base import Base
from .game import Game
from .wpf_pkg import WpfPkg


class WpfPackage(Base):
    game: Game
    wpf_package: WpfPkg
