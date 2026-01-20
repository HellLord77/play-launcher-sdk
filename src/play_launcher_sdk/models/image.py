from typing import Literal

from pydantic import HttpUrl

from play_launcher_sdk.types import ImageUrl

from .base import Base


class Image(Base):
    url: Literal[""] | ImageUrl
    link: Literal[""] | HttpUrl
    login_state_in_link: bool
