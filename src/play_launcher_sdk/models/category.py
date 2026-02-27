from play_launcher_sdk.enums.category_type import CategoryType
from play_launcher_sdk.types import ScenarioList

from .base import Base


class Category(Base):
    category_id: int
    matching_field: str
    type: CategoryType
    scenarios: ScenarioList
