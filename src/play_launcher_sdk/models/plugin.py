from pydantic_extra_types.semantic_version import SemanticVersion

from .base import Base
from .plugin_pkg import PluginPkg


class Plugin(Base):
    plugin_id: str
    release_id: str
    version: SemanticVersion
    plugin_pkg: PluginPkg
