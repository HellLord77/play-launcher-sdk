from typing import Literal

from .base import Base
from .branch import Branch
from .branch_pre_download import BranchPreDownload
from .game import Game


class GameBranch(Base):
    game: Game
    main: Branch
    pre_download: BranchPreDownload | None
    enable_base_pkg_predownload: Literal[False]
