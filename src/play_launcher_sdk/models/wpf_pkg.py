from pydantic import ByteSize

from play_launcher_sdk.types import HexMd5
from play_launcher_sdk.types import MetadataVersion
from play_launcher_sdk.types import ZipUrl

from .base import Base


class WpfPkg(Base):
    version: MetadataVersion
    url: ZipUrl
    md5: HexMd5
    size: ByteSize
