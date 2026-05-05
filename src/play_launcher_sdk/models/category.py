from play_launcher_sdk.enums.category_scenario import CategoryScenario
from play_launcher_sdk.enums.category_type import CategoryType

from .base import Base


class Category(Base):
    category_id: int
    matching_field: str
    type: CategoryType
    scenarios: list[CategoryScenario]
