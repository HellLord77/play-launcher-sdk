from typing import Literal

from play_launcher_sdk.types import EmptyList

from .base import Base


class PreDownload(Base):
    major: None
    patches: EmptyList
    required_client_version: Literal[""]
