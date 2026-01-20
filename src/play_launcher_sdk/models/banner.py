from typing import Literal

from .base import Base
from .image import Image


class Banner(Base):
    id: str
    image: Image
    i18n_identifier: Literal[""]
