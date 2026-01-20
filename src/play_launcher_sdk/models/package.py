from typing import Literal

from .base import Base
from .pkg import Pkg


class Package(Base):
    major: Pkg
    patches: list[Pkg]
    required_client_version: Literal[""]
