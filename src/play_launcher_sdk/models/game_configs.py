from .base import Base
from .launch_config import LaunchConfig


class GameConfigs(Base):
    launch_configs: list[LaunchConfig]
