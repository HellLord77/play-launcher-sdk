from typing import Literal

from play_launcher_sdk.types import ExeFileName
from play_launcher_sdk.types import ExpandablePath
from play_launcher_sdk.types import FileName
from play_launcher_sdk.types import RelativeExePath
from play_launcher_sdk.types import RelativeJsonPath
from play_launcher_sdk.types import RelativePath
from play_launcher_sdk.types import RelativeTxtPath

from .base import Base
from .game import Game
from .game_log_export_config import GameLogExportConfig


class LaunchConfig(Base):
    game: Game
    exe_file_name: ExeFileName
    installation_dir: FileName
    audio_pkg_scan_dir: Literal[""] | RelativePath
    audio_pkg_res_dir: Literal[""] | RelativePath
    audio_pkg_cache_dir: Literal[""] | RelativePath
    game_cached_res_dir: Literal[""] | RelativePath
    game_screenshot_dir: RelativePath
    game_log_gen_dir: Literal[""] | ExpandablePath
    game_crash_file_gen_dir: ExpandablePath
    default_download_mode: Literal["DOWNLOAD_MODE_CHUNK"]
    enable_customer_service: bool
    local_res_dir: Literal[""] | RelativePath
    local_res_cache_dir: Literal[""] | RelativePath
    res_category_dir: Literal[""] | RelativePath
    game_res_cut_dir: Literal[""] | FileName
    enable_game_log_export: bool
    game_log_export_config: GameLogExportConfig | None
    blacklist_dir: Literal[""] | RelativeJsonPath
    wpf_exe_dir: Literal[""] | RelativeExePath
    wpf_pkg_version_dir: Literal[""] | FileName
    enable_audio_pkg_mgmt: bool
    audio_pkg_config_dir: Literal[""] | RelativeTxtPath
    enable_resource_deletion_adapter: bool
    enable_resource_blacklist: bool
    enable_redundant_file_cleanup: bool
    redundant_file_cleanup_paths: list[RelativePath]
    enable_v2_game_detection: Literal[False]
    related_processes: list[str]
    enable_ldiff: bool
