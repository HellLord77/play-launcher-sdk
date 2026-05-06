from typing import Literal

from play_launcher_sdk.types_ import FourPartVersion

from .base import Base
from .pkg import Pkg


class Package(Base):
    major: Pkg
    patches: list[Pkg]
    required_client_version: Literal[""] | FourPartVersion
