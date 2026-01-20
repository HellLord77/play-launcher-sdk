from play_launcher_sdk.enums.language import Language

from .base import Base
from .icon import Icon
from .image import Image


class GameDisplay(Base):
    language: Language
    name: str
    icon: Icon
    title: str
    subtitle: str
    background: Image | None
    logo: Image | None
    thumbnail: Image | None
    korea_rating: None
    shortcut: Icon
    wpf_icon: Icon | None = None
