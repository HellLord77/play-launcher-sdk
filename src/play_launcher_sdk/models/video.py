from typing import Literal

from play_launcher_sdk.types_ import WebmUrl

from .base import Base


class Video(Base):
    url: Literal[""] | WebmUrl
    size: Literal[0]
