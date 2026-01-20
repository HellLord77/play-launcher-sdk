from pydantic import ByteSize

from play_launcher_sdk.types import HexMd5
from play_launcher_sdk.types import SplitArchiveUrl

from .base import Base


class GamePkg(Base):
    url: SplitArchiveUrl
    md5: HexMd5
    size: ByteSize
    decompressed_size: ByteSize
