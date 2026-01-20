from typing import Literal

from .base import Base
from .game import Game
from .icon import Icon
from .image import Image


class MessageInfo(Base):
    title: str
    content: str
    content_image: Image
    header_icon: Icon
    jump_type: Literal["NOTIFICATION_JUMP_TYPE_GAME_DETAIL"]
    game: Game
    jump_url: Literal[""]
    msg_tmpl: Literal["NOTIFICATION_MSG_TMPL_STRENGTHEN"]
