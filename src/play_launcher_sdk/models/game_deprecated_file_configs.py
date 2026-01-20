from .base import Base
from .deprecated_file_config import DeprecatedFileConfig


class GameDeprecatedFileConfigs(Base):
    deprecated_file_configs: list[DeprecatedFileConfig]
