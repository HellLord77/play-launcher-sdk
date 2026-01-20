from .base import Base
from .export_file import ExportFile


class GameLogExportConfig(Base):
    file_size_filter: int
    export_timeout: int
    export_files: list[ExportFile]
