from typing import Literal

from play_launcher_sdk.types import EmptyList

from .base import Base
from .pkg import Pkg


class PackagePreDownload(Base):
    major: Pkg | None
    patches: EmptyList
    required_client_version: Literal[""]
