from pydantic import ByteSize

from play_launcher_sdk.types import HexMd5
from play_launcher_sdk.types import ZipUrl

from .base import Base


class SdkPkg(Base):
    url: ZipUrl
    md5: HexMd5
    size: ByteSize
    decompressed_size: ByteSize
