from typing import Literal

from play_launcher_sdk.enums.language import Language

from .banner import Banner
from .base import Base
from .game import Game
from .post import Post
from .social_media import SocialMedia


class Content(Base):
    game: Game
    language: Literal[""] | Language
    banners: list[Banner]
    posts: list[Post]
    social_media_list: list[SocialMedia]
