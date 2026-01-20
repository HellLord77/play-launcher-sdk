from typing import Literal

from pydantic_extra_types.semantic_version import SemanticVersion

from .base import Base
from .category import Category


class Branch(Base):
    package_id: str
    branch: Literal["main"]
    password: str
    tag: SemanticVersion
    diff_tags: list[SemanticVersion]
    categories: list[Category]
    required_client_version: Literal[""]
