from typing import Literal

from pydantic_extra_types.semantic_version import SemanticVersion

from play_launcher_sdk.types import EmptyList

from .base import Base
from .category import Category


class BranchPreDownload(Base):
    package_id: str
    branch: Literal["predownload"]
    password: str
    tag: SemanticVersion
    diff_tags: EmptyList
    categories: list[Category]
    required_client_version: Literal[""]
