from pydantic import ByteSize
from pydantic import Json

from play_launcher_sdk.types import Command
from play_launcher_sdk.types import HexMd5
from play_launcher_sdk.types import ZipUrl

from .base import Base
from .validation import Validation


class PluginPkg(Base):
    url: ZipUrl
    md5: HexMd5
    size: ByteSize
    decompressed_size: ByteSize
    command: Command
    validation: Json[list[Validation]]
