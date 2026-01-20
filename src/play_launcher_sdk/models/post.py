from typing import Literal

from pydantic import HttpUrl

from play_launcher_sdk.enums.post_type import PostType
from play_launcher_sdk.types import Date

from .base import Base


class Post(Base):
    id: str
    type: PostType
    title: str
    link: HttpUrl
    date: Date
    login_state_in_link: bool
    i18n_identifier: Literal[""]
