from typing import Literal

from play_launcher_sdk.types import EmptyList

from .base import Base


class Category(Base):
    category_id: int
    matching_field: str
    type: Literal["CATEGORY_TYPE_UNSPECIFIED"]
    scenarios: EmptyList
