from .base import Base
from .icon import Icon
from .image import Image
from .link import Link


class SocialMedia(Base):
    id: str
    icon: Icon
    qr_image: Image
    qr_desc: str
    links: list[Link]
    enable_red_dot: bool
    red_dot_content: str
