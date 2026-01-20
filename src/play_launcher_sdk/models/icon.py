from typing import Literal

from pydantic import ByteSize
from pydantic import HttpUrl

from play_launcher_sdk.types import HexMd5
from play_launcher_sdk.types import IconUrl
from play_launcher_sdk.types import PngUrl

from .base import Base


class Icon(Base):
    url: Literal[""] | IconUrl
    hover_url: Literal[""] | PngUrl
    link: Literal[""] | HttpUrl
    login_state_in_link: bool
    md5: Literal[""] | HexMd5
    size: ByteSize
