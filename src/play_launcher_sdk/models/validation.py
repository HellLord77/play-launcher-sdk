from pydantic import ByteSize

from play_launcher_sdk.types_ import HexMd5
from play_launcher_sdk.types_ import RelativePath

from .base import Base


class Validation(Base):
    path: RelativePath
    md5: HexMd5
    size: ByteSize | None = None
