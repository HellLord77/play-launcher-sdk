from typing import Literal

from pydantic import HttpUrl

from .base import Base


class Link(Base):
    title: str
    link: HttpUrl
    login_state_in_link: Literal[False]
