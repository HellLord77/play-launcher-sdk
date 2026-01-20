from pydantic import ByteSize

from play_launcher_sdk.enums.language import Language
from play_launcher_sdk.types import ArchiveUrl
from play_launcher_sdk.types import HexMd5

from .base import Base


class AudioPkg(Base):
    language: Language
    url: ArchiveUrl
    md5: HexMd5
    size: ByteSize
    decompressed_size: ByteSize
