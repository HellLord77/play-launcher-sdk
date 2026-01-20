from play_launcher_sdk.enums.background_type import BackgroundType

from .base import Base
from .icon import Icon
from .image import Image
from .video import Video


class Background(Base):
    id: str
    background: Image
    icon: Icon
    video: Video
    theme: Image
    type: BackgroundType
