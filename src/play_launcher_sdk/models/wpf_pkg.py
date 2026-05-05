from pydantic import ByteSize

from play_launcher_sdk.types_ import FourPartVersion
from play_launcher_sdk.types_ import HexMd5
from play_launcher_sdk.types_ import ZipUrl

from .base import Base


class WpfPkg(Base):
    version: FourPartVersion
    url: ZipUrl
    md5: HexMd5
    size: ByteSize
