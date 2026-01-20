from play_launcher_sdk.enums.export_file_type import ExportFileType
from play_launcher_sdk.enums.export_method import ExportMethod
from play_launcher_sdk.types import ExpandablePath

from .base import Base


class ExportFile(Base):
    file_type: ExportFileType
    method: ExportMethod
    path: ExpandablePath
